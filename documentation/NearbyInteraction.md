# Nearby Interaction

Locate and interact with nearby devices using identifiers, distance, and direction.

**SDK catalog:** iOS 14.0+ | iPadOS 14.0+ | Mac Catalyst 14.0+ | macOS 11.0+ | watchOS 8.0+. Hardware and individual feature support must be checked separately.

## Overview

Nearby Interaction reports relative position information for supported nearby devices and accessories. In an Apple-device UWB interaction, apps exchange discovery tokens through a separate data link and configure a ranging session. Accessory interactions instead exchange the accessory protocol's configuration data. A product-family name alone is not a hardware capability check.

Check `NISession.deviceCapabilities` on iOS 16/watchOS 9 and later, using the legacy `isSupported` check for earlier supported releases. Distance is measured in meters. In Swift, distance or direction can be `nil` when a peer is out of range or outside the supported line of sight; do not assume every update supplies both.

Supply `NSNearbyInteractionUsageDescription`, and handle `NIError.Code.userDidNotAllow`, invalid configurations, suspension, and peer removal. The system remembers the person's sharing decision in Settings and checks it for later sessions; previously granted access is not permanent.

Apple devices use the high-frequency capabilities of the UWB chip to share their positions in the physical environment and enable fluid, interactive sessions. For example:

- A multiuser AR experience that places virtual water balloons in the hands of its participants
- A taxi or rideshare app that employs a peer user's direction in real time to identify the relative locations of a driver and a customer
- A game app that enables a user to control a paddle with their device and respond to a moving ball on the peer user's screen

For guidance on designing nearby interactions, see the Human Interface Guidelines > Nearby interactions.

### Interact with Apple Watch

The UWB chip-capable Apple Watch running watchOS 8 supports Nearby Interaction sessions. Apps share discovery tokens to begin an interaction session in watchOS using a custom server, Core Bluetooth, LAN (TCP/UDP), or Watch Connectivity.

Nearby Interaction in iOS provides a peer device's distance and direction, whereas Nearby Interaction in watchOS provides only a peer device's distance.

### Interact with Third-Party Devices

In iOS 15 and later and watchOS 8 and later, supported UWB-enabled devices can interact with third-party accessories using the Nearby Interaction Accessory Protocol Specification. Establish a data link, receive the accessory's configuration data, and create an **NINearbyAccessoryConfiguration**. Send the shareable configuration supplied by the session delegate back to the accessory as required by the protocol.

**Note:** The `supportsPreciseDistanceMeasurement` capability property returns false in Mac apps built with Mac Catalyst. For a compatible iPad or iPhone app running in visionOS, framework features are unavailable, and any calls you make to the framework APIs have no effect.

The [27 Channel Sounding sample](https://developer.apple.com/documentation/corebluetooth/measuring-distance-between-devices-using-channel-sounding) demonstrates a separate Bluetooth ranging path through Nearby Interaction, with a horizontal angle when camera assistance is available. It requires compatible Channel Sounding hardware and AccessorySetupKit pairing, not just an arbitrary BLE connection or a UWB discovery token.

### Using Nearby Interaction in the Background

While your app is in the foreground, it can freely use Nearby Interaction to perform ranging between UWB devices. When the app moves to the background, it can perform UWB ranging only with devices that are Bluetooth Low Energy (LE)-paired and connected.

For the Bluetooth-accessory background path on iOS 16 and later, use `NINearbyAccessoryConfiguration.init(accessoryData:bluetoothPeerIdentifier:)` with the accessory's Bluetooth identifier.

In iOS 18.4 and later, your app can continue ranging in the background with any supported device if the app starts a Live Activity as it goes to the background. For more information about creating Live Activities, see ActivityKit.

**Note:** Both these forms of background activity require that you enable the appropriate capability in Xcode. In your target's Signing & Capabilities tab, add the "Background Modes" capability, then select "Uses Nearby Interaction".

Handle suspension and loss of the required connection or Live Activity; these paths do not promise continuous execution for every session.

## Topics

### Setup
- [Initiating and maintaining a session](https://developer.apple.com/documentation/nearbyinteraction/initiating-and-maintaining-a-session) - Measure the relative position of a nearby device and coach the user to sustain interaction
- **NISession** - An object that identifies a unique connection between two peer devices

### Authorization
- **NSNearbyInteractionUsageDescription** - The Info.plist purpose string shown in the system's permission request.

### Phone Interaction
- [Implementing Interactions Between Users in Close Proximity](https://developer.apple.com/documentation/nearbyinteraction/implementing-interactions-between-users-in-close-proximity) - Enable devices to access relative positioning information
- [Discovering peers with Multipeer Connectivity](https://developer.apple.com/documentation/nearbyinteraction/discovering-peers-with-multipeer-connectivity) - The legacy token-exchange sample; Multipeer Connectivity is deprecated in 27, so consider Network for new discovery transport.
- [Extending advanced direction finding and ranging](https://developer.apple.com/documentation/nearbyinteraction/extending-advanced-direction-finding-and-ranging) - Extend your app's direction finding capabilities with data from Ultra Wideband devices
- **NINearbyPeerConfiguration** - A configuration that enables interaction between iPhone or Apple Watch devices

### Watch Interaction
- [Implementing proximity-based interactions between a phone and watch](https://developer.apple.com/documentation/nearbyinteraction/implementing-proximity-based-interactions-between-a-phone-and-watch) - Interact with a nearby Apple Watch by measuring its distance to a paired iPhone

### Third-Party Accessories
- [Implementing spatial interactions with third-party accessories](https://developer.apple.com/documentation/nearbyinteraction/implementing-spatial-interactions-with-third-party-accessories) - Establish a connection with a nearby accessory to receive periodic measurements of its distance from the user
- **NINearbyAccessoryConfiguration** - A configuration that enables interaction between iPhone and third-party accessories

### Periodic Updates
- **NINearbyObject** - Location information for a peer device in an interaction session
- **NISessionDelegate** - An object that monitors and reacts to session updates

### Camera Assistance
- [Finding devices with precision](https://developer.apple.com/documentation/nearbyinteraction/finding-devices-with-precision) - Use supported camera assistance, introduced in iOS 16, to improve ranging guidance.
- **NIAlgorithmConvergence** - An object that provides the state and reason for user coaching recommendations
- **NIAlgorithmConvergenceStatus** - The possible states of Camera Assistance

### Errors
- **NIError** - An error Nearby Interaction reports
- **NIError.Code** - Codes that identify errors in Nearby Interaction
- **NIErrorDomain** - A unique error domain for Nearby Interaction

### Deprecated
- **NSNearbyInteractionAllowOnceUsageDescription** - A one-time request for user permission to begin an interaction session with nearby devices (Deprecated)

### DL-TDOA Features

The DL-TDOA configuration types begin at 26. The [DL-TDOA guide](https://developer.apple.com/documentation/nearbyinteraction/dl-tdoa-ranging) states that 27 removes the DL-TDOA entitlement requirement, but **not** location authorization. Supply `NSLocationWhenInUseUsageDescription` for a when-in-use request or `NSLocationAlwaysAndWhenInUseUsageDescription` for an always-authorization request; denial ends the session with an error. Check `supportsDLTDOAMeasurement` before configuring a session. Measurements from multiple deployed anchors are inputs for the app's location calculation, not an automatically available universal positioning service.

- **NIDLTDOAConfiguration** - A session configuration that enables UWB Down Link Time Difference of Arrival(DL-TDoA) ranging with nearby anchors
- **NIDLTDOAMeasurement** - Information from an anchor used to derive a range estimate.
- **NIDLTDOACoordinatesType** - The coordinate types of DL-TDOA measurement updates that Nearby Interaction supports
- **NIDLTDOAMeasurementType** - The possible phases of downlink positioning signals.
---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/NearbyInteraction)*
