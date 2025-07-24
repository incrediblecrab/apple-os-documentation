# vmnet

Connect with network interfaces to read and write packets on guest operating systems.

**Platforms:** Mac Catalyst 13.0+ | macOS 10.10+

## Overview

The vmnet framework is an API for virtual machines to read and write packets.

The API allows a Guest OS interface to be in host mode or shared mode. Interfaces in host mode can communicate with the native host system and other interfaces running in host mode. In shared mode, the network interface can send and receive packets to the Internet, the native host, and other interfaces running in sharing mode.

**Note:** For more information about virtualization technologies, see the Hypervisor framework.

### Requirements

The vmnet framework has the following requirements:

**Entitlements**  
A sandboxed user space process must have the com.apple.vm.networking entitlement in order to use vmnet API.

### Architecture

The VM Network API provides support for an interface in the guest operating system. The API provides the MAC address and MTU that needs to be configured on the guest OS interface. The interface receives a private IPv4 address via DHCP. IPv4 traffic originating from the guest operating system must use the private IPv4 address. Packets sent from a different IPv4 address are dropped by the system.

You can create a maximum of 32 interfaces with a limit of 4 per guest operating system. Each read/write call allows up to 200 packets to be read or written for a maximum of 256KB. Each packet written should be a complete ethernet frame.

## Topics

### Essentials
- **com.apple.vm.networking** - A Boolean that indicates whether the app manages virtual network interfaces without escalating privileges to the root user.

### Starting and Stopping Interfaces
- **vmnet_start_interface** - Starts host or shared mode on an interface with a specified configuration.
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
- **vmnet_enable_virtio_header_key**
- **vmnet_read_max_packets_key**
- **vmnet_write_max_packets_key**

### Functions
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