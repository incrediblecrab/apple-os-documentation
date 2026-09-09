# LockedCameraCapture

Capture content with your app's camera experience when the device is locked.

**Platforms:** iOS 18.0+ | iPadOS 18.0+ | Mac Catalyst 18.0+

## Overview
Use the LockedCameraCapture framework to create an extension that allows people to launch your app’s camera experience and capture content quickly when the device is locked. This extension makes your camera experience accessible to people from Control Center, the Lock Screen, or the Action button.

Entry points depend on the device and the controls the person configures. A Catalyst SDK annotation is not a promise that a Mac offers the iPhone Lock Screen or Action button workflow.

### Restricted extension lifecycle

The [camera-experience guide](https://developer.apple.com/documentation/lockedcameracapture/creating-a-camera-experience-for-the-lock-screen) states that the extension cannot access the network or the App Group's shared container. Its own container is erased when it is suspended. Use the documented PhotoKit or `LockedCameraCaptureSession.sessionContentURL` handoff rather than relying on files left in the extension's container.

Camera permission is inherited from the containing app. If access is not already granted, the system requires authentication and opens the app to request it. An extension without an active camera view, the required capture-event interaction, or requested camera access can terminate shortly after launch.

`CameraCaptureIntent.appContext` carries at most four KB of launch configuration, not a media archive. Tasks requiring broader access continue in the containing app after authentication.

## Topics

### Essentials
- [Creating a camera experience for the Lock Screen](https://developer.apple.com/documentation/lockedcameracapture/creating-a-camera-experience-for-the-lock-screen) - Offer your app's camera experience on locked devices from Control Center, the Lock Screen, and the Action button.
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
