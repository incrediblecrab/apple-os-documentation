# AVKit

Create user interfaces for media playback, complete with transport controls, chapter navigation, picture-in-picture support, and display of subtitles and closed captions.

**Platforms:** iOS 8.0+ | iPadOS 8.0+ | Mac Catalyst 13.0+ | macOS 10.9+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 9.0+

## Playback UI and OS 27 integration

Choose the presentation API for the target: `AVPlayerViewController` for its supported UIKit platforms, `AVPlayerView` for AppKit, or SwiftUI's `VideoPlayer` where available. Picture in Picture, multiview, immersive playback, and capture interactions each have their own requirements; the framework-wide platform header is not a capability list for every class.

- Use [Playing video content in a standard user interface](https://developer.apple.com/documentation/avkit/playing-video-content-in-a-standard-user-interface) for a system player rather than recreating transport and accessibility controls unnecessarily.
- On the OS 27 targets supported by [AVSystemRouting](AVSystemRouting.md), route selection can lead to playback through a [Media Device](MediaDevice.md) extension. The picker does not itself implement the receiver's protocol or guarantee playback.
- Keep metadata publication consistent with the player. [Now Playing](NowPlaying.md) offers the OS 27 observable-model API. Do not mix its local-playback APIs with `MPNowPlayingInfoCenter` and `MPRemoteCommandCenter` in your app; Apple documents undefined behavior.
- Test route loss, interrupted playback, subtitles, and transitions into and out of Picture in Picture or immersive presentation on the target device. Do not infer hardware or media-format support from a system UI being available.

## Topics

### iOS Playback and Capture

- [Playing video content in a standard user interface](https://developer.apple.com/documentation/avkit/playing-video-content-in-a-standard-user-interface) - Play media full screen, embedded inline, or in a floating Picture in Picture (PiP) window using a player view controller.
- **AVPlayerViewController** - A view controller that displays content from a player and presents a native user interface to control playback.
- **AVPlayerViewControllerDelegate** - A protocol that defines the methods to implement to respond to player view controller events.
- **AVCaptureEventInteraction** - An object that registers handlers to respond to capture events from system hardware buttons.
- **AVCaptureEvent** - An object that describes a user interaction with a system hardware button.
- **AVCaptureEventSound** - A sound object for a capture event.
- **AVInputPickerInteraction** - Use AVInputPickerInteraction to present an input picker.
### tvOS Playback and Capture

- [Customizing the tvOS Playback Experience](https://developer.apple.com/documentation/avkit/customizing-the-tvos-playback-experience) - Adopt the latest features of the redesigned tvOS player user interface to provide a more streamlined way to watch your content.
- [Presenting Navigation Markers](https://developer.apple.com/documentation/avkit/presenting-navigation-markers) - Present navigation markers in the Chapters panel to help users quickly navigate your content.
- [Working with Interstitial Content](https://developer.apple.com/documentation/avkit/working-with-interstitial-content) - Present additional content alongside your main media presentation using HTTP Live Streaming support.
- [Presenting Content Proposals in tvOS](https://developer.apple.com/documentation/avkit/presenting-content-proposals-in-tvos) - Display a preview of an upcoming media item at the conclusion of the currently playing media item.
- [Working with Overlays and Parental Controls in tvOS](https://developer.apple.com/documentation/avkit/working-with-overlays-and-parental-controls-in-tvos) - Add interactive overlays, parental controls, and livestream channel flipping using a player view controller.
- [Supporting Continuity Camera in your tvOS app](https://developer.apple.com/documentation/avkit/supporting-continuity-camera-in-your-tvos-app) - Capture high-quality photos, video, and audio in your Apple TV app by connecting an iPhone or iPad as a continuity device.
- **AVPlayerViewController** - A view controller that displays content from a player and presents a native user interface to control playback.
- **AVPlayerViewControllerDelegate** - A protocol that defines the methods to implement to respond to player view controller events.
- **AVInterstitialTimeRange** - A time range in an audiovisual presentation for content with an interstitial designation, such as advertisements or legal notices.
- **AVNavigationMarkersGroup** - A set of markers for navigating playback of an audiovisual presentation.
- **AVContentProposalViewController** - A view controller that proposes content to watch next.
- **AVDisplayManager** - A tvOS management object that controls whether a TV switches modes to match the video's native mode.
- **AVContinuityDevicePickerViewController** - A view controller that provides an interface to a person so they can select and connect a continuity device to the system.
- **AVContinuityDevicePickerViewControllerDelegate** - An interface that responds to events from a continuity device picker view controller.

### visionOS Playback

- [Playing immersive media with AVKit](https://developer.apple.com/documentation/avkit/playing-immersive-media-with-avkit) - Adopt the system playback interface to provide an immersive video watching experience.
- [Creating a multiview video playback experience in visionOS](https://developer.apple.com/documentation/avkit/creating-a-multiview-video-playback-experience-in-visionos) - Build an interface that plays multiple videos simultaneously and handles transitions to different experience types gracefully.
- [Adopting the system player interface in visionOS](https://developer.apple.com/documentation/avkit/adopting-the-system-player-interface-in-visionos) - Provide an optimized viewing experience for watching 3D video content.
- [Trimming and exporting media in visionOS](https://developer.apple.com/documentation/avkit/trimming-and-exporting-media-in-visionos) - Display standard controls in your app to edit the timeline of the currently playing media.
- **AVPlayerViewController** - A view controller that displays content from a player and presents a native user interface to control playback.
- **AVPlayerViewControllerDelegate** - A protocol that defines the methods to implement to respond to player view controller events.
- **AVExperienceController** - An object that controls video experiences.
- **AVMultiviewManager** - An object that manages viewing multiple videos at once.
- **AVGroupExperienceCoordinator** - An object that synchronizes viewing environment state across participants in a SharePlay session.

### macOS Playback and Capture

- [Implementing Trimming in a macOS Player](https://developer.apple.com/documentation/avkit/implementing-trimming-in-a-macos-player) - Provide a QuickTime media-trimming experience in your macOS app.
- **AVPlayerView** - A view that displays content from a player and presents a native user interface to control playback.
- **AVCaptureView** - A view that displays standard user interface controls for capturing media data.

### Multiplatform Playback and Capture

- **VideoPlayer** - A view that displays content from a player and a native user interface to control playback.

### Picture in Picture

- [Adopting Picture in Picture Playback in tvOS](https://developer.apple.com/documentation/avkit/adopting-picture-in-picture-playback-in-tvos) - Add advanced multitasking capabilities to your video apps by using Picture in Picture playback in tvOS.
- [Adopting Picture in Picture in a Standard Player](https://developer.apple.com/documentation/avkit/adopting-picture-in-picture-in-a-standard-player) - Add Picture in Picture (PiP) playback to your app using a player view controller.
- [Adopting Picture in Picture in a Custom Player](https://developer.apple.com/documentation/avkit/adopting-picture-in-picture-in-a-custom-player) - Add controls to your custom player user interface to invoke Picture in Picture (PiP) playback.
- [Adopting Picture in Picture for video calls](https://developer.apple.com/documentation/avkit/adopting-picture-in-picture-for-video-calls) - Add multitasking capability to your video-call apps by using Picture in Picture (PiP).
- [Accessing the camera while multitasking on iPad](https://developer.apple.com/documentation/avkit/accessing-the-camera-while-multitasking-on-ipad) - Operate the camera in Split View, Slide Over, Picture in Picture, and Stage Manager modes.
- **AVPictureInPictureController** - A controller that responds to user-initiated Picture in Picture playback of video in a floating, resizable window.

### Playback Route Selection

- **AVRoutePickerView** - A view that presents a list of nearby media receivers.

### Metadata

- **AVKit Metadata Identifiers** - Additional metadata that an asset contains.

### Errors

- **AVKitErrorDomain** - The domain of errors the framework generates.
- **AVKitError** - A structure that represents a framework error.
- **Code** - Constants that identify framework error codes.

### Macros

- **Macros**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AVKit)*
