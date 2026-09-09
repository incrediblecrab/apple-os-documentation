# FamilyControls

Authorize your app to provide parental controls on a device.

**Platforms:** iOS 15.0+ | iPadOS 15.0+. The framework catalog also lists Mac Catalyst 15.0, but `AuthorizationCenter` is not documented for that target and the public 26.5 SDK explicitly marks it unavailable there.

## Overview

To authorize your parental controls app, use a shared `AuthorizationCenter` on a supported device and account configuration. Importing the framework is not proof that authorization is available on every device.

**Important**

You must add the Family Controls capability to your app before you call the requestAuthorization(for:) or revokeAuthorization(completionHandler:) methods. This capability adds the Family Controls entitlement to your app. Before submitting your app to the App Store, you must request permission to use the entitlement. For more information, see Adding capabilities to your app.

Authorizing parental controls for a child requires approval from a parent or guardian in the same Family Sharing group. The system displays an authentication sheet on the child's device, and the parent or guardian approves or denies the authorization request. The system sends the result to your app's AuthorizationCenter.

Authorizing controls for an individual requires the device owner's approval. When a person who has not previously authorized the app chooses to continue, the device requests Face ID or Touch ID authentication. Cancellation or failure does not authorize the app. Subsequent requests after approval do not repeat biometric authentication.

The asynchronous `requestAuthorization(for:)` method and `FamilyControlsMember` start at iOS/iPadOS 16. The original 15.0 completion-handler request is deprecated from 16 in favor of that method. Individual authorization does not impose the child-account restrictions on deleting the app or signing out of iCloud.

The Family Controls framework prevents child users, authorized by a parent or guardian, from performing actions that might circumvent the parental controls settings. For example, authorizing an app prevents the child user from deleting the app that provides parental controls. In addition, while a device has at least one app authorized for parental controls by a parent or guardian, the user can't sign out of iCloud.

In a compatible iPad or iPhone app running in visionOS, authorization attempts always fail.

### Denial and revocation

Observe [`authorizationStatus`](https://developer.apple.com/documentation/familycontrols/authorizationcenter/authorizationstatus), including changes made outside the app. A parent or guardian can change authorization in Settings, and account transitions can also change it. Do not continue claiming controls are active after approval ends.

Use [`revokeAuthorization(completionHandler:)`](https://developer.apple.com/documentation/familycontrols/authorizationcenter/revokeAuthorization(completionHandler:)) to give up authorization. Its completion result describes whether the request completed, **not** the resulting authorization state. After revocation, the app no longer provides parental controls and the system no longer enforces the associated anti-circumvention restrictions.

Configure the exact `com.apple.developer.family-controls` entitlement through the Family Controls capability. Handle refusal and authorization errors before applying [ManagedSettings](ManagedSettings.md) or starting [DeviceActivity](DeviceActivity.md) monitoring.

## Topics

### Authorizations
- **class AuthorizationCenter** - The center for requesting authorization to provide parental controls.
- **enum AuthorizationStatus** - The status of your app's authorization to provide parental controls.
- **Family Controls** - A Boolean value that indicates whether the app can request or revoke authorization to provide parental controls.

### Account Types
- **enum FamilyControlsMember** - The type of account that Family Controls is currently managing.

### User-Selected Apps and Web Domains
- **struct FamilyActivityPicker** - A view in which users specify applications, web domains, and categories without revealing their choices to the app.
- **struct FamilyActivitySelection** - A collection of applications, categories, and web domains selected by the user.

### Activity Labels
- [Displaying Activity Labels](https://developer.apple.com/documentation/familycontrols/displayingactivitylabels) - Provide users with a read-only, visual representation of an application, category, or web domain.

### Errors
- **enum FamilyControlsError** - Errors the Family Controls framework reports.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/FamilyControls)*

*Authorization lifecycle reviewed September 8, 2026: [AuthorizationCenter](https://developer.apple.com/documentation/familycontrols/authorizationcenter.md) and [revocation semantics](https://developer.apple.com/documentation/familycontrols/authorizationcenter/revokeAuthorization(completionHandler:).md).*
