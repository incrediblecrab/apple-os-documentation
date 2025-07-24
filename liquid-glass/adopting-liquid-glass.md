# Adopting Liquid Glass

Find out how to bring the new material to your app.

**Platforms:** iOS 26.0+ | iPadOS 26.0+ | macOS Tahoe 26.0+ | tvOS 26.0+ | visionOS 3.0+ | watchOS 26.0+

## Overview

If you have an existing app, adopting Liquid Glass doesn't mean reinventing your app from the ground up. Start by building your app in the latest version of Xcode to see the changes. As you review your app, use the following sections to understand the scope of changes and learn how you can adopt these best practices in your interface.

### See Your App with Liquid Glass

If your app uses standard components from SwiftUI, UIKit, or AppKit, your interface picks up the latest look and feel on the latest platform releases for iOS, iPadOS, macOS, tvOS, and watchOS. In Xcode, build your app with the latest SDKs, and run it on the latest platform releases to see the changes in your interface.

## Topics

### Visual Refresh

Interfaces across Apple platforms feature a new dynamic material called Liquid Glass, which combines the optical properties of glass with a sense of fluidity. This material forms a distinct functional layer for controls and navigation elements. It affects how the interface looks, feels, and moves, adapting in response to a variety of factors to help bring focus to the underlying content.

**Implementation Guidelines:**
- **Leverage system frameworks to adopt Liquid Glass automatically** - Standard components like bars, sheets, popovers, and controls automatically adopt this material
- **Reduce your use of custom backgrounds in controls and navigation elements** - Custom backgrounds might overlay or interfere with Liquid Glass or other system effects
- **Test your interface with accessibility settings** - Translucency and fluid morphing animations can adapt to people's needs when accessibility settings like reduced transparency are enabled
- **Avoid overusing Liquid Glass effects** - Apply these effects sparingly to custom controls to maintain focus on content

**Core Components:**
- [NavigationStack](https://developer.apple.com/documentation/swiftui/navigationstack) - SwiftUI
- [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview) - SwiftUI
- [titleBar](https://developer.apple.com/documentation/swiftui/titlebar) - SwiftUI
- [toolbar(content:)](https://developer.apple.com/documentation/swiftui/view/toolbar(content:)) - SwiftUI
- [glassEffect(_:in:)](https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:)) - SwiftUI

### App Icons

App icons take on a design that's dynamic and expressive. Updates to the icon grid result in a standardized iconography that's visually consistent across devices and concentric with hardware and other elements across the system. App icons now contain layers, which dynamically respond to lighting and other visual effects the system provides.

**Design Principles:**
- **Provide a visually consistent, optically balanced design** - Ensure consistency across all platforms your app supports
- **Consider a simplified design comprised of solid, filled, overlapping semi-transparent shapes** - This approach works best with the new layered system
- **Let the system handle applying masking, blurring, and other visual effects** - Don't factor these into your design
- **Design using layers** - Define separate layers for foreground, middle, and background elements
- **Compose and preview in Icon Composer** - Use the Icon Composer app to create layer groupings and preview your design

### Controls

Controls have a refreshed look across platforms, and come to life when a person interacts with them. The shape of the hardware informs the curvature of controls, so many controls adopt rounder forms to elegantly nestle into the corners of windows and displays.

**Updated Controls:**
- [Button](https://developer.apple.com/documentation/swiftui/button) - SwiftUI
- [Toggle](https://developer.apple.com/documentation/swiftui/toggle) - SwiftUI
- [Slider](https://developer.apple.com/documentation/swiftui/slider) - SwiftUI
- [Stepper](https://developer.apple.com/documentation/swiftui/stepper) - SwiftUI
- [Picker](https://developer.apple.com/documentation/swiftui/picker) - SwiftUI
- [TextField](https://developer.apple.com/documentation/swiftui/textfield) - SwiftUI

**Best Practices:**
- **Review updates to control appearance and dimensions** - Standard controls automatically adopt changes when you rebuild with the latest Xcode
- **Review your use of color in controls** - Be judicious with color use and leverage system colors for automatic light/dark adaptation
- **Check for crowding or overlapping of controls** - Allow Liquid Glass room to move and breathe

### Navigation

Liquid Glass applies to the topmost layer of the interface, where you define your navigation. Key navigation elements like tab bars and sidebars float in this Liquid Glass layer to help people focus on the underlying content.

**Navigation Components:**
- [sidebarAdaptable](https://developer.apple.com/documentation/swiftui/tabviewstyle/sidebaradaptable) - SwiftUI
- [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview) - SwiftUI
- [inspector(isPresented:content:)](https://developer.apple.com/documentation/swiftui/view/inspector(ispresented:content:)) - SwiftUI
- [backgroundExtensionEffect()](https://developer.apple.com/documentation/swiftui/view/backgroundextensioneffect()) - SwiftUI
- [tabBarMinimizeBehavior(.onScrollDown)](https://developer.apple.com/documentation/swiftui/view/tabbarminimizebehavior(_:)) - SwiftUI

**Implementation Guidelines:**
- **Establish a clear navigation hierarchy** - Clearly separate content from navigation elements
- **Consider adapting your tab bar into a sidebar automatically** - Use sidebarAdaptable for contextual adaptation
- **Use split views for sidebar layouts with inspector panels** - Split views provide consistent experiences across platforms
- **Extend content beneath sidebars and inspectors** - Use background extension effects for full edge-to-edge experiences

### Menus and Toolbars

Menus have a refreshed look across platforms. They adopt Liquid Glass, and menu items for common actions use icons to help people quickly scan and identify those actions. Toolbars provide a grouping mechanism for toolbar items.

**Toolbar Components:**
- [fixed](https://developer.apple.com/documentation/swiftui/toolbaritemspacing/fixed) - SwiftUI
- [ToolbarSpacer](https://developer.apple.com/documentation/uikit/uitoolbarspacer) - UIKit
- [hidden(_:)](https://developer.apple.com/documentation/swiftui/view/hidden(_:)) - SwiftUI

**Best Practices:**
- **Adopt standard icons in menu items** - For common actions like Cut, Copy, and Paste, use standard selectors
- **Match top menu actions to swipe actions** - Ensure consistency between contextual menus and swipe actions
- **Determine which toolbar items to group together** - Group items that perform similar actions or affect the same interface parts
- **Find icons to represent common actions** - Use standard icons instead of text for better interface clarity

### Windows and Modals

Windows adopt rounder corners to fit controls and navigation elements. In iPadOS, apps show window controls and support continuous window resizing. Modal views like sheets and action sheets adopt Liquid Glass.

**Window Components:**
- [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview) - SwiftUI
- [confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)](https://developer.apple.com/documentation/swiftui/view/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)) - SwiftUI

**Implementation Guidelines:**
- **Support arbitrary window sizes** - Allow people to resize windows to their preferred dimensions
- **Use split views to allow fluid resizing of columns** - Split views automatically reflow content with beautiful transitions
- **Use layout guides and safe areas** - Specify safe areas for automatic window control adjustment
- **Check content around sheet edges** - Verify content appearance near rounder corners and inset sheets

### Organization and Layout

Style updates to list-based layouts help you organize and showcase your content. Organizational components like lists, tables, and forms have larger row height and padding, with increased corner radius to match system curvature.

**Best Practices:**
- **Check capitalization in section headers** - Lists optimize for legibility by adopting title-style capitalization
- **Adopt forms to take advantage of layout metrics** - Use SwiftUI forms with grouped form style for automatic layout updates

### Search

Platform conventions for location and behavior of search optimize the experience for each device and use case.

**Search Components:**
- [Tab(role: .search)](https://developer.apple.com/documentation/swiftui/tab/init(role:content:)) - SwiftUI

**Implementation Guidelines:**
- **Check keyboard layout when activating search interface** - Test the experience of search fields sliding upward as keyboard appears
- **Use semantic search tabs** - Use standard system APIs for indicating search tabs

### Platform Considerations

**iOS 26.0+, iPadOS 26.0+, macOS Tahoe 26.0+, tvOS 26.0+, visionOS 3.0+**  
Liquid Glass can have distinct appearance and behavior across different platforms, contexts, and input methods. Test your app across devices to understand how the material looks and feels.

**watchOS 26.0+**  
Liquid Glass changes are minimal in watchOS and appear automatically when you open your app on the latest release. However, adopt standard toolbar APIs and button styles from watchOS 10 to ensure proper appearance.

### Performance Considerations

- **Combine custom Liquid Glass effects** - Use GlassEffectContainer to optimize performance when applying effects to custom elements
- **Performance test your app across platforms** - Regularly assess and improve performance when building with latest SDKs
- **Use UIDesignRequiresCompatibility key** - Add to your information property list to maintain previous SDK appearance while updating

### Related Components

- [Icon Composer](https://developer.apple.com/documentation/xcode/icon-composer) - Icon design tool
- [Improving your app's performance](https://developer.apple.com/documentation/xcode/improving_your_app_s_performance) - Performance guidance

### Developer Documentation

- [SwiftUI](https://developer.apple.com/documentation/swiftui) - Framework
- [UIKit](https://developer.apple.com/documentation/uikit) - Framework  
- [AppKit](https://developer.apple.com/documentation/appkit) - Framework
- [Creating your app icon using Icon Composer](https://developer.apple.com/documentation/xcode/creating_your_app_icon_using_icon_composer) - Icon creation guidance

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/xcode/adopting-liquid-glass)*