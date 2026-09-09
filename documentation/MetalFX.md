# MetalFX

Boost your Metal app's performance by upscaling lower-resolution content to save GPU time.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 16.0+ | macOS 13.0+ | visionOS 1.0+

## Overview

The MetalFX framework integrates with Metal to upscale a relatively low-resolution image to a higher output resolution, potentially reducing the cost of rendering directly at the output resolution.

Apple's overview illustrates a lower-resolution render followed by upscaling. Actual savings depend on the GPU, input/output sizes, and effect; measure your workload instead of assuming a fixed speedup.

Use the GPU time savings to further enhance your app or game's experience. For example, add more effects or scene details.

The basic MetalFX upscaling paths are:

- Temporal antialiased upscaling
- Spatial upscaling

If you can provide pixel color, depth, and motion information, add an **MTLFXTemporalScaler** instance to your render pipeline. Otherwise, add an **MTLFXSpatialScaler** instance, which only requires a pixel color input texture.

Because the scaling effects take time to initialize, make an instance of either effect at launch or when a display changes resolutions. Once you've created an effect instance, you can use it repeatedly, typically once per frame.

## Effect availability and integration

The current reference also includes frame interpolation, temporal denoising/scaling, and Metal 4 variants. These effects do not all share the framework's minimum versions or platforms. For example, [MTLFXFrameInterpolatorDescriptor](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatordescriptor) lists iOS, iPadOS, Mac Catalyst, macOS, and tvOS 26.0 availability; it does not list visionOS. It is not an OS 27 introduction.

Before creating an effect, check its own availability and GPU support. The temporal scaler's [supportsDevice(_:)](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerdescriptor/supportsdevice(_:)) tests the selected Metal device, not merely the operating-system version. Handle effect-creation failure and keep native rendering or another supported scaling path available.

Match the configured texture formats to the textures supplied each frame. Test camera cuts, resolution changes, depth and motion inputs, and temporal history behavior; a higher displayed frame rate does not by itself prove correct motion or lower input latency. Consult the individual effect's contract rather than mixing `MTL` and `MTL4` command objects interchangeably.

## Topics

### Temporal scaling

- [Applying temporal antialiasing and upscaling using MetalFX](https://developer.apple.com/documentation/metalfx/applying-temporal-antialiasing-and-upscaling-using-metalfx) - Reduce render workloads while increasing image detail with MetalFX.
- **MTLFXTemporalScaler** - An upscaling effect that generates a higher resolution texture in a render pass by analyzing multiple input textures over time.
- **MTLFXTemporalScalerDescriptor** - A set of properties that configure a temporal scaling effect, and a factory method that creates the effect.

### Spatial scaling

- **MTLFXSpatialScaler** - An upscaling effect that generates a higher resolution texture in a render pass by spatially analyzing an input texture.
- **MTLFXSpatialScalerDescriptor** - A set of properties that configure a spatial scaling effect, and a factory method that creates the effect.
- **MTLFXSpatialScalerColorProcessingMode** - The color space modes for the input and output textures you use with a spatial scaling effect instance.

### Classes

- **MTLFXFrameInterpolatorDescriptor** - A set of properties that configure a frame interpolator, and a factory method that creates the effect.
- **MTLFXTemporalDenoisedScalerDescriptor**

### Protocols

- **MTL4FXFrameInterpolator**
- **MTL4FXSpatialScaler** - An upscaling effect that generates a higher resolution texture in a render pass by spatially analyzing an input texture.
- **MTL4FXTemporalDenoisedScaler**
- **MTL4FXTemporalScaler**
- **MTLFXFrameInterpolatableScaler**
- **MTLFXFrameInterpolator**
- **MTLFXFrameInterpolatorBase**
- **MTLFXSpatialScalerBase** - An upscaling effect that generates a higher resolution texture in a render pass by spatially analyzing an input texture.
- **MTLFXTemporalDenoisedScaler**
- **MTLFXTemporalDenoisedScalerBase**
- **MTLFXTemporalScalerBase** - An upscaling effect that generates a higher resolution texture in a render pass by analyzing multiple input textures over time.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MetalFX)*
