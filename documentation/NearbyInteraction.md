# Nearby Interaction

Locate and interact with nearby devices using identifiers, distance, and direction.

**Platforms:** iOS 14.0+ | iPadOS 14.0+ | Mac Catalyst 14.0+ | macOS 11.0+ | watchOS 8.0+

## Overview

Use Nearby Interaction in your app to acquire the position of devices with an Ultra Wideband (UWB) chip, such as iPhone 11 or later, Apple Watch, and third-party accessories. To participate in an interaction, devices in physical proximity run an app and share their position and device tokens that uniquely identify them. When the app runs in the foreground, Nearby Interaction notifies the interaction session of the peer's location by reporting the peer's direction and distance in meters.

Apple devices use the high-frequency capabilities of the UWB chip to share their positions in the physical environment and enable fluid, interactive sessions. For example:

- A multiuser AR experience that places virtual water balloons in the hands of its participants
- A taxi or rideshare app that employs a peer user's direction in real time to identify the relative locations of a driver and a customer
- A game app that enables a user to control a paddle with their device and respond to a moving ball on the peer user's screen

For guidance on designing nearby interactions, see the Human Interface Guidelines > Nearby interactions.

### Interact with Apple Watch

The UWB chip-capable Apple Watch running watchOS 8 supports Nearby Interaction sessions. Apps share discovery tokens to begin an interaction session in watchOS using a custom server, Core Bluetooth, LAN (TCP/UDP), or Watch Connectivity.

Nearby Interaction in iOS provides a peer device's distance and direction, whereas Nearby Interaction in watchOS provides only a peer device's distance.

### Interact with Third-Party Devices

In iOS 15 and later and watchOS 8 and later, U1-enabled devices can interact with third-party accessories you partner with or develop using the Ultra Wideband (UWB) third-party device specification. To begin an interaction session with a third-party accessory, establish a data link with the accessory, receive its configuration data, and create an **NINearbyAccessoryConfiguration**.

**Note:** The `supportsPreciseDistanceMeasurement` function returns false in Mac apps built with Mac Catalyst. For a compatible iPad or iPhone app running in visionOS, framework features are unavailable, and any calls you make to the framework APIs have no effect.

### Using Nearby Interaction in the Background

While your app is in the foreground, it can freely use Nearby Interaction to perform ranging between UWB devices. When the app moves to the background, it can perform UWB ranging only with devices that are Bluetooth Low Energy (LE)-paired and connected.

In iOS 18.4 and later, your app can continue ranging in the background with any supported device if the app starts a Live Activity as it goes to the background. For more information about creating Live Activities, see ActivityKit.

**Note:** Both these forms of background activity require that you enable the appropriate capability in Xcode. In your target's Signing & Capabilities tab, add the "Background Modes" capability, then select "Uses Nearby Interaction".

## Topics

### Setup
- [Initiating and maintaining a session](https://developer.apple.com/documentation/nearbyinteraction/initiating_and_maintaining_a_session) - Measure the relative position of a nearby device and coach the user to sustain interaction
- **NISession** - An object that identifies a unique connection between two peer devices

### Authorization
- **NSNearbyInteractionUsageDescription** - A request for user permission to begin an interaction session with nearby devices

### Phone Interaction
- [Implementing Interactions Between Users in Close Proximity](https://developer.apple.com/documentation/nearbyinteraction/implementing_interactions_between_users_in_close_proximity) - Enable devices to access relative positioning information
- [Discovering peers with Multipeer Connectivity](https://developer.apple.com/documentation/nearbyinteraction/discovering_peers_with_multipeer_connectivity) - Exchange discovery tokens over the local network
- [Extending advanced direction finding and ranging](https://developer.apple.com/documentation/nearbyinteraction/extending_advanced_direction_finding_and_ranging) - Extend your app's direction finding capabilities with data from Ultra Wideband devices
- **NINearbyPeerConfiguration** - A configuration that enables interaction between iPhone or Apple Watch devices

### Watch Interaction
- [Implementing proximity-based interactions between a phone and watch](https://developer.apple.com/documentation/nearbyinteraction/implementing_proximity-based_interactions_between_a_phone_and_watch) - Interact with a nearby Apple Watch by measuring its distance to a paired iPhone

### Third-Party Accessories
- [Implementing spatial interactions with third-party accessories](https://developer.apple.com/documentation/nearbyinteraction/implementing_spatial_interactions_with_third-party_accessories) - Establish a connection with a nearby accessory to receive periodic measurements of its distance from the user
- **NINearbyAccessoryConfiguration** - A configuration that enables interaction between iPhone and third-party accessories

### Periodic Updates
- **NINearbyObject** - Location information for a peer device in an interaction session
- **NISessionDelegate** - An object that monitors and reacts to session updates

### Camera Assistance
- [Finding devices with precision](https://developer.apple.com/documentation/nearbyinteraction/finding_devices_with_precision) - Leverage the spatial awareness of ARKit and Apple Ultra Wideband Chips in your app to guide users to a nearby device
- **NIAlgorithmConvergence** - An object that provides the state and reason for user coaching recommendations
- **NIAlgorithmConvergenceStatus** - The possible states of Camera Assistance

### Errors
- **NIError** - An error Nearby Interaction reports
- **Code** - Codes that identify errors in Nearby Interaction
- **NIErrorDomain** - A unique error domain for Nearby Interaction

### Deprecated
- **NSNearbyInteractionAllowOnceUsageDescription** - A one-time request for user permission to begin an interaction session with nearby devices (Deprecated)

### Beta Features
- **NIDLTDOAConfiguration** - A session configuration that enables UWB Down Link Time Difference of Arrival(DL-TDoA) ranging with nearby anchors (Beta)
- **NIDLTDOAMeasurement** - Represents a single measurement relative to a DL-TDOA anchor (Beta)
- **NIDLTDOACoordinatesType** - The coordinate types of DL-TDOA measurement updates that Nearby Interaction supports (Beta)
- **NIDLTDOAMeasurementType** - The measurement types of DL-TDOA measurement updates that Nearby Interaction supports (Beta)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/NearbyInteraction)*