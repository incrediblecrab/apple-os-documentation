# ScreenCaptureKit

Filter and select screen content and stream it to your app.

**Platforms:** Mac Catalyst 18.2+ | macOS 12.3+

## Overview

Use the ScreenCaptureKit framework to add support for high-performance frame capture of screen and audio content to your Mac app. The framework gives you fine-grained control to select and stream only the content that you want to capture. As a stream captures new video frames and audio samples, it passes them to your app as CMSampleBuffer objects that contain the media data and its related metadata. ScreenCaptureKit also provides a macOS-integrated picker for streaming selection and management, SCContentSharingPicker.

### Related Sessions from WWDC22 and WWDC23
- Session 10156: Meet ScreenCaptureKit
- Session 10155: Take ScreenCaptureKit to the next level
- Session 10136: What's new in ScreenCaptureKit

## Topics

### Essentials
- [ScreenCaptureKit updates](https://developer.apple.com/documentation/screencapturekit/screencapturekit_updates) - Learn about important changes to ScreenCaptureKit.
- **Persistent Content Capture** - A Boolean value that indicates whether a Virtual Network Computing (VNC) app needs persistent access to screen capture.
- [Capturing screen content in macOS](https://developer.apple.com/documentation/screencapturekit/capturing_screen_content_in_macos) - Stream desktop content like displays, apps, and windows by adopting screen capture in your app.

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