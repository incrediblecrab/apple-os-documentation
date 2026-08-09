# BlockStorageDeviceDriverKit

Develop drivers for custom storage devices that communicate with the driver using custom protocols.

**Platforms:** DriverKit 21.0+

## Overview

Use BlockStorageDeviceDriverKit in conjunction with frameworks like PCIDriverKit to create drivers that can communicate with their hardware using custom storage interconnect protocols.

Develop your driver by subclassing IOUserBlockStorageDevice and overriding all methods the framework declares as C++ pure virtual. Then package your driver in an app that uses the System Extensions framework to install and upgrade the driver on the user's Mac.

**Note**: BlockStorageDeviceDriverKit is available on macOS.

## Topics

### Essentials
- **com.apple.developer.driverkit.family.block-storage-device** - A Boolean value that indicates whether to match the driver against block storage devices that use custom drivers.

### Driver Interfaces
- **IOUserBlockStorageDevice** - A DriverKit provider object that manages communications with a block storage device.

### Macros
- **kMaxDeviceStringLength**

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/BlockStorageDeviceDriverKit)*