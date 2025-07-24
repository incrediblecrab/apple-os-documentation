# AccessorySetupKit

Enable privacy-preserving discovery and configuration of accessories.

**Platforms:** iOS 18.0+ | iPadOS 18.0+

## Overview

Use AccessorySetupKit to discover and configure Bluetooth or Wi-Fi accessories with images and names provided by the app. Allow seamless, privacy-preserving user consent and control for Bluetooth, Wi-Fi, and Local Network permissions. AccessorySetupKit apps can access enhanced accessory controls including accessory pairing removal and renaming.

To use AccessorySetupKit with Wi-Fi Aware, specify Wi-Fi Aware properties in a ASDiscoveryDescriptor prior to beginning accessory discovery.

> **Important:** AccessorySetupKit is available for iOS and iPadOS. The accessory's Bluetooth permission doesn't sync to a companion watchOS app.

## Topics

### Essentials
- [Setting up and authorizing a Bluetooth accessory](https://developer.apple.com/documentation/accessorysetupkit/setting_up_and_authorizing_a_bluetooth_accessory) - Discover, select, and set up a specific Bluetooth accessory without requesting permission to use Bluetooth.
- [Discovering and configuring accessories](https://developer.apple.com/documentation/accessorysetupkit/discovering_and_configuring_accessories) - Detect nearby accessories and facilitate their setup.
- **ASAccessorySession** - A class to coordinate accessory discovery.

### Accessory Discovery
- **ASAccessoryEvent** - Properties of an event encountered during accessory discovery.
- **ASAccessoryEventType** - An enumeration of the types of events encountered during accessory discovery
- **ASDiscoveryDescriptor** - Descriptive traits used to discover accessories.

### Accessory Description
- **ASAccessory** - An accessory discovered by the accessory session.
- **AccessoryState** - An enumeration of possible authorization states of an accessory.

### Displaying Picker Items
- **ASPickerDisplayItem** - An accessory as presented by the discovery picker.
- **ASMigrationDisplayItem** - A previously-discovered accessory as presented by the discovery picker, for use when migrating it to AccessorySetupKit.

### Information Property List Keys
- **NSAccessorySetupSupports** - An array of strings that indicates the wireless technologies AccessorySetupKit uses when discovering and configuring accessories.
- **NSAccessorySetupBluetoothCompanyIdentifiers** - An array of strings that represent the Bluetooth company identifiers for accessories that your app configures.
- **NSAccessorySetupBluetoothNames** - An array of strings that represent the Bluetooth device names or substrings for accessories that your app configures.
- **NSAccessorySetupBluetoothServices** - An array of strings that represent the hexadecimal values of Bluetooth SIG-defined services or custom services for accessories your app configures.

### Errors
- **ASError** - An error encountered during accessory discovery.
- **ASErrorDomain** - NSError domain for AccessorySetupKit errors.
- **Code** - Codes that describe errors encountered during accessory discovery.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AccessorySetupKit)*