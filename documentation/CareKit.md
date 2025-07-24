# CareKit

Create apps that help people better understand and manage their health.

**Platforms:** iOS 13.0+ | Mac Catalyst 13.0+ | watchOS 7.0+

## Overview

CareKit gives users the ability to manage and understand their health. Your apps can highlight trends, celebrate goals, and create incentives for users. CareKit 2.0 is available for iOS 13/iPadOS 13 and above.

CareKit makes it easy to provide engaging, consistent interfaces with delightful animations, and full interaction with the accessibility features of iOS and iPadOS.

This open source framework is written entirely in Swift, and it leverages some of the most powerful Swift language features, such as Combine.

Your CareKit apps can:
- Easily digitize a prescription.
- Provide meaningful health data and trends to users.
- Allow users to connect with their care providers.

The framework provides a powerful set of data models for persistence. Your app's user is represented in CareKit's data as a patient. A patient needs to complete a set of tasks, like taking a medication or logging their symptoms. Tasks are created with a schedule, so a patient knows when to perform each task. Schedules are composable, so you can build a complex set of requirements by combining simple ones.

The combination of a patient's tasks make up a care plan. A care plan is designed to help a user improve part of their health, for example, recovering from an operation or managing diabetes. A patient can have multiple care plans, and each care plan can have contacts associated to them. Contacts are the patient's care providers.

When a patient completes a task, the results are stored as outcomes. These outcomes and their associated values enable you to provide charts and graphs for a user, that help them understand the health impact of their care plan.

## Topics

### Essentials
- [Setting up Your Project to Use CareKit](https://carekit-apple.github.io/CareKit/documentation/carekit/setting_up_your_project_to_use_carekit) - Add and update CareKit in your project using Swift Package Manger.

### Data Management
- **OCKStore** - The database where you store all CareKit data.
- **OCKSynchronizedStoreManager** - Provides synchronization to CareKit view controllers by setting itself as the store delegate, and then listening in on the store's activity.
- **OCKLocalVersionID** - A string value that represents the ID of an object in the local database.
- **OCKSemanticVersion** - A three-component number format for specifying version numbers.
- [Save and Retrieve Data](https://carekit-apple.github.io/CareKit/documentation/carekit/save_and_retrieve_data) - Add, update, delete, and fetch data from the store.
- [Data Queries](https://carekit-apple.github.io/CareKit/documentation/carekit/data_queries) - Create querries to limit the results that the store returns.

### Tasks and Outcomes
- [Creating and Displaying Tasks for a Patient](https://carekit-apple.github.io/CareKit/documentation/carekit/creating_and_displaying_tasks_for_a_patient) - Create tasks and schedules for patients and display them using a synchronized view controller.
- [Creating Schedules for Tasks](https://carekit-apple.github.io/CareKit/documentation/carekit/creating_schedules_for_tasks) - Create schedules for tasks using multiple schedule elements.
- **OCKTask** - An object that represents some task or action a patient needs to perform.
- **OCKSchedule** - A compositon of any number of other schedulable objects.
- **OCKScheduleElement** - An object that represents a single event that repeats at fixed intervals.
- **OCKScheduleEvent** - The schedule event for the task occurrence.
- **OCKEvent** - An object that represents a single occasion on which a task is scheduled to occur.
- **OCKOutcome** - The result of an event that corresonds to a task.
- **OCKOutcomeValue** - An object that represents a measurement that a user gives in response to a task.

### Patient Data
- **OCKPatient** - A patient object that represents the user of your application.
- **OCKCarePlan** - An object that represents a set of tasks, that includes interventions and assessments a patient needs to complete for a specific condition.
- **OCKContact** - An object that represents a contact with which a user may want to get in touch.
- **OCKNote** - An object that provides additional information or context for objects and values.

### User Interface
- **OCKDailyPageViewController** - A view controller that displays a calendar in the header, and a page view controller in the body.
- **OCKDailyPageViewControllerDataSource** - A protocol that manages data changes in a view controller, that handles daily tasks, and has a synchronized calendar.
- **OCKDailyPageViewControllerDelegate** - The object that handles callbacks when important events occur in a daily page view controller.
- **OCKDailyTasksPageViewController** - A view controller that displays a calendar page view controller in the header, and a collection of tasks in the body.
- **OCKListViewController** - A view controller that displays views in a list view.
- **OCKSynchronizationContext** - An object that provides context for a view model value.
- [Task Interfaces](https://carekit-apple.github.io/CareKit/documentation/carekit/task_interfaces) - Display tasks to users.
- [Chart Interfaces](https://carekit-apple.github.io/CareKit/documentation/carekit/chart_interfaces) - Display charts to users.
- [Contacts Interfaces](https://carekit-apple.github.io/CareKit/documentation/carekit/contacts_interfaces) - Display contacts to users.
- [Calendar Interfaces](https://carekit-apple.github.io/CareKit/documentation/carekit/calendar_interfaces) - Display calendars to users.
- [Components](https://carekit-apple.github.io/CareKit/documentation/carekit/components) - Create and customize controls, labels, and views.
- [Style and Appearance](https://carekit-apple.github.io/CareKit/documentation/carekit/style_and_appearance) - Customize the style and appearance of user interface elements.

### Data Customization
- **OCKAnyTask** - A protocol that allows you to query and display a custom task data type.
- **OCKAnyOutcome** - A protocol that allows you to query and display a custom outcome data type.
- **OCKOutcomeValueUnderlyingType** - A protocol that allows you to query and disply a custom underlying outcome value data type.
- **OCKAnyContact** - A protocol that allows you to query and display a custom contact data type.
- **OCKAnyPatient** - A protocol that allows you to query and display a custom patient data type.
- **OCKAnyCarePlan** - A protocol that allows you to query and display a custom patient data type.
- **OCKAnyVersionableTask** - A task you can version and persist in a database.
- **OCKAnyEvent** - An object that represents a single occasion on which a task is scheduled to occur.

### Protocols
- **OCKDailyTasksPageViewControllerDelegate** - Handles events related to an OCKDailyTasksPageViewController.
- **OCKStoreNotification**

### Structures
- **OCKCarePlanNotification**
- **OCKContactNotification**
- **OCKOutcomeNotification**
- **OCKPatientNotification**
- **OCKTaskNotification**

### Type Aliases
- **OCKButtonLogTaskViewController**
- **OCKCartesianChartController**
- **OCKCartesianChartViewController**
- **OCKChecklistTaskController**
- **OCKChecklistTaskViewController**
- **OCKDetailedContactController**
- **OCKDetailedContactViewController**
- **OCKGridTaskController**
- **OCKInstructionsTaskController**
- **OCKInstructionsTaskViewController**
- **OCKSimpleContactController**
- **OCKSimpleContactViewController**
- **OCKSimpleTaskController**
- **OCKWeekCalendarViewController**

### Enumerations
- **OCKStoreNotificationCategory**

---

*Source: [CareKit Documentation](https://carekit-apple.github.io/CareKit/documentation/carekit)*