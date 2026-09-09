# vmnet

Connect with network interfaces to read and write packets on guest operating systems.

**Platforms:** macOS 10.10+

**Availability qualification:** Apple's catalog lists Mac Catalyst 13.0, but the public macOS 26.5 SDK explicitly rejects both `vmnet_start_interface` and the newer network-configuration API for Mac Catalyst. This reference covers native macOS use; the catalog listing is not evidence of a usable Catalyst interface.

## Overview

The vmnet framework is an API for virtual machines to read and write packets.

Interfaces support three modes:

- **Host:** communication with the host and eligible peer interfaces, without an external-network connection.
- **Shared:** external connectivity through NAT, plus host and eligible peer communication.
- **Bridged:** direct bridging to an eligible physical interface; macOS 10.15+.

Subnet selection and interface isolation affect which peers can communicate. Use `vmnet_copy_shared_interface_list` to find eligible bridged interfaces rather than assuming every physical interface is usable. The macOS 26 network-object configuration APIs described below accept host or shared mode; do not pass bridged mode merely because it exists in the older mode enumeration.

**Note:** For more information about virtualization technologies, see the Hypervisor framework.

### Requirements

The vmnet framework has the following requirements:

**Entitlements**  
The Boolean [`com.apple.vm.networking`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.vm.networking) entitlement enables virtual networking without escalating to root. It defaults to `NO` and is restricted to developers of virtualization software; Apple's reference directs applicants to their Apple representative. Handle missing authorization instead of assuming that a virtualization or sandbox entitlement grants network access.

### Architecture

Configure the guest with the interface parameters returned by vmnet, including MTU and the MAC address when automatic allocation is enabled. The default host/shared path uses private IPv4 addressing and DHCP. This is not a universal DHCP-only contract: custom IPv4 ranges permit static assignments outside the DHCP pool, isolated host networks can omit DHCP, and the macOS 26 configuration API can disable DHCP explicitly. Use source addresses appropriate to the selected network; default-interface source-address checks can drop invalid traffic.

Size I/O from the interface's reported limits, not a fixed packet-count or byte-budget assumption. `vmnet_read_max_packets_key` and `vmnet_write_max_packets_key` are available in macOS 15; `vmnet_max_packet_size_key` bounds each packet. Reads report the actual packet count, which may be zero. Supply complete Ethernet frames and handle oversized packets, too many packets, exhausted buffers, and interface-creation failures.

The macOS 15.4 `vmnet_enable_virtio_header_key` option adds a **12-byte Virtio network header** to every packet. Include those bytes in buffer sizing and do not combine this option with `vmnet_enable_checksum_offload_key`.

### Interface and network lifecycle

For either starting API, check the immediate result and wait for successful asynchronous setup before using the interface. Register or disable event callbacks with the documented queue/callback pairing. After `vmnet_stop_interface`, further packet I/O fails.

In macOS 26+, create a `vmnet_network_configuration_ref`, customize it, and create a `vmnet_network_ref` before starting interfaces with `vmnet_interface_start_with_network`. The network object owns its resource reservations. A successfully started interface retains that object; stopping the interface releases its reference. Release independently owned Core Foundation configuration/network references when no longer needed.

Configuration functions control NAT44/NAT66, DHCP, DNS proxying, router advertisements, subnets, MTU, reservations, and forwarding. Treat returned status codes, `NULL` objects, authorization failures, and conflicting sharing services as real failure paths. These 26+ operations are not part of the framework's 10.10 baseline.

## Topics

### Essentials
- **com.apple.vm.networking** - A Boolean that indicates whether the app manages virtual network interfaces without escalating privileges to the root user.

### Starting and Stopping Interfaces
- **vmnet_start_interface** - Starts an interface with a specified configuration, including supported bridged-mode configurations on macOS 10.15+.
- **vmnet_interface_set_event_callback** - Schedules a callback to be executed when events for the specified interface are received.
- **vmnet_stop_interface** - Stops the interface.

### Reading and Writing Packets
- **vmnet_read** - Attempts to read a specified number of packets from an interface.
- **vmnet_write** - Attempts to write specified packets to an interface.

### Data Types
- **vmnet_return_t** - Values returned by functions in the vmnet Framework.
- **vmpktdesc** - Describes a packet.
- **interface_ref** - A virtual network interface.
- **interface_event_t** - Interface event types.
- **operating_modes_t** - The operating modes for an interface.

### Constants
- [interface_desc XPC Dictionary Keys](https://developer.apple.com/documentation/vmnet/interface_desc_xpc_dictionary_keys) - XPC dictionary keys supported by the interface_desc parameter passed to the vmnet function to describe the parameters of the network interface.
- [interface_param XPC Dictionary Keys](https://developer.apple.com/documentation/vmnet/interface_param_xpc_dictionary_keys) - XPC dictionary keys used by the interface_param argument returned by the completion handler of the vmnet function that describes the parameters that should be used to configure the network interface.
- [event XPC Dictionary](https://developer.apple.com/documentation/vmnet/event_xpc_dictionary) - XPC dictionary keys used by the event value returned to the client in the handler callback specified by the vmnet function that provides information about the callback event.

### Reference
- [vmnet Constants](https://developer.apple.com/documentation/vmnet/vmnet_constants)
- [vmnet Functions](https://developer.apple.com/documentation/vmnet/vmnet_functions)
- [vmnet Data Types](https://developer.apple.com/documentation/vmnet/vmnet_data_types)

### Variables
- **vmnet_enable_virtio_header_key** - Enables the packet-header option; macOS 15.4+.
- **vmnet_read_max_packets_key** - Maximum packet count for a read; macOS 15+.
- **vmnet_write_max_packets_key** - Maximum packet count for a write; macOS 15+.

### Network-object functions — macOS 26+
- **vmnet_interface_start_with_network**
- **vmnet_network_configuration_add_dhcp_reservation**
- **vmnet_network_configuration_add_port_forwarding_rule**
- **vmnet_network_configuration_create**
- **vmnet_network_configuration_disable_dhcp**
- **vmnet_network_configuration_disable_dns_proxy**
- **vmnet_network_configuration_disable_nat44**
- **vmnet_network_configuration_disable_nat66**
- **vmnet_network_configuration_disable_router_advertisement**
- **vmnet_network_configuration_set_external_interface**
- **vmnet_network_configuration_set_ipv4_subnet**
- **vmnet_network_configuration_set_ipv6_prefix**
- **vmnet_network_configuration_set_mtu**
- **vmnet_network_copy_serialization**
- **vmnet_network_create**
- **vmnet_network_create_with_serialization**
- **vmnet_network_get_ipv4_subnet**
- **vmnet_network_get_ipv6_prefix**

### Type Aliases
- **vmnet_mode_t**
- **vmnet_network_configuration_ref**
- **vmnet_network_ref**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/vmnet)*
