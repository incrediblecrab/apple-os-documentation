# Image I/O

Read and write most image file formats, and access an image's metadata.

**Platforms:** iOS 4.0+ | iPadOS 4.0+ | Mac Catalyst 13.1+ | macOS 10.4+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 2.0+

These minimums describe the longstanding image-source path. The landing page currently annotates macOS 10.8 and Mac Catalyst 13.0, while [`CGImageSourceCreateWithDataProvider(_:_:)`](https://developer.apple.com/documentation/imageio/cgimagesourcecreatewithdataprovider(_:_:)) explicitly specifies macOS 10.4 and Mac Catalyst 13.1. The macOS SDK declaration also gives 10.4. Neither the landing annotation nor this older image-reading baseline determines the availability of every metadata and encoding API below.

## Overview

The Image I/O framework allows applications to read and write most image file formats. This framework offers high efficiency, color management, and access to image metadata.

For more information, see Image I/O Programming Guide.

## Topics

### Image Management

- **CGImageSource** - An opaque type that you use to read image data from a URL, data object, or data provider.
- **CGImageDestination** - An opaque type that you use to write image data to a URL, data object, or data consumer.

### XMP Metadata

- **CGImageMetadata** - An immutable object that contains the XMP metadata associated with an image.
- **CGMutableImageMetadata** - An opaque type for adding or modifying image metadata.
- **CGImageMetadataTag** - An immutable type that contains information about a single piece of image metadata.
- [XMP Namespaces and Prefixes](https://developer.apple.com/documentation/imageio/xmp-namespaces-and-prefixes) - Discover the public namespaces and prefixes that exist in XMP metadata tags.
- **kCFErrorDomainCGImageMetadata** - The domain for metadata-related errors that originate in the Image I/O framework.
- **CGImageMetadataErrors** - Constants for errors that occur when getting or setting metadata information.

### Common Image Properties

- [Image Properties](https://developer.apple.com/documentation/imageio/image-properties) - Properties that apply to the container in general, and not necessarily to an individual image in the container.
- [EXIF Dictionary Keys](https://developer.apple.com/documentation/imageio/exif-dictionary-keys) - Metadata keys for Exchangeable Image File Format (EXIF) data.
- [IPTC Dictionary Keys](https://developer.apple.com/documentation/imageio/iptc-dictionary-keys) - Metadata keys for International Press Telecommunications Council (IPTC) data.
- [GPS Dictionary Keys](https://developer.apple.com/documentation/imageio/gps-dictionary-keys) - Keys for Global Positioning System (GPS) information.
- [WebP Data](https://developer.apple.com/documentation/imageio/webp-data) - Metadata keys for WebP metadata.

### Format-Specific Properties

- [CIFF Image Properties](https://developer.apple.com/documentation/imageio/ciff-image-properties) - Metadata keys for the Camera Image File Format (CIFF) image format.
- [DNG Image Properties](https://developer.apple.com/documentation/imageio/dng-image-properties) - Metadata keys for the Digital Negative (DNG) archival format.
- [GIF Image Properties](https://developer.apple.com/documentation/imageio/gif-image-properties) - Metadata keys for the Graphics Interchange Format (GIF).
- [HEIC Image Properties](https://developer.apple.com/documentation/imageio/heic-image-properties) - Metadata keys for the High Efficiency Image Container (HEIC) format.
- [JFIF Image Properties](https://developer.apple.com/documentation/imageio/jfif-image-properties) - Metadata keys for the JPEG File Interchange Format (JFIF).
- [PNG Image Properties](https://developer.apple.com/documentation/imageio/png-image-properties) - Metadata keys for the Portable Network Graphics (PNG) format.
- [TGA Image Properties](https://developer.apple.com/documentation/imageio/tga-image-properties) - Metadata keys for the Truevision Graphics Adapter (TGA) format.
- [TIFF Image Properties](https://developer.apple.com/documentation/imageio/tiff-image-properties) - Metadata keys for the Tagged Image File Format (TIFF).
- [8BIM Image Properties](https://developer.apple.com/documentation/imageio/8bim-image-properties) - Metadata keys for the Adobe Photoshop image format.

### Manufacturer-Specific Properties

- [Nikon Camera Dictionary Keys](https://developer.apple.com/documentation/imageio/nikon-camera-dictionary-keys) - Metadata keys for an image from a Nikon camera.
- [Canon Camera Dictionary Keys](https://developer.apple.com/documentation/imageio/canon-camera-dictionary-keys) - Metadata keys for an image from a Canon camera.
- **kCGImagePropertyMakerAppleDictionary** - A dictionary of key-value pairs for an image from an Apple camera.
- **kCGImagePropertyMakerMinoltaDictionary** - A dictionary of key-value pairs for an image from a Minolta camera.
- **kCGImagePropertyMakerFujiDictionary** - A dictionary of key-value pairs for an image from a Fuji camera.
- **kCGImagePropertyMakerOlympusDictionary** - A dictionary of key-value pairs for an image from a Olympus camera.
- **kCGImagePropertyMakerPentaxDictionary** - A dictionary of key-value pairs for an image from a Pentax camera.
- **kCGImagePropertyRawDictionary** - A dictionary of key-value pairs for an image that contains minimally processed, or raw, data.

### Spatial Photos

- [Writing spatial photos](https://developer.apple.com/documentation/imageio/writing-spatial-photos) - Create spatial photos for visionOS by packaging a pair of left- and right-eye images as a stereo HEIC file with related spatial metadata.
- [Creating spatial photos and videos with spatial metadata](https://developer.apple.com/documentation/imageio/creating-spatial-photos-and-videos-with-spatial-metadata) - Add spatial metadata to stereo photos and videos to create spatial media for viewing on Apple Vision Pro.

### Animations

- **CGAnimateImageAtURLWithBlock** - Animate the sequence of images in the Graphics Interchange Format (GIF) or Animated Portable Network Graphics (APNG) file at the specified URL.
- **CGAnimateImageDataWithBlock** - Animate the sequence of images using data from a Graphics Interchange Format (GIF) or Animated Portable Network Graphics (APNG) file.
- **CGImageSourceAnimationBlock** - The block to execute for each frame of an image animation.
- **kCGImageAnimationStartIndex** - A property that specifies the index of the first frame of an animation.
- **kCGImageAnimationDelayTime** - The number of seconds to wait before displaying the next image in an animated sequence.
- **kCGImageAnimationLoopCount** - The number of times to repeat the animated sequence.
- **CGImageAnimationStatus** - Constants that indicate the result of animating an image sequence.

### Reference

- [Image I/O Constants](https://developer.apple.com/documentation/imageio/image-i-o-constants)
- [Image I/O Functions](https://developer.apple.com/documentation/imageio/image-i-o-functions)
- [Image I/O Macros](https://developer.apple.com/documentation/imageio/image-i-o-macros)

### Variables

- **kCGComputeHDRStats**
- **kCGImageDestinationEncodeAlternateColorSpace**
- **kCGImageDestinationEncodeBaseColorSpace**
- **kCGImageDestinationEncodeBaseIsSDR**
- **kCGImageDestinationEncodeBasePixelFormatRequest**
- **kCGImageDestinationEncodeGainMapPixelFormatRequest**
- **kCGImageDestinationEncodeGainMapSubsampleFactor**
- **kCGImageDestinationEncodeGenerateGainMapWithBaseImage**
- **kCGImageDestinationEncodeIsBaseImage**
- **kCGImageDestinationEncodeRequest**
- **kCGImageDestinationEncodeRequestOptions**
- **kCGImageDestinationEncodeToISOGainmap**
- **kCGImageDestinationEncodeToISOHDR**
- **kCGImageDestinationEncodeToSDR**
- **kCGImageDestinationEncodeTonemapMode**
- **kCGImagePropertyASTCBlockSize**
- **kCGImagePropertyASTCBlockSize4x4**
- **kCGImagePropertyASTCBlockSize8x8**
- **kCGImagePropertyASTCEncoder**
- **kCGImagePropertyBCEncoder**
- **kCGImagePropertyBCFormat**
- **kCGImagePropertyEncoder**
- **kCGImagePropertyOpenEXRCompression**
- **kCGImagePropertyPVREncoder**
- **kCGImageProviderPreferredTileHeight**
- **kCGImageProviderPreferredTileWidth**
- **kCGImageSourceGenerateImageSpecificLumaScaling**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ImageIO)*
