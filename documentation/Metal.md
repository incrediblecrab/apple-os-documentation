# Metal

Render advanced 3D graphics and compute data in parallel with graphics processors.

**Platforms:** iOS 8.0+ | iPadOS 8.0+ | Mac Catalyst 13.0+ | macOS 10.11+ | tvOS 9.0+ | visionOS 1.0+

## Overview

The Metal framework gives your app direct access to a device's graphics processing unit (GPU). With Metal, apps can leverage a GPU to quickly render complex scenes and run computational tasks in parallel. For example, apps in these categories use Metal to maximize their performance:

- Games that render sophisticated 2D or 3D environments
- Video processing apps, like Final Cut Pro
- Scientific research apps that analyze and process large datasets
- Fully immersive visionOS apps

Metal works hand-in-hand with other frameworks that supplement its capability. For example, **MetalFX** upscales your renderings in less time than rendering them natively, and **MetalKit** simplifies the tasks that display your Metal content onscreen. The **Metal Performance Shaders** framework provides a large library of optimized compute and rendering shaders that take advantage of each GPU's unique hardware. In visionOS, create fully immersive stereoscopic content with the help of the **Compositor Services** framework.

Many high-level Apple frameworks leverage the performance of Metal, including **RealityKit**, **SceneKit**, **SpriteKit**, and **Core Image**. These high-level frameworks implement the GPU programming details for you. However, you can typically get better performance by writing your own custom Metal and shader code. See the Metal Shading Language Specification for shader implementation details.

## Topics

### Essentials
Begin with the Metal fundamentals.
- [Understanding the Metal 4 core API](https://developer.apple.com/documentation/metal/understanding_the_metal_4_core_api) - Discover the features and functionality in the Metal 4 foundational APIs.
- [Using a Render Pipeline to Render Primitives](https://developer.apple.com/documentation/metal/using_a_render_pipeline_to_render_primitives) - Render a colorful, 2D triangle by running a draw command on the GPU.
- [Performing Calculations on a GPU](https://developer.apple.com/documentation/metal/performing_calculations_on_a_gpu) - Use Metal to find GPUs and perform calculations on them.
- [Using Metal to Draw a View's Contents](https://developer.apple.com/documentation/metal/using_metal_to_draw_a_view_s_contents) - Create a MetalKit view and a render pass to draw the view's contents.

### Samples
Discover graphics techniques and Metal features through sample code projects.
- [Metal Sample Code Library](https://developer.apple.com/documentation/metal/metal_sample_code_library) - Explore the complete set of Metal samples.

### GPU Devices
Start with a Metal device instance to begin working with the GPU it represents.
- [GPU Devices and Work Submission](https://developer.apple.com/documentation/metal/gpu_devices_and_work_submission) - Find any available GPU, submit work to it with command buffers, suspend work, and coordinate between multiple GPUs.

### Command Encoders
Send work to a GPU by issuing commands and configuring the pipeline states for those commands.

### Render Passes
- [Render Passes](https://developer.apple.com/documentation/metal/render_passes) - Encode a render pass to draw graphics into an image.

### Compute Passes
- [Compute Passes](https://developer.apple.com/documentation/metal/compute_passes) - Encode a compute pass that runs computations in parallel on a thread grid, processing and manipulating Metal resource data on multiple cores of a GPU.

### Machine-Learning Passes
- [Machine-Learning Passes](https://developer.apple.com/documentation/metal/machine-learning_passes) - Add machine-learning model inference to your Metal app's GPU workflow.

### Blit Passes
- [Blit Passes](https://developer.apple.com/documentation/metal/blit_passes) - Encode a block information transfer pass to adjust and copy data to and from GPU resources, such as buffers and textures.

### Indirect Command Encoding
- [Indirect Command Encoding](https://developer.apple.com/documentation/metal/indirect_command_encoding) - Store draw commands in Metal buffers and run them at a later time on the GPU, either once or repeatedly.

### Ray Tracing with Acceleration Structures
- [Ray Tracing with Acceleration Structures](https://developer.apple.com/documentation/metal/ray_tracing_with_acceleration_structures) - Build a representation of your scene's geometry using triangles and bounding volumes to quickly trace rays through the scene.

### Resources
Store data in buffers and textures, and optionally manage the underlying GPU memory yourself.
- [Resource Fundamentals](https://developer.apple.com/documentation/metal/resource_fundamentals) - Control the common attributes of all Metal memory resources, including buffers and textures, and how to configure their underlying memory.
- [Buffers](https://developer.apple.com/documentation/metal/buffers) - Create and manage untyped data your app uses to exchange information with its shader functions.
- [Textures](https://developer.apple.com/documentation/metal/textures) - Create and manage typed data your app uses to exchange information with its shader functions.
- [Memory Heaps](https://developer.apple.com/documentation/metal/memory_heaps) - Take control of your app's GPU memory management by creating a large memory allocation for various buffers, textures, and other resources.
- [Resource Loading](https://developer.apple.com/documentation/metal/resource_loading) - Load assets in your games and apps quickly by running a dedicated input/output queue alongside your GPU tasks.
- [Resource Synchronization](https://developer.apple.com/documentation/metal/resource_synchronization) - Prevent multiple commands that can access the same resources simultaneously by coordinating those accesses with barriers, fences, or events.

### Shader Compilation and Libraries
Compile and organize shaders, the GPU functions that run on a Metal device's execution units.
- [Using the Metal 4 compilation API](https://developer.apple.com/documentation/metal/using_the_metal_4_compilation_api) - Control when and how you compile an app's shaders.
- [Shader Libraries](https://developer.apple.com/documentation/metal/shader_libraries) - Manage and load your app's Metal shaders.
- [Using Function Specialization to Build Pipeline Variants](https://developer.apple.com/documentation/metal/using_function_specialization_to_build_pipeline_variants) - Create pipelines for different levels of detail from a common shader source.

### Presentation
Display standard or high-dynamic-range content on a device's display with Core Animation or MetalKit, in standard or high dynamic range.
- [Managing your game window for Metal in macOS](https://developer.apple.com/documentation/metal/managing_your_game_window_for_metal_in_macos) - Set up a window and view for optimally displaying your Metal content.
- [Adapting your game interface for smaller screens](https://developer.apple.com/documentation/metal/adapting_your_game_interface_for_smaller_screens) - Make text legible on all devices the player chooses to run your game on.
- [Onscreen Presentation](https://developer.apple.com/documentation/metal/onscreen_presentation) - Show the output from a GPU's rendering pass to the user in your app.
- [HDR Content](https://developer.apple.com/documentation/metal/hdr_content) - Take advantage of high dynamic range to present more vibrant colors in your apps and games.

### Developer Tools
Identify and fix issues with your app's Metal API calls, shader code, resources, and performance during development by using Metal Debugger.
- [Supporting Simulator in a Metal app](https://developer.apple.com/documentation/metal/supporting_simulator_in_a_metal_app) - Configure alternative render paths in your Metal app to enable running your app in Simulator.
- [Capturing Metal Commands Programmatically](https://developer.apple.com/documentation/metal/capturing_metal_commands_programmatically) - Invoke a Metal frame capture from your app, then save the resulting GPU trace to a file or view it in Xcode.
- [Logging shader debug messages](https://developer.apple.com/documentation/metal/logging_shader_debug_messages) - Print debugging messages that a shader generates using shader logging.
- [Developing Metal apps that run in Simulator](https://developer.apple.com/documentation/metal/developing_metal_apps_that_run_in_simulator) - Prototype and test your Metal apps in Simulator.
- [Improving your game's graphics performance and settings](https://developer.apple.com/documentation/metal/improving_your_game_s_graphics_performance_and_settings) - Fix performance glitches and develop default settings for smooth experiences on Apple platforms using the powerful suite of Metal development tools.
- [Metal debugger](https://developer.apple.com/documentation/metal/metal_debugger) - Debug and profile your Metal workload with a GPU trace.
- [Metal developer workflows](https://developer.apple.com/documentation/metal/metal_developer_workflows) - Locate and fix issues related to your app's use of the Metal API and GPU functions.
- [GPU Counters and Counter Sample Buffers](https://developer.apple.com/documentation/metal/gpu_counters_and_counter_sample_buffers) - Retrieve runtime data from a GPU device by sampling one or more of its counters.
- [Metal Debugging Types](https://developer.apple.com/documentation/metal/metal_debugging_types) - Create capture managers and capture scopes, and review a GPU device's log after it runs a command buffer.

### Apple Silicon
Take advantage of the unique architecture of Apple silicon GPUs.
- [Porting your Metal code to Apple silicon](https://developer.apple.com/documentation/metal/porting_your_metal_code_to_apple_silicon) - Create a version of your Metal app that runs on both Apple silicon and Intel-based Mac computers.
- [Tailor Your Apps for Apple GPUs and Tile-Based Deferred Rendering](https://developer.apple.com/documentation/metal/tailor_your_apps_for_apple_gpus_and_tile-based_deferred_rendering) - Learn about characteristic Apple GPU features, including imageblocks, tile shaders, and raster order groups.

### Reference
- **Metal Structures**
- **Metal Enumerations**
- **Metal Constants**
- **Metal Data Types**
- **Metal Variables**

### Articles
- [Achieving smooth frame rates with a Metal display link](https://developer.apple.com/documentation/metal/achieving_smooth_frame_rates_with_a_metal_display_link) - Pace rendering with minimal input latency while providing essential information to the operating system for power-efficient rendering, thermal mitigation, and the scheduling of sustainable workloads.

### Structures
- **MTL4CommandQueueError** (Beta)

### Type Aliases
- **MTLGPUAddress** - A 64-bit unsigned integer type appropriate for storing GPU addresses.

### See Also
- **Metal Programming Guide**
- **Metal Best Practices Guide**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Metal)*