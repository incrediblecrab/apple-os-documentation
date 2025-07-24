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

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/BlockStorageDeviceDriverKit)*