# Image I/O

Read and write most image file formats, and access an image's metadata.

**Platforms:** iOS 4.0+ | iPadOS 4.0+ | Mac Catalyst 13.0+ | macOS 10.8+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 2.0+

## Overview

The Image I/O framework allows applications to read and write most image file formats. This framework offers high efficiency, color management, and access to image metadata.

For more information, see Image I/O Programming Guide.

## Topics

### Image Management
- **CGImageSource** - An opaque type that you use to read image data from a URL, data object, or data consumer.
- **CGImageDestination** - An opaque type that you use to write image data to a URL, data object, or data consumer.

### XMP Metadata
- **CGImageMetadata** - An immutable object that contains the XMP metadata associated with an image.
- **CGMutableImageMetadata** - An opaque type for adding or modifying image metadata.
- **CGImageMetadataTag** - An immutable type that contains information about a single piece of image metadata.
- [XMP Namespaces and Prefixes](https://developer.apple.com/documentation/imageio/xmp_namespaces_and_prefixes) - Discover the public namespaces and prefixes that exist in XMP metadata tags.
- **kCFErrorDomainCGImageMetadata** - The domain for metadata-related errors that originate in the Image I/O framework.
- **CGImageMetadataErrors** - Constants for errors that occur when getting or setting metadata information.

### Common Image Properties
- [Image Properties](https://developer.apple.com/documentation/imageio/image_properties) - Properties that apply to the container in general, and not necessarily to an individual image in the container.
- [EXIF Dictionary Keys](https://developer.apple.com/documentation/imageio/exif_dictionary_keys) - Metadata keys for Exchangeable Image File Format (EXIF) data.
- [IPTC Dictionary Keys](https://developer.apple.com/documentation/imageio/iptc_dictionary_keys) - Metadata keys for International Press Telecommunications Council (IPTC) data.
- [GPS Dictionary Keys](https://developer.apple.com/documentation/imageio/gps_dictionary_keys) - Keys for Global Positioning System (GPS) information.
- [WebP Data](https://developer.apple.com/documentation/imageio/webp_data) - Metadata keys for WebP metadata.

### Format-Specific Properties
- [CIFF Image Properties](https://developer.apple.com/documentation/imageio/ciff_image_properties) - Metadata keys for the Camera Image File Format (CIFF) image format.
- [DNG Image Properties](https://developer.apple.com/documentation/imageio/dng_image_properties) - Metadata keys for the Digital Negative (DNG) archival format.
- [GIF Image Properties](https://developer.apple.com/documentation/imageio/gif_image_properties) - Metadata keys for the Graphics Interchange Format (GIF).
- [HEIC Image Properties](https://developer.apple.com/documentation/imageio/heic_image_properties) - Metadata keys for the High Efficiency Image Container (HEIC) format.
- [JFIF Image Properties](https://developer.apple.com/documentation/imageio/jfif_image_properties) - Metadata keys for the JPEG File Interchange Format (JFIF).
- [PNG Image Properties](https://developer.apple.com/documentation/imageio/png_image_properties) - Metadata keys for the Portable Network Graphics (PNG) format.
- [TGA Image Properties](https://developer.apple.com/documentation/imageio/tga_image_properties) - Metadata keys for the Truevision Graphics Adapter (TGA) format.
- [TIFF Image Properties](https://developer.apple.com/documentation/imageio/tiff_image_properties) - Metadata keys for the Tagged Image File Format (TIFF).
- [8BIM Image Properties](https://developer.apple.com/documentation/imageio/8bim_image_properties) - Metadata keys for the Adobe Photoshop image format.

### Manufacturer-Specific Properties
- [Nikon Camera Dictionary Keys](https://developer.apple.com/documentation/imageio/nikon_camera_dictionary_keys) - Metadata keys for an image from a Nikon camera.
- [Canon Camera Dictionary Keys](https://developer.apple.com/documentation/imageio/canon_camera_dictionary_keys) - Metadata keys for an image from a Canon camera.
- **kCGImagePropertyMakerAppleDictionary** - A dictionary of key-value pairs for an image from an Apple camera.
- **kCGImagePropertyMakerMinoltaDictionary** - A dictionary of key-value pairs for an image from a Minolta camera.
- **kCGImagePropertyMakerFujiDictionary** - A dictionary of key-value pairs for an image from a Fuji camera.
- **kCGImagePropertyMakerOlympusDictionary** - A dictionary of key-value pairs for an image from a Olympus camera.
- **kCGImagePropertyMakerPentaxDictionary** - A dictionary of key-value pairs for an image from a Pentax camera.
- **kCGImagePropertyRawDictionary** - A dictionary of key-value pairs for an image that contains minimally processed, or raw, data.

### Spatial Photos
- [Writing spatial photos](https://developer.apple.com/documentation/imageio/writing_spatial_photos) - Create spatial photos for visionOS by packaging a pair of left- and right-eye images as a stereo HEIC file with related spatial metadata.
- [Creating spatial photos and videos with spatial metadata](https://developer.apple.com/documentation/imageio/creating_spatial_photos_and_videos_with_spatial_metadata) - Add spatial metadata to stereo photos and videos to create spatial media for viewing on Apple Vision Pro.

### Animations
- **CGAnimateImageAtURLWithBlock** - Animate the sequence of images in the Graphics Interchange Format (GIF) or Animated Portable Network Graphics (APNG) file at the specified URL.
- **CGAnimateImageDataWithBlock** - Animate the sequence of images using data from a Graphics Interchange Format (GIF) or Animated Portable Network Graphics (APNG) file file.
- **CGImageSourceAnimationBlock** - The block to execute for each frame of an image animation.
- **kCGImageAnimationStartIndex** - A property that specifies the index of the first frame of an animation.
- **kCGImageAnimationDelayTime** - The number of seconds to wait before displaying the next image in an animated sequence.
- **kCGImageAnimationLoopCount** - The number of times to repeat the animated sequence.
- **CGImageAnimationStatus** - Constants that indicate the result of animating an image sequence.

### Reference
- [Image I/O Constants](https://developer.apple.com/documentation/imageio/image_i_o_constants)
- [Image I/O Functions](https://developer.apple.com/documentation/imageio/image_i_o_functions)
- [Image I/O Macros](https://developer.apple.com/documentation/imageio/image_i_o_macros)

### Variables
- **kCGComputeHDRStats** (Beta)
- **kCGImageDestinationEncodeAlternateColorSpace** (Beta)
- **kCGImageDestinationEncodeBaseColorSpace** (Beta)
- **kCGImageDestinationEncodeBaseIsSDR**
- **kCGImageDestinationEncodeBasePixelFormatRequest** (Beta)
- **kCGImageDestinationEncodeGainMapPixelFormatRequest** (Beta)
- **kCGImageDestinationEncodeGainMapSubsampleFactor** (Beta)
- **kCGImageDestinationEncodeGenerateGainMapWithBaseImage** (Beta)
- **kCGImageDestinationEncodeIsBaseImage** (Beta)
- **kCGImageDestinationEncodeRequest**
- **kCGImageDestinationEncodeRequestOptions**
- **kCGImageDestinationEncodeToISOGainmap**
- **kCGImageDestinationEncodeToISOHDR**
- **kCGImageDestinationEncodeToSDR**
- **kCGImageDestinationEncodeTonemapMode**
- **kCGImagePropertyASTCBlockSize**
- **kCGImagePropertyASTCBlockSize4x4** (Beta)
- **kCGImagePropertyASTCBlockSize8x8** (Beta)
- **kCGImagePropertyASTCEncoder**
- **kCGImagePropertyBCEncoder**
- **kCGImagePropertyBCFormat**
- **kCGImagePropertyEncoder**
- **kCGImagePropertyOpenEXRCompression**
- **kCGImagePropertyPVREncoder**
- **kCGImageProviderPreferredTileHeight** (Beta)
- **kCGImageProviderPreferredTileWidth** (Beta)
- **kCGImageSourceGenerateImageSpecificLumaScaling**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ImageIO)*