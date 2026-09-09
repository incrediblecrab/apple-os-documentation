# Liquid Glass

Learn how to design and develop beautiful interfaces that leverage Liquid Glass.

**Platforms:** iOS 26.0+ | iPadOS 26.0+ | macOS 26.0+ | tvOS 26.0+ | watchOS 26.0+

For native visionOS window glass, follow the separate [Materials guidance](../human-interface-guidelines/foundations/materials.md#visionos). Do not infer visionOS API availability from the shared visual vocabulary.

## Overview

Interfaces across Apple platforms feature a new dynamic material called Liquid Glass, which combines the optical properties of glass with a sense of fluidity. Learn how to adopt this material and embrace the design principles of Apple platforms to create beautiful interfaces that establish hierarchy, create harmony, and maintain consistency across devices and platforms.

Standard components from SwiftUI, UIKit, and AppKit like controls and navigation elements pick up the appearance and behavior of this material automatically. You can also implement these effects in custom interface elements.

## Topics

### Introduction to Liquid Glass

Liquid Glass separates controls and navigation from the content they act on. Its appearance responds to the surrounding content and to interaction, so prefer system components over reproducing a fixed blur or highlight in artwork.

**Key Characteristics:**
- **Functional hierarchy** - Reserve glass for important interactive and navigation elements, not every content surface.
- **Context-sensitive appearance** - Test over actual content instead of assuming a fixed color or opacity.
- **Platform-specific behavior** - Touch, pointer, remote focus, and watch interactions need different treatment.
- **Accessible adaptation** - Respect the appearances and accessibility preferences the device provides.

For the `regular` and `clear` variants, dimming, and standard content-layer materials, see [Materials](../human-interface-guidelines/foundations/materials.md). For the documented OS 27 compatibility-key change, see [Adopting Liquid Glass](adopting-liquid-glass.md#sdk-runtime-and-deployment-targets).

### The Real API Surface

Use these verified API names when working with Liquid Glass. Do not invent framework or modifier names.

**SwiftUI** — use `import SwiftUI`
- `glassEffect(_:in:)` — apply the material to a custom view
- `GlassEffectContainer` — group multiple glass effects so they blend and morph together, and to reduce rendering cost
- `glassEffectID(_:in:)` — identify a glass element across state transitions for smooth morphing
- `glassEffectUnion(id:namespace:)` — combine effects with a shared union identifier, shape, and glass variant into a single shape
- `buttonStyle(.glass)` and `buttonStyle(.glassProminent)` — standard glass button styles
- `backgroundExtensionEffect()` — extend a background using mirrored, blurred copies of adjacent content beneath sidebars and inspectors

**UIKit**
- `UIGlassEffect` — the material as a visual effect
- `UIGlassContainerEffect` — the container analogue of `GlassEffectContainer`
- `UIBackgroundExtensionView` — edge-to-edge content extension

**AppKit**
- `NSGlassEffectView` and `NSGlassEffectContainerView`
- `NSBackgroundExtensionView`

There is no `LiquidGlass` module to import, and no `.liquidGlassStyle`-style modifiers. The material is delivered through the frameworks you already use.

Check each symbol's availability. In particular, the references for [`glassEffect(_:in:)`](https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:)) and [`GlassEffectContainer`](https://developer.apple.com/documentation/swiftui/glasseffectcontainer) list the 26-generation iOS, iPadOS, Mac Catalyst, macOS, tvOS, and watchOS platforms, not visionOS. A newer build SDK does not make a new API available on an older runtime.

### Adopting Liquid Glass

If you have an existing app, adopting Liquid Glass doesn't mean reinventing your app from the ground up. Start by building your app in the latest version of Xcode to see the changes. Then, follow best practices in your interface to help your app look right at home on Apple platforms.

**Core Implementation Areas:**
- **Embrace the visual refresh** for materials, controls, and app icons
- **Provide a universal navigation and search experience** across platforms
- **Ensure your interface's organization and layout** looks consistent with other apps and system experiences
- **Adopt best practices** for windows, modals, menus, and toolbars
- **Test your app** to ensure it provides a great experience across platforms

### Design Principles

Use the HIG's [Design principles](../human-interface-guidelines/getting-started/design-principles.md) to evaluate hierarchy, agency, accessibility, and platform fit before applying a visual treatment.

**Design Guidelines:**
- **Define a layout and choose a navigation structure** that puts the most important content in focus
- **Reimagine your app icon** with simple, bold layers that offer dimensionality and consistency across devices and appearances
- **Be judicious with your use of color** in controls and navigation so they stay legible and allow your content to infuse them and shine through
- **Ensure interface elements fit in** with software and hardware design across devices
- **Adopt standard iconography** and predictable action placement across platforms

### Sample Code and Examples

The Landmarks app showcases how to create a beautiful and engaging user experience using SwiftUI and Liquid Glass. Explore how the Landmarks app implements the look and feel of the Liquid Glass material throughout its interface.

**Featured Examples:**
- **Configure an app icon with Icon Composer** - Create layered, dynamic icons
- **Create an edge-to-edge content experience** with the background extension effect
- **Enhance the edge-to-edge content experience** by extending horizontal scroll views under a sidebar or inspector
- **Make your interface adaptable** to changing window sizes
- **Explore search conventions** across platforms
- **Apply Liquid Glass effects** to custom interface elements and animations

### Platform Integration

| Platform | Design emphasis |
|----------|-----------------|
| [iOS](../human-interface-guidelines/getting-started/iOS.md) | Reachable controls, clear navigation, and text that reflows with accessibility sizes. |
| [iPadOS](../human-interface-guidelines/getting-started/iPadOS.md) | Resizable windows, legible sidebars, and seamless changes between touch, Pencil, pointer, and keyboard. |
| [macOS](../human-interface-guidelines/getting-started/macOS.md) | Document work, menus, keyboard commands, and separation between tools and content. |
| [tvOS](../human-interface-guidelines/getting-started/tvOS.md) | System focus behavior and readable controls over media. Apple's adoption guide limits Liquid Glass effects to Apple TV 4K (2nd generation) and newer. |
| [watchOS](../human-interface-guidelines/getting-started/watchOS.md) | Brief interactions, glanceable information, and standard button and toolbar APIs. |
| [visionOS](../human-interface-guidelines/getting-started/visionOS.md) | Platform-specific window glass, comfortable spatial placement, and awareness of the surroundings; do not copy the other platforms' material APIs indiscriminately. |

### Related Components

- [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass) - Implementation guidance
- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) - Design principles
- [Landmarks: Building an app with Liquid Glass](https://developer.apple.com/documentation/swiftui/landmarks-building-an-app-with-liquid-glass) - Sample code

### Developer Documentation

- [SwiftUI](https://developer.apple.com/documentation/swiftui) - Framework
- [UIKit](https://developer.apple.com/documentation/uikit) - Framework
- [AppKit](https://developer.apple.com/documentation/appkit) - Framework
- [RealityKit](https://developer.apple.com/documentation/realitykit) - 3D content framework
- [Icon Composer](https://developer.apple.com/icon-composer/) - Icon design tool

### Videos

- [Meet Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219/) - Introduction to the design system
- [Get to know the new design system](https://developer.apple.com/videos/play/wwdc2025/356/) - Design principles and guidelines
- [Build a SwiftUI app with the new design](https://developer.apple.com/videos/play/wwdc2025/323/) - SwiftUI implementation
- [Build a UIKit app with the new design](https://developer.apple.com/videos/play/wwdc2025/284/) - UIKit implementation
- [Build an AppKit app with the new design](https://developer.apple.com/videos/play/wwdc2025/310/) - AppKit implementation

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/technologyoverviews/liquid-glass)*