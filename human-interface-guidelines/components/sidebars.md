# Sidebars

A sidebar appears on the leading side of a view and lets people navigate between sections in your app or game.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS

## Overview

A sidebar floats above content without being anchored to the edges of the view. It provides a broad, flat view of an app's information hierarchy, giving people access to several peer content areas or modes at the same time.

A sidebar requires a large amount of vertical and horizontal space. When space is limited or you want to devote more of the screen to other information or functionality, a more compact control such as a tab bar may provide a better navigation experience. For guidance, see [Layout](https://developer.apple.com/design/human-interface-guidelines/layout).

## Topics

### Best Practices

- **Extend visually rich content beneath a floating sidebar** - On iOS, iPadOS, and macOS, sidebars can appear in the Liquid Glass layer above content. Where appropriate, let rich content scroll beneath the sidebar or use a background extension effect to mirror adjacent imagery into that area. See [backgroundExtensionEffect()](https://developer.apple.com/documentation/swiftui/view/backgroundextensioneffect()).

- **Let people customize the contents when possible** - A sidebar lets people navigate to important areas in your app, so it works well when people can decide which areas are most important and in what order they appear.

- **Group hierarchy with disclosure controls** - Using disclosure controls helps keep the sidebar's vertical space to a manageable level if your app has a lot of content.

- **Use familiar symbols to represent items** - SF Symbols provides a wide range of customizable symbols you can use to represent items in your app. If you need to use a custom icon, consider creating a custom symbol rather than using a bitmap image. Download the SF Symbols app from [Apple Design Resources](https://developer.apple.com/design/resources/).

- **Consider letting people hide the sidebar** - People sometimes want to hide the sidebar to create more room for content details or to reduce distraction. When possible, let people hide and show the sidebar using the platform-specific interactions they already know. For example, in iPadOS, people expect to use the built-in edge swipe gesture; in macOS, you can include a show/hide button or add Show Sidebar and Hide Sidebar commands to your app's View menu. In visionOS, a window typically expands to accommodate a sidebar, so people rarely need to hide it. Avoid hiding the sidebar by default to ensure that it remains discoverable.

- **Show no more than two levels of hierarchy** - When a data hierarchy is deeper than two levels, consider using a split view interface that includes a content list between the sidebar items and detail view.

- **Use succinct, descriptive labels** - If you need to include two levels of hierarchy in a sidebar, use succinct, descriptive labels to title each group. To help keep labels short, omit unnecessary words.

- **Use icon color purposefully** - Sidebar icons normally use the app's accent color. On macOS, respect the system accent color a person chooses. Use fixed colors sparingly when they convey meaning or importance, as Mail does with its yellow VIP icon.

### Platform Considerations

No additional considerations for tvOS. Not supported in watchOS.

**iOS, iPadOS**

- Use the adaptable tab style with its platform-specific presentation. The [`sidebarAdaptable` API reference](https://developer.apple.com/documentation/swiftui/tabviewstyle/sidebaradaptable) specifies a bottom tab bar on iOS and a top tab bar that can become a sidebar on iPadOS. On iPadOS, choose the initial appearance and retain the standard toggle; the style responds to rotation and window resizing. The HIG discusses these platforms together, but the API doesn't promise the same presentation on both.
- Consider using a tab bar first. A tab bar provides more space to feature content, and offers enough flexibility to navigate between many apps' main areas. If you need to expose more areas than fit in a tab bar, the tab bar's convertible sidebar-style appearance can provide access to content that people use less frequently. For guidance, see [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars).
- For a UIKit collection-view sidebar, choose the sidebar appearance from [UICollectionLayoutListConfiguration.Appearance](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum) rather than recreating its styling.

Developer note: To display a sidebar only, use NavigationSplitView to present a sidebar in the primary pane of a split view, or use UISplitViewController.

**macOS**  
- A sidebar's row height, text, and glyph size depend on its small, medium, or large size. Respect the person's system sidebar icon-size preference as well as programmatic sizing.
- Consider automatically hiding and revealing a sidebar when its container window resizes. For example, reducing the size of a Mail viewer window can automatically collapse its sidebar, making more room for message content.
- Avoid putting critical information or actions at the bottom of a sidebar. People often relocate a window in a way that hides its bottom edge.

**visionOS**  
- If your app's hierarchy is deep, consider using a sidebar within a tab in a tab bar. In this situation, a sidebar can support secondary navigation within the tab. If you do this, be sure to prevent selections in the sidebar from changing which tab is currently open.

### Related Components

- [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views)
- [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars)
- [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)

### Developer Documentation

- [sidebarAdaptable](https://developer.apple.com/documentation/swiftui/tabviewstyle/sidebaradaptable) - SwiftUI
- [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview) - SwiftUI
- [sidebar](https://developer.apple.com/documentation/swiftui/liststyle/sidebar) - SwiftUI
- [UICollectionLayoutListConfiguration](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct) - UIKit
- [NSSplitViewController](https://developer.apple.com/documentation/appkit/nssplitviewcontroller) - AppKit

### Videos

- [Elevate the design of your iPad app](https://developer.apple.com/videos/play/wwdc2025/208)

## Changelog

These dates describe changes to Apple's HIG article, not edits to this repository.

### June 8, 2026
- Updated sidebar icon-color guidance and clarified the adaptable sidebar style.

### June 9, 2025
- Added guidance for extending content beneath the sidebar

### August 6, 2024
- Updated guidance to include the SwiftUI adaptable sidebar style

### December 5, 2023
- Added artwork for iPadOS

### June 21, 2023
- Updated to include guidance for visionOS

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/sidebars)*
