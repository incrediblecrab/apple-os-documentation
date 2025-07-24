# LockedCameraCapture

Capture content with your app's camera experience when the device is locked.

**Platforms:** iOS 18.0+ | iPadOS 18.0+ | Mac Catalyst 18.0+

## Overview
Use the LockedCameraCapture framework to create an extension that allows people to launch your app’s camera experience and capture content quickly when the device is locked. This extension makes your camera experience accessible to people from Control Center, the Lock Screen, or the Action button.

A conceptual image that shows a control with a camera icon on the Lock Screen on iPhone, in Control Center on iPhone, and being performed with the Action button on iPhone 15 Pro.

## Topics

### Essentials
- [Creating a camera experience for the Lock Screen](https://developer.apple.com/documentation/lockedcameracapture/creating_a_camera_experience_for_the_lock_screen) - Offer your app's camera experience on locked devices from Control Center, the Lock Screen, and the Action button.
### Capture and launch
- **LockedCameraCaptureUIScene** - A structure that contains the session object and UI to display for the locked camera capture extension.
- **LockedCameraCaptureSession** - An object that can request to open the extension's containing app and receives session configuration updates.
### App integration
- **LockedCameraCaptureManager** - An object that provides handling of captured content and transitioning to the extension's containing app.
- **NSUserActivityTypeLockedCameraCapture** - A type to use when opening your app from the capture extension.
### Extension
- **LockedCameraCaptureExtension** - A protocol that creates a locked camera capture extension.
- **LockedCameraCaptureExtensionScene** - A protocol that provides the UI for the locked camera capture extension.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/LockedCameraCapture)*
