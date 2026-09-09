# hvf

Render Hierarchical Variable Font (HVF) glyph outlines, and support font editors and related tools.

**Platforms:** iOS 18.4+ | iPadOS 18.4+ | Mac Catalyst 18.4+ | macOS 15.4+ | tvOS 18.4+ | visionOS 2.4+ | watchOS 11.4+

## Overview

The hvf library provides C and Swift interfaces for font data. It is distinct from the [Hypervisor](Hypervisor.md) framework. The C interface supports rendering `hvgl` and `hvpm` tables in existing fonts.

The Swift interface adds support for the following:

- Writing a custom loader to render HVF glyphs from other sources, such as a database in a font editor.
- Generating data needed to build an hvgl table, using the same code as the custom loader.
- Interactively modifying part appearances and data, such as in a font editor.

## Topics

### Classes
- [HVGLPartLoader](https://developer.apple.com/documentation/hvf/hvglpartloader) - Loads an in-memory HVGL table, typically from a mapped font. The table must be aligned for `Double`.
- [PartRenderer](https://developer.apple.com/documentation/hvf/partrenderer) - Configures and renders a part and provides rendering diagnostics.

### Protocols
- **CompositeWriter** - Protocol for creating a Composite part for rendering or to build an HVGL table
- **PartGenerator** - Protocol for returning a writer object to create Shape or Composite data
- **ShapeWriter** - A protocol for creating a Shape part for rendering or to build an HVGL table

### Structures
- **CompositeExtremumIndex** - The index of an extremum rotation or translation in a Composite part
- **CompositeSubpart** - A subpart in a Composite part
- **CompositeSubpartTranslation** - A subpart translation in a Composite part

### Variables
- [hvfLibraryVersion](https://developer.apple.com/documentation/hvf/hvflibraryversion-swift.var) - A read-only `(major: Int, minor: Int, patch: Int)` version tuple, not a Swift function call.

### Type Aliases
- [CustomPartLoader](https://developer.apple.com/documentation/hvf/custompartloader) - A closure of type `(Int, any PartGenerator) -> PartResult`. It receives a loader-assigned part index and a generator that supplies a shape or composite writer, then returns the generated part's result.

### Enumerations
- **AxisExtremum** - Which extremum within an axis
- **PartResult** - The result returned from a part loader
- **PointCoordinate** - Which coordinate within a point
- **SegmentBlendType** - The blend type for a segment of a path
- **SegmentPoint** - Which point within a segment

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/hvf)*
