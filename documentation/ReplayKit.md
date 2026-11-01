# ReplayKit

Record or stream video from the screen, and audio from the app and microphone.

**Platforms:** iOS 9.0+ | iPadOS 9.0+ | Mac Catalyst 13.0+ | macOS 11.0+ | tvOS 10.0+ | visionOS 1.0+

**Status:** Apple's OS 27 documentation marks every class, protocol, and error symbol listed under Topics as deprecated. Most were deprecated in 27.0 on each platform where the symbol is available; `RPBroadcastMP4ClipHandler` and `RPBroadcastConfiguration` were deprecated earlier, in 11.0 on iOS, iPadOS, and tvOS. The replacement varies: ScreenCaptureKit for the recorder and error symbols, `SCRecordingEditor` for the preview controller, and `SCContentSharingPicker` for the system broadcast picker. The broadcast controller, handler, and activity-picker symbols deprecated in 27.0 carry the message "No longer supported" and name no replacement. The unlisted delegate protocols `RPScreenRecorderDelegate`, `RPPreviewViewControllerDelegate`, `RPBroadcastControllerDelegate`, and `RPBroadcastActivityViewControllerDelegate` are also deprecated in 27.0. The ReplayKit framework page itself is not marked deprecated, and deprecation is not removal.

## Overview

Using the **ReplayKit** framework, users can record video from the screen, and audio from the app and microphone. They can then share their recordings with other users through email, messages, and social media. You can build app extensions for live broadcasting your content to sharing services. ReplayKit is incompatible with **AVPlayer** content.

## Screen-streaming migration

The current [ScreenCaptureKit overview](https://developer.apple.com/documentation/screencapturekit) directs screen streaming and mirroring to ScreenCaptureKit and says that its workflow no longer needs a broadcast extension. The OS 27 SDK extends that framework to iOS, iPadOS, tvOS, and visionOS, while preserving earlier Mac availability.

Use [ScreenCaptureKit](ScreenCaptureKit.md) for new supported capture paths, with its system content picker and capture authorization. Retain ReplayKit where older deployment targets or existing recording/broadcast integrations require it. This guidance is not a claim that the entire ReplayKit framework was removed in OS 27, nor does it make `AVPlayer` content recordable through ReplayKit.

## Topics

### Replay Sharing
- [Recording and Streaming Your macOS App](https://developer.apple.com/documentation/replaykit/recording-and-streaming-your-macos-app) - Share screen recordings, or broadcast live audio and video of your app, by adding ReplayKit to your macOS apps and games.
- **RPScreenRecorder** - The shared recorder object that provides the ability to record audio and video of your app. (Deprecated in 27.0; use ScreenCaptureKit.)
- **RPPreviewViewController** - An object that displays a user interface where users preview and edit a screen recording that you create with ReplayKit. (Deprecated in 27.0; use `SCRecordingEditor`.)

### Media Clip Processing
- **RPBroadcastController** - An object containing methods for starting and controlling a broadcast. (Deprecated in 27.0; "No longer supported".)
- **RPBroadcastHandler** - An object that sends messages to the broadcasting app. (Deprecated in 27.0; "No longer supported".)
- **RPBroadcastSampleHandler** - An object that processes buffer objects as received from ReplayKit. (Deprecated in 27.0; "No longer supported".)
- **RPBroadcastMP4ClipHandler** - An object that processes MP4 movie clips from ReplayKit. (Deprecated in 11.0 on iOS, iPadOS, and tvOS, in 13.1 on Mac Catalyst, and in 1.0 on visionOS; use RPBroadcastSampleHandler.)

### Live Broadcast Implementation
- **RPBroadcastActivityViewController** - A view controller that displays a user interface where users choose a broadcast service. (Deprecated in 27.0 on iOS, iPadOS, Mac Catalyst, tvOS, and visionOS; "No longer supported".)
- **RPSystemBroadcastPickerView** - A view displaying a broadcast button that, when tapped, shows a broadcast picker. (Deprecated in 27.0 on iOS, iPadOS, Mac Catalyst, and visionOS; use ScreenCaptureKit's `SCContentSharingPicker`.)
- **RPBroadcastActivityController** - A controller object that presents the macOS broadcast picker. (Deprecated in macOS 27.0; "No longer supported".)
- **RPBroadcastActivityControllerDelegate** - A protocol that defines the methods to implement to respond to selection events from a broadcast activity controller. (Deprecated in macOS 27.0; "No longer supported".)
- **RPBroadcastConfiguration** - An object used to configure the movie clips produced during a live broadcast. (Deprecated in 11.0 on iOS, iPadOS, and tvOS, in 13.1 on Mac Catalyst, and in 1.0 on visionOS; "No longer supported".)

### Errors
- **RPRecordingErrorCode** - The ReplayKit error domain codes. (Deprecated in 27.0; use ScreenCaptureKit.)
- **RPRecordingErrorDomain** - The ReplayKit framework error domain. (Deprecated in 27.0; use ScreenCaptureKit.)

### Reference
- **ReplayKit Constants** - ReplayKit constants affecting multiple classes.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ReplayKit)*
