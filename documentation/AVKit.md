# AVKit

Create user interfaces for media playback, complete with transport controls, chapter navigation, picture-in-picture support, and display of subtitles and closed captions.

**Platforms:** iOS 8.0+ | iPadOS 8.0+ | Mac Catalyst 13.0+ | macOS 10.9+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 9.0+

## Topics

### iOS Playback and Capture
- [Playing video content in a standard user interface](https://developer.apple.com/documentation/avkit/playing_video_content_in_a_standard_user_interface) - Play media full screen, embedded inline, or in a floating Picture in Picture (PiP) window using a player view controller.
- **AVPlayerViewController** - A view controller that displays content from a player and presents a native user interface to control playback.
- **AVPlayerViewControllerDelegate** - A protocol that defines the methods to implement to respond to player view controller events.
- **AVCaptureEventInteraction** - An object that registers handlers to respond to capture events from system hardware buttons.
- **AVCaptureEvent** - An object that describes a user interaction with a system hardware button.
- **AVCaptureEventSound** - A sound object for a capture event. (Beta)
- **AVInputPickerInteraction** - Use AVInputPickerInteraction to present an input picker. (Beta)

### tvOS Playback and Capture
- [Customizing the tvOS Playback Experience](https://developer.apple.com/documentation/avkit/customizing_the_tvos_playback_experience) - Adopt the latest features of the redesigned tvOS player user interface to provide a more streamlined way to watch your content.
- [Presenting Navigation Markers](https://developer.apple.com/documentation/avkit/presenting_navigation_markers) - Present navigation markers in the Chapters panel to help users quickly navigate your content.
- [Working with Interstitial Content](https://developer.apple.com/documentation/avkit/working_with_interstitial_content) - Present additional content alongside your main media presentation using HTTP Live Streaming support.
- [Presenting Content Proposals in tvOS](https://developer.apple.com/documentation/avkit/presenting_content_proposals_in_tvos) - Display a preview of an upcoming media item at the conclusion of the currently playing media item.
- [Working with Overlays and Parental Controls in tvOS](https://developer.apple.com/documentation/avkit/working_with_overlays_and_parental_controls_in_tvos) - Add interactive overlays, parental controls, and livestream channel flipping using a player view controller.
- [Supporting Continuity Camera in your tvOS app](https://developer.apple.com/documentation/avkit/supporting_continuity_camera_in_your_tvos_app) - Capture high-quality photos, video, and audio in your Apple TV app by connecting an iPhone or iPad as a continuity device.
- **AVPlayerViewController** - A view controller that displays content from a player and presents a native user interface to control playback.
- **AVPlayerViewControllerDelegate** - A protocol that defines the methods to implement to respond to player view controller events.
- **AVInterstitialTimeRange** - A time range in an audiovisual presentation for content with an interstitial designation, such as advertisements or legal notices.
- **AVNavigationMarkersGroup** - A set of markers for navigating playback of an audiovisual presentation.
- **AVContentProposalViewController** - A view controller that proposes content to watch next.
- **AVDisplayManager** - A tvOS management object that controls whether a TV switches modes to match the video's native mode.
- **AVContinuityDevicePickerViewController** - A view controller that provides an interface to a person so they can select and connect a continuity device to the system.
- **AVContinuityDevicePickerViewControllerDelegate** - An interface that responds to events from a continuity device picker view controller.

### visionOS Playback
- [Playing immersive media with AVKit](https://developer.apple.com/documentation/avkit/playing_immersive_media_with_avkit) - Adopt the system playback interface to provide an immersive video watching experience.
- [Creating a multiview video playback experience in visionOS](https://developer.apple.com/documentation/avkit/creating_a_multiview_video_playback_experience_in_visionos) - Build an interface that plays multiple videos simultaneously and handles transitions to different experience types gracefully.
- [Adopting the system player interface in visionOS](https://developer.apple.com/documentation/avkit/adopting_the_system_player_interface_in_visionos) - Provide an optimized viewing experience for watching 3D video content.
- [Trimming and exporting media in visionOS](https://developer.apple.com/documentation/avkit/trimming_and_exporting_media_in_visionos) - Display standard controls in your app to edit the timeline of the currently playing media.
- **AVPlayerViewController** - A view controller that displays content from a player and presents a native user interface to control playback.
- **AVPlayerViewControllerDelegate** - A protocol that defines the methods to implement to respond to player view controller events.
- **AVExperienceController** - An object that controls video experiences.
- **AVMultiviewManager** - An object that manages viewing multiple videos at once.
- **AVGroupExperienceCoordinator** - An object that synchronizes viewing environment state across participants in a SharePlay session.

### macOS Playback and Capture
- [Implementing Trimming in a macOS Player](https://developer.apple.com/documentation/avkit/implementing_trimming_in_a_macos_player) - Provide a QuickTime media-trimming experience in your macOS app.
- **AVPlayerView** - A view that displays content from a player and presents a native user interface to control playback.
- **AVCaptureView** - A view that displays standard user interface controls for capturing media data.

### Multiplatform Playback and Capture
- **VideoPlayer** - A view that displays content from a player and a native user interface to control playback.

### Picture in Picture
- [Adopting Picture in Picture Playback in tvOS](https://developer.apple.com/documentation/avkit/adopting_picture_in_picture_playback_in_tvos) - Add advanced multitasking capabilities to your video apps by using Picture in Picture playback in tvOS.
- [Adopting Picture in Picture in a Standard Player](https://developer.apple.com/documentation/avkit/adopting_picture_in_picture_in_a_standard_player) - Add Picture in Picture (PiP) playback to your app using a player view controller.
- [Adopting Picture in Picture in a Custom Player](https://developer.apple.com/documentation/avkit/adopting_picture_in_picture_in_a_custom_player) - Add controls to your custom player user interface to invoke Picture in Picture (PiP) playback.
- [Adopting Picture in Picture for video calls](https://developer.apple.com/documentation/avkit/adopting_picture_in_picture_for_video_calls) - Add multitasking capability to your video-call apps by using Picture in Picture (PiP).
- [Accessing the camera while multitasking on iPad](https://developer.apple.com/documentation/avkit/accessing_the_camera_while_multitasking_on_ipad) - Operate the camera in Split View, Slide Over, Picture in Picture, and Stage Manager modes.
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