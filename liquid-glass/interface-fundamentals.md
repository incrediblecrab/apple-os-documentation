# Interface Fundamentals

Explore the components that go into building your app's interface, and discover platform-specific features that improve the experience you offer to people.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

These are architectural and design concepts, not a shared minimum-OS requirement. Check individual APIs for availability. See [Liquid Glass](introduction.md) for the material's adoption guidance and [Materials](../human-interface-guidelines/foundations/materials.md) for the distinct visionOS window treatment.

## Overview

To build your app's interface, you can use standard system views, draw content yourself, or mix custom drawing with the standard views. Regardless of how you create your content, all interfaces rely on some standard components to present that content:

- **Windows** are the primary containers for your app's content, and they also facilitate system-related interactions
- **Scenes** organize interface instances in SwiftUI, including on macOS, and in UIKit's scene-based lifecycle
- **Views and controls** display specific types of content in your interface
- **Volumes** are a specific type of window that you use to showcase 2D and 3D content in visionOS

The app-builder technologies you use to create your app maintain a separation between your app's data and the views and other interface elements you use to display that data. Your data model objects are always the source of truth for your app's content.

## Topics

### Core Architecture Components

**Windows**  
Windows are the primary containers for window-based app content, and they also facilitate system-related interactions. Some platforms let your app display multiple windows simultaneously. Not every app needs a conventional content window: SwiftUI supports macOS utilities composed only of a [`MenuBarExtra`](https://developer.apple.com/documentation/swiftui/menubarextra). Windows in macOS, iPadOS, and visionOS can have a visible border and resizing controls; in iOS, tvOS, and watchOS, the window container has no visible appearance of its own.

**Scenes**  
In the SwiftUI app lifecycle, an app's body combines one or more [`Scene`](https://developer.apple.com/documentation/swiftui/scene) values, including on macOS. UIKit's scene-based lifecycle uses `UIWindowScene` and scene delegates to manage interface instances. Don't conflate these with AppKit's own window/controller lifecycle, or assume that older UIKit lifecycle implementations use scenes.

**Views and Controls**  
Views and controls display specific types of content in your interface. SwiftUI, UIKit, and AppKit provide views for displaying standard types of content like images, text, collections, pickers, buttons, toggles, and much more. They also define the architecture that you use to create custom views and display any content you want.

**Volumes (visionOS)**  
Volumes are a specific type of window that you use to showcase 2D and 3D content in visionOS.

### Platform-Specific Design Approaches

**iOS and iPadOS**  
Design iOS and iPadOS apps as experiences people can take with them anywhere. Apps in iOS fill the screen, and apps in iPadOS need to be flexible enough to fill all or part of the screen. Because space is more constrained, interfaces make greater use of layout and navigation elements to organize content.

Key considerations:
- Handle different iPhone and iPad sizes and orientations gracefully
- Use automatic layout for size adaptability
- Support Magic Keyboard and Apple Pencil features on iPad
- Implement pointer-based navigation and hover interactions

**macOS**  
Design your macOS app to take advantage of the power, space, and flexibility of a Mac. Mac gives you more space for your content, but that doesn't mean you want a cluttered interface.

Key considerations:
- Support flexible layouts and different window sizes
- Adopt full-screen mode for distraction-free environments
- Utilize the menu bar for app-relevant actions
- Implement proper window management

**tvOS**  
Design your tvOS interface with focus-based navigation in mind. Most interactions with your app occur through the Siri Remote. People use directional buttons to change focus and the select button to act on focused items.

Key considerations:
- Implement straightforward navigation patterns
- Minimize text input and complex interactions
- Use lockups to group related views into single, selectable elements
- Design for comfortable viewing and interaction from across the room

**visionOS**  
Design your visionOS interface around an initial window to provide a familiar starting point for interactions. Add depth-based offsets to specific views to emphasize parts of your window, or to indicate a change in modality.

Key considerations:
- Incorporate 3D objects directly into view layouts
- Add hover effects to highlight elements when someone looks at them
- Use ornaments for frequently used tools and commands
- Build 3D content as USD assets using RealityKit

**watchOS**  
Design your watchOS app to deliver only the most relevant content in a timely manner. Adapt to all supported watch display sizes and larger text instead of assuming a fixed range of hardware dimensions.

Key considerations:
- Support Always-On display updates
- Create widgets for Smart Stacks
- Build complications for watch faces using WidgetKit
- Design notifications with haptics, sound, and visual cues

### Asset Management

**Images and Icons**  
For images in your app's interface, use SF Symbols whenever possible. The SF Symbols app offers a vast collection of configurable, vector-based images that adapt naturally to appearance and size changes.

**Asset Catalogs**  
Store images, colors, and appearance-sensitive items in asset catalogs. Interfaces need to adapt to different appearances, including light and dark appearances and accessibility settings for people with visual impairments.

**Resource Loading**  
To load resource files present in your app bundle:
- **Images**: Use Image (SwiftUI), UIImage (UIKit), or NSImage (AppKit)
- **Colors**: Use Color (SwiftUI), UIColor (UIKit), or NSColor (AppKit)  
- **Other Resources**: Use Bundle type to locate files by URL

### Standard Interface Behaviors

- **Automatic Layout** - Size and position views using rules-based approach for device adaptability
- **Internationalization** - Prepare for localization using Foundation framework
- **Accessibility** - Review default information and make improvements based on content
- **Undo Support** - Identify actions and build reversible tasks
- **Pasteboard** - Support Cut, Copy, and Paste operations

### Platform review map

| Entrypoint | Review a representative task |
|------------|------------------------------|
| [iOS](../human-interface-guidelines/getting-started/iOS.md) | Navigate and edit with reachable controls, the keyboard visible, and larger text. |
| [iPadOS](../human-interface-guidelines/getting-started/iPadOS.md) | Resize a window and switch between touch, Pencil, pointer, and keyboard without losing work. |
| [macOS](../human-interface-guidelines/getting-started/macOS.md) | Work across document windows, menus, toolbars, and keyboard commands. |
| [tvOS](../human-interface-guidelines/getting-started/tvOS.md) | Move focus, select content, and dismiss playback controls using a remote from across the room. |
| [visionOS](../human-interface-guidelines/getting-started/visionOS.md) | Read and interact comfortably while preserving awareness of the surroundings. |
| [watchOS](../human-interface-guidelines/getting-started/watchOS.md) | Understand a glanceable value and complete a brief action, including with the Digital Crown. |

Across these tasks, test VoiceOver, appropriate larger-text support, right-to-left layouts, contrast, and reduced visual effects. API availability and particular input devices vary by platform; they cannot be reduced to a universal yes/no feature table.

### Related Components

- [Design principles](../human-interface-guidelines/getting-started/design-principles.md)
- [Accessibility](../human-interface-guidelines/foundations/accessibility.md)
- [Materials](../human-interface-guidelines/foundations/materials.md)

### Developer Documentation

- [SwiftUI](https://developer.apple.com/documentation/swiftui) - Framework
- [UIKit](https://developer.apple.com/documentation/uikit) - Framework
- [AppKit](https://developer.apple.com/documentation/appkit) - Framework
- [WindowGroup](https://developer.apple.com/documentation/swiftui/windowgroup) - SwiftUI
- [Scene](https://developer.apple.com/documentation/swiftui/scene) - SwiftUI
- [View layout](https://developer.apple.com/documentation/uikit/view-layout) - UIKit

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/technologyoverviews/interface-fundamentals)*