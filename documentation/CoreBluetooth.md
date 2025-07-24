# Core Bluetooth

Communicate with Bluetooth low energy and BR/EDR ("Classic") Devices.

**Platforms:** iOS 5.0+ | iPadOS 5.0+ | Mac Catalyst 13.0+ | macOS 10.10+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 4.0+

## Overview

The Core Bluetooth framework provides the classes needed for your apps to communicate with Bluetooth-equipped low energy (LE) and Basic Rate / Enhanced Data Rate (BR/EDR) wireless technology.

Don't subclass any of the classes of the Core Bluetooth framework. Overriding these classes isn't supported and results in undefined behavior.

Core Bluetooth background execution modes aren't supported in iPad apps running on macOS.

> **Important:** Your app will crash if its Info.plist doesn't include usage description keys for the types of data it needs to access. To access Core Bluetooth APIs on apps linked on or after iOS 13, include the NSBluetoothAlwaysUsageDescription key. In iOS 12 and earlier, include NSBluetoothPeripheralUsageDescription to access Bluetooth peripheral data.

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
- [Transferring Data Between Bluetooth Low Energy Devices](https://developer.apple.com/documentation/corebluetooth/transferring_data_between_bluetooth_low_energy_devices) - Create a Bluetooth low energy central and peripheral device, and allow them to discover each other and exchange data.

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
- [Using Core Bluetooth Classic](https://developer.apple.com/documentation/corebluetooth/using_core_bluetooth_classic) - Discover and communicate with a Bluetooth Classic device by using the Core Bluetooth APIs.

### Errors
- **CBError** - An error that Core Bluetooth returns during Bluetooth transactions.
- **CBErrorDomain** - The domain for Core Bluetooth errors.
- **Code** - The codes for errors that Core Bluetooth returns during Bluetooth transactions.
- **CBATTError** - An error that Core Bluetooth returns while using Attribute Protocol (ATT).
- **CBATTErrorDomain** - The domain for Core Bluetooth ATT errors.
- **Code** - The possible errors returned by a GATT server (a remote peripheral) during Bluetooth low energy ATT transactions.
- **CBATTError** - An error that Core Bluetooth returns while using Attribute Protocol (ATT).

### Deprecated
- **CBCentralManagerState** - Values that represent the current state of a central manager object. *Deprecated*
- **CBPeripheralManagerState** - Values that represent the current state of the peripheral manager. *Deprecated*
- [Deprecated Constants](https://developer.apple.com/documentation/corebluetooth/deprecated_constants) - This document describes the constants found in the Core Bluetooth framework.

### Variables
- **CBUUIDCharacteristicObservationScheduleString**

### See Also
- [Core Bluetooth Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/AboutCoreBluetooth/Introduction.html) - Related Documentation

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreBluetooth)*