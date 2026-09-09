# Exposure Notification

Reference for the legacy COVID-19 exposure notification APIs.

**Historical SDK catalog:** iOS 13.5+ | iPadOS 13.5+ | Mac Catalyst 13.5+. Selected APIs were also backported to iOS 12.5; this does not imply support on iOS 13.0–13.4.

**Status, reviewed September 8, 2026:** [`ENManager`](https://developer.apple.com/documentation/exposurenotification/enmanager) and the core authorization/status APIs are deprecated in 27.0 with the message “No longer supported.” The material below describes the historical API and configuration model, not a supported new 27-generation deployment.

## Overview

The Exposure Notification framework supported notifications of potential exposure to COVID-19, the disease caused by the SARS-CoV-2 virus. Its model uses random, rotating keys and identifiers, with risk evaluation based on information such as proximity and duration.

### Establish User Roles

The ExposureNotification framework defines two user roles:

**Affected user**  
An affected user has a confirmed or probable diagnosis under the Health Authority's definition. Releasing diagnosis keys for server sharing requires the person's authorization; the role itself does not automatically publish their keys.

**Potentially exposed user**  
To assign a user the potentially exposed role, use the framework to determine whether a set of temporary exposure keys indicate proximity to an affected user. If so, the app can retrieve additional information such as date and duration from the framework.

> **Historical prerequisite:** The Boolean `com.apple.developer.exposure-notification` entitlement requires Apple's permission. An entitlement is separate from the person's consent and does not restore support for the deprecated service.

### Consent and lifecycle

In the legacy flow, activating `ENManager` only prepares the object; it does not enable exposure notification. Enabling can present a consent dialog. Check authorization and service status, including denial, restrictions, pause, and Bluetooth being off.

`getDiagnosisKeys(completionHandler:)` requires the foreground app and requests authorization each time it is called. Disabling exposure notification stops scanning and advertising but does not delete existing diagnosis keys and data. Invalidating the manager is asynchronous, and the instance cannot be reused afterward.

### Identify Your App's Region

All EN apps must specify the region for which they work by adding a key called ENDeveloperRegion to the app's Info.plist file. The value for ENDeveloperRegion is set to a string that represents the app's region. This value can be an ISO 3166-1 country code (for example, "CA" for Canada), or the ISO 3166-1/3166-2 country code plus subdivision code ("US-CA" for California).

Explicitly set the associated domain link to your region code. Avoid using wildcards because they can impact system operations. See Associated Domains Entitlement for more information.

### Specify Exposure Notification API Version

iOS 13.7 introduces a new method of calculating the user's Exposure Risk Value, described in ENExposureConfiguration. Apps can implement this new method, or continue to use the calculation method introduced in earlier versions of iOS. To choose your app's approach, add an entry to your app's Info.plist file with a key of ENAPIVersion. To use the new approach, specify a value of 2. To use the original approach, specify a value of 1.

### Support Exposure Notification Express

Starting with iOS 13.7, Health Authorities can inform users of potential exposure to COVID-19 without a dedicated Exposure Notification app. This feature is called Exposure Notification Express and must be enabled by a Health Authority. For more information, see Supporting Exposure Notifications Express.

## Topics

### Essentials
- [Supporting Exposure Notifications Express](https://developer.apple.com/documentation/exposurenotification/supporting-exposure-notifications-express) - Historical server configuration for the app-less workflow.
- [Building an App to Notify Users of COVID-19 Exposure](https://developer.apple.com/documentation/exposurenotification/building-an-app-to-notify-users-of-covid-19-exposure) - The legacy exposure-notification sample.
- [Setting Up a Key Server](https://developer.apple.com/documentation/exposurenotification/setting-up-a-key-server) - The documented legacy key-server requirements.
- **ENManager** - A class that manages exposure notifications.
- **ENDeveloperRegion** - A string that specifies the region that the app supports.
- **ENAPIVersion** - A number that specifies the version of the API to use.
- [Changing Configuration Values Using the Server‑to‑Server API](https://developer.apple.com/documentation/exposurenotification/changing-configuration-values-using-the-server-to-server-api) - Historical Public Health Authority configuration updates.
- [Testing Exposure Notifications Apps in iOS 13.7 and Later](https://developer.apple.com/documentation/exposurenotification/testing-exposure-notifications-apps-in-ios-13-7-and-later) - The legacy device-testing workflow with manually loaded configuration.
- [Supporting Exposure Notifications in iOS 12.5](https://developer.apple.com/documentation/exposurenotification/supporting-exposure-notifications-in-ios-12-5) - The separately backported iPhone implementation and its version checks.

### Exposures
- [Configuring Exposure Notifications](https://developer.apple.com/documentation/exposurenotification/configuring-exposure-notifications) - Historical regional server-based configuration.
- **ENExposureConfiguration** - The object that contains parameters for configuring exposure notification risk scoring behavior.
- **ENExposureWindow** - A set of scan events from observed beacons within a time span.
- **ENScanInstance** - The aggregation of attenuations of beacons received during a scan.
- [Exposure Parameter Limits](https://developer.apple.com/documentation/exposurenotification/exposure-parameter-limits) - The documented limits for legacy exposure-risk calculations.

### Summaries
- **ENExposureDetectionSummary** - A summary of exposures.
- **ENExposureDaySummary** - The summary of exposure information for a single day.
- **ENExposureSummaryItem** - The summary of exposures for a specific time period or report type.

### Status
- **ENAuthorizationStatus** - A set of cases that indicates the authorization status for the app.
- **ENStatus** - A set of cases that represents the overall status of exposure notification on the system.

### Errors
- **ENError** - Errors that the exposure notification framework issues.
- **ENError.Code** - Error codes that the exposure notification framework issues.
- **ENErrorDomain** - The domain for an error.
- **ENErrorHandler** - The handler for error conditions.

### Variables
- **ENRiskWeightDefaultV2** - This weight is not used.
- **ENRiskWeightMaxV2** - This weight is not used.
- **EN_FEATURE_GENERAL**

### Type Aliases
- **ENDetectExposuresHandler** - The definition of a handler that returns exposure summaries.
- **ENErrorOutType** - Type for returning NSError's from functions. Avoids long and repetitious method signatures.
- **ENGetDiagnosisKeysHandler** - The definition of a handler that returns diagnosis keys.
- **ENGetExposureInfoHandler** - The definition of a handler that receives exposure info.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ExposureNotification)*
