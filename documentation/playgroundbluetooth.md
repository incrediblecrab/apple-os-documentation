# Playground Bluetooth

Display and manage connections to Bluetooth peripherals in Swift Playgrounds.

**Platforms:** Swift Playgrounds 2.0+

## Overview

The PlaygroundBluetooth framework provides a common interface that you use to display and manage connections to Bluetooth peripherals from the framework's central manager within a playground page.

## Topics

### Peripheral Connection
Connecting to Bluetooth Peripherals in Swift Playgrounds - Scan for peripherals and display them in your playground's live view.

- **PlaygroundBluetoothCentralManager** - A streamlined interface for connecting the central manager for the current playground page to nearby Bluetooth peripherals.
- **PlaygroundBluetoothCentralManagerDelegate** - A delegate you use to respond to peripheral discovery and manage the lifecycle of connections.

### Peripheral Display

- **PlaygroundBluetoothConnectionView** - A view that displays the connection status of a peripheral to the central manager for the current page and manages connections to other peripherals.
- **PlaygroundBluetoothConnectionViewDelegate** - A delegate you use to respond to user- and system-initiated interactions with the central manager's connection view.
- **PlaygroundBluetoothConnectionViewDataSource** - The protocol you adopt to display an available peripheral in a playground page's connection view.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/playgroundbluetooth)*