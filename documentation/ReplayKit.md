# ReplayKit

Record or stream video from the screen, and audio from the app and microphone.

**Platforms:** iOS 9.0+ | iPadOS 9.0+ | Mac Catalyst 13.0+ | macOS 11.0+ | tvOS 10.0+ | visionOS 1.0+

## Overview

Using the **ReplayKit** framework, users can record video from the screen, and audio from the app and microphone. They can then share their recordings with other users through email, messages, and social media. You can build app extensions for live broadcasting your content to sharing services. ReplayKit is incompatible with **AVPlayer** content.

## Topics

### Replay Sharing
- [Recording and Streaming Your macOS App](https://developer.apple.com/documentation/replaykit/recording_and_streaming_your_macos_app) - Share screen recordings, or broadcast live audio and video of your app, by adding ReplayKit to your macOS apps and games.
- **RPScreenRecorder** - The shared recorder object that provides the ability to record audio and video of your app.
- **RPPreviewViewController** - An object that displays a user interface where users preview and edit a screen recording that you create with ReplayKit.

### Media Clip Processing
- **RPBroadcastController** - An object containing methods for starting and controlling a broadcast.
- **RPBroadcastHandler** - An object that sends messages to the broadcasting app.
- **RPBroadcastSampleHandler** - An object that processes buffer objects as received from ReplayKit.
- **RPBroadcastMP4ClipHandler** - An object that processes MP4 movie clips from ReplayKit.

### Deprecated
Live Broadcast Implementation

### Live Broadcast Implementation
- **RPBroadcastActivityViewController** - A view controller that displays a user interface where users choose a broadcast service.
- **RPSystemBroadcastPickerView** - A view displaying a broadcast button that, when tapped, shows a broadcast picker.
- **RPBroadcastActivityController** - A controller object that presents the macOS broadcast picker.
- **RPBroadcastActivityControllerDelegate** - A protocol that defines the methods to implement to respond to selection events from a broadcast activity controller.
- **RPBroadcastConfiguration** - An object used to configure the movie clips produced during a live broadcast. (Deprecated)

### Errors
- **RPRecordingErrorCode** - The ReplayKit error domain codes.
- **RPRecordingErrorDomain** - The ReplayKit framework error domain.

### Reference
- **ReplayKit Constants** - ReplayKit constants affecting multiple classes.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ReplayKit)*