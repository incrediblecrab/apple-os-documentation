# iPadOS 26.0 Developer Introduction

Maintain iPad apps that adapt to windows, keyboard and pointer input, Apple Pencil, and external displays. iPadOS 26 adds Liquid Glass and on-device Foundation Models, while earlier document and multitasking capabilities remain part of a complete iPad experience.

**Platform:** iPadOS 26.0+

> **Status checked September 8, 2026:** the shipping release is **iPadOS 26.6.2** (`23G90`), released September 8. iPadOS 27 beta 8 was released August 31; see the [iPadOS 27 introduction](../os27-intro/iPadOS.md). Its exact device list is not verified here; do not infer that A12-class hardware has reached its final release.

## Overview

Treat a resizable scene, not a fixed full-screen rectangle, as the unit of UI design. Keep document state separate from window state and test layouts with touch, keyboard, and pointer input. Hardware-dependent intelligence and display capabilities need their own availability checks.

## Key Features

### New Design

**Say hello to Liquid Glass**  
Use standard controls and materials for Liquid Glass, then test custom sidebars, toolbars, and popovers at different window sizes and accessibility settings.

### Apple Intelligence

**Tap into the on-device large language model**  
Foundation Models provides on-device generation on eligible hardware. Keep document editing functional if the model is unavailable or a request fails, and distinguish on-device work from any separately consented cloud integration.

### Enhanced App Capabilities

**App Intents**  
Make your app's core functions available throughout the iPadOS system. Enable seamless integration with multitasking, search, and productivity workflows.

**Apple Pencil Integration**  
Support drawing and editing with the appropriate PencilKit and UIKit input APIs. Test the Pencil models and gestures your app advertises instead of assuming every accessory provides identical capabilities.

**Live Activities**  
Use ActivityKit and a widget extension for supported iPad Live Activity presentations. Handle update limits and design useful content even when a fresh network update is unavailable.

**Enhanced Notifications**  
Provide local or remote notifications and supported actions, respecting authorization and adapting their content to the system presentation.

### Productivity Features

**Advanced Multitasking**  
Support the windowing modes available on the running iPadOS version and device. Re-test resizing, keyboard focus, restoration, and external-display transitions instead of assuming every minor release has identical multitasking behavior.

**Window Management**  
Take advantage of iPad's flexible window system to create apps that adapt to different sizes and configurations.

## What's New in iPadOS 26

Dive into the latest key technologies and capabilities:

- **Liquid Glass Design System**: Adaptive visual effects for larger displays
- **Apple Intelligence**: Advanced AI capabilities for productivity and creativity
- **Apple Pencil and input**: Preserve drawing and editing behavior across supported accessories
- **Windowing**: Adapt document and navigation layouts to changing geometry
- **Widgets and system actions**: Surface useful content outside the app
- **Accessibility**: Test keyboard access, text size, contrast, and alternative input

### iPadOS 26.1 Updates (November 2025)
- The [26.1 notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-26_1-release-notes) correct `UIDocument`'s erroneous main-actor-only annotation; affected Swift code can produce new diagnostics.
- The same notes fix local asset-file URL lookup and a back-deployed `navigationLinkIndicatorVisibility` crash, with an SDK rebuild required for the latter.

### iPadOS 26.2 Updates
- **Hypertension Notifications API**: Authorize `HKCategoryTypeIdentifierHypertensionEvent` to read hypertension notifications from Apple Watch
- **StoreKit `AppStore.ageRatingCode`**: Fetch the current age rating code for your app to detect rating changes
- **DeclaredAgeRange fixes**: Recompile against the 26.2 SDK for the affected eligibility/declaration symbols enumerated in issue 165248390, not as a universal remedy for age-range errors

### iPadOS 26.3 Updates
- **StoreKit fix**: Corrects a defect that made `Product.products(for:)` fail silently instead of throwing an error

### iPadOS 26.4 Updates
- **Memory Integrity Enforcement (MIE)**: The 26.4 notes add opt-in full protections, previously limited to Soft Mode; check hardware and build-setting requirements
- **Background Assets offline APIs**: Query available local status information and request the latest local asset-pack version; some status information still requires a connection
- **StoreKit revocation fields**: New `Transaction.revocationType` and `Transaction.revocationPercentage` properties
- **AudioAccessoryKit (developer testing)**: The 26.4 notes describe automatic-audio-switching integration and a future EU customer rollout, not worldwide availability
- **SwiftUI fix**: `.userActivity` now correctly surfaces as the current user activity
- **Networking fix**: Resolves `CFRunLoopSource` leaks when PAC or Auto proxy discovery is configured

### iPadOS 26.5 through 26.6.2
- Keep the [26.5](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-26_5-release-notes) and [26.6](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-26_6-release-notes) notes for version-specific diagnosis
- **iPadOS 26.6.2 (September 8, 2026)** is the shipping maintenance baseline
- [Apple's security release list](https://support.apple.com/en-us/100100) describes patch scope separately from SDK changes

### Preparing an OS26 App for OS27

- Adopt the [UIKit scene life cycle](https://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle) before a 27-SDK rebuild. Multiple-window support is optional, but scenes are required to launch.
- Audit external-display scene registration, menu image visibility, document I/O, and ODR-to-Background-Assets migration using the [iPadOS 27 checklist](../os27-intro/iPadOS.md).
- Finish UI adaptation: [`UIDesignRequiresCompatibility`](https://developer.apple.com/documentation/bundleresources/information-property-list/uidesignrequirescompatibility) is ignored by builds for iPadOS 27 or later.
- Keep SiriKit legacy support while adding modern App Intents integrations. Do not raise the deployment floor based on an unverified hardware-drop claim.
- Xcode 27 beta 6 requires **Apple silicon and macOS Tahoe 26.4 or later**, not macOS 27. The current [submission SDK requirement](../guides/app-store-readiness.md) is separate from the OS versions your app supports.

## Getting Started

**New to iPadOS development?**  
Check out the [iPadOS Pathway](https://developer.apple.com/ipados/get-started/), a collection of resources to get started with iPad app development.

## Developer Success Stories

### The reign of Carrot Weather
[Apple's Carrot Weather profile](https://developer.apple.com/news/?id=kf623ldf) explains how Brian Mueller combines weather information with the app's distinctive personality.

### The long history of Goodnotes
[Apple's Goodnotes profile](https://developer.apple.com/articles/goodnotes/) traces its development on iPad and adoption of Apple Pencil.

### Powering up Procreate
[Apple's Procreate story](https://developer.apple.com/news/?id=e409h6ja) describes motion filtering and Pencil stroke smoothing as examples of making drawing more accessible.

## Resources

### Development Tools
- [Xcode](https://developer.apple.com/xcode/) - Complete development environment with iPad simulators
- [TestFlight](https://developer.apple.com/testflight/) - Beta testing platform for iPad apps
- [App Store Connect](https://developer.apple.com/app-store-connect/) - App management and analytics

### Documentation
- [UIKit Documentation](https://developer.apple.com/documentation/uikit)
- [PencilKit Documentation](https://developer.apple.com/documentation/pencilkit/)
- [Multitasking on iPad](https://developer.apple.com/design/human-interface-guidelines/multitasking/)

### Related Platforms
Build apps that integrate seamlessly across all Apple platforms:
- [iOS](iOS.md) - Mobile experiences
- [macOS](macOS.md) - Desktop and laptop applications  
- [tvOS](tvOS.md) - Living room entertainment
- [visionOS](visionOS.md) - Spatial computing
- [watchOS](watchOS.md) - Wearable experiences

## Support

### Meet with Apple
Sharpen your skills through in-person and online activities around the world. Connect with Apple engineers and designers to optimize your iPad experiences.

### Apple Developer Program
Join the [Apple Developer Program](Program.md) for TestFlight, App Store distribution, and capabilities that require membership. Developer beta access is a separate account benefit.

---

*Platform requirements and feature availability may vary. Some capabilities and services may not be available in all regions or all languages.*

## Sources

[Designing for iPadOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados), [Liquid Glass adoption](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass), and [SystemLanguageModel](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel) support the platform guidance. [Apple Developer releases](https://developer.apple.com/news/releases/), [26.2 notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-26_2-release-notes), [26.4 notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-26_4-release-notes), [iOS/iPadOS 27 notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes), [SiriKit](https://developer.apple.com/documentation/sirikit), and [Xcode 27 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes) support the status and migration guidance checked September 8, 2026. Inline story sources describe historical examples.
