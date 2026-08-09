# tvOS 27.0 Developer Introduction

tvOS 27 carries the generation's design refinements and rebuilt Siri to the living room, with continued emphasis on immersive audio, gaming, and the shared-screen experiences that distinguish Apple TV from personal devices.

**Platform:** tvOS 27.0+

> **Status:** tvOS 27 is in developer and public beta as of August 2026 (developer beta 1 on June 8, 2026; public beta 1 on July 13, 2026). A public release is expected in fall 2026. Apple has not announced a release date. The current shipping line is tvOS 26.6, released July 27, 2026.

## Overview

tvOS 27 is an incremental release. The material refinements introduced across the generation apply to the focus-driven television interface, and Siri's rebuild reaches the Apple TV remote and voice input. Apple's WWDC 2026 messaging for tvOS was comparatively light on new developer API surface.

## Key Features

### Design

Liquid Glass refinements apply to tvOS: stronger diffusion of busy background content, a subtle darkened edge ring for separation, and brighter specular highlights. Because tvOS is viewed at a distance and navigated by focus rather than touch, verify that focus states remain unmistakable against refined translucent materials — especially over bright, moving video artwork.

### Siri

Siri on Apple TV benefits from the generation's rebuild on Apple Foundation Models, with improved conversational understanding for search and playback.

### Media and Gaming

Apple TV remains the platform's living-room media and gaming surface, with continued support for immersive audio formats, game controllers, and multiuser profiles.

> **Note:** tvOS 27's developer-facing changes are modest relative to iOS and macOS. Confirm specifics against the [tvOS release notes](https://developer.apple.com/documentation/tvos-release-notes) before depending on any individual feature.

## What's New in tvOS 27

- **Liquid Glass refinements** consistent with the rest of the generation
- **Siri**: rebuilt on Apple Foundation Models
- **App Intents** entity and intent schemas for system-level content understanding
- Continued media, audio, and gaming platform investment

## Device Support

tvOS 27 supports Apple TV 4K (all generations) and Apple TV HD. Confirm the exact supported model list against Apple's official tvOS page.

## Migrating to tvOS 27

**Appearance follows the linked SDK.** Rebuilding with Xcode 27 adopts the refined appearance. Custom focus treatments and bespoke background blur need manual review.

**Re-test focus and legibility.** The most common tvOS regression in this generation is a focus ring that reads clearly on a solid background but not against refined glass over video.

**SiriKit is deprecated.** Migrate to App Intents.

## Getting Started

**New to tvOS development?**
Check out the [tvOS Pathway](https://developer.apple.com/tvos/) for resources on building Apple TV apps.

## Resources

### Development Tools
- [Xcode](https://developer.apple.com/xcode/) - Xcode 27 requires macOS 27 Golden Gate on Apple silicon
- [TestFlight](https://developer.apple.com/testflight/) - Beta testing platform
- [App Store Connect](https://developer.apple.com/app-store-connect/) - App management and analytics

### Documentation
- [tvOS Developer Documentation](https://developer.apple.com/documentation/tvos/)
- [Designing for tvOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos)
- [Focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection)

### Related Platforms
- [iOS](iOS.md) - iPhone experiences
- [iPadOS](iPadOS.md) - Enhanced tablet experiences
- [macOS](macOS.md) - macOS Golden Gate 27
- [visionOS](visionOS.md) - Spatial computing
- [watchOS](watchOS.md) - Wearable experiences
- [Apple Developer Program](Program.md) - Membership, distribution, and policy

### Previous Generation
- [tvOS 26 Developer Introduction](../os26-intro/tvOS.md)

---

*Reviewed 2026-08-09. tvOS 27 is pre-release software; features and availability may change before general release. Platform requirements and feature availability may vary, and some capabilities may not be available in all regions or languages.*
