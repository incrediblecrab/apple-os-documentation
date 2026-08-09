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

## Topics

### Essentials
- **NSUserTrackingUsageDescription** - A message that informs the user why an app is requesting permission to use data for tracking the user or the device.

### Class and Components
- **ATTrackingManager** - A class that provides a tracking authorization request and the tracking authorization status of the app.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AppTrackingTransparency)*