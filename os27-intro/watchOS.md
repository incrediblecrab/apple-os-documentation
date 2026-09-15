# watchOS 27.0 Developer Introduction

Prepare Apple Watch apps for watchOS 27 by reviewing HealthKit zones, SwiftUI state and image loading, and older WatchKit life-cycle APIs. Preserve quick interactions and useful offline behavior rather than making the watch app depend on an always-available phone or cloud service.

**Platform:** watchOS 27.0+

> **Status checked September 14, 2026:** watchOS 27.0 (`24R364`) shipped September 14. The previous 26-generation release is **watchOS 26.6** (`23U67`), released July 27.

## Overview

The [watchOS 27 release notes](https://developer.apple.com/documentation/watchos-release-notes/watchos-27-release-notes) distinguish new API behavior from fixes to complications, connectivity, and workouts. Keep your watchOS 26 deployment and device testing decisions separate from rebuilding with the new SDK.

## Developer-Facing Changes

### Health and workouts

HealthKit adds support for **heart-rate and cycling-power zones**. Request authorization only for the data your feature needs, handle unavailable readings, and test workout transitions on a device. A new health data type is not a guarantee that every Watch model, region, or user has data for it.

The 27 notes also contain resolved workout and Workout Buddy issues. Those fixes do not establish a public third-party “Workout Buddy API” or a new hardware eligibility list.

### SwiftUI and WatchKit

- **Life cycle:** `WKExtension` and `WKExtensionDelegate` are deprecated for apps with a **minimum deployment target of watchOS 9.2 or later**. Review the SwiftUI app life cycle and preserve an older-target path where needed. This is not the UIKit scene requirement used on iPhone, iPad, Apple TV, Catalyst, and visionOS.
- **State:** Xcode 27's macro-based `@State` avoids repeatedly evaluating initial-value expressions. Check initializer patterns and side effects; the change back-deploys to iOS 17-aligned OS releases.
- **Images:** `AsyncImage` follows HTTP caching and adds request/session customization. Handle slow or missing connectivity and avoid tying essential workout information to a fresh image download.
- **Controls:** new text-input border configuration and concentric corner geometry APIs support more deliberate control styling. Test text sizes, VoiceOver, Digital Crown interaction, and the dimmed/Always-On state where supported.

### Commerce, intents, and networking

- StoreKit represents managed-account transaction assignments and subscription Bundles/Suites. Handle verification, ownership, and revocation rather than unlocking content solely because a product is listed.
- [SiriKit](https://developer.apple.com/documentation/sirikit) retains legacy support for Shortcuts, widget configuration, and most existing Siri interactions. Use App Intents for modern integrations; do not remove working legacy paths based on a blanket deprecation claim.
- New TLS enforcement applies to selected system-managed enrollment, management, profile/app installation, and update connections. Apple's [network guidance](https://support.apple.com/en-us/126655) notes that much watchOS networking runs out of process; use its watch-specific testing advice rather than assuming the Mac log command works on the Watch.

## Migration and Testing

1. Rebuild and inspect deprecations with the actual deployment target; do not raise it merely to silence a warning.
2. Exercise app launch, background refresh, complications, notifications, and workouts with the companion phone disconnected.
3. Treat the 27 notes' resolved issues as regression cases, not permanent restrictions. Keep workarounds tied to an affected build.
4. If using Foundation Models/PCC, check the specific API's availability and runtime eligibility, not the OS version alone. See [PCC eligibility and failure handling](../guides/private-cloud-compute.md).

## Devices and Toolchain

**Exact watchOS 27 Watch model and companion-iPhone requirements: not verified by the reviewed sources.** Do not infer them from the watchOS 26 list or assume that each health or intelligence feature works on every eligible device.

**Xcode 27** (`27A266a`), released September 14, requires **an Apple silicon Mac running macOS Tahoe 26.6 or later**. macOS 27 is not required, and Rosetta does not make Intel Macs eligible hosts. See the [Xcode notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes).

Since April 28, 2026, watchOS uploads require Xcode 26 or later and the watchOS 26 SDK or later. The checked [requirements page](https://developer.apple.com/news/upcoming-requirements/) gives no OS 27 SDK deadline. See [App Store readiness](../guides/app-store-readiness.md).

## Getting Started

**New to watchOS development?**
Check out the [watchOS Pathway](https://developer.apple.com/watchos/get-started/) for resources on building Apple Watch apps.

## Resources

### Development Tools
- [Xcode](https://developer.apple.com/xcode/) - See the version-specific host requirements above
- [TestFlight](https://developer.apple.com/testflight/) - Beta testing platform
- [App Store Connect](https://developer.apple.com/app-store-connect/) - App management and analytics

### Documentation
- [Developing watchOS Apps](https://developer.apple.com/documentation/watchos-apps)
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

## Sources

[Apple Developer releases](https://developer.apple.com/news/releases/), [watchOS 27 notes](https://developer.apple.com/documentation/watchos-release-notes/watchos-27-release-notes), and [Xcode 27 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes), with additional scoped citations above. Reviewed September 8, 2026; health permissions, hardware eligibility, and version-specific behavior require separate validation.
