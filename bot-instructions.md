# 🤖 Bot & LLM Instructions for Apple OS Documentation

> **For AI assistants, LLMs, and automated tools consuming this repository.**

**Reviewed 2026-08-09.** This repository documents the shipping **OS 26** line and the **OS 27** beta generation.

## Read This First: Accuracy Rules

This is an unofficial community mirror of Apple's documentation. It contains content about **pre-release software**. If you generate answers from it, these rules matter more than any loading strategy below.

1. **Never invent API names.** If a symbol is not in this repository or Apple's official documentation, treat it as nonexistent. There is **no `LiquidGlass` module**, no `LiquidGlassContainer`, and no `.liquidGlassStyle` modifier. The real API is listed under [Liquid Glass API](#liquid-glass-api-authoritative).
2. **Preserve hedges.** Pages mark lower-confidence claims with `> **Note:**` callouts or phrasing like "Apple says" and "reported from the WWDC 2026 keynote". Carry that uncertainty into your output; do not upgrade a hedged claim into a stated fact.
3. **Distinguish shipping from beta.** OS 26 content describes released software. OS 27 content describes betas that may change. Say which you mean.
4. **Do not state unannounced dates.** There is **no announced OS 27 SDK submission deadline** and no announced OS 27 release date. If asked, say so.
5. **Prefer the `*Source:*` link** at the bottom of each page over the mirrored text when correctness matters.
6. **`**Platforms:**` lines are minimum availability**, not "current OS". A framework marked `iOS 13.0+` still says `iOS 13.0+` after OS 27 ships.

## Current Platform State

Use this when a user asks "what's the latest".

| | Version | Status | Date |
|---|---|---|---|
| iOS, iPadOS, tvOS, watchOS, visionOS | 26.6 | Shipping | 2026-07-27 |
| macOS Tahoe | 26.6.1 | Shipping | 2026-08-06 |
| Xcode | 26.6 (`17F113`) | Shipping | 2026-06-25 |
| All platforms | 27 | Beta | Public beta 2026-07-13 |
| Xcode | 27 | Beta | Requires macOS 27 |

OS 27 public release is expected fall 2026 but **has not been dated by Apple**. Beta numbering diverges across platforms — do not assume parity.

## Token Budget

Total corpus excluding `figma/` is **~610K tokens (~459,000 words)**. Selective loading is mandatory.

| Directory | Files | Words | Approx. tokens | Strategy |
|---|---|---|---|---|
| `documentation/` | 371 | 229,491 | ~305K | Search, then load individual files |
| `human-interface-guidelines/` | 156 | 208,309 | ~277K | Query specific pages only |
| `os27-intro/` | 7 | 6,732 | ~8K | Can load fully |
| `os26-intro/` | 7 | 6,580 | ~8K | Can load fully |
| `liquid-glass/` | 4 | 5,453 | ~7K | Can load fully |
| `figma/` | 254 images | — | — | Reference paths; never load as text |

### Representative File Sizes

| File | Approx. tokens |
|---|---|
| `os27-intro/iOS.md` | ~2,100 |
| `os27-intro/macOS.md` | ~1,500 |
| `liquid-glass/adopting-liquid-glass.md` | ~2,600 |
| `liquid-glass/introduction.md` | ~1,400 |
| `documentation/SwiftUI.md` | ~1,700 |
| `documentation/AppIntents.md` | ~1,700 |
| `documentation/UIKit.md` | ~1,400 |
| `human-interface-guidelines/components/buttons.md` | ~3,800 |

## Priority Loading Order

```yaml
1. CRITICAL — load first for almost any task:
   - os27-intro/iOS.md              # ~2,100 tokens — current generation state
   - liquid-glass/introduction.md   # ~1,400 tokens — design system + real API names

2. HIGH — load when the task touches them:
   - liquid-glass/adopting-liquid-glass.md   # migration, SDK gating, OS 27 changes
   - os27-intro/<platform>.md                # platform-specific features + device support
   - os27-intro/Program.md                   # App Store policy, SDK requirements
   - documentation/SwiftUI.md | UIKit.md | AppKit.md

3. REFERENCE — query-based, never bulk load:
   - documentation/          # ~305K tokens
   - human-interface-guidelines/  # ~277K tokens

4. NON-TEXT:
   - figma/                  # reference by path only
```

## Liquid Glass API (Authoritative)

Use only these names. Everything else is fabrication.

| Framework | Types and modifiers |
|---|---|
| **SwiftUI** | `glassEffect(_:in:)`, `GlassEffectContainer`, `glassEffectID(_:in:)`, `glassEffectUnion(id:namespace:)`, `buttonStyle(.glass)`, `buttonStyle(.glassProminent)`, `backgroundExtensionEffect()` |
| **UIKit** | `UIGlassEffect`, `UIGlassContainerEffect`, `UIBackgroundExtensionView` |
| **AppKit** | `NSGlassEffectView`, `NSGlassEffectContainerView`, `NSBackgroundExtensionView` |

```swift
import SwiftUI

GlassEffectContainer {
    Text("Welcome")
        .padding()
        .glassEffect(.regular, in: .rect(cornerRadius: 20))
}
```

**No new named Liquid Glass API types were introduced in OS 27.** OS 27 changes rendering and user controls, not the API surface.

## OS 27 Facts Bots Get Wrong

These are the highest-frequency errors. Answer them from this table, not from memory.

| Question | Correct answer |
|---|---|
| Can I opt out of Liquid Glass in OS 27? | No. `UIDesignRequiresCompatibility` is **ignored by the OS 27 SDK**. |
| What decides whether my app looks glassy? | The **SDK you link against**, not the OS the device runs. An OS 26-SDK app keeps its old look on OS 27. |
| Can I build with Xcode 27 on my Intel Mac? | No. **Xcode 27 requires macOS 27 Golden Gate**, which is Apple silicon only. |
| Which iPhones lose iOS 27? | **None.** iOS 27 drops no iPhones. |
| Which iPads lose iPadOS 27? | All **A12-class** iPads: iPad Pro 2018 models, iPad Air 3rd gen, iPad mini 5th gen, iPad 8th gen and earlier. |
| Is SiriKit still the way to do voice? | No. **SiriKit is deprecated**; migrate to App Intents. |
| When must I submit with the OS 27 SDK? | **Not announced.** Do not invent a date. OS 26 SDK has been required since 2026-04-28. |
| What is macOS 27 called? | **macOS Golden Gate 27.** Last release with full Rosetta 2. |
| Does OS 27 change the Clear/Tinted toggle? | Yes — replaced by a **continuous transparency slider** in Settings > Appearance. |

## Task-Specific Loading

### Code Generation

```yaml
Required:
  - liquid-glass/introduction.md            # real API names — prevents fabrication
  - documentation/SwiftUI.md OR UIKit.md OR AppKit.md
Optional:
  - liquid-glass/adopting-liquid-glass.md   # if migrating existing UI
  - documentation/Swift.md                  # if using Swift 6.4 features
Skip:
  - figma/, human-interface-guidelines/ (unless a specific component is in scope)
```

### UI/UX Design Questions

```yaml
Required:
  - liquid-glass/introduction.md
  - human-interface-guidelines/components/<component>.md
Optional:
  - human-interface-guidelines/foundations/color.md | accessibility.md
Reference:
  - figma/<component>/ — describe by path, do not load
Skip:
  - documentation/*
```

### Migration and Compatibility

```yaml
Required:
  - liquid-glass/adopting-liquid-glass.md   # SDK gating table lives here
  - os27-intro/<platform>.md                # device support + migration section
Optional:
  - os27-intro/Program.md                   # submission requirements
  - os27-intro/macOS.md                     # if CI/build fleet is in scope
```

### Policy, App Store, and Release Planning

```yaml
Required:
  - os27-intro/Program.md
Optional:
  - documentation/DeclaredAgeRange.md
  - documentation/ios-ipados-release-notes.md
```

## Navigation Patterns

### Search before loading

```bash
# DON'T — 305K tokens
cat documentation/*.md

# DO — find candidates, then load 1–3 files
grep -ril "urlsession" documentation/
```

### Find version-specific guidance

Version-specific behavior lives in blockquote callouts with a consistent prefix:

```bash
# All OS 27 callouts across the repo
grep -rn "iOS 27+, iPadOS 27+" documentation/ human-interface-guidelines/ liquid-glass/

# OS 26-era callouts
grep -rn "iOS 26+, iPadOS 26+" human-interface-guidelines/
```

### Reference images without loading them

```bash
ls figma/Buttons/*.png   # describe by filename; never read as text
```

## Page Structure

Pages are predictably shaped, which makes partial extraction reliable.

```
# Title
One-line summary
**Platforms:** iOS 13.0+ | iPadOS 13.0+ | macOS 10.15+ | ...
> **iOS 27+, iPadOS 27+, macOS Golden Gate 27+:** version-specific callout
## Overview
## Topics
### Subsection
- [Link](url) - description
- **class Foo** - description
---
*Source: [Apple Developer Documentation](url)*
*SDK baseline: Apple OS 27 generation — ...*
```

- `documentation/` pages end with a **SDK baseline** footer and an Apple Developer `*Source:*` link.
- `human-interface-guidelines/` pages end with a **Design baseline** footer and an Apple HIG `*Source:*` link.
- `os26-intro/` and `os27-intro/` pages carry a generation status callout before `## Overview`.

To extract just a section, split on `### ` headings under `## Topics`.

## Topic Map

```yaml
SwiftUI development:
  - documentation/SwiftUI.md
  - liquid-glass/introduction.md
  - os26-liquid-glass-example/Landmarks/*.swift

UIKit / AppKit development:
  - documentation/UIKit.md | documentation/AppKit.md
  - liquid-glass/adopting-liquid-glass.md

Design system:
  - liquid-glass/*.md
  - human-interface-guidelines/foundations/
  - figma/ (reference only)

Platform overviews:
  iOS:      os27-intro/iOS.md      | os26-intro/iOS.md
  iPadOS:   os27-intro/iPadOS.md   | os26-intro/iPadOS.md
  macOS:    os27-intro/macOS.md    | os26-intro/macOS.md
  tvOS:     os27-intro/tvOS.md     | os26-intro/tvOS.md
  watchOS:  os27-intro/watchOS.md  | os26-intro/watchOS.md
  visionOS: os27-intro/visionOS.md | os26-intro/visionOS.md

WWDC 2026 / OS 27 additions:
  - documentation/FoundationModels.md  # generalized LanguageModel protocol, third-party providers
  - documentation/AppIntents.md        # entity + intent schemas, View Annotations API
  - documentation/Evaluations.md       # validating AI feature behavior
  - documentation/CoreAI.md            # intelligence infrastructure (hedged — read the caveats)
  - documentation/Swift.md             # Swift 6.4: anyAppleOS, @diagnose, weak let, ~Sendable, @C
  - documentation/Xcode.md             # Xcode 27, requires macOS 27
  - documentation/SiriKit.md           # DEPRECATED — points to App Intents

WWDC 2025 / OS 26 additions:
  - documentation/DeclaredAgeRange.md  # age-range API, iOS 26.0+
  - documentation/Charts.md            # Chart3D
  - documentation/Containerization.md  # Linux containers on Apple silicon
```

## Response Generation Guidelines

1. **Cite file paths** in the form `path/to/file.md` or `path/to/file.md:Section`.
2. **Say whether a claim is shipping or beta.** "In iOS 27, currently in beta…" not "In iOS 27…".
3. **Do not exceed the source.** If the repo hedges a number (for example, the OS 27 performance percentages), hedge it too.
4. **Recommend files rather than dumping content** when the answer is large.
5. **If the repo lacks the answer, say so** and point at the relevant `*Source:*` URL. Do not fill the gap by guessing.

### Example Response

```markdown
Liquid Glass adoption is gated on the SDK you link against, not the OS the
device runs (`liquid-glass/adopting-liquid-glass.md:Adoption Timeline`).

- Building against the OS 26 SDK: you may set `UIDesignRequiresCompatibility`
  to keep the legacy appearance, including when running on OS 27.
- Building against the OS 27 SDK: the key is ignored — Liquid Glass is applied
  with no supported opt-out.

Standard SwiftUI/UIKit/AppKit controls migrate automatically on recompile;
custom blur and navigation chrome need manual work using `glassEffect(_:in:)`
and `GlassEffectContainer`.

Note: no OS 27 SDK submission deadline has been announced
(`os27-intro/Program.md`). Track Apple's Upcoming Requirements page.
```

## Common Pitfalls

### ❌ DON'T

- Load entire directories recursively
- Parse `figma/` images as text
- Present OS 27 beta behavior as final shipping behavior
- Invent Liquid Glass API names, framework names, or SDK deadline dates
- Change `**Platforms:**` minimum-availability lines when summarizing
- Assume beta numbers match across platforms
- Claim macOS 27 supports Intel Macs, or that Xcode 27 runs on macOS 26

### ✅ DO

- Search, then load 1–3 specific files
- Load `os27-intro/` and `liquid-glass/` fully — they are small and high value
- Reference `figma/` by path with a description
- Carry hedges and uncertainty markers into your output
- Distinguish "shipping (26.6)" from "beta (27)" in every version claim
- Point at `*Source:*` links when precision matters

## Integration Examples

### Custom instructions for a chat assistant

```
When using the apple-os-documentation repository:
1. Load os27-intro/iOS.md and liquid-glass/introduction.md as base context (~3.5K tokens).
2. Search before loading anything from documentation/ or human-interface-guidelines/.
3. Reference figma/ paths without loading images.
4. Never invent API names — the real Liquid Glass API is in liquid-glass/introduction.md.
5. State clearly whether a fact describes shipping OS 26.6 or beta OS 27.
6. Never state an OS 27 release date or SDK deadline; neither has been announced.
```

### Progressive loading

```python
from pathlib import Path

BASE = ["os27-intro/iOS.md", "liquid-glass/introduction.md"]  # ~3.5K tokens

TASK_FILES = {
    "swiftui":   ["documentation/SwiftUI.md"],
    "uikit":     ["documentation/UIKit.md", "liquid-glass/adopting-liquid-glass.md"],
    "migration": ["liquid-glass/adopting-liquid-glass.md", "os27-intro/Program.md"],
    "design":    ["human-interface-guidelines/foundations/color.md"],
    "policy":    ["os27-intro/Program.md"],
}

def build_context(root: Path, task: str) -> dict[str, str]:
    paths = BASE + TASK_FILES.get(task, [])
    return {p: (root / p).read_text(encoding="utf-8") for p in paths}
```

## Maintenance

### Version Tracking

- **Shipping**: OS 26.6 across platforms; macOS Tahoe 26.6.1; Xcode 26.6
- **Beta**: OS 27 generation; Xcode 27 (requires macOS 27)
- **Last reviewed**: 2026-08-09
- Token counts are estimates and drift with edits

### Known Deadlines

| Date | Requirement |
|---|---|
| **2026-04-28** | App Store Connect uploads require the OS 26 SDK or later (Xcode 26+) — in effect |
| **Not announced** | OS 27 SDK submission requirement. Do not state a date. Track [Upcoming Requirements](https://developer.apple.com/news/upcoming-requirements/). |

### Platform Version Reference

All Apple platforms use unified generation numbering: OS 26 (2025–2026), OS 27 (2026–2027). visionOS jumped from 2.x directly to 26 — there is no visionOS 3 through 25.

macOS retains code names: **macOS Tahoe 26**, **macOS Golden Gate 27**.

### Change Detection

```bash
git diff HEAD~1 liquid-glass/          # design system changes
git diff HEAD~1 os27-intro/            # OS 27 generation changes
git diff HEAD~1 documentation/Swift.md # toolchain changes
```

## Contact & Support

- Human-readable overview: [`README.md`](./README.md)
- Bot-specific guidance: this file
- Report inaccuracies: [Issues](https://github.com/incrediblecrab/apple-os-documentation/issues)

---

**Remember**: load selectively, cite paths, preserve hedges, and never invent an API name or a date.

*Last reviewed: 2026-08-09 | Shipping: OS 26.6 | Beta: OS 27 | Community maintained*
