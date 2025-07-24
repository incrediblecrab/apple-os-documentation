# DeviceDiscoveryUI

Display an interface that lets users connect a tvOS app to a mobile device over the local network.

**Platforms:** tvOS 16.0+

## Overview

The DeviceDiscoveryUI framework provides an encrypted connection between your tvOS app and your iOS, iPadOS, or watchOS app using the local network. For example, users could control a tvOS game from their iPad. Or, a fitness tvOS app could connect to the watchOS version, which records the workout session and passes heart rate and calorie data back to the tvOS app.

On Apple TV, you start by presenting a DevicePicker view or a DDDevicePickerViewController. This view displays a list of all the devices your tvOS app can connect to on the local network. When the user selects a device, the system attempts to launch your app on that device. If your app is already installed, the system asks the user if they want to connect to Apple TV. If your app isn't installed, the system prompts the user to install it.

You use DeviceDiscoveryUI to present a view that lists available devices, and then use the Network framework to create the listeners, create the connections, and send and receive messages.

DeviceDiscoveryUI provides several advantages over creating a connection using the Network framework directly. It automatically sets up an optimized, encrypted connection between versions of your app running on different local devices. It helps preserve the user's privacy by only providing access to iOS, iPadOS, and watchOS devices on the local network. Also, because the system securely manages the connection, your users don't need to authorize full access to their local network.

### Requirements

The following requirements apply:

- DeviceDiscoveryUI is supported only on Apple TV 4K.
- Your tvOS app can only connect to one device at a time.
- Your tvOS app can only connect to other copies of your app running on iOS, iPadOS, or watchOS.
- You must distribute your app as a universal purchase, so that all copies of your app share the same bundle ID. For more information, see Offering Universal Purchase.
- DeviceDiscoveryUI uses the iCloud account of the default user on Apple TV. If Apple TV has more than one user, the user who manages Family Sharing is the default user. DeviceDiscoveryUI only shows devices logged into that user's iCloud account, or accounts from the user's Family Sharing group.

## Topics

### Selecting nearby devices
- [Connecting a tvOS app to other devices over the local network](https://developer.apple.com/documentation/devicediscoveryui/connecting_a_tvos_app_to_other_devices_over_the_local_network) - Display a view in your tvOS app that lists available iOS, iPadOS, and watchOS devices that the user can connect to over their local network.
- **DevicePicker** - A SwiftUI view that displays other devices on the network, and creates an encrypted connection to a copy of your app running on that device.
- **DDDevicePickerViewController** - A UIKit view that displays other devices on the network, and creates an encrypted connection to a copy of your app running on that device.
- **DevicePickerSupportedAction** - An environment value that indicates whether the current device supports device discovery.
- **NSApplicationServices** - A list of service providers and the devices that they support.

### Classes
- **DDDevicePairingViewController** - Beta

### Structures
- **DDDevicePairingAccess** - Specifies the access level requested for device discovery. Beta
- **DevicePairingView** - A control that allows a user to become discoverable and advertise to local devices. Beta

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/DeviceDiscoveryUI)*