# iPadOS 27.0 Developer Introduction

Build iPad apps that behave like desktop software when people want them to. iPadOS 27 refines the windowing system introduced in iPadOS 26, adds a persistent menu bar, makes external displays substantially more capable, and brings the rebuilt Siri AI and Apple Pencil–driven Visual Intelligence to the largest Apple touch canvas.

**Platform:** iPadOS 27.0+

> **Status:** iPadOS 27 is in developer and public beta as of August 2026 (developer beta 1 on June 8, 2026; public beta 1 on July 13, 2026). A public release is expected in September 2026. Apple has not announced a release date. The current shipping line is iPadOS 26.6, released July 27, 2026.

## Overview

iPadOS 27 is the release where the iPad windowing model settles. Windows resize, move, and close more smoothly, Split View and Slide Over now operate inside the windowing framework rather than alongside it, and a persistent menu bar option gives multitasking a stable anchor. Paired with a rebuilt Siri and Apple Pencil–driven Visual Intelligence, iPad becomes materially more useful for sustained, document-centric work.

## Key Features

### Multitasking and Windowing

**A refined windowing system**
Windows resize, move, and close more smoothly than in iPadOS 26, with tuning aimed at large iPads paired with a Magic Keyboard. Multiple overlapping windows behave much closer to the Mac.

**Persistent menu bar**
People can keep the menu bar visible during multitasking, with the active app's name displayed for orientation.

**Split View and Slide Over, unified**
Split View and Slide Over remain available but now operate within the windowing framework. There is no separate classic mode; people invoke them through windowing controls.

**Stage Manager refinements**
Window arrangement gains more granular control, particularly when an external display is attached.

### External Display

The external display experience moves closer to macOS: improved windowing, the persistent menu bar, resizable iPhone apps on the external screen, and the ability to pin different apps to the iPad and the external display independently.

### Files and Background Work

**Background uploads and exports**
File uploads to iCloud or third-party services and long photo or video exports no longer pause or fail when someone leaves your app or locks the iPad. Design long-running transfer and export flows to continue in the background.

**Preview and quick actions**
Files gains more robust in-place document viewing, smarter quick actions, and improved annotation for documents on external media.

### Siri AI and Apple Intelligence

Siri is rebuilt on Apple Foundation Models — conversational, context-aware across apps, and able to perform multi-step in-app actions. The standalone Siri app syncs conversations across iPhone, iPad, Mac, Apple Watch, and Apple Vision Pro.

### Visual Intelligence

**Point and understand**
Photograph a meal and Siri breaks down nutritional information, ingredients, and dietary guidance. Photograph a restaurant receipt and Siri identifies and splits items per person; in the US, Apple Cash requests can be sent directly from the result.

**Apple Pencil as an intelligence input**
Circle or tap anything on screen with Apple Pencil to ask Siri about it — the interaction modality that most distinguishes iPad from iPhone in this release.

### App Intents

Entity schemas contribute your app's content to Spotlight's semantic index, and intent schemas let people act on that content in natural language without fixed phrases. The new View Annotations API maps SwiftUI views to entities so people can reference on-screen content conversationally — a natural fit for the larger iPad canvas.

## What's New in iPadOS 27

- **Refined windowing**: smoother resize, move, and close; Mac-like overlapping windows
- **Persistent menu bar**: always-visible option with active app name
- **Unified Split View and Slide Over**: now inside the windowing framework
- **External display**: pinning, resizable iPhone apps, persistent menu bar
- **Background file uploads and exports**: continue when leaving the app or locking the device
- **Siri AI**: rebuilt assistant with a standalone, cross-device Siri app
- **Apple Pencil Visual Intelligence**: circle or tap to ask
- **Liquid Glass refinements**: including sidebars that extend to the full window edge with refraction continuing beneath, and sidebar icons that retain their tint color

## Device Support

iPadOS 27 drops every A12-class iPad — the largest iPad compatibility pruning in recent memory.

**Supported:**

- **iPad Pro** — 13-inch (M4 and later), 12.9-inch (4th generation and later), 11-inch (2nd generation and later)
- **iPad Air** — 13-inch and 11-inch (M2 and later), and 4th generation and later
- **iPad** — 9th generation (2021) and later, plus iPad with A16
- **iPad mini** — 6th generation (2021) and later, including iPad mini with A17 Pro

**Dropped versus iPadOS 26:**

| Device | Chip |
|--------|------|
| iPad Pro 12.9-inch (3rd generation, 2018) | A12X |
| iPad Pro 11-inch (1st generation, 2018) | A12X |
| iPad Air (3rd generation, 2019) | A12 |
| iPad mini (5th generation, 2019) | A12 |
| iPad (8th generation, 2020) and earlier | A12 / A10 |

If your app still supports A12-class hardware, iPadOS 26 is now its terminal iPad release — plan deployment targets accordingly.

### Apple Intelligence availability

Advanced on-device features target iPad Air M4 and iPad Pro M4 and later. Core Apple Intelligence is available on iPad mini with A17 Pro and any iPad with an M1 chip or newer. Exact cutoffs for iPad 9th generation (A13) and iPad Air 4th generation (A14) should be confirmed against Apple's official feature availability page.

## Migrating to iPadOS 27

**Liquid Glass is mandatory once you rebuild.** The `UIDesignRequiresCompatibility` key is ignored by the iPadOS 27 SDK. Appearance is gated on the linked SDK, not the running OS.

**Audit your multitasking assumptions.** With Split View and Slide Over folded into the windowing framework, apps that hard-code size-class transitions or assume a fixed set of multitasking states should be re-tested across free-form window sizes and external displays.

**Raise your deployment floor deliberately.** With A12 hardware gone, confirm whether your minimum deployment target still needs to accommodate devices that can no longer receive the current OS.

**SiriKit is deprecated.** Migrate to App Intents.

## Getting Started

**New to iPad development?**
Check out the [iPadOS Pathway](https://developer.apple.com/ipados/) for resources on building iPad apps.

## Resources

### Development Tools
- [Xcode](https://developer.apple.com/xcode/) - Xcode 27 requires macOS 27 Golden Gate on Apple silicon
- [TestFlight](https://developer.apple.com/testflight/) - Beta testing platform
- [App Store Connect](https://developer.apple.com/app-store-connect/) - App management and analytics

### Documentation
- [iPadOS Developer Documentation](https://developer.apple.com/documentation/ipados/)
- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Multitasking guidance](https://developer.apple.com/design/human-interface-guidelines/multitasking)

### Related Platforms
- [iOS](iOS.md) - iPhone experiences
- [macOS](macOS.md) - macOS Golden Gate 27
- [tvOS](tvOS.md) - Living room entertainment
- [visionOS](visionOS.md) - Spatial computing
- [watchOS](watchOS.md) - Wearable experiences
- [Apple Developer Program](Program.md) - Membership, distribution, and policy

### Previous Generation
- [iPadOS 26 Developer Introduction](../os26-intro/iPadOS.md)

---

*Reviewed 2026-08-09. iPadOS 27 is pre-release software; features and availability may change before general release. Platform requirements and feature availability may vary, and some capabilities may not be available in all regions or languages.*
