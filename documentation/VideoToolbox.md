# Video Toolbox

Work directly with hardware-accelerated video encoding and decoding capabilities.

**Platforms:** iOS 6.0+ | iPadOS 6.0+ | Mac Catalyst 13.0+ | macOS 10.8+ | tvOS 10.2+ | visionOS 1.0+

## Overview

VideoToolbox is a low-level framework that provides direct access to hardware encoders and decoders. It provides services for video compression and decompression, and for conversion between raster image formats stored in CoreVideo pixel buffers. These services are provided in the form of session objects (compression, decompression, and pixel transfer), which are vended as Core Foundation (CF) types. Apps that don't need direct access to hardware encoders and decoders shouldn't need to use VideoToolbox directly.

## Topics

### Frame Processing
- [Frame processing](https://developer.apple.com/documentation/videotoolbox/frame_processing) - An interface for accessing a range of different video-processing features.

### Compression
- [Encoding video for low-latency conferencing](https://developer.apple.com/documentation/videotoolbox/encoding_video_for_low-latency_conferencing) - Configure a compression session to optimize encoding for video-conferencing apps.
- [Encoding video for live streaming](https://developer.apple.com/documentation/videotoolbox/encoding_video_for_live_streaming) - Configure a compression session to encode video for live streaming.
- [Encoding video for offline transcoding](https://developer.apple.com/documentation/videotoolbox/encoding_video_for_offline_transcoding) - Configure a compression session to transcode video in offline workflows.
- **VTCompressionSession** - An object that compresses video data.
- **VTDecompressionSession** - An object that decompresses video data.
- **VTFrameSilo** - An object that stores sample buffers from a multipass encoding session.
- **VTMultiPassStorage** - An object that stores video encoding metadata from a multipass encoding session.

### Transformation
- **VTPixelTransferSession** - An object converts video data from source pixel buffers to destination pixel buffers.
- **VTPixelRotationSession** - An object that rotates source pixel buffers to destination pixel buffers.

### RAW Processing
- **VTRAWProcessingSession** - An object that processes frames in camera native formats such as RAW or Bayer.

### Media Extension
- **VTExtensionPropertiesKey** - A key in a Media Extension extension properties dictionary.

### HDR Metadata
- **VTHDRPerFrameMetadataGenerationSession** - An object that generates per-frame HDR metadata.

### Codec Support
- **VTIsHardwareDecodeSupported** - Returns a Boolean value that indicates whether the current system supports hardware decode for the specified codec.
- **VTRegisterProfessionalVideoWorkflowVideoEncoders** - Loads encoders appropriate for the client's professional video workflows.
- **VTRegisterProfessionalVideoWorkflowVideoDecoders** - Loads decoders appropriate for the client's professional video workflows.
- **VTRegisterSupplementalVideoDecoderIfAvailable** - Registers a video decoder for the specified codec type, if one exists on the current system.
- **VTCopySupportedPropertyDictionaryForEncoder** - Builds a list of supported properties and encoder ID for an encoder.
- **VTCopyVideoEncoderList** - Builds a list of available video encoders.
- [Video Encoder List Keys](https://developer.apple.com/documentation/videotoolbox/video_encoder_list_keys) - Dictionary key constants to use to retrieve video encoder information.

### Utilities
- **VTCreateCGImageFromCVPixelBuffer** - Creates a Core Graphics bitmap image or image mask using the provided pixel buffer.

### Data Types
- **VTSession** - An abstract object that provides the common interface to configure VideoToolbox session objects.
- **VTInt32Point** - A structure that represents a 32-bit integer point value.
- **VTInt32Size** - A structure that represents a 32-bit integer size value.

### Errors
- [Error Code Constants](https://developer.apple.com/documentation/videotoolbox/error_code_constants) - Constants for Video Toolbox operation error codes.

### Reference
- [VideoToolbox Reference](https://developer.apple.com/documentation/videotoolbox/videotoolbox_reference)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/VideoToolbox)*