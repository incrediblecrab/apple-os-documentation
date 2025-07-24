# USBDriverKit

Develop drivers for USB-based devices.

**Platforms:** DriverKit 19.0+

## Overview

Use the **USBDriverKit** framework to develop drivers for custom or non-class-compliant USB devices for use with macOS. The objects in this framework serve as providers for your driver. Use them as is to access the device configurations, interfaces, and endpoints of the USB device. Each object provides methods for fetching any needed descriptors from the USB device, and for initiating requests to perform your driver's custom behaviors.

Develop your driver by subclassing **IOService** in the **DriverKit** framework. On macOS, use the **System Extensions** framework to install and upgrade your driver. On iPadOS, the system automatically discovers and upgrades drivers along with their host apps.

**Note**

**USBDriverKit** is available on macOS for Intel and Apple Silicon devices, and on iPadOS for devices with an M-series chip.

## Topics

### Essentials
- **com.apple.developer.driverkit.transport.usb** - An array of dictionaries that identify the USB devices the driver supports.

### Samples
- [DriverKit sample code](https://developer.apple.com/documentation/usbdriverkit/driverkit_sample_code) - Explore projects that demonstrate how to write macOS device drivers with the DriverKit family of frameworks.

### Providers
- **IOUSBHostInterface** - A provider object that manages interactions with an interface of the USB device.
- **IOUSBHostDevice** - A provider object that represents the USB device.

### Endpoint Communication
- **IOUSBHostPipe** - An object you use to transfer data to or from a USB endpoint.

### USB Specifications
- [USB Device Descriptors](https://developer.apple.com/documentation/usbdriverkit/usb_device_descriptors) - Determine the capabilities and configuration of a device using descriptors from the USB specification.
- [Additional Specifications](https://developer.apple.com/documentation/usbdriverkit/additional_specifications) - Request information from a device and get hardware and timing information.
- [Registry Property Names](https://developer.apple.com/documentation/usbdriverkit/registry_property_names) - Search for specific keys in the device registry.

### Utilities
Manipulate bit structures and convert integers between device- and platform-native formats.

### References
- **USBDriverKit Enumerations**
- **USBDriverKit Functions**
- **USBDriverKit Data Types**
- **USBDriverKit Macros**

### Macros
- **kUSBHostBillboardDevicePropertyAltModeFailed**
- **kUSBHostBillboardDevicePropertyAltModePowerFailed**
- **kUSBHostBillboardDevicePropertyCurrentMode**
- **kUSBHostBillboardDevicePropertyModeValueDisplayPort**
- **kUSBHostBillboardDevicePropertyModeValueThunderbolt**
- **kUSBHostBillboardDevicePropertyModeValueUSB4**
- **kUSBHostBillboardDevicePropertyPreferredMode**
- **kUSBHostBillboardDevicePropertyVersion**
- **kUSBHostControllerPropertyProtocolRevision**
- **kUSBHostDevicePropertyIdlePolicy**
- **kUSBHostDevicePropertyPowerSinkAllocation**
- **kUSBHostDevicePropertyUSB3Preferred**
- **kUSBHostDevicePropertyUSB3Required**
- **kUSBHostPortPropertyIOPortServicePath**
- **kUSBHostPortPropertyProtocolCompanionRevision1**
- **kUSBHostPortPropertyProtocolCompanionRevision2**
- **kUSBHostPortPropertyProtocolCompanionRevision3**
- **kUSBHostPortPropertyProtocolRevision1**
- **kUSBHostPortPropertyProtocolRevision2**
- **kUSBHostPortPropertyProtocolRevision3**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/USBDriverKit)*