# Compositor Services

Take control of the drawing environment and render your own content using Metal.

**Platforms:** visionOS 1.0+ | macOS 26.0+ (remote compositor content)

## Overview

Compositor Services lets you draw directly to the device's displays using Metal and your own rendering engine. Use this framework to create a fully immersive scene in your app that doesn't require integration with the person's surroundings.

When you present an immersive space with CompositorLayer content from your app, you receive a LayerRenderer with the information you need to set up your Metal drawing environment. Use the layer to start your rendering loop and deliver successive frames of content. The layer provides the timing information you need to deliver frames at the refresh rate of the display. It also provides the Metal textures and other information that you need to draw content on the device displays.

For more information about how to draw your app's content using Metal, see Metal.

## Local, remote, and streamed rendering

Choose this framework when your engine owns Metal rendering and frame scheduling. Use the renderer's timing and drawable information rather than assuming a fixed display rate or texture layout. For passthrough integration, follow the mixed-immersion guide below instead of treating every compositor scene as full immersion.

[RemoteImmersiveSpace](https://developer.apple.com/documentation/swiftui/remoteimmersivespace) is a separate SwiftUI scene available on **macOS 26.0+** for presenting [CompositorLayer](https://developer.apple.com/documentation/compositorservices/compositorlayer) content on a selected visionOS device. Check `supportsRemoteScenes`, handle device selection and cancellation, and do not persist `remoteDeviceIdentifier` across launches. The remote system permits only one open immersive space at a time.

This is distinct from [Spatial Preview](SpatialPreview.md), the OS 27 document/USD authoring workflow, and [Foveated Streaming](FoveatedStreaming.md), the visionOS 26.4+ endpoint-streaming framework.

The [visionOS 27 Beta 8 notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-27-release-notes#Compositor-Services), checked September 8, 2026, mark the `RemoteImmersiveSpace` device-discovery failure as **resolved** (177989580). Re-test discovery and reconnection; do not describe remote immersive delivery as currently broken.

## Topics

### App integration
- [Drawing fully immersive content using Metal](https://developer.apple.com/documentation/compositorservices/drawing-fully-immersive-content-using-metal) - Create a fully immersive experience in visionOS using a custom Metal-based rendering engine.
- [Interacting with virtual content blended with passthrough](https://developer.apple.com/documentation/compositorservices/interacting-with-virtual-content-blended-with-passthrough) - Present a mixed immersion style space to draw content in a person's surroundings, and choose how upper limbs appear with respect to rendered content.
- [Rendering hover effects in Metal immersive apps](https://developer.apple.com/documentation/CompositorServices/rendering_hover_effects_in_metal_immersive_apps) - Change the appearance of a rendered onscreen element when a player gazes at it.
- **CompositorLayer** - A type that you use with an immersive space to display fully immersive content using Metal.
- **CompositorLayerConfiguration** - An interface for specifying the texture configurations and rendering behaviors to use with your Metal rendering engine.
- **DefaultCompositorLayerConfiguration** - A type that configures the layer with the default texture configurations and rendering behaviors for the current device.

### Render-loop setup
- **LayerRenderer** - A type that provides the Metal types and timing information you need to draw your content.
- **LayerRenderer.Frame** - A type that provides access to the timing information and data types you need to render a single frame of content.

### Drawing environment
- **Drawable** - A type that provides the textures and information you need to draw a frame of content.
- **View** - A type that provides information on how to render content into the frame's textures.

### Errors
- **LayerRendererConfigurationError** - Errors that can occur during layer configuration.

### Articles
- **CompositorServices Functions**

### Structures
- **TextureTopology** - A type that specifies the organization of one of the drawable's textures.

### Type Aliases
- **cp_drawable_array_t** - An opaque type that contains the drawable types and other information you need to set up your render pipeline.

### Hover Effects
- **cp_hover_effect_t** - An opaque type that describes a hover effect of the tracking area.
---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CompositorServices)*
