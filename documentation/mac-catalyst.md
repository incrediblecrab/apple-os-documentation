# Mac Catalyst

Create a version of your iPad app that users can run on a Mac device.

## Overview
With Mac Catalyst, you can make a Mac version of your iPad app. Click the Mac checkbox in your iPad app’s project settings to configure the project to build both Mac and iPad versions of your app. The two apps share the same project and source code, making it easy to change your code in one place.

For information about designing a Mac version of your iPad app, see Mac Catalyst in the Human Interface Guidelines.

Important

Mac apps built with Mac Catalyst can only use AppKit APIs marked as available in Mac Catalyst, such as NSToolbar and NSTouchBar. Mac Catalyst doesn’t support accessing unavailable AppKit APIs.

## Topics

### Essentials
- [Creating a Mac version of your iPad app](https://developer.apple.com/documentation/uikit/mac_catalyst/creating_a_mac_version_of_your_ipad_app) - Bring your iPad app to macOS with Mac Catalyst.
### App support
- [Bring an iPad App to the Mac with Mac Catalyst](https://developer.apple.com/documentation/uikit/mac_catalyst/bring_an_ipad_app_to_the_mac_with_mac_catalyst) - Build a native Mac app from the same codebase as your iPad app.
- [Choosing a user interface idiom for your Mac app](https://developer.apple.com/documentation/uikit/mac_catalyst/choosing_a_user_interface_idiom_for_your_mac_app) - Select the iPad or the Mac user interface idiom in your Mac app built with Mac Catalyst.
- [Optimizing your iPad app for Mac](https://developer.apple.com/documentation/uikit/mac_catalyst/optimizing_your_ipad_app_for_mac) - Make your iPad app more like a Mac app by taking advantage of system features in macOS.
- **LSMinimumSystemVersion** - The minimum version of the operating system required for the app to run in macOS.
- **UIApplicationSupportsTabbedSceneCollection** - A Boolean value indicating whether an app built with Mac Catalyst supports automatic tabbing mode.
### User interface
- [UIKit Catalog: Creating and customizing views and controls](https://developer.apple.com/documentation/uikit/mac_catalyst/uikit_catalog_creating_and_customizing_views_and_controls) - Customize your app's user interface with views and controls.
- [Building and improving your app with Mac Catalyst](https://developer.apple.com/documentation/uikit/mac_catalyst/building_and_improving_your_app_with_mac_catalyst) - Improve your iPadOS app with Mac Catalyst by supporting native controls, multiple windows, sharing, printing, menus and keyboard shortcuts.
- [Displaying a checkbox in your Mac app built with Mac Catalyst](https://developer.apple.com/documentation/uikit/mac_catalyst/displaying_a_checkbox_in_your_mac_app_built_with_mac_catalyst) - Present a switch control as a Mac-style checkbox when your app runs in the Mac user interface idiom.
- [Removing the title bar in your Mac app built with Mac Catalyst](https://developer.apple.com/documentation/uikit/mac_catalyst/removing_the_title_bar_in_your_mac_app_built_with_mac_catalyst) - Display content that fills the entire height of a window by removing the title bar.
- **Toolbar** - Provide a space for controls under a window's title bar and above your custom content.
- **Touch Bar** - Display interactive content and controls in the Touch Bar.
### User interactions
- [Navigating an app's user interface using a keyboard](https://developer.apple.com/documentation/uikit/mac_catalyst/navigating_an_app_s_user_interface_using_a_keyboard) - Navigate between user interface elements using a keyboard and focusable UI elements in iPad apps and apps built with Mac Catalyst.
- [Adding menus and shortcuts to the menu bar and user interface](https://developer.apple.com/documentation/uikit/mac_catalyst/adding_menus_and_shortcuts_to_the_menu_bar_and_user_interface) - Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [Handling key presses made on a physical keyboard](https://developer.apple.com/documentation/uikit/mac_catalyst/handling_key_presses_made_on_a_physical_keyboard) - Detect when someone presses and releases keys on a physical keyboard.
- **UIHoverGestureRecognizer** - A continuous gesture recognizer that interprets pointer movement over a view.
### User preferences
- [Displaying a Preferences window](https://developer.apple.com/documentation/uikit/mac_catalyst/displaying_a_preferences_window) - Provide a Preferences window in your Mac app built with Mac Catalyst so users can manage app preferences defined in a Settings bundle.
- [Detecting changes in the preferences window](https://developer.apple.com/documentation/uikit/mac_catalyst/detecting_changes_in_the_preferences_window) - Listen for and respond to a user's preference changes in your Mac app built with Mac Catalyst using Combine.
### Tooltips
- [Showing help tags for views and controls using tooltip interactions](https://developer.apple.com/documentation/uikit/mac_catalyst/showing_help_tags_for_views_and_controls_using_tooltip_interactions) - Explain the purpose of interface elements by showing a tooltip when a person positions the pointer over the element.
- **UIToolTipInteraction** - An interaction object that makes it possible to show a tooltip when hovering a pointer over a view or control.
- **UIToolTipInteractionDelegate** - An interface that provides tooltip settings to an interaction.
## See Also

### App structure
- **App and environment** - Manage life-cycle events and your app's UI scenes, and get information about traits and the environment in which your app runs.
- **Documents, data, and pasteboard** - Organize your app's data and share that data on the pasteboard.
- **Resource management** - Manage the images, strings, storyboards, and nib files that you use to implement your app's interface.
- **App extensions** - Extend your app's basic functionality to other parts of the system.
- **Interprocess communication** - Display activity-based services to people.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/UIKit/mac-catalyst)*
