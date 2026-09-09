# Metal

Render advanced 3D graphics and compute data in parallel with graphics processors.

**Platforms:** iOS 8.0+ | iPadOS 8.0+ | Mac Catalyst 13.0+ | macOS 10.11+ | tvOS 9.0+ | visionOS 1.0+

## Overview

The Metal framework gives your app direct access to a device's graphics processing unit (GPU). With Metal, apps can leverage a GPU to quickly render complex scenes and run computational tasks in parallel. For example, apps in these categories use Metal to maximize their performance:

- Games that render sophisticated 2D or 3D environments
- Video processing apps, like Final Cut Pro
- Scientific research apps that analyze and process large datasets
- Fully immersive visionOS apps

Metal works hand-in-hand with other frameworks that supplement its capability. For example, **MetalFX** provides upscaling effects that can reduce rendering cost, and **MetalKit** simplifies the tasks that display your Metal content onscreen. The **Metal Performance Shaders** framework provides a large library of optimized compute and rendering shaders designed for different GPU families. In visionOS, create fully immersive stereoscopic content with the help of the **Compositor Services** framework.

Many high-level Apple frameworks use Metal, including **RealityKit**, **SceneKit**, **SpriteKit**, and **Core Image**. These frameworks implement GPU programming details for you. Custom Metal and shader code gives you more control, but is not inherently faster; measure it against the higher-level implementation. See the Metal Shading Language Specification for shader implementation details.

## Capability checks and OS 27 regression testing

The framework's OS minimum is not a GPU feature guarantee. Query the actual `MTLDevice` with [supportsFamily(_:)](https://developer.apple.com/documentation/metal/mtldevice/supportsfamily(_:)) and the feature-specific properties needed by your renderer. Use both API availability checks and device capability checks, and retain a compatible rendering path when a feature is absent.

[MTLGPUFamily.metal4](https://developer.apple.com/documentation/metal/mtlgpufamily/metal4) is available from the OS 26 SDKs, not newly introduced in OS 27. The [Metal 4 core API guide](https://developer.apple.com/documentation/metal/understanding-the-metal-4-core-api) describes incremental adoption alongside existing `MTLCommandQueue` code. In particular, Metal 4 command buffers do not strongly retain their resources; manage resource lifetimes and reset command allocators only after their GPU work completes.

The **Beta 8** [iOS and iPadOS](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes#Metal), [macOS](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes#Metal), and [visionOS](https://developer.apple.com/documentation/visionos-release-notes/visionos-27-release-notes#Metal) notes checked September 8, 2026 mark clamp-to-edge sampler results incorrectly becoming zero as **resolved** (172520325), including the separate Apple 10 GPU-family report (177318505).

Use edge-sampling images and the affected GPU families in regression tests. These resolved issues are not a reason to describe clamp-to-edge addressing as unsupported or to impose a permanent all-device shader workaround. Profile render timing, synchronization, and memory on actual hardware; Simulator is not a substitute for a target GPU.

## Topics

### Essentials
Begin with the Metal fundamentals.
- [Understanding the Metal 4 core API](https://developer.apple.com/documentation/metal/understanding-the-metal-4-core-api) - Discover the features and functionality in the Metal 4 foundational APIs.
- [Drawing a triangle with Metal 4](https://developer.apple.com/documentation/metal/drawing-a-triangle-with-metal-4) - Follow the current sample's render-command and frame-lifetime workflow. This sample requires the Metal 4-era SDK and supported Apple silicon GPU, not merely Metal's original framework minimum.
- [Performing Calculations on a GPU](https://developer.apple.com/documentation/metal/performing-calculations-on-a-gpu) - Use Metal to find GPUs and perform calculations on them.
- [Using Metal to Draw a View's Contents](https://developer.apple.com/documentation/metal/using-metal-to-draw-a-view's-contents) - Create a MetalKit view and a render pass to draw the view's contents.

### Samples
Discover graphics techniques and Metal features through sample code projects.
- [Metal Sample Code Library](https://developer.apple.com/documentation/metal/metal-sample-code-library) - Explore the complete set of Metal samples.

### GPU Devices
Start with a Metal device instance to begin working with the GPU it represents.
- [GPU Devices and Work Submission](https://developer.apple.com/documentation/metal/gpu-devices-and-work-submission) - Find any available GPU, submit work to it with command buffers, suspend work, and coordinate between multiple GPUs.

### Command Encoders
Send work to a GPU by issuing commands and configuring the pipeline states for those commands.

### Render Passes
- [Render Passes](https://developer.apple.com/documentation/metal/render-passes) - Encode a render pass to draw graphics into an image.

### Compute Passes
- [Compute Passes](https://developer.apple.com/documentation/metal/compute-passes) - Encode a compute pass that runs computations in parallel on a thread grid, processing and manipulating Metal resource data on multiple cores of a GPU.

### Machine-Learning Passes
- [Machine-Learning Passes](https://developer.apple.com/documentation/metal/machine-learning-passes) - Add machine-learning model inference to your Metal app's GPU workflow.

### Blit Passes
- [Blit Passes](https://developer.apple.com/documentation/metal/blit-passes) - Encode a block information transfer pass to adjust and copy data to and from GPU resources, such as buffers and textures.

### Indirect Command Encoding
- [Indirect Command Encoding](https://developer.apple.com/documentation/metal/indirect-command-encoding) - Store draw commands in Metal buffers and run them at a later time on the GPU, either once or repeatedly.

### Ray Tracing with Acceleration Structures
- [Ray Tracing with Acceleration Structures](https://developer.apple.com/documentation/metal/ray-tracing-with-acceleration-structures) - Build a representation of your scene's geometry using triangles and bounding volumes to quickly trace rays through the scene.

### Resources
Store data in buffers and textures, and optionally manage the underlying GPU memory yourself.
- [Resource Fundamentals](https://developer.apple.com/documentation/metal/resource-fundamentals) - Control the common attributes of all Metal memory resources, including buffers and textures, and how to configure their underlying memory.
- [Buffers](https://developer.apple.com/documentation/metal/buffers) - Create and manage untyped data your app uses to exchange information with its shader functions.
- [Textures](https://developer.apple.com/documentation/metal/textures) - Create and manage typed data your app uses to exchange information with its shader functions.
- [Memory Heaps](https://developer.apple.com/documentation/metal/memory-heaps) - Take control of your app's GPU memory management by creating a large memory allocation for various buffers, textures, and other resources.
- [Resource Loading](https://developer.apple.com/documentation/metal/resource-loading) - Load assets in your games and apps quickly by running a dedicated input/output queue alongside your GPU tasks.
- [Resource Synchronization](https://developer.apple.com/documentation/metal/resource-synchronization) - Prevent multiple commands that can access the same resources simultaneously by coordinating those accesses with barriers, fences, or events.

### Shader Compilation and Libraries
Compile and organize shaders, the GPU functions that run on a Metal device's execution units.
- [Using the Metal 4 compilation API](https://developer.apple.com/documentation/metal/using-the-metal-4-compilation-api) - Control when and how you compile an app's shaders.
- [Shader Libraries](https://developer.apple.com/documentation/metal/shader-libraries) - Manage and load your app's Metal shaders.
- [Using Function Specialization to Build Pipeline Variants](https://developer.apple.com/documentation/metal/using-function-specialization-to-build-pipeline-variants) - Create pipelines for different levels of detail from a common shader source.

### Presentation
Display standard or high-dynamic-range content on a device's display with Core Animation or MetalKit, in standard or high dynamic range.
- [Managing your game window for Metal in macOS](https://developer.apple.com/documentation/metal/managing-your-game-window-for-metal-in-macos) - Set up a window and view for optimally displaying your Metal content.
- [Adapting your game interface for smaller screens](https://developer.apple.com/documentation/metal/adapting-your-game-interface-for-smaller-screens) - Make text legible on all devices the player chooses to run your game on.
- [Onscreen Presentation](https://developer.apple.com/documentation/metal/onscreen-presentation) - Show the output from a GPU's rendering pass to the user in your app.
- [HDR Content](https://developer.apple.com/documentation/metal/hdr-content) - Take advantage of high dynamic range to present more vibrant colors in your apps and games.

### Developer Tools
Identify and fix issues with your app's Metal API calls, shader code, resources, and performance during development by using Metal Debugger.
- [Supporting Simulator in a Metal app](https://developer.apple.com/documentation/metal/supporting-simulator-in-a-metal-app) - Configure alternative render paths in your Metal app to enable running your app in Simulator.
- [Capturing Metal Commands Programmatically](https://developer.apple.com/documentation/metal/capturing-metal-commands-programmatically) - Invoke a Metal frame capture from your app, then save the resulting GPU trace to a file or view it in Xcode.
- [Logging shader debug messages](https://developer.apple.com/documentation/metal/logging-shader-debug-messages) - Print debugging messages that a shader generates using shader logging.
- [Developing Metal apps that run in Simulator](https://developer.apple.com/documentation/metal/developing-metal-apps-that-run-in-simulator) - Prototype and test your Metal apps in Simulator.
- [Improving your game's graphics performance and settings](https://developer.apple.com/documentation/metal/improving-your-games-graphics-performance-and-settings) - Fix performance glitches and develop default settings for smooth experiences on Apple platforms using the powerful suite of Metal development tools.
- [Metal debugger](https://developer.apple.com/documentation/xcode/metal-debugger) - Debug and profile your Metal workload with a GPU trace.
- [Metal developer workflows](https://developer.apple.com/documentation/xcode/metal-developer-workflows) - Locate and fix issues related to your app's use of the Metal API and GPU functions.
- [GPU Counters and Counter Sample Buffers](https://developer.apple.com/documentation/metal/gpu-counters-and-counter-sample-buffers) - Retrieve runtime data from a GPU device by sampling one or more of its counters.
- [Metal Debugging Types](https://developer.apple.com/documentation/metal/metal-debugging-types) - Create capture managers and capture scopes, and review a GPU device's log after it runs a command buffer.

### Apple Silicon
Take advantage of the unique architecture of Apple silicon GPUs.
- [Porting your Metal code to Apple silicon](https://developer.apple.com/documentation/apple-silicon/porting-your-metal-code-to-apple-silicon) - Create a version of your Metal app that runs on both Apple silicon and Intel-based Mac computers.
- [Tailor Your Apps for Apple GPUs and Tile-Based Deferred Rendering](https://developer.apple.com/documentation/metal/tailor-your-apps-for-apple-gpus-and-tile-based-deferred-rendering) - Learn about characteristic Apple GPU features, including imageblocks, tile shaders, and raster order groups.

### Reference
- **Metal Structures**
- **Metal Enumerations**
- **Metal Constants**
- **Metal Data Types**
- **Metal Variables**

### Articles
- [Achieving smooth frame rates with a Metal display link](https://developer.apple.com/documentation/metal/achieving-smooth-frame-rates-with-a-metal-display-link) - Pace rendering with minimal input latency while providing essential information to the operating system for power-efficient rendering, thermal mitigation, and the scheduling of sustainable workloads.

### Structures
- **MTL4CommandQueueError**
### Type Aliases
- **MTLGPUAddress** - A 64-bit unsigned integer type appropriate for storing GPU addresses.

### See Also
- **Metal Programming Guide**
- **Metal Best Practices Guide**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Metal)*
