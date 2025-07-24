# Background Tasks

Support background processing in your app by wrapping your app's most critical work in framework-provided tasks.

**Platforms:** iOS 13.0+ | iPadOS 13.0+ | Mac Catalyst 13.1+ | tvOS 13.0+ | visionOS 1.0+

## Overview

Use this framework to keep your app content up to date and run tasks requiring minutes to complete even if your app is in the background. Longer tasks can leverage external power, network connectivity, and the GPU on supported devices.

To launch your app in the background and perform necessary work, register launch handlers for framework-provided tasks and schedule the tasks as needed.

Your app can also use a framework-provided task to execute critical jobs in the foreground and complete them in the background if a person backgrounds your app before the job completes.

## Topics

### Essentials
- [Background Tasks updates](https://developer.apple.com/documentation/backgroundtasks/background_tasks_updates) - Learn about important changes in Background Tasks.
- **BGTaskScheduler** - A class for scheduling tasks that add background support to your app's most critical work.
- **BGTask** - An abstract class for the framework's tasks.

### Background Tasks
- [Using background tasks to update your app](https://developer.apple.com/documentation/backgroundtasks/using_background_tasks_to_update_your_app) - Configure your app to perform tasks in the background to make efficient use of processing time and power.
- [Refreshing and Maintaining Your App Using Background Tasks](https://developer.apple.com/documentation/backgroundtasks/refreshing_and_maintaining_your_app_using_background_tasks) - Use scheduled background tasks for refreshing your app content and for performing maintenance.
- [Choosing Background Strategies for Your App](https://developer.apple.com/documentation/backgroundtasks/choosing_background_strategies_for_your_app) - Select the best method of scheduling background runtime for your app.
- **BGProcessingTask** - A time-consuming processing task that runs while the app is in the background.
- **BGAppRefreshTask** - An object representing a short task typically used to refresh content that's run while the app is in the background.
- **BGHealthResearchTask** - A time-consuming, necessary processing task that runs while the app is in the background to prepare data essential to a health research study.

### Foreground Tasks with Background Support
- [Performing long-running tasks on iOS and iPadOS](https://developer.apple.com/documentation/backgroundtasks/performing_long-running_tasks_on_ios_and_ipados) - Use a continuous background task to do work that can complete as needed.
- **BGContinuedProcessingTask** - A task that starts in the foreground and can continue running in the background as needed. (Beta)
- **Background GPU Access** - The entitlement the system requires for a continuous background task to use the GPU. (Beta)

### Task Requests
- **BGProcessingTaskRequest** - A request to launch your app in the background to execute a processing task that can take minutes to complete.
- **BGAppRefreshTaskRequest** - A request to launch your app in the background to execute a short refresh task.
- **BGTaskRequest** - An abstract class for representing task requests.
- **BGHealthResearchTaskRequest** - A request to launch your app in the background to execute processing for a health research study in which a user participates.
- **BGContinuedProcessingTaskRequest** - A request for a workload that the system continues processing even if a person backgrounds the app. (Beta)

### Development and Testing
- [Starting and Terminating Tasks During Development](https://developer.apple.com/documentation/backgroundtasks/starting_and_terminating_tasks_during_development) - Use the debugger during development to start tasks and to terminate them before completion.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/BackgroundTasks)*