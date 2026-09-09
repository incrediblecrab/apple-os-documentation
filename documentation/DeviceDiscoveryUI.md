# DeviceDiscoveryUI

Present system interfaces for pairing apps and nearby devices.

**SDK platforms:** tvOS 16.0+ | iOS 26.0+ | iPadOS 26.0+ | Mac Catalyst 26.0+. Supported workflows and transports differ by platform.

## Overview

DeviceDiscoveryUI provides system-managed pairing for app-to-app and app-to-device communication. Its original Apple TV workflow connects a tvOS app to its iOS, iPadOS, or watchOS counterpart over the local network. For example, a companion app can provide game controls or workout data to an Apple TV app.

The 26 pairing APIs also support publishing and discovering services for peer-to-peer app or accessory connections. Present `DevicePairingView` or `DDDevicePairingViewController` on the publishing side and a device picker on the browsing side. Use Network or Wi-Fi Aware, as appropriate to the workflow, for listeners, connections, and message transfer. Pairing UI does not itself replace the application's data-transfer code.

Check the specific UI and transport capabilities before presenting a workflow, and accommodate unsupported devices or an unfinished pairing interaction. Wi-Fi Aware has its own entitlement and supported iPhone/iPad hardware requirements; DeviceDiscoveryUI's Catalyst listing is not proof of a working Wi-Fi Aware transport on a Mac. For hardware accessory onboarding rather than app-to-app pairing, also consider AccessorySetupKit.

System-managed pairing limits access to the selected connection and can avoid asking for broad local-network access. This benefit does not grant permission for unrelated network or Bluetooth operations.

### Apple TV requirements

On Apple TV, present `DevicePicker` or `DDDevicePickerViewController`. After selection, the system offers to launch and authorize the counterpart app, or to install it if absent. The following restrictions apply specifically to this tvOS workflow:

- DeviceDiscoveryUI is supported only on Apple TV 4K, using `NSApplicationServices` and Network's `NWListener`, not Wi-Fi Aware.
- Your tvOS app can only connect to one device at a time.
- Your tvOS app can only connect to other copies of your app running on iOS, iPadOS, or watchOS.
- You must distribute your app as a universal purchase, so that all copies of your app share the same bundle ID. For more information, see Offering Universal Purchase.
- DeviceDiscoveryUI uses the iCloud account of the default user on Apple TV. If Apple TV has more than one user, the user who manages Family Sharing is the default user. DeviceDiscoveryUI only shows devices logged into that user's iCloud account, or accounts from the user's Family Sharing group.

## Topics

### Selecting nearby devices
- [Connecting a tvOS app to other devices over the local network](https://developer.apple.com/documentation/devicediscoveryui/connecting-a-tvos-app-to-other-devices-over-the-local-network) - Implement the Apple TV companion-app workflow.
- **DevicePicker** - A SwiftUI view that displays other devices on the network, and creates an encrypted connection to a copy of your app running on that device.
- **DDDevicePickerViewController** - A UIKit view that displays other devices on the network, and creates an encrypted connection to a copy of your app running on that device.
- **DevicePickerSupportedAction** - An environment value that indicates whether the current device supports device discovery.
- **NSApplicationServices** - A list of service providers and the devices that they support.

### Publishing and pairing services
- [Building peer-to-peer apps](https://developer.apple.com/documentation/wifiaware/building-peer-to-peer-apps) - Pair and connect supported devices using Wi-Fi Aware and Network.
- **DDDevicePairingViewController** - The UIKit pairing interface.

- **DDDevicePairingAccess** - Specifies the access level requested for device discovery.
- **DevicePairingView** - A control that allows a user to become discoverable and advertise to local devices.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/DeviceDiscoveryUI)*
