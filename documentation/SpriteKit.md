# SpriteKit

Add high-performance 2D content with smooth animations to your app, or create a game with a high-level set of 2D game-based tools.

**Platforms:** iOS 7.0+ | iPadOS 7.0+ | Mac Catalyst 13.0+ | macOS 10.9+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 10.0+

## Overview

SpriteKit is a general-purpose framework for drawing shapes, particles, text, images, and video in two dimensions. It leverages Metal to achieve high-performance rendering, while offering a simple programming interface to make it easy to create games and other graphics-intensive apps. Using a rich set of animations and physics behaviors, you can quickly add life to your visual elements and gracefully transition between screens.

SpriteKit is supported in iOS, macOS, tvOS, and watchOS, and it integrates well with frameworks such as GameplayKit and SceneKit. You can use SpriteKit in a compatible iPhone or iPad app running in visionOS, but don't use it in apps you create specifically for visionOS.

## Topics

### Essentials
- [Drawing SpriteKit Content in a View](https://developer.apple.com/documentation/spritekit/drawing_spritekit_content_in_a_view) - Display visual content using SpriteKit.
- **SKScene** - An object that organizes all of the active SpriteKit content.

### Nodes for Scene Building
- [Define the appearance or layout of scene content](https://developer.apple.com/documentation/spritekit/nodes_for_scene_building)

### Scene Renderers
- [Draw a SpriteKit scene using a rendering object](https://developer.apple.com/documentation/spritekit/scene_renderers)
- [Choosing a SpriteKit Scene Renderer](https://developer.apple.com/documentation/spritekit/choosing_a_spritekit_scene_renderer) - Compare the different ways to display a SpriteKit scene.
- **SKView** - A view subclass that renders a SpriteKit scene.
- **SKRenderer** - An object that renders a scene into a custom Metal rendering pipeline and drives the scene update cycle.
- **WKInterfaceSKScene** - A visual WatchKit element that displays a SpriteKit scene.

### Textures
- [Load graphics from various sources, or use an atlas to maximize rendering performance](https://developer.apple.com/documentation/spritekit/textures)
- [Maximizing Texture Performance](https://developer.apple.com/documentation/spritekit/maximizing_texture_performance) - Speed up image display and enable more images to be displayed at one time.
- **SKTexture** - An image, decoded on the GPU, that can be used to render various SpriteKit objects.
- **SKTextureAtlas** - A collection of textures optimized for storage and drawing performance.
- **SKMutableTexture** - A texture whose contents can be dynamically updated.

### Animation
- [Animate nodes by using a suite of provided actions, or create custom actions](https://developer.apple.com/documentation/spritekit/animation)
- [Getting Started with Actions](https://developer.apple.com/documentation/spritekit/getting_started_with_actions) - Create, configure, and run actions in SpriteKit.
- **SKAction** - An object that is run by a node to change its structure or content.

### Constraints
- [Constrain the position or orientation of nodes](https://developer.apple.com/documentation/spritekit/constraints)
- **SKConstraint** - A specification for constraining a node's position or rotation.
- **SKReachConstraints** - A specification of the degree of freedom when solving inverse kinematics.

### Mathematical Tools
- [Multipurpose mathematical objects you use to facilitate other graphical work](https://developer.apple.com/documentation/spritekit/mathematical_tools)
- **SKKeyframeSequence** - An object that performs interpolation between values specified at different times (keyframes).
- **SKRange** - A definition of a range of floating-point values.
- **SKRegion** - The definition of an arbitrary area.

### Physics Simulation
- [Add physics behaviors to nodes in your scene](https://developer.apple.com/documentation/spritekit/physics_simulation)
- [Getting Started with Physics](https://developer.apple.com/documentation/spritekit/getting_started_with_physics) - Simulate gravity, acceleration, collision detection, or joints.
- **SKPhysicsWorld** - The driver of the physics engine in a scene; it exposes the ability for you to configure and query the physics system.
- **SKPhysicsBody** - An object that adds physics simulation to a node.
- **SKPhysicsContact** - A description of the contact between two physics bodies.
- **SKPhysicsContactDelegate** - Methods your app can implement to respond when physics bodies come into contact.
- **SKFieldNode** - A node that applies physics effects to nearby nodes.

### Physics Joints
- [Connect physics bodies by using conceptual tools like pins, sliding joints, and spring joints](https://developer.apple.com/documentation/spritekit/physics_joints)
- [Working with Inverse Kinematics](https://developer.apple.com/documentation/spritekit/working_with_inverse_kinematics) - Gain fine-tuned control of objects that are connected by joints.
- **SKPhysicsJoint** - The abstract superclass for objects that connect physics bodies.
- **SKPhysicsJointFixed** - A joint that fuses two physics bodies together at a reference point.
- **SKPhysicsJointLimit** - A joint that imposes a maximum distance between two physics bodies, as if they were connected by a rope.
- **SKPhysicsJointPin** - A joint that pins together two physics bodies, allowing independent rotation.
- **SKPhysicsJointSliding** - A joint that allows two physics bodies to slide along an axis.
- **SKPhysicsJointSpring** - A joint that simulates a spring connecting two physics bodies.

### Tiling
- [Configure the images or autotiling behavior of a tile map node](https://developer.apple.com/documentation/spritekit/tiling)
- **SKTileMapNode** - A two-dimensional array of images.
- **SKTileDefinition** - A single tile that can be repeated in a tile map.
- **SKTileGroup** - A set of tiles that collectively define one type of terrain.
- **SKTileGroupRule** - Rules that describe how various tiles should be placed in a map.
- **SKTileSet** - A container for related tile groups.

### Shaders
- [Customize node drawing by augmenting the node's color or shape](https://developer.apple.com/documentation/spritekit/shaders)
- **SKShader** - An object that allows you to apply a custom fragment shader.
- **SKAttribute** - A specification for dynamic per-node data used with a custom shader.
- **SKAttributeValue** - A container for dynamic shader data associated with a node.
- **SKUniform** - A container for uniform shader data.

### Warping
- [Distort a node by supplying vertices and their transformations](https://developer.apple.com/documentation/spritekit/warping)
- **SKWarpGeometry** - A definition for a deformation of nodes that conform to SKWarpable.
- **SKWarpGeometryGrid** - A definition for a grid-based deformation of nodes that conform to SKWarpable.
- **SKWarpable** - A protocol for objects that can be warped and animated by an SKWarpGeometry.

### Reference
- [SpriteKit Enumerations](https://developer.apple.com/documentation/spritekit/spritekit_enumerations) - Enumerations used across SpriteKit.
- [SpriteKit Data Types](https://developer.apple.com/documentation/spritekit/spritekit_data_types) - Data types used across SpriteKit.
- [SpriteKit Constants](https://developer.apple.com/documentation/spritekit/spritekit_constants) - Constants used across SpriteKit.
- [SpriteKit Type Aliases](https://developer.apple.com/documentation/spritekit/spritekit_type_aliases) - Type aliases used across SpriteKit.
- [SpriteKit Variables](https://developer.apple.com/documentation/spritekit/spritekit_variables) - Global variables and macros used across SpriteKit.

### Structures
- **SpriteView** - A SwiftUI view that renders a SpriteKit scene.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SpriteKit)*