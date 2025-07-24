# Core Image

Use built-in or custom filters to process still and video images.

**Platforms:** iOS 5.0+ | iPadOS 5.0+ | Mac Catalyst 13.1+ | macOS 10.11+ | tvOS 9.0+ | visionOS 1.0+

## Overview

Core Image is an image processing and analysis technology that provides high-performance processing for still and video images. Use the many built-in image filters to process images and build complex effects by chaining filters. For a list of all the built-in filters see the Filter Catalog.

You can also create new effects with custom filters and image processors; see Custom Filters.

## Topics

### Essentials
- [Processing an Image Using Built-in Filters](https://developer.apple.com/documentation/coreimage/processing_an_image_using_built-in_filters) - Apply effects such as sepia tint, highlight strengthening, and scaling to images.
- **class CIContext** - An evaluation context for rendering image processing results and performing image analysis.
- **class CIImage** - A representation of an image to be processed or produced by Core Image filters.

### Filters
- **class CIFilter** - An image processor that produces an image by manipulating one or more input images or by generating new image data.
- **class CIRAWFilter** - A filter subclass that produces an image by manipulating RAW image sensor data from a digital camera or scanner.
- **class CIColor** - The component values defining a color in a specific color space.
- **class CIVector** - A container for coordinate values, direction vectors, matrices, and other non-scalar values, typically used in Core Image for filter parameters.

### Filter Catalog
- [Blur Filters](https://developer.apple.com/documentation/coreimage/blur_filters) - Apply blurs, simulate motion and zoom effects, reduce noise, and erode and dilate image regions.
- [Color Adjustment Filters](https://developer.apple.com/documentation/coreimage/color_adjustment_filters) - Apply color transformations, including exposure, hue, and tint adjustments.
- [Color Effect Filters](https://developer.apple.com/documentation/coreimage/color_effect_filters) - Apply color effects, including photo effects, dithering, and color maps.
- [Composite Operations](https://developer.apple.com/documentation/coreimage/composite_operations) - Composite images by using a range of blend modes and compositing operators.
- [Convolution Filters](https://developer.apple.com/documentation/coreimage/convolution_filters) - Produce effects such as blurring, sharpening, edge detection, translation, and embossing.
- [Distortion Filters](https://developer.apple.com/documentation/coreimage/distortion_filters) - Apply distortion to images.
- [Generator Filters](https://developer.apple.com/documentation/coreimage/generator_filters) - Generate barcode, geometric, and special-effect images.
- [Geometry Adjustment Filters](https://developer.apple.com/documentation/coreimage/geometry_adjustment_filters) - Translate, scale, and rotate images in 2D and 3D.
- [Gradient Filters](https://developer.apple.com/documentation/coreimage/gradient_filters) - Generate linear and radial gradients.
- [Halftone Effect Filters](https://developer.apple.com/documentation/coreimage/halftone_effect_filters) - Simulate monochrome and CMYK halftone screens.
- [Reduction Filters](https://developer.apple.com/documentation/coreimage/reduction_filters) - Create statistical information about an image.
- [Sharpening Filters](https://developer.apple.com/documentation/coreimage/sharpening_filters) - Apply sharpening to images.
- [Stylizing Filters](https://developer.apple.com/documentation/coreimage/stylizing_filters) - Create stylized versions of images by applying effects including pixelation and line overlays.
- [Tile Effect Filters](https://developer.apple.com/documentation/coreimage/tile_effect_filters) - Produce tiled images from source images.
- [Transition Filters](https://developer.apple.com/documentation/coreimage/transition_filters) - Transition between two images by using effects including page curl and swipe.

### Filter Recipes
- [Applying a Chroma Key Effect](https://developer.apple.com/documentation/coreimage/applying_a_chroma_key_effect) - Replace a color in one image with the background from another.
- [Selectively Focusing on an Image](https://developer.apple.com/documentation/coreimage/selectively_focusing_on_an_image) - Focus on a part of an image by applying Gaussian blur and gradient masks.
- [Customizing Image Transitions](https://developer.apple.com/documentation/coreimage/customizing_image_transitions) - Transition between images in creative ways using Core Image filters.
- [Simulating Scratchy Analog Film](https://developer.apple.com/documentation/coreimage/simulating_scratchy_analog_film) - Degrade the quality of an image to make it look like dated, analog film.

### Custom Filters
- [Writing Custom Kernels](https://developer.apple.com/documentation/coreimage/writing_custom_kernels) - Write your own custom kernels in either the Core Image Kernel Language or the Metal Shading Language.
- **class CIKernel** - A GPU-based image-processing routine used to create custom Core Image filters.
- **class CIColorKernel** - A GPU-based image-processing routine that processes only the color information in images, used to create custom Core Image filters.
- **class CIWarpKernel** - A GPU-based image-processing routine that processes only the geometry information in an image, used to create custom Core Image filters.
- **class CIBlendKernel** - A GPU-based image-processing routine that is optimized for blending two images.
- **class CISampler** - An object that retrieves pixel samples for processing by a filter kernel.
- **class CIFilterShape** - A description of the bounding shape of a filter and the domain of definition for a filter operation.
- **struct CIFormat** - Pixel data formats for image input, output, and processing.

### Custom Image Processors
- **class CIImageProcessorKernel** - The abstract class you extend to create custom image processors that can integrate with Core Image workflows.
- **protocol CIImageProcessorInput** - A container of image data and information for use in a custom image processor.
- **protocol CIImageProcessorOutput** - A container for writing image data and information produced by a custom image processor.

### Custom Render Destination
- [Generating an animation with a Core Image Render Destination](https://developer.apple.com/documentation/coreimage/generating_an_animation_with_a_core_image_render_destination) - Animate a filtered image to a Metal view in a SwiftUI app using a Core Image Render Destination.
- **class CIRenderDestination** - A specification for configuring all attributes of a render task's destination and issuing asynchronous render tasks.
- **class CIRenderInfo** - An encapsulation of a render task's timing, passes, and pixels processed.
- **class CIRenderTask** - A single render task.
- **enum CIRenderDestinationAlphaMode** - Different ways of representing alpha.

### Feedback-Based Processing
- **class CIImageAccumulator** - An object that manages feedback-based image processing for tasks such as painting or fluid simulation.

### Barcode Descriptions
- **class CIBarcodeDescriptor** - An abstract base class that represents a machine-readable code's attributes.
- **class CIQRCodeDescriptor** - A square QR code symbol.
- **class CIAztecCodeDescriptor** - An Aztec code symbol.
- **class CIPDF417CodeDescriptor** - A PDF417 symbol.
- **class CIDataMatrixCodeDescriptor** - A Data Matrix code symbol.

### Image Feature Detection
- **class CIDetector** - An image processor that identifies notable features, such as faces and barcodes, in a still image or video.
- **class CIFeature** - The abstract superclass for objects representing notable features detected in an image.
- **class CIFaceFeature** - Information about a face detected in a still or video image.
- **class CIRectangleFeature** - Information about a rectangular region detected in a still or video image.
- **class CITextFeature** - Information about a region likely to contain text detected in a still or video image.
- **class CIQRCodeFeature** - Information about a Quick Response code detected in a still or video image.

### Image Units
- **class CIPlugIn** - The mechanism for loading image units in macOS.
- **class CIFilterGenerator** - An object that creates and configures chains of individual image filters.
- **protocol CIPlugInRegistration** - The interface for loading Core Image image units.
- **protocol CIFilterConstructor** - A general interface for objects that produce filters.

### Reference
- **Core Image Constants**

### Variables
- **let kCIInputBacksideImageKey: String** - A key to get or set the backside image for a transition Core Image filter.
- **let kCIInputBiasVectorKey: String** - A key to get or set the vector bias value of a Core Image filter.
- **let kCIInputColor0Key: String** - A key to get or set a color value of a Core Image filter.
- **let kCIInputColor1Key: String** - A key to get or set a color value of a Core Image filter.
- **let kCIInputColorSpaceKey: String** - A key to get or set a color space value of a Core Image filter.
- **let kCIInputCountKey: String** - A key to get or set the scalar count value of a Core Image filter.
- **let kCIInputExtrapolateKey: String** - A key to get or set the boolean behavior of a Core Image filter that specifies if the filter should extrapolate a table beyond the defined range. The value for this key needs to be an NSNumber instance.
- **let kCIInputPaletteImageKey: String** - A key to get or set the palette image for a Core Image filter.
- **let kCIInputPerceptualKey: String** - A key to get or set the boolean behavior of a Core Image filter that specifies if the filter should operate in linear or perceptual colors. The value for this key needs to be an NSNumber instance.
- **let kCIInputPoint0Key: String** - A key to get or set the coordinate value of a Core Image filter. The value for this key needs to be a CIVector instance containing the x,y coordinate.
- **let kCIInputPoint1Key: String** - A key to get or set a coordinate value of a Core Image filter. The value for this key needs to be a CIVector instance containing the x,y coordinate.
- **let kCIInputRadius0Key: String** - A key to get or set the geometric radius value of a Core Image filter.
- **let kCIInputRadius1Key: String** - A key to get or set the geometric radius value of a Core Image filter.
- **let kCIInputThresholdKey: String** - A key to get or set the scalar threshold value of a Core Image filter.

### See Also
- **Related Documentation**
  - [Core Image Filter Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html)
  - [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreImage)*