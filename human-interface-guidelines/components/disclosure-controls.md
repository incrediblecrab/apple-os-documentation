# Disclosure Controls

Disclosure controls reveal and hide information and functionality related to specific controls or views.

**Platforms:** iOS | iPadOS | macOS | visionOS

## Overview

Disclosure controls help manage complexity by showing and hiding content as needed. They come in two main forms: disclosure triangles and disclosure buttons.

## Topics

### Best Practices

- **Use a disclosure control to hide details until they're relevant** - Place controls that people are most likely to use at the top of the disclosure hierarchy so they're always visible, with more advanced functionality hidden by default. This organization helps people quickly find the most essential information without overwhelming them with too many detailed options.

### Disclosure Triangles

A disclosure triangle shows and hides information and functionality associated with a view or a list of items. For example, Keynote uses a disclosure triangle to show advanced options when exporting a presentation, and the Finder uses disclosure triangles to progressively reveal hierarchy when navigating a folder structure in list view.

A disclosure triangle points inward from the leading edge when its content is hidden and down when its content is visible. Clicking or tapping the disclosure triangle switches between these two states, and the view expands or collapses accordingly to accommodate the content.

- **Provide a descriptive label when using a disclosure triangle** - Make sure your labels indicate what is disclosed or hidden, like "Advanced Options."

### Disclosure Buttons

A disclosure button shows and hides functionality associated with a specific control. For example, the macOS Save sheet shows a disclosure button next to the Save As text field. When people click or tap this button, the Save dialog expands to give advanced navigation options for selecting an output location for their document.

A disclosure button points down when its content is hidden and up when its content is visible. Clicking or tapping the disclosure button switches between these two states, and the view expands or collapses accordingly to accommodate the content.

- **Place a disclosure button near the content that it shows and hides** - Establish a clear relationship between the control and the expanded choices that appear when a person clicks or taps a button.

- **Use no more than one disclosure button in a single view** - Multiple disclosure buttons add complexity and can be confusing.

### Platform Considerations

**iOS, iPadOS, visionOS**  
Disclosure controls are available in iOS, iPadOS, and visionOS with the SwiftUI DisclosureGroup view.

**macOS**  
No additional considerations for macOS.

Not supported in tvOS or watchOS.

### Related Components

- [Outline views](https://developer.apple.com/design/human-interface-guidelines/outline-views) - Display hierarchical data
- [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables) - Present collections of information
- [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons) - Initiate app-specific actions

### Developer Documentation

- [DisclosureGroup](https://developer.apple.com/documentation/swiftui/disclosuregroup) - SwiftUI
- [NSButton.BezelStyle.disclosure](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle/disclosure) - AppKit
- [NSButton.BezelStyle.pushDisclosure](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle/pushdisclosure) - AppKit

### Videos

- [Stacks, Grids, and Outlines in SwiftUI](https://developer.apple.com/videos/play/wwdc2020/10031/)

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/disclosure-controls)*