# Tab Views

A tab view presents multiple mutually exclusive panes of content in the same area, which people can switch between using a tabbed control.

**Platforms:** macOS | watchOS

## Overview

Tab views provide a strong visual indication of enclosure, helping organize related content into separate panes. Each pane is mutually exclusive, displaying content that is similar or related to the content in other tabs. The tabbed control enables efficient navigation with a single click or tap to switch between panes.

This page follows the HIG's tabbed-pane component and watchOS paging guidance. Its platform list is not the availability of SwiftUI's `TabView`, which also provides tab navigation on iOS, iPadOS, tvOS, and visionOS; see [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars).

## Topics

### Best Practices

- **Use a tab view to present closely related areas of content** - The appearance of a tab view provides a strong visual indication of enclosure. People expect each tab to display content that is in some way similar or related to the content in the other tabs.

- **Make sure the controls within a pane affect content only in the same pane** - Panes are mutually exclusive, so ensure they're fully self-contained.

- **Provide a label for each tab that describes the contents of its pane** - A good label helps people predict the contents of a pane before clicking or tapping its tab. In general, use nouns or short noun phrases for tab labels. A verb or short verb phrase may make sense in some contexts. Use title-style capitalization for tab labels.

- **Avoid using a pop-up button to switch between tabs** - A tabbed control is efficient because it requires a single click or tap to make a selection, whereas a pop-up button requires two. A tabbed control also presents all choices onscreen at the same time, whereas people must click a pop-up button to see its choices. Note that a pop-up button can be a reasonable alternative in cases where there are too many panes of content to reasonably display with tabs.

- **Avoid providing more than six tabs in a tab view** - Having more than six tabs can be overwhelming and create layout issues. If you need to present six or more tabs, consider another way to implement the interface. For example, you could instead present each tab as a view option in a pop-up button menu.

### Anatomy

The current HIG describes a tabbed control along the top edge of the content area. You can hide the control when the app switches panes programmatically.

When you hide the tabbed control, the content area can be borderless, bezeled, or bordered with a line. A borderless view can be solid or transparent.

In general, inset a tab view by leaving a margin of window-body area on all sides of a tab view. This layout looks clean and leaves room for additional controls that aren't directly related to the contents of the tab view. You can extend a tab view to meet the window edges, but this layout is unusual.

### Platform Considerations

**macOS**  
- Use native tabbed panes with the top-edge presentation described above
- See [NSTabView](https://developer.apple.com/documentation/appkit/nstabview) for developer guidance

**iOS, iPadOS**  
- The HIG doesn't apply this tabbed-pane component to these platforms. For closely related subviews, consider a [segmented control](https://developer.apple.com/design/human-interface-guidelines/segmented-controls); use tab navigation for top-level app sections.

**tvOS, visionOS**  
- Outside this HIG component's scope; this doesn't exclude SwiftUI `TabView` or platform tab navigation

**watchOS**  
- watchOS displays tab views using page controls
- For vertical paging, the HIG illustrates the page control next to the Digital Crown, with an enlarged current dot indicating scrolling within the content as well as between pages
- For developer guidance, see [TabView](https://developer.apple.com/documentation/swiftui/tabview) and [verticalPage](https://developer.apple.com/documentation/swiftui/tabviewstyle/verticalpage), which is available in watchOS 10 or later

### Related Components

- [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) - Navigation component for switching between major sections of an app
- [Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls) - Alternative for iOS and iPadOS

### Developer Documentation

- [TabView](https://developer.apple.com/documentation/swiftui/tabview) - SwiftUI
- [NSTabView](https://developer.apple.com/documentation/appkit/nstabview) - AppKit

## Changelog

These dates describe changes to Apple's HIG article, not edits to this repository.

### June 5, 2023
- Added guidance for using tab views in watchOS

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/tab-views)*
