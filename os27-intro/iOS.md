# iOS 27.0 Developer Introduction

Prepare iPhone apps for the iOS 27 SDK: migrate UIKit life-cycle handling, review data and asset delivery, and test system integrations against the current release. This introduction summarizes developer-facing changes rather than promising consumer features or performance gains.

**Platform:** iOS 27.0+

> **Status checked September 14, 2026:** iOS 27.0 (`24A437`) shipped September 14. The latest 26-generation release that day was **iOS 26.7**, also released September 14, 2026.

> **Update checked October 29, 2026:** iOS **27.2** (`24B119`) shipped October 26, 2026; the developer feed also lists iOS 27.2 build `24B91020` without identifying its device scope. iOS 27.0.1 (`24A446`) shipped September 28, 2026. Apple's security list records iOS **27.1** for **iPhone Duo only** on October 23, 2026, without a build number; this release is absent from the checked developer feed. The latest 26-generation release is **iOS 26.7.2** (October 26, 2026), following iOS 26.7.1 (September 28, 2026); the security list gives no iOS build numbers for these maintenance releases.

## Overview

iOS 26 introduced Liquid Glass and the on-device Foundation Models framework. For iOS 27, separate three tests: running your shipping binary on the new OS, rebuilding it with the new SDK, and adopting new APIs. Linked-SDK changes can affect an existing feature even if you add no new code.

## Developer-Facing Changes

The following changes are documented in the [iOS & iPadOS 27 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes).

### App Intents and intelligence

- Audit schema conformances when rebuilding. `calendar.deleteEvents` is renamed to `calendar.deleteEvent`; existing `.photos.asset` entities may need additional properties and availability checks.
- Keep SiriKit integrations working while adding modern App Intents support. Apple describes SiriKit, Intents, and IntentsUI as providing **legacy support** for Shortcuts, widget configuration, and most existing Siri interactions—not a blanket framework shutdown. See [SiriKit](https://developer.apple.com/documentation/sirikit).
- The OS 27 Foundation Models API includes an entitlement-gated Private Cloud Compute model. Device, region, model availability, and developer eligibility remain separate requirements; see the [PCC guide](../guides/private-cloud-compute.md). Do not silently redirect a failed request to a third-party AI service.

### Data, assets, and diagnostics

- **Background Assets:** localized asset packs let the system select resources for a person's preferred languages. The notes deprecate On Demand Resources and `NSBundleResourceRequest` in favor of Background Assets; they do not announce removal. Plan download progress, offline access, cancellation, and missing-resource handling.
- **HealthKit:** heart-rate and cycling-power zones are supported. The permissions flow can distinguish limited from full history, so an authorized query need not return all historical samples. New reproductive-health categories require their own HealthKit authorization.
- **MetricKit:** the Swift-first `MetricManager` delivers reports through `AsyncStream`, including interval breakdowns and additional diagnostics. Check renamed/removed pre-release metric types when rebuilding rather than assuming code built with an earlier pre-release is compatible.
- **StoreKit:** offer-code redemption reports verification results or errors; transaction APIs also represent managed-account assignments and subscription Bundles/Suites. Verify transactions before granting access and keep payment-policy decisions separate from API availability.

### SwiftUI and UIKit

- `AsyncImage` participates in HTTP caching and gains request/session customization. Test authenticated images, cache headers, and failure states.
- Xcode 27 changes `@State` to a macro-based implementation that avoids repeated evaluation of an initial-value expression. Some initializer patterns need changes; the behavior also back-deploys to iOS 17-aligned releases.
- Selectable SwiftUI `Text` gains system selection gestures when linked with the iOS 27 SDK. Check conflicts with custom gestures.
- In apps built with the iOS 27 SDK, presented UIKit controllers inherit traits through their view hierarchy. Re-test custom presentations and trait overrides.

## Migration Priorities

1. **Adopt scenes before rebuilding.** UIKit apps built with the latest SDK must use the scene-based life cycle or fail to launch on iOS 27. Move UI state and URL/activity handling to the appropriate scene; supporting multiple windows is optional. See [UIKit scene migration](https://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle).
2. **Include a launch screen.** Apps built with the iOS/iPadOS 27 SDK must declare a supported launch-screen key, such as `UILaunchStoryboardName` or `UILaunchScreen`. The notes tie submission enforcement to when the App Store starts accepting 27-SDK apps, not to a date inferred from pre-release notes.
3. **Finish the design transition.** [`UIDesignRequiresCompatibility`](https://developer.apple.com/documentation/bundleresources/information-property-list/uidesignrequirescompatibility) is ignored when building for iOS 27 or later. Test custom chrome, accessibility settings, and standard controls; installing a new OS and relinking against its SDK are different operations.
4. **Review resource and URL handling.** Migrate ODR usage; the notes also deprecate `canOpenURL:` in favor of attempting to open a URL and handling failure. Prefer universal links where appropriate.
5. **Audit managed-service TLS.** The stricter requirements affect selected system processes for MDM/DDM, enrollment, profiles, app installation, and software updates. Servers need TLS 1.2 or later and ATS-compliant certificates and ciphers. This is not a blanket new rule for every app socket; Apple's [network preparation guide](https://support.apple.com/en-us/126655) documents scope and exceptions.

### Beta testing, not permanent limitations

The iOS 27 notes mark earlier Foundation Models simulator/PCC problems and several App Intents failures as **resolved**. Re-test those paths; do not retain them as enduring restrictions. One listed known issue is that the default `SpotlightSearchTool` configuration can exceed the on-device model's context window; use the documented focused configuration when applicable.

## Devices and Toolchain

**Device scope checked October 29, 2026:** Apple's security-release entries for iOS 27 and iOS 27.2 list **iPhone 11 and later**; they give a range rather than a model-by-model compatibility list. Apple Intelligence eligibility remains a separate, feature-specific check.

**Xcode 27** (`27A266a`, September 14) includes Swift 6.4 and requires **an Apple silicon Mac running macOS Tahoe 26.6 or later**. It does not require macOS 27. Intel Macs cannot host Xcode 27; running Intel applications under Rosetta on Apple silicon is a different capability. See the [Xcode notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes).

**Toolchain update checked October 29, 2026:** Xcode 27.1 (`27A9275`, October 15, 2026) includes the iOS 27.1 SDK; Xcode 27.2 includes SDKs for all six 27.2 platforms. Both include Swift 6.4 and require macOS Tahoe 26.6 or later. Apple's [security-releases list](https://support.apple.com/en-us/100100) dates Xcode 27.2 to October 29, 2026. The [developer feed](https://developer.apple.com/news/releases/rss/releases.rss) checked that day still listed only Xcode 27.2 RC (`27B48`, October 19, 2026); the feed checked November 1, 2026 lists the final release, Xcode 27.2 (`27B52`), dated October 29, 2026.

**Point-release build caveats:** The [Xcode 27.1 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes) and [Xcode 27.2 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes) list Mac Catalyst compile failures for iOS 27.1-specific APIs; use compile-time platform conditionals to exclude affected code from Mac Catalyst builds. Xcode 27.2 incorrectly offers 27.1 deployment targets for macOS, watchOS, tvOS, and visionOS, and its notes warn that Mac Catalyst targets of 27.1 or 27.2 may be unable to use newly introduced APIs.

## Submission Requirements

Since April 28, 2026, iOS uploads must use Xcode 26 or later and the iOS 26 SDK or later. This does not require raising your deployment target to iOS 26. Since September 9, 2026, however, iOS and iPadOS uploads must target iOS 13 or later. The [Upcoming Requirements](https://developer.apple.com/news/upcoming-requirements/) page checked October 29, 2026 does not announce an OS 27 SDK deadline. Use the [App Store readiness checklist](../guides/app-store-readiness.md) for policy and submission checks.

## Getting Started

**New to iOS development?** Check out the [iOS Pathway](https://developer.apple.com/ios/get-started/) for resources to get started with iOS app development.

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

[Apple Developer releases](https://developer.apple.com/news/releases/), [Apple security releases](https://support.apple.com/en-us/100100), [developer release feed](https://developer.apple.com/news/releases/rss/releases.rss), [iOS/iPadOS 27 notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes), [iOS/iPadOS 27.2 notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_2-release-notes), [Xcode 27 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes), [Xcode 27.1 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes), and [Xcode 27.2 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes), with additional scoped citations above. Reviewed September 8, 2026; updated and fully reviewed October 29 and November 1, 2026. Hardware, region, language, and entitlement availability require separate checks.
