# ScreenCaptureKit

Filter and select screen content and stream it to your app.

**Platforms:** iOS 27.0+ | iPadOS 27.0+ | Mac Catalyst 18.2+ | macOS 12.3+ | tvOS 27.0+ | visionOS 27.0+

## Overview

Use ScreenCaptureKit to capture selected screen and audio content as `CMSampleBuffer` objects with associated metadata. Its original Mac capture APIs remain available at their earlier minimum versions; the OS 27 SDK adds iOS, iPadOS, tvOS, and visionOS support. Individual capture sources, picker options, and output types still have platform-specific availability.

## OS 27 capture integration

Apple's current framework overview directs screen-streaming and mirroring work from ReplayKit to ScreenCaptureKit, without requiring a broadcast extension. Keep an older-OS [ReplayKit](ReplayKit.md) path when your deployment range needs it rather than assuming all ReplayKit functionality is removed.

Use the system `SCContentSharingPicker` to let the person select content. Request screen-recording permission and provide `NSScreenCaptureUsageDescription` as described in the framework overview. Background capture needs the appropriate execution modes; framework availability is not permission to record.

The [Capturing screen content on iOS](https://developer.apple.com/documentation/screencapturekit/capturing-screen-content-on-ios) sample requires a physical iOS 27+ device and demonstrates:

- Full-display selection versus `presentForCurrentApplication()` for the current app's windows and layers.
- `screen-capture` background execution, plus `audio` for the sample's continuing microphone input. Camera and Photos access need their own usage descriptions and runtime authorization.
- `SCRecordingOutput` for encoded files and `SCClipBufferingOutput` for rolling clips. Await recording finalization before handing a completed file to another subsystem.
- An in-app camera overlay through `SCVideoEffectOutput`. The sample explicitly excludes camera overlays from full-display capture; do not present that as a supported combination.

Treat picker cancellation, stream errors, revoked access, and background/foreground transitions as normal states. Mirror the person's microphone and camera choices instead of attaching those inputs unconditionally.

### Related Sessions from WWDC22 and WWDC23
- Session 10156: Meet ScreenCaptureKit
- Session 10155: Take ScreenCaptureKit to the next level
- Session 10136: What's new in ScreenCaptureKit

## Topics

### Essentials
- [ScreenCaptureKit updates](https://developer.apple.com/documentation/updates/screencapturekit) - Learn about important changes to ScreenCaptureKit.
- [Capturing screen content on iOS](https://developer.apple.com/documentation/screencapturekit/capturing-screen-content-on-ios) - Adopt system-selected screen capture on iOS 27 and later.
- **Persistent Content Capture** - A Boolean value that indicates whether a Virtual Network Computing (VNC) app needs persistent access to screen capture.
- [Capturing screen content in macOS](https://developer.apple.com/documentation/screencapturekit/capturing-screen-content-in-macos) - Stream desktop content like displays, apps, and windows by adopting screen capture in your app.

### Shareable content
- **SCShareableContent** - An instance that represents a set of displays, apps, and windows that your app can capture.
- **SCShareableContentInfo** - An instance that provides information for the content in a given stream.
- **SCShareableContentStyle** - The style of content presented in a stream.
- **SCDisplay** - An instance that represents a display device.
- **SCRunningApplication** - An instance that represents an app running on a device.
- **SCWindow** - An instance that represents an onscreen window.

### Content capture
- **SCStream** - An instance that represents a stream of shareable content.
- **SCStreamConfiguration** - An instance that provides the output configuration for a stream.
- **SCContentFilter** - An instance that filters the content a stream captures.
- **SCStreamDelegate** - A delegate protocol your app implements to respond to stream events.
- **SCScreenshotManager** - An instance for the capture of single frames from a stream.
- **SCScreenshotConfiguration**
- **SCScreenshotOutput**

### Output processing
- **SCStreamOutput** - A delegate protocol your app implements to receive capture stream output events.
- **SCStreamOutputType** - Constants that represent output types for a stream frame.
- **SCStreamFrameInfo** - An instance that defines metadata keys for a stream frame.
- **SCFrameStatus** - Status values for a frame from a stream.

### System content-sharing picker
- **SCContentSharingPicker** - An instance of a picker presented by the operating system for managing frame-capture streams.
- **SCContentSharingPickerConfiguration** - An instance for configuring the system content-sharing picker.
- **SCContentSharingPickerMode** - Available modes for selecting streaming content from a picker presented by the operating system.
- **SCContentSharingPickerObserver** - An observer protocol your app implements to receive messages from the operating system's content picker.

### Stream errors
- **SCStreamErrorDomain** - A string representation of the error domain.
- **SCStreamError** - An instance representing a ScreenCaptureKit framework error.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ScreenCaptureKit)*
