# Core Telephony

Access information about a user's cellular service provider, such as its unique identifier and whether the carrier allows VoIP.

**Platforms:** iOS 4.0+ | iPadOS 4.0+ | Mac Catalyst 14.0+ | macOS 10.10+

## Overview

Use the Core Telephony framework to obtain information about a user's home cellular service provider. Carriers can use this information to write apps that provide services only for their own subscribers. You can also use this framework to obtain information about current cellular calls.

A CTCarrier object gives you information about the user's cellular service provider, such as whether it allows use of VoIP (Voice over Internet Protocol) on its network. A CTCall object gives you information about a current call, including a unique identifier and state information such as dialing, incoming, connected, or disconnected.

**Note:** VoIP and cellular services through Core Telephony are unavailable for compatible iPad and iPhone apps running in visionOS. You can still use the APIs of this framework, but services don't return carrier information.

## Topics

### Service Information
- **CTTelephonyNetworkInfo** - An object that provides notifications of changes to the user's cellular service provider.

### eSIM
Carrier apps use the classes in this group to provision cellular plan eSIMs on supported devices.

- **CTCellularPlanProvisioning** - An object you use to download and install a carrier eSIM.
- **CTCellularPlanProvisioningRequest** - A request specifying an eSIM to download and install.
- **CTCellularPlanProperties** - An object you use for an eSIM. (Beta)
- **CTCellularPlanCapability** - The type of cellular plan available for an eSIM.

### SIM
Check the presence of a SIM based on authentication.

- **CTCellularPlanStatus** - An object used for retrieving and checking the validity of a token. (Beta)

### Subscriber Information
- **CTSubscriber** - A cellular network subscriber.
- **CTSubscriberDelegate** - A protocol to handle changes to subscriber information.
- **CTSubscriberInfo** - An object that provides an array of cellular network subscribers.

### Cellular Data Access
- **CTCellularData** - An object indicating whether the app can access cellular data.

### Errors
- **CTError** - A type representing a Core Telephony error.

### Deprecated
Getting call information in Core Telephony is no longer supported. Use CallKit instead.

- **CTCarrier** - Information about the user's cellular service provider, such as its unique identifier and whether it allows VoIP calls on its network. (Deprecated)
- **CTCall** - An object used to identify a cellular call and determine its state. (Deprecated)
- **CTCallCenter** - An object that provides a list of current cellular calls, and provides the ability to respond to state changes for calls. (Deprecated)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreTelephony)*