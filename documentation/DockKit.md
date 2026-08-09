# DockKit

Interact with accessories that track subjects on camera as they move around.

**Platforms:** iOS 17.0+ | iPadOS 17.0+ | Mac Catalyst 17.0+

## Overview

DockKit interfaces with DockKit-compatible motorized stands known as dock accessories to track the location of objects that appear in video frames. It determines how to best position the iPhone camera to frame and track objects, with improved person tracking using combined body and face tracking for human subjects. This feature, known as system tracking, automatically starts as soon as a person docks iPhone onto a compatible motorized stand and launches the Camera app. For example, system tracking is useful for content creators who want the camera to follow them while they move around their space, or instructors on a video call who are walking around a classroom.

You can disable system tracking and implement your own tracking behavior by using DockAccessoryManager and DockAccessory. Implement your own tracking behavior to follow a location of a custom object such as a pet, or a pair of hands performing a task. DockKit accessories integrate with AVCaptureSession so apps with camera permissions work seamlessly together.

## Topics

### Controlling the dock accessory
- [Controlling a DockKit accessory using your camera app](https://developer.apple.com/documentation/dockkit/controlling-a-dockkit-accessory-using-your-camera-app) - Follow subjects in real time using an iPhone that you mount on a DockKit accessory.
- **DockAccessoryManager** - Observe the state of dock accessories and enable or disable system tracking.
- **DockAccessory** - Obtain accessory information and control tracking behavior.
- **DockKitError** - A list of errors that DockKit sends.

### Customizing tracking behavior
- [Modify rotation and positioning programmatically](https://developer.apple.com/documentation/dockkit/modify-rotation-and-positioning-programmatically) - Perform custom control of the dock accessory.
- [Track custom objects in a frame](https://developer.apple.com/documentation/dockkit/track-custom-objects-in-a-frame) - Use your machine learning model to focus on a specific subject.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/DockKit)*