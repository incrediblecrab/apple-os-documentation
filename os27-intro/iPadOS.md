# iPadOS 27.0 Developer Introduction

Prepare document, drawing, and productivity apps for iPadOS 27 by testing scene restoration, flexible window sizes, external displays, and the new document APIs. Treat SDK adoption separately from the decision to keep supporting older iPads.

**Platform:** iPadOS 27.0+

> **Status checked September 14, 2026:** iPadOS 27.0 (`24A437`) shipped September 14. The previous 26-generation release is **iPadOS 26.7** (`23H24`), released September 9.

## Overview

iPadOS 26's windowing and Liquid Glass work remains relevant. The 27 SDK adds concrete changes to how apps restore scenes, supply external-display content, read and write documents, and present menus. Use the [iOS & iPadOS 27 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes) to distinguish new behavior from resolved pre-release regressions.

## Developer-Facing Changes

### Scenes and external displays

- UIKit apps built with the latest SDK must adopt the **scene-based life cycle** or fail to launch on iPadOS 27. A single-window app still needs scenes; multiple-window support is optional.
- `UIScene.extendStateRestoration` and `completeStateRestoration` allow restoration to span background-to-foreground transitions. Keep restoration state associated with its scene, not one global window.
- For apps built with the iOS 27 SDK, the system no longer automatically offers `windowExternalDisplayNonInteractive` scenes. Register a `UISceneAccessory.externalNonInteractive` through `UIViewController.registerSceneAccessory(_:)` when you need that role.
- Test resizing, rotation, scene reconnection, and disconnecting an external display. The 27 notes list several earlier `UIRequiresFullScreen`, orientation, and `UIScreen` problems as resolved; those bugs are not permanent windowing rules.

See [UIKit scene migration](https://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle) for the configuration and life-cycle responsibilities.

### Documents, menus, and input

- SwiftUI's `ReadableDocument`, `WritableDocument`, and combined `Document` protocol support asynchronous document operations. Updated `DocumentGroup` APIs expose progress reporting and URL access, but the 27 notes list a known issue where read/write progress might not be presented (158441261). `FileDocument` and `ReferenceFileDocument` are deprecated, not removed; retain appropriate code paths for older deployment targets.
- Menu bars and context menus use fewer images by default. Set `UIMenuElement.preferredImageVisibility` deliberately where an image communicates something essential; don't rely on every supplied icon remaining visible.
- Re-test custom gestures on selectable SwiftUI `Text`, which gains system selection interactions when linked with the 27 SDK.
- PencilKit renames `__PKStrokeRenderState` to `PKStrokeRenderStateReference`, replacing the earlier Objective-C render-state conversion path. Audit code that uses those APIs rather than assuming all PencilKit drawing code needs replacement.

### Assets, background work, and intelligence

- Background Assets adds localized asset packs, while On Demand Resources and `NSBundleResourceRequest` are deprecated. Handle offline availability and storage pressure in document-template, media, and model downloads.
- Leaving an app or locking an iPad is **not a guarantee of unlimited background execution**. Use the appropriate transfer or background-task API, expose progress, and handle expiration, interruption, and retry.
- App Intents schema changes include the `calendar.deleteEvent` rename and additional `.photos.asset` conformance requirements. Test actual intent invocation and entity resolution.
- [SiriKit](https://developer.apple.com/documentation/sirikit) retains legacy support for Shortcuts, widget configuration, and most existing Siri interactions. Adopt App Intents for modern Siri/Apple Intelligence integration rather than describing all SiriKit APIs as deprecated.
- [Private Cloud Compute](../guides/private-cloud-compute.md) access through Foundation Models is gated by developer eligibility, entitlement, and runtime availability. It is not automatically enabled by installing iPadOS 27.

## Migration Checklist

1. Migrate scene handling and ensure the app declares a launch screen before submitting a 27-SDK build.
2. Remove dependence on [`UIDesignRequiresCompatibility`](https://developer.apple.com/documentation/bundleresources/information-property-list/uidesignrequirescompatibility): the system ignores it for builds targeting the iPadOS 27 SDK or later. Test toolbars, sidebars, keyboard focus, and accessibility settings.
3. Test document read/write failures, conflicting changes, cancellation, and restoration after termination; asynchronous I/O does not remove these responsibilities.
4. Audit system-managed installation and enrollment servers for the [stricter TLS requirements](https://support.apple.com/en-us/126655). Their scope is selected system processes, not every app connection.
5. Keep your shipping iPadOS 26 test matrix while adding iPadOS 27.0 tests. Do not raise deployment targets based on an unverified device list.

## Devices and Toolchain

**Exact iPadOS 27 device list: not verified by the sources reviewed here.** This page does not claim that all A12-class iPads are dropped or that any particular iPad has reached its final OS release. Hardware requirements for Apple Intelligence, Pencil features, and external displays must be checked separately.

**Xcode 27** (`27A266a`), released September 14, requires **an Apple silicon Mac running macOS Tahoe 26.6 or later**, not macOS 27. It includes Swift 6.4 and the 27 SDKs. Intel-host eligibility is separate from Rosetta's ability to run Intel apps on Apple silicon. See the [Xcode release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes).

Since April 28, 2026, uploads require Xcode 26 or later and the iPadOS 26 SDK or later; deployment targets can be older. The checked [Upcoming Requirements](https://developer.apple.com/news/upcoming-requirements/) page gives no OS 27 SDK deadline. See [App Store readiness](../guides/app-store-readiness.md).

## Getting Started

**New to iPad development?**
Check out the [iPadOS Pathway](https://developer.apple.com/ipados/get-started/) for resources on building iPad apps.

## Resources

### Development Tools
- [Xcode](https://developer.apple.com/xcode/) - See the version-specific host requirements above
- [TestFlight](https://developer.apple.com/testflight/) - Beta testing platform
- [App Store Connect](https://developer.apple.com/app-store-connect/) - App management and analytics

### Documentation
- [UIKit Documentation](https://developer.apple.com/documentation/uikit)
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

## Sources

[Apple Developer releases](https://developer.apple.com/news/releases/), [iOS/iPadOS 27 notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes), and [Xcode 27 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes), with additional scoped citations above. Reviewed September 8, 2026; version-specific changes and hardware/feature eligibility must be rechecked before release.
