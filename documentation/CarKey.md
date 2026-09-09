# CarKey

Access the remote keyless features of configured vehicles in the Wallet app.

**Session API availability:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 16.0+ | macOS 13.3+ | watchOS 9.0+

The framework catalog lists the first three platforms; the [`CarKeyRemoteControl`](https://developer.apple.com/documentation/carkey/carkeyremotecontrol) and [`CarKeyRemoteControlSession`](https://developer.apple.com/documentation/carkey/carkeyremotecontrolsession) declarations also list macOS and watchOS. These annotations do not provision a vehicle key or grant the automaker entitlement.

## Overview

The CarKey framework offers a way to communicate with vehicles already provisioned to someone's Apple Wallet. Car manufacturers adopt this framework in the apps they use to support and control their vehicles. For example, your app might use it to lock or unlock the vehicle, or open a power sunroof. To control a vehicle remotely, you need the following information for that vehicle:

- The function identifiers for each of your vehicle's features.
- The action identifiers for each action you can perform on a feature.
- The execution status the vehicle can return in response to an action.

The Wallet app maintains a list of vehicles that match your company's make, and that the user previously configured for remote access. Create a session object to get information about those vehicles and to establish a connection to ones that are in range. Use the session to retrieve the list of commands available to the current person, and to initiate actions from your app.

> **Note**
> 
> Your app must have the com.apple.developer.carkey.session entitlement to use this framework. To request the entitlement, you must be an automaker enrolled in the MFi Program. For details, see https://developer.apple.com/mfi/.

## Topics

### Setup
- **CarKeyRemoteControl** - The object you use to start a new vehicle-related session.
- **CarKeyRemoteControlSession** - The object that manages communication with the vehicles you manufacture.
- **CarKeyRemoteControlSessionDelegate** - An interface you use to receive session- and vehicle-related information from the system.
- **VehicleReport** - A type that contains information about a vehicle configured for remote keyless entry in the user's Apple Wallet.

### Vehicle Actions
- **RemoteKeylessEntryAction** - An automatically ending action that you want to perform on a vehicle.
- **RemoteKeylessEntryEnduringAction** - An action with an optional stopping point that you want to perform on a vehicle.

- [`FunctionIdentifier`](https://developer.apple.com/documentation/carkey/functionidentifier) - A vehicle-specific feature code.
- [`ActionIdentifier`](https://developer.apple.com/documentation/carkey/actionidentifier) - A code for an action supported by that feature.

These identifier types are not marked deprecated in their current declarations.

### Error Codes
- **CarKeyErrorCode** - The errors that can occur when you perform remote-keyless entry operations on a vehicle.

### Structures
- [`ExecutionStatus`](https://developer.apple.com/documentation/carkey/executionstatus) - A status code returned by the vehicle, including supported custom codes.
- [`RemoteKeylessEntryConfigurableEnduringAction`](https://developer.apple.com/documentation/carkey/remotekeylessentryconfigurableenduringaction) - An action that can be stopped or run to completion; its iOS/iPadOS/Mac Catalyst availability starts at 18.0, not the framework's 16.0 baseline.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CarKey)*
