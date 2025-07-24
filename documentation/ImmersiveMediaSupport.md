# Immersive Media Support

Read and write essential Apple Immersive Video metadata.

**Platforms:** macOS 26.0+ (Beta) | visionOS 26.0+ (Beta)

## Overview

Immersive Media Support enables you to create custom workflows for processing Apple Immersive Video (AIV). Use it to read and write AIV-specific metadata and enable previewing content in editorial workflows.

> **Beta Software**
> 
> This documentation contains preliminary information about an API or technology in development. This information is subject to change, and software implemented according to this documentation should be tested with final operating system software.

## Topics

### Essentials
- [Authoring Apple Immersive Video](https://developer.apple.com/documentation/immersivemediasupport/authoring_apple_immersive_video) - Prepare and package immersive video content for delivery.

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
- **ImmersiveVideoFrame** - A type that represents an immersive video frame. An immersive video frame contains: layout (SideBySide, OverUnder, Separate, Mono), presentationTime: frame presentation time, pixelBuffers: an array with one or more images representing the frame.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ImmersiveMediaSupport)*