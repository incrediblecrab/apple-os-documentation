# Core Graphics

Harness the power of Quartz technology to perform lightweight 2D rendering with high-fidelity output. Handle path-based drawing, antialiased rendering, gradients, images, color management, PDF documents, and more.

**Platforms:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 13.1+ | macOS 10.8+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 2.0+

## Overview

The Core Graphics framework is based on the Quartz advanced drawing engine. It provides low-level, lightweight 2D rendering with unmatched output fidelity. You use this framework to handle path-based drawing, transformations, color management, offscreen rendering, patterns, gradients and shadings, image data management, image creation, and image masking, as well as PDF document creation, display, and parsing.

In macOS, Core Graphics also includes services for working with display hardware, low-level user input events, and the windowing system.

## Topics

### Geometric Data Types
- **@frozen struct CGFloat** - The basic type for floating-point scalar values in Core Graphics and related frameworks.
- **struct CGPoint**
- **struct CGSize** - A structure that contains width and height values.
- **struct CGRect**
- **struct CGVector** - A structure that contains a two-dimensional vector.
- **struct CGAffineTransform**

### 2D Drawing
- **class CGContext** - A Quartz 2D drawing environment.
- **class CGImage** - A bitmap image or image mask.
- **class CGPath** - An immutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- **class CGMutablePath** - A mutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- **class CGLayer** - An offscreen context for reusing content drawn with Core Graphics.

### Colors and Fonts
- **class CGColor** - A set of components that define a color, with a color space specifying how to interpret them.
- **class CGColorConversionInfo** - An object that describes how to convert between color spaces for use by other system services.
- **class CGColorSpace** - A profile that specifies how to interpret a color value for display.
- **class CGFont** - A set of character glyphs and layout information for drawing text.

### Working with PDF Documents
- **class CGPDFDocument** - A document that contains PDF (Portable Document Format) drawing information.

### Utility and Support Classes
- **class CGDataConsumer** - An abstraction for data-writing tasks that eliminates the need to manage a raw memory buffer.
- **class CGDataProvider** - An abstraction for data-reading tasks that eliminates the need to manage a raw memory buffer.
- **class CGShading** - A definition for a smooth transition between colors, controlled by a custom function you provide, for drawing radial and axial gradient fills.
- **class CGGradient** - A definition for a smooth transition between colors for drawing radial and axial gradient fills.
- **class CGFunction** - A general facility for defining and using callback functions.
- **class CGPattern** - A 2D pattern to be used for drawing graphics paths.

### Services
- **Quartz Display Services** - Provides direct access to features in the macOS window server for configuring and controlling display hardware.
- **Quartz Event Services** - Provides features for managing event taps—filters for observing and altering the stream of low-level user input events in macOS.
- **Quartz Window Services** - Provides information about the windows managed by the macOS window server.

### Reference
- **Core Graphics Structures**
- **Core Graphics Enumerations**
- **Core Graphics Constants**
- **Core Graphics Functions**
- **Core Graphics Data Types**
- **Classes**
  - **class CGRenderingBufferProvider**
- **Structures**
  - **struct CGBitmapParameters**
  - **struct CGColorModel**
  - **struct CGContentInfo**
- **Enumerations**
  - **enum CGBitmapLayout**
  - **enum CGComponent**
  - **enum CGContentToneMappingInfo**
  - **enum CGImageComponentInfo**

### See Also
- **Related Documentation**
  - [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreGraphics)*