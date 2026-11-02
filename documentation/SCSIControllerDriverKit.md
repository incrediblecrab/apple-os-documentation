# SCSIControllerDriverKit

Develop drivers for SCSI protocol-based devices.

**Platforms:** DriverKit 20.4+

## Overview

The SCSIControllerDriverKit framework supports the development of DriverKit extension (dext) drivers for devices that communicate using SCSI protocols.

Develop your driver by subclassing IOUserSCSIParallelInterfaceController, overriding all methods the framework declares as pure virtual. Then package your driver in an app that uses the System Extensions framework to install and upgrade the driver on the user's Mac.

Match the driver to hardware through the [`IOKitPersonalities`](https://developer.apple.com/documentation/bundleresources/information-property-list/iokitpersonalities) entry in the dext's information property list. Apple requires these keys for this class: `CFBundleIdentifier` (your driver's bundle ID), `CFBundleIdentifierKernel` set to `com.apple.iokit.IOSCSIParallelFamily`, `IOClass` set to `IOUserSCSIParallelInterfaceController`, `IOUserClass` set to your subclass's name, `IOUserServerName` set to your driver's bundle identifier, and `IOProviderClass` set to `IOPCIDevice`. You can add other keys as needed.

**Note:** SCSIControllerDriverKit is available on macOS.

## Topics

### Entitlements
- [com.apple.developer.driverkit](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.driverkit) - A Boolean value that indicates whether your extension has permission to run as a user-space driver.
- [com.apple.developer.driverkit.transport.pci](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.driverkit.transport.pci) - An array of PCI device descriptors that your driver supports.
- **com.apple.developer.driverkit.family.scsicontroller** - A Boolean value that indicates whether to match the driver against devices with SCSI controllers.

### Samples
- [DriverKit sample code](https://developer.apple.com/documentation/driverkit/driverkit-sample-code) - Explore projects that demonstrate how to write macOS device drivers with the DriverKit family of frameworks.

### Driver Interfaces
- **IOUserSCSIParallelInterfaceController** - A DriverKit provider object that manages communications with SCSI-based devices.

### Macros
- [Macros](https://developer.apple.com/documentation/scsicontrollerdriverkit/scsicontrollerdriverkit-macros) - Lists `kIOHierarchicalLogicalUnitSupportKey`, `kIOMinimumHBADataAlignmentMaskKey`, `kIOServicePowerCapabilityPause`, and `kMaxSenseBufferSize`.
- **kMaxBundledParallelTasks** - Still has its own reference page, but Apple's Macros collection no longer lists it.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SCSIControllerDriverKit)*
