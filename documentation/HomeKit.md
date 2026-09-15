# HomeKit

Configure, control, and communicate with home automation accessories.

**Platforms:** iOS 8.0+ | iPadOS 8.0+ | Mac Catalyst 14.0+ | tvOS 10.0+ | visionOS 1.0+ | watchOS 2.0+

## Overview

HomeKit enables your app to coordinate and control home automation accessories from multiple vendors to present a coherent, user-focused interface.

Using HomeKit, your app can:

- Discover HomeKit-compatible automation accessories and add them to a persistent, cross-device home configuration database.
- Display, edit, and act upon the data in the home configuration database.
- Communicate with configured accessories and services in order to perform actions like turning on the lights in the living room.

For access to home configuration data, enable the Boolean `com.apple.developer.homekit` entitlement and supply the `NSHomeKitUsageDescription` purpose string. The system normally presents the permission prompt when the app creates an `HMHomeManager`; there is no separate explicit authorization request to issue. Missing purpose text causes a crash when the app first uses HomeKit.

Check the manager's authorization status where available and handle `HMError.Code.homeAccessNotAuthorized` in completion handlers. A person can deny initial access or revoke it later in Settings. Accessory setup is a distinct flow: `HMAccessorySetupManager` does not require the calling app to already have home-data authorization.

## OS 27: Home intelligence behavior

**Reviewed September 8, 2026:** The iOS/iPadOS, macOS, and tvOS 27 release notes say that, when Apple Intelligence in Home is enabled, HomeKit Secure Video recordings are processed on-device **and through Private Cloud Compute** for video descriptions and search. Apple Intelligence for Home requires an iCloud+ subscription starting at 2 TB.

These are conditional Home-system features, not new permissions for third-party apps to read recordings or a promise that every accessory gains 4K recording. They do not replace the authorization requirements for the app's own home-data access.

## Topics

### Essentials
- [Enabling HomeKit in your app](https://developer.apple.com/documentation/homekit/enabling-homekit-in-your-app) - Configure the capability, purpose string, and denial handling.
- **HomeKit Entitlement** - A Boolean value that indicates whether users of the app may manage HomeKit-compatible accessories.
- **NSHomeKitUsageDescription** - A message that tells people why the app is requesting access to their HomeKit configuration data.

### Home Manager
- [Configuring a home automation device](https://developer.apple.com/documentation/homekit/configuring-a-home-automation-device) - Give users a familiar experience when they manage HomeKit accessories.
- [Testing your app with the HomeKit Accessory Simulator](https://developer.apple.com/documentation/homekit/testing-your-app-with-the-homekit-accessory-simulator) - Use Mac-hosted simulated accessories while testing a HomeKit app.
- **HMHomeManager** - The manager for a collection of one or more of a user's homes.

### Accessories
- **HMAccessorySetupManager** - Coordinates accessory setup; iOS/iPadOS 15 and Mac Catalyst 27.
- **HMAccessorySetupResult** - Describes a successful setup request; iOS/iPadOS 15.4 and Mac Catalyst 27.
- **HMAccessorySetupRequest** - Describes how to add and set up accessories; iOS/iPadOS 15.4 and Mac Catalyst 27.
- [Interacting with a home automation network](https://developer.apple.com/documentation/homekit/interacting-with-a-home-automation-network) - Inspect accessories, services, and characteristics in the primary home.
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
- **HMError.Code** - Possible error values that can be returned from HomeKit APIs.
- **HMErrorBlock** - A completion block that provides an error.

### Classes
- **HMAccessorySetupPayload** - A payload for authenticating a HomeKit accessory.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/HomeKit)*

*27 sources: [iOS/iPadOS release notes — HomeKit](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes.md) and [macOS release notes — HomeKit](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes.md).*
