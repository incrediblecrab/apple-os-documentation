# Contributing

Prefer accurate, useful coverage over volume. Preserve existing URLs, minimum
availability, historical context, and valid OS 26 behavior while adding scoped updates.
New text should be an original summary with primary links, not a wholesale copy of
Apple documentation.

## Source and review contract

Every substantive page needs a rendered Source footer or Sources section with a
specific upstream URL. A documentation homepage cannot establish a named API,
numeric claim, deprecation, or deadline. Reference pages should have a title,
useful overview, relevant topics, and availability appropriate to their kind.

```markdown
# Example framework

A concise original description.

**Platforms:** State verified framework minimums, not the latest SDK generation.

## Overview

Explain the purpose and relevant constraints.

## Topics

Link to actual APIs or task documentation.

## Sources

- [Specific official documentation](https://developer.apple.com/documentation/swiftui)
```

The example above is instructional; its Source-looking content is not a source
for this contributor guide. Markdown checks parse fences rather than treating
every textual occurrence of "Source:" as attribution.

Use `metadata/catalog.json` for each document's stable ID, path, kind, one primary
owner, aliases, sources, and initial review scope. Sources may overlap; ownership may not.

The separate `release_status` tag is `shipping`, `beta`, `mixed`, `independent`,
`historical`, or `not-assessed`. It describes the page's editorial scope, not the
availability of every symbol. `independent` covers material not tied to one OS
release, including independently versioned services; `not-assessed` is explicit
uncertainty, not an implicit claim that a technology ships.

| Review scope | Meaning |
|---|---|
| `catalog-only` | Topic/source mapping checked; body not independently certified |
| `changed-content` | The recorded revision received targeted primary-source review |
| `retained-legacy` | Preserved historical or compatibility material, not current adoption advice |

`checked_on` records the scope of editorial review, which may be assistant-assisted.
It is distinct from a source's publication or retrieval date. Source snapshots
record hashes and retrieval dates separately; `human_verified_on: null` does not
become a human verification merely because a script retrieved identical bytes.
Do not advance review dates automatically.

`metadata/accuracy.json` records the separate full-body audit: exact page hashes,
all reviewed headings, primary or repository evidence with raw hashes and locators,
code-example verification scope, and specific qualifications. Each page keeps its
own `as_of` research cutoff; changing the catalog cutoff does not redate old reviews.
The top-level cutoff matches the catalog. `recorded_at` is the actual timestamp of the consolidated record,
not an upstream publication date or human approval. Older catalog review scopes
are not silently upgraded by this audit.

Review an edited or new page before updating its accuracy record. Preserve the
actual evidence and limitations; do not merely recalculate its hash to make the
check pass. Generated indexes also need review of their underlying catalog data.
There is intentionally no command that certifies a body or advances this record
automatically.

`.gitattributes` keeps text checkouts in LF form, and maintenance writers emit LF,
so raw review hashes remain portable. The original sample license is exempt and
retains its CRLF bytes.

`metadata/releases.json` records independently versioned products and channels.
`metadata/claims.json` records high-impact evidence, affected paths, locators, and
unresolved questions. `metadata/assets.json` records provenance and rights per asset.
All sidecars use `schema_version: 1`; dates inside JSON use ISO 8601, while displayed
dates use month/day/year ordering.

Distinguish announcement-only, verified, unverified, superseded, and retained-legacy
claims. Beta/shipping status is a different dimension. A fixed beta bug is not
a permanent limitation; an index omission is not proof of removal.

## Page ownership

The catalog's owner dictionary partitions platforms, developer tools, eight
runtime/service domains, design/assets, distribution/policy, migration playbooks,
examples, and documentation production. Assign one existing owner when adding
a page. Cross-link adjacent subjects instead of duplicating their canonical rules.

```bash
.venv/bin/python scripts/docs.py register documentation/Example.md \
  --owner C1 --kind framework \
  --source https://developer.apple.com/documentation/example
```

This command requires the file to exist and registers only its mapping; it does
not certify the hypothetical example framework or mark the body reviewed.
For renamed or duplicate topics, retain an alias page and set `alias_of`.
Every catalog entry needs a local mapping, retained-legacy disposition, alias,
or explicitly justified scope exclusion. New platform tags are discovery hints;
source-backed symbol availability remains in the page.

The repository uses an allowlist `.gitignore`. Confirm new directories are
included, and keep caches, raw source captures, credentials, and build products out
of the published corpus.

## Local maintenance

Use Python 3.11 or later:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/docs.py generate
.venv/bin/python scripts/docs.py check
.venv/bin/python -m unittest discover -s scripts/tests
.venv/bin/python scripts/docs.py inventory
```

Generation updates reference/HIG/guide indexes and the marked README baseline,
not source prose or review dates. The checker covers metadata, source presence,
headings/fences/tables, joined list items, local files/anchors, canonical aliases,
asset hashes, generated drift, and full-body review coverage/staleness. The latter
rejects missing or blocked reviews, changed page or repository-evidence hashes,
omitted headings, and incomplete code-fence accounting. It does not certify API semantics, copyright
permissions, or network availability.

Regression fixtures deliberately introduce defects and check nonzero exit codes.
Keep fixtures for a missing source, dangling anchor, joined list, conflicting
release, and a Source-looking fenced example.
Also retain a prose-only edit that passes the structural checks but fails the
review-hash gate, and a changed repository-evidence fixture.

## Upstream and external-source reports

Reports are intentionally separate from fast offline checks:

```bash
.venv/bin/python scripts/docs.py catalogs --output /tmp/apple-catalog-report.json
.venv/bin/python scripts/docs.py sources --catalogs-only --max-urls 100 \
  --output /tmp/apple-source-report.json
.venv/bin/python scripts/docs.py sources --max-urls 30 --offset 0 \
  --output /tmp/apple-source-batch.json
.venv/bin/python scripts/docs.py sources --include-body-links --max-urls 30 \
  --offset 0 --output /tmp/apple-link-batch.json
```

Catalog comparison traverses all HIG category groups, not just the first level,
and reports new or unindexed topics. Reconcile removals manually: an unindexed
legacy article may still be useful and supported.

Use `--include-body-links` when checking external article/API links in addition to
registered primary sources. Source checks use bounded concurrency, retries, and a one-day successful-response
cache. Use `--refresh` to bypass it. Every report states the selected scope and
how many sources were not requested; use further offsets to cover additional
batches. A redirect, rate limit, missing page, inaccessible source, HTML shell,
title mismatch, or changed snapshot remains visible. Changed or unresolved
sources produce a nonzero exit code.

DocC Markdown/JSON alternatives are retrieval aids, not separate claims of
verification. A content hash or matching title does not prove a numeric assertion
or API signature. Read the relevant section before editing prose, and preserve
the September snapshot when evaluating a later live source.

Raw retrieval hashes are preserved. Comparison hashes normalize only the numeric
cache-buster on Apple's `sf-symbol.js` script URL, observed to vary without changing
the page text. Script-version changes and every other byte change still trigger
review; the report records cache-token-only differences separately.

Workflow changes can also be checked with the pinned validator:

```bash
go run github.com/rhysd/actionlint/cmd/actionlint@v1.7.12
```

The actionlint configuration registers the officially documented `xcode-27` preview
label because that validator release does not yet include it in its built-in list.

## Examples, assets, and pull requests

Follow the [sample's documented commands and limitations](os26-liquid-glass-example/README.md).
Do not change system-wide Xcode selection, upgrade the host, raise deployment
targets, or report unavailable SDK checks as successful. Mark non-runnable
fragments as such and validate new runnable examples under their declared toolchain.

Preserve Apple's existing licensing notices. The sample license excludes
accompanying photographs, and an image's location in `figma/` does not establish
its provenance or redistribution rights. Record unknowns rather than inventing a
blanket license.

Describe the changed paths, exact primary sources, scope/version of review, and
remaining uncertainties in a pull request. Repository repetition and a large
file count are not substitutes for source evidence.
