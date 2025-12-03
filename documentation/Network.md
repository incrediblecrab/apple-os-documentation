# Network

Create network connections to send and receive data using transport and security protocols.

**Platforms:** iOS 12.0+ | iPadOS 12.0+ | Mac Catalyst 13.0+ | macOS 10.14+ | tvOS 12.0+ | visionOS 1.0+ | watchOS 6.0+

## Overview

Use this framework when you need direct access to protocols like TLS, TCP, and UDP for your custom application protocols. Continue to use URLSession, which is built upon this framework, for loading HTTP- and URL-based resources. For in-depth advice on where to start with networking, see TN3151: Choosing the right networking API.

> **Note:** watchOS supports Network framework for specific use cases. For more details, see TN3135: Low-level networking on watchOS.

## Topics

### Essentials
- **NWEndpoint** - A local or remote endpoint in a network connection.
- **NWParameters** - An object that stores the protocols to use for connections, options for sending data, and network path constraints.

### Connections and Listeners
- **NWConnection** - A bidirectional data connection between a local endpoint and a remote endpoint.
- **NWListener** - An object you use to listen for incoming network connections.
- **NWBrowser** - An object you use to browse for available network services.
- **NWConnectionGroup** - An object you use to communicate with a group of endpoints, such as an IP multicast group on a local network.
- **NWEthernetChannel** - An object you use to send and receive custom Ethernet frames.

### Network Protocols
- Configure protocol options to use with connections and listeners, and inspect the results of protocol handshakes.
- [Building a custom peer-to-peer protocol](https://developer.apple.com/documentation/network/building_a_custom_peer-to-peer_protocol) - Use networking frameworks to create a custom protocol for playing a game across iOS, iPadOS, watchOS, and tvOS devices.
- **NWProtocolTCP** - A network protocol for connections that use the Transmission Control Protocol.
- **NWProtocolTLS** - A network protocol for connections that use Transport Layer Security.
- **NWProtocolQUIC** - A network protocol for connections that use the QUIC transport protocol.
- **NWProtocolUDP** - A network protocol for connections that use the User Datagram Protocol.
- **NWProtocolIP** - A network protocol for configuring the Internet Protocol on connections.
- **NWProtocolWebSocket** - A network protocol for connections that use WebSocket.
- **NWProtocolFramer** - A customizable network protocol for defining application message parsers.

### Network Security and Privacy

#### Security Options
- Configure security options for TLS handshakes.

#### Privacy Management
- Configure parameters related to user privacy.
- [Creating an Identity for Local Network TLS](https://developer.apple.com/documentation/network/creating_an_identity_for_local_network_tls) - Learn how to create and use a digital identity in your application for local network TLS.

### Paths and Interfaces
- **NWPath** - An object that contains information about the properties of the network that a connection uses, or that are available to your app.
- **NWPathMonitor** - An observer that you use to monitor and react to network changes.
- **NWInterface** - An interface that a network connection uses to send and receive data.

### Errors
- **NWError** - The errors returned by objects in the Network framework.

### Network Debugging
- [Choosing a Network Debugging Tool](https://developer.apple.com/documentation/network/choosing_a_network_debugging_tool) - Decide which tool works best for your network debugging problem.
- [Debugging HTTP Server-Side Errors](https://developer.apple.com/documentation/network/debugging_http_server-side_errors) - Understand HTTP server-side errors and how to debug them.
- [Debugging HTTPS Problems with CFNetwork Diagnostic Logging](https://developer.apple.com/documentation/network/debugging_https_problems_with_cfnetwork_diagnostic_logging) - Use CFNetwork diagnostic logging to investigate HTTP and HTTPS problems.
- [Recording a Packet Trace](https://developer.apple.com/documentation/network/recording_a_packet_trace) - Learn how to record a low-level trace of network traffic.
- [Taking Advantage of Third-Party Network Debugging Tools](https://developer.apple.com/documentation/network/taking_advantage_of_third-party_network_debugging_tools) - Learn about the available third-party network debugging tools.
- [Testing and Debugging L4S in Your App](https://developer.apple.com/documentation/network/testing_and_debugging_l4s_in_your_app) - Learn how to verify your app on an L4S-capable host and network to improve your app's responsiveness.

### C-Language Symbols
- Access Network framework symbols used in C.

### Structures
- **nw_interface_radio_type_t**
- **nw_multipath_version_t**
- **nw_path_unsatisfied_reason_t**
- **nw_quic_stream_type_t**
- **Bonjour** - A browser that discovers Bonjour services.- **BonjourListenerProvider** - Advertise a Bonjour service.- **Coder** - A protocol that frames and encodes/decodes Codable types.- **DefaultProtocolStorage**- **Framer** - An instance of a Framer protocol to load into a protocol stack.- **IP** - The system definition of the Internet Protocol (IP).- **NWParametersBuilder** - An opaque class that is responsible for creating and configuring NWParameters based on the parameterized protocol stack.- **NWTXTRecord** - A dictionary representing a TXT record in a DNS packet.
- **NetworkJSONCoder**- **NetworkPropertyListCoder**- **ProtocolMetadataBuilder** - A resultBuilder for configuring metadata in send methods in a declarative way.- **ProtocolStackBuilder** - A resultBuilder for specifying and configuring protocol stacks in a declarative way- **ProxyConfiguration** - A proxy configuration for Relays, Oblivious HTTP, HTTP CONNECT, or SOCKSv5.
- **QUIC** - The system definition of the QUIC protocol.- **QUICDatagram** - Send and receive unreliable datagrams over QUIC via RFC 9221- **QUICStream** - A QUIC stream that runs over a QUIC connection.- **TCP** - The system definition of the Transmission Control Protocol (TCP).- **TLS** - The system definition of the Transport Layer Security (TLS) protocol.- **TLV** - A Type-Length-Value (TLV) framing protocol.- **TXTRecordDecoder**
- **UDP** - The system definition of the User Datagram Protocol (UDP).- **UnexpectedEndpointType** - An error generated when an unexpected endpoint type is supplied.- **WebSocket** - The system definition of the WebSocket protocol.- **nw_link_quality_t**

### Classes
- **NWMultiplexGroup**
- **NetworkBrowser** - Discover advertised services and devices on the network.- **NetworkConnection** - Connect to an endpoint on the network to send and receive data.- **NetworkListener** - Listen for incoming network connections.
### Reference
- **Network Constants** - Access Network framework constants used in C.
- **Network Functions** - Access Network framework functions used in C.
- **Network Data Types**

### Protocols
- **BrowserProvider** - BrowserProviders can be used when creating NetworkBrowsers.- **Connectable** - Describes types that can be used to make NetworkConnections.- **ConnectionProtocol**- **ConnectionStorage** - Types that conform to ConnectionStorage can be used as additional storage within a connection.- **DatagramProtocol** - Types that conform to DatagramProtocol send and receive messages with minimal or no metadata, usually constrained to a fixed maximum size.- **FramerProtocol** - Framer protocols allow custom framing and serialization of messages on a connection.- **ListenerProvider** - Extensible support for configuring advertise descriptors to define the service a listener should advertise.- **MessageProtocol** - Types that conform to MessageProtocol send and receive messages. The conforming type is responsible for specifying its message-specific metadata.- **MultiplexProtocol** - Types that conform to MultiplexProtocol are allowed to be the top protocol in a network protocol stack for multiplexing network connection objects.- **NWParametersProvider** - Types that conform to the NWParametersProvider protocol can be used to generate an NWParameters.- **NetworkCoder**- **NetworkDecoder** - A type that conforms to the NetworkEncoder protocol can decode data to an Encodable object- **NetworkEncoder** - A type that conforms to the NetworkEncoder protocol can encode a Encodable object to Data- **NetworkFixedWidthInteger**- **NetworkMetadataProtocol** - Types that conform to NetworkProtocolOptions can be used when configuring protocol stacks.- **NetworkProtocolOptions**- **OneToOneProtocol** - Types that conform to OneToOneProtocol are allowed to be the top protocol in a network protocol stack for non-multiplexed connections.- **StreamProtocol** - Types that conform to the StreamProtocol protocol expose methods for sending and receiving byte streams.- **SubConnectionProtocol**
### Variables
- **kNWErrorDomainWiFiAware**- **nw_error_domain_wifi_aware**- **nw_link_quality_good**
- **nw_link_quality_minimal**
- **nw_link_quality_moderate**
- **nw_link_quality_unknown**

### Functions
- **nw_parameters_get_allow_ultra_constrained**- **nw_parameters_set_allow_ultra_constrained**- **nw_path_get_link_quality**- **nw_path_is_ultra_constrained**- **withNetworkConnection**
### Enumerations
- **AdvertisedRoute**
---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Network)*