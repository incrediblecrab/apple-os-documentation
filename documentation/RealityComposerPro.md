# Reality Composer Pro

Author, preview, and prepare 3D scenes for RealityKit applications.

**Tool:** Reality Composer Pro 3; **host:** Apple silicon Mac running macOS Tahoe 26.5 or later. Beta 5 is a standalone download, no longer part of Xcode. This tool's host minimum differs from Xcode 27's macOS 26.6 minimum.

## Overview

Reality Composer Pro works with entities and components in [RealityKit](RealityKit.md). Assemble scenes, edit materials, animate characters, and test behavior in the editor or through a linked Xcode project. The current documentation covers visionOS, iOS, and other RealityKit app workflows; individual runtime APIs still require their own availability checks.

The version 3 documentation describes Shader Graph, Script Graph, Compute Graph, Animation Graphs, a skeleton editor, a lightmap baker, and device preview. It also states that this release replaces the previous Reality Composer Pro version. Preserve a copy of existing projects and validate their assets and behavior before migrating an established workflow.

## Topics

### Project and preview workflow

- [Linking an Xcode project](https://developer.apple.com/documentation/realitycomposerpro/realitycomposerpro-essentials-linkingxcodeproject.md) — Connect authoring and app iteration.
- [Adding entities and assets](https://developer.apple.com/documentation/realitycomposerpro/realitycomposerpro-essentials-addingentitiestoscene.md) — Import scene content.
- [Prototypes and instances](https://developer.apple.com/documentation/realitycomposerpro/realitycomposerpro-essentials-understandingprototypes.md) — Reuse content while propagating edits.
- [Previewing content and running simulations](https://developer.apple.com/documentation/realitycomposerpro/realitycomposerpro-essentials-previewcontentrunsimulations.md) — Check scenes in the editor and on a supported destination.

### Graphs and character behavior

- [Shader Graph materials](https://developer.apple.com/documentation/realitycomposerpro/designing-materials-with-shader-graph.md) — Author surface appearance.
- [Script Graph](https://developer.apple.com/documentation/realitycomposerpro/getting-started-with-script-graphs.md) — Connect behavior through visual scripting.
- [Compute Graph](https://developer.apple.com/documentation/realitycomposerpro/introducing-compute-graph.md) — Author GPU-driven particle simulations; see the [Compute Graph API reference](ComputeGraph.md).
- [Animation Graph](https://developer.apple.com/documentation/realitycomposerpro/working-with-the-animation-graph.md) — Configure character animation states and transitions.
- [Navigation meshes](https://developer.apple.com/documentation/realitycomposerpro/building-a-navmesh-in-reality-composer-pro.md) and [behavior trees](https://developer.apple.com/documentation/realitycomposerpro/defining-a-behavior-with-behavior-trees.md) — Define navigable areas and entity decisions.

### Lighting, audio, and diagnostics

- [Lights and light layers](https://developer.apple.com/documentation/realitycomposerpro/lighting-a-scene-with-lights-and-light-layers.md) — Configure scene illumination.
- [Audio components](https://developer.apple.com/documentation/realitycomposerpro/introduction-to-reality-composer-pro-audio.md) — Attach audio behavior and review playback resource costs.
- [Reality Composer Pro Assistant](https://developer.apple.com/documentation/realitycomposerpro/working-with-the-reality-composer-pro-assistant.md) — Configure the authoring assistant; do not confuse it with an app-runtime model API.
- [Release notes](https://developer.apple.com/documentation/realitycomposerpro/reality-composer-pro-release-notes.md) and [beta 5 notes](https://developer.apple.com/documentation/realitycomposerpro/reality-composer-pro-beta-5-release-notes.md) — Check the selected beta's known issues before treating an editor or preview failure as an app defect.

Validate imported assets, graph execution, device rendering, and performance independently. Use [Xcode](Xcode.md) profiling for the running app; editor previews alone do not establish runtime support or frame-time budgets.

**Beta 5 limitations:** Project migration with Reality Composer Pro 2 timelines can fail (184861508); “On Initialize” can fail to start audio or animation on build/run, with “On Activate” documented as the workaround (182533099). Asset Generation requires macOS 27 even though the editor runs on Tahoe 26.5. The beta 5 notes also list shader, preview-texture, and mesh issues; review them before migrating production assets.

*Source: [Reality Composer Pro](https://developer.apple.com/documentation/realitycomposerpro.md).*
