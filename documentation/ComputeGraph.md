# Compute Graph

Author GPU-driven particle simulations and compute effects for RealityKit.

**Runtime platforms:** iOS 27.0+ | iPadOS 27.0+ | macOS 27.0+ | tvOS 27.0+ | visionOS 27.0+

**Authoring:** Reality Composer Pro 3.0+

Reality Composer Pro beta 5 is a standalone app requiring an Apple silicon Mac with macOS Tahoe 26.5 or later. These authoring requirements are separate from the runtime OS versions above; see its [release notes](https://developer.apple.com/documentation/realitycomposerpro/reality-composer-pro-beta-5-release-notes).

**Mac Catalyst:** `ComputeGraphSimulation` and the framework's DocC metadata explicitly list 27.0+. The framework's Markdown overview omits Catalyst, so its platform list alone is incomplete. No watchOS availability is listed.

## Overview

Compute Graph describes simulation behavior as connected, typed nodes. It is a graphics and simulation technology—not a general replacement for [Core AI](CoreAI.md) model inference. Use [Reality Composer Pro](RealityComposerPro.md) to author effects, and [RealityKit](RealityKit.md) and [Metal](Metal.md) to integrate and measure their runtime behavior.

The framework overview describes three stages: define a graph, assemble its resource layout, and compile GPU pipelines. A pipeline can support multiple simulations. At runtime, bind the required buffers, textures, and uniforms before advancing the simulation.

## Topics

### Runtime simulation

- [`ComputeGraphSimulation`](https://developer.apple.com/documentation/computegraph/computegraphsimulation.md) — Represent a simulation backed by a pipeline.
- [`advance(_:)`](https://developer.apple.com/documentation/computegraph/computegraphsimulation/advance(_:).md) — Advance using frame timing and execution resources described by [`AdvanceParams`](https://developer.apple.com/documentation/computegraph/computegraphsimulation/advanceparams.md).
- [`spawn(elements:in:using:)`](https://developer.apple.com/documentation/computegraph/computegraphsimulation/spawn(elements:in:using:).md) — Insert elements with [`ElementSpawnParameters`](https://developer.apple.com/documentation/computegraph/elementspawnparameters.md).
- [`ElementGrouping`](https://developer.apple.com/documentation/computegraph/elementgrouping.md), [`CoordinateSpace`](https://developer.apple.com/documentation/computegraph/coordinatespace.md), and [`Sorting`](https://developer.apple.com/documentation/computegraph/sorting.md) — Control grouping, coordinate interpretation, and ordering.

### Node families

- [`emitter`](https://developer.apple.com/documentation/computegraph/emitter.md) and [`initialize`](https://developer.apple.com/documentation/computegraph/initialize.md) — Control emission and initial particle state.
- [`force`](https://developer.apple.com/documentation/computegraph/force.md) — Apply forces such as gravity, drag, or noise.
- [`module`](https://developer.apple.com/documentation/computegraph/module.md) and [`element`](https://developer.apple.com/documentation/computegraph/element.md) — Read and modify per-element state.
- [`output`](https://developer.apple.com/documentation/computegraph/output.md) — Set appearance without changing the simulated element itself.
- [`texture`](https://developer.apple.com/documentation/computegraph/texture.md) and [`PortReference`](https://developer.apple.com/documentation/computegraph/portreference.md) — Generate textures and connect graph values.

### Authoring and validation

Start with Apple's [working Compute Graph example](https://developer.apple.com/documentation/realitycomposerpro/building-a-working-compute-graph-example.md). Verify emission, initialization, simulation, and output independently, then test frame-time and memory costs in the actual app.

The beta landing page names low-level graph-definition and assembly types but does not fully enumerate their symbol references. Follow documented nodes and the selected SDK rather than inventing a graph-construction signature. Keep an existing effect path for older OS versions or failed asset preparation.

Reality Composer Pro beta 5 lists the failure to render loaded `ComputeGraphComponent` instances as fixed (177674901); its remaining editor and migration issues are tracked in [Reality Composer Pro](RealityComposerPro.md).

*Sources: [Compute Graph](https://developer.apple.com/documentation/computegraph.md), [ComputeGraphSimulation](https://developer.apple.com/documentation/computegraph/computegraphsimulation.md).*
