# IOKit

Access hardware devices and drivers from your apps and services.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 13.0+ | macOS 10.0+ | visionOS 1.0+

## Overview

The IOKit framework provides nonkernel access to driver and device objects through device interfaces.

> **Important**
>
> Use DriverKit or system extensions when they support the required driver or service. Apple's [migration guidance](https://developer.apple.com/documentation/systemextensions/implementing-drivers-system-extensions-and-kexts) makes the macOS 11+ restriction conditional on an equivalent supported solution; it does not say that every device or low-level service has a DriverKit replacement. IOKit's user-space discovery and device interfaces are distinct from deploying a kernel extension.

## Topics

### Serial Ports
- [Communicating with a Modem on a Serial Port](https://developer.apple.com/documentation/iokit/communicating_with_a_modem_on_a_serial_port) - Find and connect to a modem attached to a serial port using IOKit.

### Reference
- [IODataQueueClient.h](https://developer.apple.com/documentation/iokit/iodataqueueclient_h)
- [IOKitLib.h](https://developer.apple.com/documentation/iokit/iokitlib_h)
- [IOTypes.h User-Space](https://developer.apple.com/documentation/iokit/iotypes_h_user-space)
- [IOKit Structures](https://developer.apple.com/documentation/iokit/iokit_structures)
- [IOKit Enumerations](https://developer.apple.com/documentation/iokit/iokit_enumerations)
- [IOKit Constants](https://developer.apple.com/documentation/iokit/iokit_constants)
- [IOKit Functions](https://developer.apple.com/documentation/iokit/iokit_functions)
- [IOKit Data Types](https://developer.apple.com/documentation/iokit/iokit_data_types)

### See Also
- [IOKit Fundamentals](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/IOKitFundamentals/Introduction/Introduction.html) - Historical conceptual guidance for device interfaces and kernel-resident drivers. Use the current migration guidance above when choosing an implementation.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/iokit)*
