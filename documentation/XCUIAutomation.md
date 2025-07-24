# XCUIAutomation

Replicate sequences of interactions and make sure that your app's user interface behaves as intended.

**Platforms:** Xcode 16.3+

## Overview

UI testing lets you verify that when you change parts of your app's data model, your app's view controllers, views, and controls respond appropriately. You can also create test cases to manipulate your app's views and controls, as if a person is interacting with your interface. Use the XCUIAutomation framework to control your app's user interface and inspect its state. Use XCTest to write tests that control your app using XCUIAutomation, and check if your app's state matches your expectations.

Note

UI testing isn't available to apps you build using the visionOS SDK. You can still use it to test compatible iPad and iPhone apps that you build using the iOS SDK but run in visionOS.

## Topics

### Essentials
- [Recording UI automation for testing](https://developer.apple.com/documentation/xcuiautomation/recording_ui_automation_for_testing) - Capture and replay interaction sequences to verify your app's behavior.

### UI element queries
- **XCUIElementQuery** - An object that defines the search criteria a test uses to identify UI elements.
- **XCUIElementTypeQueryProvider** - A type that provides ready-made queries for locating descendant UI elements.

### UI elements
- **XCUIElement** - A UI element in an application.
- **XCUIElementAttributes** - Attributes exposed by UI elements.
- **XCUIElementSnapshot** - A set of attributes to express a snapshot of an element's attributes and descendant user interface hierarchy.
- **XCUIElementSnapshotProviding** - A method to capture a snapshot of an element's attributes and descendant user interface hierarchy.
- **XCUICoordinate** - A location on screen relative to a UI element.

### Application lifecycle
- **XCUIApplication** - A proxy that can launch, monitor, and terminate a test application.

### Screenshots
- **XCUIScreen** - A physical screen attached to a device.
- **XCUIScreenshot** - A captured image of a screen, app, or UI element state.
- **XCUIScreenshotProviding** - A type that can provide a screenshot of its current UI state.

### Device simulation
- **XCUIDevice** - A proxy that can simulate physical buttons, device orientation, and Siri interaction for an iOS, watchOS, or tvOS device.
- **XCUISystem** - A proxy that provides an interface to OS-specific properties and actions.
- **XCUISiriService** - A proxy that simulates a device's Siri interface.

### Remote control simulation
- **XCUIRemote** - A class that simulates interaction with a physical remote control.

### UI testing availability
- **XCUI_UI_TESTING_AVAILABLE** - Indicates whether the current environment supports UI testing.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/XCUIAutomation)*
