# Labels

A label is a static piece of text that people can read and often copy, but not edit.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

Labels display text throughout the interface, in buttons, menu items, and views, helping people understand the current context and what they can do next.

The term label refers to uneditable text that can appear in various places. For example:

- Within a button, a label generally conveys what the button does, such as Edit, Cancel, or Send.
- Within many lists, a label can describe each item, often accompanied by a symbol or an image.
- Within a view, a label might provide additional context by introducing a control or describing a common action or task that people can perform in the view.

**Developer note:** To display uneditable text, SwiftUI defines two components: Label and Text.

## Topics

### Best Practices

- **Use a label to display a small amount of text that people don't need to edit** - If you need to let people edit a small amount of text, use a text field. If you need to display a large amount of text, and optionally let people edit it, use a text view.
- **Prefer system fonts** - A label can display plain or styled text, and it supports Dynamic Type (where available) by default. If you adjust the style of a label or use custom fonts, make sure the text remains legible.
- **Use system-provided label colors to communicate relative importance** - The system defines four label colors that vary in appearance to help you give text different levels of visual importance. For additional guidance, see Color.
- **Make useful label text selectable** - If a label contains useful information — like an error message, a location, or an IP address — consider letting people select and copy it for pasting elsewhere.

### System Label Colors

| System color | Example usage | iOS, iPadOS, tvOS, visionOS | macOS |
|---|---|---|---|
| Label | Primary information | label | labelColor |
| Secondary label | A subheading or supplemental text | secondaryLabel | secondaryLabelColor |
| Tertiary label | Text that describes an unavailable item or behavior | tertiaryLabel | tertiaryLabelColor |
| Quaternary label | Watermark text | quaternaryLabel | quaternaryLabelColor |

### Platform Considerations

**iOS, iPadOS, tvOS, and visionOS**  
No additional considerations for iOS, iPadOS, tvOS, or visionOS.

**macOS**  
**Developer note:** To display uneditable text in a label, use the isEditable property of NSTextField.

**watchOS**  
- Date and time text components display the current date, the current time, or a combination of both. You can configure a date text component to use a variety of formats, calendars, and time zones.
- A countdown timer text component displays a precise countdown or count-up timer. You can configure a timer text component to display its count value in a variety of formats.
- When you use the system-provided date and timer text components, watchOS automatically adjusts the label's presentation to fit the available space. The system also updates the content without further input from your app.
- Consider using date and timer components in complications. For design guidance, see Complications; for developer guidance, see Text.

### Related Components

- [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields)
- [Text views](https://developer.apple.com/design/human-interface-guidelines/text-views)

### Developer Documentation

- [Label](https://developer.apple.com/documentation/swiftui/label) - SwiftUI
- [Text](https://developer.apple.com/documentation/swiftui/text) - SwiftUI
- [UILabel](https://developer.apple.com/documentation/uikit/uilabel) - UIKit
- [NSTextField](https://developer.apple.com/documentation/appkit/nstextfield) - AppKit

## Changelog

### June 5, 2023
- Updated guidance to reflect changes in watchOS 10.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/labels)*