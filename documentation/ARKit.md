# ARKit

Integrate hardware sensing features to produce augmented reality apps and games.

**Platforms:** iOS 11.0+ | iPadOS 11.0+ | Mac Catalyst 14.0+ | visionOS 1.0+

## Overview

Augmented reality (AR) describes user experiences that add 2D or 3D elements to the live view from a device's sensors in a way that makes those elements appear to inhabit the real world. ARKit combines device motion tracking, world tracking, scene understanding, and display conveniences to simplify building an AR experience.

> **iOS 27+, iPadOS 27+, visionOS 27+:** Interface chrome layered over camera or passthrough content uses the refined Liquid Glass material, with stronger content diffusion and a darkened edge ring. Because the background is live and uncontrolled, test controls against bright, dark, and rapidly changing scenes.

## Topics

### visionOS
- [Setting up access to ARKit data](https://developer.apple.com/documentation/arkit/setting_up_access_to_arkit_data) - Check whether your app can use ARKit and respect people's privacy.
- **ARKitSession** - The main entry point for receiving data from ARKit.
- **DataProvider** - A source of live data from ARKit.
- **Anchor** - The identity, location, and orientation of an object in world space.
- [ARKit in visionOS](https://developer.apple.com/documentation/arkit/arkit_in_visionos) - Create immersive augmented reality experiences.
- [ARKit in visionOS C API](https://developer.apple.com/documentation/arkit/arkit_in_visionos_c_api) - Integrate ARKit with low-level libraries and functionality.

### iOS
- [Verifying Device Support and User Permission](https://developer.apple.com/documentation/arkit/verifying_device_support_and_user_permission) - Check whether your app can use ARKit and respect user privacy at runtime.
- **ARSession** - The object that manages the major tasks associated with every AR experience, such as motion tracking, camera passthrough, and image analysis.
- **ARAnchor** - An object that specifies the position and orientation of an item in the physical environment.
- [ARKit in iOS](https://developer.apple.com/documentation/arkit/arkit_in_ios) - Integrate iOS device camera and motion features to produce augmented reality experiences in your app or game.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ARKit)*
