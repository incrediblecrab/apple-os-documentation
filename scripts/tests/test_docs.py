from __future__ import annotations

from contextlib import redirect_stdout
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "docs.py"
SPEC = importlib.util.spec_from_file_location("docs", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
docs = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(docs)

SOURCE = "\n\n*Source: [Apple](https://developer.apple.com/documentation/swiftui)*\n"
PAGE = "# Example\n\n## Overview\n\nA useful original summary.\n" + SOURCE
CUTOFF = "2026-09-08"


class MarkdownTests(unittest.TestCase):
    def test_source_examples_inside_fences_are_ignored(self):
        parsed = docs.analyze_markdown(
            "# Example\n\n```markdown\n# Fake title\n\n"
            "*Source: [Fake](https://example.invalid)*\n```\n" + SOURCE
        )
        self.assertEqual(parsed["sources"], ["https://developer.apple.com/documentation/swiftui"])
        self.assertEqual(parsed["problems"], [])
        self.assertNotIn("fake-title", parsed["anchors"])

    def test_code_containing_list_syntax_is_not_a_joined_list(self):
        parsed = docs.analyze_markdown("# Example\n\n`a- **b**` is literal code.\n")
        self.assertEqual(parsed["problems"], [])

    def test_unclosed_fence_fails(self):
        parsed = docs.analyze_markdown("# Example\n\n```swift\nlet value = 1\n")
        self.assertTrue(any("unclosed" in message for _, message in parsed["problems"]))

    def test_valid_table_and_malformed_table(self):
        valid = docs.analyze_markdown("# Example\n\n| A | B |\n|---|---|\n| one | two |\n")
        malformed = docs.analyze_markdown("# Example\n\n| A | B |\n| one | two |\n")
        self.assertFalse(valid["problems"])
        self.assertTrue(any("table" in message for _, message in malformed["problems"]))

    def test_unicode_and_collision_slugs(self):
        parsed = docs.analyze_markdown(
            "# Example\n\n## Caf\u00e9\n\n## \u4f60\u597d\n\n## A\n\n## A-1\n\n## A\n\n## API(_:in:)\n"
        )
        self.assertEqual(parsed["anchors"], {"example", "caf\u00e9", "\u4f60\u597d", "a", "a-1", "a-2", "api_in"})

    def test_explicit_html_anchor(self):
        parsed = docs.analyze_markdown('# Example\n\n<a id="custom"></a>\n')
        self.assertIn("custom", parsed["anchors"])


class GateExitCodeTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix="apple-docs-fixture-")
        self.root = Path(self.directory.name)
        subprocess.run(["git", "init", "--quiet", str(self.root)], check=True)
        self.page = self.root / "documentation/Example.md"
        self.page.parent.mkdir()
        self.page.write_text(PAGE, encoding="utf-8", newline="\n")
        self.catalog = {
            "schema_version": 1, "as_of": CUTOFF, "owners": {"C1": "UI"},
            "documents": [{
                "id": "example", "path": "documentation/Example.md",
                "title": "Example", "kind": "framework", "owner": "C1",
                "release_status": "shipping",
                "sources": ["https://developer.apple.com/documentation/swiftui"],
                "review": {"scope": "changed-content", "checked_on": CUTOFF},
            }],
            "coverage": [{
                "scope": "technology", "title": "Example",
                "source": "https://developer.apple.com/documentation/swiftui",
                "paths": ["documentation/Example.md"], "disposition": "existing",
            }],
        }
        self.releases = {
            "schema_version": 1, "as_of": CUTOFF,
            "releases": [{
                "product": "iOS", "version": "26.6.2", "status": "shipping",
                "released_on": CUTOFF, "checked_on": CUTOFF,
                "source": "https://developer.apple.com/news/releases/",
            }],
        }
        docs.write_json(self.root / "metadata/catalog.json", self.catalog)
        docs.write_json(self.root / "metadata/releases.json", self.releases)
        docs.write_json(self.root / "metadata/claims.json", {"schema_version": 1, "as_of": CUTOFF, "claims": []})
        docs.write_json(self.root / "metadata/assets.json", {"schema_version": 1, "as_of": CUTOFF, "assets": []})
        self.accuracy = {
            "schema_version": 1, "as_of": CUTOFF, "complete": True,
            "recorded_at": CUTOFF + "T12:00:00+00:00",
            "method": "Synthetic fixture, not a factual certification.",
            "limitations": ["No upstream retrieval occurs in this fixture."],
            "pages": [],
        }
        self.record_fixture_review("documentation/Example.md")

    def record_fixture_review(self, path):
        content = (self.root / path).read_bytes()
        tokens = docs.PARSER.parse(content.decode("utf-8"))
        self.accuracy["pages"].append({
            "path": path, "as_of": CUTOFF, "full_body_reviewed": True, "status": "verified",
            "content_sha256": hashlib.sha256(content).hexdigest(),
            "headings_reviewed": [title for _, title in docs.analyze_markdown(content.decode("utf-8"))["headings"]],
            "sources": [{
                "url": "https://developer.apple.com/documentation/swiftui",
                "retrieval_url": "https://developer.apple.com/documentation/swiftui.md",
                "sha256": "0" * 64, "locator": "Synthetic fixture source.",
            }],
            "code_examples": {
                "fences_reviewed": sum(token.type == "fence" for token in tokens),
                "verification": "Synthetic fixture contains no executable examples.",
            },
            "qualifications": [], "remaining_blockers": [],
        })
        docs.write_json(self.root / "metadata/accuracy.json", self.accuracy)

    def tearDown(self):
        self.directory.cleanup()

    def run_gate(self):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--root", str(self.root), "check", "--skip-generated"],
            capture_output=True, text=True,
        )

    def assert_gate_failure(self, message):
        result = self.run_gate()
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(message, result.stderr)

    def test_clean_fixture_passes(self):
        result = self.run_gate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_review_hashes_survive_crlf_checkout_preferences(self):
        attributes = self.root / ".gitattributes"
        policy = (SCRIPT.parents[1] / ".gitattributes").read_bytes()
        license_path = self.root / "os26-liquid-glass-example/LICENSE.txt"
        license_path.parent.mkdir()
        license_path.write_bytes(b"Original fixture license.\r\n")
        binary = self.root / "fixture.bin"
        binary.write_bytes(b"\x00binary\r\nbytes\n")
        self.accuracy["pages"][0]["sources"].append({
            "path": license_path.relative_to(self.root).as_posix(),
            "sha256": hashlib.sha256(license_path.read_bytes()).hexdigest(),
            "locator": "Synthetic byte-preserved license fixture.",
        })
        docs.write_json(self.root / "metadata/accuracy.json", self.accuracy)
        git = [
            "git", "-C", str(self.root), "-c", "core.autocrlf=true",
            "-c", "core.safecrlf=false", "-c", f"core.attributesfile={os.devnull}",
        ]
        for protected in (True, False):
            with self.subTest(protected=protected), tempfile.TemporaryDirectory(
                prefix="apple-docs-checkout-",
            ) as directory:
                if protected:
                    attributes.write_bytes(policy)
                else:
                    attributes.unlink()
                subprocess.run(git + ["add", "--all"], check=True, capture_output=True)
                checkout = Path(directory)
                subprocess.run(
                    git + ["checkout-index", "--all", f"--prefix={checkout.as_posix()}/"],
                    check=True, capture_output=True,
                )
                subprocess.run(
                    ["git", "init", "--quiet", str(checkout)], check=True, capture_output=True,
                )
                result = subprocess.run(
                    [sys.executable, str(SCRIPT), "--root", str(checkout), "check", "--skip-generated"],
                    capture_output=True, text=True,
                )
                if protected:
                    self.assertEqual(result.returncode, 0, result.stderr)
                    for original in (self.page, license_path, binary):
                        self.assertEqual(
                            original.read_bytes(),
                            (checkout / original.relative_to(self.root)).read_bytes(),
                        )
                else:
                    self.assertIn(b"\r\n", (checkout / "documentation/Example.md").read_bytes())
                    self.assertNotEqual(result.returncode, 0, result.stderr)
                    self.assertIn("content changed since full-body review", result.stderr)

    def test_generated_files_use_lf_with_a_crlf_io_default(self):
        readme = self.root / "README.md"
        readme.write_bytes(
            f"# Fixture\n\n{docs.README_START}\n\n{docs.README_END}\n".encode("utf-8"),
        )
        expected = docs.generated_indexes(self.catalog)
        expected["README.md"] = docs.generated_readme(self.root, self.catalog)
        expected["generated.json"] = json.dumps({"fixture": True}, indent=2) + "\n"
        temporary_file = tempfile.NamedTemporaryFile
        write_text = Path.write_text

        def temporary_with_crlf_default(*args, **kwargs):
            kwargs.setdefault("newline", "\r\n")
            return temporary_file(*args, **kwargs)

        def write_with_crlf_default(path, *args, **kwargs):
            kwargs.setdefault("newline", "\r\n")
            return write_text(path, *args, **kwargs)

        with (
            patch.object(docs.tempfile, "NamedTemporaryFile", temporary_with_crlf_default),
            patch.object(Path, "write_text", write_with_crlf_default),
        ):
            docs.write_json(self.root / "generated.json", {"fixture": True})
            docs.generate(self.root, self.catalog)
        for relative, content in expected.items():
            with self.subTest(path=relative):
                self.assertEqual((self.root / relative).read_bytes(), content.encode("utf-8"))

    def test_generated_indexes_distinguish_initial_and_full_body_reviews(self):
        for scope in docs.REVIEW_SCOPES:
            with self.subTest(scope=scope):
                self.catalog["documents"][0]["review"]["scope"] = scope
                before = json.dumps(self.catalog, sort_keys=True)
                index = docs.generated_indexes(self.catalog)["documentation/README.md"]
                self.assertIn("| Initial review scope |", index)
                self.assertIn("`metadata/accuracy.json`", index)
                self.assertIn(f"| {scope} |", index)
                self.assertEqual(json.dumps(self.catalog, sort_keys=True), before)

    def test_missing_accuracy_manifest_fails(self):
        (self.root / "metadata/accuracy.json").unlink()
        self.assert_gate_failure("accuracy.json")

    def test_missing_page_review_fails(self):
        self.accuracy["pages"] = []
        docs.write_json(self.root / "metadata/accuracy.json", self.accuracy)
        self.assert_gate_failure("missing full-body review")

    def test_factual_body_change_invalidates_review(self):
        self.page.write_text(PAGE.replace("useful", "incorrect"), encoding="utf-8")
        self.assertEqual(docs.check_documents(self.root, self.catalog), [])
        self.assert_gate_failure("content changed since full-body review")

    def test_review_cannot_omit_headings(self):
        self.accuracy["pages"][0]["headings_reviewed"].pop()
        docs.write_json(self.root / "metadata/accuracy.json", self.accuracy)
        self.assert_gate_failure("every current heading")

    def test_review_cannot_omit_code_scope(self):
        self.page.write_text(PAGE + "\n```swift\nlet value = 1\n```\n", encoding="utf-8")
        self.accuracy["pages"][0]["content_sha256"] = hashlib.sha256(self.page.read_bytes()).hexdigest()
        docs.write_json(self.root / "metadata/accuracy.json", self.accuracy)
        self.assert_gate_failure("account for all fences")

    def test_incomplete_audit_fails_even_with_complete_page_rows(self):
        self.accuracy["complete"] = False
        docs.write_json(self.root / "metadata/accuracy.json", self.accuracy)
        self.assert_gate_failure("full-body audit is incomplete")

    def test_each_review_keeps_its_own_cutoff(self):
        self.accuracy["pages"][0]["as_of"] = "2026-09-07"
        docs.write_json(self.root / "metadata/accuracy.json", self.accuracy)
        result = self.run_gate()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(docs.load_json(self.root / "metadata/accuracy.json")["pages"][0]["as_of"], "2026-09-07")
        self.accuracy["pages"][0]["as_of"] = "2026-09-09"
        docs.write_json(self.root / "metadata/accuracy.json", self.accuracy)
        self.assert_gate_failure("its own ISO cutoff")

    def test_incomplete_or_blocked_review_fails(self):
        page = self.accuracy["pages"][0]
        for field, value, message in (
            ("full_body_reviewed", False, "full-body review is not complete"),
            ("status", "blocked", "full-body review is not complete"),
            ("remaining_blockers", ["Unresolved API claim."], "remaining_blockers"),
        ):
            with self.subTest(field=field):
                original = page[field]
                page[field] = value
                docs.write_json(self.root / "metadata/accuracy.json", self.accuracy)
                self.assert_gate_failure(message)
                page[field] = original

    def test_qualified_review_needs_its_qualification(self):
        self.accuracy["pages"][0]["status"] = "verified-qualified"
        docs.write_json(self.root / "metadata/accuracy.json", self.accuracy)
        self.assert_gate_failure("specific qualifications")

    def test_review_needs_evidence(self):
        self.accuracy["pages"][0]["sources"] = []
        docs.write_json(self.root / "metadata/accuracy.json", self.accuracy)
        self.assert_gate_failure("primary or repository evidence")

    def test_evidence_needs_retrieval_hash_and_locator(self):
        source = self.accuracy["pages"][0]["sources"][0]
        for field, value, message in (
            ("retrieval_url", "", "retrieval HTTP(S) URLs"),
            ("sha256", "not-a-hash", "valid raw sha256"),
            ("locator", "", "precise locator"),
        ):
            with self.subTest(field=field):
                original = source[field]
                source[field] = value
                docs.write_json(self.root / "metadata/accuracy.json", self.accuracy)
                self.assert_gate_failure(message)
                source[field] = original

    def test_repository_evidence_must_stay_inside_repository(self):
        self.accuracy["pages"][0]["sources"] = [{
            "path": "../outside.txt", "sha256": "0" * 64, "locator": "Invalid fixture path.",
        }]
        docs.write_json(self.root / "metadata/accuracy.json", self.accuracy)
        self.assert_gate_failure("invalid repository-evidence path")

    def test_repository_evidence_changes_invalidate_review(self):
        evidence = self.root / "implementation.txt"
        evidence.write_text("Original implementation.", encoding="utf-8")
        self.accuracy["pages"][0]["sources"] = [{
            "path": evidence.name, "sha256": hashlib.sha256(evidence.read_bytes()).hexdigest(),
            "locator": "Fixture implementation contract.",
        }]
        docs.write_json(self.root / "metadata/accuracy.json", self.accuracy)
        result = self.run_gate()
        self.assertEqual(result.returncode, 0, result.stderr)
        evidence.write_text("Changed implementation.", encoding="utf-8")
        self.assert_gate_failure("repository evidence changed")

    def test_duplicate_review_fails(self):
        self.record_fixture_review("documentation/Example.md")
        self.assert_gate_failure("duplicate full-body review")

    def test_registration_does_not_create_a_factual_review(self):
        second = self.root / "documentation/Second.md"
        second.write_text(PAGE.replace("# Example", "# Second").replace("swiftui", "foundation"), encoding="utf-8")
        result = subprocess.run(
            [
                sys.executable, str(SCRIPT), "--root", str(self.root), "register",
                "documentation/Second.md", "--owner", "C1", "--kind", "framework",
                "--source", "https://developer.apple.com/documentation/foundation",
            ],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        registered = docs.load_json(self.root / "metadata/catalog.json")["documents"]
        self.assertEqual(next(page for page in registered if page["path"] == "documentation/Second.md")["review"]["scope"], "catalog-only")
        self.assert_gate_failure("documentation/Second.md: missing full-body review")

    def test_missing_source_fails_even_with_a_fenced_source_example(self):
        self.page.write_text(
            "# Example\n\n```markdown\n*Source: [Fake](https://example.invalid)*\n```\n",
            encoding="utf-8",
        )
        self.assert_gate_failure("missing rendered Source")

    def test_dangling_anchor_fails(self):
        self.page.write_text(PAGE + "\n[Missing section](#not-present)\n", encoding="utf-8")
        self.assert_gate_failure("missing anchor")

    def test_joined_items_fail(self):
        self.page.write_text(
            "# Example\n\n- **First** - description.- **Second** - description.\n" + SOURCE,
            encoding="utf-8",
        )
        self.assert_gate_failure("joined list items")

    def test_conflicting_release_fails(self):
        self.releases["releases"].append({**self.releases["releases"][0], "version": "27"})
        docs.write_json(self.root / "metadata/releases.json", self.releases)
        self.assert_gate_failure("conflicting current entries")

    def test_release_missing_review_date_fails(self):
        del self.releases["releases"][0]["checked_on"]
        docs.write_json(self.root / "metadata/releases.json", self.releases)
        self.assert_gate_failure("checked_on is required")

    def test_inconsistent_snapshot_cutoffs_fail(self):
        self.releases["as_of"] = "2026-09-07"
        docs.write_json(self.root / "metadata/releases.json", self.releases)
        self.assert_gate_failure("snapshot cutoff differs")

    def test_invalid_source_snapshot_hash_fails(self):
        self.catalog["source_snapshots"] = [{
            "url": "https://developer.apple.com/documentation/swiftui",
            "retrieved_on": CUTOFF, "sha256": "not-a-hash",
        }]
        docs.write_json(self.root / "metadata/catalog.json", self.catalog)
        self.assert_gate_failure("invalid sha256")

    def test_future_release_cannot_be_verified_before_publication(self):
        self.releases["releases"][0]["checked_on"] = "2026-09-07"
        docs.write_json(self.root / "metadata/releases.json", self.releases)
        self.assert_gate_failure("release was not published by the review date")

    def test_claim_source_dates_remain_distinct_and_valid(self):
        claim = {
            "id": "example", "status": "verified", "claim": "Example.",
            "source": "https://developer.apple.com/documentation/swiftui",
            "locator": "Overview", "checked_on": CUTOFF,
            "affected_paths": ["documentation/Example.md"],
        }
        for field in ("source_published_on", "source_updated_on"):
            for value, error in ((None, None), (CUTOFF, None), ("September 8", "invalid"), ("2026-09-09", "after review")):
                with self.subTest(field=field, value=value):
                    docs.write_json(self.root / "metadata/claims.json", {
                        "schema_version": 1, "as_of": CUTOFF,
                        "claims": [{**claim, field: value}],
                    })
                    if error:
                        self.assert_gate_failure(error)
                    else:
                        result = self.run_gate()
                        self.assertEqual(result.returncode, 0, result.stderr)

    def test_unregistered_page_fails(self):
        (self.root / "documentation/Unregistered.md").write_text(PAGE, encoding="utf-8")
        self.assert_gate_failure("has no catalog entry")

    def test_missing_metadata_collection_does_not_succeed_as_empty(self):
        docs.write_json(self.root / "metadata/releases.json", {"schema_version": 1, "as_of": CUTOFF})
        self.assert_gate_failure("required releases array")

    def test_link_case_is_checked_on_case_insensitive_filesystems(self):
        self.page.write_text(PAGE + "\n[Wrong case](example.md)\n", encoding="utf-8")
        result = self.run_gate()
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue("incorrect case" in result.stderr or "missing local target" in result.stderr)

    def test_unknown_owner_fails(self):
        self.catalog["documents"][0]["owner"] = "missing-owner"
        docs.write_json(self.root / "metadata/catalog.json", self.catalog)
        self.assert_gate_failure("unknown or missing primary owner")

    def test_duplicate_canonical_topic_needs_alias(self):
        second = {**self.catalog["documents"][0], "id": "second", "path": "documentation/Second.md"}
        self.catalog["documents"].append(second)
        (self.root / second["path"]).write_text(PAGE, encoding="utf-8")
        self.record_fixture_review(second["path"])
        docs.write_json(self.root / "metadata/catalog.json", self.catalog)
        self.assert_gate_failure("duplicate canonical topic")
        second["alias_of"] = "documentation/Example.md"
        docs.write_json(self.root / "metadata/catalog.json", self.catalog)
        result = self.run_gate()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_alias_cycle_fails(self):
        self.catalog["documents"][0]["alias_of"] = "documentation/Example.md"
        docs.write_json(self.root / "metadata/catalog.json", self.catalog)
        self.assert_gate_failure("alias cycle")

    def test_generated_drift_is_detected(self):
        (self.root / "README.md").write_text(
            f"# Fixture\n\n{docs.README_START}\n\n{docs.README_END}\n", encoding="utf-8",
        )
        docs.generate(self.root, self.catalog)
        self.assertEqual(docs.generate(self.root, self.catalog, check=True), [])
        (self.root / "documentation/README.md").write_text("# Stale index\n", encoding="utf-8")
        self.assertTrue(docs.generate(self.root, self.catalog, check=True))


class CatalogTests(unittest.TestCase):
    def test_only_the_documented_script_cache_token_is_normalized(self):
        first = b'<p>SDK 26 is required.</p><script src="https://sfss.cdn-apple.com/2.0.0-beta.2/sf-symbol.js?111"></script>'
        next_token = first.replace(b"?111", b"?222")
        changed_rule = next_token.replace(b"SDK 26", b"SDK 27")
        changed_script = next_token.replace(b"/2.0.0-beta.2/", b"/3.0.0/")
        self.assertEqual(docs.comparison_hash(first, "text/html"), docs.comparison_hash(next_token, "text/html"))
        self.assertNotEqual(docs.comparison_hash(first, "text/html"), docs.comparison_hash(changed_rule, "text/html"))
        self.assertNotEqual(docs.comparison_hash(first, "text/html"), docs.comparison_hash(changed_script, "text/html"))
        self.assertNotEqual(docs.comparison_hash(first, "text/plain"), docs.comparison_hash(next_token, "text/plain"))

    def test_duplicate_metadata_keys_fail(self):
        with tempfile.TemporaryDirectory(prefix="apple-metadata-fixture-") as directory:
            path = Path(directory) / "catalog.json"
            path.write_text('{"owner": "C1", "owner": "C2"}', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
                docs.load_json(path)

    def test_absolute_catalog_urls_are_not_prefixed_twice(self):
        payload = {
            "sections": [{"groups": [{"name": "Services", "technologies": [
                {"title": "CareKit", "destination": {"identifier": "carekit"}},
            ]}]}],
            "references": {"carekit": {"url": "https://github.com/carekit"}},
        }
        self.assertEqual(list(docs.technology_entries(payload)), ["https://github.com/carekit"])

    def test_hig_traverses_nested_groups_not_just_first_level(self):
        nested = "https://developer.apple.com/tutorials/data/design/human-interface-guidelines/components.json"
        content = "https://developer.apple.com/tutorials/data/design/human-interface-guidelines/content.json"
        pages = {
            docs.HIG_CATALOG: {
                "topicSections": [{"identifiers": ["components"]}],
                "references": {"components": {"role": "collectionGroup", "url": "/design/human-interface-guidelines/components"}},
            },
            nested: {
                "topicSections": [{"identifiers": ["content"]}],
                "references": {"content": {"role": "collectionGroup", "url": "/design/human-interface-guidelines/content"}},
            },
            content: {
                "topicSections": [{"identifiers": ["charts"]}],
                "references": {"charts": {"kind": "article", "title": "Charts", "url": "/design/human-interface-guidelines/charts"}},
            },
        }
        entries, visited, failures = docs.hig_entries(pages.__getitem__)
        self.assertEqual(len(entries), 1)
        self.assertEqual(len(visited), 3)
        self.assertEqual(failures, [])
        del pages[content]
        entries, visited, failures = docs.hig_entries(pages.__getitem__)
        self.assertEqual(entries, {})
        self.assertEqual(len(failures), 1)

    def test_docc_shell_is_not_success(self):
        title, substantive = docs.source_identity(
            b"<html><head><title>SwiftUI</title></head><body>This page requires JavaScript.</body></html>",
            "text/html",
        )
        self.assertEqual(title, "SwiftUI")
        self.assertFalse(substantive)

    def test_markdown_metadata_and_legal_footer_do_not_count_as_content(self):
        body = (
            '<!-- {"availability": ["iOS 27", "macOS 27"], "title": "Empty topic", '
            '"description": "' + "metadata " * 60 + '"} -->\n\n'
            '# Empty topic\n\n---\n\nCopyright &copy; 2026 Apple Inc. All rights reserved. '
            '[Terms of Use](https://www.apple.com/legal/)\n'
        ).encode()
        title, substantive = docs.source_identity(body, "text/markdown")
        self.assertEqual(title, "Empty topic")
        self.assertFalse(substantive)
        self.assertTrue(docs.source_identity(body + b"\nThis topic has a real explanation.\n", "text/markdown")[1])
        self.assertTrue(docs.source_identity(body + b"\n```swift\nvar count: Int { get }\n```\n", "text/markdown")[1])

    def test_json_breadcrumb_references_are_not_substantive(self):
        body = json.dumps({"metadata": {"title": "Empty"}, "references": {"parent": {"title": "Framework"}}}).encode()
        self.assertFalse(docs.source_identity(body, "application/json")[1])
        with self.assertRaisesRegex(ValueError, "documentation JSON object"):
            docs.source_identity(b'["not a DocC object"]', "application/json")
        with self.assertRaisesRegex(ValueError, "metadata to be an object"):
            docs.source_identity(b'{"metadata": null}', "application/json")
        with self.assertRaisesRegex(ValueError, "title string"):
            docs.source_identity(b'{"metadata": {"title": []}}', "application/json")

    def test_hig_uses_json_before_html(self):
        url = "https://developer.apple.com/design/human-interface-guidelines/materials"
        self.assertEqual(
            docs.source_candidates(url)[0],
            "https://developer.apple.com/tutorials/data/design/human-interface-guidelines/materials.json",
        )

    def test_bounded_source_report_records_unrequested_urls(self):
        with tempfile.TemporaryDirectory(prefix="apple-sources-fixture-") as directory:
            root = Path(directory)
            args = type("Args", (), {
                "catalogs_only": False, "url": None, "offset": 0, "max_urls": 1,
                "output": root / "report.json", "refresh": True,
            })()
            catalog = {
                "source_snapshots": [], "coverage": [],
                "documents": [{"sources": ["https://example.org/one", "https://example.org/two"]}],
            }
            with patch.object(docs, "probe_source", return_value={
                "url": "https://example.org/one", "status": "retrieved",
                "retrieved_on": "2026-09-08T00:00:00+00:00", "sha256": "0" * 64,
            }), redirect_stdout(io.StringIO()):
                result = docs.check_sources(root, catalog, args)
            report = json.loads(args.output.read_text(encoding="utf-8"))
            self.assertEqual(result, 0)
            self.assertEqual(report["not_requested"], 1)
            self.assertFalse(report["complete_for_selected_scope"])
            self.assertIsNone(report["results"][0].get("human_verified_on"))


class ContextLoaderExampleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        directory = tempfile.TemporaryDirectory(prefix="apple-context-example-")
        cls.addClassCleanup(directory.cleanup)
        examples = [
            token.content for token in docs.PARSER.parse(
                (SCRIPT.parent.parent / "bot-instructions.md").read_text(encoding="utf-8")
            )
            if token.type == "fence" and token.info == "python"
        ]
        if len(examples) != 1:
            raise ValueError("Expected one documented Python context-loader example")
        path = Path(directory.name) / "context_loader.py"
        path.write_text(examples[0], encoding="utf-8")
        spec = importlib.util.spec_from_file_location("context_loader_example", path)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        cls.load_context = staticmethod(module.load_context)

    def setUp(self):
        directory = tempfile.TemporaryDirectory(prefix="apple-context-fixture-")
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        (self.root / "metadata").mkdir()
        (self.root / "docs").mkdir()
        self.canonical = {
            "id": "canonical", "path": "docs/canonical.md",
            "review": {"scope": "changed-content"},
            "sources": ["https://developer.apple.com/documentation/swiftui"],
        }
        self.alias = {
            "id": "alias", "path": "docs/alias.md",
            "alias_of": self.canonical["path"],
            "review": {"scope": "retained-legacy"}, "sources": [],
        }
        self.chain = {
            "id": "chain", "path": "docs/chain.md",
            "alias_of": self.alias["path"],
            "review": {"scope": "catalog-only"}, "sources": [],
        }
        (self.root / self.canonical["path"]).write_text("Canonical content.\n", encoding="utf-8")
        (self.root / self.alias["path"]).write_text("Alias navigation.\n", encoding="utf-8")
        (self.root / self.chain["path"]).write_text("Second alias.\n", encoding="utf-8")
        self.write_catalog()

    def write_catalog(self):
        docs.write_json(self.root / "metadata/catalog.json", {
            "documents": [self.canonical, self.alias, self.chain],
        })

    def test_direct_document(self):
        result = self.load_context(self.root, ["canonical"])["canonical"]
        self.assertEqual(result["path"], self.canonical["path"])
        self.assertEqual(result["review"], self.canonical["review"])
        self.assertEqual(result["text"], "Canonical content.\n")

    def test_alias_uses_canonical_body_metadata(self):
        result = self.load_context(self.root, ["alias"])["alias"]
        self.assertEqual(result["path"], self.canonical["path"])
        self.assertEqual(result["review"], self.canonical["review"])
        self.assertEqual(result["sources"], self.canonical["sources"])

    def test_alias_chain_reaches_canonical_body(self):
        result = self.load_context(self.root, ["chain"])["chain"]
        self.assertEqual(result["path"], self.canonical["path"])
        self.assertEqual(result["text"], "Canonical content.\n")

    def test_unknown_id_raises(self):
        with self.assertRaises(KeyError):
            self.load_context(self.root, ["unknown"])

    def test_alias_cycle_raises(self):
        self.alias["alias_of"] = self.chain["path"]
        self.write_catalog()
        with self.assertRaisesRegex(ValueError, "Alias cycle"):
            self.load_context(self.root, ["alias"])


if __name__ == "__main__":
    unittest.main()
