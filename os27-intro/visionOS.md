# visionOS 27.0 Developer Introduction

Prepare spatial apps for visionOS 27 by reviewing scene life cycles, asset delivery, document handling, and beta-specific rendering or streaming regressions. Retain the distinction between native spatial apps and compatible iPhone/iPad apps.

**Platform:** visionOS 27.0+

> **Status checked September 8, 2026:** visionOS 27 **beta 8** (`24M5361a`) was released August 31. The shipping release is **visionOS 26.6.1** (`23O780`), released August 17. The [release listings](https://developer.apple.com/news/releases/) establish neither a public-beta program nor a general-availability date.

## Overview

Windows, volumes, immersive spaces, RealityKit, and Compositor Services remain the foundation of spatial apps. The [visionOS 27 beta 8 notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-27-release-notes) add specific migration work; they should not be replaced by assumptions that every iOS design or Siri feature has identical visionOS availability.

## Developer-Facing Changes

### Scenes, documents, and assets

- **UIKit life cycle:** apps built with the latest SDK must adopt scenes or fail to launch on visionOS 27. `UIScene.extendStateRestoration` and `completeStateRestoration` extend restoration across background-to-foreground transitions. See [UIKit scene migration](https://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle).
- **Documents:** SwiftUI's `ReadableDocument`, `WritableDocument`, and combined `Document` protocol support asynchronous document operations. Review migration from `FileDocument`/`ReferenceFileDocument` and test cancellation, save failures, and restoration.
- **Background Assets:** localized asset packs help deliver the appropriate language resources. On Demand Resources and `NSBundleResourceRequest` are deprecated. Keep a usable window-based experience if optional spatial content has not downloaded.
- **PhotoKit:** the nullable `PHAssetResource.filename` replaces the incorrectly non-nullable `originalFilename`. Handle a missing filename in import/export interfaces.

### Spatial interaction and rendering

- The notes describe activating Siri by looking at its orb and speaking, enabled from beta 2. This is a system interaction, not an entitlement to unrestricted eye-tracking data in your app.
- VideoToolbox adds a queryable 1.5× low-latency super-resolution option and broader source-dimension support for low-latency frame interpolation. Check supported configurations before offering a processing mode.
- Test permissions, tracking loss, immersive-space transitions, remote disconnection, and recovery. Beta 8 marks the earlier `RemoteImmersiveSpace` device-discovery failure as **resolved**; it is not a permanent Compositor Services restriction.
- Check SwiftUI `@State` initializer changes and `AsyncImage` HTTP caching when rebuilding. A successful compile does not validate spatial layout or comfortable interaction.

### Intelligence and managed deployment

- App Intents schema changes need availability-aware migration. [SiriKit](https://developer.apple.com/documentation/sirikit) continues legacy support for Shortcuts, widget configuration, and most existing Siri interactions; modern integrations use App Intents.
- Foundation Models' PCC access requires separate developer approval and runtime eligibility. See [PCC privacy, permissions, and fallback handling](../guides/private-cloud-compute.md).
- For managed devices, audit the selected system connections used for enrollment, MDM/DDM, profiles, app installation, and updates against the [stricter TLS requirements](https://support.apple.com/en-us/126655). Retain Apple's documented exceptions instead of applying the rule to every connection.

## Migration and Testing

1. Run your shipping binary and a 27-SDK rebuild separately, including any compatible iPad/iPhone app path you distribute.
2. Test windows, ornaments, and text against varied real surroundings. Verify accessibility and comfort on hardware, not only in Simulator.
3. Keep beta workarounds scoped to the affected build. A resolved ARKit, RealityKit, or streaming issue is a regression-test case, not a reason to document an API as unsupported.
4. In **Xcode 27 beta 6**, Device Hub does not support viewing video from or sending input to a physical Vision Pro; other Device Hub features remain available. Apple suggests AirPlay for remote viewing. This is a tool-version limitation, not a visionOS app capability limit.

## Devices and Toolchain

**Exact visionOS 27 Vision Pro model list: not verified by the reviewed release sources.** Do not extrapolate the visionOS 26 model list or assume every sensor, streaming, or intelligence feature is available to every app.

**Xcode 27 beta 6**, released August 24, requires **an Apple silicon Mac running macOS Tahoe 26.4 or later**, not macOS 27. Intel Macs cannot host it, regardless of Rosetta support for running Intel apps on Apple silicon. The [Xcode notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes) cover both host requirements and Device Hub limitations.

Since April 28, 2026, visionOS uploads require Xcode 26 or later and the visionOS 26 SDK or later. The checked [requirements page](https://developer.apple.com/news/upcoming-requirements/) gives no OS 27 SDK deadline. See [App Store readiness](../guides/app-store-readiness.md).

## Getting Started

**New to spatial computing?**
Check out the [visionOS Pathway](https://developer.apple.com/visionos/get-started/) for resources on building spatial apps.

## Resources

### Development Tools
- [Xcode](https://developer.apple.com/xcode/) - See the version-specific host requirements above
- [Reality Composer Pro](https://developer.apple.com/augmented-reality/tools/) - Author 3D content
- [TestFlight](https://developer.apple.com/testflight/) - Beta testing platform

### Documentation
- [visionOS Developer Documentation](https://developer.apple.com/documentation/visionos/)
- [Designing for visionOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos)
- [RealityKit](../documentation/RealityKit.md)
- [CompositorServices](../documentation/CompositorServices.md)

### Related Platforms
- [iOS](iOS.md) - iPhone experiences
- [iPadOS](iPadOS.md) - Enhanced tablet experiences
- [macOS](macOS.md) - macOS Golden Gate 27
- [tvOS](tvOS.md) - Living room entertainment
- [watchOS](watchOS.md) - Wearable experiences
- [Apple Developer Program](Program.md) - Membership, distribution, and policy

### Previous Generation
- [visionOS 26 Developer Introduction](../os26-intro/visionOS.md)

---

## Sources

[Apple Developer releases](https://developer.apple.com/news/releases/), [visionOS 27 beta 8 notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-27-release-notes), and [Xcode 27 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes), with additional scoped citations above. Reviewed September 8, 2026; hardware eligibility, permissions, and beta behavior must be checked separately.
