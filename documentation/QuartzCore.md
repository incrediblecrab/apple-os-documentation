# Core Animation

Render, compose, and animate visual elements.

**Platforms (CALayer-based APIs):** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 13.1+ | macOS 10.5+ | tvOS 9.0+ | visionOS 1.0+

The framework landing metadata lists macOS 10.3 and watchOS 11, but those collection annotations are not [`CALayer`](https://developer.apple.com/documentation/quartzcore/calayer) minimums. Its concrete declaration starts at macOS 10.5 and does not list watchOS. Apple's installed WatchOS 26.5 SDK explicitly marks both `CALayer` and [`CACurrentMediaTime()`](https://developer.apple.com/documentation/quartzcore/cacurrentmediatime()) as `API_UNAVAILABLE(watchos)`. The root watchOS entry therefore does not make these layer and timing APIs available on Apple Watch; no earlier universal QuartzCore watchOS baseline is inferred.

## Overview

Core Animation manages much of the frame rendering for layer-based animations and can offload compositing to dedicated graphics hardware. Your app configures the layers and animation parameters and remains responsible for its layout, content updates, and other CPU work. Performance depends on the content and rendering path; using Core Animation does not guarantee a particular frame rate or eliminate CPU cost. For more details, see [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/).

## Topics

### Layer Basics

- **CALayer** - An object that manages image-based content and allows you to perform animations on that content.
- **CALayerDelegate** - Methods your app can implement to respond to layer-related events.
- **CAConstraint** - A representation of a single layout constraint between two layers.
- **CALayoutManager** - Methods that allow an object to manage the layout of a layer and its sublayers.
- **CAConstraintLayoutManager** - An object that provides a constraint-based layout manager.
- **CAAction** - An interface that allows instances to respond to actions triggered by a Core Animation layer change.

### Text, Shapes, and Gradients

- **CATextLayer** - A layer that provides simple text layout and rendering of plain or attributed strings.
- **CAShapeLayer** - A layer that draws a cubic Bezier spline in its coordinate space.
- **CAGradientLayer** - A layer that draws a color gradient over its background color, filling the shape of the layer.

### Animation

- **CAAnimation** - The abstract superclass for animations in Core Animation.
- **CAAnimationDelegate** - Methods your app can implement to respond when animations start and stop.
- **CAPropertyAnimation** - An abstract subclass for creating animations that manipulate the value of layer properties.
- **CABasicAnimation** - An object that provides basic, single-keyframe animation capabilities for a layer property.
- **CAKeyframeAnimation** - An object that provides keyframe animation capabilities for a layer object.
- **CASpringAnimation** - An animation that applies a spring-like force to a layer's properties.
- **CATransition** - An object that provides an animated transition between a layer's states.
- **CAValueFunction** - An object that provides a flexible method of defining animated transformations.

### Animation Groups

- **CAAnimationGroup** - An object that allows multiple animations to be grouped and run concurrently.
- **CATransaction** - A mechanism for grouping multiple layer-tree operations into atomic updates to the render tree.

### Animation Timing

- **CACurrentMediaTime()** - Returns the current absolute time, in seconds.
- **CAMediaTimingFunction** - A function that defines the pacing of an animation as a timing curve.
- **CAMediaTiming** - Methods that model a hierarchical timing system, allowing objects to map time between their parent and local time.
- **CADisplayLink** - A timer object that allows your app to synchronize its drawing to the refresh rate of the display.
- **CAMetalDisplayLink** - A class your Metal app uses to register for callbacks to synchronize its animations for a display.
- **CAMetalDisplayLink.Update** - Stores information about a single update from a Metal display link instance.
- **CAMetalDisplayLinkDelegate** - A protocol your app implements to respond to callbacks from Core Animation for a Metal display link.

### Particle Systems

- **CAEmitterLayer** - A layer that emits, animates, and renders a particle system.
- **CAEmitterCell** - The definition of a particle emitted by a particle layer.

### Advanced Layer Options

- **CAScrollLayer** - A layer that displays scrollable content larger than its own bounds.
- **CATiledLayer** - A layer that provides a way to asynchronously provide tiles of the layer's content, potentially cached at multiple levels of detail.
- **CATransformLayer** - Objects used to create true 3D layer hierarchies, rather than the flattened hierarchy rendering model used by other layer types.
- **CAReplicatorLayer** - A layer that creates a specified number of sublayer copies with varying geometric, temporal, and color transformations.

### Metal and OpenGL

- **CAMetalLayer** - A Core Animation layer that Metal can render into, typically displayed onscreen.
- **CAMetalDrawable** - A Metal drawable associated with a Core Animation layer.
- **CAEAGLLayer** - A layer that supports drawing OpenGL content in iOS and tvOS applications.
- [CARenderer](https://developer.apple.com/documentation/quartzcore/carenderer) - Renders a layer tree into a destination such as a Metal texture. The class is not deprecated as a whole; do not infer its status from the legacy OpenGL path.

### Deprecated

- **CAEDRMetadata** - Metadata describing how extended dynamic range (EDR) values should be tone mapped.
- **CAOpenGLLayer** - A layer that provides a layer suitable for rendering OpenGL content.

### ProMotion

- [Optimizing iPhone and iPad apps to support ProMotion displays](https://developer.apple.com/documentation/quartzcore/optimizing-iphone-and-ipad-apps-to-support-promotion-displays) - Request preferred refresh rates and synchronize animations with the system; a preference is not a guaranteed frame rate.

### Remote Display of Layer Content

- **CARemoteLayerClient** - A legacy class for cross-process rendering.
- **CARemoteLayerServer** - A legacy class for cross-process rendering.

### Transforms

- [Transforms](https://developer.apple.com/documentation/quartzcore/transforms) - Define transform matrices to apply affine transformations to layers in Core Animation.

### Quartz Composer

- **QCCompositionLayer** (Deprecated) - A layer that loads, plays, and controls Quartz Composer compositions in a Core Animation layer hierarchy.

### Reference

- [Core Animation Structures](https://developer.apple.com/documentation/quartzcore/core-animation-structures)
- [Core Animation Constants](https://developer.apple.com/documentation/quartzcore/core-animation-constants)
- [QuartzCore Functions](https://developer.apple.com/documentation/quartzcore/quartzcore-functions)
- [Core Animation Data Types](https://developer.apple.com/documentation/quartzcore/core-animation-data-types)

### See Also

#### Related Documentation

- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/QuartzCore)*
