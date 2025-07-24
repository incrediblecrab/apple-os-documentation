# SCSIControllerDriverKit

Develop drivers for SCSI protocol-based devices.

**Platforms:** DriverKit 20.4+

## Overview

The SCSIControllerDriverKit framework supports the development of DriverKit extension (dext) drivers for devices that communicate using SCSI protocols.

Develop your driver by subclassing IOUserSCSIParallelInterfaceController, overriding all methods the framework declares as pure virtual. Then package your driver in an app that uses the System Extensions framework to install and upgrade the driver on the user's Mac.

**Note:** SCSIControllerDriverKit is available on macOS.

## Topics

### Essentials
- **com.apple.developer.driverkit.family.scsicontroller** - A Boolean value that indicates whether to match the driver against devices with SCSI controllers.

### Samples
- [DriverKit sample code](https://developer.apple.com/documentation/driverkit/samples) - Explore projects that demonstrate how to write macOS device drivers with the DriverKit family of frameworks.

### Driver Interfaces
- **IOUserSCSIParallelInterfaceController** - A DriverKit provider object that manages communications with SCSI-based devices.

### Macros
- **kMaxBundledParallelTasks** - Macros

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SCSIControllerDriverKit)*