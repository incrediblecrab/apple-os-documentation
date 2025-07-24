# SceneKit

Create 3D games and add 3D content to apps using high-level scene descriptions, and easily add animations, physics simulation, particle effects, and realistic physically based rendering.

**Platforms:** iOS 8.0+ | iPadOS 8.0+ | Mac Catalyst 13.1+ | macOS 10.8+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 3.0+

**Status:** Deprecated - Use RealityKit instead. For more information, see WWDC25 session 288: Bring your SceneKit projects to RealityKit.

## Overview

SceneKit combines a high-performance rendering engine with a descriptive API for import, manipulation, and rendering of 3D assets. Unlike lower-level APIs such as Metal and OpenGL that require you to implement in precise detail the rendering algorithms that display a scene, SceneKit requires only descriptions of your scene's contents and the actions or animations you want it to perform.

> **Note:** In visionOS, you can display SceneKit content only in 2D views and textures. For information about how to create immersive 3D content, see Creating fully immersive experiences in your app.

## Topics

### Essentials
- **SCNScene** - A container for the node hierarchy and global properties that together form a displayable 3D scene.
- **SCNView** - A view for displaying 3D SceneKit content.
- **SceneView** - A SwiftUI view for displaying 3D SceneKit content.

### Scene Structure
- [Organizing a Scene with Nodes](https://developer.apple.com/documentation/scenekit/organizing_a_scene_with_nodes) - Use nodes to define the structure of a scene.
- **SCNNode** - A structural element of a scene graph, representing a position and transform in a 3D coordinate space, to which you can attach geometry, lights, cameras, or other displayable content.
- **SCNReferenceNode** - A scene graph node that serves as a placeholder for content to be loaded from a separate scene file.

### Display and Interactivity
- **SCNSceneRenderer** - Methods and properties common to the SCNView, SCNLayer, and SCNRenderer classes.
- **SCNSceneRendererDelegate** - Methods your app can implement to participate in SceneKit's animation loop or perform additional rendering.
- **SCNLayer** - A Core Animation layer that renders a SceneKit scene as its content.
- **SCNRenderer** - A renderer for displaying a SceneKit scene in an existing Metal workflow or OpenGL context.
- **SCNHitTestResult** - Information about the result of a scene-space or view-space search for scene elements.

### Lighting, Cameras, and Shading
- **SCNLight** - A light source that can be attached to a node to illuminate the scene.
- **SCNCamera** - A set of camera attributes that can be attached to a node to provide a point of view for displaying the scene.
- **SCNMaterial** - A set of shading attributes that define the appearance of a geometry's surface when rendered.
- **SCNMaterialProperty** - A container for the color or texture of one of a material's visual properties.

### Geometry
- **SCNGeometry** - A three-dimensional shape (also called a model or mesh) that can be displayed in a scene, with attached materials that define its appearance.
- **SCNGeometrySource** - A container for vertex data forming part of the definition for a three-dimensional object, or geometry.
- **SCNGeometryElement** - A container for index data describing how vertices connect to define a three-dimensional object, or geometry.
- **Built-in Geometry Types** - Basic shapes—such as spheres, boxes, and planes—and features for generating 3D objects from 2D text and Bézier curves.

### Animation and Constraints
- **Animation** - Create declarative animations that move elements of a scene in predetermined ways, or manage animations imported with external authoring tools.
- **Constraints** - Automatically adjust the position or orientation of a node based on specified rules.
- **SCNSkinner** - An object that manages the relationship between skeletal animations and the nodes and geometries they animate.
- **SCNMorpher** - An object that manages smooth transitions between a node's base geometry and one or more target geometries.

### Physics
- **Physics Simulation** - Add dynamic behaviors to scene elements; detect contacts and collisions; simulate realistic effects like gravity, springs, and vehicles.

### Particle Systems
- **SCNParticleSystem** - An object that animates and renders a system of small image sprites using a high-level simulation whose general behavior you specify.
- **SCNParticlePropertyController** - An animation for a single property of the individual particles rendered by a particle system.

### Audio
- **SCNAudioSource** - A simple, reusable audio source—music or sound effects loaded from a file—for use in positional audio playback.
- **SCNAudioPlayer** - A controller for playback of a positional audio source in a SceneKit scene.

### Renderer Customization
- **SCNShadable** - Methods for customizing SceneKit's rendering of geometry and materials using Metal or OpenGL shader programs.
- **SCNProgram** - A complete Metal or OpenGL shader program that replaces SceneKit's rendering of a geometry or material.
- **SCNBufferStream** - An object that manages a Metal buffer used by a custom shader program.
- **SCNTechnique** - A specification for augmenting or postprocessing SceneKit's rendering of a scene using additional drawing passes with custom Metal or OpenGL shaders.
- **SCNTechniqueSupport** - The common interface for SceneKit objects that support multipass rendering using SCNTechnique objects.
- **SCNNodeRendererDelegate** - Methods you can implement to use your own custom Metal or OpenGL drawing code to render content for a node.
- [Postprocessing a Scene With Custom Symbols](https://developer.apple.com/documentation/scenekit/postprocessing_a_scene_with_custom_symbols) - Create visual effects in a scene by defining a rendering technique with custom symbols.

### Scene Asset Import
- **SCNSceneSource** - An object that manages the data-reading tasks associated with loading scene contents from a file or data.

### JavaScript
- **SCNExportJavaScriptModule** - Makes SceneKit classes and global constants available to the specified JavaScript context.

### SceneKit Data Types
- **SceneKit 3D Data Types** - SceneKit-specific vectors, matrices, and related functions and operations.

### Reference
- **SceneKit Enumerations**
- **SceneKit Constants** - Constants used throughout the SceneKit framework.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SceneKit)*