# AccessorySetupKit

Enable privacy-preserving discovery and configuration of accessories.

**Platforms:** iOS 18.0+ | iPadOS 18.0+

## Overview

Use AccessorySetupKit to discover and configure Bluetooth or Wi-Fi accessories with images and names provided by the app. Allow seamless, privacy-preserving user consent and control for Bluetooth, Wi-Fi, and Local Network permissions. AccessorySetupKit apps can access enhanced accessory controls including accessory pairing removal and renaming.

To use AccessorySetupKit with Wi-Fi Aware, specify Wi-Fi Aware properties in an `ASDiscoveryDescriptor` before beginning accessory discovery. Wi-Fi Aware has its own 26.0 minimum and supported-hardware requirements.

> **Important:** AccessorySetupKit is available for iOS and iPadOS. Starting in watchOS 26, a companion watchOS app can use Core Bluetooth with an accessory set up by the iOS app, but the watchOS app still shows its own Bluetooth privacy alerts. iOS accessory consent is not silently transferred to the watch.

### Authorization lifecycle and related features

An activated session can report accessory additions, removals, changes, and invalidation. Treat picker cancellation as no new authorization, stop using invalidated sessions, and update app state when an accessory is removed. A discovery descriptor's identifiers must match the declared setup metadata; invalid discovery configuration can cause a runtime failure.

Pairing is only the first step for [Wi-Fi Infrastructure](WiFiInfrastructure.md), [Accessory Notifications](AccessoryNotifications.md), [Accessory Live Activities](AccessoryLiveActivities.md), and [AudioAccessoryKit](AudioAccessoryKit.md). Each feature has separate authorization, version, hardware, and regional requirements. Do not apply an EU restriction from one of those features to AccessorySetupKit itself, or treat pairing as consent to notification forwarding.

**Configuration key, verified September 8, 2026:** Use the string-array key `NSAccessorySetupKitSupports`, as instructed by the discovery guide and used in the `ASKSample/ASKSample/Info.plist` file of Apple's published Bluetooth-accessory sample. Apple's [property-list catalog entry](https://developer.apple.com/documentation/bundleresources/information-property-list/nsaccessorysetupsupports) omits `Kit` in its name. That catalog-label discrepancy is not evidence that the two spellings are interchangeable.

## Topics

### Essentials
- [Setting up and authorizing a Bluetooth accessory](https://developer.apple.com/documentation/accessorysetupkit/setting-up-and-authorizing-a-bluetooth-accessory) - Authorize a specific Bluetooth accessory without a broad Bluetooth permission request. Apple's dice sample needs two physical iOS/iPadOS 18-or-later devices, a developer profile, and Xcode 16; it does not run this Bluetooth workflow in Simulator.
- [Discovering and configuring accessories](https://developer.apple.com/documentation/accessorysetupkit/discovering-and-configuring-accessories) - Detect nearby accessories and facilitate their setup.
- **ASAccessorySession** - A class to coordinate accessory discovery.

### Accessory Discovery
- **ASAccessoryEvent** - Properties of an event encountered during accessory discovery.
- **ASAccessoryEventType** - An enumeration of the types of events encountered during accessory discovery
- **ASDiscoveryDescriptor** - Descriptive traits used to discover accessories.

### Accessory Description
- **ASAccessory** - An accessory discovered by the accessory session.
- **ASAccessory.AccessoryState** - An enumeration of possible authorization states of an accessory.

### Displaying Picker Items
- **ASPickerDisplayItem** - An accessory as presented by the discovery picker.
- **ASMigrationDisplayItem** - A previously-discovered accessory as presented by the discovery picker, for use when migrating it to AccessorySetupKit.

### Information Property List Keys
- **NSAccessorySetupKitSupports** - The setup-technologies string array used by the discovery guide and published sample; see the documented catalog-label discrepancy above.
- **NSAccessorySetupBluetoothCompanyIdentifiers** - An array of strings that represent the Bluetooth company identifiers for accessories that your app configures.
- **NSAccessorySetupBluetoothNames** - An array of strings that represent the Bluetooth device names or substrings for accessories that your app configures.
- **NSAccessorySetupBluetoothServices** - An array of strings that represent the hexadecimal values of Bluetooth SIG-defined services or custom services for accessories your app configures.

### Errors
- **ASError** - An error encountered during accessory discovery.
- **ASErrorDomain** - NSError domain for AccessorySetupKit errors.
- **ASError.Code** - Codes that describe errors encountered during accessory discovery.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AccessorySetupKit)*

*Changed-content sources: [discovery and session lifecycle](https://developer.apple.com/documentation/accessorysetupkit/discovering-and-configuring-accessories.md) and [property-list key metadata](https://developer.apple.com/tutorials/data/documentation/bundleresources/information-property-list/nsaccessorysetupsupports.json).*
