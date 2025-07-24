# hvf

Render Hierarchical Variation Font (HVF) glyph outlines, and support font editors and related tools.

**Platforms:** iOS 18.4+ | iPadOS 18.4+ | macOS 15.4+ | tvOS 18.4+ | visionOS 2.4+ | watchOS 11.4+

## Overview

The hvf library provides C and Swift interfaces. The C interface supports rendering hvgl and hvpm tables in existing fonts.

The Swift interface adds support for the following:

- Writing a custom loader to render HVF glyphs from other sources, such as a database in a font editor.
- Generating data needed to build an hvgl table, using the same code as the custom loader.
- Interactively modifying part appearances and data, such as in a font editor.

## Topics

### Classes
- **HVGLPartLoader** - Special loader object for an HVGL table in memory, which must be Double-aligned Typically this is from a memory-mapped font
- **PartRenderer** - An object that can be used to set parameters for rendering a part, to render the part, and to diagnose the results of rendering

### Protocols
- **CompositeWriter** - Protocol for creating a Composite part for rendering or to build an HVGL table
- **PartGenerator** - Protocol for returning a writer object to create Shape or Composite data
- **ShapeWriter** - A protocol for creating a Shape part for rendering or to build an HVGL table

### Structures
- **CompositeExtremumIndex** - The index of an extremum rotation or translation in a Composite part
- **CompositeSubpart** - A subpart in a Composite part
- **CompositeSubpartTranslation** - A subpart translation in a Composite part

### Variables
- **hvfLibraryVersion** - Return the version of the HVF library

### Type Aliases
- **CustomPartLoader** - Closure which loads parts from an arbitrary source The first parameter is the part index which uniquely identifiers a part; these are assigned by the loader The second parameter is a PartGenerator the loader uses to get a ShapeWriter or CompositeWriter to create the requested part The result is the generated part, passed back in a PartResult

### Enumerations
- **AxisExtremum** - Which extremum within an axis
- **PartResult** - The result returned from a part loader
- **PointCoordinate** - Which coordinate within a point
- **SegmentBlendType** - The blend type for a segment of a path
- **SegmentPoint** - Which point within a segment

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/hvf)*