# NetworkingDriverKit

Develop drivers for Ethernet networking devices.

**Platforms:** DriverKit 19.0+

## Overview

Use NetworkingDriverKit to develop drivers for USB Ethernet adapters. This framework extends the API of DriverKit, providing you with a service class for managing your networking driver. It also provides support for managing the memory you use to store packets, transferring those packets between the device and networking stack, and inspecting the Ethernet link status.

Note that Ethernet is the only networking interface currently supported by NetworkingDriverKit.

Develop your driver with DriverKit and NetworkingDriverKit. Use USBDriverKit to manage the connection to your hardware device. Include your driver inside your macOS app and use the System Extensions framework to install and upgrade the driver on the user's Mac.

> **Note:** NetworkingDriverKit is available on macOS.

## Topics

### Essentials
- **com.apple.developer.driverkit.family.networking** - A Boolean value that indicates whether to match the driver against devices that communicate using networking protocols.

### Samples
- [Connecting a network driver](https://developer.apple.com/documentation/networkingdriverkit/connecting_a_network_driver) - Create an Ethernet driver that interfaces with the system's network protocol stack.
- [DriverKit sample code](https://developer.apple.com/documentation/networkingdriverkit/driverkit_sample_code) - Explore projects that demonstrate how to write macOS device drivers with the DriverKit family of frameworks.

### Network Service
- **IOUserNetworkEthernet** - The object you use to manage the setup, configuration, and teardown of your networking driver.

### Packet Management
- **IOUserNetworkPacketBufferPool** - An object that manages the storage space for packets coming into and out of your driver.
- **IOUserNetworkPacket** - A network packet containing the data for your driver to process.
- **IOUserNetworkPacketDirection** - The direction in which the packet moves, relative to the device.

### Packet Queues
- **IOUserNetworkRxSubmissionQueue** - The queue that receives packets from the device.
- **IOUserNetworkRxCompletionQueue** - The queue you use to store packets that you successfully transferred to the networking stack.
- **IOUserNetworkTxSubmissionQueue** - The queue that receives packets from the networking stack.
- **IOUserNetworkTxCompletionQueue** - The queue you use to store packets that you successfully transferred to the device.
- **IOUserNetworkPacketQueue** - The base class for the queues that manage the packets moving to and from your device.

### Reference
- **NetworkingDriverKit Structures**
- **NetworkingDriverKit Data Types**
- **NetworkingDriverKit Constants**

### Classes
- **IOUserNetworkPacketPoller**

### Structures
- **IOUserNetworkEthernet_IVars**

### Macros
- **NDK_25**

### Enumeration Cases
- **kIOUserNetworkHWAssistLRONumSeg**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/NetworkingDriverKit)*