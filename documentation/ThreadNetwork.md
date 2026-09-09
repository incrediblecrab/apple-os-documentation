# ThreadNetwork

Create robust, smart device networks using Thread Border Routers.

**Core API declarations:** iOS 15.0+ | iPadOS 15.0+ | Mac Catalyst 15.0+ | macOS 13.0+ | visionOS 1.0+

The framework catalog lists later Catalyst 16.1 and macOS 14 baselines; `THClient` and `THCredentials` declare the versions above. Individual methods still need their own availability checks.

## Overview

Thread is an IP-based, low-power wireless mesh technology used by smart-home devices. Routing-capable members forward packets and can provide alternate paths when topology changes. End devices do not forward other devices' packets; simply adding more devices does not guarantee faster communication or eliminate every failure mode.

A network can split into partitions when groups lose radio connectivity. Each partition has its own leader and network data while retaining the network's security credentials; partitions can merge again when connectivity returns.

The **Thread Border Router** connects Thread to another IP network such as Wi-Fi or Ethernet. Examples include HomePod mini, HomePod (2nd generation), and Apple TV 4K (3rd generation) **Wi-Fi + Ethernet**. Do not assume every HomePod or Apple TV model includes Thread hardware.

Use **ThreadNetwork** to coordinate credentials and choose a network for your certified Border Router. The framework does not itself supply a hardware router or implement your device's Thread packet-forwarding stack.

### Credential permission and lifecycle

The Boolean `com.apple.developer.networking.manage-thread-network-credentials` entitlement supports development and testing; distribution access requires Apple's approval and the assigned distribution entitlement. Enabling the development capability alone is not distribution permission.

Preferred-network credentials require the person's consent. Retrieving credentials owned by your developer team does not require that same prompt and does not expose every other team's stored credentials. Treat denial, missing credentials, and stale cached data as recoverable outcomes. These secrets allow devices to join the network; do not expose them in logs.

Keep iCloud Keychain records synchronized when your Border Router's credentials change, and delete its stored record when it leaves the network. Before reusing cached preferred credentials, compare them with the current preferred network and request updated credentials when needed. The comparison method starts at iOS/iPadOS/Catalyst 15.5; preferred-network availability and active-credential queries start at 16.4. Their macOS and visionOS declarations are 13.0 and 1.0 respectively.

### Learn About Thread Network Device Roles

A Thread network can contain several types of devices that someone can deploy in many combinations:

**Thread Border Router**  
A device that connects Thread to an existing Wi-Fi or Ethernet network. It may be standalone or part of a multifunction product; multiple Border Routers can serve a network.

**Thread Leader**  
A self-elected routing device that manages network-wide configuration within its partition. There is one leader **per partition**, not necessarily one across all disconnected partitions sharing the same Thread credentials.

**End Device**  
A device attached to a parent routing device. It exchanges its own messages but does not forward packets for other devices.

**Sleepy End Device**  
A low-power end device whose radio normally sleeps and wakes to poll its parent and exchange messages. Battery-powered temperature and air-quality sensors are examples.

For routing roles and partitions, see [OpenThread's Node Roles and Types](https://openthread.io/guides/thread-primer/node-roles-and-types). For the protocol overview, see [What is Thread?](https://www.threadgroup.org/What-is-Thread/Overview).

**Note:** Thread standard is developed by the Thread Group, and that use of "Thread" to describe Border Routers is subject to Thread Group's Trademark and Certification Policies.

## Topics

### Setting Up Thread Border Routers
- [Getting started with ThreadNetwork](https://developer.apple.com/documentation/threadnetwork/getting-started-with-threadnetwork) - Configure development access and follow the conformance and distribution-entitlement process.
- [Configuring a Border Router](https://developer.apple.com/documentation/threadnetwork/configuring-a-border-router) - Set up or add a Border Router on a Thread network.
- [Managing Thread network credentials](https://developer.apple.com/documentation/threadnetwork/managing-thread-network-credentials) - Store, retrieve, update, and delete Thread network credentials on your Apple device.

### Managing Clients and Sharing Credentials
- [com.apple.developer.networking.manage-thread-network-credentials](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.networking.manage-thread-network-credentials) - The Boolean credential-management entitlement, with separate development and approved distribution access.
- **THClient** - A class that supports safely sharing Thread credentials between multiple clients.
- **THCredentials** - A class that contains credentials for a Thread network.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ThreadNetwork)*

*Topology and model qualifications: [OpenThread](https://openthread.io/guides/thread-primer/node-roles-and-types) and [Apple's Thread-enabled home-hub guidance](https://support.apple.com/en-us/102557).*
