# File Provider UI

Add actions to the document browser's context menu.

**Platforms:** iOS 11.0+ | iPadOS 11.0+ | Mac Catalyst 15.0+ | macOS 10.15+ | visionOS 1.0+

## Overview

Use the File Provider UI extension to add custom actions to your File Provider extension. These actions appear if the user long presses an item while browsing your file provider's content. When the user selects your action, the system displays your custom user interface, where the user completes the action. After the user is finished, you must explicitly cancel or complete the action.

For more about File Provider extensions, see File Provider.

For more about creating extensions, see App Extension Programming Guide.

## Topics

### Document Browser Customization
- [Adding Actions to the Context Menu](https://developer.apple.com/documentation/fileproviderui/adding_actions_to_the_context_menu) - Present custom actions from your File Provider extension in the system's file browser.
- **class FPUIActionExtensionViewController** - The custom user interface used to perform a selected action.

### Errors
- **enum FPUIExtensionErrorCode** - The error codes for errors raised by the File Provider UI extension.
- **let FPUIErrorDomain: String** - The error domain for errors raised by the File Provider UI extension.

### Reference
- **FileProviderUI Data Types**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/FileProviderUI)*