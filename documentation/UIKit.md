# UIKit

Construct and manage a graphical, event-driven user interface for your iOS, iPadOS, or tvOS app.

**Platforms:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 13.0+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 2.0+

These are framework-catalog minimums, not availability for every UI class. The watchOS surface includes types such as [`UIColor`](https://developer.apple.com/documentation/uikit/uicolor); use SwiftUI or WatchKit for the watch app interface rather than assuming UIKit's window/scene model applies there.

## Overview

**UIKit** provides a variety of features for building apps, including components you can use to construct the core infrastructure of your iOS, iPadOS, or tvOS apps. The framework provides the window and view architecture for implementing your UI, the event-handling infrastructure for delivering Multi-Touch and other types of input to your app, and the main run loop for managing interactions between the user, the system, and your app.

**UIKit** also includes support for animations, documents, drawing and printing, text management and display, search, app extensions, resource management, and getting information about the current device. You can also customize accessibility support, and localize your app's interface for different languages, countries, or cultural regions.

**UIKit** works seamlessly with the **SwiftUI** framework, so you can implement parts of your **UIKit** app in **SwiftUI** or mix interface elements between the two frameworks. For example, you can place **UIKit** views and view controllers inside **SwiftUI** views, and vice versa.

To build a macOS app, you can use **SwiftUI** to create an app that works across all of Apple's platforms, or use **AppKit** to create an app for Mac only. Alternatively, you can bring your **UIKit** iPad app to the Mac with **Mac Catalyst**.

**Important**

Use **UIKit** classes only from your app's main thread or main dispatch queue, unless otherwise indicated in the documentation for those classes. This restriction particularly applies to classes that derive from **UIResponder** or that involve manipulating your app's user interface in any way.

## OS 27 migration

### Required scene life cycle and launch screen

**Beginning in iOS 27, iPadOS 27, Mac Catalyst 27, tvOS 27, and visionOS 27, apps built with the latest SDK must adopt the scene-based life cycle or they fail to launch.** This is no longer only a warning. See [Transitioning to the UIKit scene-based life cycle](https://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle).

Declare scene support with `UIApplicationSceneManifest`; supply dynamic configurations from `application(_:configurationForConnecting:options:)` when needed. Associate each programmatic `UIWindow` with its `UIWindowScene`. Move UI activation, backgrounding, URL handling, and restoration into the relevant scene delegate, while keeping process-level setup in `UIApplicationDelegate`. Supporting multiple windows remains optional; a single-window app still needs a scene.

Separately, iOS/iPadOS apps built with the 27 SDK must provide a launch screen through `UILaunchStoryboardName`, `UILaunchStoryboards`, `UILaunchScreen`, or `UILaunchScreens`. The release notes specify App Store rejection of missing launch screens when submissions built with this SDK are accepted.

### Behavior and API changes

- `UIScene.extendStateRestoration` and `completeStateRestoration` can extend restoration during background-to-foreground transitions when linked with the iOS/tvOS/Mac Catalyst/visionOS 27 SDKs.
- For iOS 27 SDK builds, presented controllers inherit traits through the presentation's view/superview chain. Audit custom `UIPresentationController` trait overrides rather than assuming a direct jump to the presentation controller.
- Noninteractive external-display scenes are no longer offered automatically in iOS 27 SDK builds. Register a `UISceneAccessory.externalNonInteractive` with `UIViewController.registerSceneAccessory(_:)`.
- Use `UINavigationItem.navigationBarMinimization` instead of the earlier-beta `barMinimizeBehavior` and `barMinimizationSafeAreaAdjustment` properties. Also recheck inline search scope bars and scroll-edge geometry.
- iPadOS/macOS 27 menu image defaults changed. [`UIMenuElement.preferredImageVisibility`](https://developer.apple.com/documentation/uikit/uimenuelement/preferredimagevisibility) controls explicit exceptions; follow the [menu HIG](https://developer.apple.com/design/human-interface-guidelines/menus).
- On iOS and iPadOS 27, Siri can request content through `UIDragInteractionDelegate` without a person starting a drag. Put drag-specific animation or modal presentation in `dragInteraction(_:sessionDidMove:)`, not `dragInteraction(_:sessionWillBegin:)`.
- The 27 SDK deprecates [`canOpenURL(_:)`](https://developer.apple.com/documentation/uikit/uiapplication/canopenurl(_:)). Attempt to open a URL and handle failure, or use universal links rather than treating a preflight result as a guarantee.

### Text and framework integration

The [June 2026 UIKit update](https://developer.apple.com/documentation/updates/uikit) highlights [`NSTextTable`](https://developer.apple.com/documentation/uikit/nstexttable), [`NSTextBlock`](https://developer.apple.com/documentation/uikit/nstextblock), and [`NSTextTableBlock`](https://developer.apple.com/documentation/uikit/nstexttableblock) for attributed-text tables. Their current class metadata lists iOS/iPadOS 6+, Mac Catalyst 13.1+, tvOS 9+, visionOS 1+, and watchOS 2+; the update's publication date is not a uniform OS 27 introduction date.

It also describes [`UITextAttachmentViewProviderReusePolicy`](https://developer.apple.com/documentation/uikit/uitextattachmentviewproviderreusepolicy) for retaining attachment views during editing/scrolling. Apply it with [`UITextView.register(_:forTextAttachmentViewProviderType:)`](https://developer.apple.com/documentation/uikit/uitextview/register(_:fortextattachmentviewprovidertype:)), which requires iOS/iPadOS/Mac Catalyst/tvOS/visionOS 27+. [`NSTextViewportRenderingSurface`](https://developer.apple.com/documentation/uikit/nstextviewportrenderingsurface), a protocol for custom text rendering, explicitly requires version 27 on its listed UIKit platforms.

Compositional-layout section-provider closures now participate in automatic Observation tracking. `UIRefreshControl` and `UIStepper` gain full support in the Mac Catalyst Mac idiom. For SwiftUI-hosted scenes, use [`UIHostingSceneDelegate`](https://developer.apple.com/documentation/swiftui/uihostingscenedelegate), available since iOS/iPadOS/Mac Catalyst/visionOS 26 and newly available on tvOS 27.

### Liquid Glass and validation

[`UIGlassEffect`](https://developer.apple.com/documentation/uikit/uiglasseffect) and [`UIGlassContainerEffect`](https://developer.apple.com/documentation/uikit/uiglasscontainereffect) list iOS/iPadOS/Mac Catalyst/tvOS 26+. [`UIBackgroundExtensionView`](https://developer.apple.com/documentation/uikit/uibackgroundextensionview) also lists visionOS 26+. These are UIKit APIs, not an independent Liquid Glass module or a blanket watchOS/visionOS glass API surface.

Prefer system controls; use custom effects only where the [Liquid Glass adoption guidance](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass) calls for them. See [Bundle Resources](BundleResources.md#ui-design-compatibility) for the exact platforms/build targets where `UIDesignRequiresCompatibility` is ignored; rebuilding with Xcode 27 does not itself forbid deployment to OS 26.

Test scene connection and reconnection, deep links, restoration, background/foreground transitions, window resizing, text selection, and legibility with Reduce Transparency and Increase Contrast. See [XCUIAutomation](XCUIAutomation.md) for test tooling.

Sources: [iOS & iPadOS 27 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes) and [UIKit updates](https://developer.apple.com/documentation/updates/uikit). These are September 2026 beta changes, not a new minimum version for UIKit.

## Topics

### Essentials
- [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass) - Find out how to bring the new material to your app.
- [UIKit updates](https://developer.apple.com/documentation/updates/uikit) - Learn about important changes to UIKit.
- [About App Development with UIKit](https://developer.apple.com/documentation/uikit/about-app-development-with-uikit) - Learn about the basic support that UIKit and Xcode provide for your iOS and tvOS apps.
- [Protecting the User's Privacy](https://developer.apple.com/documentation/uikit/protecting-the-user-s-privacy) - Secure personal data, and respect user preferences for how data is used.

### App Structure
**UIKit** manages your app's interactions with the system and provides classes for you to manage your app's data and resources.

### App and Environment
Manage life-cycle events and your app's UI scenes, and get information about traits and the environment in which your app runs.

### Documents, Data, and Pasteboard
Organize your app's data and share that data on the pasteboard.

### Resource Management
Manage the images, strings, storyboards, and nib files that you use to implement your app's interface.

### App Extensions
Extend your app's basic functionality to other parts of the system.

### Interprocess Communication
Display activity-based services to people.

### Mac Catalyst
Create a version of your iPad app that users can run on a Mac device.

### User Interface
Views help you display content onscreen and facilitate user interactions; view controllers help you manage views and the structure of your interface.

### Views and Controls
Present your content onscreen and define the interactions allowed with that content.

### View Controllers
Manage your interface using view controllers and facilitate navigation around your app's content.

### View Layout
Use stack views to lay out the views of your interface automatically. Use Auto Layout when you require precise placement of your views.

### Appearance Customization
Apply Liquid Glass to views, support Dark Mode in your app, customize the appearance of bars, and use appearance proxies to modify your UI.

### Animation and Haptics
Provide feedback to users using view-based animations and haptics.

### Windows and Screens
Provide a container for your view hierarchies and other content.

### User Interactions
Responders and gesture recognizers help you handle touches and other events. Drag and drop, focus, context menus, and accessibility handle other user interactions.

### Touches, Presses, and Gestures
Encapsulate your app's event-handling logic in gesture recognizers so that you can reuse that code throughout your app.

### Menus and Shortcuts
Simplify interactions with your app using menu systems, contextual menus, Home Screen quick actions, and keyboard shortcuts.

### Drag and Drop
Bring drag and drop to your app by using interaction APIs with your views.

### Pointer Interactions
Support pointer interactions in your custom controls and views.

### Apple Pencil Interactions
Handle user interactions like double tap and squeeze on Apple Pencil.

### Focus-Based Navigation
Navigate the interface of your UIKit app using a remote, game controller, or keyboard.

### Accessibility for UIKit
Make your UIKit apps accessible to everyone who uses iOS and tvOS.

### Graphics, Drawing, and Printing
**UIKit** provides classes and protocols that help you configure your drawing environment and render your content.

### Images and PDF
Create and manage images, including those that use bitmap and PDF formats.

### Drawing
Configure your app's drawing environment using colors, renderers, draw paths, strings, and shadows.

### Printing
Display the system print panels and manage the printing process.

### Text
In addition to text views that simplify displaying text in your app, **UIKit** provides custom text management and rendering that supports the system keyboards.

### Text Display and Fonts
Display text, manage fonts, and check spelling.

### TextKit
Manage text storage and perform custom layout of text-based content in your app's views.

### Keyboards and Input
Configure the system keyboard, create your own keyboards to handle input, or detect key presses on a physical keyboard.

### Writing Tools
Add support for Writing Tools to your app's text views.

### Handwriting Recognition
Configure text fields and custom views that accept text to handle input from Apple Pencil.

### Deprecated
Avoid using deprecated classes and protocols in your apps.

### Deprecated Symbols
Review deprecated symbols and their replacements. Deprecation discourages use; it does not by itself establish removal.

### Reference
- **UIKit Enumerations**
- **UIKit Constants** - This document describes constants that are used throughout the UIKit framework.
- **UIKit Data Types** - The UIKit framework defines data types that are used in multiple places throughout the framework.
- **UIKit Functions** - The UIKit framework defines a number of functions, many of them used in graphics and drawing operations.

### Structures
- [`UICornerConfiguration`](https://developer.apple.com/documentation/uikit/uicornerconfiguration-swift.struct) - Maps corner radii to a rectangle's corners; iOS/iPadOS/Mac Catalyst/tvOS/visionOS 26+.
- [`UICornerRadius`](https://developer.apple.com/documentation/uikit/uicornerradius-swift.struct) - Represents a corner radius, including fixed and container-concentric forms; the same 26+ platform set.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/UIKit)*
