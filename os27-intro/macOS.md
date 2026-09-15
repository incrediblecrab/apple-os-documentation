# macOS Golden Gate 27.0 Developer Introduction

Prepare Mac apps for macOS Golden Gate 27 by reviewing AppKit behavior, document handling, installer architecture, and Intel-only dependencies. Keep the development Mac's requirements separate from the architectures and older OS releases your app supports.

**Platform:** macOS Golden Gate 27.0+

> **Status checked September 14, 2026:** macOS 27 Golden Gate 27.0 (`26A428`) shipped September 14. The previous 26-generation release is **macOS Tahoe 26.6.2** (`25G83`), released August 17.

## Overview

The [macOS 27 release notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes) document changes that affect existing apps, not just new features. Test a shipping build on the new OS and a newly linked build separately. Continue testing Tahoe and other supported deployment targets instead of treating SDK adoption as an automatic deployment-floor increase.

## Toolchain and Architecture

### Xcode 27

Released September 14, **Xcode 27 (`27A266a`) requires an Apple silicon Mac running macOS Tahoe 26.6 or later** and includes Swift 6.4 and the 27 SDKs. **It does not require macOS 27.** The [Xcode notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes) explicitly exclude Intel Macs as hosts, while allowing the macOS 27 SDK to build universal Intel/Apple-silicon apps that back-deploy to macOS 12 or later.

For CI, verify the runner architecture, host OS, selected Xcode, SDK, deployment target, and architectures of build-time tools independently. Running an Intel executable through Rosetta on an Apple silicon host does not make an Intel Mac eligible to run Xcode 27.

For a minimum macOS deployment target of 27 or later, `ARCHS_STANDARD` no longer includes `x86_64`. The notes allow an explicit `ARCHS` setting to add it; default build architectures and OS installation eligibility are different questions (161837535).

### Rosetta and installers

The macOS notes document these migration considerations:

- An upgrade to macOS 27 does not automatically restore a prior Rosetta installation.
- Apps previously configured to “Open using Rosetta” launch natively; reassess the compatibility problem that required translation.
- Installer packages without `hostArchitecture` default to `arm64`. Check pre/post-install scripts and installer plug-ins on Apple silicon.
- Intel plug-ins and loaders may not appear in the system's incompatibility warnings. Audit bundled helpers and dependencies rather than relying on that list.
- Apple states that Intel-based software will not be compatible with macOS 28, excluding legacy games. This is a documented future migration direction, not a claim that all Intel apps are already unusable on macOS 27.

**Exact macOS 27 model list: not verified by the sources reviewed here.** The Xcode host architecture requirement is verified; it is not evidence that every Mac with a particular chip can install every OS release. Check OS installation eligibility separately.

## Developer-Facing Changes

### AppKit and Mac Catalyst

- **Menus:** linked-SDK behavior changes image visibility. For apps linked with the macOS 27 SDK, both symbol and non-symbol images can be hidden automatically, including image-only items. Use `NSMenuItem.preferredImageVisibility` where needed and verify accessible names.
- **Refresh and selection:** `NSRefreshController` adds pull-to-refresh support to `NSScrollView`; `NSTextSelectionManager` provides gesture-based selection handling. Test existing text-view subclasses rather than assuming every mouse override must be rewritten.
- **Semantic tabs:** toolbar groups and segmented controls gain roles, including tabs, improving the distinction between navigation and value selection.
- **Mac Catalyst:** switching to an app with no open windows no longer automatically creates a window unless activation comes through Dock or Spotlight. Test reopen and document commands.
- **UIKit life cycle:** Catalyst apps built with the latest SDK must adopt scenes or fail to launch on Mac Catalyst 27. This requirement does not turn native AppKit apps into UIKit scene apps. See [scene migration](https://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle).

### Documents, assets, and diagnostics

- SwiftUI adds asynchronous document reading/writing through `ReadableDocument`, `WritableDocument`, and `Document`; older `FileDocument`/`ReferenceFileDocument` APIs are deprecated. Test autosave, package documents, cancellation, and older-OS code paths.
- Background Assets adds localized asset packs. Keep offline and missing-asset behavior explicit.
- `DiskImageKit` provides Swift disk-image management APIs for use with Virtualization. Check the API's format and availability constraints instead of treating every disk-image workflow as supported.
- Unified Logging archives produced by 27 releases require macOS 26.2 or later to read. Upgrade diagnostic workstations as well as build runners.

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

**New to macOS development?**
Check out the [macOS Pathway](https://developer.apple.com/macos/get-started/) for resources on building Mac apps.

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

[Apple Developer releases](https://developer.apple.com/news/releases/), [macOS 27 notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes), and [Xcode 27 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes), with additional scoped citations above. Reviewed September 8, 2026; version-specific behavior, model eligibility, and future Rosetta scope should be rechecked before release.
