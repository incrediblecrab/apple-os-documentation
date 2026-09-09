# Network

Create network connections to send and receive data using transport and security protocols.

**Platforms:** iOS 12.0+ | iPadOS 12.0+ | Mac Catalyst 13.0+ | macOS 10.14+ | tvOS 12.0+ | visionOS 1.0+ | watchOS 6.0+

## Overview

Use this framework when you need direct access to protocols like TLS, TCP, and UDP for your custom application protocols. Continue to use URLSession, which is built upon this framework, for loading HTTP- and URL-based resources. For in-depth advice on where to start with networking, see [TN3151: Choosing the right networking API](https://developer.apple.com/documentation/technotes/tn3151-choosing-the-right-networking-api).

The reference spans multiple API generations. `NetworkConnection`, `NetworkListener`, `NetworkBrowser`, `ProtocolStackBuilder`, and `NetworkEncoder`/`NetworkDecoder` require **26.0** on their declared platforms; they are not aliases available at the older `NWConnection` minimum. Other milestones include `NWBrowser` and WebSocket/framing support in iOS 13/macOS 10.15, connection groups in iOS 14/macOS 11, QUIC in iOS 15/macOS 12, `ProxyConfiguration` in iOS 17/macOS 14, and `TXTRecordDecoder` in iOS 18/macOS 15. Wi-Fi Aware error constants and the ultra-constrained/link-quality query functions listed below are also 26.0 additions.

> **watchOS:** Low-level networking is limited to active audio streaming (watchOS 6+), CallKit VoIP calls (9+), and the supported watchOS 9/tvOS 16 DeviceDiscoveryUI connection workflow. An ordinary unsupported connection can remain waiting with `ENETDOWN`; Simulator behavior is not proof of device support. See [TN3135](https://developer.apple.com/documentation/technotes/tn3135-low-level-networking-on-watchos).

### Local-network permission and connection failures

Local-network privacy applies on iOS/iPadOS 14+, macOS 15+, and visionOS 1+, not tvOS or watchOS. Add `NSLocalNetworkUsageDescription` when required, and declare Bonjour service types used for registration or browsing in `NSBonjourServices`. Raw multicast/broadcast and some unrestricted Bonjour operations additionally require `com.apple.developer.networking.multicast` on iOS/iPadOS/visionOS, but not macOS.

An operation can initially fail while the permission alert is still pending. Handle waiting and failure states instead of treating a discovered endpoint as an authorized, usable connection. Bonjour can report `kDNSServiceErr_PolicyDenied`; an `NWConnection` path can report `.localNetworkDenied`. If permission is revoked, an established local TCP connection closes. See [TN3179](https://developer.apple.com/documentation/technotes/tn3179-understanding-local-network-privacy) for platform and provider exceptions.

### Security scope in the 27 generation

**Reviewed September 8, 2026:** The new TLS 1.2 minimum and stricter ATS cipher/certificate requirements in the 27 release notes concern selected **system processes** for MDM, DDM, Automated Device Enrollment, configuration-profile installation, app installation, and software updates. They are not a universal behavioral change to every `NWConnection` or other app network call.

Use TLS appropriately for your own protocols and preserve server trust validation. Apple's [ATS documentation](https://developer.apple.com/documentation/security/preventing-insecure-network-connections) distinguishes the URL Loading System, where ATS applies, from lower-level Network and CFNetwork calls, where the app controls connection security. See [Security](Security.md) and [Device Management](DeviceManagement.md) for the targeted system-process changes and audit guidance.

## Topics

### Essentials
- **NWEndpoint** - A local or remote endpoint in a network connection.
- **NWParameters** - An object that stores the protocols to use for connections, options for sending data, and network path constraints.

### Connections and Listeners
- **NWConnection** - A bidirectional data connection between a local endpoint and a remote endpoint.
- **NWListener** - An object you use to listen for incoming network connections.
- **NWBrowser** - An object you use to browse for available network services.
- **NWConnectionGroup** - An object you use to communicate with a group of endpoints, such as an IP multicast group on a local network.
- **NWEthernetChannel** - Native macOS 10.15+ custom Ethernet-frame access, requiring `com.apple.developer.networking.custom-protocol`; not a cross-platform connection class.

### Network Protocols
- Configure protocol options to use with connections and listeners, and inspect the results of protocol handshakes.
- [Building a custom peer-to-peer protocol](https://developer.apple.com/documentation/network/building-a-custom-peer-to-peer-protocol) - The TicTacToe sample uses Bonjour/TLS between iOS/iPadOS peers and DeviceDiscoveryUI for Apple TV companions, including watchOS. Its deployment metadata starts at iOS/iPadOS/tvOS 16 and watchOS 9.
- **NWProtocolTCP** - A network protocol for connections that use the Transmission Control Protocol.
- **NWProtocolTLS** - A network protocol for connections that use Transport Layer Security.
- **NWProtocolQUIC** - A network protocol for connections that use the QUIC transport protocol.
- **NWProtocolUDP** - A network protocol for connections that use the User Datagram Protocol.
- **NWProtocolIP** - A network protocol for configuring the Internet Protocol on connections.
- **NWProtocolWebSocket** - A network protocol for connections that use WebSocket.
- **NWProtocolFramer** - A customizable network protocol for defining application message parsers.

### Network Security and Privacy

#### Security Options
- [Security options](https://developer.apple.com/documentation/network/security-options) - Configure security options for TLS handshakes.

#### Privacy Management
- [Privacy management](https://developer.apple.com/documentation/network/privacy-management) - Configure parameters related to user privacy.
- [Creating an Identity for Local Network TLS](https://developer.apple.com/documentation/network/creating-an-identity-for-local-network-tls) - Distribute a server identity and client trust anchor. Prefer correct DNS/IP subject alternative names and normal trust evaluation over a custom verification fallback.

### Paths and Interfaces
- **NWPath** - An object that contains information about the properties of the network that a connection uses, or that are available to your app.
- **NWPathMonitor** - An observer that you use to monitor and react to network changes.
- **NWInterface** - An interface that a network connection uses to send and receive data.

### Errors
- **NWError** - The errors returned by objects in the Network framework.

### Network Debugging
- [Choosing a Network Debugging Tool](https://developer.apple.com/documentation/network/choosing-a-network-debugging-tool) - Decide which tool works best for your network debugging problem.
- [Debugging HTTP Server-Side Errors](https://developer.apple.com/documentation/network/debugging-http-server-side-errors) - Understand HTTP server-side errors and how to debug them.
- [Debugging HTTPS Problems with CFNetwork Diagnostic Logging](https://developer.apple.com/documentation/network/debugging-https-problems-with-cfnetwork-diagnostic-logging) - Use CFNetwork diagnostic logging to investigate HTTP and HTTPS problems.
- [Recording a Packet Trace](https://developer.apple.com/documentation/network/recording-a-packet-trace) - Learn how to record a low-level trace of network traffic.
- [Taking Advantage of Third-Party Network Debugging Tools](https://developer.apple.com/documentation/network/taking-advantage-of-third-party-network-debugging-tools) - Learn about the available third-party network debugging tools.
- [Testing and Debugging L4S in Your App](https://developer.apple.com/documentation/network/testing-and-debugging-l4s-in-your-app) - Verify client, server, and bottleneck-network support; L4S does not provide a universal latency guarantee.

### C-Language Symbols
- [C-language symbols](https://developer.apple.com/documentation/network/c-language-symbols) - Access Network framework symbols used in C.

### Structures
- **nw_interface_radio_type_t**
- **nw_multipath_version_t**
- **nw_path_unsatisfied_reason_t**
- **nw_quic_stream_type_t**
- **Bonjour** - A browser that discovers Bonjour services.
- **BonjourListenerProvider** - Advertise a Bonjour service.
- **Coder** - Frames and encodes or decodes Codable messages.
- [DTLS](https://developer.apple.com/documentation/network/dtls) - A **27 beta** protocol-stack type for encrypted byte datagrams using Datagram Transport Layer Security.
- **DefaultProtocolStorage**
- **Framer** - An instance of a Framer protocol to load into a protocol stack.
- **IP** - The system definition of the Internet Protocol (IP).
- **NWParametersBuilder** - A generic structure that creates and configures NWParameters from a typed protocol stack.
- **NWTXTRecord** - A dictionary representing a TXT record in a DNS packet.
- **NetworkJSONCoder**
- **NetworkPropertyListCoder**
- **ProtocolMetadataBuilder** - A result builder for configuring metadata in send methods.
- **ProtocolStackBuilder** - A result builder for specifying and configuring protocol stacks.
- **ProxyConfiguration** - A proxy configuration for Relays, Oblivious HTTP, HTTP CONNECT, or SOCKSv5.
- **QUIC** - The system definition of the QUIC protocol.
- **QUICDatagram** - Sends and receives unreliable datagrams over QUIC via RFC 9221.
- **QUICStream** - A QUIC stream that runs over a QUIC connection.
- **TCP** - The system definition of the Transmission Control Protocol (TCP).
- **TLS** - The system definition of the Transport Layer Security (TLS) protocol.
- **TLV** - A Type-Length-Value (TLV) framing protocol.
- **TXTRecordDecoder**
- **UDP** - The system definition of the User Datagram Protocol (UDP).
- **UnexpectedEndpointType** - An error generated when an unexpected endpoint type is supplied.
- **WebSocket** - The system definition of the WebSocket protocol.
- **nw_link_quality_t**

### Classes
- **NWMultiplexGroup**
- **NetworkBrowser** - Discovers advertised services and devices on the network.
- [NetworkChannel](https://developer.apple.com/documentation/network/networkchannel) - The 26.0+ generic base class whose send/receive interface depends on its application protocol.
- **NetworkConnection** - Connects to an endpoint on the network to send and receive data.
- **NetworkListener** - Listens for incoming network connections.

### Reference
- **Network Constants** - Access Network framework constants used in C.
- **Network Functions** - Access Network framework functions used in C.
- **Network Data Types**

### Protocols
- **BrowserProvider** - Provides browsing behavior when creating NetworkBrowser instances.
- **Connectable** - Describes endpoints usable by NetworkConnection.
- **ConnectionStorage** - Additional storage within a connection.
- **DatagramProtocol** - Sends and receives datagrams, typically subject to a maximum size.
- **FramerProtocol** - Provides custom framing and serialization of messages.
- **ListenerProvider** - Configures the service a listener advertises.
- **MessageProtocol** - Sends and receives messages with protocol-specific metadata.
- **MultiplexProtocol** - A top-level protocol for multiplexed connections.
- **NWParametersProvider** - Generates NWParameters.
- **NetworkCoder**
- [NetworkDecoder](https://developer.apple.com/documentation/network/networkdecoder) - Decodes Data into a `Decodable` value using a throwing method; distinct from NetworkEncoder.
- [NetworkEncoder](https://developer.apple.com/documentation/network/networkencoder) - Encodes Encodable values into Data.
- **NetworkFixedWidthInteger**
- **NetworkMetadataProtocol** - A marker protocol for the metadata type associated with `NetworkProtocolOptions`.
- **NetworkProtocolOptions**
- **OneToOneProtocol** - A top-level protocol for nonmultiplexed connections.
- **StreamProtocol** - Sends and receives byte streams.

### Variables
- **kNWErrorDomainWiFiAware**
- **nw_error_domain_wifi_aware**
- **nw_link_quality_good**
- **nw_link_quality_minimal**
- **nw_link_quality_moderate**
- **nw_link_quality_unknown**

### Functions
- **nw_parameters_get_allow_ultra_constrained**
- **nw_parameters_set_allow_ultra_constrained**
- **nw_path_get_link_quality**
- **nw_path_is_ultra_constrained**
- **withNetworkConnection**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Network)*

*Security-scope sources: [ATS documentation](https://developer.apple.com/documentation/security/preventing-insecure-network-connections.md) and [iOS/iPadOS 27 release notes — Network Security](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes.md).*
