# FamilyControls

Authorize your app to provide parental controls on a device.

**Platforms:** iOS 15.0+ | iPadOS 15.0+ | Mac Catalyst 15.0+

## Overview

To authorize your parental controls app, use a shared AuthorizationCenter instance. You can authorize parental controls on any device.

**Important**

You must add the Family Controls capability to your app before you call the requestAuthorization(for:) or revokeAuthorization(completionHandler:) methods. This capability adds the Family Controls entitlement to your app. Before submitting your app to the App Store, you must request permission to use the entitlement. For more information, see Adding capabilities to your app.

Authorizing parental controls for a child requires approval from a parent or guardian in the same Family Sharing group. The system displays an authentication sheet on the child's device, and the parent or guardian approves or denies the authorization request. The system sends the result to your app's AuthorizationCenter.

Authorizing parental controls for an individual requires approval from the owner of the device. The system displays a biometric authentication alert on the individual's device after the individual approves or denies the authorization request. The system sends the result to your app's AuthorizationCenter.

The Family Controls framework prevents child users, authorized by a parent or guardian, from performing actions that might circumvent the parental controls settings. For example, authorizing an app prevents the child user from deleting the app that provides parental controls. In addition, while a device has at least one app authorized for parental controls by a parent or guardian, the user can't sign out of iCloud.

In a compatible iPad or iPhone app running in visionOS, authorization attempts always fail.

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
- [Displaying Activity Labels](https://developer.apple.com/documentation/familycontrols/displaying_activity_labels) - Provide users with a read-only, visual representation of an application, category, or web domain.

### Errors
- **enum FamilyControlsError** - Errors the Family Controls framework reports.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/FamilyControls)*