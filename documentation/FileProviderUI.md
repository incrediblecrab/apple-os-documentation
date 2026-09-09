# File Provider UI

Add actions to the document browser's context menu.

**Platforms:** iOS 11.0+ | iPadOS 11.0+ | Mac Catalyst 15.0+ | macOS 10.15+ | visionOS 1.0+

## Overview

Use a File Provider UI extension to present custom actions from the file browser's context menu. Define actions in `NSExtensionFileProviderActions`, including an identifier, localized name, and activation predicate. An action without a predicate isn't displayed; `TRUEPREDICATE` makes it eligible regardless of the selected items.

Provide one `FPUIActionExtensionViewController` subclass and configure each selected action in `prepare(forAction:itemIdentifiers:)`. Finish through the extension context's `completeRequest()` or `cancelRequest(withError:)`; merely hiding your view doesn't complete the request.

On macOS 11+, [FileProvider](FileProvider.md) also supports custom actions performed directly by the provider without additional UI. That is a separate workflow from this UI extension.

The published Catalyst minima are inconsistent: the framework catalog says 15, while the controller and error declarations say 11. The header preserves the framework catalog rather than treating that earlier symbol label as a reliable deployment target.

For extension architecture, see the archived [App Extension Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html).

## Topics

### Document Browser Customization
- [Adding Actions to the Context Menu](https://developer.apple.com/documentation/fileproviderui/adding-actions-to-the-context-menu) - Configure action metadata, predicates, presentation, and completion.
- [`FPUIActionExtensionViewController`](https://developer.apple.com/documentation/fileproviderui/fpuiactionextensionviewcontroller) - Subclass this controller to present the selected action.

### Errors
- [`FPUIExtensionErrorCode`](https://developer.apple.com/documentation/fileproviderui/fpuiextensionerrorcode) - Error codes distinguishing failure and user cancellation.
- [`FPUIErrorDomain`](https://developer.apple.com/documentation/fileproviderui/fpuierrordomain) - The extension's error-domain string.

### Reference
- [FileProviderUI Data Types](https://developer.apple.com/documentation/fileproviderui/fileproviderui-data-types) - The action identifier and related reference macros.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/FileProviderUI)*
