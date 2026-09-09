# Core WLAN

Query AirPort interfaces and choose wireless networks.

**Platforms:** macOS 10.6+; the `CWWiFiClient` workflow below requires macOS 10.10+.

The framework catalog also lists Mac Catalyst 13.0, but the client APIs described here are macOS APIs. In particular, `CWWiFiClient` is explicitly unavailable to Mac Catalyst in the macOS 26.5 SDK. Importing module constants is not evidence that a Catalyst app can use this Wi-Fi client.

## Overview

The CoreWLAN framework provides APIs for querying AirPort interfaces and choosing networks.

You access the Wi-Fi subsystem by working with a CWWiFiClient instance. This client object provides methods to obtain a handle on all of the system's Wi-Fi interfaces, represented by CWInterface objects. You can also use the client to register to receive Wi-Fi event notifications. You assign a delegate conforming to the CWEventDelegate protocol to process these notifications.

Because creating the client object is resource intensive, it's usually best to work with a single object over the life of your app rather than creating a series of short lived instances. For convenience, the client class defines a shared instance singleton that you can use for this purpose.

You can use the CoreWLAN framework in an app that adopts App Sandbox without any special exceptions as long as you use the interface objects vended from a client instance. If you initialize interface objects directly, you incur low level system socket accesses that are not considered sandbox safe. For more information about App Sandbox, read App Sandbox Design Guide.

Handle query failures independently of object creation. For example, `CWInterface.ssid()` can return `nil` after an error, when not associated with a network, or when the SSID cannot be represented as a supported string.

## Topics

### Classes
- **CWChannel** - Encapsulates an IEEE 802.11 channel.
- **CWConfiguration** - Encapsulates an immutable configuration for an AirPort WLAN interface.
- **CWInterface** - Encapsulates an IEEE 802.11 interface.
- **CWMutableConfiguration** - Encapsulates a mutable configuration for an AirPort WLAN interface.
- **CWMutableNetworkProfile** - Encapsulates a mutable network profile entry.
- **CWNetwork** - Encapsulates an IEEE 802.11 network, providing read-only accessors to various properties of the network.
- **CWNetworkProfile** - Encapsulates an immutable network profile entry.
- **CWWiFiClient** - A wrapper around the entire Wi-Fi subsystem that you use to access interfaces and set up event notifications.

### Protocols
- **CWEventDelegate** - The interface a Wi-Fi client object uses to notify its delegate about Wi-Fi events.

### Reference
- **CoreWLANConstants.h**
- **CoreWLANTypes.h**
- **CoreWLANUtil.h**
- **CoreWLAN Enumerations**
- **CoreWLAN Functions**

### Structures
- **CWCipherKeyFlags** - Cipher key flags.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreWLAN)*
