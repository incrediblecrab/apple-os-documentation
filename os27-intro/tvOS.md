# tvOS 27.0 Developer Introduction

Prepare Apple TV apps for tvOS 27 by migrating UIKit life-cycle handling, updating downloadable assets, and testing playback and focus behavior with the new SDK.

**Platform:** tvOS 27.0+

> **Status checked September 14, 2026:** tvOS 27.0 (`24J361`) shipped September 14. The previous 26-generation release is **tvOS 26.6** (`23L773`), released July 27.

> **Update checked November 1, 2026:** tvOS 27.2 (`24K122`) shipped October 26, 2026. The same day, Apple TV HD and Apple TV 4K (1st generation) received tvOS 26.6.1; Apple's security list gives no build number for it.

## Overview

The [tvOS 27 release notes](https://developer.apple.com/documentation/tvos-release-notes/tvos-27-release-notes) contain concrete migration work even for an app that adds no new features. Keep the existing living-room priorities—readable content, predictable focus, playback continuity, and multiple viewers—while validating linked-SDK changes.

## Developer-Facing Changes

### Scene life cycle

UIKit apps built with the latest SDK must adopt the scene-based life cycle or fail to launch on tvOS 27. This does not require a multiple-window user experience. Move UI life-cycle responsibilities to the scene and re-test launch, backgrounding, restoration, and playback resumption. `UIScene.extendStateRestoration` and `completeStateRestoration` can extend restoration across background-to-foreground transitions. See [UIKit scene migration](https://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle).

### Asset delivery and video

- **Background Assets:** localized asset packs let the system deliver resources matching preferred languages. On Demand Resources and `NSBundleResourceRequest` are deprecated in favor of Background Assets.
- **Failure handling:** keep browsing or playback usable when optional artwork or assets are absent; expose download progress and retry without assuming a request completes before the app backgrounds.
- **VideoToolbox:** `VTLowLatencySuperResolutionScalerConfiguration` gains a 1.5× scale factor, with a query for supported factors at the source dimensions. Low-latency frame interpolation supports arbitrary source dimensions up to 1080p. Query actual support; this is not a guarantee that every Apple TV supports every processing path.

### Commerce and system integration

- StoreKit adds managed-account transaction assignments and subscription Bundle/Suite information. Treat ownership, revocation, and verification failures as distinct states before unlocking content.
- Use available App Intents integrations and check each intent's tvOS support. Apple's cross-platform [SiriKit guidance](https://developer.apple.com/documentation/sirikit) describes legacy support, not a blanket shutdown; it does not imply that iPhone Shortcuts and widget surfaces exist on Apple TV.
- Selected system processes for device management, enrollment, profile/app installation, and updates impose stricter TLS requirements. Audit the relevant servers using Apple's [network preparation guide](https://support.apple.com/en-us/126655); don't equate this with a change to every media-stream connection.

## Migration and Testing

- [`UIDesignRequiresCompatibility`](https://developer.apple.com/documentation/bundleresources/information-property-list/uidesignrequirescompatibility) is ignored when building for tvOS 27 or later. Review custom focus effects and navigation surfaces rather than relying on the temporary compatibility appearance.
- Test remote and game-controller navigation, accessibility, subtitles, account switching, and playback interruptions against moving as well as static backgrounds.
- Treat the 27 notes' **Resolved Issues** as regression tests, not lasting platform limitations. Record the OS and Xcode build for a failure before carrying a workaround forward.

## Devices and Toolchain

**tvOS 27 devices:** Apple's [security release list](https://support.apple.com/en-us/100100) gives tvOS 27 (September 14, 2026) and tvOS 27.2 (October 26, 2026) as available for Apple TV 4K (2nd generation) and later. Apple TV HD and Apple TV 4K (1st generation) are not in those rows; their October 26, 2026 update was tvOS 26.6.1.

**Xcode 27** (`27A266a`), released September 14, requires **an Apple silicon Mac running macOS Tahoe 26.6 or later**, not macOS 27. Intel Macs cannot host it; Rosetta execution of Intel apps on Apple silicon is a separate issue. See the [Xcode release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes).

[Xcode 27.2](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes) (`27B52`, October 29, 2026) includes the tvOS 27.2 SDK and keeps the macOS Tahoe 26.6 host minimum. Its tvOS SDK wrongly reports 27.1 as a valid deployment target, and Apple warns that builds using it may behave unexpectedly (187160501).

Since April 28, 2026, tvOS uploads require Xcode 26 or later and the tvOS 26 SDK or later. The checked [requirements page](https://developer.apple.com/news/upcoming-requirements/) gives no OS 27 SDK deadline. See [App Store readiness](../guides/app-store-readiness.md).

## Getting Started

**New to tvOS development?**
Check out the [tvOS Pathway](https://developer.apple.com/tvos/get-started/) for resources on building Apple TV apps.

## Resources

### Development Tools
- [Xcode](https://developer.apple.com/xcode/) - See the version-specific host requirements above
- [TestFlight](https://developer.apple.com/testflight/) - Beta testing platform
- [App Store Connect](https://developer.apple.com/app-store-connect/) - App management and analytics

### Documentation
- [tvOS Release Notes](https://developer.apple.com/documentation/tvos-release-notes)
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

## Sources

[Apple Developer releases](https://developer.apple.com/news/releases/), [tvOS 27 notes](https://developer.apple.com/documentation/tvos-release-notes/tvos-27-release-notes), and [Xcode 27 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes), with additional scoped citations above. Reviewed September 8, 2026; full-body review updated November 1, 2026 against the [security release list](https://support.apple.com/en-us/100100), [release feed](https://developer.apple.com/news/releases/rss/releases.rss), [tvOS 27.2 notes](https://developer.apple.com/documentation/tvos-release-notes/tvos-27_2-release-notes), and [Xcode 27.2 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes). Feature and hardware eligibility remain separate checks.
