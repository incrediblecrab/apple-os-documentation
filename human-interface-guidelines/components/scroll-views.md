# Scroll Views

A scroll view lets people view content that's larger than the view's boundaries by moving the content vertically or horizontally.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

The scroll view itself has no appearance, but it can display a translucent scroll indicator that typically appears after people begin scrolling the view's content. Although the appearance and behavior of scroll indicators can vary per platform, all indicators provide visual feedback about the scrolling action. For example, in iOS, iPadOS, macOS, visionOS, and watchOS, the indicator shows whether the currently visible content is near the beginning, middle, or end of the view.

## Topics

### Best Practices

- **Support default scrolling gestures and keyboard shortcuts** - People are accustomed to the systemwide scrolling behavior and expect it to work everywhere. If you build custom scrolling for a view, make sure your scroll indicators use the elastic behavior that people expect.
- **Make it apparent when content is scrollable** - Because scroll indicators aren't always visible, it can be helpful to make it obvious when content extends beyond the view. For example, displaying partial content at the edge of a view indicates that there's more content in that direction. Although most people immediately try scrolling a view to discover if additional content is available, it's considerate to draw their attention to it.
- **Avoid putting a scroll view inside another scroll view with the same orientation** - Nesting scroll views that have the same orientation can create an unpredictable interface that's difficult to control. It's alright to place a horizontal scroll view inside a vertical scroll view (or vice versa), however.
- **Consider supporting page-by-page scrolling if it makes sense for your content** - In some situations, people appreciate scrolling by a fixed amount of content per interaction instead of scrolling continuously. On most platforms, you can define the size of such a page — typically the current height or width of the view — and define an interaction that scrolls one page at a time. To help maintain context during page-by-page scrolling, you can define a unit of overlap, such as a line of text, a row of glyphs, or part of a picture, and subtract the unit from the page size.
- **In some cases, scroll automatically to help people find their place** - Although people initiate almost all scrolling, automatic scrolling can be helpful when relevant content is no longer in view, such as when:
  - Your app performs an operation that selects content or places the insertion point in an area that's currently hidden
  - People start entering information in a location that's not currently visible
  - The pointer moves past the edge of the view while people are making a selection
  - People select something and scroll to a new location before acting on the selection
- **If you support zoom, set appropriate maximum and minimum scale values** - For example, zooming in on text until a single character fills the screen doesn't make sense in most situations.

### Platform Considerations

**iOS, iPadOS**  
- **In general, display one scroll view per screen** - People often make large swipe gestures when scrolling, and it can be hard to avoid interacting with a neighboring scroll view on the same screen. If you need to put two scroll views on one screen, consider allowing them to scroll in different directions so one gesture is less likely to affect both views.
- **Consider showing a page control when a scroll view is in page-by-page mode** - Page controls show how many pages, screens, or other chunks of content are available and indicates which one is currently visible. If you show a page control with a scroll view, don't show the scrolling indicator on the same axis to avoid confusing people with redundant controls.

**macOS**  
In macOS, a scroll indicator is commonly called a scroll bar.

- **Account for scroll bars in your layout** - By default, scroll bars appear only when people interact with views that contain them, but people can use a setting in General settings to make them appear all the time. Some input devices also cause scroll bars to display all the time. If necessary, adjust the layout of your window so important interface elements don't appear beneath scroll bars. The scroll bar track has a thickness of 15 points (regular size) or 11 points (small or mini size).
- **Avoid moving window content when transient scroll bars appear** - Constantly shifting content every time scroll bars appear can be disorienting.
- **Avoid placing controls inline with a scroll bar** - Doing this can cause the bar to appear even when people set it to be transient.
- **If necessary, use small or mini scroll bars in a panel** - When space is tight, you can use smaller scroll bars in panels that need to coexist with other windows. Be sure to use the same size for all controls in such a panel.

**tvOS**  
Views in tvOS can scroll, but they aren't treated as distinct objects with scroll indicators. Instead, when content exceeds the size of the screen, the system automatically scrolls the interface to keep focused items visible.

**visionOS**  
In visionOS, the scroll indicator has a small, fixed size to help communicate that people can scroll efficiently without making large movements. To make it easy to find, the scroll indicator always appears in a predictable location with respect to the window: vertically centered at the trailing edge during vertical scrolling and horizontally centered at the window's bottom edge during horizontal scrolling.

When people begin swiping content in the direction they want it to scroll, the scroll indicator appears at the window's edge, visually reinforcing the effect of their gesture and providing feedback about the content's current position and overall length. When people look at the scroll indicator and begin a drag gesture, the indicator enables a jog bar experience that lets people manipulate the scrolling speed instead of the content's position.

- **If necessary, account for the size of the scroll indicator** - Although the indicator's overall size is small, it's a little thicker than the same component in iOS. If your content uses tight margins, consider increasing them to prevent the scroll indicator from overlapping the content.

**watchOS**  
- **Prefer vertically scrolling content** - People are accustomed to using the Digital Crown to navigate to and within apps on Apple Watch. If your app contains a single list or content view, rotating the Digital Crown scrolls vertically when your app's content is taller than the height of the display.
- **Use tab views to provide page-by-page scrolling** - watchOS displays tab views as pages. If you place tab views in a vertical stack, people can rotate the Digital Crown to move vertically through full-screen pages of content. In this scenario, the system displays a page indicator next to the Digital Crown that shows people where they are in the content.
- **When displaying paged content, consider limiting the content of an individual page to a single screen height** - Embracing this constraint clarifies the purpose of each page, helping you create a more glanceable design. However, if your app has long pages, people can still use the Digital Crown both to navigate between shorter pages and to scroll content in a longer page because the page indicator expands into a scroll indicator when necessary.

### Related Components

- [Page controls](https://developer.apple.com/design/human-interface-guidelines/page-controls) - For page-by-page navigation
- [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures) - Scrolling gesture guidance
- [Pointing devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices) - Scrolling with pointing devices

### Developer Documentation

- [ScrollView](https://developer.apple.com/documentation/swiftui/scrollview) - SwiftUI
- [UIScrollView](https://developer.apple.com/documentation/uikit/uiscrollview) - UIKit
- [NSScrollView](https://developer.apple.com/documentation/appkit/nsscrollview) - AppKit
- [WKPageOrientation](https://developer.apple.com/documentation/watchkit/wkpageorientation) - WatchKit
- [PagingScrollTargetBehavior](https://developer.apple.com/documentation/swiftui/pagingscrolltargetbehavior) - SwiftUI

## Changelog

### February 2, 2024
- Added artwork showing the behavior of the visionOS scroll indicator.

### December 5, 2023
- Described the visionOS scroll indicator and added guidance for integrating it with window layout.

### June 5, 2023
- Updated guidance for using scroll views in watchOS.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/scroll-views)*