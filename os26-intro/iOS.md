# iOS 26.0 Developer Introduction

Build and maintain iPhone apps using the iOS 26 generation's Liquid Glass interfaces, on-device Foundation Models, App Intents, and established notification, widget, and media APIs. This page preserves OS26 context while identifying work needed for an eventual OS27 SDK migration.

**Platform:** iOS 26.0+

> **Status checked September 8, 2026:** the shipping release is **iOS 26.6.2** (`23G90`), released September 8. iOS 27 beta 8 was released August 31; see the [iOS 27 introduction](../os27-intro/iOS.md). A beta listing does not establish a general-availability date.

## Overview

iOS 26 adds a new system appearance and access to Apple's on-device language model. Existing capabilities such as passkeys and Live Activities remain useful; their inclusion here does not mean they first appeared in iOS 26. Check each API's availability and keep a non-AI path on devices where the model is unavailable.

## Key Features

### New Design

**Say hello to Liquid Glass**  
Use system controls and materials to adopt Liquid Glass, then review custom navigation surfaces, contrast, and accessibility. Avoid placing decorative glass over content that people need to read.

### Apple Intelligence

**Tap into the on-device large language model**  
Use Foundation Models for supported on-device generation and tool-calling workflows. Check model availability and handle unsupported devices, disabled intelligence features, and generation failures; cloud processing is a separate integration and privacy decision.

### Enhanced App Capabilities

**App Intents**  
Make your app's core functions available throughout the system with App Intents. Enable users to access your app's features through Siri, Shortcuts, and system-wide search.

**Live Activities**  
Use Live Activities for ongoing activity information on supported system surfaces, including the Lock Screen and, where available, the Dynamic Island. Handle update limits and periods without a fresh network update.

**Widgets**  
Use WidgetKit for glanceable content and supported interactions. Review widget appearance with the OS26 design; interactive widgets predate iOS 26.

**Notifications**  
Use local or remote notifications and supported notification actions. Respect authorization choices and handle delivery or network interruptions.

### Gaming and Graphics

**Metal-powered games**  
Use Metal's low-level GPU APIs for rendering and compute work. Profile your workload rather than assuming a particular performance gain.

### Security

**Powerful passkeys**  
Use phishing-resistant public-key credentials and the system's authentication flow. Biometrics can authorize use of a passkey, but are not themselves the account credential. See [Supporting passkeys](https://developer.apple.com/documentation/authenticationservices/supporting-passkeys).

## What's New in iOS 26

Dive into the latest key technologies and capabilities:

- **Liquid Glass**: System appearance changes that require testing custom chrome
- **Foundation Models**: On-device model access with runtime availability checks
- **App Intents, widgets, and Live Activities**: System entry points to review alongside your app
- **Metal 4**: New graphics capabilities subject to GPU and API support
- **Privacy and accessibility**: Validate permissions and system appearance settings as part of adoption

### iOS 26.1 Updates (November 2025)
- The [26.1 notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-26_1-release-notes) fix `AssetPackManager.url(for:)` incorrectly failing for a locally available asset.
- Recompile against the 26.1 SDK for the documented `navigationLinkIndicatorVisibility` crash fix on iOS 17/18 and aligned releases.

### iOS 26.2 Updates
- **Hypertension Notifications API**: Authorize `HKCategoryTypeIdentifierHypertensionEvent` to read hypertension notifications from Apple Watch
- **StoreKit `AppStore.ageRatingCode`**: Fetch the current age rating code for your app to detect rating changes
- **DeclaredAgeRange fixes**: Recompile against the 26.2 SDK for the specific affected eligibility/declaration symbols listed in issue 165248390; this is not a fix for every age-range failure
- **TLS Client Hello updated**: Servers with strict bot-detection should adopt resilient policies that handle TLS fingerprint changes

### iOS 26.3 Updates
- **StoreKit fix**: Corrects a defect that made `Product.products(for:)` fail silently instead of throwing an error

### iOS 26.4 Updates
- **Memory Integrity Enforcement (MIE)**: The 26.4 notes add opt-in full protections, previously limited to Soft Mode; check hardware and build-setting requirements
- **Background Assets offline status**: Check asset-pack status offline via `localStatus(ofAssetPackWithID:)` and `assetPackIsAvailableLocally(withID:)`; the notes warn that not all status information is available offline
- **Background Assets latest version**: Use `ensureLocalAvailability(of:requireLatestVersion:)` to keep asset packs current
- **StoreKit revocation fields**: New `Transaction.revocationType` and `Transaction.revocationPercentage` properties
- **RCS end-to-end encryption (developer testing)**: The 26.4 notes describe beta testing between Apple and Android devices, not a shipped feature in that release
- **AudioAccessoryKit (developer testing)**: The 26.4 notes describe headphone information for automatic audio switching and a future EU customer rollout, not worldwide availability
- **Accessory Notifications Framework (developer testing)**: The 26.4 notice limits testing to iPhone and describes a future EU customer rollout; accessory companion apps request notification forwarding through an extension
- **SwiftUI fix**: `.userActivity` now correctly surfaces as the current user activity
- **Networking fix**: Resolves `CFRunLoopSource` leaks when PAC or Auto proxy discovery is configured

### iOS 26.5 through 26.6.2
- Retain the [26.5](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-26_5-release-notes) and [26.6](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-26_6-release-notes) notes when diagnosing older behavior
- **iOS 26.6.2 (September 8, 2026)** supersedes 26.6 as the shipping maintenance baseline
- Consult [Apple's security release list](https://support.apple.com/en-us/100100) for security-update scope; absence of a published CVE is not evidence of a new developer API

### Preparing an OS26 App for OS27

- Migrate UIKit app-delegate UI handling to scenes before rebuilding with the latest SDK: on iOS 27, an unmigrated app fails to launch. See [scene migration](https://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle).
- Plan migration from ODR to Background Assets and complete custom UI work before the temporary [`UIDesignRequiresCompatibility`](https://developer.apple.com/documentation/bundleresources/information-property-list/uidesignrequirescompatibility) key is ignored by 27-SDK builds.
- Keep existing SiriKit behavior while adopting App Intents; [Apple documents legacy support](https://developer.apple.com/documentation/sirikit), not a blanket SiriKit shutdown.
- Xcode 27 beta 6 needs **Apple silicon and macOS Tahoe 26.4 or later**, not macOS 27. Keep OS26 deployment tests while adding [OS27 migration tests](../os27-intro/iOS.md); the exact iOS 27 device list is not verified here.
- Apply the current [App Store readiness requirements](../guides/app-store-readiness.md) independently of your deployment target.

## Getting Started

**New to iOS development?**  
Check out the [iOS Pathway](https://developer.apple.com/ios/get-started/), a collection of resources to get started with iOS app development.

## Developer Success Stories

### Learning to fly
Read [Apple's Flighty profile](https://developer.apple.com/news/?id=970ncww4) about Ryan Jones and the team's use of Live Activities, widgets, and flight information.

### A gentler approach
[Apple's Gentler Streak profile](https://developer.apple.com/news/?id=3m0ht22s) describes the team's emphasis on personal progress and a less competitive fitness experience.

### A photo finish
[Apple's 2022 Design Awards](https://developer.apple.com/design/awards/2022/) describe Halide Mark II's camera interface and focus/exposure controls.

## Resources

### Development Tools
- [Xcode](https://developer.apple.com/xcode/) - Complete development environment
- [TestFlight](https://developer.apple.com/testflight/) - Beta testing platform
- [App Store Connect](https://developer.apple.com/app-store-connect/) - App management and analytics

### Documentation
- [UIKit Documentation](https://developer.apple.com/documentation/uikit)
- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)

### Related Platforms
Build apps that integrate seamlessly across all Apple platforms:
- [iPadOS](iPadOS.md) - Enhanced iPad experiences
- [macOS](macOS.md) - Desktop and laptop applications  
- [tvOS](tvOS.md) - Living room entertainment
- [visionOS](visionOS.md) - Spatial computing
- [watchOS](watchOS.md) - Wearable experiences

## Support

### Meet with Apple
Sharpen your skills through in-person and online activities around the world. Connect directly with Apple engineers and designers to create your best apps and games.

### Apple Developer Program
Join the [Apple Developer Program](Program.md) for TestFlight, App Store distribution, and capabilities that require membership. Developer beta access and paid membership are separate questions.

---

*Platform requirements and feature availability may vary. Some capabilities and services may not be available in all regions or all languages.*

## Sources

[Designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios), [Liquid Glass adoption](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass), and [SystemLanguageModel](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel) support the platform guidance. [Apple Developer releases](https://developer.apple.com/news/releases/), [26.2 notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-26_2-release-notes), [26.4 notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-26_4-release-notes), [iOS/iPadOS 27 notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes), and [Xcode 27 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes) support the status and migration guidance checked September 8, 2026. Inline story sources describe historical examples.
