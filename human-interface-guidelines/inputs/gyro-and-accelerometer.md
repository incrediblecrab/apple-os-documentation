# Gyroscope and Accelerometer

On-device gyroscopes and accelerometers can supply data about a device's movement in the physical world.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

You can use available accelerometer and gyroscope data to provide real-time, motion-based experiences. Check the chosen API and device's capabilities rather than assuming every platform has the same sensors. For example, Core Motion exposes availability properties for device sensors, while a game controller's [`motion`](https://developer.apple.com/documentation/gamecontroller/gccontroller/motion) profile is `nil` when the controller doesn't support motion input. Don't assume every Siri Remote provides it.

If your app adds motion-driven visual effects, check that they do not distract from a task or impair comfort. Respect [Reduce Motion](../foundations/motion.md), and provide alternatives when a physical motion gesture would make an essential action difficult.

## Topics

### Best Practices

- **Use motion data only to offer a tangible benefit to people** - For example, a fitness app might use the data to provide feedback about people's activity and general health, and a game might use the data to enhance gameplay. Avoid gathering data simply to have the data.
- **Outside of active gameplay, avoid using accelerometers or gyroscopes for the direct manipulation of your interface** - Some motion-based gestures may be difficult to replicate precisely, may be physically challenging for some people to perform, and may affect battery usage.

Important: Explain why your app needs motion data and handle unavailable or denied access. Include [`NSMotionUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsmotionusagedescription) when required by the motion APIs you use. Don't assume that every live sensor or controller API has the same authorization flow.

### Platform Considerations

No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.

### Related Components

- [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback) - Feedback guidance

### Developer Documentation

- [Getting processed device-motion data](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data) - Core Motion

### Videos

- [Measure health with motion](https://developer.apple.com/videos/play/wwdc2021/10287)

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/gyro-and-accelerometer)*
