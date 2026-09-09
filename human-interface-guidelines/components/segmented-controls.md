# Segmented Controls

A segmented control is a linear set of two or more segments, each of which functions as a button.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS

## Overview

Within a segmented control, all segments are usually equal in width. Like buttons, segments can contain text or images. Segments can also have text labels beneath them (or beneath the control as a whole).

## Topics

### Best Practices

A segmented control normally represents a single choice. On macOS, it can also support multiple selections: Keynote's text-alignment control selects one option, while its font-attribute controls can combine bold, italic, and underline. Keynote also groups controls for showing and hiding editing panes.

Native segmented controls can also offer momentary actions without retaining a selection, such as Mail's Reply, Reply All, and Forward controls on macOS. See UIKit's [isMomentary](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/ismomentary) and AppKit's [momentary tracking mode](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/switchtracking/momentary).

- **Group closely related choices or actions** - A control can select attributes, switch related views, or group actions on the current view. Its connected appearance makes the grouping visible even when the interface changes size.
- **Use one interaction model within a control** - Don't mix segments that retain selection with segments that perform momentary actions.
- **Avoid crowding the control with too many segments** - Too many segments can be hard to parse and time-consuming to navigate. Aim for no more than about five to seven segments in a wide interface and no more than about five segments on iPhone.
- **In general, keep segment size consistent** - When all segments have equal width, a segmented control feels balanced. To the extent possible, it's best to keep icon and title widths consistent too.

### Content

- **Prefer using either text or images — not a mix of both — in a single segmented control** - Although individual segments can contain text labels or images, mixing the two in a single control can lead to a disconnected and confusing interface.
- **As much as possible, use content with a similar size in each segment** - Because all segments typically have equal width, it doesn't look good if content fills some segments but not others.
- **Use nouns or noun phrases for segment labels** - Write text that describes each segment and uses title-style capitalization. A segmented control that displays text labels doesn't need introductory text.

**SwiftUI-specific guidance differs:** The [`segmented` picker-style reference](https://developer.apple.com/documentation/swiftui/pickerstyle/segmented) recommends two to five options and sentence-style labels. Follow that API's guidance when using this SwiftUI style; the HIG's broader five-to-seven recommendation is not a universal API limit.

### Platform Considerations

**watchOS**  
Not supported in watchOS.

**iOS, iPadOS**  
- **Switch between related subviews** - For example, Calendar's New Event sheet switches between creating an event and a reminder. Use a [tab bar](https://developer.apple.com/design/human-interface-guidelines/tab-bars), rather than a segmented control, for separate top-level app sections.

**macOS**  
- **Consider using introductory text to clarify the purpose of a segmented control** - When the control uses symbols or interface icons, you could also add a label below each segment to clarify its meaning. If your app includes tooltips, provide one for each segment in a segmented control.
- **Use a tab view in the main window area — instead of a segmented control — for view switching** - A tab view supports efficient view switching and is similar in appearance to a box combined with a segmented control. Consider using a segmented control to help people switch views in a toolbar or inspector pane.
- **Consider supporting spring loading** - On a Mac equipped with a Magic Trackpad, spring loading lets people activate a segment by dragging selected items over it and force clicking without dropping the selected items. People can also continue dragging the items after a segment activates.

**tvOS**  
- **Consider using a split view instead of a segmented control on screens that perform content filtering** - People generally find it easy to navigate back and forth between content and filtering options using a split view. Depending on its placement, a segmented control may not be as easy to access.
- **Avoid putting other focusable elements close to segmented controls** - Segments become selected when focus moves to them, not when people click them. Carefully consider where you position a segmented control relative to other interface elements. If other focusable elements are too close, people might accidentally focus on them when attempting to switch between segments.

**visionOS**  
When people look at a segmented control that uses icons, the system displays a tooltip that contains the descriptive text you supply.

### Related Components

- [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views)

### Developer Documentation

- [segmented](https://developer.apple.com/documentation/swiftui/pickerStyle/segmented) - SwiftUI
- [UISegmentedControl](https://developer.apple.com/documentation/uikit/uisegmentedcontrol) - UIKit
- [NSSegmentedControl](https://developer.apple.com/documentation/appkit/nssegmentedcontrol) - AppKit

## Changelog

These dates describe changes to Apple's HIG article, not edits to this repository.

### June 21, 2023
- Updated to include guidance for visionOS.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)*
