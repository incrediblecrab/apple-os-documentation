# AVFoundation

Work with audiovisual assets, control device cameras, process audio, and configure system audio interactions.

**Platforms:** iOS 2.2+ | iPadOS 13.1+ | Mac Catalyst 13.1+ | macOS 10.7+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 3.0+

## Overview

AVFoundation combines several major technology areas that together encompass a wide range of tasks for inspecting, playing, capturing, and processing audiovisual media on Apple platforms.

## Topics

### Essentials
- [AVFoundation updates](https://developer.apple.com/documentation/avfoundation/avfoundation_updates) - Learn about important changes to AVFoundation.

### Common
- **Media assets** - Load media assets from files and streams to inspect their attributes, tracks, and embedded metadata.
- **Media reading and writing** - Read images from video, export to alternative formats, and perform sample-level reading and writing of media data.
- **Media types and utilities** - Identify the types of content and file formats that AVFoundation supports.
- **Video settings** - Configure video processing settings using standard key and value constants.
- **Audio settings** - Configure audio processing settings using standard key and value constants.

### Playback
- **Media playback** - Manage the playback of media assets and interstitial content, independent of how you present that content in your interface.
- **Offline playback and storage** - Download streamed content to disk to allow offline playback, and define policies to automatically remove downloaded assets.
- **Streaming and AirPlay** - Stream content wirelessly to other devices using AirPlay, and handle requests involving FairPlay-protected assets.
- **Sample buffer playback** - Create custom controllers to play and synchronize the timing of sample buffer streams.

### Capture
- **Capture setup** - Configure built-in cameras and microphones, and external capture devices, for media capture.
- **Photo capture** - Capture high-quality still images, Live Photos, and supporting photo data.
- **Audio and video capture** - Capture audio and video directly to media files, or capture streams of media for direct access to media sample buffers.
- **Additional data capture** - Capture additional data including depth and metadata, and synchronize capture from multiple outputs.

### Editing
- **Composite assets** - Combine tracks and segments of tracks from multiple assets into a composite asset that you can play or process.
- **QuickTime movies** - Access the contents of a QuickTime movie file, and perform sample-level edits of its media tracks.
- **Video effects** - Define standard video transition effects, synchronize layer animations with media timing, and create custom video compositors.
- **Audio mixing** - Define how to mix the audio levels from multiple audio tracks over an asset's duration.

### Audio
- **Audio playback, recording, and processing** - Play, record, and process audio; configure your app's system audio behavior.
- **Speech synthesis** - Configure voices to speak strings of text.

### Errors
- **AVFoundationErrorDomain** - The error domain of AVFoundation errors.
- **AVError** - A structure that defines the errors that framework operations can generate.

### Macros
- **Macros**

### Classes
- **AVCaptureSpatialAudioMetadataSampleGenerator** (Beta)
- **AVCustomMediaSelectionScheme** - For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVCustomMediaSelectionScheme provides a collection of custom settings for controlling the presentation of the media. (Beta)
- **AVMediaPresentationSelector** - For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVMediaPresentationSelector represents a collection of mutually exclusive settings. (Beta)
- **AVMediaPresentationSetting** - For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVMediaPresentationSetting represents a selectable setting for controlling the presentation of the media. (Beta)
- **AVMetadataCatHeadObject** (Beta)
- **AVMetadataDogHeadObject** (Beta)
- **AVMetricDownloadSummaryEvent** - Represents a summary metric event with aggregated metrics for the entire download task.
- **AVMetricMediaRendition** (Beta)
- **AVPlaybackCoordinationMedium**

### Structures
- **AVCIImageFilteringParameters**
- **AVCIImageFilteringResult** - An output video frame processed with Core Image filtering.
- **AVCaptureSceneMonitoringStatus** (Beta)
- **AVSpatialVideoConfiguration**

### Variables
- **AVAssetExportPresetHEVC4320x2160** (Beta)
- **AVAssetExportPresetMVHEVC4320x4320** (Beta)
- **AVAssetExportPresetMVHEVC7680x7680** (Beta)
- **AVContentKeyRequestRandomDeviceIdentifierSeedKey** - Value is an NSData containing a 16-byte seed to randomize the user's deviceID contained in the SPC blob during FairPlay key exchange (Beta)
- **AVContentKeyRequestShouldRandomizeDeviceIdentifierKey** - Value is an Boolean indicating whether the user's deviceID contained in the SPC blob during FairPlay key exchange should be randomized using a system generated seed (Beta)
- **AVURLAssetShouldParseExternalSphericalTagsKey** - Indicates whether additional projected media signaling in the asset should be parsed and resolved as format description extensions. (Beta)

### Enumerations
- **AVCaptureCameraLensSmudgeDetectionStatus** (Beta)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AVFoundation)*