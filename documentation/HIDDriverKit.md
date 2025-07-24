# HIDDriverKit

Develop drivers for human-interface devices, such as keyboards, pointing devices, and digitizers like pens and touch pads.

**Platforms:** DriverKit 19.0+ | macOS 10.15+

## Overview

The HIDDriverKit framework provides C++ classes for developing drivers for human interface devices. HIDDriverKit uses the core types defined in DriverKit, and adds features specific to human interface device development.

Develop your driver with DriverKit and HIDDriverKit, and package it in an app that uses the System Extensions framework to install and upgrade the driver on the user's Mac.

> **Note:** HIDDriverKit is available on macOS.

## Topics

### Essentials
- **com.apple.developer.driverkit.transport.hid** - A Boolean value that indicates whether the driver communicates with human interface devices.
- [Handling Keyboard Events from a Human Interface Device](https://developer.apple.com/documentation/hiddriverkit/handling_keyboard_events_from_a_human_interface_device) - Process keyboard-related data from a human interface device and dispatch events to the system.
- [Handling Stylus Input from a Human Interface Device](https://developer.apple.com/documentation/hiddriverkit/handling_stylus_input_from_a_human_interface_device) - Process stylus-related input from a human interface device and dispatch events to the system.

### Samples
- [DriverKit sample code](https://developer.apple.com/documentation/hiddriverkit/driverkit_sample_code) - Explore projects that demonstrate how to write macOS device drivers with the DriverKit family of frameworks.

### Driver Interfaces
- **com.apple.developer.driverkit.family.hid.eventservice** - A Boolean value that indicates whether the driver provides a HID-related event service to the system.
- **IOUserHIDEventDriver** - A complete driver object that dispatches keyboard, digitizer, scrolling, and pointer events originating from a HID device.
- **IOUserHIDEventService** - A service that parses HID report data into elements that you can use to dispatch events.
- **IOHIDEventService** - The base class for implementing a device or operating system service that dispatches events to the system.

### Providers
- **com.apple.developer.driverkit.family.hid.device** - A Boolean value that indicates whether the driver provides a HID-related service to the system.
- **IOHIDInterface** - A provider object for a HID device's interface.
- **IOUserUSBHostHIDDevice** - A provider object for USB devices that support HID interactions.
- **IOUserHIDDevice** - A provider object for devices that support interactions with users.
- **IOHIDDevice** - An object containing the low-level behavior for all HID device providers.

### Events
- **IOHIDDigitizerStylusData** - A structure containing digitizer stylus data.
- **IOHIDDigitizerTouchData** - A structure containing the current digitizer touch data.

### HID Usage Tables
- **HID Usage Tables** - Identify the types of data that HID devices can report to your driver.
- **Match Criteria** - Specify the criteria that the system uses to match your driver to a device.

### HID Device Data
- **IOHIDElement** - An object that contains parsed information from a HID input report.
- **IOHIDDigitizerCollection** - A collection of elements that contain digitizer-related data.
- **com.apple.developer.hid.virtual.device** - A Boolean value that indicates whether the driver creates a virtual HID device.
- **Low-Level Information** - Understand the underlying structures that support HID drivers.

### Reference
- **HIDDriverKit Macros** - Macros
- **kIOHIDEventServiceSensorControlOptionsKey** - Enumeration Cases
- **kHIDUsage_LED_BlueLEDChannel**
- **kHIDUsage_LED_GoodStatus**
- **kHIDUsage_LED_GreenLEDChannel**
- **kHIDUsage_LED_IndicatorBlue**
- **kHIDUsage_LED_IndicatorOrange**
- **kHIDUsage_LED_LEDIntensity**
- **kHIDUsage_LED_RGB_LED**
- **kHIDUsage_LED_RedLEDChannel**
- **kHIDUsage_LED_SystemMicrophoneMute**
- **kHIDUsage_LED_WarningStatus**
- **kHIDUsage_Snsr_Biometric_HeartRate**
- **kHIDUsage_Snsr_Data_Biometric_HeartRate**
- **kHIDUsage_Snsr_Motion_GravityVector**
- **kHIDUsage_Snsr_Motion_LinearAccelerometer**

### Enumerations
- **IOHIDServiceSensorControlOptions**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/HIDDriverKit)*