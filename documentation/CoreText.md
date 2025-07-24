# Core Text

Create text layouts, optimize font handling, and access font metrics and glyph data.

**Platforms:** iOS 3.2+ | iPadOS 3.2+ | Mac Catalyst 13.1+ | macOS 10.8+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 2.0+

## Overview

Core Text provides a low-level programming interface for laying out text and handling fonts. The Core Text layout engine is designed for high performance, ease of use, and close integration with Core Foundation. The text layout API provides high-quality typesetting, including character-to-glyph conversion, with ligatures, kerning, and so on. The complementary Core Text font technology provides automatic font substitution (cascading), font descriptors and collections, easy access to font metrics and glyph data, and many other features.

**Note:** All individual functions in Core Text are thread-safe. Font objects (CTFont, CTFontDescriptor, and associated objects) can be used simultaneously by multiple operations, work queues, or threads. However, the layout objects (CTTypesetter, CTFramesetter, CTRun, CTLine, CTFrame, and associated objects) should be used in a single operation, work queue, or thread.

## Topics

### Opaque Types
- **CTFont** - A font object.
- **CTFontCollection** - A font collection.
- **CTFontDescriptor** - A font descriptor.
- **CTFrame** - A frame.
- **CTFramesetter** - Generate text frames.
- **CTGlyphInfo** - Override a font's specified mapping from Unicode to the glyph ID.
- **CTLine** - A line of text.
- **CTParagraphStyle** - Paragraph or ruler attributes in an attributed string.
- **CTRun** - A glyph run.
- **CTRunDelegate** - A run delegate.
- **CTTextTab** - A tab in a paragraph style, storing an alignment type and location.
- **CTTypesetter** - A typesetter which performs line layout.

### Reference
- **Styling Attributed Strings** - Attributes to which Core Text responds when placed in a CFAttributedString object.
- **Core Text Structures**
- **Core Text Enumerations**
- **Core Text Constants**
- **Core Text Functions**
- **Core Text Data Types**
- **SFNT Support**

### Macros
- **Macros**

### Classes
- **CTRubyAnnotation**

### Protocols
- **CTAdaptiveImageProviding**

### See Also
#### Related Documentation
- [Core Text Programming Guide](https://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/CoreText_Programming/Introduction/Introduction.html)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreText)*