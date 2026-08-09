# Liquid Glass

Learn how to design and develop beautiful interfaces that leverage Liquid Glass.

**Platforms:** iOS 26.0+ | iPadOS 26.0+ | macOS Tahoe 26.0+ | tvOS 26.0+ | visionOS 26.0+ | watchOS 26.0+

## Overview

Interfaces across Apple platforms feature a new dynamic material called Liquid Glass, which combines the optical properties of glass with a sense of fluidity. Learn how to adopt this material and embrace the design principles of Apple platforms to create beautiful interfaces that establish hierarchy, create harmony, and maintain consistency across devices and platforms.

Standard components from SwiftUI, UIKit, and AppKit like controls and navigation elements pick up the appearance and behavior of this material automatically. You can also implement these effects in custom interface elements.

## Topics

### Introduction to Liquid Glass

Liquid Glass is a revolutionary material that transforms how interfaces look, feel, and respond across Apple platforms. This translucent material reflects and refracts its surroundings while dynamically transforming to help bring greater focus to content, delivering a new level of vitality across controls, navigation, app icons, widgets, and more.

**Key Characteristics:**
- **Translucent and Glass-like** - Behaves like real glass with optical properties
- **Dynamic and Fluid** - Transforms based on content and context
- **Platform Universal** - Consistent experience across iOS, iPadOS, macOS, tvOS, visionOS, and watchOS
- **Content-Focused** - Designed to highlight and emphasize underlying content

> **iOS 27+, iPadOS 27+, macOS Golden Gate 27+:** Liquid Glass is refined in the OS 27 generation, not replaced. Busy background content is diffused more aggressively, a subtle darkened edge ring improves separation, and specular highlights are brighter and better defined. A continuous transparency slider in Settings > Appearance replaces the Clear/Tinted toggle, so your interface must stay legible across the full range people can choose. **No new named Liquid Glass API types were introduced in OS 27** — existing code continues to work.

### The Real API Surface

Use these verified API names when working with Liquid Glass. Do not invent framework or modifier names.

**SwiftUI**
- `glassEffect(_:in:)` — apply the material to a custom view
- `GlassEffectContainer` — group multiple glass effects so they blend and morph together, and to reduce rendering cost
- `glassEffectID(_:in:)` — identify a glass element across state transitions for smooth morphing
- `glassEffectUnion(id:namespace:)` — merge adjacent glass shapes into one continuous surface
- `buttonStyle(.glass)` and `buttonStyle(.glassProminent)` — standard glass button styles
- `backgroundExtensionEffect()` — extend content beneath sidebars and inspectors

**UIKit**
- `UIGlassEffect` — the material as a visual effect
- `UIGlassContainerEffect` — the container analogue of `GlassEffectContainer`
- `UIBackgroundExtensionView` — edge-to-edge content extension

**AppKit**
- `NSGlassEffectView` and `NSGlassEffectContainerView`
- `NSBackgroundExtensionView`

There is no `LiquidGlass` module to import, and no `.liquidGlassStyle`-style modifiers. The material is delivered through the frameworks you already use.

### Adopting Liquid Glass

If you have an existing app, adopting Liquid Glass doesn't mean reinventing your app from the ground up. Start by building your app in the latest version of Xcode to see the changes. Then, follow best practices in your interface to help your app look right at home on Apple platforms.

**Core Implementation Areas:**
- **Embrace the visual refresh** for materials, controls, and app icons
- **Provide a universal navigation and search experience** across platforms
- **Ensure your interface's organization and layout** looks consistent with other apps and system experiences
- **Adopt best practices** for windows, modals, menus, and toolbars
- **Test your app** to ensure it provides a great experience across platforms

### Design Principles

The Human Interface Guidelines contains guidance and best practices that can help you design a great experience for any Apple platform. Browse the HIG to discover more about adapting your interface for Liquid Glass.

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

Liquid Glass extends across all Apple platforms with platform-specific optimizations:

**iOS 26**  
- Dynamic tab bars that adapt during scrolling
- Enhanced control interactions with fluid morphing
- Lock Screen time integration with photo wallpapers

**iPadOS 26**  
- Immersive sidebars with content refraction
- Enhanced window management with Liquid Glass
- Magic Keyboard and Apple Pencil integration

**macOS Tahoe 26**  
- Completely transparent menu bar
- Customizable desktop with multiple appearance options
- Window controls integrated with Liquid Glass

**tvOS 26**  
- Enhanced focus-based navigation
- Siri Remote integration with Liquid Glass materials
- 10-foot experience optimization

**visionOS 26.0+**
- 3D content integration with 2D interfaces
- Depth-based visual effects
- Spatial computing enhancements

**watchOS 26**  
- Refined controls optimized for Apple Watch
- Smart Stack widget integration
- Always-On display compatibility

### Related Components

- [Adopting Liquid Glass](https://developer.apple.com/documentation/xcode/adopting-liquid-glass) - Implementation guidance
- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) - Design principles
- [Landmarks: Building an app with Liquid Glass](https://developer.apple.com/documentation/swiftui/landmarks-building-an-app-with-liquid-glass) - Sample code

### Developer Documentation

- [SwiftUI](https://developer.apple.com/documentation/swiftui) - Framework
- [UIKit](https://developer.apple.com/documentation/uikit) - Framework
- [AppKit](https://developer.apple.com/documentation/appkit) - Framework
- [RealityKit](https://developer.apple.com/documentation/realitykit) - 3D content framework
- [Icon Composer](https://developer.apple.com/documentation/xcode/icon-composer) - Icon design tool

### Videos

- [Meet Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/10001/) - Introduction to the new design system
- [Get to know the new design system](https://developer.apple.com/videos/play/wwdc2025/10002/) - Design principles and guidelines
- [Build a SwiftUI app with the new design](https://developer.apple.com/videos/play/wwdc2025/10003/) - SwiftUI implementation
- [Build a UIKit app with the new design](https://developer.apple.com/videos/play/wwdc2025/10004/) - UIKit implementation
- [Build an AppKit app with the new design](https://developer.apple.com/videos/play/wwdc2025/10005/) - AppKit implementation

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/technologyoverviews/liquid-glass)*