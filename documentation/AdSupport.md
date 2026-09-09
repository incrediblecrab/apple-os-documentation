# AdSupport

Provide apps with access to an advertising identifier.

**Platforms:** iOS 6.0+ | iPadOS 6.0+ | Mac Catalyst 13.0+ | macOS 10.14+ | tvOS 9.0+

## Overview

Use AdSupport to obtain an advertising UUID, subject to system settings and authorization. On iOS/iPadOS 14.5 and later, request App Tracking Transparency authorization and provide `NSUserTrackingUsageDescription` before accessing a nonzero identifier.

### Get an Advertising Identifier

Use [`requestTrackingAuthorization(completionHandler:)`](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/requesttrackingauthorization(completionhandler:)) when authorization is not determined. iOS prompts only while the app is active, with no other permission prompt pending; extension calls do not prompt. A call therefore does not guarantee that an alert appeared. The system remembers the person's decision, and they can change it in Settings. Inspect `trackingAuthorizationStatus` rather than repeatedly requesting a decided permission.

To get the advertising identifier, follow these steps:

1. Use the AdSupport framework to call the shared() class method to retrieve an instance of ASIdentifierManager.

2. Use the advertisingIdentifier property to obtain the UUID.

The code below reads the current identifier only; it does not request permission.

```swift
import AdSupport

let sharedASIdentifierManager = ASIdentifierManager.shared()
var adID = sharedASIdentifierManager.advertisingIdentifier
```

The [`advertisingIdentifier`](https://developer.apple.com/documentation/adsupport/asidentifiermanager/advertisingidentifier) reference specifies **all zeros on macOS and in Simulator**, and for compatible iPhone/iPad apps running in visionOS. It also returns zeros when the required tracking authorization is absent, denied, or restricted. Framework availability is not a promise of a usable advertising identifier. The property itself is available from Mac Catalyst 13.1.

Do not store the identifier as a permanent identity: obtain the current value and authorization status when needed. See [User Privacy and Data Use](https://developer.apple.com/app-store/user-privacy-and-data-use/).

## Topics

### Essentials
- [`ASIdentifierManager`](https://developer.apple.com/documentation/adsupport/asidentifiermanager) - The object that provides the advertising identifier.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AdSupport)*
