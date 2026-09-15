# IOUSBHost

Create host-mode user space drivers for USB devices.

**Platforms:** Mac Catalyst 14.0+ | macOS 10.15+

## Overview

IOUSBHost provides application-side access to custom and non–class-compliant USB devices. Device objects manage configuration and requests; interface objects provide pipes and streams for data transfers. A device being a camera, keyboard, audio interface, or other USB peripheral does not by itself mean an app can take it away from an existing driver.

Apple's reference cites the USB Implementers Forum (USB-IF) USB 3.2 Specification, Revision 1.0, dated September 22, 2017. That identifies the cited specification, not the newest USB standard or a guarantee that every device feature is supported.

### Ownership and transfer lifecycle

Creating an `IOUSBHostDevice` or `IOUSBHostInterface` establishes exclusive ownership of the selected service. Initialization can fail when the service is missing or already has a user client. Monitor service termination, handle transfer errors and disconnects, and call `destroy()` when finished to release the user-client connection and notifications.

A sandboxed app needs Boolean [`com.apple.security.device.usb`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.device.usb) enabled for USB access. That sandbox permission is separate from exclusive device-capture authorization and from the macOS 27 AccessoryAccess entitlement.

`IOUSBHostObject` sends device requests to the default control endpoint; `IOUSBHostPipe` also supports control transfers on control endpoints, in addition to bulk, interrupt, and isochronous I/O. Synchronous control requests block until completion, and a completion timeout of zero disables the timeout rather than requesting an immediate failure.

For native macOS's legacy device-capture option, a non-root caller needs Boolean [`com.apple.vm.device-access`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.vm.device-access) and successful `IOServiceAuthorize` authorization. Capture terminates other device/interface clients and drivers; it is not ordinary discovery or a general permission to claim any peripheral. The macOS 26.5 SDK documents a root-privilege exception to those two checks, not a requirement to run ordinary USB apps as root.

### macOS 27 accessory access

**Reviewed September 8, 2026:** [AccessoryAccess](AccessoryAccess.md) adds a macOS 27 workflow for matching connected USB accessories and coordinating exclusive access for IOUSBHost clients. It requires Boolean [`com.apple.developer.accessory-access.usb`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.accessory-access.usb) set to `true` and a UI application that appears in the Dock, not a background-only service. Missing the entitlement produces an AccessoryAccess `internalError` with “Unable to communicate with service.” This is not a blanket deprecation of IOUSBHost.

Discovery does not guarantee that an accessory can be opened. Handle exclusive-use conflicts, disconnection, and failed transfers, and keep the new manager's availability separate from IOUSBHost's older minimum versions.

## Topics

### Function Drivers
- **IOUSBHostInterface** - The class for accessing USB-related services.
- **IOUSBHostPipe** - The class that sends control, bulk, interrupt, and isochronous input/output requests for function drivers, and manages stream capabilities.
- **IOUSBHostStream** - The class responsible for sending stream data for function drivers.

### Device Drivers
- **IOUSBHostDevice** - The class that claims and configures devices, retrieves descriptors, and sends device requests.

### Base Classes
- **IOUSBHostObject** - This class provides basic functionality for sending device requests and retrieving descriptors.
- **IOUSBHostIOSource** - Base for pipe and stream objects. Do not instantiate or subclass it directly; obtain concrete objects through `copyPipe(withAddress:)` and `copyStream(withStreamID:)`.

### IOServicePlane Properties
Properties on the device and interface classes in the service plane.

- **IOUSBHostInterfacePropertyKey** - Properties of a USB interface that describe its state.
- **IOUSBHostDevicePropertyKey** - Properties of a USB device that describe its state.
- **IOUSBHostMatchingPropertyKey** - Properties for implementing the matching service.
- **IOUSBHostPropertyKey** - Properties that the USB host device and interface classes share.

### Error Domain
- **IOUSBHostErrorDomain** - The error domain for the framework.

### Classes
- **IOUSBHostCIControllerStateMachine**
- **IOUSBHostCIDeviceStateMachine**
- **IOUSBHostCIEndpointStateMachine**
- **IOUSBHostCIPortStateMachine**
- [IOUSBHostControllerInterface](https://developer.apple.com/documentation/iousbhost/iousbhostcontrollerinterface) - Creates a user-mode host controller for remote or synthetic USB devices. This is distinct from opening a physical device and requires the separate `com.apple.developer.usb.host-controller-interface` entitlement documented in its public SDK header.

### Reference
- **IOUSBHost Structures**
- **IOUSBHost Enumerations**
- **IOUSBHost Constants**
- **IOUSBHost Functions**
- **IOUSBHost Data Types**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/IOUSBHost)*

*27 source: [AAUSBAccessoryManager](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymanager.md).*
