# SCSIPeripheralsDriverKit

Develop drivers for peripherals that use SCSI Block Command and Multimedia Command protocols.

**Platforms:** DriverKit 22.0+

## Overview

The SCSIPeripheralsDriverKit framework supports the development of drivers for external devices that communicate using SCSI protocols. This framework operates at the logical unit level. For block-level driver development, use BlockStorageDeviceDriverKit. For protocol-level driver development, use SCSIControllerDriverKit.

Develop your driver by subclassing IOUserSCSIPeripheralDeviceType00 or IOUserSCSIPeripheralDeviceType05, depending on whether your device works with SCSI Block Commands (SBC) or SCSI Multimedia Commands (SMC), respectively. In your subclass, override all methods the framework declares as pure virtual. Then package your driver in an app that uses the System Extensions framework to install and upgrade the driver on the user's Mac.

**Note:** SCSIPeripheralsDriverKit is available on macOS.

## Topics

### Driver interfaces
- **IOUserSCSIPeripheralDeviceType00** - A DriverKit provider object that works with type 00 devices, those that use SCSI Block Commands (SBC).
- **IOUserSCSIPeripheralDeviceType05** - A DriverKit provider object that works with type 05 devices, those that use SCSI Multimedia Commands (SMC).

### Device commands
- **SCSI commands** - Call the framework's free functions to populate Command Descriptor Blocks (CDBs) to send to your peripheral.

### Classes
- **IOUserSCSIPeripheralDeviceType07** - Reference

### Reference
- **SCSIPeripheralsDriverKit Enumerations**
- **SCSIPeripheralsDriverKit Data Types**

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SCSIPeripheralsDriverKit)*