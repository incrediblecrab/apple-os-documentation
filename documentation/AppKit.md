# AppKit

Construct and manage a graphical, event-driven user interface for your macOS app.

**Platforms:** macOS 10.0+ for the AppKit app/interface model.

The framework catalog also lists Mac Catalyst 13.0, but [`NSApplication`](https://developer.apple.com/documentation/appkit/nsapplication) and [`NSView`](https://developer.apple.com/documentation/appkit/nsview) are documented as macOS APIs. That aggregate catalog label is not permission to use the macOS app/view model in a Catalyst app; follow individual declarations and the UIKit-based [Mac Catalyst](https://developer.apple.com/documentation/uikit/mac-catalyst) guidance.

## Overview

AppKit contains the objects you need to build the user interface for a macOS app. In addition to drawing windows, buttons, panels, and text fields, it handles all the event management and interaction between your app, people, and macOS.

Aside from drawing and managing interactions, AppKit handles printing, animating, as well as creating documents with large amounts of data efficiently. The framework also contains built-in support for localization and accessibility to ensure that your app reaches as many people as possible.

AppKit also works with SwiftUI, so you can implement parts of your AppKit app in SwiftUI or mix interface elements between the two frameworks. For example, you can place AppKit views and view controllers inside SwiftUI views, and vice versa.

**Note:** Mac Catalyst brings UIKit-based iPad apps to Mac. SwiftUI spans Apple's platforms, while UIKit supports interfaces on iOS, iPadOS, tvOS, and visionOS as well as Catalyst; it is not an iOS-only framework.

## macOS 27 migration

### Controls, input, and observation

- [`NSRefreshController`](https://developer.apple.com/documentation/appkit/nsrefreshcontroller) adds pull-to-refresh to `NSScrollView` on macOS 27. Set `refreshController`, handle the target/action, and call `endRefreshing` when the work completes.
- [`NSTextSelectionManager`](https://developer.apple.com/documentation/appkit/nstextselectionmanager) coordinates selection gestures in custom text views on macOS 27. `NSTextView` now uses gesture recognizers while retaining a compatibility path for existing `mouseDown:` overrides.
- [`NSControl.Events`](https://developer.apple.com/documentation/appkit/nscontrol/events) is highlighted in the June 2026 update, but its current type declaration lists macOS 11+. [`NSView.beginDraggingSession(items:gesture:source:)`](https://developer.apple.com/documentation/appkit/nsview/begindraggingsession(items:gesture:source:)) requires macOS 27. Adopt recognizers for [Sidecar touch input](https://developer.apple.com/documentation/technotes/tn3212-adopting-gesture-recognizers-for-sidecar-touch-support) from an iPad running iPadOS 27 rather than assuming every interaction originates as a mouse event.
- Review [automatic Observation tracking in AppKit](https://developer.apple.com/documentation/appkit/updating-views-automatically-with-observation-tracking-in-appkit) so observable-model changes invalidate the appropriate view work. This integration predates 27: macOS 15 requires opting in with `NSObservationTrackingEnabled`; supported drawing/layout/constraint hooks, not arbitrary closures, perform the tracking.
- `NSToolbarItemGroup.role` and `NSSegmentedControl.role` distinguish navigation tabs from value selection. The tab role changes VoiceOver semantics as well as appearance.

### Menus, panels, and compatibility

Menu image behavior depends on **both the runtime and the linked SDK**. The macOS 27 beta notes initially describe hiding symbol images for apps linked on macOS 26 or later; a subsequent resolved entry extends automatic hiding to non-symbol images for apps linked with the macOS 27 SDK. Older-linked apps retain compatibility behavior. Use [`NSMenuItem.preferredImageVisibility`](https://developer.apple.com/documentation/appkit/nsmenuitem/preferredimagevisibility) for necessary exceptions, especially image-only items, and consult the [menu HIG](https://developer.apple.com/design/human-interface-guidelines/menus).

The notes also describe the “macOS 26.0 only” image checkbox for xib-created items and automatically supplied images for common system items such as Settings, Share, and Print. Don't replace these qualified defaults with a rule that every menu image is hidden.

Retest open/save-panel keyboard navigation, content-type filters, and filename extensions. The beta notes classify several panel problems as **resolved issues**, not enduring limitations. In macOS 27 SDK builds, `NSTextView` moves Layout Orientation into the Font submenu, and `NSTitlebarAccessoryViewController` allows out-of-bounds drawing by default (with clipping during some reveal/hidden transitions).

SwiftUI controls are not guaranteed to retain an AppKit implementation detail: the macOS 27 notes say bordered SwiftUI `Menu`/`Picker` controls no longer use `NSPopUpButton`, and `Slider` no longer uses `NSSlider`. Avoid introspection that depends on those private view arrangements. [`NSHostingSceneRepresentation`](https://developer.apple.com/documentation/swiftui/nshostingscenerepresentation), available from macOS 26, remains the supported bridge for SwiftUI scenes in an AppKit-lifecycle app.

### Build host and design

[Xcode 27 beta 6](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes) requires an **Apple silicon Mac running macOS Tahoe 26.4 or later**, not macOS 27. Its host restriction does not prohibit building Universal output for supported older deployment targets. The build host, output architecture, SDK, and deployment target are separate choices; see [Xcode](Xcode.md) for the toolchain matrix.

`NSGlassEffectView`, `NSGlassEffectContainerView`, and `NSBackgroundExtensionView` arrived in macOS 26. Follow [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass), test Reduce Transparency and Increase Contrast, and review custom window chrome without relying on a fixed blur or highlight recipe. [Bundle Resources](BundleResources.md#ui-design-compatibility) documents the compatibility key's build-target limits.

Sources: [AppKit updates](https://developer.apple.com/documentation/updates/appkit) and [macOS 27 release notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes), reviewed for the September 2026 betas. New symbols have their own availability; AppKit's minimum remains unchanged.

## Topics

### Essentials
- [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass) - Find out how to bring the new material to your app.
- [AppKit updates](https://developer.apple.com/documentation/updates/appkit) - Learn about important changes to AppKit.
- [Protecting the User's Privacy](https://developer.apple.com/documentation/uikit/protecting-the-user-s-privacy) - Secure personal data, and respect user preferences for how data is used.
- [Porting your macOS apps to Apple silicon](https://developer.apple.com/documentation/apple-silicon/porting-your-macos-apps-to-apple-silicon) - Create a version of your macOS app that runs on both Apple silicon and Intel-based Mac computers.

### App Structure
- [App and Environment](https://developer.apple.com/documentation/appkit/app-and-environment) - Learn about the objects that you use to interact with the system.
- [Documents, Data, and Pasteboard](https://developer.apple.com/documentation/appkit/documents-data-and-pasteboard) - Organize your app's data and preferences, and share that data on the pasteboard or in iCloud.
- [Cocoa Bindings](https://developer.apple.com/documentation/appkit/cocoa-bindings) - Automatically synchronize your data model with your app's interface using Cocoa Bindings.
- [Resource Management](https://developer.apple.com/documentation/appkit/resource-management) - Manage the storyboards and nib files containing your app's user interface, and learn how to load data that is stored in resource files.
- [App Extensions](https://developer.apple.com/documentation/appkit/app-extensions) - Extend your app's basic functionality to other parts of the system.

### User Interface
- [Views and Controls](https://developer.apple.com/documentation/appkit/views-and-controls) - Present your content onscreen and handle user input and events.
- [View Management](https://developer.apple.com/documentation/appkit/view-management) - Manage your user interface, including the size and position of views in a window.
- [View Layout](https://developer.apple.com/documentation/appkit/view-layout) - Position and size views using a stack view or Auto Layout constraints.
- [Appearance Customization](https://developer.apple.com/documentation/appkit/appearance-customization) - Add Dark Mode support to your app, and use appearance proxies to modify your UI.
- [Animation](https://developer.apple.com/documentation/appkit/animation) - Animate your views and other content to create a more engaging experience for users.
- [Windows, Panels, and Screens](https://developer.apple.com/documentation/appkit/windows-panels-and-screens) - Organize your view hierarchies and facilitate their display onscreen.
- [Sound, Speech, and Haptics](https://developer.apple.com/documentation/appkit/sound-speech-and-haptics) - Play sounds and haptic feedback, and incorporate speech recognition and synthesis into your interface.
- [Supporting Continuity Camera in Your Mac App](https://developer.apple.com/documentation/appkit/supporting-continuity-camera-in-your-mac-app) - Incorporate scanned documents and pictures from a user's iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.

### User Interactions
- [Mouse, Keyboard, and Trackpad](https://developer.apple.com/documentation/appkit/mouse-keyboard-and-trackpad) - Handle events related to mouse, keyboard, and trackpad input.
- [Menus, Cursors, and the Dock](https://developer.apple.com/documentation/appkit/menus-cursors-and-the-dock) - Implement menus and cursors to facilitate interactions with your app, and use your app's Dock tile to convey updated information.
- [Gestures](https://developer.apple.com/documentation/appkit/gestures) - Encapsulate your app's event-handling logic in gesture recognizers so that you can reuse that code throughout your app.
- [Touch Bar](https://developer.apple.com/documentation/appkit/touch-bar) - Display interactive content and controls in the Touch Bar.
- [Drag and Drop](https://developer.apple.com/documentation/appkit/drag-and-drop) - Support the direct manipulation of your app's content using drag and drop.
- [Accessibility for AppKit](https://developer.apple.com/documentation/appkit/accessibility-for-appkit) - Make your AppKit apps accessible to everyone who uses macOS.

### Graphics, Drawing, Color, and Printing
- [Images and PDF](https://developer.apple.com/documentation/appkit/images-and-pdf) - Create and manage images, in bitmap, PDF, and other formats.
- [Drawing](https://developer.apple.com/documentation/appkit/drawing) - Draw shapes, images, and other content on the screen.
- [Color](https://developer.apple.com/documentation/appkit/color) - Represent colors using built-in or custom formats, and give users options for selecting and applying colors.
- [Printing](https://developer.apple.com/documentation/appkit/printing) - Display the system print panels and manage the printing process.

### Text
- [Text Display](https://developer.apple.com/documentation/appkit/text-display) - Display text and check spelling.
- [TextKit](https://developer.apple.com/documentation/appkit/textkit) - Manage text storage and perform custom layout of text-based content in your app's views.
- [Fonts](https://developer.apple.com/documentation/appkit/fonts) - Manage the fonts used to display text.
- [Writing Tools](https://developer.apple.com/documentation/appkit/writing-tools) - Add support for Writing Tools to your app's text views.

### Deprecated
- [Deprecated Symbols](https://developer.apple.com/documentation/appkit/deprecated-symbols) - Review discouraged APIs and recommended replacements; deprecation is not itself removal.

### Reference
- [Enumerations](https://developer.apple.com/documentation/appkit/enumerations) - Enumerations for use with multiple classes.
- [Constants](https://developer.apple.com/documentation/appkit/constants) - Constants for use with multiple classes.
- [Data Types](https://developer.apple.com/documentation/appkit/data-types) - Data types for use with multiple classes.
- [Macros](https://developer.apple.com/documentation/appkit/macros) - Macros for use with multiple classes.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AppKit)*
