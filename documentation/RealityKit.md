# RealityKit

Simulate and render 3D content for use in your augmented reality apps.

**Platforms:** iOS 13.0+ | iPadOS 13.0+ | Mac Catalyst 13.1+ | macOS 10.15+ | tvOS 26.0+ | visionOS 1.0+

## Overview

**RealityKit** provides high-performance 3D simulation and rendering capabilities you can use to create apps with 3D or augmented reality (AR) for iOS, iPadOS, macOS, tvOS, and visionOS. RealityKit is an AR-first 3D framework that leverages ARKit to seamlessly integrate virtual objects into the real world.

Use RealityKit's rich functionality to create compelling augmented reality (AR) experiences:

- Create and import full RealityKit scenes with models, animations, and Spatial Audio by using Reality Composer Pro for visionOS.
- Build or modify scenes at runtime by adding 3D models, shape primitives, and sounds from code.
- Have virtual objects interact with objects in the real world.
- Animate objects, both manually and with physics simulations.
- Respond to user input and changes in a person's surroundings.
- Synchronize across devices and use SharePlay to enable group AR experiences.

## OS 27 rendering and asset workflows

[USDKit](USDKit.md) adds Swift USD composition and stage rendering on its OS 27 platforms. [Spatial Preview](SpatialPreview.md) connects Mac authoring to Apple Vision Pro. These additions do not change RealityKit's earlier deployment requirements or imply that every USD feature is supported by every import path; consult [USD feature validation](https://developer.apple.com/documentation/usd/validating-usd-files).

### Gaussian splats: platform and beta status

The [GaussianSplatComponent reference](https://developer.apple.com/documentation/realitykit/gaussiansplatcomponent) lists iOS, iPadOS, Mac Catalyst, macOS, and visionOS 27.0 availability and requires **Apple7 GPU-family support**. The beta notes are not identical across those platforms:

| Target | Status in the sources checked September 8, 2026 |
| --- | --- |
| visionOS 27 | The API reference includes visionOS, and the Beta 8 notes list the offscreen/re-entry splat-rendering defect as resolved (183538823). Do not classify this platform as unavailable merely because another platform's notes say “upcoming.” |
| iOS, iPadOS, macOS 27 | Their Beta 8 RealityKit sections still say the API will arrive in an upcoming release (178061856), while their Gaussian Splats sections also list the offscreen/re-entry defect as resolved (183538823). Preserve this internal contradiction alongside the reference's 27.0 annotations; verify the actual target SDK and beta before enabling it. |
| Mac Catalyst 27 | Listed by the API reference; inspect the Catalyst SDK and runtime rather than inferring its beta status from a different platform. |

The component uses application-populated `GaussianSplatResource` buffers; it does not load PLY, USD, or other source files itself. Captured lighting is baked into the splat colors and does not respond to scene lights. Budget for splat count and overdraw, and handle resource-construction failures rather than assuming an unlimited point count. No tvOS or watchOS availability is listed for this component.

### Regression checks, not current restrictions

The Beta 8 notes mark missing MaterialX 1.39 nodes, loading failures for `ComputeGraphComponents` in Reality files, and incorrect opaque-material behavior under `OpacityComponent` as **resolved**. The earlier visionOS Simulator soft-shadow restriction is also listed as resolved.

On visionOS, rebuilding with the 27.0 SDK makes `RealityRenderer.isToneMappingEnabled` control tone mapping; apps built with earlier SDKs keep their prior behavior (177283932). For primitive restart with triangle or line strips, the notes require `LowLevelMesh.Descriptor.allowsPrimitiveRestart = true` (180878999). Include both cases in render regression tests.

For surrounding interface controls, follow the verified [HIG materials guidance](https://developer.apple.com/design/human-interface-guidelines/materials): Liquid Glass belongs to the functional control/navigation layer, not as a blanket material treatment for 3D content.

Sources for these beta-specific checks: [iOS and iPadOS 27](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes#RealityKit), [macOS 27](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes#RealityKit), and [visionOS 27](https://developer.apple.com/documentation/visionos-release-notes/visionos-27-release-notes#RealityKit).

## Topics

### Essentials

- [Understanding the modular architecture of RealityKit](https://developer.apple.com/documentation/visionos/understanding-the-realitykit-modular-architecture) - Learn how everything fits together in RealityKit.
- [Building an immersive experience with RealityKit](https://developer.apple.com/documentation/realitykit/building-an-immersive-experience-with-realitykit) - Use systems and postprocessing effects to create a realistic underwater scene.
- **Entity** - An element of a RealityKit scene to which you attach components that provide appearance and behavior characteristics for the entity.
- **Component** - A representation of a geometry or a behavior that you apply to an entity.

### Presentation

- [Views and attachments](https://developer.apple.com/documentation/realitykit/presentation-views-and-attachments) - Bring RealityKit content into your app with views and renderers.

### Presentation UI
Control your app's content and how people can interact with it.

### Scene management and logic

- [Scenes](https://developer.apple.com/documentation/realitykit/ecs-scenes) - The context that holds all RealityKit entities.
- [Systems](https://developer.apple.com/documentation/realitykit/ecs-systems) - Apply behaviors and physical effects to the entities in a RealityKit scene.
- [Events](https://developer.apple.com/documentation/realitykit/ecs-events) - Respond to things happening in your RealityKit scene by subscribing to specific event types.
- [Entity actions](https://developer.apple.com/documentation/realitykit/ecs-entity-actions) - Create simple, reusable actions that can change your app state, RealityKit scene, or animate an entity.

### Asset creation

- [Reality Composer Pro](https://developer.apple.com/documentation/realitycomposerpro) - Build, design, and orchestrate 3D content for RealityKit apps.
- [Swift Splash](https://developer.apple.com/documentation/visionos/swift-splash) - Use RealityKit to create an interactive ride in visionOS.
- [Diorama](https://developer.apple.com/documentation/visionos/diorama) - Design scenes for your visionOS app using Reality Composer Pro.
- [Composing interactive 3D content with RealityKit and Reality Composer Pro](https://developer.apple.com/documentation/realitykit/composing-interactive-3d-content-with-realitykit-and-reality-composer-pro) - Build an interactive scene using an animation timeline.
- [Presenting an artist's scene](https://developer.apple.com/documentation/realitykit/presenting-an-artists-scene) - Display a scene from Reality Composer Pro in visionOS.
- [Reality Composer — legacy authoring workflow](https://developer.apple.com/videos/play/wwdc2019/609/) - WWDC19's visual editor for AR scenes and Reality files. This historical workflow is distinct from current Reality Composer Pro.
- [Object capture](https://developer.apple.com/documentation/realitykit/realitykit-object-capture) - Create 3D objects from a series of photographs using photogrammetry.
- [USD](USD.md) - Scene-description, authoring, and renderer-compatibility guidance.

### Scene content

- [Hello World](https://developer.apple.com/documentation/visionos/world) - Use windows, volumes, and immersive spaces to teach people about the Earth.
- [Enabling video reflections in an immersive environment](https://developer.apple.com/documentation/visionos/enabling-video-reflections-in-an-immersive-environment) - Create a more immersive experience by adding video reflections in a custom environment.
- [Creating a spatial drawing app with RealityKit](https://developer.apple.com/documentation/realitykit/creating-a-spatial-drawing-app-with-realitykit) - Use low-level mesh and texture APIs to achieve fast updates to a person's brush strokes by integrating RealityKit with ARKit and SwiftUI.
- [Generating interactive geometry with RealityKit](https://developer.apple.com/documentation/realitykit/generating-interactive-geometry-with-realitykit) - Create an interactive mesh with low-level mesh and low-level texture.
- [Combining 2D and 3D views in an immersive app](https://developer.apple.com/documentation/realitykit/combining-2d-and-3d-views-in-an-immersive-app) - Use attachments to place 2D content relative to 3D content in your visionOS app.
- [Transforming RealityKit entities using gestures](https://developer.apple.com/documentation/realitykit/transforming-realitykit-entities-with-gestures) - Build a RealityKit component to support standard visionOS gestures on any entity.
- [Models and meshes](https://developer.apple.com/documentation/realitykit/scene-content-models-and-meshes) - Display virtual objects in your scene with mesh-based models.
- [Materials, textures, and shaders](https://developer.apple.com/documentation/realitykit/scene-content-materials-and-shaders) - Apply textures to the surface of your scene's 3D objects to give each object a unique appearance.
- [Anchors](https://developer.apple.com/documentation/realitykit/scene-content-anchors) - Lock virtual content to the real world.
- [Lights and cameras](https://developer.apple.com/documentation/realitykit/scene-content-lights-and-cameras) - Control the lighting and point of view for a scene.
- [Content synchronization](https://developer.apple.com/documentation/realitykit/scene-content-content-synchronization) - Synchronize the contents of entities locally or across the network.
- [Audio](https://developer.apple.com/documentation/realitykit/scene-content-audio) - Create personalized and realistic spatial audio experiences.
- [Videos](https://developer.apple.com/documentation/realitykit/scene-content-videos) - Present videos in your RealityKit experiences.
- [Images](https://developer.apple.com/documentation/realitykit/scene-content-images) - Present images and spatial scenes in your RealityKit experiences.

### Game development

- [Gaming sample code projects](https://developer.apple.com/documentation/realitykit/game-development-sample-code) - Explore a collection of projects relating to game development.
- [Entity animations](https://developer.apple.com/documentation/realitykit/game-development-entity-animations) - Dynamically move, rotate, and scale entities at runtime.
- [Character control, skeletons, and inverse kinematics](https://developer.apple.com/documentation/realitykit/game-development-character-skeletons) - Direct the movements and animation of models.

### Physics simulation

- [Collision detection](https://developer.apple.com/documentation/realitykit/physics-collision-detection) - Determine when entities collide with each other or the environment.
- [Simulations and motion](https://developer.apple.com/documentation/realitykit/physics-simulations-and-motion) - Simulate physical interactions between entities or systems.
- [Force effects](https://developer.apple.com/documentation/realitykit/physics-force-effects) - Control the movement of virtual objects with forces.
- [Physics joints and pins](https://developer.apple.com/documentation/realitykit/physics-joints-and-pins) - Simulate joint physics that connect virtual objects.

### Performance improvements

- [Improving the Performance of a RealityKit App](https://developer.apple.com/documentation/realitykit/improving-the-performance-of-a-realitykit-app) - Measure CPU and GPU utilization to find ways to improve your app's performance.
- [Reducing GPU Utilization in Your RealityKit App](https://developer.apple.com/documentation/realitykit/reducing-gpu-utilization-in-your-realitykit-app) - Prevent the GPU from limiting your app's frame rate by reducing the complexity of your render.
- [Reducing CPU Utilization in Your RealityKit App](https://developer.apple.com/documentation/realitykit/reducing-cpu-utilization-in-your-realitykit-app) - Target specific CPU metrics with adjustments to your app and its content.
- [Construct an immersive environment for visionOS](https://developer.apple.com/documentation/realitykit/construct-an-immersive-environment-for-visionos) - Build efficient custom worlds for your app.
- [Passing Metal command objects around your application](https://developer.apple.com/documentation/realitykit/passing-metal-command-objects-around-your-application) - Build a system that creates and passes Metal command objects to entities dispatching Metal compute shaders.
- **Resource** - A shared resource you use to configure a component, like a material, mesh, or texture.

### Articles

- [Responding to gestures on an entity](https://developer.apple.com/documentation/realitykit/responding-to-gestures-on-an-entity) - Respond to gestures performed on RealityKit entities using input target and collision components.
- [AnchoringComponent](https://developer.apple.com/documentation/realitykit/anchoringcomponent) - Choose a real-world target and tracking behavior for an entity. The entity remains inactive until the system finds a matching anchor; handle anchor-state changes rather than assuming immediate placement.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/RealityKit)*
