# SerialDriverKit

Develop drivers for serial I/O devices connected to your Mac.

**Platforms:** DriverKit 19.0+

## Overview

The SerialDriverKit framework supports the development of drivers for devices that communicate using a serial interface. The framework lets you build drivers to support modem hardware or a universal asynchronous receiver/transmitter (UART). To create a driver that communicates serially with a USB device, use the **USBSerialDriverKit** framework instead.

Package your driver in an app that uses the **System Extensions** framework to install and upgrade the driver on the user's Mac.

**Note:** SerialDriverKit is available on macOS.

## Topics

### Samples
- [DriverKit sample code](https://developer.apple.com/documentation/serialdriverkit/driverkit_sample_code) - Explore projects that demonstrate how to write macOS device drivers with the DriverKit family of frameworks.

### Serial Interface
- **com.apple.developer.driverkit.family.serial** - A Boolean value that indicates whether to match the driver against devices with serial communication interfaces.
- **IOUserSerial** - The class for building a service that communicates using a serial connection.

### Reference
- **SerialDriverKit Enumerations**
- **SerialDriverKit Data Types**

### Namespaces
- **driverkit**

### Macros
- **PD_RS232_S_LE**
- **PD_RS232_S_RNG**
- **kIOTTYBaseNameKey**
- **kIOTTYSuffixKey**

### Enumeration Cases
- **kIOSerialMemoryArena**
- **kIOSerialMemoryRxBuf**
- **kIOSerialMemoryTxBuf**
- **kIOSerialPTYMaster**
- **kIOSerialUserClient**
- **kIOSerialUserClientIoctl**
- **kIOSerialUserClientOpen**
- **kIOSerialUserClientPoll**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SerialDriverKit)*