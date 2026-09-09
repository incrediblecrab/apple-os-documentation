# USD

Author and exchange layered 3D scenes for Apple's rendering and spatial-content workflows.

**Availability:** USD is a scene-description format and documentation collection, not an OS 27-only framework. Reader, renderer, schema, and API availability vary. [USDKit](USDKit.md) is the separate Swift framework introduced in OS 27.

## Overview

Universal Scene Description (OpenUSD, commonly USD) represents scene hierarchies, assets, and animation. Its composition model lets a scene reference other assets and layer overrides without destructively modifying the originals. Apple uses USD content in RealityKit, Reality Composer Pro, and AR Quick Look.

Choose USD for exchanging scene data; choose an appropriate runtime for rendering or editing it. A valid USD file does not guarantee that every Apple renderer imports every feature in that file.

## Topics

### Authoring and validation

- [Creating USD files for Apple devices](https://developer.apple.com/documentation/usd/creating-usd-files-for-apple-devices) — Prepare assets for the Apple application and renderer that will display them.
- [Validating feature support for USD files](https://developer.apple.com/documentation/usd/validating-usd-files) — Compare supported geometry, materials, animation, physics, and media features across renderers.
- [USDKit](USDKit.md) — Compose and edit USD through the system Swift API on supported OS 27 targets.
- [Model I/O](ModelIO.md) — Existing asset-processing APIs remain relevant to pipelines that support earlier operating systems.

### Augmented reality

- [OpenUSD schemas for AR](https://developer.apple.com/documentation/usd/usd-schemas-for-ar) — Describes Apple's proposed schemas for AR behavior.
- [Schema definitions for third-party DCCs](https://developer.apple.com/documentation/usd/schema-definitions-for-third-party-dccs) — Integrate those schemas with content-creation tools.
- [Placing a prim in the real world](https://developer.apple.com/documentation/usd/placing-a-prim-in-the-real-world) — Author anchoring information for a runtime that recognizes the physical target.
- [Spatial Preview](SpatialPreview.md) — Review Mac-authored documents and USD stages on Apple Vision Pro.

## Practical asset checks

1. **Identify the actual consumer.** RealityKit, Raytracer, Storm, and legacy SceneKit have different import capabilities. Apple's support tables describe USD import, not everything an engine can do through its own APIs.
2. **Validate the complete scene.** Check referenced assets, the selected variants, transform and skeletal animation, texture color spaces, and the intended shader network in the destination app.
3. **Separate data support from rendering support.** An unsupported geometry representation can disappear; an unsupported modifier may simply have no effect. Keep a visually representative test asset for each target renderer.
4. **Test the import route.** For example, Apple's validation guide explicitly excludes USD physics import through USDKit, even though RealityKit itself supports physics simulation.
5. **Keep editable originals.** Exported or compressed beta artifacts should not be the only copy of a production asset.

## OS 27 context

USDKit provides a system authoring API without requiring an embedded OpenUSD build, and Spatial Preview adds a Mac-to-headset review workflow. Neither introduction makes USD itself new to OS 27.

Apple's [asset-creation guide](https://developer.apple.com/documentation/usd/creating-usd-files-for-apple-devices) also documents a **macOS 27 viewer change**: Preview and Quick Look default to RealityKit for all USD file types. Preview uses the USDKit backend; Quick Look uses it for non-USDZ files. Storm is an alternative in both apps, while Raytracer is available in Preview. USDKit-backed rendering does not support the legacy backend's interactive behaviors, so test the actual app/backend rather than relying on an older preview result.

For source control and distribution, distinguish editable text USDA, compact binary USDC, and self-contained USDZ packages. Run OpenUSD's `usdchecker` for structural validation, then inspect the result in the target renderer; structural success alone does not validate appearance or behavior.

Do not infer automatic Gaussian-splat file loading from RealityKit's [GaussianSplatComponent](https://developer.apple.com/documentation/realitykit/gaussiansplatcomponent). Its documented data path uses application-populated buffers; the component does not parse source files itself. Apple's USD import table and the component API describe different paths.

[SceneKit](SceneKit.md) was deprecated in OS 26. Its presence in compatibility tables is useful for existing assets, not a recommendation for new rendering work.

## Sources

- [USD documentation](https://developer.apple.com/documentation/usd)
- [Creating USD files for Apple devices](https://developer.apple.com/documentation/usd/creating-usd-files-for-apple-devices)
- [Validating feature support for USD files](https://developer.apple.com/documentation/usd/validating-usd-files)
