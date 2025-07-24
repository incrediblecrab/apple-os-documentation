# Core HID

Interact with keyboards, mice, and other human interface devices.

**Platforms:** macOS 15.0+

## Overview

The CoreHID framework facilitates interaction with human interface devices (HID), like a keyboard, mouse, or other device. Interactions include receiving data that a device generates, such as a key press or mouse click. CoreHID also allows sending requests to a device, such as a request to turn on an LED. You can also emulate a device connected to the system, such as a virtual game controller, and send input to other apps without physical hardware.

To learn more about HID devices, see the USB standards website.

## Topics

### Discovery
- [Discovering HID devices from Terminal](https://developer.apple.com/documentation/corehid/discovering_hid_devices_from_terminal) - Identify devices connected to your Mac from the command line.
- **actor HIDDeviceManager** - A helper for discovering human interface devices (HID) connected to the system.
- **struct DeviceMatchingCriteria** - Matching criteria used to filter HID devices.

### Interaction
- [Communicating with human interface devices](https://developer.apple.com/documentation/corehid/communicating_with_human_interface_devices) - Interact with and obtain data from devices such as keyboards and mice.
- **actor HIDDeviceClient** - A client of a physical or virtual HID compatible peripheral.
- **struct HIDElement** - A representation of an item from a report descriptor for a HID device.
- **struct HIDElementCollection** - A collection of items from a report descriptor for a HID device.
- **struct Value** - Data associated with a HID element.
- **protocol HIDElementUpdate** - A base protocol for element update types.
- **enum HIDReportType** - Types for HID reports.
- **struct HIDReportID** - A type to represent the report IDs of HID reports.
- **enum HIDUsage** - A type to represent HID usage pages.
- **enum HIDDeviceError** - Errors that the framework can throw.
- **enum HIDDeviceTransport** - Common transport types that transmit data to or from a HID device.
- **enum HIDDeviceLocalizationCode** - The localization codes that some HID devices declare to specify conformance to a certain format or language.

### Simulation
- [Creating virtual devices](https://developer.apple.com/documentation/corehid/creating_virtual_devices) - Use and interact with a virtual human interface device for testing and development.
- **actor HIDVirtualDevice** - A virtual service to emulate a HID device connected to the system.
- **protocol HIDVirtualDeviceDelegate** - The delegate to receive notifications for a virtual HID device.
- **struct Properties** - The properties for a virtual HID device.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreHID)*