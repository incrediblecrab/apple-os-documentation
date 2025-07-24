# System Extensions

Install and manage user space code that extends the capabilities of macOS.

**Platforms:** macOS 10.15+

## Overview

Extend the capabilities of macOS by installing and managing system extensions—drivers and other low-level code—in user space rather than in the kernel. By running in user space, system extensions can't compromise the security or stability of macOS. The system grants these extensions a high level of privilege, so they can perform the kinds of tasks previously reserved for kernel extensions (KEXTs).

You use frameworks like DriverKit, Endpoint Security, and Network Extension to write your system extension, and you package the extension in your app bundle. At runtime, use the SystemExtensions framework to install or update the extension on the user's system. Once installed, an extension remains available for all users on the system. Users can disable the extension by deleting the app, which deletes the extension.

### Configure the System Extension and the Host App

To successfully activate your extension, you must adhere to the following rules:

- The extension must match your bundle identifier, excluding file extension. For example, a DriverKit extension with bundle identifier `com.example.usbdriver` must use the filename `com.example.usbdriver.dext`. Similarly, a NetworkExtension extension with bundle identifier `com.example.networkextension` must use the filename `com.example.networkextension.systemextension`.

- You must use the same Team ID when signing the extension that you use for signing your app, unless the extension has the `com.apple.developer.system-extension.redistributable` entitlement.

- You must either distribute your app and extension through the Mac App Store, or notarize them. See Notarizing macOS software before distribution to learn more about notarization.

## Topics

### Essentials
- [Implementing drivers, system extensions, and kexts](https://developer.apple.com/documentation/systemextensions/implementing_drivers_system_extensions_and_kexts) - Create drivers and system extensions to communicate with hardware and provide low-level services, and only use kernel extensions for a few tasks
- [Debugging and testing system extensions](https://developer.apple.com/documentation/systemextensions/debugging_and_testing_system_extensions) - Debug your system extensions by temporarily disabling the security checks that macOS performs during the installation process
- **System Extension Entitlement** - A Boolean value that indicates whether your app has permission to activate or deactivate system extensions

### Usage Descriptions
- **NSSystemExtensionUsageDescriptionKey** - A message that tells the user why the app is trying to install a system extension bundle
- **OSBundleUsageDescriptionKey** - A message that tells the user why the app is trying to install a driver extension bundle

### Extension Activation and Deactivation
- [Installing System Extensions and Drivers](https://developer.apple.com/documentation/systemextensions/installing_system_extensions_and_drivers) - Activate system extensions and drivers to make them available to the system, and update or deactivate them as needed
- **OSSystemExtensionManager** - A type that facilitates activation and deactivation of system extensions
- **OSSystemExtensionRequest** - A request to activate or deactivate a system extension
- **System Extension Redistributable Entitlement** - A Boolean value that indicates whether other development teams may distribute a system extension you create

### Errors
- **OSSystemExtensionError** - An error that describes a failed extension manager request
- **Code** - Error codes for system extensions
- **OSSystemExtensionErrorDomain** - The error domain identifying system extension errors

### Reference
- **SystemExtensions Constants**

### Classes
- **OSSystemExtensionInfo**
- **OSSystemExtensionsWorkspace**

### Protocols
- **OSSystemExtensionsWorkspaceObserver**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SystemExtensions)*