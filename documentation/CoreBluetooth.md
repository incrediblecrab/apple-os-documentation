# Core Bluetooth

Communicate with Bluetooth low energy and BR/EDR ("Classic") Devices.

**Framework catalog:** iOS 5.0+ | iPadOS 5.0+ | macOS 10.10+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 4.0+. For Mac Catalyst, core classes such as `CBCentralManager` require 13.1, not the catalog's 13.0 label. Individual declarations can also predate the catalog minimum, such as `CBCentralManager` on macOS 10.7.

## Overview

The Core Bluetooth framework provides the classes needed for your apps to communicate with Bluetooth-equipped low energy (LE) and Basic Rate / Enhanced Data Rate (BR/EDR) wireless technology.

Don't subclass any of the classes of the Core Bluetooth framework. Overriding these classes isn't supported and results in undefined behavior.

Core Bluetooth background execution modes aren't supported in iPad apps running on macOS.

> **Important:** Your app will crash if its Info.plist doesn't include usage description keys for the types of data it needs to access. To access Core Bluetooth APIs on apps linked on or after iOS 13, include the NSBluetoothAlwaysUsageDescription key. In iOS 12 and earlier, include NSBluetoothPeripheralUsageDescription to access Bluetooth peripheral data.

Purpose strings are not permission grants. Check `CBManager.authorization` where available and handle refusal or later changes. Wait for the manager's state-update callback and a `.poweredOn` state before scanning or connecting; `state` is read-only, not a switch an app can set to turn on Bluetooth.

In iOS 26 and later, an app with an instantiated `CBManager` can retain foreground-like Bluetooth privileges while a Live Activity started before backgrounding is active, including the documented less-restricted scanning behavior. This is a conditional background path, not a guarantee of unlimited runtime or support for every iOS-compatible Mac app.

## Topics

### Centrals
- **CBCentral** - A remote device connected to a local app, which is acting as a peripheral.
- **CBCentralManager** - An object that scans for, discovers, connects to, and manages peripherals.
- **CBCentralManagerDelegate** - A protocol that provides updates for the discovery and management of peripheral devices.

### Peripherals
- **CBPeripheral** - A remote peripheral device.
- **CBPeripheralDelegate** - A protocol that provides updates on the use of a peripheral's services.
- **CBPeripheralManager** - An object that manages and advertises peripheral services exposed by this app.
- **CBPeripheralManagerDelegate** - A protocol that provides updates for local peripheral state and interactions with remote central devices.
- **CBAttribute** - A representation of common aspects of services offered by a peripheral.
- **CBAttributePermissions** - Values that represent the read, write, and encryption permissions for a characteristic's value.

### Data Transfer
- [Transferring Data Between Bluetooth Low Energy Devices](https://developer.apple.com/documentation/corebluetooth/transferring-data-between-bluetooth-low-energy-devices) - Create a Bluetooth low energy central and peripheral device, and allow them to discover each other and exchange data.

### Channel Sounding in 27
- [Measuring distance between devices using Channel Sounding](https://developer.apple.com/documentation/corebluetooth/measuring-distance-between-devices-using-channel-sounding) - Apple's sample requires an iOS 27 Channel Sounding-capable iPhone, described as iPhone 17 or later, and a Bluetooth 6.3 Channel Sounding responder. It cannot run this ranging workflow in Simulator.
- The sample pairs through AccessorySetupKit before creating its Bluetooth manager to avoid a competing permission prompt. Channel Sounding sessions require an AccessorySetupKit-paired accessory. Check hardware support after the manager reaches `.poweredOn`, and handle failed or unavailable measurements rather than displaying an invalid distance.

### Services
- **CBService** - A collection of data and associated behaviors that accomplish a function or feature of a device.
- **CBMutableService** - A service with writeable property values.
- **CBCharacteristic** - A characteristic of a remote peripheral's service.
- **CBMutableCharacteristic** - A characteristic of a local peripheral's service.
- **CBDescriptor** - An object that provides further information about a remote peripheral's characteristic.
- **CBMutableDescriptor** - An object that provides additional information about a local peripheral's characteristic.

### Supporting Types
- **CBManager** - The abstract base class that manages central and peripheral objects.
- **CBATTRequest** - A request that uses the Attribute Protocol (ATT).
- **CBPeer** - An object that represents a remote device.
- **CBUUID** - A universally unique identifier, as defined by Bluetooth standards.

### Bluetooth Classic Support
- [Using Core Bluetooth Classic](https://developer.apple.com/documentation/corebluetooth/using-core-bluetooth-classic) - Discover and communicate with a Bluetooth Classic device using the sample's iOS 13-generation Core Bluetooth APIs.

### Errors
- **CBError** - An error that Core Bluetooth returns during Bluetooth transactions.
- **CBErrorDomain** - The domain for Core Bluetooth errors.
- **CBError.Code** - The codes for errors that Core Bluetooth returns during Bluetooth transactions.
- **CBATTError** - An error that Core Bluetooth returns while using Attribute Protocol (ATT).
- **CBATTErrorDomain** - The domain for Core Bluetooth ATT errors.
- **CBATTError.Code** - The possible errors returned by a GATT server (a remote peripheral) during Bluetooth low energy ATT transactions.

### Deprecated
- **CBCentralManagerState** - Values that represent the current state of a central manager object. *Deprecated*
- **CBPeripheralManagerState** - Values that represent the current state of the peripheral manager. *Deprecated*
- [Deprecated Constants](https://developer.apple.com/documentation/corebluetooth/deprecated-constants) - The framework's deprecated constants reference.

### Variables
- **CBUUIDCharacteristicObservationScheduleString**

### See Also
- [Core Bluetooth Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/AboutCoreBluetooth/Introduction.html) - Archived concepts and background-processing guidance; consult current references for newer behavior.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreBluetooth)*
