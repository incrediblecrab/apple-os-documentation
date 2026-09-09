# CareKit

Create apps that help people better understand and manage their health.

**Platforms:** Depend on the selected CareKit release and product; this is a separately versioned open-source package.

## Overview

CareKit provides models, persistence, and interface components for care-related apps. An app can present scheduled activities, record responses, display trends, and help people contact their support network.

The framework is written in Swift. Its UI components support accessibility features, but custom layouts, content, and interactions still need accessibility testing. Combine, used by older synchronization APIs, is a framework rather than a Swift language feature.

A patient model can have care plans containing tasks and contacts. These relationships are not mandatory for every object: tasks, contacts, and care plans can exist without a parent care plan or patient. Contacts can include clinicians, family members, and other support contacts, not only care providers.

Schedules combine calendar-based elements to describe task occurrences. The app records outcomes and associated values for those occurrences; performing a real-world activity does not itself guarantee a saved outcome. Displaying recorded trends is not evidence that a treatment caused a health improvement.

### Version and module scope

The [hosted documentation](https://carekit-apple.github.io/CareKit/documentation/carekit) describes the older CareKit 2.0 API generation and lists iOS/iPadOS 13, Mac Catalyst 13, and watchOS 7 catalog availability. The topic links below preserve that catalog; its setup and synchronization examples are not a current-`main` migration guide.

The current [`Package.swift`](https://github.com/carekit-apple/CareKit/blob/main/Package.swift) declares Swift tools 6.1 and platform minimums of iOS 18, macOS 15, and watchOS 11. It exposes CareKit, CareKitUI, CareKitStore, and optional CareKitFHIR products. These package declarations do not make every UIKit view controller usable on every listed platform. Pin a compatible release or commit and consult its README and manifest.

In current `main`, `OCKSynchronizedStoreManager` and its notification types are explicitly **unavailable**, not merely discouraged. Store asynchronous streams replace that synchronization mechanism. Several older controller names are also unavailable, with their functionality moved to the corresponding view controllers. The entries below identify those names without inventing an OS 27 removal date.

## Topics

### Essentials
- [Setting up Your Project to Use CareKit](https://carekit-apple.github.io/CareKit/documentation/carekit/setting-up-your-project-to-use-carekit) - Older package-integration guide. Use the selected release's manifest and README for current tools and resource handling.

### Data Management
- **OCKStore** - The provided Core Data-backed store; compatible custom stores are also possible.
- **OCKSynchronizedStoreManager** - Legacy delegate-based synchronization wrapper; unavailable in current `main`.
- **OCKLocalVersionID** - A legacy-catalog structure representing a local object-version identifier, not a `String` type alias.
- **OCKSemanticVersion** - A three-component number format for specifying version numbers.
- [Save and Retrieve Data](https://carekit-apple.github.io/CareKit/documentation/carekit/save-and-retrieve-data) - Add, update, delete, and fetch data from the store.
- [Data Queries](https://carekit-apple.github.io/CareKit/documentation/carekit/data-queries) - Construct queries that filter the store's results.

Check store-operation results before reporting a successful save. Handle validation and persistence failures, and surface relevant UI/delegate errors rather than treating an empty display as proof that no data exists.

### Tasks and Outcomes
- [Creating and Displaying Tasks for a Patient](https://carekit-apple.github.io/CareKit/documentation/carekit/creating-and-displaying-tasks-for-a-patient) - Older task/schedule and store-manager workflow; see the version distinction above.
- [Creating Schedules for Tasks](https://carekit-apple.github.io/CareKit/documentation/carekit/creating-schedules-for-tasks) - Compose task schedules from multiple elements.
- **OCKTask** - An object that represents some task or action a patient needs to perform.
- **OCKSchedule** - A composition of schedule elements.
- **OCKScheduleElement** - An element describing occurrences using dates and calendar intervals, with duration and target-value configuration.
- **OCKScheduleEvent** - The schedule event for the task occurrence.
- **OCKEvent** - An object that represents a single occasion on which a task is scheduled to occur.
- **OCKOutcome** - A recorded result for a task occurrence.
- **OCKOutcomeValue** - An object that represents a measurement that a user gives in response to a task.

### Patient Data
- **OCKPatient** - A record for a person whose care the app manages.
- **OCKCarePlan** - A record grouping related care activities, optionally associated with a patient.
- **OCKContact** - An object that represents a contact with which a user may want to get in touch.
- **OCKNote** - An object that provides additional information or context for objects and values.

### User Interface
- **OCKDailyPageViewController** - A view controller that displays a calendar in the header, and a page view controller in the body.
- **OCKDailyPageViewControllerDataSource** - Supplies content for a day's list view controller.
- **OCKDailyPageViewControllerDelegate** - The object that handles callbacks when important events occur in a daily page view controller.
- **OCKDailyTasksPageViewController** - A view controller that displays a calendar page view controller in the header, and a collection of tasks in the body.
- **OCKListViewController** - A view controller that displays views in a list view.
- **OCKSynchronizationContext** - A structure containing current and previous view-model values and an animation flag.
- [Task Interfaces](https://carekit-apple.github.io/CareKit/documentation/carekit/task-interfaces) - Display tasks to users.
- [Chart Interfaces](https://carekit-apple.github.io/CareKit/documentation/carekit/chart-interfaces) - Display charts to users.
- [Contacts Interfaces](https://carekit-apple.github.io/CareKit/documentation/carekit/contacts-interfaces) - Display contacts to users.
- [Calendar Interfaces](https://carekit-apple.github.io/CareKit/documentation/carekit/calendar-interfaces) - Display calendars to users.
- [Components](https://carekit-apple.github.io/CareKit/documentation/carekit/components) - Create and customize controls, labels, and views.
- [Style and Appearance](https://carekit-apple.github.io/CareKit/documentation/carekit/style-and-appearance) - Customize the style and appearance of user interface elements.

### Data Customization
- **OCKAnyTask** - A protocol that allows you to query and display a custom task data type.
- **OCKAnyOutcome** - A protocol that allows you to query and display a custom outcome data type.
- **OCKOutcomeValueUnderlyingType** - The protocol for underlying outcome values. Current `OCKOutcomeValue` storage and encoding handle `Int`, `Double`, `Bool`, `String`, `Data`, and `Date`; protocol conformance alone does not make arbitrary custom values supported.
- **OCKAnyContact** - A protocol that allows you to query and display a custom contact data type.
- **OCKAnyPatient** - A protocol that allows you to query and display a custom patient data type.
- **OCKAnyCarePlan** - A protocol for a custom care-plan data type.
- **OCKAnyVersionableTask** - A task you can version and persist in a database.
- **OCKAnyEvent** - A protocol for a custom task-event representation.

### Protocols
- **OCKDailyTasksPageViewControllerDelegate** - Handles events related to an OCKDailyTasksPageViewController.
- **OCKStoreNotification** - Legacy notification protocol; unavailable in current `main`.

### Structures
- **OCKCarePlanNotification** - Unavailable in current `main`.
- **OCKContactNotification** - Unavailable in current `main`.
- **OCKOutcomeNotification** - Unavailable in current `main`.
- **OCKPatientNotification** - Unavailable in current `main`.
- **OCKTaskNotification** - Unavailable in current `main`.

### Additional Controllers
- **OCKButtonLogTaskViewController**
- **OCKCartesianChartController** - Unavailable in current `main`; use `OCKCartesianChartViewController`.
- **OCKCartesianChartViewController**
- **OCKChecklistTaskController** - Unavailable in current `main`; use `OCKChecklistTaskViewController`.
- **OCKChecklistTaskViewController**
- **OCKDetailedContactController** - Unavailable in current `main`; use `OCKDetailedContactViewController`.
- **OCKDetailedContactViewController**
- **OCKGridTaskController** - Unavailable in current `main`; use `OCKGridTaskViewController`.
- **OCKInstructionsTaskController** - Unavailable in current `main`; use `OCKInstructionsTaskViewController`.
- **OCKInstructionsTaskViewController**
- **OCKSimpleContactController** - Unavailable in current `main`; use `OCKSimpleContactViewController`.
- **OCKSimpleContactViewController**
- **OCKSimpleTaskController** - Unavailable in current `main`; use `OCKSimpleTaskViewController`.
- **OCKWeekCalendarViewController**

### Enumerations
- **OCKStoreNotificationCategory** - Legacy add/update/delete notification categories; unavailable in current `main`.

---

*Source: [CareKit Documentation](https://carekit-apple.github.io/CareKit/documentation/carekit)*

*Current source: [CareKit repository and README](https://github.com/carekit-apple/CareKit), including its manifest and explicit unavailable declarations.*
