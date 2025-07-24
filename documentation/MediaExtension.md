# MediaExtension

This framework provides a means for developers to create format readers, video decoders, and RAW processors for media that the system doesn't natively support.

**Platforms:** Mac Catalyst 18.0+ | macOS 15.0+

## Overview

MediaExtension format readers encapsulate media assets that the system doesn't natively support so that the system can recognize them. MediaExtension video decoders decode video formats that the system doesn't natively support. MediaExtension RAW processors work together with video decoders to allow direct control over the RAW decoding process. Developers need to build format readers, video decoders, and RAW processors as ExtensionKit bundles and embed them in a host app. Once a user installs and runs the host app, the embedded extensions become available to any app on the user's system that opts in to using them.

## Topics

### Format readers
- **MEFormatReader** - A protocol that defines the requirements for a format reader, which represents a single media asset.
- **MEFormatReaderExtension** - A protocol that defines a factory to create a new format reader with a byte source.
- **MEFormatReaderInstantiationOptions** - An object that contains options to pass to a format reader extension.
- **MEFileInfo** - An object that contains file properties from the media asset.
- [Format reader property list dictionaries](https://developer.apple.com/documentation/mediaextension/format_reader_property_list_dictionaries) - Include property list dictionaries to describe a format reader and register the formats it supports.
- [Format reader entitlement](https://developer.apple.com/documentation/mediaextension/format_reader_entitlement) - Include an entitlement to indicate your extension is a MediaExtension format reader.

### Track readers
- **METrackReader** - A protocol that defines the information to provide about a track within a media asset.
- **METrackInfo** - An object that includes track properties parsed from the media asset.

### Sample cursors
- **MESampleCursor** - A protocol that defines the information to provide about samples within a track of a media asset, and enables stepping through samples in the track in decode or presentation order.
- **MESampleLocation** - An object that provides information about the sample location with the media.
- **MESampleCursorChunk** - An object that provides information about the chunk of media at the location of a sample.
- **MEEstimatedSampleLocation** - An object that provides information about the estimated sample location with the media.
- **MEHEVCDependencyInfo** - An object that provides information about the HEVC dependency attributes of a sample.

### Byte sources
- **MEByteSource** - Provides read access to the data in a media asset file.

### Video decoders
- **MEVideoDecoder** - A protocol that defines the requirements for a video decoder.
- **MEVideoDecoderExtension** - A protocol that defines a factory to create new video decoders for a codec type that the extension implements.
- **MEDecodeFrameOptions** - An object that guides the video decoder operation on a per-frame basis.
- **MEVideoDecoderPixelBufferManager** - Describes pixel buffer requirements and creates new pixel buffers.
- [Video decoder property list dictionary](https://developer.apple.com/documentation/mediaextension/video_decoder_property_list_dictionary) - Include a property list dictionary to describe a video decoder.
- [Video decoder entitlement](https://developer.apple.com/documentation/mediaextension/video_decoder_entitlement) - Include an entitlement to indicate your extension is a MediaExtension video decoder.

### RAW processors
- **MERAWProcessor** - A protocol that defines the requirements for a RAW processor.
- **MERAWProcessorExtension** - A protocol that defines a factory to create RAW processors for a codec type that the extension implements.
- **MERAWProcessorPixelBufferManager** - Describes pixel buffer requirements and creates new pixel buffers.
- **MERAWProcessingParameter** - An object for the RAW processor to describe each processing parameter the processor exposes.
- **MERAWProcessorNotification** - Notifications that indicate a RAW processor state change.
- [RAW processor property list dictionary](https://developer.apple.com/documentation/mediaextension/raw_processor_property_list_dictionary) - Include a property list dictionary to describe a RAW processor.
- [RAW processor entitlement](https://developer.apple.com/documentation/mediaextension/raw_processor_entitlement) - Include an entitlement to indicate your extension is a MediaExtension RAW processor.

### Errors
- **MediaExtensionErrorDomain** - The domain of the error.
- **MEError** - A MediaExtension framework error.
- **Code** - An enumeration that models media extension error codes.

### Variables
- **kMERAWProcessorClassImplementationIDKey**
- **kMERAWProcessorCodecNameKey**
- **kMERAWProcessorCodecTypeKey**
- **kMERAWProcessorObjectNameKey**
- **kMERAWProcessorProcessorInfoKey**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MediaExtension)*