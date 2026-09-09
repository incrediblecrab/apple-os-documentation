# Wi-Fi Aware

Securely pair and connect to external devices over peer-to-peer Wi-Fi.

**Platforms:** iOS 26.0+ | iPadOS 26.0+

## Overview
Wi-Fi Aware™ (also known as Neighbor Awareness Networking or NAN) is a Wi-Fi Alliance™ standard specification that enables devices to securely discover, pair, and communicate with nearby devices without an internet connection or access point. Your app can use the Wi-Fi Aware framework to connect with Wi-Fi Aware certified accessories. The framework offers a secure and standardized way to establish peer-to-peer (P2P) connections between Wi-Fi devices, providing networking capabilities such as:

- High-bandwidth and low-latency data transfers, subject to radio conditions and configuration.
- Connections to paired devices authenticated and encrypted at the Wi-Fi layer.
- Simultaneous connections to multiple Wi-Fi Aware devices.
- Concurrent use of Wi-Fi Aware and an infrastructure Wi-Fi network.
- Peer-to-peer links that do not require one peer to remain as a central access point.

The Wi-Fi Aware technology works without the need for Wi-Fi infrastructure networks, cellular links, internet connections, or cloud servers. Your app can pair Wi-Fi Aware devices using AccessorySetupKit or DeviceDiscoveryUI. When paired, your app can create secure, authenticated, and encrypted peer-to-peer connections between paired devices on-demand, using the Wi-Fi Aware and Network frameworks.

Apple lists the following supported device families; use `WACapabilities` to check the capabilities needed by a particular operation:

- iPhone 12 and later.
- iPad (10th generation) and later.
- iPad Air (4th generation) and later.
- iPad Pro 11-inch (3rd generation) and later.
- iPad Pro 12.9-inch (5th generation) and later.
- iPad mini (6th generation) and later.

The catalog also lists Mac Catalyst symbols, but its hardware-support discussion identifies iPhone and iPad, not eligible Mac hardware. Do not infer a working Mac data path from those symbol listings.

## Configuration, pairing, and lifetime

The [`com.apple.developer.wifi-aware`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.wifi-aware) entitlement is an array of strings containing `Publish`, `Subscribe`, or both. Declare [`WiFiAwareServices`](https://developer.apple.com/documentation/bundleresources/information-property-list/wifiawareservices) as a dictionary keyed by complete service names such as `_example._tcp`. Each service contains a `Publishable` empty dictionary, a `Subscribable` empty dictionary, or both. Missing or malformed declarations can cause failures or crashes.

The service component before `._tcp` or `._udp`, excluding its leading underscore, is at most 15 letters, digits, or hyphens. It must contain a letter and cannot begin or end with a hyphen. Publish a given service only once per device and avoid redundant concurrent subscriptions.

Use DeviceDiscoveryUI for device/app pairing or AccessorySetupKit for a personal accessory and its companion app. Track `WAPairedDevice.allDevices`: it contains only paired devices accessible to the app and changes when people add or remove access. Pre-pairing `PairingInfo` is unauthenticated, not a trusted identity. Handle pairing refusal, revoked access, unavailable peers, and connection errors.

Wi-Fi Aware can operate while an app has foreground or background runtime; it does not itself grant indefinite background execution. Match the connection and listener performance modes. Apple recommends `.bulk` for most uses; `.realtime` trades additional energy use for latency-sensitive work.

`WAConnection` and `WASharedSecret` require 26.4, rather than the framework's 26.0 minimum. A derived shared secret belongs to one connection and can bootstrap higher-layer protocol security. Do not store it, transmit it to peers, reuse it across connections, or use it as a long-term key. `WAPerformanceForecast` is a separate 27.0 beta addition; a forecast is not a throughput or latency guarantee.

## Topics

### Essentials
- [Building peer-to-peer apps](https://developer.apple.com/documentation/wifiaware/building-peer-to-peer-apps) - Mirror a satellite simulation between a publisher and subscribers. Requires two physical supported devices; not Simulator.
- [Connecting paired devices](https://developer.apple.com/documentation/wifiaware/connecting-paired-devices) - Make outgoing and accept incoming secure connections with paired devices.
- [Adopting Wi-Fi Aware](https://developer.apple.com/documentation/wifiaware/adopting-wi-fi-aware) - Add entitlements and declare your app's services.
- **com.apple.developer.wifi-aware** - The entitlement the system requires for an app to use the Wi-Fi Aware framework.
- **WiFiAwareServices** - Dictionaries of Wi-Fi Aware services that the app can publish or subscribe to.

### Host capabilities
- **WACapabilities** - A structure that checks the host device's supported features and capabilities.
- **WACapabilities.Feature** - Features that your app's current host device can support.

### Services to discover
- **WAService** - A protocol that defines a service that a device can publish or subscribe to.
- **WASubscribableService** - A service your app discovers on remote devices and can connect to.
- **WAPublishableService** - A service, hosted by your app, that remote devices can connect to.

### Paired devices
- **WAPairedDevice** - A known Wi-Fi Aware device that your app can connect to.
- **WAPairedDevice.Devices** - A dictionary holding a snapshot of currently paired devices accessible and known to your app.
- **WAPairedDevice.DevicesSequence** - A sequence that vends updates to a paired device list, as the list changes.
- **WAPairedDevice.PairingInfo** - A collection of unauthenticated information the system receives from a device before it's paired for the first time.

### Subscriber
- **WASubscriberBrowser** - The structure that configures a network browser to subscribe to a Wi-Fi Aware service and make outgoing connections to paired devices.
- **WASubscriberBrowser.Action** - The structure that configures the Wi-Fi Aware subscriber operation the network browser performs.
- **WASubscriberBrowser.Devices** - The structure that determines the devices to connect to.

### Publisher
- **WAPublisherListener** - Configures a network listener to publish a service over Wi-Fi Aware and accept incoming connections from paired devices.
- **WAPublisherListener.Action** - The structure that configures the Wi-Fi Aware publisher operation that the network listener performs.
- **WAPublisherListener.Devices** - The structure that determines the devices to connect to.
- **WAPublisherListener.DatapathParameters** - The parameter that sets the initial Wi-Fi Aware data path configuration for connected devices.

### Parameters
- **NWParameters** - An object that stores the protocols to use for connections, options for sending data, and network path constraints.
- **NWParametersBuilder** - A generic Network framework structure that builds parameters for a typed protocol stack.
- **WAParameters** - Parameters configuring a Wi-Fi Aware data path connection.

### Connections
- **WAEndpoint** - The endpoint of a Wi-Fi Aware connection.
- [WAConnection](https://developer.apple.com/documentation/wifiaware/waconnection) - Wi-Fi Aware information and configuration associated with a `NetworkConnection`; 26.4+.
- [WASharedSecret](https://developer.apple.com/documentation/wifiaware/washaredsecret) - A connection-specific secret for establishing higher-layer security; 26.4+.

### Connection performance
- **NWPath** - An object that contains information about the properties of the network that a connection uses, or that are available to your app.
- **WAPath** - A representation of the current Wi-Fi Aware path.
- **WAPerformanceMode** - The performance mode that indicates what performance criterion to prioritize.
- **WAAccessCategory** - The underlying quality-of-service (QoS) category the Wi-Fi layer uses to transmit data packets.
- **WAPerformanceReport** - The current performance state of the data path.
- [WAPerformanceForecast](https://developer.apple.com/documentation/wifiaware/waperformanceforecast) - A forecast for connection setup to a remote device; 27.0 beta.

### Errors
- **NWError** - The errors returned by objects in the Network framework.
- **WAError** - An error in Wi-Fi Aware.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/WiFiAware)*
