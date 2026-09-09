# HealthKit

Access and share health and fitness data while maintaining the user's privacy and control.

**Framework catalog annotations:** iOS 8.0+ | iPadOS 8.0+ | Mac Catalyst 17.0+ | macOS 14.0+ | visionOS 1.0+ | watchOS 2.0+. These are symbol-catalog labels, not a guarantee of a readable or writable health store.

## Overview

HealthKit provides a central repository for health and fitness data on iPhone and Apple Watch. With the user's permission, apps communicate with the HealthKit store to access and share this data.

Creating a complete, personalized health and fitness experience includes a variety of tasks:

- Collecting and storing health and fitness data
- Analyzing and visualizing the data
- Enabling social interactions

HealthKit apps take a collaborative approach to building this experience. Your app doesn't need to provide all of these features. Instead, you can focus just on the subset of tasks that most interests you.

For example, users can select their favorite weight-tracking, step-counting, and health challenge app, each calibrated to their personal needs. Because HealthKit apps freely exchange data (with user permission), the combined suite provides a more customized experience than any single app on its own. For example, when a group of friends joins a daily step-counting challenge, each person can use their preferred hardware device and app to track their steps, while everyone in the group uses the same social app for the challenge.

HealthKit is also designed to manage and merge data from multiple sources. For example, users can view and manage all of their data in the Health App, including adding data, deleting data, and changing an app's permissions. Therefore, your app needs to handle these changes, even when they occur outside your app.

**Note:** Because health data may contain sensitive, personal information, apps must receive permission from the user to read data from or write data to the HealthKit store. They must also take steps to protect that data at all times. For more information, see Protecting user privacy.

## OS 27 API changes reviewed September 8, 2026

### Heart-rate and cycling-power zones

HealthKit adds workout-zone configuration and time-in-zone data. Use [`HKWorkoutZoneGroup`](https://developer.apple.com/documentation/healthkit/hkworkoutzonegroup), [`HKWorkoutZoneConfiguration`](https://developer.apple.com/documentation/healthkit/hkworkoutzoneconfiguration), and [`HKWorkoutZoneDuration`](https://developer.apple.com/documentation/healthkit/hkworkoutzoneduration) for completed workouts and activities. Live workout integration uses [`HKLiveWorkoutZoneUpdate`](https://developer.apple.com/documentation/healthkit/hkliveworkoutzoneupdate) and the live workout builder delegate.

Retrieve a person's preferred settings with [`preferredWorkoutZoneConfiguration(for:)`](https://developer.apple.com/documentation/healthkit/hkhealthstore/preferredworkoutzoneconfiguration(for:)), rather than assuming fixed thresholds. Handle a `nil` configuration or a thrown retrieval error; settings can be manually chosen or system-generated. [Tracking heart rate zones for workouts](https://developer.apple.com/documentation/healthkit/tracking-heart-rate-zones-for-workouts) provides an iOS/watchOS 27 sample. The zone-group's DocC availability lists 27.0 on iOS, iPadOS, Mac Catalyst, macOS, visionOS, and watchOS; check related APIs individually.

### Limited-history authorization

The updated permission flow groups data-type choices into categories, then lets the person choose a recent history window or full history. **Time-bound authorization applies only to sample types.** After requesting authorization, call [`getEarliestAuthorizedSampleDate(for:completion:)`](https://developer.apple.com/documentation/healthkit/hkhealthstore/getearliestauthorizedsampledate(for:completion:)) to discover their limited-access boundaries. Calculate query ranges per type and treat inaccessible earlier data as **unknown**, not as zero activity or a missing medical history.

An absent dictionary entry does **not** establish full read access: full access, denied access, and limited access without an available boundary can all omit a type. HealthKit evaluates the boundary against a sample's end date, so a returned sample can begin before the boundary. Authorization completion is not a guarantee that every requested type was granted. `authorizationStatus(for:)` checks permission to save a type; it does not reveal whether the person granted read access.

### Menopause categories

- [`HKCategoryTypeIdentifier.menopausalState`](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/menopausalstate) uses [`HKCategoryValueMenopausalState`](https://developer.apple.com/documentation/healthkit/hkcategoryvaluemenopausalstate): `.menopause`, `.perimenopause`, or `.none`. These are point-in-time samples: **start and end dates must be equal**, or saving fails.
- [`HKCategoryTypeIdentifier.bleedingAfterMenopause`](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/bleedingaftermenopause) records an interval and uses [`HKCategoryValueVaginalBleeding`](https://developer.apple.com/documentation/healthkit/hkcategoryvaluevaginalbleeding) intensity values, not the menopausal-state enumeration.

Both category identifiers are read/write reproductive-health types, require standard per-type authorization, and have 27.0 availability on iOS, iPadOS, Mac Catalyst, macOS, visionOS, and watchOS. Missing or inaccessible samples do not establish `.none`, and these APIs do not themselves diagnose menopause.

### Availability, privacy, and failure handling

Framework symbol availability is not proof that a device exposes a usable health store. Call [`HKHealthStore.isHealthDataAvailable()`](https://developer.apple.com/documentation/healthkit/hkhealthstore/ishealthdataavailable()) first. Its documentation explicitly excludes reading or writing health data on macOS and on iPadOS 16 or earlier; iPad health-data access starts with iPadOS 17. Enterprise restrictions can also prevent access. Configure the HealthKit capability and appropriate `NSHealthShareUsageDescription`/`NSHealthUpdateUsageDescription` messages, then request only the types needed for the feature.

Handle authorization and save errors without treating an empty query as permission denial. Preserve input for recoverable errors only when appropriate: [Guest User sessions on Vision Pro](https://developer.apple.com/documentation/healthkit/authorizing-access-to-health-data) prohibit HealthKit writes even when the owner previously authorized them. Apple's guidance discards passive or periodic guest writes and explains the restriction for explicit save attempts; do not queue those blocked writes for a later owner session. People can also change permissions or delete data outside your app. Reconcile those changes and ensure trends remain meaningful with partial history.

## Topics

### Essentials
- [About the HealthKit framework](https://developer.apple.com/documentation/healthkit/about-the-healthkit-framework) - Learn about the architecture and design of the HealthKit framework.
- [Setting up HealthKit](https://developer.apple.com/documentation/healthkit/setting-up-healthkit) - Set up and configure your HealthKit store.
- [Authorizing access to health data](https://developer.apple.com/documentation/healthkit/authorizing-access-to-health-data) - Request permission to read and share data in your app.
- [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting-user-privacy) - Respect and safeguard your user's privacy.
- [HealthKit updates](https://developer.apple.com/documentation/updates/healthkit) - Learn about important changes to HealthKit.
- [HealthKitUI](https://developer.apple.com/documentation/healthkitui) - Display user interface that enables a person to view and interact with their health data.

### Health Data
- [Saving data to HealthKit](https://developer.apple.com/documentation/healthkit/saving-data-to-healthkit) - Create and share HealthKit samples.
- [Reading data from HealthKit](https://developer.apple.com/documentation/healthkit/reading-data-from-healthkit) - Use queries to request sample data from HealthKit.
- **HKHealthStore** - The access point for all data managed by HealthKit.
- [Creating a Mobility Health App](https://developer.apple.com/documentation/healthkit/creating-a-mobility-health-app) - Create a health app that allows a clinical care team to send and receive mobility data.

### Data Types
- [Data types](https://developer.apple.com/documentation/healthkit/data-types) - Specify the kind of data used in HealthKit.

### Samples
- [Samples](https://developer.apple.com/documentation/healthkit/samples) - Create and save health and fitness samples.

### Queries
- [Queries](https://developer.apple.com/documentation/healthkit/queries) - Query health and fitness data.
- [Visualizing HealthKit State of Mind in visionOS](https://developer.apple.com/documentation/healthkit/visualizing-healthkit-state-of-mind-in-visionos) - Incorporate HealthKit State of Mind into your app and visualize the data in visionOS.
- [Logging symptoms associated with a medication](https://developer.apple.com/documentation/healthkit/logging-symptoms-associated-with-a-medication) - Fetch medications and dose events from the HealthKit store, and create symptom samples to associate with them.

### Workout Data
- [Workouts and activity rings](https://developer.apple.com/documentation/healthkit/workouts-and-activity-rings) - Manage workouts, workout sessions, and activity summaries.

### Errors
- **HKError** - An error returned from a HealthKit method.
- **HKErrorDomain** - The domain for all HealthKit errors.
- [`HKError.Code`](https://developer.apple.com/documentation/healthkit/hkerror/code) - Error codes returned by HealthKit.

### Reference
- [HealthKit Enumerations](https://developer.apple.com/documentation/healthkit/healthkit-enumerations)
- [HealthKit Classes](https://developer.apple.com/documentation/healthkit/healthkit-classes)
- [HealthKit Constants](https://developer.apple.com/documentation/healthkit/healthkit-constants)
- [HealthKit Data Types](https://developer.apple.com/documentation/healthkit/healthkit-data-types)
- [HealthKit Functions](https://developer.apple.com/documentation/healthkit/healthkit-functions)
- [Macros](https://developer.apple.com/documentation/healthkit/healthkit-macros)
- [HealthKit Variables](https://developer.apple.com/documentation/healthkit/healthkit-variables)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/HealthKit)*

### Additional reviewed sources

- [HealthKit updates](https://developer.apple.com/documentation/updates/healthkit)
- [iOS and iPadOS 27 release notes — HealthKit](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- [watchOS 27 release notes — HealthKit](https://developer.apple.com/documentation/watchos-release-notes/watchos-27-release-notes)
- [Authorization behavior](https://developer.apple.com/documentation/healthkit/authorizing-access-to-health-data)
- [Earliest authorized sample date](https://developer.apple.com/documentation/healthkit/hkhealthstore/getearliestauthorizedsampledate(for:completion:))
