# Multipeer Connectivity

Support peer-to-peer connectivity and the discovery of nearby devices.

**Platforms:** iOS 7.0+ | iPadOS 7.0+ | Mac Catalyst 13.0+ | macOS 10.10+ | tvOS 10.0+ | visionOS 1.0+

## Overview

The Multipeer Connectivity framework supports the discovery of services provided by nearby devices and supports communicating with those services through message-based data, streaming data, and resources (such as files). In iOS, the framework uses infrastructure Wi-Fi networks, peer-to-peer Wi-Fi, and Bluetooth personal area networks for the underlying transport. In macOS and tvOS, it uses infrastructure Wi-Fi, peer-to-peer Wi-Fi, and Ethernet.

**Important:** Apps that use the local network must provide a usage string in their Info.plist with the key `NSLocalNetworkUsageDescription`. Apps that use Bonjour must also declare the services they browse, using the `NSBonjourServices` key.

### Architecture

When working with the Multipeer Connectivity framework, your app must interact with several types of objects:

- Session objects (**MCSession**) support communication between connected peer devices
- Advertiser objects (**MCNearbyServiceAdvertiser**) tell nearby peers that your app is willing to join sessions
- Advertiser assistant objects (**MCAdvertiserAssistant**) provide the same functionality as advertiser objects with a standard user interface
- Browser objects (**MCNearbyServiceBrowser**) let your app search programmatically for nearby devices
- Browser view controller objects (**MCBrowserViewController**) provide a standard user interface for choosing nearby peers
- Peer IDs (**MCPeerID**) uniquely identify an app running on a device to nearby peers

### Discovery Phase and Session Phase

This framework is used in two phases: the discovery phase and the session phase.

In the discovery phase, your app uses an **MCNearbyServiceBrowser** object to browse for nearby peers, optionally using the **MCBrowserViewController** object to display a user interface. The app also uses an **MCNearbyServiceAdvertiser** object or an **MCAdvertiserAssistant** object to tell nearby peers that it is available.

After the user chooses which peers to add to a session, the app invites those peers to join the session. If the peer accepts the invitation, the browser establishes a connection with the advertiser and the session phase begins. In this phase, your app can perform direct communication to one or more peers within the session.

## Topics

### Classes
- **MCAdvertiserAssistant** - A convenience class that handles advertising, presents incoming invitations to the user, and handles users' responses
- **MCBrowserViewController** - Presents nearby devices to the user and enables the user to invite nearby devices to a session
- **MCNearbyServiceAdvertiser** - Publishes an advertisement for a specific service that your app provides through the Multipeer Connectivity framework
- **MCNearbyServiceBrowser** - Searches for services offered by nearby devices using infrastructure Wi-Fi, peer-to-peer Wi-Fi, and Bluetooth
- **MCPeerID** - Represents a peer in a multipeer session
- **MCSession** - Enables and manages communication among all peers in a Multipeer Connectivity session

### Protocols
- **MCAdvertiserAssistantDelegate** - Methods for handling advertising-related events
- **MCBrowserViewControllerDelegate** - Methods for handling events related to the MCBrowserViewController class
- **MCNearbyServiceAdvertiserDelegate** - Methods for handling events from the MCNearbyServiceAdvertiser class
- **MCNearbyServiceBrowserDelegate** - Methods for handling browser-related events
- **MCSessionDelegate** - Methods for handling session-related events

### Structures
- **MCError**

### Reference
- MultipeerConnectivity Enumerations
- MultipeerConnectivity Constants

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MultipeerConnectivity)*