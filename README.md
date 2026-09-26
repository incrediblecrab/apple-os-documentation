# apple-os-documentation

Unofficial, community-maintained Apple platform references, design guidance, and migration playbooks in plain Markdown. The collection preserves OS 26 guidance while covering the current OS 27 generation; it is not an Apple product or a complete mirror of every API.

**Objective:** keep a dated, source-linked Apple platform reference that can be read directly, used as AI context, and checked for drift against recorded metadata.

**Inputs:** Apple developer documentation, Human Interface Guidelines, release notes, design resources, and local evidence records in `metadata/`; maintenance uses Python 3.11 or later and the scripts in `scripts/`.

**Files:**

- [`documentation/`](documentation/README.md): framework, language, tool, and service references
- [`guides/`](guides/README.md): OS 27 migration, App Store readiness, regional distribution, and related checklists
- [`human-interface-guidelines/`](human-interface-guidelines/README.md): indexed Apple HIG articles and retained legacy material
- [`liquid-glass/`](liquid-glass/): Liquid Glass adoption and design notes
- [`metadata/`](metadata/): release, catalog, claim, asset, and accuracy records used by the checks
- [`os27-intro/`](os27-intro/): OS 27 introductory material
- [`os26-intro/`](os26-intro/): retained OS 26 introductory material
- [`os26-liquid-glass-example/`](os26-liquid-glass-example/README.md): Landmarks sample app demonstrating Liquid Glass
- [`figma/`](figma/README.md): design images and provenance notes
- [`scripts/`](scripts/): generation, inventory, and validation tooling
- [`bot-instructions.md`](bot-instructions.md): guidance for using the collection as AI context
- [`CONTRIBUTING.md`](CONTRIBUTING.md): evidence and contribution rules
- [`requirements-dev.txt`](requirements-dev.txt): Python maintenance dependencies

**Try it:** read the Markdown directly, or run `python3 -m venv .venv`, `.venv/bin/python -m pip install -r requirements-dev.txt`, `.venv/bin/python scripts/docs.py generate`, `.venv/bin/python scripts/docs.py check`, and `.venv/bin/python -m unittest discover -s scripts/tests`.

## Start here

| Task | Entry point |
|---|---|
| Plan an OS 27 migration | [Migration and readiness guides](guides/README.md) |
| Compare platform generations | [OS 27](os27-intro/) and [OS 26](os26-intro/) introductions |
| Find a framework, language, tool, or service | [Reference index](documentation/README.md) |
| Design an interaction | [HIG index](human-interface-guidelines/README.md) |
| Adopt Liquid Glass | [Adoption guide](liquid-glass/adopting-liquid-glass.md) |
| Run an example | [Landmarks sample](os26-liquid-glass-example/README.md) |
| Browse design images and their provenance | [Figma-directory assets](figma/README.md) |
| Use the collection as AI context | [Bot instructions](bot-instructions.md) |

## Release snapshot

<!-- BEGIN GENERATED BASELINE -->

**Research cutoff: September 14, 2026.** This is a dated snapshot, not a live latest-version service.

| Product | Version | Status | Release date |
|---|---|---|---|
| iOS | 27.0 (`24A437`) | shipping | [September 14, 2026](https://developer.apple.com/news/releases/) |
| iPadOS | 27.0 (`24A437`) | shipping | [September 14, 2026](https://developer.apple.com/news/releases/) |
| macOS Golden Gate | 27.0 (`26A428`) | shipping | [September 14, 2026](https://developer.apple.com/news/releases/) |
| tvOS | 27.0 (`24J361`) | shipping | [September 14, 2026](https://developer.apple.com/news/releases/) |
| watchOS | 27.0 (`24R364`) | shipping | [September 14, 2026](https://developer.apple.com/news/releases/) |
| visionOS | 27.0 (`24M362`) | shipping | [September 14, 2026](https://developer.apple.com/news/releases/) |
| Xcode | 27 (`27A266a`) | shipping | [September 14, 2026](https://developer.apple.com/news/releases/) |
| Safari | 27.0 (`20625.1.29`) | shipping | [September 14, 2026](https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes) |
| iOS 26 | 26.6.2 (`23G90`) | shipping | [September 8, 2026](https://developer.apple.com/news/releases/) |
| iPadOS 26 | 26.7 (`23H24`) | shipping | [September 9, 2026](https://developer.apple.com/news/releases/) |
| macOS Tahoe | 26.6.2 (`25G83`) | shipping | [August 17, 2026](https://developer.apple.com/news/releases/) |
| tvOS 26 | 26.6 (`23L773`) | shipping | [July 27, 2026](https://developer.apple.com/news/releases/) |
| watchOS 26 | 26.6 (`23U67`) | shipping | [July 27, 2026](https://developer.apple.com/news/releases/) |
| visionOS 26 | 26.6.1 (`23O780`) | shipping | [August 17, 2026](https://developer.apple.com/news/releases/) |
| Xcode 26 | 26.6 (`17F113`) | shipping | [June 25, 2026](https://developer.apple.com/news/releases/) |
| Safari (Sonoma and Sequoia security update) | 26.6.1 | shipping | [August 18, 2026](https://support.apple.com/en-us/100100) |

**Catalog scope:** 405/405 technology entries and 157/157 indexed HIG articles have an explicit local disposition. The repository has 406 reference pages (including aliases), 158 HIG articles (including retained legacy material), and 254 cataloged Figma-directory images. Generated indexes are excluded from page counts. Coverage is not a certification of every API symbol or every sentence.

<!-- END GENERATED BASELINE -->

See [release metadata](metadata/releases.json) for source URLs and builds, and the [coverage catalog](metadata/catalog.json) for individual mappings and review scopes. OS, standalone Safari, Xcode, SDK, compiler, and deployment versions are separate facts.

## Important adoption corrections

- Xcode 27 (`27A266a`) requires an Apple silicon Mac running macOS Tahoe 26.6 or later, not macOS 27. It includes Swift 6.4. The release notes explicitly restrict IDE hosts to Apple silicon while preserving universal-app back-deployment to macOS 12 and later; those are separate constraints. See [Xcode](documentation/Xcode.md) and its [official release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes).
- Check UIKit scene-lifecycle adoption before rebuilding. The current SDK has a launch requirement, not just a new navigation recommendation. iOS/iPadOS apps built with SDK 27 also need a declared launch screen for acceptance once the App Store accepts that SDK. See [UIKit](documentation/UIKit.md) and the [migration checklist](guides/os27-migration.md).
- SiriKit retains legacy support, including most existing Siri interactions. Prefer App Intents for modern integrations without treating legacy support as a universal removal notice. See [SiriKit](documentation/SiriKit.md) and [App Intents migration](guides/app-intents-migration.md).
- Design compatibility is platform- and build-specific. The compatibility key is ignored for the OS 27 build targets explicitly listed by Apple. Linked SDK, runtime OS, and deployment target are not interchangeable. See [Liquid Glass adoption](liquid-glass/adopting-liquid-glass.md).
- Submission and regional rules need their own checks. For iOS, iPadOS, tvOS, watchOS, and visionOS, the SDK 26 upload minimum has applied since April 28, 2026; it does not require a deployment target of 26. Alternative marketplaces, web distribution, and alternative payments have different eligibility rules. See [App Store readiness](guides/app-store-readiness.md) and [regional distribution](guides/regional-distribution.md).

The [claim register](metadata/claims.json) separates supported corrections from unresolved hardware, release-date, and design claims. A missing SDK deadline in a dated source snapshot is not a permanent promise that Apple will never announce one.

## Coverage and confidence

The scope is Apple's top-level technology catalog, the indexed HIG articles, and the existing repository material. Catalog coverage does not mean every sentence was independently reverified or every code fragment was compiled.

Each document has one primary owner and a kind in `metadata/catalog.json`. `catalog-only` means its topic/source mapping was checked; `changed-content` means the recorded revision received a targeted source review. Historical, alias, and retained legacy pages remain discoverable rather than being silently deleted.

The separate [full-body audit record](metadata/accuracy.json) binds page-level outcomes, evidence, qualifications, and code-example scope to exact content hashes and each page's research cutoff. It does not turn an AI-assisted source review into human approval or certify unavailable runtime checks. The local gate detects later edits and missing reviews; it cannot determine whether an attestation is factually true.

Framework minimum availability stays separate from the version introducing an individual API. Services and web technologies do not inherit a blanket Swift or OS SDK requirement. The June 2025 Liquid Glass announcement remains historical.

Use [contributor guidance](CONTRIBUTING.md) for the evidence contract and `scripts/docs.py inventory` for current file and word counts. No tokenizer-derived corpus size is claimed.

## Maintain the collection

Reading the Markdown does not require any tooling. Maintenance uses Python 3.11 or later:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/docs.py generate
.venv/bin/python scripts/docs.py check
.venv/bin/python -m unittest discover -s scripts/tests
```

The local checks cover catalog ownership, sources, Markdown structure, local links and anchors, asset hashes, generated-file drift, and full-body review coverage/staleness. The separate upstream job reports changes and access failures; a successful HTTP response is not factual verification.

For application requirements and destination-specific commands, use the [sample README](os26-liquid-glass-example/README.md), not the documentation toolchain above.

## Attribution and reuse

Apple documentation, trademarks, design resources, and third-party material retain their original rights and terms. New community summaries link to the relevant primary sources; this repository does not grant a blanket license over those sources.

The Landmarks software retains its [Apple sample license](os26-liquid-glass-example/LICENSE.txt). That grant expressly excludes accompanying photographs. The [asset manifest](metadata/assets.json) records unresolved provenance and rights rather than implying permission to reuse images. Check the original terms before redistributing assets.

Report inaccuracies through the [issue tracker](https://github.com/incrediblecrab/apple-os-documentation/issues), including the affected path, exact claim, and primary source.

## License

MIT. See [`LICENSE`](LICENSE).
