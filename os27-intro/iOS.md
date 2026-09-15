# iOS 27.0 Developer Introduction

Prepare iPhone apps for the iOS 27 SDK: migrate UIKit life-cycle handling, review data and asset delivery, and test system integrations against the current release. This introduction summarizes developer-facing changes rather than promising consumer features or performance gains.

**Platform:** iOS 27.0+

> **Status checked September 14, 2026:** iOS 27.0 (`24A437`) shipped September 14. The previous 26-generation release is **iOS 26.6.2** (`23G90`), released September 8.

## Overview

iOS 26 introduced Liquid Glass and the on-device Foundation Models framework. For iOS 27, separate three tests: running your shipping binary on the new OS, rebuilding it with the new SDK, and adopting new APIs. Linked-SDK changes can affect an existing feature even if you add no new code.

## Developer-Facing Changes

The following changes are documented in the [iOS & iPadOS 27 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes).

### App Intents and intelligence

- Audit schema conformances when rebuilding. `calendar.deleteEvents` is renamed to `calendar.deleteEvent`; existing `.photos.asset` entities may need additional properties and availability checks.
- Keep SiriKit integrations working while adding modern App Intents support. Apple describes SiriKit, Intents, and IntentsUI as providing **legacy support** for Shortcuts, widget configuration, and most existing Siri interactions—not a blanket framework shutdown. See [SiriKit](https://developer.apple.com/documentation/sirikit).
- The OS 27 Foundation Models API includes an entitlement-gated Private Cloud Compute model. Device, region, model availability, and developer eligibility remain separate requirements; see the [PCC guide](../guides/private-cloud-compute.md). Do not silently redirect a failed request to a third-party AI service.

### Data, assets, and diagnostics

- **Background Assets:** localized asset packs let the system select resources for a person's preferred languages. On Demand Resources and `NSBundleResourceRequest` are deprecated in favor of Background Assets. Plan download progress, offline access, cancellation, and missing-resource handling.
- **HealthKit:** heart-rate and cycling-power zones are supported. The permissions flow can distinguish limited from full history, so an authorized query need not return all historical samples. New reproductive-health categories require their own HealthKit authorization.
- **MetricKit:** the Swift-first `MetricManager` delivers reports through `AsyncStream`, including interval breakdowns and additional diagnostics. Check renamed/removed pre-release metric types when rebuilding rather than assuming code built with an earlier pre-release is compatible.
- **StoreKit:** offer-code redemption reports verification results or errors; transaction APIs also represent managed-account assignments and subscription Bundles/Suites. Verify transactions before granting access and keep payment-policy decisions separate from API availability.

### SwiftUI and UIKit

- `AsyncImage` participates in HTTP caching and gains request/session customization. Test authenticated images, cache headers, and failure states.
- Xcode 27 changes `@State` to a macro-based implementation that avoids repeated evaluation of an initial-value expression. Some initializer patterns need changes; the behavior also back-deploys to iOS 17-aligned releases.
- Selectable SwiftUI `Text` gains system selection gestures when linked with the iOS 27 SDK. Check conflicts with custom gestures.
- Presented UIKit controllers inherit traits through their view hierarchy. Re-test custom presentations and trait overrides.

## Migration Priorities

1. **Adopt scenes before rebuilding.** UIKit apps built with the latest SDK must use the scene-based life cycle or fail to launch on iOS 27. Move UI state and URL/activity handling to the appropriate scene; supporting multiple windows is optional. See [UIKit scene migration](https://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle).
2. **Include a launch screen.** Apps built with the iOS/iPadOS 27 SDK must declare a supported launch-screen key, such as `UILaunchStoryboardName` or `UILaunchScreen`. The notes tie submission enforcement to when the App Store starts accepting 27-SDK apps, not to a date inferred from pre-release notes.
3. **Finish the design transition.** [`UIDesignRequiresCompatibility`](https://developer.apple.com/documentation/bundleresources/information-property-list/uidesignrequirescompatibility) is ignored when building for iOS 27 or later. Test custom chrome, accessibility settings, and standard controls; installing a new OS and relinking against its SDK are different operations.
4. **Review resource and URL handling.** Migrate ODR usage; the notes also deprecate `canOpenURL:` in favor of attempting to open a URL and handling failure. Prefer universal links where appropriate.
5. **Audit managed-service TLS.** The stricter requirements affect selected system processes for MDM/DDM, enrollment, profiles, app installation, and software updates. Servers need TLS 1.2 or later and ATS-compliant certificates and ciphers. This is not a blanket new rule for every app socket; Apple's [network preparation guide](https://support.apple.com/en-us/126655) documents scope and exceptions.

### Beta testing, not permanent limitations

The iOS 27 notes mark earlier Foundation Models simulator/PCC problems and several App Intents failures as **resolved**. Re-test those paths; do not retain them as enduring restrictions. One listed known issue is that the default `SpotlightSearchTool` configuration can exceed the on-device model's context window; use the documented focused configuration when applicable.

## Devices and Toolchain

**Exact iOS 27 device list: not verified by the release sources used here.** Do not infer it from iOS 26 compatibility or devices mentioned in bug reports. Apple Intelligence eligibility is a separate, feature-specific check; this page does not invent hardware tiers.

**Xcode 27** (`27A266a`, September 14) includes Swift 6.4 and requires **an Apple silicon Mac running macOS Tahoe 26.6 or later**. It does not require macOS 27. Intel Macs cannot host Xcode 27; running Intel applications under Rosetta on Apple silicon is a different capability. See the [Xcode notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes).

## Submission Requirements

Since April 28, 2026, iOS uploads must use Xcode 26 or later and the iOS 26 SDK or later. This does not require raising your deployment target to iOS 26. The checked [Upcoming Requirements](https://developer.apple.com/news/upcoming-requirements/) page does not announce an OS 27 SDK deadline. Use the [App Store readiness checklist](../guides/app-store-readiness.md) for policy and submission checks.

## Getting Started

**New to iOS development?**
Check out the [iOS Pathway](https://developer.apple.com/ios/get-started/) for resources to get started with iOS app development.

## Resources

### Development Tools
- [Xcode](https://developer.apple.com/xcode/) - See the version-specific host requirements above
- [TestFlight](https://developer.apple.com/testflight/) - Beta testing platform
- [App Store Connect](https://developer.apple.com/app-store-connect/) - App management and analytics

### Documentation
- [UIKit Documentation](https://developer.apple.com/documentation/uikit)
- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)

### Related Platforms
- [iPadOS](iPadOS.md) - Enhanced iPad experiences
- [macOS](macOS.md) - macOS Golden Gate 27
- [tvOS](tvOS.md) - Living room entertainment
- [visionOS](visionOS.md) - Spatial computing
- [watchOS](watchOS.md) - Wearable experiences
- [Apple Developer Program](Program.md) - Membership, distribution, and policy

### Previous Generation
- [iOS 26 Developer Introduction](../os26-intro/iOS.md)

---

## Sources

[Apple Developer releases](https://developer.apple.com/news/releases/), [iOS/iPadOS 27 notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes), and [Xcode 27 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes), with additional scoped citations above. Reviewed September 8, 2026; hardware, region, language, and entitlement availability require separate checks.
