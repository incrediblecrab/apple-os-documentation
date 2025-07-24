# Interface Fundamentals

Explore the components that go into building your app's interface, and discover platform-specific features that improve the experience you offer to people.

**Platforms:** iOS 14.0+ | iPadOS 14.0+ | macOS 11.0+ | tvOS 14.0+ | visionOS 1.0+ | watchOS 7.0+

## Overview

To build your app's interface, you can use standard system views, draw content yourself, or mix custom drawing with the standard views. Regardless of how you create your content, all interfaces rely on some standard components to present that content:

- **Windows** are the primary containers for your app's content, and they also facilitate system-related interactions
- **Scenes** manage instances of your app's interface in iOS, iPadOS, tvOS, visionOS, and watchOS
- **Views and controls** display specific types of content in your interface
- **Volumes** are a specific type of window that you use to showcase 2D and 3D content in visionOS

The app-builder technologies you use to create your app maintain a separation between your app's data and the views and other interface elements you use to display that data. Your data model objects are always the source of truth for your app's content.

## Topics

### Core Architecture Components

**Windows**  
Windows are the primary containers for your app's content, and they also facilitate system-related interactions. Every SwiftUI, UIKit, and AppKit app has at least one window, and some platforms let your app display multiple windows simultaneously. Windows in macOS, iPadOS, and visionOS can have a visible border and controls to change the size of the window. Windows in iOS, tvOS, and watchOS have no visible appearance of their own.

**Scenes**  
Scenes manage instances of your app's interface in iOS, iPadOS, tvOS, visionOS, and watchOS. Every SwiftUI and UIKit app has at least one scene, and you can create additional scenes to manage distinct experiences. Each scene manages the data for one instance of your interface and any relevant system behaviors. AppKit apps don't use scenes.

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
- Design for the 10-foot experience

**visionOS**  
Design your visionOS interface around an initial window to provide a familiar starting point for interactions. Add depth-based offsets to specific views to emphasize parts of your window, or to indicate a change in modality.

Key considerations:
- Incorporate 3D objects directly into view layouts
- Add hover effects to highlight elements when someone looks at them
- Use ornaments for frequently used tools and commands
- Build 3D content as USD assets using RealityKit

**watchOS**  
Design your watchOS app to deliver only the most relevant content in a timely manner. Be prepared to support different sizes of Apple Watch, ranging from 38mm to 45mm.

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

### Platform Feature Matrix

| Feature | iOS | iPadOS | macOS | tvOS | visionOS | watchOS |
|---------|-----|--------|-------|------|----------|---------|
| **Supported Technologies** | SwiftUI, UIKit | SwiftUI, UIKit | SwiftUI, AppKit | SwiftUI, UIKit, TVUIKit | SwiftUI, UIKit | SwiftUI |
| **Full-screen Mode** | Yes | Yes | Available | Yes | Available | Yes |
| **Dark Mode** | Yes | Yes | Yes | Yes | No | No |
| **Dynamic Type** | Yes | Yes | No | No | Yes | Yes |
| **Multiple Windows** | Yes* | Yes | Yes | No | Yes | No |
| **Menu Types** | Context | Main, context | Main, context, Dock | None | Main, context | None |
| **Primary Interaction** | Touch | Touch, Apple Pencil, Magic Keyboard | Mouse, keyboard | Siri Remote | Eyes, hands | Touch, Digital Crown |
| **Bluetooth Keyboard** | Yes | Yes | Yes | No | Yes | No |
| **Background Tasks** | Limited | Limited | Yes | No | Limited | No |
| **CarPlay Support** | Yes | No | No | No | No | No |

*iOS supports multiple windows when an external display is connected.*

### Related Components

- [SwiftUI](https://developer.apple.com/design/human-interface-guidelines/swiftui) - Declarative UI framework
- [UIKit](https://developer.apple.com/design/human-interface-guidelines/uikit) - iOS and iPadOS UI framework
- [AppKit](https://developer.apple.com/design/human-interface-guidelines/appkit) - macOS UI framework

### Developer Documentation

- [SwiftUI](https://developer.apple.com/documentation/swiftui) - Framework
- [UIKit](https://developer.apple.com/documentation/uikit) - Framework
- [AppKit](https://developer.apple.com/documentation/appkit) - Framework
- [WindowGroup](https://developer.apple.com/documentation/swiftui/windowgroup) - SwiftUI
- [Scene](https://developer.apple.com/documentation/swiftui/scene) - SwiftUI
- [Auto Layout](https://developer.apple.com/documentation/uikit/auto_layout) - UIKit
- [Background Assets](https://developer.apple.com/documentation/backgroundassets) - Framework

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/technologyoverviews/interface-fundamentals)*