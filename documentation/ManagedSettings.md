# ManagedSettings

Access and change settings with your app while maintaining user privacy and control.

**Platforms:** iOS 15.0+ | iPadOS 15.0+ | Mac Catalyst 15.0+

## Overview

Managed Settings provides a privacy-preserving way for users to restrict access to certain settings and features on their devices. With the user's permission, your app can limit media showings, restrict app purchases, lock passcode settings, and configure other device behavior.

Managed Settings works together with ManagedSettingsUI, DeviceActivity, and FamilyControls to allow your app to restrict, authorize, and monitor device usage. To learn more about authorizing Managed Settings on your app, see FamilyControls. For more information about monitoring and scheduling device usage with your app, see DeviceActivity.

## Topics

### Essentials
- [Manage Settings on Devices in a Family Sharing Group](https://developer.apple.com/documentation/managedsettings/manage_settings_on_devices_in_a_family_sharing_group) - Empower parents and guardians to configure constraints on other devices while preserving the family's privacy.
- [Confirming the Effective TV and Movie Ratings](https://developer.apple.com/documentation/managedsettings/confirming_the_effective_tv_and_movie_ratings) - Read the media rating on a device and determine what media to display on your app.

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