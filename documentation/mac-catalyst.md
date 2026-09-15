# Mac Catalyst

Create a version of your iPad app that users can run on a Mac device.

## Overview
With Mac Catalyst, you can make a Mac version of your iPad app. Add the Mac Catalyst destination to your iPad app's target settings to configure the project for both platforms. The two apps share the same project and source code, making it easy to change your code in one place.

For Mac window, menu, and input conventions, see [Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos).

Important

Mac apps built with Mac Catalyst can only use AppKit APIs marked as available in Mac Catalyst, such as NSToolbar and NSTouchBar. Mac Catalyst doesn’t support accessing unavailable AppKit APIs.

## OS26 and OS27 Planning

**Checked September 8, 2026:** macOS Tahoe **26.6.2** (August 17) is the last 26-generation release; macOS 27 Golden Gate **27.0** shipped September 14. Keep the older Catalyst guidance below when supporting earlier deployment targets.

- **Scenes are required:** on Mac Catalyst 27, apps built with the latest SDK must use the UIKit scene-based life cycle or fail to launch. Move UI state, activation, and restoration to the relevant scene; multiple-window support remains optional. See [scene migration](https://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle).
- **Reopen behavior changes:** switching to a Catalyst app with no open windows no longer automatically creates a window unless activation is through Dock or Spotlight. Test document and reopen commands.
- **Menu images:** review `UIMenuElement.preferredImageVisibility` for menu-bar/context-menu images rather than depending on every supplied image being shown.
- **Appearance:** [`UIDesignRequiresCompatibility`](https://developer.apple.com/documentation/bundleresources/information-property-list/uidesignrequirescompatibility) is ignored for Mac Catalyst 27 builds. Re-test custom toolbars and title-bar content.
- **Resolved is not unsupported:** the 27.0 notes list the earlier Mac-idiom `UIStepper` failure as fixed. Keep it as a regression test, not a permanent Catalyst exclusion.

Sources: [macOS 27 notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes) and [iOS/iPadOS 27 UIKit notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes).

**Xcode 27** (`27A266a`, September 14) requires **Apple silicon and macOS Tahoe 26.6 or later**, not macOS 27. Intel app translation through Rosetta does not imply Intel-host support. Check the [Xcode notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes) separately from your app's deployment target and [distribution requirements](../guides/app-store-readiness.md).

## Topics

### Essentials
- [Creating a Mac version of your iPad app](https://developer.apple.com/documentation/UIKit/creating-a-mac-version-of-your-ipad-app) - Bring your iPad app to macOS with Mac Catalyst.
### App support
- [Bring an iPad App to the Mac with Mac Catalyst](https://developer.apple.com/tutorials/mac-catalyst) - Build a native Mac app from the same codebase as your iPad app.
- [Choosing a user interface idiom for your Mac app](https://developer.apple.com/documentation/UIKit/choosing-a-user-interface-idiom-for-your-mac-app) - Select the iPad or the Mac user interface idiom in your Mac app built with Mac Catalyst.
- [Optimizing your iPad app for Mac](https://developer.apple.com/documentation/UIKit/optimizing-your-ipad-app-for-mac) - Make your iPad app more like a Mac app by taking advantage of system features in macOS.
- [LSMinimumSystemVersion](https://developer.apple.com/documentation/bundleresources/information-property-list/lsminimumsystemversion) - The minimum version of the operating system required for the app to run in macOS.
- [UIApplicationSupportsTabbedSceneCollection](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportstabbedscenecollection) - A Boolean value indicating whether an app built with Mac Catalyst supports automatic tabbing mode.
### User interface
- [UIKit Catalog: Creating and customizing views and controls](https://developer.apple.com/documentation/UIKit/uikit-catalog-creating-and-customizing-views-and-controls) - Customize your app's user interface with views and controls.
- [Building and improving your app with Mac Catalyst](https://developer.apple.com/documentation/UIKit/building-and-improving-your-app-with-mac-catalyst) - Improve your iPadOS app with Mac Catalyst by supporting native controls, multiple windows, sharing, printing, menus and keyboard shortcuts.
- [Displaying a checkbox in your Mac app built with Mac Catalyst](https://developer.apple.com/documentation/UIKit/displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst) - Present a switch control as a Mac-style checkbox when your app runs in the Mac user interface idiom.
- [Removing the title bar in your Mac app built with Mac Catalyst](https://developer.apple.com/documentation/UIKit/removing-the-title-bar-in-your-mac-app-built-with-mac-catalyst) - Display content that fills the entire height of a window by removing the title bar.
- [Toolbar](https://developer.apple.com/documentation/uikit/toolbar) - Provide a space for controls under a window's title bar and above your custom content.
- [Touch Bar](https://developer.apple.com/documentation/appkit/touch-bar) - Display interactive content and controls in the Touch Bar.
### User interactions
- [Navigating an app's user interface using a keyboard](https://developer.apple.com/documentation/uikit/navigating-an-app-s-user-interface-using-a-keyboard) - Navigate between user interface elements using a keyboard and focusable UI elements in iPad apps and apps built with Mac Catalyst.
- [Adding menus and shortcuts to the menu bar and user interface](https://developer.apple.com/documentation/UIKit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface) - Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [Handling key presses made on a physical keyboard](https://developer.apple.com/documentation/UIKit/handling-key-presses-made-on-a-physical-keyboard) - Detect when someone presses and releases keys on a physical keyboard.
- [UIHoverGestureRecognizer](https://developer.apple.com/documentation/uikit/uihovergesturerecognizer) - A continuous gesture recognizer that interprets pointer movement over a view.
### User preferences
- [Displaying a Settings window](https://developer.apple.com/documentation/uikit/displaying-a-settings-window) - Expose preferences from your Settings bundle in a Mac Catalyst settings window.
- [Detecting changes in the preferences window](https://developer.apple.com/documentation/UIKit/detecting-changes-in-the-preferences-window) - Listen for and respond to a user's preference changes in your Mac app built with Mac Catalyst using Combine.
### Tooltips
- [Showing help tags for views and controls using tooltip interactions](https://developer.apple.com/documentation/UIKit/showing-help-tags-for-views-and-controls-using-tooltip-interactions) - Explain the purpose of interface elements by showing a tooltip when a person positions the pointer over the element.
- [UIToolTipInteraction](https://developer.apple.com/documentation/uikit/uitooltipinteraction) - An interaction object that makes it possible to show a tooltip when hovering a pointer over a view or control.
- [UIToolTipInteractionDelegate](https://developer.apple.com/documentation/uikit/uitooltipinteractiondelegate) - An interface that provides tooltip settings to an interaction.
## See Also

### App structure
- [App and environment](https://developer.apple.com/documentation/uikit/app-and-environment) - Manage life-cycle events and your app's UI scenes, and get information about traits and the environment in which your app runs.
- [Documents, data, and pasteboard](https://developer.apple.com/documentation/uikit/documents-data-and-pasteboard) - Organize your app's data and share that data on the pasteboard.
- [Resource management](https://developer.apple.com/documentation/uikit/resource-management) - Manage the images, strings, storyboards, and nib files that you use to implement your app's interface.
- [App extensions](https://developer.apple.com/documentation/uikit/app-extensions) - Extend your app's basic functionality to other parts of the system.
- [Interprocess communication](https://developer.apple.com/documentation/uikit/interprocess-communication) - Display activity-based services to people.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/UIKit/mac-catalyst)*
