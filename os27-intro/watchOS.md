# watchOS 27.0 Developer Introduction

watchOS 27 focuses on health intelligence and low-friction interaction. A rebuilt Siri arrives on the wrist, Workout Buddy expands, and the Liquid Glass refinements from the rest of the generation carry through to the smallest Apple display.

**Platform:** watchOS 27.0+

> **Status:** watchOS 27 is in developer and public beta as of August 2026 (developer beta 1 on June 8, 2026; public beta 1 on July 13, 2026). A public release is expected in fall 2026. Apple has not announced a release date. The current shipping line is watchOS 26.6, released July 27, 2026.

## Overview

watchOS 27 continues the generation's intelligence theme, adapted to a device where interactions must be measured in seconds. Siri is rebuilt on Apple Foundation Models and syncs conversation context with the standalone Siri app on iPhone, iPad, Mac, and Apple Vision Pro, so a question started on one device can be continued on the wrist.

## Key Features

### Siri AI

Siri on Apple Watch is rebuilt on Apple Foundation Models with improved conversational understanding and cross-device continuity through the standalone Siri app.

### Health and Fitness

**Workout Buddy**
The personalized, motivational workout companion introduced in watchOS 26 expands its coverage and guidance.

**Cycle Tracking**
Perimenopause notifications alert people when logged patterns suggest perimenopause, with support for logging associated symptoms. Corresponding workout categories arrive in Fitness+.

**GymKit**
Gym equipment can now pair directly from iPhone, removing the requirement for an Apple Watch to be present to establish the connection.

### Design

Liquid Glass refinements carry to watchOS: better diffusion of busy content, a subtle darkened edge ring for separation, and brighter specular highlights. On a small, frequently glanced display, prioritize legibility — validate your complications and workout views under Reduce Transparency and Increase Contrast.

### App Intents

Entity and intent schemas make your app's content available to the system's semantic index and actionable through natural language, which is particularly valuable on a device where typing is impractical.

## What's New in watchOS 27

- **Siri AI**: rebuilt assistant with cross-device conversation sync
- **Workout Buddy**: expanded coverage
- **Cycle Tracking**: perimenopause notifications and symptom logging
- **GymKit**: direct iPhone pairing with equipment
- **Liquid Glass refinements** consistent with the rest of the generation
- **App Intents** entity and intent schemas

> **Note:** Apple's watchOS 27 announcements at WWDC 2026 emphasized health and intelligence over developer-facing API surface. Verify feature-level detail against the [watchOS release notes](https://developer.apple.com/documentation/watchos-release-notes) before relying on it.

## Device Support

watchOS 27 requires an Apple Watch Series 6 or later, Apple Watch SE (2nd generation) or later, or any Apple Watch Ultra, paired with an iPhone running iOS 27. Confirm the exact supported model list against Apple's official watchOS page, which is updated through the beta period.

## Migrating to watchOS 27

**Rebuild consciously.** As on other platforms, the current design appearance is gated on the linked SDK. Recompiling with Xcode 27 adopts the refined Liquid Glass appearance.

**SiriKit is deprecated.** Migrate watch-facing voice interactions to App Intents.

**Re-test complications.** Refined material rendering changes how translucent surfaces composite over watch faces; check every complication family you support.

## Getting Started

**New to watchOS development?**
Check out the [watchOS Pathway](https://developer.apple.com/watchos/) for resources on building Apple Watch apps.

## Resources

### Development Tools
- [Xcode](https://developer.apple.com/xcode/) - Xcode 27 requires macOS 27 Golden Gate on Apple silicon
- [TestFlight](https://developer.apple.com/testflight/) - Beta testing platform
- [App Store Connect](https://developer.apple.com/app-store-connect/) - App management and analytics

### Documentation
- [watchOS Developer Documentation](https://developer.apple.com/documentation/watchos/)
- [WatchKit Documentation](https://developer.apple.com/documentation/watchkit/)
- [HealthKit](../documentation/HealthKit.md)
- [Designing for watchOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos)

### Related Platforms
- [iOS](iOS.md) - iPhone experiences
- [iPadOS](iPadOS.md) - Enhanced tablet experiences
- [macOS](macOS.md) - macOS Golden Gate 27
- [tvOS](tvOS.md) - Living room entertainment
- [visionOS](visionOS.md) - Spatial computing
- [Apple Developer Program](Program.md) - Membership, distribution, and policy

### Previous Generation
- [watchOS 26 Developer Introduction](../os26-intro/watchOS.md)

---

*Reviewed 2026-08-09. watchOS 27 is pre-release software; features and availability may change before general release. Platform requirements and feature availability may vary, and some capabilities may not be available in all regions or languages.*
