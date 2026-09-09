# ARKit

Integrate hardware sensing features to produce augmented reality apps and games.

**Documented framework platforms:** iOS 11.0+ | iPadOS 11.0+ | visionOS 1.0+

## Overview

Augmented reality (AR) describes user experiences that add 2D or 3D elements to the live view from a device's sensors in a way that makes those elements appear to inhabit the real world. ARKit combines device motion tracking, world tracking, scene understanding, and display conveniences to simplify building an AR experience.

## Support, authorization, and OS 27 testing

The framework's minimum version does not guarantee support for every tracking configuration or data provider. Check the [iOS device-support and permission guidance](https://developer.apple.com/documentation/arkit/verifying-device-support-and-user-permission) and the separate [visionOS data-access requirements](https://developer.apple.com/documentation/visionos/setting-up-access-to-arkit-data). Provide a useful state when tracking is unavailable or permission is denied.

For spatial controllers and styli, Game Controller supplies input while ARKit or RealityKit supplies tracking. Follow [Discovering and tracking spatial game controllers and styli](https://developer.apple.com/documentation/gamecontroller/discovering-and-tracking-spatial-game-controllers-and-styli), including accessory-tracking authorization; receiving button events does not itself grant access to transforms.

The [visionOS 27 Beta 8 release notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-27-release-notes#ARKit), checked September 8, 2026, distinguish these changes:

- **Resolved:** room anchors from `RoomTrackingProvider` and the room-tracking C API previously returned empty plane/mesh anchor identifiers (173005535). Keep this as a regression test, not a current provider restriction.
- **C callback ownership:** outside ARC, retain a reference object or error inside the completion handler if you need it afterward. The notes specifically require `ar_retain` for results from functions such as `ar_reference_object_load_from_url` and `ar_reference_object_load_with_name` (173812495). This is documented lifetime behavior following a fix, not a persistent tracking failure or a requirement to retain every result indefinitely.

## Topics

### visionOS
- [Setting up access to ARKit data](https://developer.apple.com/documentation/visionos/setting-up-access-to-arkit-data) - Check whether your app can use ARKit and respect people's privacy.
- **ARKitSession** - The main entry point for receiving data from ARKit.
- **DataProvider** - A source of live data from ARKit.
- **Anchor** - The identity, location, and orientation of an object in world space.
- [ARKit in visionOS](https://developer.apple.com/documentation/arkit/arkit-in-visionos) - Create immersive augmented reality experiences.
- [ARKit in visionOS C API](https://developer.apple.com/documentation/arkit/arkit-in-visionos-c-api) - Integrate ARKit with low-level libraries and functionality.

### iOS
- [Verifying Device Support and User Permission](https://developer.apple.com/documentation/arkit/verifying-device-support-and-user-permission) - Check whether your app can use ARKit and respect user privacy at runtime.
- **ARSession** - The object that manages the major tasks associated with every AR experience, such as motion tracking, camera passthrough, and image analysis.
- **ARAnchor** - An object that specifies the position and orientation of an item in the physical environment.
- [ARKit in iOS](https://developer.apple.com/documentation/arkit/arkit-in-ios) - Integrate iOS device camera and motion features to produce augmented reality experiences in your app or game.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ARKit)*
