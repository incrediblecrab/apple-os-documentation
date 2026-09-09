# Going full screen

iPhone, iPad, and Mac offer full-screen modes that let people expand a window to fill the screen, hiding system controls and providing a distraction-free environment.

**Platforms:** iOS | iPadOS | macOS

## Overview

Apple TV and Apple Watch don't offer full-screen modes because apps and games already fill the screen by default. Apple Vision Pro doesn't offer a full-screen mode because people can expand a window to fill more of their view or use the Digital Crown to hide passthrough and transition to a more immersive experience (for guidance, see Immersive experiences).

On iPad, test entering and leaving full screen from different window sizes and supported display configurations. Preserve the current task and usable navigation; see [Designing for iPadOS](../getting-started/iPadOS.md).

## Topics

### Best practices

- **Support full-screen mode when appropriate** - People appreciate full-screen mode when they want to concentrate on a task or be immersed in content. Consider offering a full-screen mode if your experience lets people play a game; view media like videos or photo slideshows; or perform an in-depth task that benefits from a distraction-free environment.

- **Adjust layout without programmatic resizing** - If necessary, adjust your layout in full-screen mode, but don't programmatically resize your window. When a window is larger in full-screen mode than in non-full-screen mode, you want to keep essential content prominent while making good use of the extra space. For example, it might make sense to adjust the proportions of your interface without changing which items appear. If you make such adjustments, be sure they're subtle enough to maintain a consistent interface and avoid causing visually jarring transitions between modes.

- **Provide access to essential features** - Continue to provide access to essential features and controls so people can complete their task without exiting full-screen mode. For example, a full-screen media experience needs to make playback controls persistently available or easy to reveal when people need them.

- **Preserve Dock access** - Except in games, let people reveal the Dock in a full-screen iPadOS or macOS experience. For a game prone to accidental edge gestures, consider [UIHostingController's gesture-deferral property](https://developer.apple.com/documentation/swiftui/uihostingcontroller/preferredscreenedgesdeferringsystemgestures) or [UIViewController's equivalent](https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredscreenedgesdeferringsystemgestures) on iPadOS. AppKit's [hideDock](https://developer.apple.com/documentation/appkit/nsapplication/presentationoptions-swift.struct/hidedock) option entirely hides and disables the Dock on macOS.

- **Support resumption** - After people switch away from your full-screen experience, help them resume where they left off when they return. For example, a game or a slideshow needs to pause automatically when people leave the experience so they don't miss anything.

- **Let people control mode exits** - People generally don't expect full-screen mode to end automatically when they switch to a different experience or finish an absorbing activity, like playing a game or viewing a movie.

- **Temporarily hide non-essential UI** - Prioritize content by temporarily hiding toolbars and navigation controls. You can offer a distraction-free environment by hiding elements when content is the primary focus, such as when viewing full-screen photos or reading a document. If you implement such behavior, let people restore the hidden elements with a familiar gesture or action like tapping, swiping down, or moving the cursor to the top of the screen. Be sure to keep controls visible when they're essential for navigation or performing tasks. Although a visionOS window can hide its toolbars or navigation controls, people generally expect different types of immersive experiences while wearing Apple Vision Pro; for guidance, see Immersive experiences.

### Platform considerations

This window-expansion mode isn't provided in tvOS, visionOS, or watchOS. That doesn't rule out full-screen modal presentations or visionOS immersive experiences.

**iOS, iPadOS**  
Preserve familiar system gestures unless they cause accidental exits. Gesture deferral can make the first edge swipe yield to the app and require another swipe to leave; it is separate from hiding the Home indicator. UIKit's [prefersHomeIndicatorAutoHidden](https://developer.apple.com/documentation/uikit/uiviewcontroller/prefershomeindicatorautohidden) defaults to false, and even returning true is only a preference, not a guarantee of hiding. The HIG describes an auto-hiding full-screen experience, but it isn't the default behavior promised by every view controller.

**macOS**  
- Use the system-provided full-screen experience. It accommodates system layout constraints such as the camera housing on supported Mac displays. See [toggleFullScreen(_:)](https://developer.apple.com/documentation/appkit/nswindow/togglefullscreen(_:)).

- In a game, don't change the hardware display mode just because someone enters full screen. Preserve the person's display choice; rendering resolution and scaling are separate decisions. See [Managing your game window for Metal in macOS](https://developer.apple.com/documentation/metal/managing-your-game-window-for-metal-in-macos).

- Always let people choose when to enter full-screen mode. Prefer letting people use your window's Enter Full Screen button, View menu item, or the Control-Command-F keyboard shortcut. Avoid offering a custom menu of window modes. In a game, you might also provide a custom toggle that turns full-screen mode on and off.

### Related

- [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- [Multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking)
- [Windows](https://developer.apple.com/design/human-interface-guidelines/windows)
- [The menu bar](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar)

### Developer documentation

- [fullScreenCover(item:onDismiss:content:) — SwiftUI](https://developer.apple.com/documentation/swiftui/view/fullscreencover(item:ondismiss:content:))
- [NSScreen — AppKit](https://developer.apple.com/documentation/appkit/nsscreen)
- [NSWindow.CollectionBehavior — AppKit](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior-swift.struct)
- [Managing your game window for Metal in macOS](https://developer.apple.com/documentation/metal/managing-your-game-window-for-metal-in-macos)

### Videos

- [Elevate the design of your iPad app](https://developer.apple.com/videos/play/wwdc2025/208)

## Changelog

These dates describe changes to Apple's HIG article, not edits to this repository.

### June 9, 2025
- Updated guidance for hiding toolbars and navigation controls, and deferring Home Screen indicator gestures in full-screen iOS and iPadOS apps and games.

### June 10, 2024
- Enhanced guidance for playing a game in full-screen mode.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/going-full-screen)*
