# visionOS 27.0 Developer Introduction

visionOS 27 continues to build out spatial computing on Apple Vision Pro, extending the generation's design refinements and rebuilt Siri into an environment where interface materials are composited against the real world.

**Platform:** visionOS 27.0+

> **Status:** visionOS 27 is in developer beta as of August 2026 (developer beta 1 on June 8, 2026). A public release is expected in fall 2026. Apple has not announced a release date. The current shipping line is visionOS 26.6, released July 27, 2026.

## Overview

Liquid Glass originated as a spatial material, so visionOS is where the generation's refinements are most native. The rebuilt Siri reaches Apple Vision Pro with conversation sync through the standalone Siri app, and RealityKit and Compositor Services continue as the primary surfaces for immersive content.

## Key Features

### Design

The generation's material refinements — improved diffusion of busy content, a darkened edge ring for separation, brighter specular highlights — apply to visionOS windows and ornaments. In a passthrough environment the background is the real world, uncontrolled and constantly changing, so validate legibility across bright, dark, and high-motion surroundings rather than a fixed test scene.

### Siri AI

Siri on Apple Vision Pro is rebuilt on Apple Foundation Models, with conversations synced through the standalone Siri app across iPhone, iPad, Mac, and Apple Watch.

### Spatial Frameworks

RealityKit and Compositor Services remain the primary paths for immersive and mixed-immersion experiences. See [RealityKit](../documentation/RealityKit.md) and [CompositorServices](../documentation/CompositorServices.md).

> **Note:** Apple's WWDC 2026 visionOS 27 announcements were less detailed publicly than those for iOS and macOS. Confirm specifics against the [visionOS release notes](https://developer.apple.com/documentation/visionos-release-notes) before depending on any individual feature.

## What's New in visionOS 27

- **Liquid Glass refinements** applied to windows and ornaments
- **Siri AI**: rebuilt with cross-device conversation sync
- **App Intents** entity and intent schemas, including the View Annotations API
- Continued RealityKit and Compositor Services investment

## Device Support

visionOS 27 supports Apple Vision Pro. Confirm the supported model list against Apple's official visionOS page.

## Migrating to visionOS 27

**Appearance follows the linked SDK.** Rebuilding with Xcode 27 adopts the refined appearance.

**Re-test against real environments.** Passthrough makes material legibility environment-dependent in a way no other Apple platform is. Test in a bright room, a dark room, and against moving backgrounds.

**Respect accessibility settings.** Reduce Transparency, Increase Contrast, and Reduce Motion have outsized importance in an immersive context.

**SiriKit is deprecated.** Migrate to App Intents.

## Getting Started

**New to spatial computing?**
Check out the [visionOS Pathway](https://developer.apple.com/visionos/) for resources on building spatial apps.

## Resources

### Development Tools
- [Xcode](https://developer.apple.com/xcode/) - Xcode 27 requires macOS 27 Golden Gate on Apple silicon
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

*Reviewed 2026-08-09. visionOS 27 is pre-release software; features and availability may change before general release. Platform requirements and feature availability may vary, and some capabilities may not be available in all regions or languages.*
