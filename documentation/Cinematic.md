# Cinematic

Integrate playback and editing of assets captured in Cinematic mode into your app.

**Platforms:** iOS 17.0+ | iPadOS 17.0+ | macOS 14.0+ | tvOS 17.0+

## Overview

The Cinematic framework enables you to add professional-level editing and playback features to movies, recorded with the Camera app's Cinematic mode, to your apps. These are the same features used in applications such as Final Cut Pro, Photos, and iMovie. For example, this enables your apps to change focus distance and aperture in movies, creating a bokeh effect, even after recording.

## Topics

### Essentials
- [Playing and editing Cinematic mode video](https://developer.apple.com/documentation/cinematic/playing_and_editing_cinematic_mode_video) - Play and edit Cinematic mode video with an adjustable depth of field and focus points.
- **CNScript** - A collection of focus decisions, focus transitions, detections, and detection tracks associated with a movie captured in Cinematic mode and methods to change them.

### Reading and rendering
- **CNAssetInfo** - An object that provides Cinematic-specific information about an asset, including its tracks.
- **CNCompositionInfo** - An object that enables you to add the appropriate number of tracks for a Cinematic asset.
- **CNRenderingSession** - An object representing the context in which rendering occurs.

### Editing
- [Editing Spatial Audio with an audio mix](https://developer.apple.com/documentation/cinematic/editing_spatial_audio_with_an_audio_mix) - Add Spatial Audio editing capabilities with the Audio Mix API in the Cinematic framework.
- **CNDetection** - A structure that represents a detected subject, face, torso or pet at a particular time.
- **CNDecision** - An object that represents a decision to focus on a particular detection, or group of detections, at a particular time.
- **CNDetectionTrack** - An object representing a series of detections of the same subject over time.
- **CNFixedDetectionTrack** - An object representing the fixed detection track.
- **CNCustomDetectionTrack** - An object representing a discrete detection track composed of individual detections.
- **CNDetectionType** - The type of object detected, such as face, torso, cat, dog and so on.

### Custom Object Tracking
- **CNBoundsPrediction** - A structure representing the bounds of the predicted subject.
- **CNObjectTracker** - An object that converts a normalized point or rectangle into a detection track that tracks an object over time.

### Structures
- **CNCinematicError**

### Reference
- **Cinematic Enumerations**
- **Cinematic Constants**
- **Cinematic Data Types**

### Classes
- **CNAssetSpatialAudioInfo**

### Enumerations
- **CNSpatialAudioContentType** (Beta)
- **CNSpatialAudioRenderingStyle** (Beta)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Cinematic)*