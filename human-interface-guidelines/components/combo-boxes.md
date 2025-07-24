# Combo Boxes

A combo box combines a text field with a pull-down button in a single control.

**Platforms:** macOS

## Overview

People can enter a custom value into the field or click the button to choose from a list of predefined values. When people enter a custom value, it's not added to the list of choices.

## Topics

### Best Practices

- **Populate the field with a meaningful default value from the list** - Although the field can be empty by default, it's best when the default value refers to the hidden choices. The default value doesn't have to be the first item in the list.
- **Use an introductory label to let people know what types of items to expect** - Generally, use title-style capitalization for labels and end them with a colon. For related guidance, see Labels.
- **Provide relevant choices** - People appreciate the ability to enter a custom value, as well as the convenience of choosing from a list of the most likely choices.
- **Make sure list items aren't wider than the text field** - If an item is too wide, the text field might truncate it, which is hard for people to read.

### Platform Considerations

**macOS**  
- Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.

### Related Components

- [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields) - For guidance on text input
- [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons) - For guidance on pull-down menus

### Developer Documentation

- [NSComboBox](https://developer.apple.com/documentation/appkit/nscombobox) - AppKit

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/combo-boxes)*