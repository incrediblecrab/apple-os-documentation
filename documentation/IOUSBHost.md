# IOUSBHost

Create host-mode user space drivers for USB devices.

**Platforms:** Mac Catalyst 14.0+ | macOS 10.15+

## Overview

With the IOUSBHost framework, you can access custom and non–class-compliant USB devices from within your apps. Use this framework to connect to cameras, audio devices, scanners, printers, keyboards, mouse devices, MIDI keyboards, and USB hubs.

This framework refers to the USB Implementers Forum (USB-IF) Universal Serial Bus 3.2 Specification, Revision 1.0, September 22, 2017. You can view this specification at http://www.usb.org/.

## Topics

### Function Drivers
- **IOUSBHostInterface** - The class for accessing USB-related services.
- **IOUSBHostPipe** - The class that sends control, bulk, interrupt, and isochronous input/output requests for function drivers, and manages stream capabilities.
- **IOUSBHostStream** - The class responsible for sending stream data for function drivers.

### Device Drivers
- **IOUSBHostDevice** - The class that claims and configures devices, retrieves descriptors, and sends device requests.

### Base Classes
- **IOUSBHostObject** - This class provides basic functionality for sending device requests and retrieving descriptors.
- **IOUSBHostIOSource** - This class provides basic functionality for deriving pipe and stream classes.

### IOServicePlane Properties
Properties on the device and interface classes in the service plane.

- **IOUSBHostInterfacePropertyKey** - Properties of a USB interface that describe its state.
- **IOUSBHostDevicePropertyKey** - Properties of a USB device that describe its state.
- **IOUSBHostMatchingPropertyKey** - Properties for implementing the matching service.
- **IOUSBHostPropertyKey** - Properties that the USB host device and interface classes share.

### Error Domain
- **IOUSBHostErrorDomain** - The error domain for the framework.

### Classes
- **IOUSBHostCIControllerStateMachine**
- **IOUSBHostCIDeviceStateMachine**
- **IOUSBHostCIEndpointStateMachine**
- **IOUSBHostCIPortStateMachine**
- **IOUSBHostControllerInterface**

### Reference
- **IOUSBHost Structures**
- **IOUSBHost Enumerations**
- **IOUSBHost Constants**
- **IOUSBHost Functions**
- **IOUSBHost Data Types**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/IOUSBHost)*