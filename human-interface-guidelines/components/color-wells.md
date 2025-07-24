# Color Wells

A color well lets people adjust the color of text, shapes, guides, and other onscreen elements.

**Platforms:** iOS | iPadOS | macOS | visionOS

## Overview

A color well displays a color picker when people tap or click it. This color picker can be the system-provided one or a custom interface that you design.

## Topics

### Best Practices

- **Consider the system-provided color picker for a familiar experience** - Using the built-in color picker provides a consistent experience, in addition to letting people save a set of colors they can access from any app. The system-defined color picker can also help provide a familiar experience when developing apps across iOS, iPadOS, and macOS.

### Platform Considerations

**macOS**  
- When people click a color well, it receives a highlight to provide visual confirmation that it's active. It then opens a color picker so people can choose a color. After they make a selection, the color well updates to show the new color.
- Color wells also support drag and drop, so people can drag colors from one color well to another, and from the color picker to a color well.

**iOS, iPadOS, visionOS**  
- No additional considerations.

**tvOS, watchOS**  
- Not supported.

### Related

- [Color](https://developer.apple.com/design/human-interface-guidelines/color)

### Developer Documentation

- [UIColorWell](https://developer.apple.com/documentation/uikit/uicolorwell) - UIKit
- [UIColorPickerViewController](https://developer.apple.com/documentation/uikit/uicolorpickerviewcontroller) - UIKit
- [NSColorWell](https://developer.apple.com/documentation/appkit/nscolorwell) - AppKit
- [Color Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DrawColor/DrawColor.html)

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/color-wells)*