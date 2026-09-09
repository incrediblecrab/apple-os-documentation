# Adopting Liquid Glass

Find out how to bring the new material to your app.

**Platforms:** iOS 26.0+ | iPadOS 26.0+ | macOS 26.0+ | tvOS 26.0+ | watchOS 26.0+

Native visionOS uses its own [window glass and material guidance](../human-interface-guidelines/foundations/materials.md#visionos). Check individual APIs rather than treating this platform list as universal availability.

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
- [titleBar](https://developer.apple.com/documentation/swiftui/windowstyle/titlebar) - SwiftUI
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
- **Extend backgrounds beneath sidebars and inspectors** - A background extension effect mirrors and blurs adjacent content to create an edge-to-edge appearance; it doesn't move the original content beneath the sidebar or inspector

### Menus and Toolbars

Menus have a refreshed look across platforms. They adopt Liquid Glass, and menu items for common actions use icons to help people quickly scan and identify those actions. Toolbars provide a grouping mechanism for toolbar items.

Use standard toolbar items and grouping APIs instead of reproducing the system background. Keep related actions together, and use deliberate spacing between groups.

**Best Practices:**
- **Adopt standard icons in menu items** - For common actions like Cut, Copy, and Paste, use standard selectors
- **Match top menu actions to swipe actions** - Ensure consistency between contextual menus and swipe actions
- **Determine which toolbar items to group together** - Group items that perform similar actions or affect the same interface parts
- **Choose recognizable labels and icons** - Use standard icons for familiar actions, keep accessible names, and retain text where an icon alone would be ambiguous

### Windows and Modals

Windows adopt rounder corners to fit controls and navigation elements. In iPadOS, apps show window controls and support continuous window resizing. Modal views like sheets and action sheets adopt Liquid Glass.

**Window Components:**
- [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview) - SwiftUI
- [confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)](https://developer.apple.com/documentation/swiftui/view/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)) - SwiftUI

**Implementation Guidelines:**
- **Support flexible window sizes** - Adapt continuously as people resize windows within the supported size limits
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

#### iOS, iPadOS, and macOS

Rebuild with the SDK you intend to ship, then test on each supported runtime. Check touch, pointer, keyboard, window resizing, and the distinction between content and navigation.

#### tvOS

Use standard focus APIs so controls respond consistently when focused. Apple's adoption guide specifies Apple TV 4K (2nd generation) and newer for Liquid Glass effects; older devices retain their existing appearance. Test readable focus feedback on both.

#### watchOS

The adoption guide describes a smaller visual change that can appear without rebuilding. Use standard toolbar APIs and button styles from watchOS 10, and check glanceability and the Always On state instead of adding glass to every surface.

### Appearance and accessibility validation

1. Use regular glass for most controls and text-heavy functional surfaces such as sidebars or popovers, not general content backgrounds. Choose clear glass only over appropriate media, and evaluate dimming and foreground contrast as described in [Materials](../human-interface-guidelines/foundations/materials.md).
2. Test the Liquid Glass appearance choices and accessibility preferences actually offered on each target device. Include Reduce Transparency, Increase Contrast, and Reduce Motion where available; do not assume a particular Settings control or opacity value.
3. Exercise light and dark appearances over the brightest, darkest, and busiest content your app displays. Keep focus, selection, loading, and failure understandable without relying only on color or translucency.
4. Test larger text, right-to-left layouts, keyboard navigation, and VoiceOver. Verify that morphing or resizing does not hide controls, lose focus, or change the apparent meaning of an action.
5. Preview layered app icons in [Icon Composer](https://developer.apple.com/icon-composer/), using the supported appearances and platform-specific icon requirements. Do not bake system lighting or masking into the artwork.

### Performance Considerations

- **Combine custom Liquid Glass effects** - Use `GlassEffectContainer` to optimize performance when applying effects to custom elements
- **Performance test your app across platforms** - Regularly assess and improve performance when building with latest SDKs
- **Measure the actual workload** - Profile scrolling and animation on your oldest supported devices, with representative content and accessibility settings. Do not assume a numerical performance gain from a new OS release.

### SDK, runtime, and deployment targets

[`UIDesignRequiresCompatibility`](https://developer.apple.com/documentation/bundleresources/information-property-list/uidesignrequirescompatibility) is a temporary UI migration aid. Where honored, `YES` requests compatibility with the previous SDK's UI; `NO` or an absent key uses the running OS's design for apps linked against the latest SDK.

Apple explicitly says the system **ignores this key when building for iOS 27 or later, iPadOS 27 or later, Mac Catalyst 27 or later, macOS 27 or later, or tvOS 27 or later**. Do not extend that list to watchOS or visionOS. The setting is not a supported opt-out for the listed 27-generation builds.

Keep three independent decisions clear:

- **Build SDK:** the APIs and linked-SDK behavior used to build the binary.
- **Deployment target:** the oldest OS the binary is intended to run on. Lowering it does not turn a 27-SDK build into a 26-SDK build or restore the compatibility option.
- **Runtime OS:** the system that supplies the actual controls, rendering, and accessibility behavior. A new SDK does not backport new APIs to an older runtime.

The following cases apply to the platforms listed in the key's documentation:

| Build SDK | Runtime | Deployment requirement | Appearance and compatibility review |
|-----------|---------|------------------------|-------------------------------------|
| 26-generation SDK | Corresponding OS 26 | Minimum target permits OS 26. | `YES` requests the temporary compatibility UI; `NO` or omission uses the OS 26 design. |
| 26-generation SDK | Corresponding OS 27 | Binary remains eligible to run. | The binary is still a 26-SDK build. Check its key and test the existing binary; an OS update is not a rebuild, and the key documentation is not a guarantee of every older binary's exact rendering. |
| 27-generation SDK | Corresponding OS 26 | The SDK supports this deployment target and the app's minimum is no higher than 26. | This is not automatically “N/A.” Use runtime availability checks for newer APIs and test the OS 26 presentation. Do not depend on the key as a supported escape hatch for a 27-SDK build. |
| 27-generation SDK | Corresponding OS 27 | Minimum target permits that runtime. | The key is ignored for the listed build targets; validate the runtime's system design and your custom UI. |

This is not a universal matrix for binaries built with every historical SDK. The cited key documentation does not enumerate all older-runtime combinations. Record actual test results for the SDK, deployment target, runtime, device, and preferences you ship.

App Store submission SDK requirements are a separate policy question. Consult [Upcoming Requirements](https://developer.apple.com/news/upcoming-requirements/) rather than deriving a submission deadline from the design's version number.

### Related Components

- [Icon Composer](https://developer.apple.com/icon-composer/) - Icon design tool
- [Improving your app's performance](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance) - Performance guidance

### Developer Documentation

- [SwiftUI](https://developer.apple.com/documentation/swiftui) - Framework
- [UIKit](https://developer.apple.com/documentation/uikit) - Framework  
- [AppKit](https://developer.apple.com/documentation/appkit) - Framework
- [Creating your app icon using Icon Composer](https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer) - Icon creation guidance

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass)*