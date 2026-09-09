# Multipeer Connectivity

Support peer-to-peer connectivity and the discovery of nearby devices.

**Original availability:** iOS 7.0+ | iPadOS 7.0+ | Mac Catalyst 13.1+ | macOS 10.10+ | tvOS 10.0+ | visionOS 1.0+

**Status at the September 8, 2026 cutoff:** Xcode 27 deprecates the framework, with `MCSession` carrying 27.0 deprecation annotations on the listed platforms. Deprecation is not immediate removal. Plan migration using [TN3213: Moving from Multipeer Connectivity to Network framework](https://developer.apple.com/documentation/technotes/tn3213-moving-from-multipeer-connectivity-to-network-framework); the legacy reference below remains useful for existing applications.

## Overview

The Multipeer Connectivity framework discovers nearby services and exchanges messages, streams, and resources such as files. The framework selects the underlying local transport, including infrastructure and peer-to-peer Wi-Fi; macOS and tvOS also support Ethernet. Do not design application behavior around a guaranteed particular radio or link.

**Important:** Apps that use the local network must provide a usage string in their Info.plist with the key `NSLocalNetworkUsageDescription`. Apps that use Bonjour must also declare the services they browse, using the `NSBonjourServices` key.

These declarations describe local-network use; they do not constitute user consent. Handle denied access and peer discovery failures.

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

On iOS, entering the background stops advertising and browsing and disconnects open sessions. Advertising and browsing resume on return to the foreground, but the app must reestablish its sessions; discovery does not guarantee persistent background communication.

## Topics

### Classes
- **MCAdvertiserAssistant** - A convenience class that handles advertising, presents incoming invitations to the user, and handles users' responses
- **MCBrowserViewController** - Presents nearby devices to the user and enables the user to invite nearby devices to a session
- **MCNearbyServiceAdvertiser** - Publishes an advertisement for a specific service that your app provides through the Multipeer Connectivity framework
- **MCNearbyServiceBrowser** - Searches for services offered by nearby devices using the framework's supported local transports.
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
