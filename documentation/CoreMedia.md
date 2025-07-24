# Core Media

Represent time-based audio-visual assets with essential data types.

**Platforms:** iOS 4.0+ | iPadOS 4.0+ | Mac Catalyst 13.1+ | macOS 10.7+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 6.0+

## Overview

The Core Media framework defines the media pipeline used by AVFoundation and other high-level media frameworks found on Apple platforms. Use Core Media's low-level data types and interfaces to efficiently process media samples and manage queues of media data.

## Topics

### Sample Processing
- **CMSampleBuffer** - An object that contains zero or more media samples of a uniform media type.
- **CMBlockBuffer** - An object the system uses to move blocks of memory through a processing system.
- **CMTaggedBufferGroup** - Objective-C types and interfaces for working with Core Media tagged buffer groups.
- **CMFormatDescription** - A media format descriptor that describes the samples in a sample buffer.
- **CMAttachment** - Add supporting metadata to sample buffers.
- **CMTaggedBuffer** - An instance of a media buffer containing metadata tags.
- **CMMutableDataBlockBuffer** - A block buffer that provides read-write access to a range of bytes.
- **CMReadOnlyDataBlockBuffer** - A block buffer that provides read-only access to the a range of bytes.
- **CMReadySampleBuffer** - Buffer carrying readily available samples of media data.
- **CMSampleDataReference** - References sample data in at a URL.
- **CMTaggedDynamicBuffer** - Contains a collection of tags associated with a read-only media buffer.

### Time Representation
- **CMTime** - A structure that represents time.
- **CMTimeRange** - A structure that represents a range of time.
- **CMTimeMapping** - A structure that maps a segment of a source time range to a target time range.

### Media Synchronization
- **CMClock** - A reference clock you use to synchronize applications and devices.
- **CMAudioClock** - A specialized reference clock that synchronizes with audio sources.
- **CMTimebase** - A model of a timeline under application control.

### Text Markup
- **CMTextMarkup** - Attributes that specify text markup in legible media.

### Metadata
- **CMMetadata** - The APIs for working with the framework's Metadata Identifier Services and Metadata Data Type Registry.
- **CMTag** - Types and interfaces for working with Core Media tags.
- **CMTag** - A tag to set additional metadata on media buffers.
- **CMTypedTag** - A tag to set additional metadata on media buffers, with an associated Swift type for its value.
- **CMTagCollection** - Objective-C types and interfaces for working with Core Media tag collections.
- **CMProjectionType** - Constants describing the projection surface information in a 3D video buffer or channel.
- **CMStereoViewComponents** - Constants describing the stereo views contained within a buffer or channel.
- **CMStereoViewInterpretationOptions** - Create a set of stereo view interpretation options from a constant.
- **CMPackingType** - The type of packing within each video frame, if any.

### Queues
- **CMSimpleQueue** - A simple, lockless FIFO queue of elements.
- **CMBufferQueue** - A queue of timed buffers.
- **CMMemoryPool** - An object that optimizes memory allocation when working with large blocks of memory.

### Reference
- [Core Media Constants](https://developer.apple.com/documentation/coremedia/core_media_constants)
- [Core Media Functions](https://developer.apple.com/documentation/coremedia/core_media_functions)
- [Core Media Type Aliases](https://developer.apple.com/documentation/coremedia/core_media_type_aliases)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreMedia)*