# External Accessory

Communicate with accessories that connect to a device with the Apple Lightning connector, or with Bluetooth wireless technology.

**Platforms:** iOS 3.0+ | iPadOS 3.0+ | Mac Catalyst 13.0+ | macOS 10.13+ | tvOS 10.0+ | visionOS 1.0+

## Overview

Use External Accessory to manage connections to supported MFi accessories. Apple's reference describes Lightning, legacy 30-pin and Bluetooth transports; this is not a general-purpose interface to every device that fits a connector. The framework notifies your app when an accessory connects or disconnects.

An `EASession` communicates using a manufacturer-supported protocol that your app declares in `UISupportedExternalAccessoryProtocols`. That property-list key is an array of reverse-DNS protocol-name strings. Your app formats the protocol's messages and configures the session's input and output streams; the framework does not implement arbitrary device protocols for you.

> **Note:** iPad and iPhone apps running on a Mac with Apple silicon can't connect to external accessories using this framework. You may continue to link apps to this framework and run other features on Apple silicon.

The manufacturer of an MFi accessory decides which third-party apps may communicate with their accessories. If you're developing an app, work with the manufacturer to obtain the information you need to communicate with their hardware. For example, obtain the specifications for the communication protocols the device supports.

For more information about how to connect to external accessories, see External Accessory Programming Topics.

## Topics

### Essentials
- **UISupportedExternalAccessoryProtocols** - The protocols that the app uses to communicate with external accessory hardware.
- **EAAccessoryManager** - The object you use to identify connected accessories, and begin delivery of connection and disconnection notifications.

### Accessory Communication
- **EAAccessory** - An object that contains information about a single, connected hardware accessory.
- **EASession** - The object you use to manage communications between your app and a connected hardware accessory.

### Wi-Fi Accessory Configuration
- **Wireless Accessory Configuration Entitlement** - A Boolean value that indicates whether your app may configure MFi Wi-Fi accessories.
- **EAWiFiUnconfiguredAccessoryBrowser** - An object you use to scan for wireless accessories and configure them for use with the user's app.
- **EAWiFiUnconfiguredAccessory** - An object that provides information about an unconfigured MFi Wireless Accessory Configuration accessory.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ExternalAccessory)*
