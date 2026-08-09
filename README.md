# Apple OS Documentation Repository 🍎

[![Apple Developer](https://img.shields.io/badge/Source-Apple%20Developer-black.svg)](https://developer.apple.com)
[![OS 27](https://img.shields.io/badge/OS%2027-Beta-orange.svg)](#-os-27-generation)
[![OS 26](https://img.shields.io/badge/OS%2026-Shipping-green.svg)](#-os-26-generation)
[![AI Ready](https://img.shields.io/badge/AI%20Ready-~610K%20Tokens-blue.svg)](#-ai--llm-integration)

> **An unofficial, community-maintained mirror of Apple's developer documentation, Human Interface Guidelines, and Liquid Glass design system — structured as plain Markdown for reading, searching, and LLM context.**

**Reviewed 2026-08-09.** Covers the shipping **OS 26** line and the **OS 27** beta generation.

## 🚦 Current Platform State

| | Version | Status | Released |
|---|---|---|---|
| iOS, iPadOS, tvOS, watchOS, visionOS | **26.6** | Shipping | July 27, 2026 |
| macOS Tahoe | **26.6.1** | Shipping | August 6, 2026 |
| Xcode | **26.6** (`17F113`) | Shipping | June 25, 2026 |
| iOS, iPadOS, macOS Golden Gate, tvOS, watchOS, visionOS | **27** | Beta | Public beta July 13, 2026 |
| Xcode | **27** | Beta | Requires macOS 27 |

OS 27 public releases are expected in fall 2026. **Apple has not announced release dates.**

## 🚀 Quick Start

| I want to... | Go to |
|---|---|
| See what's new in OS 27 | [`os27-intro/`](./os27-intro) |
| Reference the shipping OS 26 line | [`os26-intro/`](./os26-intro) |
| Understand Liquid Glass | [`liquid-glass/`](./liquid-glass) |
| Find framework and API docs | [`documentation/`](./documentation) |
| Read design guidelines | [`human-interface-guidelines/`](./human-interface-guidelines) |
| Browse UI component designs | [`figma/`](./figma) |
| Run sample code | [`os26-liquid-glass-example/`](./os26-liquid-glass-example) |
| Use this repo with an AI agent | [`bot-instructions.md`](./bot-instructions.md) |

## 📋 Table of Contents

- [🚦 Current Platform State](#-current-platform-state)
- [🆕 OS 27 Generation](#-os-27-generation)
- [📦 OS 26 Generation](#-os-26-generation)
- [🔥 Liquid Glass Design System](#-liquid-glass-design-system)
- [📚 Documentation Structure](#-documentation-structure)
- [🤖 AI & LLM Integration](#-ai--llm-integration)
- [💻 Sample Application](#-sample-application)
- [🛠️ Getting Started](#️-getting-started)
- [🤝 Contributing](#-contributing)
- [⚖️ Legal & Attribution](#️-legal--attribution)

## 🆕 OS 27 Generation

Announced at WWDC 2026 (June 8, 2026). Currently in developer and public beta.

### Platform Highlights

- **[iOS 27](./os27-intro/iOS.md)** — Rebuilt Siri on Apple Foundation Models, App Intents entity/intent schemas, Photos Spatial Reframing and Extend, Wallet Create a Pass. **Drops no iPhones.**
- **[iPadOS 27](./os27-intro/iPadOS.md)** — Refined windowing, persistent menu bar, Split View and Slide Over unified into the windowing framework, background uploads and exports, Apple Pencil Visual Intelligence. **Drops all A12-class iPads.**
- **[macOS Golden Gate 27](./os27-intro/macOS.md)** — **First Apple-silicon-only macOS.** Drops the final four Intel Macs; last release with full Rosetta 2.
- **[tvOS 27](./os27-intro/tvOS.md)** · **[watchOS 27](./os27-intro/watchOS.md)** · **[visionOS 27](./os27-intro/visionOS.md)**
- **[Developer Program](./os27-intro/Program.md)** — Beta access, SDK requirements, 2026 App Store Review Guidelines and regulatory changes.

### Three Things That Will Break Your Build Plan

1. **Xcode 27 requires macOS 27 Golden Gate on Apple silicon.** Since macOS 27 drops all Intel Macs, adopting the OS 27 SDK means migrating your build machines and CI fleet first. This is the long-lead item.
2. **`UIDesignRequiresCompatibility` is ignored by the OS 27 SDK.** Rebuilding with Xcode 27 opts you fully into Liquid Glass with no supported override. The appearance is gated on the **linked SDK**, not the running OS — so an app built against the OS 26 SDK keeps its current look on OS 27 until you recompile.
3. **SiriKit is deprecated.** Migrate to App Intents. SiriKit-based intents are not recognized by the new Siri.

### Toolchain

**Swift 6.4** ships with Xcode 27:

| Feature | What it does |
|---|---|
| `@available(anyAppleOS 27, *)` | One availability spelling across all Apple platforms |
| `@diagnose` | Author custom compile-time diagnostics |
| `weak let` | Immutable weak references |
| `~Sendable` | Explicitly opt out of `Sendable` inference |
| `@C` | Improved C interoperability declarations |
| Task Cancellation Shield | Protect critical sections from mid-flight cancellation |

### New Frameworks

- **[Evaluations](./documentation/Evaluations.md)** — validate AI feature behavior beyond unit tests
- **[Core AI](./documentation/CoreAI.md)** — intelligence infrastructure *(details still limited; see the file for hedged status)*
- **[Foundation Models](./documentation/FoundationModels.md)** — generalized `LanguageModel` protocol supporting Apple's on-device model and third-party providers

### SDK Submission Requirement

App Store Connect uploads have required the **OS 26 SDK or later since April 28, 2026**.

**No Xcode 27 / OS 27 SDK deadline has been announced.** Apple has historically set this requirement in the spring following a release, but no date is published. Track [Upcoming Requirements](https://developer.apple.com/news/upcoming-requirements/) rather than planning against an assumed date.

## 📦 OS 26 Generation

The current shipping line, at **26.6** across platforms (macOS Tahoe at 26.6.1). See [`os26-intro/`](./os26-intro) for per-platform guides.

macOS Tahoe 26 is the **final macOS release supporting Intel Macs**. iPadOS 26 is the **terminal release for A12-class iPads**. If you support that hardware, OS 26 is where your users stay.

## 🔥 Liquid Glass Design System

Liquid Glass is Apple's translucent, dynamically refracting interface material, introduced across all platforms in OS 26 and refined in OS 27.

### What Changed in OS 27

- **Stronger content diffusion** beneath glass, improving legibility over busy backgrounds
- **Darkened edge ring** for clearer separation from background content
- **Brighter specular highlights** defining surface boundaries
- **Adaptive toolbars** that become uniform and less translucent as content scrolls beneath
- **Continuous transparency slider** in Settings > Appearance, replacing the OS 26 Clear/Tinted toggle
- **Sidebars** extend to the full window edge with refraction continuing beneath; icons keep their tint
- **Sharper app icons** with better layer separation, authored in Icon Composer 2

**No new named Liquid Glass API types were introduced in OS 27.** Existing code continues to work.

### The Real API

There is **no `LiquidGlass` module to import**. The material is delivered through SwiftUI, UIKit, and AppKit.

```swift
import SwiftUI

struct ContentView: View {
    @Namespace private var namespace

    var body: some View {
        GlassEffectContainer {
            VStack(spacing: 16) {
                Text("Welcome")
                    .font(.largeTitle)
                    .padding()
                    .glassEffect(.regular, in: .rect(cornerRadius: 20))
                    .glassEffectID("title", in: namespace)

                Button("Get Started") { }
                    .buttonStyle(.glassProminent)
            }
        }
    }
}
```

| Framework | Types and modifiers |
|---|---|
| **SwiftUI** | `glassEffect(_:in:)`, `GlassEffectContainer`, `glassEffectID(_:in:)`, `glassEffectUnion(id:namespace:)`, `buttonStyle(.glass)`, `buttonStyle(.glassProminent)`, `backgroundExtensionEffect()` |
| **UIKit** | `UIGlassEffect`, `UIGlassContainerEffect`, `UIBackgroundExtensionView` |
| **AppKit** | `NSGlassEffectView`, `NSGlassEffectContainerView`, `NSBackgroundExtensionView` |

Standard controls — tab bars, navigation bars, sheets, alerts, toolbars — adopt Liquid Glass automatically when you recompile. Custom blur views and bespoke navigation chrome must be migrated by hand.

👉 Full guidance: [`liquid-glass/adopting-liquid-glass.md`](./liquid-glass/adopting-liquid-glass.md)

## 📚 Documentation Structure

```
apple-os-documentation/
├── os27-intro/                  ← OS 27 beta generation (7 guides)
├── os26-intro/                  ← OS 26 shipping line (7 guides)
├── liquid-glass/                ← Design system (4 documents)
├── documentation/               ← Framework & API references (371 files)
├── human-interface-guidelines/  ← Complete HIG (156 files)
│   ├── components/  foundations/  patterns/
│   ├── technologies/  inputs/  getting-started/
├── figma/                       ← UI component design images (254 files)
├── os26-liquid-glass-example/   ← SwiftUI sample app
└── bot-instructions.md          ← Guidance for AI agents using this repo
```

| Directory | Content | Files | Key topics |
|---|---|---|---|
| `os27-intro` | OS 27 platform overviews | 7 | Beta features, device support, migration |
| `os26-intro` | OS 26 platform overviews | 7 | Shipping line reference |
| `liquid-glass` | Design system | 4 | Principles, adoption, real API names |
| `documentation` | API references | 371 | SwiftUI, UIKit, AppKit, Foundation Models, App Intents |
| `human-interface-guidelines` | Design guidelines | 156 | Components, foundations, patterns, technologies |
| `figma` | UI component designs | 254 images | Liquid Glass components, materials, mockups |
| `os26-liquid-glass-example` | Sample code | Full app | SwiftUI Landmarks implementation |

### Page Conventions

Markdown pages follow a consistent shape so they parse predictably:

- `# Title` → summary → `**Platforms:**` availability line → `## Overview` → `## Topics`
- Version-specific behavior appears in blockquote callouts: `> **iOS 27+, iPadOS 27+, macOS Golden Gate 27+:** …`
- Framework pages end with an SDK baseline footer; HIG pages end with a design baseline footer
- Every page carries a `*Source:*` link back to the official Apple page it mirrors

`**Platforms:**` lines record a framework's **minimum availability** and do not change when a new OS ships.

## 🤖 AI & LLM Integration

Structured plain Markdown, suitable for retrieval, context loading, and evaluation harnesses.

### Token Budget

| Directory | Words | Approx. tokens |
|---|---|---|
| `documentation/` | 229,491 | ~305K |
| `human-interface-guidelines/` | 208,309 | ~277K |
| `os27-intro/` | 6,732 | ~8K |
| `os26-intro/` | 6,580 | ~8K |
| `liquid-glass/` | 5,453 | ~7K |
| **Total (excluding `figma/`)** | **~459,000** | **~610K** |

The full corpus does not fit in most context windows. Load selectively — see [`bot-instructions.md`](./bot-instructions.md) for a loading priority order.

### Accuracy Expectations

This is a community mirror, not an Apple product. When using it as an AI context source:

- **Verify pre-release claims.** OS 27 content describes beta software that may change before release.
- **Prefer the `*Source:*` link** on each page over the mirrored text when correctness matters.
- **Watch for hedged statements.** Pages explicitly mark lower-confidence claims; preserve those hedges in generated output rather than stating them as fact.
- **Do not invent API names.** If a symbol is not in this repo or Apple's documentation, treat it as nonexistent.

### Loading Example

```python
from pathlib import Path

def load_apple_docs(root: Path, sections=("os27-intro", "liquid-glass")):
    """Load selected sections. Loading everything is ~610K tokens."""
    return {
        section: {
            p.name: p.read_text(encoding="utf-8")
            for p in sorted((root / section).rglob("*.md"))
        }
        for section in sections
    }
```

## 💻 Sample Application

**Landmarks** — a SwiftUI app demonstrating Liquid Glass adoption.

```bash
open "os26-liquid-glass-example/Landmarks/Landmarks.xcodeproj"

xcodebuild -project "os26-liquid-glass-example/Landmarks/Landmarks.xcodeproj" \
           -scheme Landmarks build
```

Demonstrates Liquid Glass materials, SwiftUI app lifecycle, state management, navigation, and multi-platform support (iOS 26.0+, iPadOS 26.0+, macOS Tahoe 26.0+).

## 🛠️ Getting Started

### Prerequisites

| Building for | Requires |
|---|---|
| OS 26 (shipping) | Xcode 26 on macOS Tahoe 26 or later |
| OS 27 (beta) | **Xcode 27 on macOS 27 Golden Gate, Apple silicon only** |

App Store Connect uploads require the OS 26 SDK or later, in effect since April 28, 2026.

### Installation

```bash
git clone https://github.com/incrediblecrab/apple-os-documentation.git
cd apple-os-documentation
```

### Searching

```bash
# Find a framework reference
grep -ril "urlsession" documentation/

# Find every OS 27 callout
grep -rn "iOS 27+" human-interface-guidelines/ documentation/

# Find design guidance on a component
grep -ril "navigation" human-interface-guidelines/components/
```

### Common Entry Points

- **SwiftUI**: [`documentation/SwiftUI.md`](./documentation/SwiftUI.md)
- **UIKit**: [`documentation/UIKit.md`](./documentation/UIKit.md)
- **AppKit**: [`documentation/AppKit.md`](./documentation/AppKit.md)
- **App Intents**: [`documentation/AppIntents.md`](./documentation/AppIntents.md)
- **Foundation Models**: [`documentation/FoundationModels.md`](./documentation/FoundationModels.md)
- **Swift**: [`documentation/Swift.md`](./documentation/Swift.md) · **Xcode**: [`documentation/Xcode.md`](./documentation/Xcode.md)

## 🤝 Contributing

Contributions are welcome. Because this repository mirrors Apple's documentation, accuracy matters more than volume.

### Ground Rules

1. **Cite a primary source.** Link to developer.apple.com, Apple Newsroom, or an Apple release note. Rumor aggregators are not sufficient.
2. **Never invent API names.** If you cannot find a symbol in Apple's documentation, do not write it down.
3. **Hedge uncertain claims explicitly.** Use "Apple says", "reported from the WWDC 2026 keynote", or a `> **Note:**` callout. Do not present unverified detail as fact.
4. **Do not print unannounced dates.** In particular, there is no announced OS 27 SDK submission deadline.
5. **Do not modify `**Platforms:**` lines** to reflect a newly shipped OS — they record minimum availability.
6. **Match the existing page shape** and callout style described in [Page Conventions](#page-conventions).

### Workflow

1. Fork the repository
2. Create a feature branch
3. Make your change, following the ground rules above
4. Submit a pull request describing your sources

### Areas That Need Help

- [ ] Verifying OS 27 beta content against final releases when they ship
- [ ] Expanding tvOS 27, watchOS 27, and visionOS 27 coverage as Apple publishes more
- [ ] Additional code examples using verified APIs
- [ ] Correcting any remaining stale OS 26-era statements

## 📊 Repository Stats

- **Markdown files (excluding `figma/`)**: 548
- **Design images in `figma/`**: 254
- **Words**: ~459,000 (~610K tokens)
- **Framework references**: 371
- **HIG pages**: 156
- **Platforms**: iOS, iPadOS, macOS, tvOS, watchOS, visionOS

## 🔗 Related Resources

- [Apple Developer Documentation](https://developer.apple.com/documentation/)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Upcoming Requirements](https://developer.apple.com/news/upcoming-requirements/)
- [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- [Swift.org](https://www.swift.org/)

## ⚖️ Legal & Attribution

### Source Attribution

Content is derived from official Apple Developer resources — Apple Developer Documentation, the Human Interface Guidelines, Apple Newsroom, and official release notes. Each page links back to its source.

### Disclaimer

This is an **unofficial**, community-maintained repository. Apple Inc. does not endorse, maintain, or review this project. Apple, iOS, iPadOS, macOS, tvOS, watchOS, visionOS, Liquid Glass, Xcode, Swift, and related marks are trademarks of Apple Inc. All trademarks and copyrights belong to their respective owners.

Documentation covering pre-release software describes beta builds and may not reflect final shipping behavior. Always verify against Apple's official documentation before relying on it in production.

## 📞 Support & Community

- **🐛 Issues**: [Report a problem or request a topic](https://github.com/incrediblecrab/apple-os-documentation/issues)
- **💬 Discussions**: [Join the discussion](https://github.com/incrediblecrab/apple-os-documentation/discussions)

### Star this repository ⭐ if you find it useful

---

*Last reviewed: 2026-08-09 | Shipping: OS 26.6 (macOS 26.6.1) | Beta: OS 27 | Community maintained*
