# USBSerialDriverKit

Develop drivers for serial USB devices connected to your Mac.

**Platforms:** DriverKit 19.0+

## Overview

Use the USBSerialDriverKit framework to develop drivers that communicate with USB devices using serial protocols. This framework augments the behavior of the SerialDriverKit framework by configuring the buffers and endpoints needed to transfer data to and from the device. You handle the initial configuration of your device, and the framework manages the transfer of data to and from that device.

Package your driver in an app that uses the System Extensions framework to install and upgrade the driver on the user's Mac.

**Note:** USBSerialDriverKit is available on macOS.

## Topics

### Samples
- [DriverKit sample code](https://developer.apple.com/documentation/driverkit/driverkit_sample_code) - Explore projects that demonstrate how to write macOS device drivers with the DriverKit family of frameworks.

### Serial USB Interface
- [com.apple.developer.driverkit.family.serial](https://developer.apple.com/documentation/driverkit/com_apple_developer_driverkit_family_serial) - A Boolean value that indicates whether to match the driver against devices with serial communication interfaces.
- **IOUserUSBSerial** - A service that manages a serial connection to a USB device.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/USBSerialDriverKit)*