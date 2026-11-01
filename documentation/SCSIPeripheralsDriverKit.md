# SCSIPeripheralsDriverKit

Develop drivers for peripherals that use SCSI Block Command and Multimedia Command protocols.

**Platforms:** DriverKit 22.0+

## Overview

The SCSIPeripheralsDriverKit framework supports the development of drivers for external devices that communicate using SCSI protocols. This framework operates at the logical unit level. For block-level driver development, use BlockStorageDeviceDriverKit. For protocol-level driver development, use SCSIControllerDriverKit.

The framework covers three SCSI peripheral device types: Type00 block storage devices that use SCSI Block Commands (SBC), such as magnetic disks and solid-state drives; Type05 multimedia devices that use SCSI Multimedia Commands (SMC), such as CD-ROM and DVD-ROM drives; and Type07 optical memory devices that use an extended form of SBC, such as erasable or rewritable optical disk drives. Develop your driver by subclassing IOUserSCSIPeripheralDeviceType00, IOUserSCSIPeripheralDeviceType05, or IOUserSCSIPeripheralDeviceType07 to match the device type. In your subclass, override all methods the framework declares as pure virtual. Then package your driver in an app that uses the System Extensions framework to install and upgrade the driver on the user's Mac.

To match the driver to hardware, add an `IOKitPersonalities` entry to the driver extension's information property list. For all three classes, Apple requires `CFBundleIdentifier`, `CFBundleIdentifierKernel` (`com.apple.iokit.IOSCSIBlockCommandsDevice` for Type00 and Type07, `com.apple.iokit.IOSCSIMultimediaCommandsDevice` for Type05), `IOClass` (the framework class you subclass), `IOUserClass` (your driver extension's class), `IOUserServerName` (your driver's bundle identifier), `IOProviderClass` (`IOSCSIPeripheralDeviceNub`), and the peripheral device type (`0`, `5`, or `7`, under the `Peripheral Device Type` key in Apple's example). Add other keys as your driver needs them.

**Note:** SCSIPeripheralsDriverKit is available on macOS.

## Topics

### Entitlements
- [com.apple.developer.driverkit](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.driverkit) - Grants an extension permission to run as a user-space driver.
- [com.apple.developer.driverkit.family.scsicontroller](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.driverkit.family.scsicontroller) - Matches the driver against devices with SCSI controllers.

### Driver interfaces
- **IOUserSCSIPeripheralDeviceType00** - A DriverKit provider object that works with type 00 devices, those that use SCSI Block Commands (SBC).
- **IOUserSCSIPeripheralDeviceType05** - A DriverKit provider object that works with type 05 devices, those that use SCSI Multimedia Commands (SMC).
- [IOUserSCSIPeripheralDeviceType07](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype07) - A DriverKit provider object for type 07 optical memory devices, which use extended SCSI Block Commands (SBC). Its command parameter and interface-version types, `SCSIType07InParameters`, `SCSIType07OutParameters`, `SCSIType07InVersion`, and `SCSIType07OutVersion`, are listed on the class page.

### Device commands
- **SCSI commands** - Call the framework's free functions to populate Command Descriptor Blocks (CDBs) to send to your peripheral.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SCSIPeripheralsDriverKit)*
