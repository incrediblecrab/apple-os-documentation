# IOKit

Access hardware devices and drivers from your apps and services.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 13.0+ | macOS 10.0+ | visionOS 1.0+

## Overview

The IOKit framework implements nonkernel access to IOKit objects such drivers and nubs through the device-interface mechanism.

> **Important**
>
> Devices supported on macOS 11 and later require DriverKit. Use IOKit in your apps and services to discover and use devices.

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
- [IOKit Fundamentals](https://developer.apple.com/documentation/iokit/iokit_fundamentals)

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/iokit)*