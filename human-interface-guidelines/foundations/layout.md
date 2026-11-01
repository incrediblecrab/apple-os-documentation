# Layout

A consistent layout that adapts across display sizes, orientations, and multitasking configurations helps people understand and enjoy your app or game on all their devices.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

Your layout gives people the structure they use to understand your content from the moment they open your app. When controls and content keep familiar relationships, people can use and discover features right away, and your design feels at home on each platform.

Apple provides templates and layout guides that can help you integrate Apple technologies and design your apps and games to run on all Apple platforms. See Apple Design Resources.

## Topics

### Visual hierarchy

**Place items to convey their relative importance.** People often start by viewing items in reading order — that is, from top to bottom and from the leading to trailing side — so it generally works well to place the most important items near the top and leading side of the window or display. Reading order varies by language; standard system components can adapt their arrangement to right-to-left languages automatically, so prefer them where you can. For guidance, see [Right to left](https://developer.apple.com/design/human-interface-guidelines/right-to-left).

**Align elements to make them easier to scan, and use indentation to convey hierarchy.** Alignment makes an app look neat and organized and can help people track content while scrolling or moving their eyes. People read aligned items as related and indented items as subordinate to the item above them, so deliberate alignment and indentation help people understand your information hierarchy.

**Group related items to show which information or functions belong together.** For example, you might use negative space, container shapes, or separator lines to show which elements are related and which are unrelated.

**Use progressive disclosure to keep layouts clean and easy to use.** Too much content and too many choices make it harder to find information and to understand what's available. Reduce what you show at first with disclosure triangles, menus, or nested views, or use scrollable sections to present additional content, which works especially well in media apps for video, music, or books.

**Differentiate controls from content.** On platforms that support Liquid Glass, use the material to give your controls a distinct appearance. Instead of placing a solid or semi-opaque background color beneath controls, use a scroll edge effect to lift the controls visually above the content. For guidance, see [Scroll views](https://developer.apple.com/design/human-interface-guidelines/scroll-views). For developer guidance, see ScrollEdgeEffectStyle, which offers two styles:

- The [soft style](https://developer.apple.com/documentation/swiftui/scrolledgeeffectstyle/soft) creates a subtle, blurred boundary between pinned controls and scrolling content.
- The [hard style](https://developer.apple.com/documentation/swiftui/scrolledgeeffectstyle/hard) creates a linear, nearly opaque boundary. Choose the effect for the content and controls involved rather than treating either style as exclusive to one platform.

Extend full-screen background content beneath sidebars, toolbars, and tab bars so it fills the entire screen or window. If scaling a background image to the window edge would leave important parts of it covered by a sidebar or inspector, use a background extension effect, which mirrors and blurs the image beneath the adjacent components so the background appears to continue under them. For developer guidance, see backgroundExtensionEffect() and UIBackgroundExtensionView.

### Adaptability

Apps and games need to adapt to different display sizes, orientation changes, window sizes, and multitasking states. In iOS, iPadOS, tvOS, and visionOS, the system defines characteristics of the device environment that can affect the way your app or game looks. Use SwiftUI or Auto Layout so your interface adapts to them.

These are the most common device and system characteristics apps need to handle:

- Regular and compact horizontal and vertical size classes
- Different device screen sizes
- Different device orientations and aspect ratios
- System features like the Dynamic Island
- External display support, Display Zoom, and resizable windows on iPad and Mac
- Text-size changes
- Locale-based internationalization features like left-to-right/right-to-left layout direction, date/time/number formatting, font variation, and text length

**Design a layout that adapts gracefully and consistently.** People expect your experience to remain familiar when they rotate their device, resize a window, add another display, or switch to a different device. You can help ensure an adaptable interface by respecting system-defined safe areas, margins, and guides (where available) and specifying layout modifiers to fine-tune the placement of views in your interface.

An app locked to one orientation, such as a landscape-only game, still needs an interface that resizes well across devices and window sizes.

**Be prepared for text-size changes.** People use Dynamic Type to make text larger and easier to read, and the setting applies systemwide. An app that ignores it can be hard or impossible to use for people who rely on it. Adjust your layout to fit larger text: horizontally adjacent views may need to stack vertically, and table rows and other containers may need to grow taller so text isn't cropped and doesn't overlap other content, including rows that show a single line of text at the default size.

To support Dynamic Type in your Unity-based game, use Apple's accessibility plug-in (for developer guidance, see Apple – Accessibility). For guidance on displaying text in your app, see Typography.

**Preview your app on multiple devices, using different size classes, localizations, and text sizes.** Test the largest and smallest layouts first to streamline the process. You can use a simulated device in Device Hub to check for clipping and other layout problems, for example to confirm that your layout holds up when people resize your app on iPad or use it through iPhone Mirroring on Mac.

**When necessary, scale background artwork in response to display changes.** For example, viewing your app or game in a different context — such as on a screen with a different aspect ratio — might make your artwork appear cropped, letterboxed, or pillarboxed. If this happens, don't change the aspect ratio of the artwork; instead, scale it so that it fills the screen. Windows can be very wide and short or tall and narrow, so background artwork often needs to extend beyond what a standard display aspect ratio would show.

#### Size classes

In iOS and iPadOS, size classes indicate how much horizontal and vertical space is available to an app's interface. Each dimension has one of two size classes, compact or regular: the horizontal size class says whether the app is narrow (compact) or wide (regular), and the vertical size class says whether it is short (compact) or tall (regular).

The system sets size classes from the device type, the window configuration, and the multitasking state, such as whether an app is full screen, in Slide Over, or mirrored from iPhone to Mac. Depending on their environment, iOS and iPadOS apps can appear in every combination of size classes. For developer guidance, see UITraitChangeObservable and UserInterfaceSizeClass.

**Base layout decisions on size classes, not on device type or orientation.** Size classes describe the space actually available, whether the app is in portrait or landscape. A device's orientation and its type (its idiom) don't tell your app how much space it has. Size classes also let your interface adapt to a wide range of window sizes; for example, people can freely resize the width and height of an iPhone app in iPhone Mirroring on Mac, and can resize an iPad app when multitasking in iPadOS or running it in macOS.

**Consider every combination of size classes.** Your app can appear in many size-class combinations in both portrait and landscape aspect ratios. A layout designed only for landscape iPhone (regular width, compact height) might waste the vertical space available when someone resizes the window to regular height on iPad in landscape; a layout designed only for compact portrait could leave empty space when someone widens the window to regular width on iPad.

**Keep functionality the same as size classes change, and keep layout changes recognizable and familiar to the platform.** Don't change what your app can do based on the space it occupies, though you can change how much of that functionality is visible. In larger spaces, consider switching from a tab bar to a sidebar or exposing functions that might otherwise sit in an overflow menu. An app's size classes can change when someone resizes it, but its idiom, the device type it's made for, stays the same, so keep the layout familiar to that platform while it resizes.

### Guides and safe areas

A layout guide defines a rectangular region that helps you position, align, and space your content on the screen. The system includes predefined layout guides that make it easy to apply standard margins around content and restrict the width of text for optimal readability. You can also define custom layout guides. For developer guidance, see UILayoutGuide and NSLayoutGuide.

A safe area defines the part of a window that isn't covered at its edges by a hardware feature or by another view in the window, like a toolbar, tab bar, or status bar. Respect the safe area so that system UI and hardware features like the Dynamic Island don't obstruct your content and controls. For developer guidance, see SafeAreaRegions and Positioning content relative to the safe area.

For templates that include the guides and safe areas for each platform, see Apple Design Resources.

### Platform considerations

No additional considerations for iOS or iPadOS.

**macOS**

**Avoid placing controls or critical information at the bottom of a window.** People often move windows so that the bottom edge is below the bottom of the screen.

**Avoid displaying content behind the camera housing at the top edge of the window.** For developer guidance, see NSPrefersDisplaySafeAreaCompatibilityMode.

**tvOS**

**Adhere to the screen's safe area.** Inset primary content 60 points from the top and bottom of the screen, and 80 points from the sides. These margins keep content visible regardless of the TV's compatibility settings or overscan cropping.

**Include appropriate padding between focusable elements.** When you use UIKit and the focus APIs, an element gets bigger when it comes into focus. Consider how elements look when they're focused, and make sure you don't let them overlap important information. For developer guidance, see About focus interactions for Apple TV.

#### Grids

The following grid layouts provide an optimal viewing experience. Be sure to use appropriate spacing between unfocused rows and columns to prevent overlap when an item comes into focus.

If you use the UIKit collection view flow element, the number of columns in a grid is automatically determined based on the width and spacing of your content. For developer guidance, see UICollectionViewFlowLayout.

| Columns | Unfocused content width | Horizontal spacing | Minimum vertical spacing |
|---------|-------------------------|--------------------|--------------------------|
| 2 | 860 pt | 40 pt | 100 pt |
| 3 | 560 pt | 40 pt | 100 pt |
| 4 | 410 pt | 40 pt | 100 pt |
| 5 | 320 pt | 40 pt | 100 pt |
| 6 | 260 pt | 40 pt | 100 pt |
| 7 | 217 pt | 40 pt | 100 pt |
| 8 | 184 pt | 40 pt | 100 pt |
| 9 | 160 pt | 40 pt | 100 pt |

**Include additional vertical spacing for titled rows.** If a row has a title, provide enough spacing between the bottom of the previous unfocused row and the center of the title to avoid crowding. Also provide spacing between the bottom of the title and the top of the unfocused items in the row.

**Use consistent spacing.** When content isn't consistently spaced, it no longer looks like a grid and it's harder for people to scan.

**Make partially hidden content look symmetrical.** To help direct attention to the fully visible content, keep partially hidden offscreen content the same width on each side of the screen.

**visionOS**

In visionOS, you can lay out content in a window, in a bounded 3D volume, or in an immersive space. The guidance below covers content in a window or volume. For guidance on displaying content spatially and on using depth, scale, and positioning, see Spatial layout. To learn more about windows and volumes in visionOS, see Windows > visionOS.

**In general, support resizing.** People expect to resize windows and volumes in visionOS, as they do in macOS and iPadOS. Make sure your layout adapts as the size changes, and at very large sizes keep content horizontally centered so people can view and interact with it easily.

You can set minimum and maximum sizes for windows, volumes, and attached elements like ornaments to keep elements from overlapping at small sizes and to keep large layouts manageable, but don't use these limits to prevent resizing. For example, Safari lets people resize browser windows while its custom navigation bar ornament has a fixed maximum size, so its controls stay easy to reach. For developer guidance, see Positioning and sizing windows.

**Use 3D content sparingly in windows.** A visionOS window can show 3D content at a fixed depth; reserve it for meaningful moments alongside 2D content, such as an inline 3D model of a rocket next to information about it in an educational app. Inset inline 3D content within the window so it doesn't collide with other content or controls or appear unpredictably past the window's edge. For larger models or views made mostly of 3D content, consider a volume or an immersive space.

**Display supplemental content in an adjacent window, not in an ornament.** Ornaments are best for app-specific interactive controls, like toolbars and video playback controls, not for supplemental content. To show a supplemental view, open a new window next to the current one with defaultWindowPlacement(_:). For guidance, see Ornaments. For developer guidance, see Positioning and sizing windows.

**Include enough space around controls for them to be easy to interact with.** Space around a control makes it clearly identifiable and keeps the system-provided hover effect from obscuring other content. For example, place buttons so their centers are at least 60 points apart. For guidance, see Eyes, Spatial layout, and Buttons > visionOS.

**watchOS**

**Avoid placing more than two or three controls side by side in your interface.** As a general rule, display no more than three buttons that contain glyphs — or two buttons that contain text — in a row. Although it's usually better to let text buttons span the full width of the screen, two side-by-side buttons with short text labels can also work well, as long as the screen doesn't scroll.

**Support autorotation in views people might want to show others.** When people flip their wrist away, apps typically respond to the motion by sleeping the display, but in some cases it makes sense to autorotate the content. For example, a wearer might want to show an image to a friend or display a QR code to a reader. For developer guidance, see isAutorotating.

### Specifications

Apple removed the device specification tables from the Layout article in its September 9, 2026 update, and the current article directs you to base layout on size classes rather than device type. The tables below are retained for reference. Each row matches the last version of the article that included them (change-log entry September 9, 2025); they list selected devices, not every model.

#### iOS, iPadOS device screen dimensions

| Model | Dimensions (portrait) |
|-------|----------------------|
| iPad Pro 12.9-inch | 1024x1366 pt (2048x2732 px @2x) |
| iPad Pro 13-inch | 1032x1376 pt (2064x2752 px @2x) |
| iPad Pro 11-inch, 5th and 6th generations | 834x1210 pt (1668x2420 px @2x) |
| iPad Pro 11-inch, 1st–4th generations | 834x1194 pt (1668x2388 px @2x) |
| iPad Pro 10.5-inch | 834x1112 pt (1668x2224 px @2x) |
| iPad Pro 9.7-inch | 768x1024 pt (1536x2048 px @2x) |
| iPad Air 13-inch | 1024x1366 pt (2048x2732 px @2x) |
| iPad Air 11-inch | 820x1180 pt (1640x2360 px @2x) |
| iPad Air 10.9-inch | 820x1180 pt (1640x2360 px @2x) |
| iPad Air 10.5-inch | 834x1112 pt (1668x2224 px @2x) |
| iPad Air 9.7-inch | 768x1024 pt (1536x2048 px @2x) |
| iPad 11-inch | 820x1180 pt (1640x2360 px @2x) |
| iPad 10.2-inch | 810x1080 pt (1620x2160 px @2x) |
| iPad 9.7-inch | 768x1024 pt (1536x2048 px @2x) |
| iPad mini 8.3-inch | 744x1133 pt (1488x2266 px @2x) |
| iPad mini 7.9-inch | 768x1024 pt (1536x2048 px @2x) |
| iPhone 17 Pro Max | 440x956 pt (1320x2868 px @3x) |
| iPhone 17 Pro | 402x874 pt (1206x2622 px @3x) |
| iPhone Air | 420x912 pt (1260x2736 px @3x) |
| iPhone 17 | 402x874 pt (1206x2622 px @3x) |
| iPhone 16 Pro Max | 440x956 pt (1320x2868 px @3x) |
| iPhone 16 Pro | 402x874 pt (1206x2622 px @3x) |
| iPhone 16 Plus | 430x932 pt (1290x2796 px @3x) |
| iPhone 16 | 393x852 pt (1179x2556 px @3x) |
| iPhone 16e | 390x844 pt (1170x2532 px @3x) |
| iPhone 15 Pro Max | 430x932 pt (1290x2796 px @3x) |
| iPhone 15 Pro | 393x852 pt (1179x2556 px @3x) |
| iPhone 15 Plus | 430x932 pt (1290x2796 px @3x) |
| iPhone 15 | 393x852 pt (1179x2556 px @3x) |

**Note:** All scale factors in the table above are UIKit scale factors, which may differ from native scale factors. For developer guidance, see scale and nativeScale.

#### iOS, iPadOS device size classes

These are the size classes each device has when an app runs full screen. Windowed and multitasking configurations can produce other combinations, so check the current size classes at run time rather than inferring them from the model. For developer guidance, see UserInterfaceSizeClass.

| Model | Portrait orientation | Landscape orientation |
|-------|---------------------|----------------------|
| iPad Pro 12.9-inch | Regular width, regular height | Regular width, regular height |
| iPad Pro 11-inch | Regular width, regular height | Regular width, regular height |
| iPad Pro 10.5-inch | Regular width, regular height | Regular width, regular height |
| iPad Air 13-inch | Regular width, regular height | Regular width, regular height |
| iPad Air 11-inch | Regular width, regular height | Regular width, regular height |
| iPad 11-inch | Regular width, regular height | Regular width, regular height |
| iPad 9.7-inch | Regular width, regular height | Regular width, regular height |
| iPad mini 7.9-inch | Regular width, regular height | Regular width, regular height |
| iPhone 17 Pro Max | Compact width, regular height | Regular width, compact height |
| iPhone 17 Pro | Compact width, regular height | Compact width, compact height |
| iPhone Air | Compact width, regular height | Regular width, compact height |
| iPhone 17 | Compact width, regular height | Compact width, compact height |
| iPhone 16 Pro Max | Compact width, regular height | Regular width, compact height |
| iPhone 16 Pro | Compact width, regular height | Compact width, compact height |
| iPhone 16 Plus | Compact width, regular height | Regular width, compact height |
| iPhone 16 | Compact width, regular height | Compact width, compact height |
| iPhone 16e | Compact width, regular height | Compact width, compact height |

#### watchOS device screen dimensions

| Series | Size | Width (pixels) | Height (pixels) |
|--------|------|----------------|-----------------|
| 10 and 11 | 42mm | 374 | 446 |
| 10 and 11 | 46mm | 416 | 496 |
| Apple Watch Ultra (3rd generation) | 49mm | 422 | 514 |
| Apple Watch Ultra (1st and 2nd generations) | 49mm | 410 | 502 |
| 7, 8, and 9 | 41mm | 352 | 430 |
| 7, 8, and 9 | 45mm | 396 | 484 |
| 4, 5, 6, and SE (all generations) | 40mm | 324 | 394 |
| 4, 5, 6, and SE (all generations) | 44mm | 368 | 448 |
| 1, 2, and 3 | 38mm | 272 | 340 |
| 1, 2, and 3 | 42mm | 312 | 390 |

### Resources

#### Related

- [Right to left](https://developer.apple.com/design/human-interface-guidelines/right-to-left)
- [Spatial layout](https://developer.apple.com/design/human-interface-guidelines/spatial-layout)
- [Layout and organization](https://developer.apple.com/design/human-interface-guidelines/layout-and-organization)

#### Developer documentation

- [Composing custom layouts with SwiftUI](https://developer.apple.com/documentation/swiftui/composing-custom-layouts-with-swiftui) — SwiftUI

#### Videos

- [Get to know the new design system](https://developer.apple.com/videos/play/wwdc2025/356)
- [Compose custom layouts with SwiftUI](https://developer.apple.com/videos/play/wwdc2022/10056/)
- [Essential Design Principles](https://developer.apple.com/videos/play/wwdc2017/802/)

## Changelog

### September 9, 2026
- Updated guidance to reflect current best practices.

### September 9, 2025
- Added specifications for iPhone 17, iPhone Air, iPhone 17 Pro, iPhone 17 Pro Max, Apple Watch SE 3, Apple Watch Series 11, and Apple Watch Ultra 3.

### June 9, 2025
- Added guidance for Liquid Glass.

### March 7, 2025
- Added specifications for iPhone 16e, iPad 11-inch, iPad Air 11-inch, and iPad Air 13-inch.

### September 9, 2024
- Added specifications for iPhone 16, iPhone 16 Plus, iPhone 16 Pro, iPhone 16 Pro Max, and Apple Watch Series 10.

### June 10, 2024
- Made minor corrections and organizational updates.

### February 2, 2024
- Enhanced guidance for avoiding system controls in iPadOS app layouts, and added specifications for 10.9-inch iPad Air and 8.3-inch iPad mini.

### December 5, 2023
- Clarified guidance on centering content in a visionOS window.

### September 15, 2023
- Added specifications for iPhone 15 Pro Max, iPhone 15 Pro, iPhone 15 Plus, iPhone 15, Apple Watch Ultra 2, and Apple Watch SE.

### June 21, 2023
- Updated to include guidance for visionOS.

### September 14, 2022
- Added specifications for iPhone 14 Pro Max, iPhone 14 Pro, iPhone 14 Plus, iPhone 14, and Apple Watch Ultra.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/layout)*
