# Exposure Notification

Implement a COVID-19 exposure notification system that protects user privacy.

**Platforms:** iOS 13.5+ | iPadOS 13.5+ | Mac Catalyst 13.5+

## Overview

Use the Exposure Notification framework to inform people of potential exposure to COVID-19, the disease caused by the SARS-CoV-2 virus. You can build a notification system that employs random, rotating keys and identifiers to convey positive diagnoses in addition to data such as associated symptoms, proximity, and duration.

### Establish User Roles

The ExposureNotification framework defines two user roles:

**Affected user**  
When a user has a confirmed or probable diagnosis of COVID-19 (as defined by the Health Authority), the framework identifies them as affected and shares their diagnosis keys to alert other users to potential exposure.

**Potentially exposed user**  
To assign a user the potentially exposed role, use the framework to determine whether a set of temporary exposure keys indicate proximity to an affected user. If so, the app can retrieve additional information such as date and duration from the framework.

> **Important:** Before you can develop an app that uses ExposureNotification, you need the com.apple.developer.exposure-notification entitlement. For more information on this entitlement, see Exposure Notification APIs Addendum. To get permission to use this entitlement, see Exposure Notification Entitlement Request.

### Identify Your App's Region

All EN apps must specify the region for which they work by adding a key called ENDeveloperRegion to the app's Info.plist file. The value for ENDeveloperRegion is set to a string that represents the app's region. This value can be an ISO 3166-1 country code (for example, "CA" for Canada), or the ISO 3166-1/3166-2 country code plus subdivision code ("US-CA" for California).

Explicitly set the associated domain link to your region code. Avoid using wildcards because they can impact system operations. See Associated Domains Entitlement for more information.

### Specify Exposure Notification API Version

iOS 13.7 introduces a new method of calculating the user's Exposure Risk Value, described in ENExposureConfiguration. Apps can implement this new method, or continue to use the calculation method introduced in earlier versions of iOS. To choose your app's approach, add an entry to your app's Info.plist file with a key of ENAPIVersion. To use the new approach, specify a value of 2. To use the original approach, specify a value of 1.

### Support Exposure Notification Express

Starting with iOS 13.7, Health Authorities can inform users of potential exposure to COVID-19 without a dedicated Exposure Notification app. This feature is called Exposure Notification Express and must be enabled by a Health Authority. For more information, see Supporting Exposure Notifications Express.

## Topics

### Essentials
- [Supporting Exposure Notifications Express](https://developer.apple.com/documentation/exposurenotification/supporting_exposure_notifications_express) - Configure servers to notify users of potential exposures to COVID-19 without an app.
- [Building an App to Notify Users of COVID-19 Exposure](https://developer.apple.com/documentation/exposurenotification/building_an_app_to_notify_users_of_covid-19_exposure) - Inform people when they may have been exposed to COVID-19.
- [Setting Up a Key Server](https://developer.apple.com/documentation/exposurenotification/setting_up_a_key_server) - Ensure that your server meets the requirements for supporting Exposure Notifications.
- **ENManager** - A class that manages exposure notifications.
- **ENDeveloperRegion** - A string that specifies the region that the app supports.
- **ENAPIVersion** - A number that specifies the version of the API to use.
- [Changing Configuration Values Using the Server‑to‑Server API](https://developer.apple.com/documentation/exposurenotification/changing_configuration_values_using_the_server-to-server_api) - Update Exposure Notifications configuration values from a Public Health Authority's server.
- [Testing Exposure Notifications Apps in iOS 13.7 and Later](https://developer.apple.com/documentation/exposurenotification/testing_exposure_notifications_apps_in_ios_13_7_and_later) - Perform end-to-end validation of Exposure Notifications apps on a device by manually loading configuration files.
- [Supporting Exposure Notifications in iOS 12.5](https://developer.apple.com/documentation/exposurenotification/supporting_exposure_notifications_in_ios_12_5) - Prepare your Exposure Notifications app to run on a previous version of iOS.

### Exposures
- [Configuring Exposure Notifications](https://developer.apple.com/documentation/exposurenotification/configuring_exposure_notifications) - Define how Exposure Notifications work for a region by assigning server-based key-value pairs.
- **ENExposureConfiguration** - The object that contains parameters for configuring exposure notification risk scoring behavior.
- **ENExposureWindow** - A set of scan events from observed beacons within a time span.
- **ENScanInstance** - The aggregation of attenuations of beacons received during a scan.
- [Exposure Parameter Limits](https://developer.apple.com/documentation/exposurenotification/exposure_parameter_limits) - The limits for the parameters you use in exposure risk calculations.

### Summaries
- **ENExposureDetectionSummary** - A summary of exposures.
- **ENExposureDaySummary** - The summary of exposure information for a single day.
- **ENExposureSummaryItem** - The summary of exposures for a specific time period or report type.

### Status
- **ENAuthorizationStatus** - A set of cases that indicates the authorization status for the app.
- **ENStatus** - A set of cases that represents the overall status of exposure notification on the system.

### Errors
- **ENError** - Errors that the exposure notification framework issues.
- **Code** - Error codes that the exposure notification framework issues.
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