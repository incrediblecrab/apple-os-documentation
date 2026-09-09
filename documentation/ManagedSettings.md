# ManagedSettings

Access and change settings with your app while maintaining user privacy and control.

**Platforms:** iOS 15.0+ | iPadOS 15.0+ | Mac Catalyst 15.0+

## Overview

Managed Settings provides a privacy-preserving way for users to restrict access to certain settings and features on their devices. With the user's permission, your app can limit media showings, restrict app purchases, lock passcode settings, and configure other device behavior.

Managed Settings works together with ManagedSettingsUI, DeviceActivity, and FamilyControls to allow your app to restrict, authorize, and monitor device usage. To learn more about authorizing Managed Settings on your app, see FamilyControls. For more information about monitoring and scheduling device usage with your app, see DeviceActivity.

### Authorization and effective settings

For parental-control configuration, use [FamilyControls](FamilyControls.md) authorization and observe denial or revocation. Do not treat possession of an activity token or a previously created settings store as continuing permission.

[`ManagedSettingsStore`](https://developer.apple.com/documentation/managedsettings/managedsettingsstore) records **your app's** settings. The system combines applicable settings to determine effective behavior, so a value written by the app is not a guarantee of the device's final state.

Setting a value to `nil` removes that store's configuration for the setting; it does not remove another store's, another app's, or the system's restrictions. Use documented effective-rating properties when deciding which media to display. Setting-specific and platform availability can differ from the framework header.

Read-only effective TV/movie-rating access does not require FamilyControls authorization or DeviceActivity monitoring. Apple's effective-rating guide separately calls for the Family Controls entitlement when subscribing to rating changes. Do not confuse reading effective restrictions with permission to configure parental controls.

## Topics

### Essentials
- [Manage Settings on Devices in a Family Sharing Group](https://developer.apple.com/documentation/managedsettings/connectionwithframeworks) - Configure settings in the parent/guardian-authorized Family Sharing workflow.
- [Confirming the Effective TV and Movie Ratings](https://developer.apple.com/documentation/managedsettings/readingmedia) - Read effective media restrictions and observe changes.

### Settings
- **ManagedSettingsStore** - A data store that applies settings to the current user or device.

### Shield Actions
- **ShieldActionDelegate** - A class for an extension that handles shield actions.

### Family Privacy
- **Token** - A representation of an activity, such as an app or website, that doesn't reveal its identity.

### Apps
- **Application** - A representation of an application on the user's device.
- **ApplicationToken** - A representation of an application.

### Categories
- **ActivityCategory** - An activity's category, such as Entertainment or Social.
- **ActivityCategoryToken** - A token that represents a category of app or website activity.

### Websites
- **WebDomain** - An object that represents a website.
- **WebDomainToken** - A representation of a web domain that preserves the user's privacy.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ManagedSettings)*

*Changed-content source, reviewed September 8, 2026: [ManagedSettingsStore](https://developer.apple.com/documentation/managedsettings/managedsettingsstore.md).*
