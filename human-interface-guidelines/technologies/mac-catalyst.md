# Mac Catalyst

When you use Mac Catalyst to create a Mac version of your iPad app, you give people the opportunity to enjoy the experience in a new environment.

**Platforms:** iPadOS | macOS

## Overview

**Developer note**  
To discover how views and controls can change when you create a Mac app using Mac Catalyst, download UIKit Catalog: Creating and customizing views and controls and build the macOS target.

## Topics

### Before You Start

Many iPad apps are great candidates for creating a Mac app built with Mac Catalyst. This is especially true for apps that already work well on iPad and support key iPad features, such as:

- **Drag and drop** - When you support drag and drop in your iPad app, you also get support for drag and drop in the Mac version.
- **Keyboard navigation and shortcuts** - Even though a physical keyboard may not always be available on iPad, iPad users appreciate using the keyboard to navigate and keyboard shortcuts to streamline their interactions. On the Mac, people expect apps to offer both keyboard navigation and shortcuts.
- **Multitasking** - Apps that do a good job scaling the interface to support Split View, Slide Over, and Picture in Picture lay the necessary groundwork to support the extensive window resizability that Mac users expect.
- **Multiple windows** - By supporting multiple scenes on iPad, you also get support for multiple windows in the macOS version of your app.

Although great iPad apps can provide a solid foundation for creating a Mac app built with Mac Catalyst, some apps rely on frameworks or features that don't exist on a Mac. For example, if the essential features of your experience require capabilities like gyroscope, accelerometer, or rear camera, frameworks like HealthKit or ARKit, or if the primary function you offer is something like marking, handwriting, or navigation, your app might not be suitable for the Mac.

Creating a Mac version of your iPad app with Mac Catalyst gives the app automatic support for fundamental macOS features such as:

- Pointer interactions and keyboard-based focus and navigation
- Window management
- Toolbars
- Rich text interaction, including copy and paste as well as contextual menus for editing
- File management
- Menu bar menus
- App-specific settings in the system-provided Settings app

System-provided UI elements take on a more Mac-like appearance, too; for example:

- Split view
- File browser
- Activity view
- Form sheet
- Contextual actions
- Color picker

### Choose an Idiom

When you first create your Mac app using Mac Catalyst, Xcode defaults to the "Scale Interface to Match iPad" setting, or iPad idiom. With this setting, the system ensures that your Mac app appears consistent with the macOS display environment without requiring significant changes to the app's layout. However, text and graphics may appear slightly less detailed because iPadOS views and text scale down to 77% in macOS when you use the iPad idiom.

When your app feels at home on the Mac using the iPad idiom, consider switching to the Mac idiom. With this setting, text and artwork render in more detail, some interface elements and views take on an even more Mac-like appearance, and graphics-intensive apps may see improved performance and lower power consumption.

**Developer note**  
When you adopt the Mac idiom, the unscaled views and interface elements report different metrics, often resulting in a significant amount of additional work. To reduce the amount of work, avoid using fixed font, view, or layout sizes. For developer guidance, see Choosing a user interface idiom for your Mac app.

### Best Practices

- **Adjust font sizes as needed** - With the Mac idiom, text renders at 100% of its configured size, which can appear too large without adjustment. When possible, use text styles and avoid fixed font sizes.

- **Make sure views and images look good in the Mac version of your app** - With the Mac idiom, iPadOS views render at 100% of their size, making them appear more detailed.

- **Limit your appearance customizations** - Limit your appearance customizations to standard macOS appearance customizations that are the same or similar to those available in iPadOS. Not all appearance customizations available to iPadOS controls are available to macOS controls.

### Integrate the Mac Experience

When you use Mac Catalyst to create a Mac version of your iPad app, you need to ensure that your Mac app gives people a rich Mac experience. Regardless of the idiom you choose, it's essential to go beyond simply displaying your iPadOS layout in a macOS window.

#### Navigation

- **Consider using a split view with a sidebar instead of a tab bar** - A split view displays a list of top-level items, each of which can disclose a list of child items. Using a sidebar streamlines navigation and creates a consistent layout that makes it easy for iPad users to start using the Mac version of your app.

- **Make sure people retain access to important tab-bar items** - Give people quick access to top-level items by listing them in the macOS View menu.

- **Offer multiple ways to move between pages** - Mac users appreciate Next and Previous buttons in addition to iPad or trackpad gestures that let them swipe between pages.

#### Layout

- **Divide a single column of content and actions into multiple columns**
- **Use regular-width and regular-height size classes** - Consider reflowing elements in the content area to a side-by-side arrangement as people resize the window.
- **Present an inspector UI next to the main content** - Instead of using a popover.
- **Consider moving controls to your Mac app's toolbar** - Move controls from the main UI of your iPad app to your Mac app's toolbar. Be sure to list the commands associated with these controls in the menus of your Mac app's menu bar.
- **Adopt a top-down flow** - Mac apps place the most important actions and content near the top of the window.
- **Relocate buttons from the side and bottom edges** - On iPad, placing buttons on these screen edges can help people reach them, but on a Mac, this ergonomic consideration doesn't apply.

#### Menus

Mac users are familiar with the persistent menu bar and expect to find all of an app's commands in it. The system automatically converts the context menus in your iPad app to context menus in the macOS version of your app. Consider looking for additional places to support context menus, as Mac users tend to expect every object in your app to offer a context menu of relevant actions.

**Developer note**  
To support keyboard shortcuts for menu commands, use UIKeyCommand. To add and remove custom app menus, use UIMenuBuilder and add menu items that represent your iPad app's commands as menu items with UICommand.

### Related Technologies

- [Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos) - Platform-specific design guidelines

### Developer Documentation

- [Mac Catalyst](https://developer.apple.com/documentation/uikit/mac_catalyst) - UIKit

## Changelog

### May 2, 2023
- Consolidated guidance into one page.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/mac-catalyst)*