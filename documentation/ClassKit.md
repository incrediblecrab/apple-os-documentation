# ClassKit

Enable teachers to assign activities from your app's content and to view student progress.

**Platforms:** iOS 11.4+ | iPadOS 11.4+ | Mac Catalyst 14.0+ | macOS 11.0+ | visionOS 1.0+

## Overview

Educational apps provide access to resources like books and videos while reinforcing learning through interactive visualizations, games, and assessments. ClassKit lets you organize educational material so that teachers can assign activities to students and see their progress.

The ClassKit environment consists of a teacher's device (or devices) and many student devices communicating through iCloud. Each device runs your app (plus other educational apps) along with Apple's Schoolwork app, with ClassKit acting as a hub on the device. Using Schoolwork, teachers can see what assignable content your app exposes to ClassKit. They can then create assignments based on that content, and monitor progress of all their students. Meanwhile, students use Schoolwork to receive assignments that link directly to content in your app.

ClassKit publishes your existing content structure and records assignment activity; it does not replace your app's own storage or teaching interface. For student-facing submission controls, use the separate [ClassKit UI](ClassKitUI.md) framework, whose initial controls are available from 26.4 on their supported platforms, not first in OS 27.

Note: ClassKit is designed for educational organizations that use Apple School Manager and Managed Apple IDs. Consider adopting ClassKit if education is your intended market.

## Setup and reliability

Enable the [ClassKit environment entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.classkit-environment) and follow Apple's development/production setup. Keep context identifiers stable so that assignments continue to open the intended content, and preserve the app's own learning state if a ClassKit save fails. Handle `CLSError` instead of treating a locally created activity as confirmation of synchronized progress.

Activity saves are limited to managed student accounts that have received an assignment for that context. Saves for other people, including teachers and students without that assignment, can silently fail. ClassKit keeps the person's role private; do not infer authorization from the absence of an error. See [Recording student progress](https://developer.apple.com/documentation/classkit/recording-student-progress).

Use [ClassKit Catalog API](ClassKitCatalogAPI.md) for a public, teacher-browsable activity catalog. Keep user-specific contexts in the runtime ClassKit integration. [Apple School Manager API](AppleSchoolAndBusinessManagerAPI.md) manages the organization's resources; it is not a replacement for ClassKit assignment/progress APIs.

## Topics

### Essentials
- [Enabling ClassKit in your app](https://developer.apple.com/documentation/ClassKit/enabling-classkit-in-your-app) - Prepare your app and your development environment to adopt ClassKit.
- **ClassKit Environment Entitlement** - The ClassKit development or production environment for an education app that works with the Schoolwork app.
- [Incorporating ClassKit into an Educational App](https://developer.apple.com/documentation/ClassKit/incorporating-classkit-into-an-educational-app) - Set up assignments and record student progress.
- [ClassKit UI](ClassKitUI.md) - Integrate submission and withdrawal controls for assigned documents.
- **CLSDataStore** - A container for all the ClassKit data in your app.

### Contexts
- [Advertising your app's assignable content](https://developer.apple.com/documentation/ClassKit/advertising-your-app-s-assignable-content) - Assemble a hierarchy of contexts and declare your app's assignable content.
- **CLSContext** - An area of your app that represents an assignable task, like a quiz or a chapter.
- **CLSContextProvider** - An interface used to tell your ClassKit context provider app extension to update contexts.

### Activities
- [Recording student progress](https://developer.apple.com/documentation/ClassKit/recording-student-progress) - Create an activity to record student progress through an assignment.
- **CLSActivity** - A representation of user interaction with a context.

### Activity items
- [Recording additional metrics about a completed task](https://developer.apple.com/documentation/ClassKit/recording-additional-metrics-about-a-completed-task) - Add information about a student's attempt to complete a task.
- **CLSScoreItem** - Activity information that signifies a score out of a possible maximum.
- **CLSBinaryItem** - Activity information that is true or false, pass or fail, yes or no.
- **CLSQuantityItem** - Activity information that signifies a quantity.
- **CLSActivityItem** - An abstract base class for gathering information about an activity.

### Errors
- **CLSError** - Errors issued by ClassKit.
- **CLSErrorCodeDomain** - The error domain that ClassKit uses when issuing errors.
- [**CLSError.Code**](https://developer.apple.com/documentation/classkit/clserror/code) - Error codes that ClassKit issues.
- **CLSErrorUserInfoKey** - Keys that appear in the user info dictionary in errors that ClassKit creates.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ClassKit)*
