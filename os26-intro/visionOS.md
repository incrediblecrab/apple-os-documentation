# visionOS 26.0 Developer Introduction

Maintain spatial apps with SwiftUI windows and volumes, RealityKit content, and appropriately authorized ARKit data. Preserve useful window-based behavior when immersive content, tracking, or a network service is unavailable.

**Platform:** visionOS 26.0+

> **Status checked September 8, 2026:** the shipping release is **visionOS 26.6.1** (`23O780`), released August 17. visionOS 27 beta 8 was released August 31; see the [visionOS 27 introduction](../os27-intro/visionOS.md). Release listings do not establish a public-beta program or general-availability date.

## Overview

The OS26 generation adds spatial widget and interaction capabilities while retaining the earlier windows/volumes/immersive-spaces model. Treat device support, sensor permissions, and the choice between a native spatial app and a compatible iPad app as separate decisions.

## Key Features

### Spatial Computing

**A spectrum of immersion**  
Create experiences that range from familiar app windows to fully immersive environments. Transition smoothly between different levels of immersion based on user intent and context.

**3D Interface Design**  
Design interfaces that exist in three-dimensional space, allowing users to interact with content naturally using their eyes, hands, and voice.

**Spatial Positioning**  
Support scene restoration for windows and volumes that people place in their surroundings. Apple documents snapping, locking, and persistence in Shared and mixed immersive spaces, not full or progressive immersive spaces. Handle changed surroundings and unavailable restoration state.

### Development Frameworks

**SwiftUI for visionOS**  
Build beautiful, compelling apps using familiar SwiftUI patterns enhanced for spatial computing. Choose appropriate window, volume, and immersive-space presentations and test the transitions between them; the framework does not design those experiences for you.

**RealityKit Integration**  
Add depth and dimension to your applications with RealityKit. Create realistic 3D content, lighting, and physics that respond naturally to the user's environment.

**ARKit Capabilities**  
Understand your surroundings with advanced ARKit features. Access world tracking, plane detection, and occlusion to create spatially-aware experiences.

### User Interaction

**System gaze and hand interaction**

Use system-managed look-and-pinch selection and standard gestures. A gaze-driven interface does not give an app unrestricted raw eye-tracking data; request only the ARKit data your feature needs and handle denial or tracking loss.

**Voice Integration**  
Expose supported Siri actions and preserve accessible controls as an alternative to voice input.

**Accessibility Excellence**  
Use the system accessibility support and test VoiceOver and Switch Control. Custom spatial content still needs appropriate labels, actions, and interaction design.

### Advanced Capabilities

**Immersive Environments**  
Transport users to entirely new worlds with full immersion experiences. Create environments that replace the user's surroundings for gaming, entertainment, and specialized applications.

**Shared Experiences**  
Use supported SharePlay and Group Activities features for shared experiences. Handle participants joining or leaving and session/network failures.

**Passthrough Integration**  
Let the system composite your spatial content with passthrough. Ordinary rendering does not give an app raw camera access; camera-data APIs have separate authorization and entitlement requirements.

## What's New in visionOS 26.0

Dive into the latest key technologies and capabilities:

- **Spatial widgets**: Add glanceable content using WidgetKit's supported spatial presentations
- **Hand tracking**: The 26.0 notes change the sensitivity of hand-joint `isTracked`; a plausible transform may still be available when the joint is occluded. Choose handling appropriate to accuracy-critical work versus custom gestures
- **SwiftUI controls**: Review sizing and interaction behavior when linking against the new SDK
- **Spatial content**: Test RealityKit scenes, shared experiences, and media in real surroundings
- **Accessibility and comfort**: Check standard interaction, readable content, and immersive transitions rather than assuming every mobile design treatment transfers unchanged

These are selected adoption areas from the [visionOS 26 notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-26-release-notes), not a claim that all spatial capabilities first appeared in OS26.

### visionOS 26.1 Updates (November 2025)
- The [26.1 notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-26_1-release-notes) fix local asset-file URL lookup and Game Controller input timestamps.
- They also fix a back-deployed `navigationLinkIndicatorVisibility` crash when rebuilt with the 26.1 SDK.

### visionOS 26.2 Updates
- The [26.2 notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-26_2-release-notes) add `AppStore.ageRatingCode` for reading the app's current rating and fix specific StoreKit subscription-testing/status issues

### visionOS 26.3 Updates
- The [26.3 notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-26_3-release-notes) fix a defect that made `Product.products(for:)` fail silently instead of throwing an error

### visionOS 26.4 Updates
- **Foveated Streaming with NVIDIA CloudXR**: Stream high-resolution, low-latency immersive content to Vision Pro using foveated streaming via the new [`FoveatedStreaming`](https://developer.apple.com/documentation/foveatedstreaming) framework
- **Background Assets offline APIs**: Query available local status and request the latest local asset-pack version; not all status information is available offline
- **StoreKit revocation fields**: New `Transaction.revocationType` and `Transaction.revocationPercentage` properties
- **SwiftUI fix**: `.userActivity` now correctly surfaces as the current user activity
- **Networking fix**: Resolves `CFRunLoopSource` leaks when PAC or Auto proxy discovery is configured

### visionOS 26.5 through 26.6.1
- Keep the [26.5](https://developer.apple.com/documentation/visionos-release-notes/visionos-26_5-release-notes) and [26.6](https://developer.apple.com/documentation/visionos-release-notes/visionos-26_6-release-notes) notes for version-specific behavior
- **visionOS 26.6.1 (August 17, 2026)** is the shipping maintenance baseline
- Check [security-update details](https://support.apple.com/en-us/100100) separately from the SDK feature list

### Preparing an OS26 App for OS27

- UIKit-based apps built with the latest SDK must adopt [scenes](https://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle) or fail to launch on visionOS 27.
- Audit ODR-to-Background-Assets migration, asynchronous SwiftUI document handling, and managed-service TLS using the [visionOS 27 checklist](../os27-intro/visionOS.md).
- Re-test spatial and streaming fixes against beta 8 rather than carrying resolved issues forward as permanent limitations. The exact OS27 hardware list is not verified here.
- Xcode 27 beta 6 needs **Apple silicon and macOS Tahoe 26.4 or later**, not macOS 27. Keep native and compatible-app tests, and check [submission requirements](../guides/app-store-readiness.md) separately.

## Getting Started

**New to visionOS development?**  
Check out the [visionOS Pathway](https://developer.apple.com/visionos/get-started/), a collection of resources to get started with spatial computing development.

### Development Tools

**Xcode for visionOS**  
Visualize and build spatial applications with enhanced Xcode support including visionOS simulators and spatial debugging tools.

**Reality Composer Pro**  
Create 3D content for your apps with Reality Composer Pro. Design scenes, import 3D models, and configure materials and lighting without writing code.

**Unity Integration**  
Bring existing Unity projects to visionOS or create new spatial experiences using familiar Unity workflows and tools.

## Developer Success Stories

### Blackbox
[Apple's 2024 Design Awards](https://developer.apple.com/design/awards/2024/) describe Blackbox's transition from screen-based puzzles to spatial interactions on Apple Vision Pro.

### Super Fruit Ninja
[Apple's Halfbrick interview](https://developer.apple.com/news/?id=455tez3y) describes Super Fruit Ninja's hand-based interactions and spatial game design.

### djay
[Apple's 2024 Design Awards](https://developer.apple.com/design/awards/2024/) describe djay's spatial turntables, effects controls, and immersive environments.

## Resources

### Development Tools
- [Xcode](https://developer.apple.com/xcode/) - Complete development environment with visionOS simulators
- [Reality Composer Pro](https://developer.apple.com/augmented-reality/tools/) - 3D content creation and scene design
- [TestFlight](https://developer.apple.com/testflight/) - Beta testing platform for visionOS apps

### Documentation
- [visionOS Developer Documentation](https://developer.apple.com/documentation/visionos/)
- [RealityKit Documentation](https://developer.apple.com/documentation/realitykit/)
- [ARKit Documentation](https://developer.apple.com/documentation/arkit/)
- [Designing for visionOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos)

### Related Platforms
Build apps that integrate seamlessly across all Apple platforms:
- [iOS](iOS.md) - Mobile companion experiences
- [iPadOS](iPadOS.md) - Enhanced tablet experiences
- [macOS](macOS.md) - Desktop development and content creation
- [tvOS](tvOS.md) - Living room entertainment
- [watchOS](watchOS.md) - Wearable integration

## Support

### Meet with Apple
Sharpen your skills through in-person and online activities around the world. Connect with Apple engineers and designers to create groundbreaking spatial computing experiences.

### Apple Developer Program
Join the [Apple Developer Program](Program.md) for TestFlight, App Store distribution for Apple Vision Pro, and capabilities that require membership. A developer beta is not evidence of a public-beta program.

### Design Principles
- **Spatial Interface Guidelines**: Best practices for designing in three-dimensional space
- **Immersion Patterns**: Effective transitions between different levels of immersion
- **Accessibility in Spatial Computing**: Creating inclusive experiences for all users

---

*Platform requirements and feature availability may vary. Apple Vision Pro availability varies by region. Some capabilities may require specific hardware features.*

## Sources

[Apple's visionOS overview](https://developer.apple.com/visionos/), [Designing for visionOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos), [persistent UI](https://developer.apple.com/documentation/visionos/adopting-best-practices-for-scene-restoration), [privacy](https://developer.apple.com/documentation/visionos/adopting-best-practices-for-privacy), and [main-camera access](https://developer.apple.com/documentation/visionos/accessing-the-main-camera) support the platform guidance. [Apple Developer releases](https://developer.apple.com/news/releases/), [visionOS 27 notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-27-release-notes), and [Xcode 27 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes) support the status and migration guidance checked September 8, 2026. Inline story sources describe historical examples.
