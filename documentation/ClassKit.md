# ClassKit

Enable teachers to assign activities from your app's content and to view student progress.

**Platforms:** iOS 11.4+ | iPadOS 11.4+ | Mac Catalyst 14.0+ | macOS 11.0+ | visionOS 1.0+

## Overview

Educational apps provide access to resources like books and videos while reinforcing learning through interactive visualizations, games, and assessments. ClassKit lets you organize educational material so that teachers can assign activities to students and see their progress.

The ClassKit environment consists of a teacher's device (or devices) and many student devices communicating through iCloud. Each device runs your app (plus other educational apps) along with Apple's Schoolwork app, with ClassKit acting as a hub on the device. Using Schoolwork, teachers can see what assignable content your app exposes to ClassKit. They can then create assignments based on that content, and monitor progress of all their students. Meanwhile, students use Schoolwork to receive assignments that link directly to content in your app.

ClassKit doesn't replace any existing logic or storage mechanisms in your app, and you don't use it to generate any new user interfaces. Instead, you use ClassKit to publicize the structure you already have, so that teachers can use Apple's Schoolwork app to create assignments based on your app's content and measure their students' progress through those assignments.

Note: ClassKit is designed for educational organizations that use Apple School Manager and Managed Apple IDs. Consider adopting ClassKit if education is your intended market.

## Topics

### Essentials
- [Enabling ClassKit in your app](https://developer.apple.com/documentation/ClassKit/enabling_classkit_in_your_app) - Prepare your app and your development environment to adopt ClassKit.
- **ClassKit Environment Entitlement** - The ClassKit development or production environment for an education app that works with the Schoolwork app.
- [Incorporating ClassKit into an Educational App](https://developer.apple.com/documentation/ClassKit/incorporating_classkit_into_an_educational_app) - Walk through the process of setting up assignments and recording student progress.
- **CLSDataStore** - A container for all the ClassKit data in your app.

### Contexts
- [Advertising your app's assignable content](https://developer.apple.com/documentation/ClassKit/advertising_your_app_s_assignable_content) - Assemble a hierarchy of contexts and declare your app's assignable content.
- **CLSContext** - An area of your app that represents an assignable task, like a quiz or a chapter.
- **CLSContextProvider** - An interface used to tell your ClassKit context provider app extension to update contexts.

### Activities
- [Recording student progress](https://developer.apple.com/documentation/ClassKit/recording_student_progress) - Create an activity to record student progress through an assignment.
- **CLSActivity** - A representation of user interaction with a context.

### Activity items
- [Recording additional metrics about a completed task](https://developer.apple.com/documentation/ClassKit/recording_additional_metrics_about_a_completed_task) - Add an activity item to an activity to record additional information about a student's attempt to complete a task.
- **CLSScoreItem** - Activity information that signifies a score out of a possible maximum.
- **CLSBinaryItem** - Activity information that is true or false, pass or fail, yes or no.
- **CLSQuantityItem** - Activity information that signifies a quantity.
- **CLSActivityItem** - An abstract base class for gathering information about an activity.

### Errors
- **CLSError** - Errors issued by ClassKit.
- **CLSErrorCodeDomain** - The error domain that ClassKit uses when issuing errors.
- **Code** - Error codes that ClassKit issues.
- **CLSErrorUserInfoKey** - Keys that appear in the user info dictionary in errors that ClassKit creates.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ClassKit)*