# Immersive Media Support

Read and write essential Apple Immersive Video metadata.

**Platforms:** macOS 26.0+ | visionOS 26.0+

## Overview

Immersive Media Support enables you to create custom workflows for processing Apple Immersive Video (AIV). Use it to read and write AIV-specific metadata and enable previewing content in editorial workflows.

## Authoring and delivery boundaries

The framework's macOS and visionOS minimum remains **26.0**, not 27. It concerns Apple Immersive Video metadata, calibration, packaging, and editorial preview, rather than every kind of spatial image or remote 3D stream.

Use the authoring guide and `AIVUValidator` below to check generated packages, then validate playback through [AVKit](AVKit.md) on the intended device. Keep camera calibration, presentation timing, and media frames consistent when editing.

[Foveated Streaming](FoveatedStreaming.md) instead connects visionOS to a remote renderer, and [Spatial Preview](SpatialPreview.md) serves Mac document/USD review. Neither framework makes an arbitrary video file an Apple Immersive Video asset.

## Topics

### Essentials
- [Authoring Apple Immersive Video](https://developer.apple.com/documentation/immersivemediasupport/authoring-apple-immersive-video) - Prepare and package immersive video content for delivery.

### Camera metadata
- **VenueDescriptor** - The Apple Immersive Media Venue Descriptor is a collection of static metadata necessary for every Apple Immersive Video.
- **ImmersiveCamera** - A structure that holds the required information for an immersive media camera to process and render video frames.
- **ImmersiveCameraCalibration** - A structure that represents immersive media camera calibration data.
- **ImmersiveCameraMask** - A structure that holds the camera mask type information and its relevant mask name.
- **ImmersiveDynamicMask** - A type that holds the information required to dynamically generate an immersive media mask at load time.

### Presentation commands
- **PresentationCommand** - A set of properties that define the interface for a presentation command.
- **FadeCommand** - A command type for color fading during immersive media playback.
- **FadeEnvironmentCommand** - A command type for opacity fading environment backdrops during immersive media playback.
- **SetCameraCommand** - A command type for immersive camera switching during playback.
- **ShotFlopCommand** - A command type to flip the video frames horizontally (mirrored horizontally) during playback for the duration of the command.
- **PresentationDescriptor** - A structure that represents dynamic metadata used during playback or when outputting the metadata track for an immersive video file.
- **PresentationDescriptorReader** - An object that provides the functionality required to understand and process immersive presentation commands.

### Parametric immersive support
- **ParametricImmersiveAssetInfo** - An object that helps convert the original wide field of view video asset to parametric immersive asset.

### Immersive video rendering support
- **ImmersiveCameraViewModel** - A view model that holds all the resources needed to render an immersive camera view.
- **ImmersiveVideoMask** - A video mask to use during video rendering to smooth the edges of the mesh.

### Preview
- **ImmersiveMediaPreviewMessagingProtocol** - An object that represents the messaging protocol a remote preview sender and receiver use to communicate.

### Validation
- **AIVUValidator** - A type to validate existing AIVU files to ensure that they meet the minimum requirements for AIV.

### Classes
- **ImmersiveCameraMeshCalibration** - Calibration mesh geometry based on USDZ data.
- **ImmersiveImageMask** - An object that holds all the information needed to load immersive media masks from image data or from a file.
- **ImmersiveMediaRemotePreviewReceiver** - An observable object that helps apps handle receiving commands and data sent from an immersive media remote preview sender object.
- **ImmersiveMediaRemotePreviewSender** - An observable object that helps an app send the required data to all connected receiver apps to help facilitate the complete preview of the immersive media playback.

### Structures
- **ImmersiveCameraLensDefinition** - This type holds the ILPD lens configuration parameters to generate camera calibration type instance.
- **ImmersiveVideoFrame** - An immersive frame's layout, presentation timestamp, and pixel buffers. Its initializers accept either left/right-eye buffers or one buffer with a specified layout.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ImmersiveMediaSupport)*
