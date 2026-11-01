# macOS Golden Gate 27.0 Developer Introduction

Prepare Mac apps for macOS Golden Gate 27 by reviewing AppKit behavior, document handling, installer architecture, and Intel-only dependencies. Keep the development Mac's requirements separate from the architectures and older OS releases your app supports.

**Platform:** macOS Golden Gate 27.0+

> **Status checked September 14, 2026:** macOS 27 Golden Gate 27.0 (`26A428`) shipped September 14. **macOS Tahoe 26.7** also shipped September 14, 2026.

> **Update checked October 29, 2026:** [macOS Golden Gate 27.2](https://developer.apple.com/documentation/macos-release-notes/macos-27_2-release-notes) (`26B123`) shipped October 26, 2026, following 27.0.1 (`26A434`) on September 28, 2026. Tahoe 26.7.1 shipped September 28, 2026, and 26.7.2 on October 26, 2026. [Safari 27.2](https://developer.apple.com/documentation/safari-release-notes/safari-27_2-release-notes) (`20625.2.8`) shipped October 26, 2026 for macOS 27.2, macOS Tahoe 26, and macOS Sequoia.

## Overview

The [macOS 27 release notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes) document changes that affect existing apps, not just new features. Test a shipping build on the new OS and a newly linked build separately. Continue testing Tahoe and other supported deployment targets instead of treating SDK adoption as an automatic deployment-floor increase.

## Toolchain and Architecture

### Xcode 27

Released September 14, **Xcode 27 (`27A266a`) requires an Apple silicon Mac running macOS Tahoe 26.6 or later** and includes Swift 6.4 and the 27 SDKs. **It does not require macOS 27.** The [Xcode notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes) explicitly exclude Intel Macs as hosts, while allowing the macOS 27 SDK to build universal Intel/Apple-silicon apps that back-deploy to macOS 12 or later.

**October 29, 2026 update:** [Xcode 27.1](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes) (`27A9275`; October 15, 2026) still bundles the macOS 27 SDK, alongside the iOS 27.1 SDK. [Xcode 27.2](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes) provides 27.2 SDKs for all six platforms. Both retain Swift 6.4 and the macOS Tahoe 26.6 host minimum. The developer release feed checked November 1, 2026 lists the final Xcode 27.2 as `27B52`, dated October 29, 2026, the date Apple's security-release list also gives; the October 19, 2026 RC (`27B48`) it showed on October 29 no longer appears.

For CI, verify the runner architecture, host OS, selected Xcode, SDK, deployment target, and architectures of build-time tools independently. Running an Intel executable through Rosetta on an Apple silicon host does not make an Intel Mac eligible to run Xcode 27.

For a minimum macOS deployment target of 27 or later, `ARCHS_STANDARD` no longer includes `x86_64`. The notes allow an explicit `ARCHS` setting to add it; default build architectures and OS installation eligibility are different questions (161837535).

**Point-release build caveats:** In Xcode 27.1 and 27.2, Mac Catalyst builds using iOS 27.1-specific APIs fail to compile; isolate affected code with build-time conditionals (185924957). Xcode 27.2 incorrectly offers 27.1 as a deployment target for macOS, watchOS, tvOS, and visionOS; do not select it merely because it appears. Mac Catalyst builds targeting 27.1 or 27.2 may also be unable to use newly introduced APIs (187160501).

### Rosetta and installers

The macOS notes document these migration considerations:

- An upgrade to macOS 27 does not automatically restore a prior Rosetta installation.
- Apps previously configured to “Open using Rosetta” launch natively; reassess the compatibility problem that required translation.
- Installer packages without `hostArchitecture` default to `arm64`. Check pre/post-install scripts and installer plug-ins on Apple silicon.
- Intel plug-ins and loaders may not appear in the system's incompatibility warnings. Audit bundled helpers and dependencies rather than relying on that list.
- Apple states that Intel-based software will not be compatible with macOS 28, excluding legacy games. This is a documented future migration direction, not a claim that all Intel apps are already unusable on macOS 27.

**macOS 27 model availability:** Apple's [security-release list](https://support.apple.com/en-us/100100) names MacBook Neo (2026); Apple silicon models of MacBook Air, MacBook Pro, and Mac mini (2020 and later); Apple silicon iMac (2021 and later); Mac Studio (2022 and later); and Apple silicon Mac Pro (2023). This OS-support list is separate from Xcode's host requirements.

## Developer-Facing Changes

### AppKit and Mac Catalyst

- **Menus:** linked-SDK behavior changes image visibility. For apps linked with the macOS 27 SDK, both symbol and non-symbol images can be hidden automatically, including image-only items. Use `NSMenuItem.preferredImageVisibility` where needed and verify accessible names.
- **Refresh and selection:** `NSRefreshController` adds pull-to-refresh support to `NSScrollView`; `NSTextSelectionManager` provides gesture-based selection handling. Test existing text-view subclasses rather than assuming every mouse override must be rewritten.
- **Touch input:** a Mac can have a touch display. AppKit emulates mouse events from a single-finger tap or drag, so existing `mouseDown(with:)` overrides and tracking loops still run, but multi-finger gestures and individual `NSTouch` input reach an app only through gesture recognizers. `NSScreen.touchCapabilities` (macOS 27.0) reports whether a screen supports touch, and custom `NSGestureRecognizer` subclasses must now implement `locationInView:` themselves. See [Adopting gesture recognizers in your app](https://developer.apple.com/documentation/appkit/adopting-gesture-recognizers-in-your-app); a Sidecar-connected iPad lets you test touch without that hardware.
- **Semantic tabs:** toolbar groups and segmented controls gain roles, including tabs, improving the distinction between navigation and value selection.
- **Mac Catalyst:** switching to an app with no open windows no longer automatically creates a window unless activation comes through Dock or Spotlight. Test reopen and document commands.
- **UIKit life cycle:** Catalyst apps built with the latest SDK must adopt scenes or fail to launch on Mac Catalyst 27. This requirement does not turn native AppKit apps into UIKit scene apps. See [scene migration](https://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle).

### Documents, assets, and diagnostics

- SwiftUI adds asynchronous document reading/writing through `ReadableDocument`, `WritableDocument`, and `Document` from macOS 27.0. The release notes deprecate `FileDocument` and `ReferenceFileDocument`, but the current [`ReferenceFileDocument`](https://developer.apple.com/documentation/swiftui/referencefiledocument) metadata dates its macOS deprecation to 27.2; it remains available. Test autosave, package documents, cancellation, and older-OS code paths.
- Background Assets adds localized asset packs. Keep offline and missing-asset behavior explicit.
- `DiskImageKit` provides Swift disk-image management APIs for use with Virtualization. Check the API's format and availability constraints instead of treating every disk-image workflow as supported.
- Unified Logging archives produced by 27.0 releases require macOS 26.2 or later to read. Upgrade diagnostic workstations as well as build runners.

### Intelligence and security

- Audit App Intents schema changes and preserve [SiriKit's documented legacy support](https://developer.apple.com/documentation/sirikit). App Intents is the route for modern Siri and Apple Intelligence integration.
- Foundation Models' PCC access has separate entitlement, eligibility, availability, and error handling; see the [PCC guide](../guides/private-cloud-compute.md).
- Selected system connections used for MDM/DDM, enrollment, profiles, app installation, and software updates require TLS 1.2 or later with ATS-compliant certificates and ciphers. Use Apple's [network audit guidance](https://support.apple.com/en-us/126655), including its SCEP and content-caching exceptions; don't generalize this to all app networking.

## Migration Checklist

1. Move Xcode 27 build jobs to eligible Apple silicon runners on Tahoe 26.6 or later; validate native build tools before switching production CI.
2. Decide deliberately whether universal binaries and older deployment targets remain necessary. Replace Intel-only dependencies without dropping users merely because the SDK changed.
3. Finish UI work instead of relying on [`UIDesignRequiresCompatibility`](https://developer.apple.com/documentation/bundleresources/information-property-list/uidesignrequirescompatibility), which is ignored when building for macOS 27 or later. Test menu visibility, keyboard focus, window restoration, and accessibility.
4. Re-test corrected pre-release failures. For example, the 27 notes list Accessory Access sandbox/VM issues as resolved; those are not permanent framework limitations.
5. Check [App Store readiness](../guides/app-store-readiness.md) separately from SDK migration. App Store and Developer ID distribution have different workflows.

## Getting Started

**New to macOS development?** Check out the [macOS Pathway](https://developer.apple.com/macos/get-started/) for resources on building Mac apps.

## Resources

### Development Tools
- [Xcode](https://developer.apple.com/xcode/) - Xcode 27: Apple silicon, macOS Tahoe 26.6 or later
- [TestFlight](https://developer.apple.com/testflight/) - Beta testing platform
- [App Store Connect](https://developer.apple.com/app-store-connect/) - App management and analytics

### Documentation
- [macOS Release Notes](https://developer.apple.com/documentation/macos-release-notes)
- [AppKit Documentation](https://developer.apple.com/documentation/appkit/)
- [Apple Silicon](../documentation/apple-silicon.md)
- [Metal Documentation](https://developer.apple.com/documentation/metal/)

### Related Platforms
- [iOS](iOS.md) - iPhone experiences
- [iPadOS](iPadOS.md) - Enhanced tablet experiences
- [tvOS](tvOS.md) - Living room entertainment
- [visionOS](visionOS.md) - Spatial computing
- [watchOS](watchOS.md) - Wearable experiences
- [Apple Developer Program](Program.md) - Membership, distribution, and policy

### Distribution Options
- **Mac App Store**: worldwide reach with built-in discovery and payment processing
- **Developer ID**: distribute outside the Mac App Store with notarization

### Previous Generation
- [macOS Tahoe 26 Developer Introduction](../os26-intro/macOS.md)

---

## Sources

[Apple Developer releases](https://developer.apple.com/news/releases/), [release feed](https://developer.apple.com/news/releases/rss/releases.rss), [Apple security releases](https://support.apple.com/en-us/100100), [macOS 27 notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes), [macOS 27.2 notes](https://developer.apple.com/documentation/macos-release-notes/macos-27_2-release-notes), [Xcode 27 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes), [Xcode 27.1 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes), [Xcode 27.2 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes), [Safari 27.2 notes](https://developer.apple.com/documentation/safari-release-notes/safari-27_2-release-notes), and [`ReferenceFileDocument`](https://developer.apple.com/documentation/swiftui/referencefiledocument), with additional scoped citations above. Reviewed September 8, 2026; full-body review updated October 29, 2026 and November 1, 2026. Version-specific behavior, model eligibility, and future Rosetta scope should be rechecked before release.
