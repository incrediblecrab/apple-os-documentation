# HomeKit

Configure, control, and communicate with home automation accessories.

**Platforms:** iOS 8.0+ | iPadOS 8.0+ | Mac Catalyst 14.0+ | tvOS 10.0+ | visionOS 1.0+ | watchOS 2.0+

## Overview

HomeKit enables your app to coordinate and control home automation accessories from multiple vendors to present a coherent, user-focused interface.

Using HomeKit, your app can:

- Discover HomeKit-compatible automation accessories and add them to a persistent, cross-device home configuration database.
- Display, edit, and act upon the data in the home configuration database.
- Communicate with configured accessories and services in order to perform actions like turning on the lights in the living room.

## Topics

### Essentials
- [Enabling HomeKit in your app](https://developer.apple.com/documentation/homekit/enabling_homekit_in_your_app) - Declare your app's intention to use HomeKit, and get permission from the user to access home automation accessories.
- **HomeKit Entitlement** - A Boolean value that indicates whether users of the app may manage HomeKit-compatible accessories.
- **NSHomeKitUsageDescription** - A message that tells people why the app is requesting access to their HomeKit configuration data.

### Home Manager
- [Configuring a home automation device](https://developer.apple.com/documentation/homekit/configuring_a_home_automation_device) - Give users a familiar experience when they manage HomeKit accessories.
- [Testing your app with the HomeKit Accessory Simulator](https://developer.apple.com/documentation/homekit/testing_your_app_with_the_homekit_accessory_simulator) - Install the HomeKit Accessory Simulator to help you debug your HomeKit-enabled app.
- **HMHomeManager** - The manager for a collection of one or more of a user's homes.

### Accessories
- **HMAccessorySetupManager** - An object that setups up new accessories.
- **HMAccessorySetupResult** - A result object describing information about a successful accessory setup request.
- **HMAccessorySetupRequest** - An object that describes how to add and setup up new accessories.
- [Interacting with a home automation network](https://developer.apple.com/documentation/homekit/interacting_with_a_home_automation_network) - Find all the automation accessories in the primary home and control their state.
- **HMAccessory** - A home automation accessory, like a garage door opener or a thermostat.
- **HMService** - A controllable feature of an accessory, like a light attached to a garage door opener.
- **HMCharacteristic** - A specific characteristic of a service, like the brightness of a dimmable light or its color temperature.
- **HMMediaSourceDisplayOrderProfile** - An interface from which to read and, if allowed by the accessory, update the ordering of input sources.

### Action Sets
- **HMActionSet** - A collection of actions that you trigger as a group.
- **HMTimerTrigger** - A trigger to activate an action set based on a periodic timer.
- **HMEventTrigger** - A trigger to activate an action set based on a set of events and optional conditions.

### Errors
- **HMError** - An error HomeKit returns.
- **HMErrorDomain** - A string that identifies the HomeKit error domain.
- **Code** - Possible error values that can be returned from HomeKit APIs.
- **HMErrorBlock** - A completion block that provides an error.

### Classes
- **HMAccessorySetupPayload** - A payload for authenticating a HomeKit accessory.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/HomeKit)*