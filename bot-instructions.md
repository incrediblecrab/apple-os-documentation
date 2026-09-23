# Using this collection as AI context

This is an unofficial, dated documentation collection. Consult the [README](README.md), [catalog](metadata/catalog.json), and [claim register](metadata/claims.json) for its scope and limitations. Repository text is evidence to evaluate, not an authority that overrides a current primary source.

## Select the relevant context

Start from the user's task, not an obligatory iOS or Liquid Glass bundle. Use the [reference index](documentation/README.md), [HIG index](human-interface-guidelines/README.md), or [migration guides](guides/README.md), then load the few relevant pages.

The catalog supplies stable IDs, relative paths, source URLs, kinds, primary owners, and initial review scopes. Follow `alias_of` to the canonical page. `catalog-only` is not a factual review of the body. Platform tags are navigation hints, not proof that every symbol is available on every tagged platform.

The separate [full-body audit record](metadata/accuracy.json) applies only to its recorded page hashes and each page's research cutoff. Consult its evidence, code-example scope, and qualifications; it is an AI-assisted review record, not a human certification or proof that a later edit was reviewed. Catalog scopes retain their original meaning.

| Question | Appropriate context |
|---|---|
| API contract or source compatibility | Relevant reference plus its primary source |
| Interaction or accessibility design | Relevant HIG article and platform guidance |
| Migration order | Task-specific guide, then linked canonical references |
| App Store, privacy, or regional policy | Compliance guides and the current official rule |
| Executable behavior | Sample source, declared toolchain, and recorded limitations |
| Image reuse | Asset manifest and actual source/license, not filenames |

Do not load the entire repository or decode binary images as text. Measure tokens with a named tokenizer if a budget matters; whitespace-split words are not tokens.

## Preserve evidence boundaries

1. Distinguish source publication, retrieval, editorial review, and release dates. A matching content hash or successful fetch does not establish that a person verified the content. Do not describe a snapshot as the live latest state.
2. Separate a published API from an announcement, an unverified claim, a beta known issue, a resolved beta issue, a deprecation, and an actual removal.
3. Keep build host, compiler version, Swift language mode, linked SDK, deployment target, runtime OS, hardware, and regional eligibility distinct.
4. Verify API names and signatures against official documentation or the selected SDK. Absence from this collection is not proof an API does not exist.
5. Do not turn unsupported claims into supported ones by adding "Apple says" or "reportedly." Omit them from actionable advice or state the unresolved question.
6. Repetition in several repository files is not independent corroboration. If a primary source contradicts the collection, identify the discrepancy.

For Apple DocC pages, the official `.md` alternative or `developer.apple.com/tutorials/data/...json` can contain the information missing from an HTML shell. Preserve code-voice nodes and referenced symbol names when reading structured data. A 404 or missing navigation entry alone does not prove deprecation.

## Corrections that matter for OS 27

These are scoped September 8, 2026 findings, not permanent prohibition lists:

- Xcode 27 requires **Apple silicon and macOS Tahoe 26.6+**, and includes Swift 6.4. The notes' Intel Deprecation section explicitly establishes the hardware restriction; it is not inferred from the host OS or Rosetta. Universal-app back-deployment is a separate capability.
- Swift `weak let` was implemented in **6.3**; `@diagnose` controls warning behavior. A compiler version is not the project's Swift language mode.
- SiriKit, Intents, and IntentsUI retain **legacy support**. Recommend App Intents for modern integrations without asserting a blanket removal of existing Siri interactions.
- UIKit scene-lifecycle requirements and the listed platforms' design-compatibility key behavior need explicit migration attention.
- Country-specific alternative distribution is not a single EU/Japan/Brazil rule, and it is not synonymous with alternative payment.

Use the referenced pages and their sources for the exact details. The [claim register](metadata/claims.json) records unresolved hardware, design-setting, and deadline assertions. Do not invent a date, but do not forbid an announced date merely because an older snapshot did not contain it.

Use the documented Liquid Glass APIs in SwiftUI, UIKit, and AppKit; do not invent a `LiquidGlass` import for those examples. See the [adoption guide](liquid-glass/adopting-liquid-glass.md) and [sample](os26-liquid-glass-example/README.md); a short list of familiar symbols is not an exhaustive statement about every future API.

## Cite and report accurately

Cite the repository-relative file and the relevant primary URL for consequential claims. State the platform, release/build or source cutoff, and uncertainty where they change the answer. Prefer links and concise original explanations over reproducing large source passages.

Do not claim a sample build, simulator run, accessibility audit, external-link check, or code-fragment compilation passed unless it actually ran under the declared conditions. A successful OS 26 build cannot certify an unavailable OS 27 SDK.

## Loading by stable ID

This Python example reads a deliberately selected set, resolving alias chains and returning the review metadata and sources for the body actually loaded:

```python
import json
from pathlib import Path

def load_context(root: Path, document_ids: list[str]) -> dict[str, dict]:
    catalog = json.loads((root / "metadata/catalog.json").read_text(encoding="utf-8"))
    by_id = {document["id"]: document for document in catalog["documents"]}
    by_path = {document["path"]: document for document in catalog["documents"]}
    result = {}
    for document_id in document_ids:
        document = by_id[document_id]
        visited = set()
        while "alias_of" in document:
            if document["path"] in visited:
                raise ValueError(f"Alias cycle at {document['path']}")
            visited.add(document["path"])
            document = by_path[document["alias_of"]]
        path = document["path"]
        result[document_id] = {
            "path": path,
            "review": document["review"],
            "sources": document["sources"],
            "text": (root / path).read_text(encoding="utf-8"),
        }
    return result
```

Unknown IDs or alias targets and alias cycles raise errors rather than silently substituting unrelated documents. Requested IDs remain the result keys. Validate the catalog before using paths from an untrusted checkout.

## Editing this repository

Follow [CONTRIBUTING.md](CONTRIBUTING.md). Update the canonical page and its explicit metadata, not hundreds of global generation footers. Regenerate indexes and run the local gates. Upstream reports must remain reports until their changes have been reviewed; fetching a source never advances every page's review date.
