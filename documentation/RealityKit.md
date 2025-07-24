# RealityKit

Simulate and render 3D content for use in your augmented reality apps.

**Platforms:** iOS 13.0+ | iPadOS 13.0+ | Mac Catalyst 13.1+ | macOS 10.15+ | tvOS 26.0+ (Beta) | visionOS 1.0+

## Overview

**RealityKit** provides high-performance 3D simulation and rendering capabilities you can use to create apps with 3D or augmented reality (AR) for iOS, iPadOS, macOS, tvOS, and visionOS. RealityKit is an AR-first 3D framework that leverages ARKit to seamlessly integrate virtual objects into the real world.

Use RealityKit's rich functionality to create compelling augmented reality (AR) experiences:

- Create and import full RealityKit scenes with models, animations, and Spatial Audio by using Reality Composer Pro for visionOS.
- Build or modify scenes at runtime by adding 3D models, shape primitives, and sounds from code.
- Have virtual objects interact with objects in the real world.
- Animate objects, both manually and with physics simulations.
- Respond to user input and changes in a person's surroundings.
- Synchronize across devices and use SharePlay to enable group AR experiences.

## Topics

### Essentials
- [Understanding the modular architecture of RealityKit](https://developer.apple.com/documentation/realitykit/understanding_the_modular_architecture_of_realitykit) - Learn how everything fits together in RealityKit.
- [Building an immersive experience with RealityKit](https://developer.apple.com/documentation/realitykit/building_an_immersive_experience_with_realitykit) - Use systems and postprocessing effects to create a realistic underwater scene.
- **Entity** - An element of a RealityKit scene to which you attach components that provide appearance and behavior characteristics for the entity.
- **Component** - A representation of a geometry or a behavior that you apply to an entity.

### Presentation
- [Views and attachments](https://developer.apple.com/documentation/realitykit/views_and_attachments) - Bring RealityKit content into your app with views and renderers.

### Presentation UI
Control your app's content and how people can interact with it.

### Scene management and logic
- [Scenes](https://developer.apple.com/documentation/realitykit/scenes) - The context that holds all RealityKit entities.
- [Systems](https://developer.apple.com/documentation/realitykit/systems) - Apply behaviors and physical effects to the entities in a RealityKit scene.
- [Events](https://developer.apple.com/documentation/realitykit/events) - Respond to things happening in your RealityKit scene by subscribing to specific event types.
- [Entity actions](https://developer.apple.com/documentation/realitykit/entity_actions) - Create simple, reusable actions that can change your app state, RealityKit scene, or animate an entity.

### Asset creation
- [Designing RealityKit content with Reality Composer Pro](https://developer.apple.com/documentation/realitykit/designing_realitykit_content_with_reality_composer_pro) - Design RealityKit scenes for your visionOS app.
- [Swift Splash](https://developer.apple.com/documentation/realitykit/swift_splash) - Use RealityKit to create an interactive ride in visionOS. (Beta)
- [Diorama](https://developer.apple.com/documentation/realitykit/diorama) - Design scenes for your visionOS app using Reality Composer Pro.
- [Composing interactive 3D content with RealityKit and Reality Composer Pro](https://developer.apple.com/documentation/realitykit/composing_interactive_3d_content_with_realitykit_and_reality_composer_pro) - Build an interactive scene using an animation timeline.
- [Presenting an artist's scene](https://developer.apple.com/documentation/realitykit/presenting_an_artist_s_scene) - Display a scene from Reality Composer Pro in visionOS.
- [Reality Composer](https://developer.apple.com/documentation/realitykit/reality_composer) - A visual editor for RealityKit AR scenes.
- [Object capture](https://developer.apple.com/documentation/realitykit/object_capture) - Create 3D objects from a series of photographs using photogrammetry.
- [USD](https://developer.apple.com/documentation/realitykit/usd) - An efficient and scalable way to represent 3D scenes.

### Scene content
- [Hello World](https://developer.apple.com/documentation/realitykit/hello_world) - Use windows, volumes, and immersive spaces to teach people about the Earth.
- [Enabling video reflections in an immersive environment](https://developer.apple.com/documentation/realitykit/enabling_video_reflections_in_an_immersive_environment) - Create a more immersive experience by adding video reflections in a custom environment.
- [Creating a spatial drawing app with RealityKit](https://developer.apple.com/documentation/realitykit/creating_a_spatial_drawing_app_with_realitykit) - Use low-level mesh and texture APIs to achieve fast updates to a person's brush strokes by integrating RealityKit with ARKit and SwiftUI.
- [Generating interactive geometry with RealityKit](https://developer.apple.com/documentation/realitykit/generating_interactive_geometry_with_realitykit) - Create an interactive mesh with low-level mesh and low-level texture.
- [Combining 2D and 3D views in an immersive app](https://developer.apple.com/documentation/realitykit/combining_2d_and_3d_views_in_an_immersive_app) - Use attachments to place 2D content relative to 3D content in your visionOS app.
- [Transforming RealityKit entities using gestures](https://developer.apple.com/documentation/realitykit/transforming_realitykit_entities_using_gestures) - Build a RealityKit component to support standard visionOS gestures on any entity.
- [Models and meshes](https://developer.apple.com/documentation/realitykit/models_and_meshes) - Display virtual objects in your scene with mesh-based models.
- [Materials, textures, and shaders](https://developer.apple.com/documentation/realitykit/materials_textures_and_shaders) - Apply textures to the surface of your scene's 3D objects to give each object a unique appearance.
- [Anchors](https://developer.apple.com/documentation/realitykit/anchors) - Lock virtual content to the real world.
- [Lights and cameras](https://developer.apple.com/documentation/realitykit/lights_and_cameras) - Control the lighting and point of view for a scene.
- [Content synchronization](https://developer.apple.com/documentation/realitykit/content_synchronization) - Synchronize the contents of entities locally or across the network.
- [Audio](https://developer.apple.com/documentation/realitykit/audio) - Create personalized and realistic spatial audio experiences.
- [Videos](https://developer.apple.com/documentation/realitykit/videos) - Present videos in your RealityKit experiences.
- [Images](https://developer.apple.com/documentation/realitykit/images) - Present images and spatial scenes in your RealityKit experiences.

### Game development
- [Gaming sample code projects](https://developer.apple.com/documentation/realitykit/gaming_sample_code_projects) - Explore a collection of projects relating to game development.
- [Entity animations](https://developer.apple.com/documentation/realitykit/entity_animations) - Dynamically move, rotate, and scale entities at runtime.
- [Character control, skeletons, and inverse kinematics](https://developer.apple.com/documentation/realitykit/character_control_skeletons_and_inverse_kinematics) - Direct the movements and animation of models.

### Physics simulation
- [Collision detection](https://developer.apple.com/documentation/realitykit/collision_detection) - Determine when entities collide with each other or the environment.
- [Simulations and motion](https://developer.apple.com/documentation/realitykit/simulations_and_motion) - Simulate physical interactions between entities or systems.
- [Force effects](https://developer.apple.com/documentation/realitykit/force_effects) - Control the movement of virtual objects with forces.
- [Physics joints and pins](https://developer.apple.com/documentation/realitykit/physics_joints_and_pins) - Simulate joint physics that connect virtual objects.

### Performance improvements
- [Improving the Performance of a RealityKit App](https://developer.apple.com/documentation/realitykit/improving_the_performance_of_a_realitykit_app) - Measure CPU and GPU utilization to find ways to improve your app's performance.
- [Reducing GPU Utilization in Your RealityKit App](https://developer.apple.com/documentation/realitykit/reducing_gpu_utilization_in_your_realitykit_app) - Prevent the GPU from limiting your app's frame rate by reducing the complexity of your render.
- [Reducing CPU Utilization in Your RealityKit App](https://developer.apple.com/documentation/realitykit/reducing_cpu_utilization_in_your_realitykit_app) - Target specific CPU metrics with adjustments to your app and its content.
- [Construct an immersive environment for visionOS](https://developer.apple.com/documentation/realitykit/construct_an_immersive_environment_for_visionos) - Build efficient custom worlds for your app.
- [Passing Metal command objects around your application](https://developer.apple.com/documentation/realitykit/passing_metal_command_objects_around_your_application) - Build a system that creates and passes Metal command objects to entities dispatching Metal compute shaders.
- **Resource** - A shared resource you use to configure a component, like a material, mesh, or texture.

### Articles
- [Responding to gestures on an entity](https://developer.apple.com/documentation/realitykit/responding_to_gestures_on_an_entity) - Respond to gestures performed on RealityKit entities using input target and collision components.
- [Taking Control of Scene Anchoring](https://developer.apple.com/documentation/realitykit/taking_control_of_scene_anchoring) - Create a more interactive user experience by choosing exactly where to anchor Reality Composer scenes.

---

**Beta Software**

This documentation contains preliminary information about an API or technology in development. This information is subject to change, and software implemented according to this documentation should be tested with final operating system software.

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/RealityKit)*