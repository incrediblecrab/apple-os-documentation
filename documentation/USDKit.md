# USDKit

Create, compose, inspect, and edit USD scenes using Apple's Swift API.

**Platforms:** iOS 27.0+ | iPadOS 27.0+ | Mac Catalyst 27.0+ | macOS 27.0+ | tvOS 27.0+ | visionOS 27.0+

**Status:** Introduced in the shipping OS 27 SDKs; beta documentation was reviewed September 8, 2026. No watchOS availability is listed.

## Overview

USDKit provides a curated, ABI-stable Swift interface to OpenUSD. It is useful for asset tools, procedural scene generation, and editors that need USD composition without building and embedding their own OpenUSD distribution. The USD format itself predates OS 27; use existing compatible asset-loading frameworks when supporting older systems.

The central distinction is between a **layer**, which stores authored scene description, and a **stage**, which resolves the contributions of multiple layers into a scene. A **prim** is a node in that composed hierarchy. Keep this distinction explicit when editing: an override in one layer need not rewrite the original asset.

## Topics

### Scene description

- [USDLayer](https://developer.apple.com/documentation/usdkit/usdlayer) — A file-backed or in-memory unit of authored data.
- [USDStage](https://developer.apple.com/documentation/usdkit/usdstage) — A composed scene assembled from layers.
- [USDPrim](https://developer.apple.com/documentation/usdkit/usdprim) — A scene node with properties, relationships, and children.
- [USDValue](https://developer.apple.com/documentation/usdkit/usdvalue) and [USDToken](https://developer.apple.com/documentation/usdkit/usdtoken) — Represent attribute values and interned identifiers.
- [USDTransformOperation](https://developer.apple.com/documentation/usdkit/usdtransformoperation) — Describes an authored transform operation.

### Rendering and playback

- [USDStageComponent](https://developer.apple.com/documentation/usdkit/usdstagecomponent) — Renders a stage as children of a RealityKit entity.
- [USDPlayer](https://developer.apple.com/documentation/usdkit/usdplayer) — Advances stage playback and produces render data.
- [USDRenderError](https://developer.apple.com/documentation/usdkit/usdrendererror) — Reports failures in stage rendering.
- [Spatial Preview](SpatialPreview.md) — Sends a Mac authoring workflow to Apple Vision Pro.

## Implementation essentials

Decide which layer owns each edit and preserve the source assets separately from generated overrides. Verify exported data by reopening the composed stage, not just by checking that a file was written.

`USDStageComponent` has automatic and manual rendering modes. Automatic mode responds to stage and time-code changes; manual mode requires an explicit render operation. Choose hit-testing support at initialization — the component does not allow changing that choice afterward.

For a Spatial Preview bridge, perform USDKit edits on the main actor and batch work from an external runtime as described in [Apple's bridging guide](https://developer.apple.com/documentation/spatialpreview/bridging-an-external-usd-runtime-to-spatial-preview). Prevent a synchronization feedback loop when applying edits that originated on the headset.

## Applicability and release-note checks

- **Composition is not universal rendering support.** Consult [Validating feature support for USD files](https://developer.apple.com/documentation/usd/validating-usd-files) for the selected renderer and import path. In particular, that guide says USDKit does not load USD physics data into RealityKit.
- **Check failures at both stages.** Successful authoring does not prove that materials, referenced resources, or animation render as intended. Handle render errors and test representative content on each target platform.
- **Resolved in the OS 27 release notes:** failures to read or modify some attributes, and inability to author array, vector, matrix, and quaternion values. Do not retain those as current API restrictions.
- **Early-beta asset compatibility:** the macOS and visionOS notes document incompatible compressed meshes between Beta 1 and Beta 2 exports, including `usdcrush`. Preserve original assets and regenerate old beta-derived artifacts with a consistent toolchain rather than treating them as durable interchange files.

## Sources

- [USDKit reference](https://developer.apple.com/documentation/usdkit)
- [USD format and authoring guidance](https://developer.apple.com/documentation/usd)
- [iOS and iPadOS 27 release notes — USDKit](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes#USDKit)
- [macOS 27 release notes — USDKit](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes#USDKit)
- [visionOS 27 release notes — USDKit](https://developer.apple.com/documentation/visionos-release-notes/visionos-27-release-notes#USDKit)
