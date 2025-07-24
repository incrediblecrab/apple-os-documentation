# DeveloperToolsSupport

Expose custom views and modifiers in the Xcode library.

**Platforms:** iOS 14.0+ | iPadOS 14.0+ | Mac Catalyst 14.0+ | macOS 11.0+ | tvOS 14.0+ | visionOS 1.0+ | watchOS 7.0+

## Overview

Using the DeveloperToolsSupport framework, you tell Xcode about your custom SwiftUI views and view modifiers. After adding your views and modifiers, Xcode makes them available to you when you click the Library button (+) in Xcode's toolbar. You can select and drag the custom library items into code, just like you would for system-provided items.

To add items to the library, create a structure that conforms to the LibraryContentProvider protocol and encapsulate any items you want to add as LibraryItem instances. Implement the views computed property to add library items containing views. Implement the modifiers(base:) method to add items containing view modifiers. Xcode harvests items from all of the library content providers in your project as you work, and makes them available to you in its library.

## Topics

### Library Customization
- **LibraryContentProvider** - A source of Xcode library and code completion content.
- **LibraryItem** - A single item to add to the Xcode library.

### Preview Registration
- **PreviewRegistry** - A protocol that the system uses to locate previews at runtime.
- **Preview** - A base type that preview macros use to create previews.
- **PreviewLayout** - A size constraint for a preview.
- **PreviewTrait** - Customizations that you can apply to a preview.

### Resource Definition
- **ColorResource** - A color resource.
- **ImageResource** - An image resource.

### Camera Management
- **PreviewCamera** - A camera that defines a viewpoint in a preview.
- **PreviewCameraBuilder** - A builder type that composes a collection of cameras for previewing a view in a 3D scene.

### Structures
- **PreviewBodyBuilder** - Builder for preview body content within a #Preview macro.
- **PreviewMacroBodyBuilder** - Builder for preview body content within a #Preview macro.
- **PreviewUnavailable** - An error that the system throws when a preview is unavailable at runtime.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/DeveloperToolsSupport)*