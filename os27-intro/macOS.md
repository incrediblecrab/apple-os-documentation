# macOS Golden Gate 27.0 Developer Introduction

macOS Golden Gate 27 is the first fully Apple-silicon-only release of macOS. Freed from Intel support, it delivers a refined Liquid Glass interface, a rebuilt Siri, deeper iPhone continuity, and a development toolchain — Xcode 27 and Swift 6.4 — that assumes a modern Mac throughout.

**Platform:** macOS Golden Gate 27.0+

> **Status:** macOS 27 is in developer and public beta as of August 2026 (developer beta 1 on June 8, 2026; public beta 1 on July 13, 2026). A public release is expected in fall 2026. Apple has not announced a release date. The current shipping line is macOS Tahoe 26.6.1, released August 6, 2026.

## Overview

Two facts define this release for developers. First, macOS 27 runs only on Apple silicon — every remaining Intel Mac is dropped. Second, **Xcode 27 requires macOS 27**, which means adopting the new SDK requires upgrading your build machines and CI fleet to Apple silicon running Golden Gate. Plan that migration before it becomes urgent.

## Key Features

### Apple Silicon Only

macOS Golden Gate 27 requires an Apple silicon Mac (M1 or later). The final four Intel Macs supported by macOS Tahoe 26 are dropped:

| Dropped device |
|----------------|
| iMac (2020) |
| Mac Pro (2019) |
| MacBook Pro 16-inch (2019) |
| MacBook Pro 13-inch (2020, four Thunderbolt ports) |

macOS Tahoe 26 is the terminal release for those machines. If you ship Mac software, macOS 27 is the point at which universal binaries stop being a requirement for new work and become a compatibility choice for users still on Tahoe.

### Rosetta 2

macOS 27 is the **last release with full Rosetta 2 support**. Beginning with macOS 28, Rosetta is expected to be retained only as a limited compatibility layer for older unmaintained games and their dependent frameworks — not as a general-purpose translation environment. Any Intel-only binary in your distribution chain, including build tooling, test harnesses, and bundled helper executables, needs a native Apple silicon replacement.

> **Note:** The specific scope of Rosetta in macOS 28 is drawn from Apple's stated direction rather than shipped documentation. Verify against Apple's platform release notes before making irreversible plans.

### Supported Macs

- MacBook Air (M1, 2020) and later
- MacBook Pro (M1, 2020) and later
- Mac mini (M1, 2020) and later
- iMac (M1, 2021) and later
- Mac Studio (M1 Max/Ultra, 2022) and later
- Mac Pro (M2 Ultra, 2023) and later

### New Design

**Liquid Glass, refined**
The Mac interface adopts the same refinements as the rest of the generation: stronger diffusion of busy background content, a subtle darkened edge ring for separation, and brighter specular highlights. Toolbars become uniform and less translucent as content scrolls beneath.

**Transparency slider**
A continuous transparency slider in System Settings > Appearance replaces the Clear/Tinted toggle from macOS Tahoe 26, letting people tune translucency to their preference and environment.

**Sidebars**
Sidebars extend to the full window edge with refraction continuing beneath them, and sidebar icons retain their tint color rather than washing out.

### Siri AI

Siri on Mac is rebuilt on Apple Foundation Models, with extended conversational context, awareness of on-device personal data, and the ability to perform multi-step in-app actions. The standalone Siri app syncs conversations with iPhone, iPad, Apple Watch, and Apple Vision Pro.

### Continuity

Deeper iPhone integration continues the direction set by Tahoe — including Live Activities and Phone app features that let Mac act as a full extension of the iPhone rather than a peripheral to it.

## Developer Toolchain

### Xcode 27

**Xcode 27 requires macOS 27 Golden Gate.** There is no supported configuration for building with the Xcode 27 toolchain on macOS Tahoe 26 or on Intel hardware. Sequence your migration: upgrade a build machine, validate your project, then move CI.

Highlights include a rebuilt Instruments with lower-overhead sampling, improved SwiftUI previews, and coding assistance integrated across the editor. See [Xcode](../documentation/Xcode.md) for detail.

### Swift 6.4

Swift 6.4 ships with the Xcode 27 toolchain. Notable additions:

- `@available(anyAppleOS 27, *)` — a single availability spelling across Apple platforms, replacing long per-platform availability lists
- `@diagnose` — author custom compile-time diagnostics for misused APIs
- `weak let` — immutable weak references, eliminating a class of accidental reassignment bugs
- `~Sendable` — explicitly opt a type out of `Sendable` inference
- `@C` — improved C interoperability declarations
- Task Cancellation Shield — protect critical sections from cancellation mid-flight

See [Swift](../documentation/Swift.md) for detail.

## What's New in macOS Golden Gate 27

- **Apple silicon only**: M1 and later; final Intel Macs dropped
- **Last full Rosetta 2 release**
- **Xcode 27 requires macOS 27** — plan build and CI migration
- **Swift 6.4**: `anyAppleOS`, `@diagnose`, `weak let`, `~Sendable`, `@C`
- **Liquid Glass refinements** and a continuous transparency slider
- **Siri AI**: rebuilt assistant with a standalone, cross-device app
- **Evaluations framework**: validate AI feature behavior
- **Deeper iPhone continuity**

## Migrating to macOS 27

**Migrate CI first, not last.** Xcode 27's macOS 27 requirement makes your build fleet the critical path. Audit for any Intel runner still in service.

**Purge Intel-only binaries.** Command-line tools, code generators, linters, bundled helpers, and third-party frameworks all need Apple silicon builds before Rosetta's scope narrows in macOS 28.

**Liquid Glass is gated on the linked SDK.** Rebuilding with Xcode 27 opts your app fully into the current appearance; `UIDesignRequiresCompatibility` is ignored. Custom window chrome and blur effects need manual migration to `glassEffect(_:in:)` / `GlassEffectContainer` in SwiftUI or the equivalent AppKit materials.

**Decide your minimum.** Supporting macOS Tahoe 26 keeps the last Intel Macs in your audience; dropping to macOS 27 lets you assume Apple silicon throughout.

## Getting Started

**New to macOS development?**
Check out the [macOS Pathway](https://developer.apple.com/macos/) for resources on building Mac apps.

## Resources

### Development Tools
- [Xcode](https://developer.apple.com/xcode/) - Requires macOS 27 Golden Gate on Apple silicon
- [TestFlight](https://developer.apple.com/testflight/) - Beta testing platform
- [App Store Connect](https://developer.apple.com/app-store-connect/) - App management and analytics

### Documentation
- [macOS Developer Documentation](https://developer.apple.com/documentation/macos/)
- [AppKit Documentation](https://developer.apple.com/documentation/appkit/)
- [Apple Silicon](../documentation/apple-silicon.md)
- [Metal Documentation](https://developer.apple.com/documentation/metal/)

### Related Platforms
- [iOS](iOS.md) - iPhone experiences
- [iPadOS](iPadOS.md) - Enhanced tablet experiences
- [tvOS](tvOS.md) - Living room entertainment
- [visionOS](visionOS.md) - Spatial computing
- [watchOS](watchOS.md) - Wearable experiences
- [Apple Developer Program](Program.md) - Membership, distribution, and policy

### Distribution Options
- **Mac App Store**: worldwide reach with built-in discovery and payment processing
- **Developer ID**: distribute outside the Mac App Store with notarization

### Previous Generation
- [macOS Tahoe 26 Developer Introduction](../os26-intro/macOS.md)

---

*Reviewed 2026-08-09. macOS 27 is pre-release software; features and availability may change before general release. Platform requirements and feature availability may vary, and some capabilities may not be available in all regions or languages.*
