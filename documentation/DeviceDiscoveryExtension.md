# DeviceDiscoveryExtension

Discover third-party media receivers for a system device-selection menu.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | macOS 15.0+ | visionOS 1.0+

## Overview

Use DeviceDiscoveryExtension (DDE) to discover third-party media receivers to which your app can stream AV content.

When a user invokes your app's media-streaming UI, a device discovery extension can offer a third-party local-network or Bluetooth receiver in an `AVRoutePickerView`. The system loads the extension when the picker displays.

Once the extension loads:

- The extension runs in a system process and searches the local network and Bluetooth devices for a specific media receiver.

- When the extension finds the device, it returns the device to the system, which displays it in the picker view as an available option.

- The user makes a selection and the system passes the chosen device to the app, which can then stream media to the device.

Because DDE runs in a system sandbox, the extension doesn't need to ask the user for local-network or Bluetooth permissions. The picker view displays discovered third-party devices and protocols in the same system menu as AirPlay, which provides a unified device-selection experience.

That permission behavior applies to discovery inside the extension; it is not a general exemption for unrelated networking or Bluetooth calls in the containing app. Add the Boolean [`com.apple.developer.media-device-discovery-extension`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.media-device-discovery-extension) entitlement to the extension using Xcode's Media Device Discovery capability. Handle discovery errors and device-state changes rather than assuming a selected receiver remains reachable.

**Note:** To stream to a third-party device that you don't manufacture, bundle your app with the device discovery extension that the manufacturer provides as part of its SDK.

The platform line follows the framework catalog. Some individual declarations have earlier annotations, including macOS 13 for `DDDiscoveryExtensionConfigurationProtocol`; the sample's macOS server target is not evidence of the discovery client's minimum OS.

## Topics

### Essentials
- [Discovering a third-party media-streaming device](https://developer.apple.com/documentation/devicediscoveryextension/discovering-a-third-party-media-streaming-device) - Run an iOS 16 discovery client against a receiver emulated by an iOS or macOS server target.
- **Media Device Discovery Extension** - An entitlement for an app extension that adds a specific third-party media receiver to a system device-picker UI.

### Extension
- **DDDiscoveryExtension** - A specification that enables the framework to start and stop the extension's discovery process.
- **DDDiscoverySession** - An object that relays device discovery events from the extension to the system.
- **DDDiscoveryExtensionConfigurationProtocol** - A specification that provides a communication channel between the extension and the framework.

### Life Cycle
- **DDDeviceEvent** - An object that provides a device or communicates its change in status.
- **DDDeviceEvent.EventType** - Identifiers for the types of events that occur in the device discovery life cycle.
- **DDEventTypeToString(DDDeviceEvent.EventType) -> String** - Returns human-readable text for the specified event identifier.
- **DDEventHandler** - A function that the extension invokes to signal an event.

### Device Information
- **DDDevice** - An object that describes a discovered device of interest.
- **DDDevice.Category** - An option that determines the icon for the device in the picker UI.
- **DDDeviceState** - A state that represents the level of user interaction with the device.
- **DDDeviceCategoryToString(DDDevice.Category) -> String** - Returns human-readable text for the specified identifier that describes a device's category.
- **DDDeviceStateToString(DDDeviceState) -> String** - Returns human-readable text for the specified identifier that describes a device's status.
- **DDDevice.Protocol** - An identifier for the manner in which an app interacts with a device.
- **DDDeviceProtocolToString(DDDevice.Protocol) -> String** - Returns human-readable text for the specified protocol identifier.
- **DDDeviceProtocolString** - String values for the manner in which an app interacts with a device.
- **DDDeviceMediaPlaybackStateToString(DDDevice.MediaPlaybackState) -> String** - Returns human-readable text for the specified media playback state.

### Errors
- **DDError** - An error that the framework reports.
- **DDError.Code** - Codes that identify errors that can occur during the framework's use.
- **DDErrorHandler** - A function that executes code you provide when an operation returns an error or completes successfully.
- **DDErrorOutType** - A type for framework functions that return error references.
- **DDErrorDomain** - A unique error domain for the framework.

### Reference
- **DeviceDiscoveryExtension Enumerations**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/DeviceDiscoveryExtension)*
