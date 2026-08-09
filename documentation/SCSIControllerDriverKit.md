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

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SCSIControllerDriverKit)*