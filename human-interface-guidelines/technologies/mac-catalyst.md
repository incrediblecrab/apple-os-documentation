# Mac Catalyst

When you use Mac Catalyst to create a Mac version of your iPad app, you give people the opportunity to enjoy the experience in a new environment.

**Platforms:** iPadOS | macOS

## Overview

**Developer note**  
To inspect how views and controls adapt, use [UIKit Catalog: Creating and customizing views and controls](https://developer.apple.com/documentation/uikit/uikit-catalog-creating-and-customizing-views-and-controls) with a Mac Catalyst destination.

Review [Adopting Liquid Glass](../../liquid-glass/adopting-liquid-glass.md) for the compatibility key's build-target rules, including Mac Catalyst. SDK selection, the runtime OS, and the deployment target are separate concerns.

## Topics

### Before You Start

Many iPad apps are great candidates for creating a Mac app built with Mac Catalyst. This is especially true for apps that already work well on iPad and support key iPad features, such as:

- **Drag and drop** - When you support drag and drop in your iPad app, you also get support for drag and drop in the Mac version.
- **Keyboard navigation and shortcuts** - Even though a physical keyboard may not always be available on iPad, iPad users appreciate using the keyboard to navigate and keyboard shortcuts to streamline their interactions. On the Mac, people expect apps to offer both keyboard navigation and shortcuts.
- **Multitasking and resizability** - Adapt to the window sizes and multitasking modes available on iPad, with Picture in Picture where appropriate. Flexible layout is useful preparation for Mac window resizing; older Split View and Slide Over terminology isn't a complete description of current iPad windowing.
- **Multiple windows** - By supporting multiple scenes on iPad, you also get support for multiple windows in the macOS version of your app.

Check required hardware, framework availability, and actual runtime capability separately. A sensor-dependent or camera-based experience may need a different Mac design, and handwriting or navigation may not translate naturally to desktop input. Don't infer capability merely because code links: HealthKit, for example, is present on macOS 13 and later, but its documentation says apps there can't read or write HealthKit data and `isHealthDataAvailable()` returns false.

Mac Catalyst adapts standard UIKit behavior and supplies integration points for fundamental macOS features. Review and configure the parts your app actually uses:

- Pointer interactions and keyboard-based focus and navigation
- Window management
- Toolbars
- Rich text interaction, including copy and paste as well as contextual menus for editing
- File management
- Menu bar menus
- An app-specific Settings window when the app includes a `Settings.bundle`, available from the app menu rather than macOS System Settings

System-provided UI elements take on a more Mac-like appearance, too; for example:

- Split view
- File browser
- Activity view
- Form sheet
- Contextual actions
- Color picker

### Choose an Idiom

When you first create your Mac app using Mac Catalyst, Xcode defaults to the "Scale Interface to Match iPad" setting, or iPad idiom. With this setting, the system adapts the interface to Mac sizing while preserving iPad-like layout metrics. Text and graphics may appear less detailed because the HIG describes scaling iPad views to approximately 77% in this idiom.

When your app feels at home on the Mac using the iPad idiom, consider switching to the Mac idiom. With this setting, text and artwork render in more detail, some interface elements and views take on an even more Mac-like appearance, and graphics-intensive apps may see improved performance and lower power consumption.

**Developer note**  
When you adopt the Mac idiom, the unscaled views and interface elements report different metrics, often resulting in significant layout work. Avoid fixed font, view, and layout sizes where possible. Audit control compatibility too: the developer guide says `UIPageControl` isn't available in the Mac idiom and displaying it raises an exception. See [Choosing a user interface idiom for your Mac app](https://developer.apple.com/documentation/uikit/choosing-a-user-interface-idiom-for-your-mac-app).

### Best Practices

- **Adjust font sizes as needed** - With the Mac idiom, text renders at 100% of its configured size, which can appear too large without adjustment. When possible, use text styles and avoid fixed font sizes.

- **Make sure views and images look good in the Mac version of your app** - With the Mac idiom, iPadOS views render at 100% of their size, making them appear more detailed.

- **Limit your appearance customizations** - Limit your appearance customizations to standard macOS appearance customizations that are the same or similar to those available in iPadOS. Not all appearance customizations available to iPadOS controls are available to macOS controls.

### Integrate the Mac Experience

When you use Mac Catalyst to create a Mac version of your iPad app, you need to ensure that your Mac app gives people a rich Mac experience. Regardless of the idiom you choose, it's essential to go beyond simply displaying your iPadOS layout in a macOS window.

#### Navigation

- **Consider using a split view with a sidebar instead of a tab bar** - A split view displays a list of top-level items, each of which can disclose a list of child items. Using a sidebar streamlines navigation and creates a consistent layout that makes it easy for iPad users to start using the Mac version of your app.

- **Make sure people retain access to important tab-bar items** - Give people quick access to top-level items by listing them in the macOS View menu.

- **Offer multiple ways to move between pages** - Mac users appreciate Next and Previous buttons and keyboard access in addition to supported trackpad gestures.

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

Mac Catalyst doesn't provide unrestricted AppKit access. Use only AppKit APIs explicitly available to Mac Catalyst; native AppKit, a Catalyst build, and an unmodified iPad app running on Apple silicon are distinct environments.

### Related Technologies

- [Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos) - Platform-specific design guidelines

### Developer Documentation

- [Mac Catalyst](https://developer.apple.com/documentation/uikit/mac-catalyst) - UIKit
- [Creating a Mac version of your iPad app](https://developer.apple.com/documentation/uikit/creating-a-mac-version-of-your-ipad-app) - Supported destination and target setup
- [Displaying a Settings window](https://developer.apple.com/documentation/uikit/displaying-a-settings-window) - Settings bundle integration
- [Adding menus and shortcuts to the menu bar and user interface](https://developer.apple.com/documentation/uikit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface)
- [HKHealthStore.isHealthDataAvailable()](https://developer.apple.com/documentation/healthkit/hkhealthstore/ishealthdataavailable()) - Framework presence versus health-data access

## Changelog

These dates describe Apple's HIG article history.

### May 2, 2023
- Consolidated guidance into one page.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/mac-catalyst)*
