# HealthKit

Access and share health and fitness data while maintaining the user's privacy and control.

**Platforms:** iOS 8.0+ | iPadOS 8.0+ | Mac Catalyst 17.0+ | macOS 14.0+ | visionOS 1.0+ | watchOS 2.0+

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

## Topics

### Essentials
- [About the HealthKit framework](https://developer.apple.com/documentation/healthkit/about_the_healthkit_framework) - Learn about the architecture and design of the HealthKit framework.
- [Setting up HealthKit](https://developer.apple.com/documentation/healthkit/setting_up_healthkit) - Set up and configure your HealthKit store.
- [Authorizing access to health data](https://developer.apple.com/documentation/healthkit/authorizing_access_to_health_data) - Request permission to read and share data in your app.
- [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting_user_privacy) - Respect and safeguard your user's privacy.
- [HealthKit updates](https://developer.apple.com/documentation/healthkit/healthkit_updates) - Learn about important changes to HealthKit.
- [HealthKitUI](https://developer.apple.com/documentation/healthkitui) - Display user interface that enables a person to view and interact with their health data.

### Health Data
- [Saving data to HealthKit](https://developer.apple.com/documentation/healthkit/saving_data_to_healthkit) - Create and share HealthKit samples.
- [Reading data from HealthKit](https://developer.apple.com/documentation/healthkit/reading_data_from_healthkit) - Use queries to request sample data from HealthKit.
- **HKHealthStore** - The access point for all data managed by HealthKit.
- [Creating a Mobility Health App](https://developer.apple.com/documentation/healthkit/creating_a_mobility_health_app) - Create a health app that allows a clinical care team to send and receive mobility data.

### Data Types
- [Data types](https://developer.apple.com/documentation/healthkit/data_types) - Specify the kind of data used in HealthKit.

### Samples
- [Samples](https://developer.apple.com/documentation/healthkit/samples) - Create and save health and fitness samples.

### Queries
- [Queries](https://developer.apple.com/documentation/healthkit/queries) - Query health and fitness data.
- [Visualizing HealthKit State of Mind in visionOS](https://developer.apple.com/documentation/healthkit/visualizing_healthkit_state_of_mind_in_visionos) - Incorporate HealthKit State of Mind into your app and visualize the data in visionOS.
- [Logging symptoms associated with a medication](https://developer.apple.com/documentation/healthkit/logging_symptoms_associated_with_a_medication) - Fetch medications and dose events from the HealthKit store, and create symptom samples to associate with them.

### Workout Data
- [Workouts and activity rings](https://developer.apple.com/documentation/healthkit/workouts_and_activity_rings) - Manage workouts, workout sessions, and activity summaries.

### Errors
- **HKError** - An error returned from a HealthKit method.
- **HKErrorDomain** - The domain for all HealthKit errors.
- **Code** - Error codes returned by HealthKit.

### Reference
- **HealthKit Enumerations**
- **HealthKit Classes**
- **HealthKit Constants**
- **HealthKit Data Types**
- **HealthKit Functions**
- **Macros**
- **HealthKit Variables**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/HealthKit)*