# ThreadNetwork

Create robust, smart device networks using Thread Border Routers.

**Platforms:** iOS 15.0+ | iPadOS 15.0+ | Mac Catalyst 16.1+ | macOS 14.0+ | visionOS 1.0+

## Overview

The Thread standard is a low-power, wireless mesh networking protocol that runs over standard Internet protocols that allows smart home devices — such as Apple Home—compatible devices — to communicate with each other. Mesh networks are peer-to-peer networks that don't have a single, centrally defined router, eliminating the risk of a single point of failure. They can dynamically reconfigure themselves and discover nearby peer devices with shared credentials. This allows them to maintain communication even when some devices go offline.

The robustness of Thread relies on member devices forwarding packets to their neighbors; this creates a mesh that strengthens and increases its reliability as people add more devices. The mesh can also provide faster communication, especially over large networks, because there are more paths for messages to take across the network.

The **Thread Border Router** hardware device is a key element of Thread networks. It routes IP traffic between Thread and Wi-Fi or Ethernet networks, and enables iOS devices to communicate with Thread devices. HomePod and HomePod mini are examples of Border Routers.

To create your own Thread Border Router, use the **ThreadNetwork** framework to configure and manage your router. The ThreadNetwork framework helps you choose the right Thread network for your certified Thread Border Router.

### Learn About Thread Network Device Roles

A Thread network can contain several types of devices that someone can deploy in many combinations:

**Thread Border Router**  
A device that provides a connection between the Thread network and an existing WiFi or Ethernet network. These devices may be standalone, acting solely as routers, or they may support additional functionality. For example, HomePod (second Generation), HomePod Mini, and AppleTV 4K are all examples of Thread Border Routers.

**Thread Leader**  
A device that manages routers on a Thread network. A Thread network can only have one Thread Leader at any time; member devices select a Thread Leader based on various routing characteristics of the network in order to optimize performance.

**End Device**  
Thread devices located at the endpoints of a Thread network. They can communicate directly with other Thread devices, but don't operate as routers forwarding packets on their behalf.

**Sleepy End Device**  
End devices that run in low-power mode and are often battery powered. To conserve power they generally only wake up occasionally (which is why they're referred to as "sleepy") to report whatever data the device collects. Examples of sleepy devices include battery-powered temperature sensors or air quality monitors.

To learn more about Thread, visit the [OpenThread Guides](https://openthread.io/guides) and [What is Thread?](https://www.threadgroup.org/What-is-Thread).

**Note:** Thread standard is developed by the Thread Group, and that use of "Thread" to describe Border Routers is subject to Thread Group's Trademark and Certification Policies.

## Topics

### Setting Up Thread Border Routers
- [Getting started with ThreadNetwork](https://developer.apple.com/documentation/threadnetwork/getting_started_with_threadnetwork) - Create a plan to build, test, and deploy your Thread Border Router app.
- [Configuring a Border Router](https://developer.apple.com/documentation/threadnetwork/configuring_a_border_router) - Set up or add a Border Router on a Thread network.
- [Managing Thread network credentials](https://developer.apple.com/documentation/threadnetwork/managing_thread_network_credentials) - Store, retrieve, update, and delete Thread network credentials on your Apple device.

### Managing Clients and Sharing Credentials
- **com.apple.developer.networking.manage-thread-network-credentials** - A Boolean value that indicates whether the app can use ThreadNetwork.
- **THClient** - A class that supports safely sharing Thread credentials between multiple clients.
- **THCredentials** - A class that contains credentials for a Thread network.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ThreadNetwork)*