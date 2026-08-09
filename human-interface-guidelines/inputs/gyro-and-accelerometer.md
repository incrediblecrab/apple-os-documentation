# Gyroscope and Accelerometer

On-device gyroscopes and accelerometers can supply data about a device's movement in the physical world.

**Platforms:** iOS | iPadOS | tvOS | watchOS

## Overview

You can use accelerometer and gyroscope data to provide experiences based on real-time, motion-based information in apps and games that run in iOS, iPadOS, and watchOS. tvOS apps can use gyroscope data from the Siri Remote.

> **iOS 27+, iPadOS 27+:** Liquid Glass specular highlights respond to device motion and are brighter and more defined in OS 27. If your app also drives motion-based visual effects, verify the combination does not become distracting, and honor Reduce Motion.

## Topics

### Best Practices

- **Use motion data only to offer a tangible benefit to people** - For example, a fitness app might use the data to provide feedback about people's activity and general health, and a game might use the data to enhance gameplay. Avoid gathering data simply to have the data.
- **Outside of active gameplay, avoid using accelerometers or gyroscopes for the direct manipulation of your interface** - Some motion-based gestures may be difficult to replicate precisely, may be physically challenging for some people to perform, and may affect battery usage.

Important: If your experience needs to access motion data from a device, you must provide copy that explains why. The first time your app or game tries to access this type of data, the system includes your copy in a permission request, where people can grant or deny access.

### Platform Considerations

No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.

### Related Components

- [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback) - Feedback guidance

### Developer Documentation

- [Getting processed device-motion data](https://developer.apple.com/documentation/coremotion/getting_processed_device-motion_data) - Core Motion

### Videos

- [Measure health with motion](https://developer.apple.com/videos/play/wwdc2024/10116/)

---

*Design baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Reviewed 2026-08-09.*

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/gyro-and-accelerometer)*
