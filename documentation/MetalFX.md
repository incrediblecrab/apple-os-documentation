# MetalFX

Boost your Metal app's performance by upscaling lower-resolution content to save GPU time.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 16.0+ | macOS 13.0+ | visionOS 1.0+

## Overview

The MetalFX framework integrates with Metal to upscale a relatively low-resolution image to a higher output resolution in less time than it takes to render directly to the output resolution.

A timeline diagram that compares a traditional rendering timespan and compares it to a MetalFX upscaling timespan. The MetalFX upscaling method, which renders at a lower resolution and then upscales to the final resolution with MetalFX, takes about half the time traditional rendering, which renders directly to the higher, final resolution.

Use the GPU time savings to further enhance your app or game's experience. For example, add more effects or scene details.

MetalFX gives you two different ways to upscale your input renderings:

- Temporal antialiased upscaling
- Spatial upscaling

If you can provide pixel color, depth, and motion information, add an **MTLFXTemporalScaler** instance to your render pipeline. Otherwise, add an **MTLFXSpatialScaler** instance, which only requires a pixel color input texture.

Because the scaling effects take time to initialize, make an instance of either effect at launch or when a display changes resolutions. Once you've created an effect instance, you can use it repeatedly, typically once per frame.

## Topics

### Temporal scaling
- [Applying temporal antialiasing and upscaling using MetalFX](https://developer.apple.com/documentation/metalfx/applying_temporal_antialiasing_and_upscaling_using_metalfx) - Reduce render workloads while increasing image detail with MetalFX.
- **MTLFXTemporalScaler** - An upscaling effect that generates a higher resolution texture in a render pass by analyzing multiple input textures over time.
- **MTLFXTemporalScalerDescriptor** - A set of properties that configure a temporal scaling effect, and a factory method that creates the effect.

### Spatial scaling
- **MTLFXSpatialScaler** - An upscaling effect that generates a higher resolution texture in a render pass by spatially analyzing an input texture.
- **MTLFXSpatialScalerDescriptor** - A set of properties that configure a spatial scaling effect, and a factory method that creates the effect.
- **MTLFXSpatialScalerColorProcessingMode** - The color space modes for the input and output textures you use with a spatial scaling effect instance.

### Classes
- **MTLFXFrameInterpolatorDescriptor** (Beta) - A set of properties that configure a frame interpolator, and a factory method that creates the effect.
- **MTLFXTemporalDenoisedScalerDescriptor**

### Protocols
- **MTL4FXFrameInterpolator** (Beta)
- **MTL4FXSpatialScaler** (Beta) - An upscaling effect that generates a higher resolution texture in a render pass by spatially analyzing an input texture.
- **MTL4FXTemporalDenoisedScaler** (Beta)
- **MTL4FXTemporalScaler** (Beta)
- **MTLFXFrameInterpolatableScaler**
- **MTLFXFrameInterpolator** (Beta)
- **MTLFXFrameInterpolatorBase** (Beta)
- **MTLFXSpatialScalerBase** - An upscaling effect that generates a higher resolution texture in a render pass by spatially analyzing an input texture.
- **MTLFXTemporalDenoisedScaler**
- **MTLFXTemporalDenoisedScalerBase** (Beta)
- **MTLFXTemporalScalerBase** - An upscaling effect that generates a higher resolution texture in a render pass by analyzing multiple input textures over time.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MetalFX)*