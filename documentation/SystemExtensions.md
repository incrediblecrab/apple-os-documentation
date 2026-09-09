# System Extensions

Install and manage user space code that extends the capabilities of macOS.

**Platforms:** macOS 10.15+

## Overview

Extend macOS with system extensions—drivers and other low-level code—running in user space rather than the kernel. This reduces the impact of faults compared with kernel extensions, but does not make an extension incapable of affecting security or stability. Its entitlements, input validation, resource use, and failure handling still matter.

You use frameworks like DriverKit, Endpoint Security, and Network Extension to write your system extension, and you package the extension in your app bundle. At runtime, use the SystemExtensions framework to install or update the extension on the user's system. Installation is system-wide rather than per user. Apple's installation guide also documents deleting the containing app as an uninstallation path; neither the bundle's presence nor an activation request alone proves that its services are running.

### Configure the System Extension and the Host App

To successfully activate your extension, you must adhere to the following rules:

- Put the extension in the containing app's `Contents/Library/SystemExtensions` directory and install the app in an appropriate Applications directory.

- The extension's filename, excluding its suffix, must match the **extension's** bundle identifier, not the containing app's identifier. For example, a DriverKit extension with bundle identifier `com.example.usbdriver` uses `com.example.usbdriver.dext`; a network system extension with identifier `com.example.networkextension` uses `com.example.networkextension.systemextension`.

- Enable Boolean [`com.apple.developer.system-extension.install`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.system-extension.install) on the containing app. Sign the app and extension with the same Team ID unless the **extension** has Boolean [`com.apple.developer.system-extension.redistributable`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.system-extension.redistributable) enabled.

- You must either distribute your app and extension through the Mac App Store, or notarize them. See Notarizing macOS software before distribution to learn more about notarization.

- Include the required usage-description **string in the extension's Info.plist**: [`NSSystemExtensionUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nssystemextensionusagedescription) for non-DriverKit system extensions, or [`OSBundleUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/osbundleusagedescription) for DriverKit extensions. Missing it fails activation. The exported constants below end in `Key`; the actual plist names do not.

### Activation, refusal, and removal

Submit an `OSSystemExtensionRequest` and handle its delegate lifecycle. [`requestNeedsUserApproval(_:)`](https://developer.apple.com/documentation/systemextensions/ossystemextensionrequestdelegate/requestneedsuserapproval(_:)) means activation is pending until the user grants or denies permission, or the app quits.

In the completion callback, distinguish `.completed` from [`.willCompleteAfterReboot`](https://developer.apple.com/documentation/systemextensions/ossystemextensionrequest/result/willcompleteafterreboot). The latter does not make the extension active immediately; the most recently processed request determines its state after restarting. Handle failures rather than reporting a pending or refused request as successful.

For updates, increment the extension's version and handle the replacement delegate decision. The manager compares `CFBundleVersion` and `CFBundleShortVersionString`; returning `.cancel` aborts the replacement with `requestCanceled`.

Entitlements are checked against the code signature and the development team's grants. A containing app's System Extension capability does not replace the driver, Endpoint Security, or Network Extension entitlements required by its extension.

Use a deactivation request to remove an extension when appropriate, and handle loss of its services. The 27 beta [VideoDriverKit](VideoDriverKit.md) family uses this macOS activation model; it does not add general iPadOS SystemExtensions support.

The workspace, extension-info, and workspace-observer APIs are macOS 15.1+, not the framework's original 10.15 baseline. Workspace access requires the System Extension entitlement. Availability metadata on inspection APIs or constants does not extend the macOS manager/request activation model to iPadOS.

## Topics

### Essentials
- [Implementing drivers, system extensions, and kexts](https://developer.apple.com/documentation/kernel/implementing_drivers_system_extensions_and_kexts) - Choose user-space drivers or system extensions where suitable, retaining kernel extensions only for functionality that requires them.
- [Debugging and testing system extensions](https://developer.apple.com/documentation/driverkit/debugging-and-testing-system-extensions) - Development-only testing options; restore normal validation before final testing and distribution.
- [System Extension Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.system-extension.install) - A Boolean value that permits the containing app to activate or deactivate system extensions.

### Usage Descriptions
- **NSSystemExtensionUsageDescriptionKey** - A message that tells the user why the app is trying to install a system extension bundle
- **OSBundleUsageDescriptionKey** - A message that tells the user why the app is trying to install a driver extension bundle

### Extension Activation and Deactivation
- [Installing System Extensions and Drivers](https://developer.apple.com/documentation/systemextensions/installing-system-extensions-and-drivers) - Activation, updates, failure handling, and deactivation.
- **OSSystemExtensionManager** - A type that facilitates activation and deactivation of system extensions
- **OSSystemExtensionRequest** - A request to activate or deactivate a system extension
- **System Extension Redistributable Entitlement** - A Boolean value that indicates whether other development teams may distribute a system extension you create

### Errors
- **OSSystemExtensionError** - An error that describes a failed extension manager request
- [OSSystemExtensionError.Code](https://developer.apple.com/documentation/systemextensions/ossystemextensionerror/code) - Error codes for system extensions.
- **OSSystemExtensionErrorDomain** - The error domain identifying system extension errors

### Reference
- **SystemExtensions Constants**

### Classes
- [OSSystemExtensionInfo](https://developer.apple.com/documentation/systemextensions/ossystemextensioninfo) - Extension information; macOS 15.1+.
- [OSSystemExtensionsWorkspace](https://developer.apple.com/documentation/systemextensions/ossystemextensionsworkspace) - Entitlement-gated workspace inspection; macOS 15.1+.

### Protocols
- [OSSystemExtensionsWorkspaceObserver](https://developer.apple.com/documentation/systemextensions/ossystemextensionsworkspaceobserver) - Workspace change observation; macOS 15.1+.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SystemExtensions)*

*Changed-content sources, reviewed September 8, 2026: [installation lifecycle](https://developer.apple.com/documentation/systemextensions/installing-system-extensions-and-drivers.md) and [request delegate](https://developer.apple.com/documentation/systemextensions/ossystemextensionrequestdelegate.md).*
