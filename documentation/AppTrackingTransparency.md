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

Request authorization while the app is active. The system skips the prompt and calls the completion handler immediately when tracking is restricted for the device, when the person has turned off "Allow Apps to Request to Track" ("Allow Apps to Request to Link Your Activity Across Companies" in the EU) in Settings > Privacy & Security > Tracking, when another permission request is pending, when the call comes from an app extension, or when the app is not in the active state.

A status of `.notDetermined` after a request means the system dismissed the prompt without a decision; request again later to get an answer. The system remembers the person's decision. In the European Union, it records the date of an answer and does not show the prompt again for a year; after that, the app can ask again whether the earlier answer was approval or denial, unless the person has turned off tracking requests in Settings. Recheck status before enabling tracking-dependent behavior and respect later changes; do not prompt again outside those rules or treat a restricted or undetermined result as consent. Cancellation or failure to present a prompt must leave tracking disabled.

### European Union prompt (iOS 27.2 SDK)

In France, Germany, Italy, Poland, and Romania, the system presents the request as a full-page sheet instead of an alert, including for `requestTrackingAuthorization(completionHandler:)`.

`requestTrackingAuthorization(preferExpandedInterface:additionalInformationAction:completionHandler:)` (iOS 27.2+, iPadOS 27.2+, Mac Catalyst 27.2+) adds two options. In those five countries the sheet appears regardless of `preferExpandedInterface`; elsewhere in the EU it appears only when `preferExpandedInterface` is `true`. A non-nil `additionalInformationAction` adds an Additional Information button. Tapping it dismisses the sheet without recording an answer, runs your closure so you can show your own explanation, and still calls the completion handler with `.notDetermined`; call the method again afterward. Outside the EU the system ignores both parameters and shows the standard alert.

The optional `NSUserTrackingMarkdownUsageDescription` key (iOS 27.2+, iPadOS 27.2+) supplies Markdown text for the sheet: bold, italic, bullet lists, and paragraph breaks, but not underline. Without it, the sheet uses `NSUserTrackingUsageDescription`, which remains required. These regional rules depend on the device being in the qualifying country and on the Apple Account's country or region.

## Topics

### Essentials
- **ATTrackingManager** - A class that requests tracking authorization and provides the current authorization status.
- **NSUserTrackingUsageDescription** - A message that informs the user why an app is requesting permission to use data for tracking the user or the device.

### Authorization requests
- **requestTrackingAuthorization(completionHandler:)** - Presents the tracking-authorization request.
- **requestTrackingAuthorization(preferExpandedInterface:additionalInformationAction:completionHandler:)** - Presents the request with the EU full-page sheet and Additional Information options (iOS 27.2+, iPadOS 27.2+, Mac Catalyst 27.2+).
- **NSUserTrackingMarkdownUsageDescription** - An optional Markdown purpose string for the EU full-page sheet (iOS 27.2+, iPadOS 27.2+).

### Authorization status and results
- **trackingAuthorizationStatus** - The app's current tracking-authorization status.
- **ATTrackingManager.AuthorizationStatus** - The status values: `authorized`, `denied`, `notDetermined`, and `restricted`.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AppTrackingTransparency)*

*Authorization behavior reviewed September 8, 2026: [requestTrackingAuthorization(completionHandler:)](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/requestTrackingAuthorization(completionHandler:).md).*

*EU prompt and yearly re-request reviewed November 1, 2026: [requestTrackingAuthorization(preferExpandedInterface:additionalInformationAction:completionHandler:)](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/requesttrackingauthorization(preferexpandedinterface:additionalinformationaction:completionhandler:)) and [NSUserTrackingMarkdownUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsusertrackingmarkdownusagedescription).*
