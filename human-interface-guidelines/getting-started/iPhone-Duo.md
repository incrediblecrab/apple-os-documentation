# Designing for iPhone Duo

An iPhone Duo app moves between an outer and an inner display as people close, open, and fold the device, and it should keep one continuous experience through each change.

**Platforms:** iOS

## Overview

iPhone Duo is an iPhone with two displays, each with its own front-facing camera, joined by a center hinge. People open it, close it, and hold or stand it in several positions, so the same app can appear at many sizes. An app built from standard system components that already supports resizing adapts to these positions with little extra work. It is still an iPhone app: the guidance in [Designing for iOS](iOS.md) continues to apply, and this page covers only what the second display, the hinge, and the side-mounted bars add. Apple added the HIG article on September 9, 2026.

**Displays.** People use the outer display when the device is closed. It is wider and shorter than the display on other iPhone models, so the system moves toolbars and tab bars to the side to leave more height for content. When the device opens in landscape, the bars stay on the side so they don't jump as people move from one display to the other.

**Hinge.** The hinge supports a range of grips and positions, and as the device folds, the fold takes space away from your content.

**Cameras.** The outer front-facing camera sits in a corner, is always visible, and lines up vertically with the controls on the side. The inner front-facing camera sits behind the display and stays hidden until the camera is in use.

**Poses.** People hold iPhone Duo partly folded like a book, lay it on a surface, or stand it on an edge. You don't need a separate layout for each pose. Use [size classes](../foundations/layout.md): a compact-width layout for the outer display and a regular-width layout for the inner display cover every pose, and the existing layout should grow into the extra space rather than turning into a different app. Xcode's [Device Hub](https://developer.apple.com/documentation/xcode/device-hub) can preview an app on iPhone Duo in its different poses.

Start with [Designing for iOS](iOS.md) and [Layout](../foundations/layout.md), then check your app on both displays and in each pose.

## Topics

### Best Practices

- **Make every view resizable** - Two displays, many poses, and Split View multitasking mean your app can appear at many sizes. Lay out content and controls with size classes, layout margins, and safe area insets, and avoid fixed widths or anything that depends on a particular display.

- **Keep the two displays consistent** - Keep features and the state of each element the same on both displays and keep the information hierarchy intact. The larger inner display can show one more level of hierarchy when your content benefits from it: closed, Mail shows either the message list or a single message; open, it shows both side by side.

- **Keep every feature available in every pose** - As the interface adapts, controls can move into an overflow menu and content can shift or resize, but people should reach the same controls and content however they hold the device.

- **Use the system's side placement for bars** - Toolbars, tab bars, and navigation controls move to the side on the outer display, and stay on the side on the inner display in landscape. Standard components get this layout automatically; refine it for your app rather than replacing it. See [Vertical controls](#vertical-controls).

- **Let games play in every pose** - A game can lock to portrait or landscape, but it still needs to fill the screen when the pose changes. Keep text and control sizes as stable as possible while resizing, and change the aspect ratio instead of adding letterbox or pillarbox bars. If bars can't be avoided, fill them with artwork so the game still feels full screen. See [Designing for games](designing-for-games.md).

### Dynamic layouts

Build layouts from layout margins and safe area insets, as on every iOS device, and avoid fixed widths and display-specific assumptions. On iPhone Duo, available space is also shaped by *reserved regions*: areas that content stays clear of, or that components adjust around, much like the window controls on iPad.

- **Outer front-facing camera** - Always present. It grows into the Dynamic Island for Live Activities. When bars are on the side, the system arranges them around it.
- **Inner front-facing camera** - Present only while the camera is active. The camera is invisible when inactive; when it turns on, the interface moves aside to show where it is.
- **Folding region** - Present only when the device is partly open. The fold splits the inner display into separate usable areas and leaves the center strip out.

Many system components handle reserved regions for you. Alerts, context menus, and sheets move away from the fold, and [split views](../components/split-views.md) adjust column widths and margins to match the inner display's symmetry. Custom components can read reserved regions through `ReservedRegion` in SwiftUI or `UIView.ReservedRegion` in UIKit and move content out of them.

- **Adapt to the fold** - Prefer containers that adjust on their own, such as the Notes split view, which resizes each pane so both stay readable as the device folds. In a grid, use an even number of columns so the content divides cleanly at the fold. Where the system doesn't move an important element away from the center, move it with the `ReservedRegion` API.

- **Keep layout changes small while the device folds** - Move only what has to move to stay visible and easy to tap. Controls that vanish or jump are hard to find again, so prefer small adjustments to rearranging the screen.

### Split views and arrangement views

A [split view](../components/split-views.md) expands on the inner display and collapses to one pane on the outer display, the same way it changes between regular and compact environments on other iPhone models. A split view built from standard components adjusts its widths and margins for the fold automatically.

An *arrangement view* is a layout container with a primary and a secondary view that it arranges according to display size, orientation, and reserved regions. It has two styles. A *split* arrangement divides its area between the two views: side by side when the arrangement is wider than it is tall, one above the other when it is taller than it is wide, and you can restrict which axes it uses. An *overlay* arrangement stacks the primary view over the secondary view; when the display is partly folded, the two views move to opposite sides of the fold, and you can collapse the secondary view when you don't want it shown.

- **Use an arrangement view where your layout already has that shape** - Two views placed side by side or stacked, as with `HStack` or `VStack`, map to a split arrangement. One view layered over another, as with `ZStack`, maps to an overlay arrangement.

- **Put navigation around an arrangement view, not inside it** - An arrangement view only lays out content. Place navigation split views, tab views, and other navigation containers outside it.

### Vertical controls

On iPhone Duo, toolbars, tab bars, and navigation controls that normally sit at the top and bottom of the display move to the side, which leaves more height for content and keeps the controls within reach. The inner display in portrait is the exception: it has enough height to keep standard horizontal bars. The side column holds both system and app elements: the Dynamic Island, the status bar, the toolbar with its navigation buttons, and the tab bar.

When two apps share the inner display in Split View multitasking, each app puts its controls along its own outer edge, so the app on the left has its controls on the left. Because side controls follow the hardware, they keep the same position relative to the outer camera and stay on the same side in right-to-left languages.

- **Plan for an asymmetric content area** - With controls along one edge, the content area is off center. Use safe areas so no controls cover your content, including controls on the far edge when two apps share the inner display.

- **Keep control positions stable across poses** - Not every pose puts controls on the side, and available space varies, so keep each control's relative position as close as you can. People shouldn't have to relearn where an action is after changing pose.

- **Use the standard order for toolbar items** - The top of the side column is for primary navigation such as Back or Close, followed by prominent actions such as Done. Keep the remaining items in their original groups; the system adds a gap between items that came from the top bar and items that came from the bottom bar.

- **Rank toolbar items so the important ones stay visible** - By default, items move into the overflow menu starting from the bottom. Set a visibility priority to change that order, first for whole groups and then for single items when you need finer control. Keep frequent actions, such as Compose in Mail or New Note in Notes, and status items, such as items with badges, visible longest.

- **Leave the default bar placement alone in most cases** - Side-mounted controls are a core iPhone Duo pattern, and keeping them where people expect helps them learn your app quickly.

- **Consider the full display width where bars aren't needed** - Visual, immersive layouts that don't scroll can span the full width if nothing conflicts with the Dynamic Island or the status bar; Calculator does this. You can also let a background image or header run full width while scrolling content stays inset.

- **Group toolbar items instead of adding space by hand** - [Toolbar](../components/toolbars.md) groups, such as `ToolbarItemGroup` in SwiftUI or `UIBarButtonItemGroup` in UIKit, put space between items and groups and adapt as space changes. Don't add fixed spacing.

- **Keep controls with the content they act on** - When controls belong to a pane other than the one along the trailing edge, leave them with that pane instead of moving them to the side. In Mail, the controls for the message list stay above the leading pane, which shows that they act on the list rather than on the open message.

- **Give each non-text toolbar item both a title and a symbol** - The system then picks the right form for each context. Provide the title even when the item shows a symbol, because the overflow menu and expanded layouts use it.

- **Use few text-only buttons** - An item with a text label and no symbol stays in a horizontal bar and isn't placed in the side column, so use a symbol wherever one works.

- **When space runs out, choose between the toolbar and the tab bar by task** - In views centered on navigation, the system's default is to move toolbar items into the overflow menu and keep the tab bar and its destinations visible. In task-focused views, minimize the tab bar instead so the toolbar actions needed to finish the task stay visible, as the minimized tab bar does on other iPhone models.

- **Use the system overflow menu** - Move actions from a custom overflow menu into the system one so people find everything in one place. Use the ellipsis symbol only for overflow, and give other menus a different symbol.

### Validation

- Build with the current Xcode. Apple's [Preparing your app for iPhone Duo](https://developer.apple.com/documentation/technologyoverviews/preparing-your-app-for-iphone-duo) says an app built with Xcode 26 or earlier doesn't extend under the status bar and camera on iPhone Duo.
- Run the app in a simulator or on the device, and check both displays closed, open, and partly folded. Rotate the device in each pose.
- Go through every view, sheet, and popover. Look for layouts that break when you fold or open the device and for controls that land in the fold.
- Check how the system places your navigation bars, toolbars, and tab bars on the side, and confirm that frequent actions stay out of the overflow menu.
- Test a right-to-left language. Side controls stay on the same physical edge, so confirm that your content still clears them.

### Resources

- [Designing for iOS](iOS.md)
- [Layout](../foundations/layout.md)
- [Split views](../components/split-views.md)
- [Toolbars](../components/toolbars.md)
- [Designing for games](designing-for-games.md)
- [Apple Design Resources](https://developer.apple.com/design/resources/#ios-apps)
- [Screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications)

### Developer Documentation

The fold, arrangement, and bar-compression APIs below are available starting in iOS 27.1. The visibility-priority types and `ToolbarOverflowMenu` start in iOS 27.0.

- [Preparing your app for iPhone Duo](https://developer.apple.com/documentation/technologyoverviews/preparing-your-app-for-iphone-duo)
- [ReservedRegion](https://developer.apple.com/documentation/swiftui/reservedregion) (SwiftUI) and [UIView.ReservedRegion](https://developer.apple.com/documentation/uikit/uiview/reservedregion) (UIKit) - iOS 27.1
- [ArrangementView](https://developer.apple.com/documentation/swiftui/arrangementview) (SwiftUI) and [UIArrangementViewController](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller) (UIKit) - iOS 27.1
- [ToolbarVerticalCompressionBehavior](https://developer.apple.com/documentation/swiftui/toolbarverticalcompressionbehavior) (SwiftUI) and [UIVerticalBarCompressionBehavior](https://developer.apple.com/documentation/uikit/uiverticalbarcompressionbehavior) (UIKit) - iOS 27.1
- [ToolbarItemVisibilityPriority](https://developer.apple.com/documentation/swiftui/toolbaritemvisibilitypriority) (SwiftUI) and [UIBarButtonItemVisibilityPriority](https://developer.apple.com/documentation/uikit/uibarbuttonitemvisibilitypriority) (UIKit) - iOS 27.0
- [ToolbarOverflowMenu](https://developer.apple.com/documentation/swiftui/toolbaroverflowmenu) (SwiftUI, iOS 27.0) and [additionalOverflowItems](https://developer.apple.com/documentation/uikit/uinavigationitem/additionaloverflowitems) (UIKit, iOS 16.0)
- [Device Hub](https://developer.apple.com/documentation/xcode/device-hub)

### Videos

- [Design for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111466)
- [Raise the bar with iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111462)
- [Strike a pose with adaptive layouts on iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111463)

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo)*
