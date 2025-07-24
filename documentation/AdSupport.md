# AdSupport

Provide apps with access to an advertising identifier.

**Platforms:** iOS 6.0+ | iPadOS 6.0+ | Mac Catalyst 13.0+ | macOS 10.14+ | tvOS 9.0+

## Overview

Use the AdSupport framework to obtain an advertising identifier. The advertisingIdentifier is an alphanumeric string that's unique to each device, and which you only use for advertising. On devices running iOS 14.5 and later and iPadOS 14.5 and later, your app must support App Tracking Transparency and define the purpose string NSUserTrackingUsageDescription before it can get the advertisingIdentifier property.

### Get an Advertising Identifier

Before requesting the advertising identifier for the first time, your app must make a one-time call to requestTrackingAuthorization(completionHandler:). That method presents the app-tracking authorization request to the user. The user chooses whether to allow tracking, but can change your app's authorization at any time in Settings > Privacy > Tracking. You can determine the user's intent by checking your app's authorization status with trackingAuthorizationStatus.

To get the advertising identifier, follow these steps:

1. Use the AdSupport framework to call the shared() class method to retrieve an instance of ASIdentifierManager.

2. Use the advertisingIdentifier property to obtain the UUID.

The code below shows how to retrieve the advertising identifier.

```swift
import AdSupport

let sharedASIdentifierManager = ASIdentifierManager.shared()
var adID = sharedASIdentifierManager.advertisingIdentifier
```

The advertising identifier returns either a unique UUID, or all zeros. For more information on the returned value, see advertisingIdentifier.

For more information about asking users for permission to track, see User Privacy and Data Use.

## Topics

### Essentials
- **ASIdentifierManager** - The object that contains the advertising identifier.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AdSupport)*