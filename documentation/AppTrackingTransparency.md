# App Tracking Transparency

Request user authorization to access app-related data for tracking the user or the device.

**Platforms:** iOS 14.0+ | iPadOS 14.0+ | Mac Catalyst 14.0+ | macOS 11.0+ | tvOS 14.0+ | visionOS 1.0+

## Overview

You must use the AppTrackingTransparency framework if your app collects data about end users and shares it with other companies for purposes of tracking across apps and web sites. The AppTrackingTransparency framework presents an app-tracking authorization request to the user and provides the tracking authorization status.

To use the AppTrackingTransparency framework:

- Set up a NSUserTrackingUsageDescription to display a system-permission alert request for your app installed on end-user devices.
- Call requestTrackingAuthorization(completionHandler:) to present the app-tracking authorization request to the end user.
- Use trackingAuthorizationStatus to determine the app-tracking permission status. See ATTrackingManager.AuthorizationStatus for status enums.

For more information about app tracking and privacy, see User Privacy and Data Use and App Privacy Details.

### Authorization lifecycle

`NSUserTrackingUsageDescription` is the Info.plist purpose string required for the request; it does not itself grant tracking permission. Check `ATTrackingManager.trackingAuthorizationStatus` and distinguish `.authorized` from `.denied`, `.restricted`, and `.notDetermined`.

Request authorization while the app is active and no other permission prompt is awaiting a response. Requests from an app extension do not present the prompt, and concurrent prompt requests are not queued for later presentation.

The system remembers the person's decision. Recheck status before enabling tracking-dependent behavior and respect later changes; do not repeatedly prompt after denial or treat a restricted/undetermined result as consent. Cancellation or failure to present a prompt must leave tracking disabled.

## Topics

### Essentials
- **NSUserTrackingUsageDescription** - A message that informs the user why an app is requesting permission to use data for tracking the user or the device.

### Class and Components
- **ATTrackingManager** - A class that provides a tracking authorization request and the tracking authorization status of the app.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AppTrackingTransparency)*

*Authorization behavior reviewed September 8, 2026: [requestTrackingAuthorization(completionHandler:)](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/requestTrackingAuthorization(completionHandler:).md).*
