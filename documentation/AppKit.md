# AppKit

Construct and manage a graphical, event-driven user interface for your macOS app.

**Platforms:** Mac Catalyst 13.0+ | macOS 10.0+

## Overview

AppKit contains the objects you need to build the user interface for a macOS app. In addition to drawing windows, buttons, panels, and text fields, it handles all the event management and interaction between your app, people, and macOS.

Aside from drawing and managing interactions, AppKit handles printing, animating, as well as creating documents with large amounts of data efficiently. The framework also contains built-in support for localization and accessibility to ensure that your app reaches as many people as possible.

AppKit also works with SwiftUI, so you can implement parts of your AppKit app in SwiftUI or mix interface elements between the two frameworks. For example, you can place AppKit views and view controllers inside SwiftUI views, and vice versa.

**Note:** For information about bringing your iPad app to Mac, see Mac Catalyst. To build an iOS app, you can use SwiftUI to create an app that works across all of Apple's platforms, or use UIKit to create an app for iOS only.

## Topics

### Essentials
- [Adopting Liquid Glass](https://developer.apple.com/documentation/appkit/adopting_liquid_glass) - Find out how to bring the new material to your app.
- [AppKit updates](https://developer.apple.com/documentation/appkit/appkit_updates) - Learn about important changes to AppKit.
- [Protecting the User's Privacy](https://developer.apple.com/documentation/appkit/protecting_the_user_s_privacy) - Secure personal data, and respect user preferences for how data is used.
- [Porting your macOS apps to Apple silicon](https://developer.apple.com/documentation/apple_silicon/porting_your_macos_apps_to_apple_silicon) - Create a version of your macOS app that runs on both Apple silicon and Intel-based Mac computers.

### App Structure
- [App and Environment](https://developer.apple.com/documentation/appkit/app_and_environment) - Learn about the objects that you use to interact with the system.
- [Documents, Data, and Pasteboard](https://developer.apple.com/documentation/appkit/documents_data_and_pasteboard) - Organize your app's data and preferences, and share that data on the pasteboard or in iCloud.
- [Cocoa Bindings](https://developer.apple.com/documentation/appkit/cocoa_bindings) - Automatically synchronize your data model with your app's interface using Cocoa Bindings.
- [Resource Management](https://developer.apple.com/documentation/appkit/resource_management) - Manage the storyboards and nib files containing your app's user interface, and learn how to load data that is stored in resource files.
- [App Extensions](https://developer.apple.com/documentation/appkit/app_extensions) - Extend your app's basic functionality to other parts of the system.

### User Interface
- [Views and Controls](https://developer.apple.com/documentation/appkit/views_and_controls) - Present your content onscreen and handle user input and events.
- [View Management](https://developer.apple.com/documentation/appkit/view_management) - Manage your user interface, including the size and position of views in a window.
- [View Layout](https://developer.apple.com/documentation/appkit/view_layout) - Position and size views using a stack view or Auto Layout constraints.
- [Appearance Customization](https://developer.apple.com/documentation/appkit/appearance_customization) - Add Dark Mode support to your app, and use appearance proxies to modify your UI.
- [Animation](https://developer.apple.com/documentation/appkit/animation) - Animate your views and other content to create a more engaging experience for users.
- [Windows, Panels, and Screens](https://developer.apple.com/documentation/appkit/windows_panels_and_screens) - Organize your view hierarchies and facilitate their display onscreen.
- [Sound, Speech, and Haptics](https://developer.apple.com/documentation/appkit/sound_speech_and_haptics) - Play sounds and haptic feedback, and incorporate speech recognition and synthesis into your interface.
- [Supporting Continuity Camera in Your Mac App](https://developer.apple.com/documentation/appkit/supporting_continuity_camera_in_your_mac_app) - Incorporate scanned documents and pictures from a user's iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.

### User Interactions
- [Mouse, Keyboard, and Trackpad](https://developer.apple.com/documentation/appkit/mouse_keyboard_and_trackpad) - Handle events related to mouse, keyboard, and trackpad input.
- [Menus, Cursors, and the Dock](https://developer.apple.com/documentation/appkit/menus_cursors_and_the_dock) - Implement menus and cursors to facilitate interactions with your app, and use your app's Dock tile to convey updated information.
- [Gestures](https://developer.apple.com/documentation/appkit/gestures) - Encapsulate your app's event-handling logic in gesture recognizers so that you can reuse that code throughout your app.
- [Touch Bar](https://developer.apple.com/documentation/appkit/touch_bar) - Display interactive content and controls in the Touch Bar.
- [Drag and Drop](https://developer.apple.com/documentation/appkit/drag_and_drop) - Support the direct manipulation of your app's content using drag and drop.
- [Accessibility for AppKit](https://developer.apple.com/documentation/appkit/accessibility_for_appkit) - Make your AppKit apps accessible to everyone who uses macOS.

### Graphics, Drawing, Color, and Printing
- [Images and PDF](https://developer.apple.com/documentation/appkit/images_and_pdf) - Create and manage images, in bitmap, PDF, and other formats.
- [Drawing](https://developer.apple.com/documentation/appkit/drawing) - Draw shapes, images, and other content on the screen.
- [Color](https://developer.apple.com/documentation/appkit/color) - Represent colors using built-in or custom formats, and give users options for selecting and applying colors.
- [Printing](https://developer.apple.com/documentation/appkit/printing) - Display the system print panels and manage the printing process.

### Text
- [Text Display](https://developer.apple.com/documentation/appkit/text_display) - Display text and check spelling.
- [TextKit](https://developer.apple.com/documentation/appkit/textkit) - Manage text storage and perform custom layout of text-based content in your app's views.
- [Fonts](https://developer.apple.com/documentation/appkit/fonts) - Manage the fonts used to display text.
- [Writing Tools](https://developer.apple.com/documentation/appkit/writing_tools) - Add support for Writing Tools to your app's text views.

### Deprecated
- [Deprecated Symbols](https://developer.apple.com/documentation/appkit/deprecated_symbols) - Review symbols that are no longer supported, and find the replacements to use instead.

### Reference
- [Enumerations](https://developer.apple.com/documentation/appkit/enumerations) - Enumerations for use with multiple classes.
- [Constants](https://developer.apple.com/documentation/appkit/constants) - Constants for use with multiple classes.
- [Data Types](https://developer.apple.com/documentation/appkit/data_types) - Data types for use with multiple classes.
- [Macros](https://developer.apple.com/documentation/appkit/macros) - Macros for use with multiple classes.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AppKit)*