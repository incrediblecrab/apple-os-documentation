# AdSupport

Provide apps with access to an advertising identifier.

**Platforms:** iOS 6.0+ | iPadOS 6.0+ | Mac Catalyst 13.0+ | macOS 10.14+ | tvOS 9.0+

## Overview

Use AdSupport to obtain an advertising UUID, subject to system settings and authorization. On iOS/iPadOS 14.5 and later, request App Tracking Transparency authorization and provide `NSUserTrackingUsageDescription` before accessing a nonzero identifier.

### Get an Advertising Identifier

Use [`requestTrackingAuthorization(completionHandler:)`](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/requesttrackingauthorization(completionhandler:)) when authorization is not determined. The system skips the prompt and calls the completion handler immediately when tracking is restricted on the device, when the person has turned off Allow Apps to Request to Track in Settings (named Allow Apps to Request to Link Your Activity Across Companies in the European Union), while another permission request is pending, when the call comes from an app extension, or when the app isn't active. A call therefore does not guarantee that a prompt appeared. In France, Germany, Italy, Poland, and Romania the request appears as a full-page sheet instead of an alert. If the system dismisses the prompt without an answer, the status stays `notDetermined` and the app needs to ask again.

The person can change their decision in Settings at any time. Check `trackingAuthorizationStatus` before asking; its reference directs apps to request authorization when the status is `notDetermined`. In the European Union, the system doesn't show the prompt again for a year after the person answers; after that year the app can make another request, whichever way the person answered, unless they have turned off tracking requests in Settings.

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
