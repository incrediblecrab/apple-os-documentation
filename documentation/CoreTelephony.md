# Core Telephony

Inspect supported cellular-service, subscriber, and provisioning information.

**Framework catalog:** iOS 4.0+ | iPadOS 4.0+ | Mac Catalyst 14.0+ | macOS 10.10+. Individual APIs have different declarations and hardware restrictions; this list does not give a Mac cellular-account or eSIM capability.

## Overview

Core Telephony provides cellular-service information and specialized provisioning interfaces, including eSIM workflows for authorized carrier apps on supported devices. Check each API's availability and access requirements rather than treating the framework as unrestricted access to cellular-account data.

`CTCarrier`, `CTCall`, and `CTCallCenter` are retained below as deprecated references. `CTCarrier` is deprecated from iOS/iPadOS 16; `CTCall` and `CTCallCenter` from 10. Current call-information retrieval through these Core Telephony interfaces is no longer supported; Apple's reference directs call integration to CallKit. Do not use legacy carrier or call objects as a reliable identity, permission, or location signal.

**Note:** VoIP and cellular services through Core Telephony are unavailable for compatible iPad and iPhone apps running in visionOS. You can still use the APIs of this framework, but services don't return carrier information.

## Topics

### Service Information
- **CTTelephonyNetworkInfo** - An object that provides notifications of changes to the user's cellular service provider.

### eSIM
Carrier apps use the classes in this group to provision cellular plan eSIMs on supported devices.

`CTCellularPlanProvisioning` starts at iOS/iPadOS 12 and requires a carrier app with `com.apple.CommCenter.fine-grained`, whose array includes `public-cellular-plan`. Merely linking Core Telephony does not grant this carrier privilege.

- **CTCellularPlanProvisioning** - An object you use to download and install a carrier eSIM.
- **CTCellularPlanProvisioningRequest** - A request specifying an eSIM to download and install.
- **CTCellularPlanProperties** - An object you use for an eSIM.
- **CTCellularPlanCapability** - The type of cellular plan available for an eSIM.

### SIM
`CTCellularPlanStatus` starts at 26 and supports UPI token validation. UPI device validation requires the Boolean [`com.apple.developer.upi-device-validation`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.upi-device-validation) entitlement; that entitlement predates this class.

The 27 additions provide a separate, user-authorized cellular-plan continuity check for a phone number. Call `requestAuthorization(forPhoneNumber:completion:)` and proceed only with `.authorized`, not `.notAuthorized` or `.restricted`. `getAuthorizationStatus(forPhoneNumber:completion:)` rechecks the current status without UI. `getHintForPhoneNumber(_:completion:)` returns an availability assessment **and confidence**, not proof of a person's identity. Handle errors and changed authorization.

- [CTCellularPlanStatus](https://developer.apple.com/documentation/coretelephony/ctcellularplanstatus) - UPI token validation and, with the newer APIs, authorized cellular-plan continuity checks.

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
