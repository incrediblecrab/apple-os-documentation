# Core Animation

Render, compose, and animate visual elements.

**Platforms:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 13.1+ | macOS 10.3+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 11.0+

## Overview

Core Animation provides high frame rates and smooth animations without burdening the CPU or slowing down your app. Core Animation does most of the work of drawing each frame of an animation for you. You're responsible for configuring the animation parameters, such as the start and end points, and Core Animation does the rest. It accelerates the rendering by handing over most of the work to dedicated graphics hardware. For more details, see [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/).

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
- **Update** - Stores information about a single update from a Metal display link instance.
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

### Deprecated

- **CAEDRMetadata** - Metadata describing how extended dynamic range (EDR) values should be tone mapped.
- **CAOpenGLLayer** - A layer that provides a layer suitable for rendering OpenGL content.
- **CARenderer** - A layer that allows an application to render a layer tree into a Core OpenGL context.

### ProMotion

- [Optimizing ProMotion refresh rates for iPhone 13 Pro and iPad Pro](https://developer.apple.com/documentation/quartzcore/optimizing_promotion_refresh_rates_for_iphone_13_pro_and_ipad_pro) - Provide custom animated content for ProMotion displays.

### Remote Display of Layer Content

- **CARemoteLayerClient** - A legacy class for cross-process rendering.
- **CARemoteLayerServer** - A legacy class for cross-process rendering.

### Transforms

- [Transforms](https://developer.apple.com/documentation/quartzcore/transforms) - Define transform matrices to apply affine transformations to layers in Core Animation.

### Quartz Composer

- **QCCompositionLayer** (Deprecated) - A layer that loads, plays, and controls Quartz Composer compositions in a Core Animation layer hierarchy.

### Reference

- [Core Animation Structures](https://developer.apple.com/documentation/quartzcore/structures)
- [Core Animation Constants](https://developer.apple.com/documentation/quartzcore/constants)
- [QuartzCore Functions](https://developer.apple.com/documentation/quartzcore/functions)
- [Core Animation Data Types](https://developer.apple.com/documentation/quartzcore/data_types)

### See Also

#### Related Documentation

- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/QuartzCore)*