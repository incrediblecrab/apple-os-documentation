# Tab Bars

A tab bar lets people navigate between top-level sections of your app.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS

## Overview

Tab bars help people understand the different types of information or functionality that an app provides. They also let people quickly switch between sections of the view while preserving the current navigation state within each section.

For guidance using a similar component in macOS, see [tab views](https://developer.apple.com/design/human-interface-guidelines/tab-views).

## Topics

### Best Practices

- **Use a tab bar to support navigation, not to provide actions** - A tab bar lets people navigate among different sections of an app, like the Alarm, Stopwatch, and Timer tabs in the Clock app. If you need to provide controls that act on elements in the current view, use a toolbar instead.

- **Make sure the tab bar is visible when people navigate to different sections of your app** - If you hide the tab bar, people can forget which area of the app they're in. The exception is when a modal view covers the tab bar, because a modal is temporary and self-contained.

- **Use the appropriate number of tabs required to help people navigate your app** - As a representation of your app's hierarchy, it's important to weigh the complexity of additional tabs against the need for people to frequently access each section; keep in mind that it's generally easier to navigate among fewer tabs. Where available, consider a sidebar or a tab bar that adapts to a sidebar as an alternative for an app with a complex information structure.

- **Avoid overflow tabs whenever possible** - Depending on device size and orientation, the number of visible tabs can be smaller than the total number of tabs. If horizontal space limits the number of visible tabs, the trailing tab becomes a More tab in iOS and iPadOS, revealing the remaining items in a separate list. The More tab makes it harder for people to reach and notice content on tabs that are hidden, so try to limit scenarios in your app where this can happen.

- **Don't disable or hide tab bar buttons, even when their content is unavailable** - Having tab bar buttons available in some cases but not others makes your app's interface appear unstable and unpredictable. If a section is empty, explain why its content is unavailable.

- **Use a succinct term for each tab title** - A useful tab title aids navigation by clearly describing the type of content or functionality the tab contains. Use single words whenever possible.

- **Reserve badges for critical information** - A badge can draw attention to an important update in a tab. Using badges for routine information weakens their meaning. For guidance, see [Notifications](https://developer.apple.com/design/human-interface-guidelines/notifications).

### Platform Considerations

**General**  
No additional considerations for macOS. Not supported in watchOS.

**iOS**  
- In the Liquid Glass design, the tab bar floats over content at the bottom of the screen. Its material lets underlying content remain visible.

- A tab bar with an accessory, such as a media player, can minimize while people scroll down and move the accessory inline. People can expand it by tapping a tab or scrolling to the top. Use the documented minimization behavior rather than hiding navigation yourself.

- A dedicated search tab can appear at the trailing end; see [Search fields](search-fields.md).

- Consider using SF Symbols to provide scalable, visually consistent tab bar icons. When you use SF Symbols, tab bar icons automatically adapt to different contexts. For example, the tab bar can be regular or compact, depending on the current device and orientation. Also, tab bar icons can appear above tab titles in portrait orientation, whereas in landscape, the icons and titles can appear side by side. Prefer filled symbols or icons for consistency with the platform.

- For custom tab bar icons, use the current templates in [Apple Design Resources](https://developer.apple.com/design/resources/), and check regular and compact presentations.

#### Target Dimensions

Apple now directs designers to its design-resource templates for tab bar icon dimensions rather than publishing a fixed shape-by-shape table in this HIG article. Use the template for the platform and appearance you are targeting; prefer SF Symbols when an appropriate symbol exists.

**iPadOS**  
- Starting with iPadOS 18, the system displays a tab bar near the top of the screen. You can choose to have the tab bar appear as a fixed element, or include a button that converts it to a sidebar. For developer guidance, see tabBarOnly and sidebarAdaptable.

- **Note:** To present a sidebar without the option to convert it to a tab bar, use a navigation split view instead of a tab view. For guidance, see [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars).

- Prefer a tab bar for navigation. A tab bar provides access to the sections of your app that people use most. If your app is more complex, you can provide the option to convert the tab bar to a sidebar so people can access a wider set of navigation options.

- Let people customize the tab bar. In apps with a lot of sections that people might want to access, it can be useful to let people select items that they use frequently and add them to the tab bar, or remove items that they use less frequently. For example, in the Music app, a person can choose a favorite playlist to display in the tab bar. For developer guidance, see TabViewCustomization and UITab.Placement.

- When offering tab customization, start with five or fewer default tabs to help preserve continuity between compact and regular sizes.

**tvOS**  
- A tab bar is highly customizable. For example, you can:
  - Specify a tint, color, or image for the tab bar background
  - Choose a font for tab items, including a different font for the selected item
  - Specify tints for selected and unselected items
  - Add button icons, like settings and search

- By default, a tab bar is translucent, and only the selected tab is opaque. When people use the remote to focus on the tab bar, the selected tab includes a drop shadow that emphasizes its selected state. The height of a tab bar is 68 points, and its top edge is 46 points from the top of the screen; you can't change either of these values.

- If there are more items than can fit in the tab bar, the system truncates the rightmost item by applying a fade effect that begins at the right side of the tab bar. If there are enough items to cause scrolling, the system also applies a truncating fade effect that starts from the left side.

- If you use an icon for a tab title, make sure it's familiar. You can use icons as tab titles to help save space, but only for universally recognized symbols like search or settings. Using an unfamiliar symbol without a descriptive title can confuse people. For guidance, see [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols).

- Be aware of tab bar scrolling behaviors. By default, people can scroll the tab bar offscreen when the current tab contains a single main view. You can see examples of this behavior in the Watch Now, Movies, TV Show, Sports, and Kids tabs in the TV app. The exception is when a screen contains a split view, such as the TV app's Library tab or an app's Settings screen. In this case, the tab bar remains pinned at the top of the view while people scroll the content within the primary and secondary panes of the split view. Regardless of a tab's contents, focus always returns to the tab bar at the top of the page when people press Menu on the remote.

- In a live-viewing app, organize tabs in a consistent way. For the best experience, organize content in live-streaming apps with tabs in the following order:
  1. Live content
  2. Cloud DVR or other recorded content
  3. Other content

- For additional guidance, see [Live-viewing apps](https://developer.apple.com/design/human-interface-guidelines/live-viewing-apps).

- If you add branding near navigation, keep it within the screen's safe area and avoid crowding the tabs. See [Layout](../foundations/layout.md) for tvOS safe-area guidance.

**visionOS**  
- In visionOS, a tab bar is always vertical, floating in a position that's fixed relative to the window's leading side. When people look at a tab bar, it automatically expands; to open a specific tab, people look at the tab and tap. While a tab bar is expanded, it can temporarily obscure the content behind it.

- Supply a symbol and a text title for each tab. A tab's symbol is always visible in the tab bar. When people look at the tab bar, the system reveals tab titles, too. Even though the tab bar expands, you need to keep tab titles short so people can read them at a glance.
  - **Collapsed:** Tab bar contains only symbols
  - **Expanded:** Tab bar contains both symbols and titles

- If it makes sense in your app, consider using a sidebar within a tab. If your app's hierarchy is deep, you might want to use a sidebar to support secondary navigation within a tab. If you do this, be sure to prevent selections in the sidebar from changing which tab is currently open.

### Related Components

- [Tab views](https://developer.apple.com/design/human-interface-guidelines/tab-views) - Similar component for macOS
- [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars) - For providing actions on current content
- [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars) - Alternative navigation for complex hierarchies

### Developer Documentation

- [TabView](https://developer.apple.com/documentation/swiftui/tabview) - SwiftUI
- [Enhancing your app's content with tab navigation](https://developer.apple.com/documentation/swiftui/enhancing-your-app-content-with-tab-navigation) - SwiftUI
- [UITabBar](https://developer.apple.com/documentation/uikit/uitabbar) - UIKit
- [Elevating your iPad app with a tab bar and sidebar](https://developer.apple.com/documentation/uikit/elevating-your-ipad-app-with-a-tab-bar-and-sidebar) - UIKit

### Videos

- [Get to know the new design system](https://developer.apple.com/videos/play/wwdc2025/356)
- [Elevate the design of your iPad app](https://developer.apple.com/videos/play/wwdc2025/208)

## Changelog

### June 8, 2026
- Apple updated terminology and artwork.

### December 16, 2025
- Apple updated Liquid Glass guidance.

### July 28, 2025
- Apple added Liquid Glass guidance.

### September 9, 2024
- Added art representing the tab bar in iPadOS 18

### August 6, 2024
- Updated with guidance for the tab bar in iPadOS 18

### June 21, 2023
- Updated to include guidance for visionOS

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/tab-bars)*
