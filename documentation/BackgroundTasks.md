# Background Tasks

Support background processing in your app by wrapping your app's most critical work in framework-provided tasks.

**Platforms:** iOS 13.0+ | iPadOS 13.0+ | Mac Catalyst 13.1+ | tvOS 13.0+ | visionOS 1.0+

## Overview

Use this framework to request execution for refresh, maintenance, or eligible user-initiated work. The system decides when scheduled background tasks run. A request does not guarantee a start time, uninterrupted execution, or completion.

To launch your app in the background and perform necessary work, register launch handlers for framework-provided tasks and schedule the tasks as needed.

Your app can also use a framework-provided task to execute critical jobs in the foreground and complete them in the background if a person backgrounds your app before the job completes.

Register each task identifier only once and configure the permitted identifiers and background modes required by its task type. Scheduled-task handlers must be registered before app launch finishes; the SDK explicitly exempts continued-processing registrations from that launch-time deadline. Registration and submission can fail, including when the person denies background launches or requested resources are unavailable.

### Continued processing is distinct from scheduled work

`BGContinuedProcessingTask` and its request type were introduced in **iOS/iPadOS 26.0**. The workflow starts with a person's action in the foreground and can continue after the app moves to the background. It is not a timer for unattended periodic jobs.

**Catalyst source conflict:** Apple's current DocC catalog lists Mac Catalyst 26.0 for continued processing, but the public macOS 26.5 SDK explicitly marks the task, request, and `supportedResources` unavailable in Catalyst. Do not treat the catalog entry as confirmed Catalyst support; check the declarations in the SDK used to build your app.

Choose whether submission queues under resource pressure (the default `.queue` strategy) or uses `.fail` if it cannot start immediately. Report progress, install an expiration handler, stop work on cancellation, and complete the task with the correct result. Closing the app from the app switcher cancels running work without an expiration notification. Persist enough state to recover later.

Background GPU access requires supported hardware, a check of `BGTaskScheduler.supportedResources`, the requested `.gpu` resource, and the `com.apple.developer.background-tasks.continued-processing.gpu` entitlement. None of these removes task scheduling or cancellation constraints.

### 27 beta: background inference entitlement

**Reviewed September 8, 2026:** Background access to the Neural Engine requires [`com.apple.developer.background-tasks.continued-processing.inference`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.background-tasks.continued-processing.inference) on the 27 operating systems. Apple's entitlement documentation explicitly applies this requirement even when inference is **not** inside a continued-processing task, including work using Core AI, Core ML, or Metal Performance Shaders Graph.

The entitlement is Boolean and defaults to `NO` in Apple's property metadata. Its declared platforms are iOS, iPadOS, macOS, tvOS, visionOS, and watchOS 27.0; the entitlement reference does not supply a Mac Catalyst minimum. Enable the Background Inference capability for the appropriate target; a usage-description string is not a replacement.

The entitlement is not a guarantee of background runtime or device support, and it is distinct from background GPU authorization. Check the availability of the processing API and execution context separately.

For transferring content instead of computing it, consider [Background Assets](BackgroundAssets.md) or background `URLSession` downloads. See [Migrating On Demand Resources to Background Assets](../guides/background-assets-migration.md).

## Topics

### Essentials
- [Background Tasks updates](https://developer.apple.com/documentation/updates/backgroundtasks) - Learn about important changes in Background Tasks.
- **BGTaskScheduler** - A class for scheduling tasks that add background support to your app's most critical work.
- **BGTask** - An abstract class for the framework's tasks.

### Background Tasks
- [Using background tasks to update your app](https://developer.apple.com/documentation/uikit/using-background-tasks-to-update-your-app) - Configure your app to perform tasks in the background to make efficient use of processing time and power.
- [Refreshing and Maintaining Your App Using Background Tasks](https://developer.apple.com/documentation/backgroundtasks/refreshing-and-maintaining-your-app-using-background-tasks) - Use scheduled background tasks for refreshing your app content and for performing maintenance.
- [Choosing Background Strategies for Your App](https://developer.apple.com/documentation/backgroundtasks/choosing-background-strategies-for-your-app) - Select the best method of scheduling background runtime for your app.
- **BGProcessingTask** - A time-consuming processing task that runs while the app is in the background.
- **BGAppRefreshTask** - An object representing a short task typically used to refresh content that's run while the app is in the background.
- **BGHealthResearchTask** - Processing for a health research study the person has joined; requires `com.apple.developer.backgroundtasks.healthresearch`. The task is available from iOS/iPadOS/Mac Catalyst 17.0 and visionOS 1.0, not the framework's older minimum.

### Foreground Tasks with Background Support
- [Performing long-running tasks on iOS and iPadOS](https://developer.apple.com/documentation/backgroundtasks/performing-long-running-tasks-on-ios-and-ipados) - Configure user-initiated work, progress reporting, cancellation, and resource requests.
- **BGContinuedProcessingTask** - A task for user-initiated work that can continue after the app backgrounds.
- [Background GPU Access](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.background-tasks.continued-processing.gpu) - Authorization required for supported background GPU execution.
- [Background Inference](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.background-tasks.continued-processing.inference) - Authorization required for background Neural Engine access in the 27 generation.

### Task Requests
- **BGProcessingTaskRequest** - A request to launch your app in the background to execute a processing task that can take minutes to complete.
- **BGAppRefreshTaskRequest** - A request to launch your app in the background to execute a short refresh task.
- **BGTaskRequest** - An abstract class for representing task requests.
- **BGHealthResearchTaskRequest** - A request for an opted-in health research study. Its declaration additionally lists tvOS 17.0; that does not establish tvOS availability of `BGHealthResearchTask` itself.
- **BGContinuedProcessingTaskRequest** - A request for a workload that the system continues processing even if a person backgrounds the app.

### Development and Testing
- [Starting and Terminating Tasks During Development](https://developer.apple.com/documentation/backgroundtasks/starting-and-terminating-tasks-during-development) - Device-only debugger testing of launch and expiration. Its private simulation functions are development tools, not APIs to include in a distributed app.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/BackgroundTasks)*

*Changed-content sources: [continued-processing lifecycle](https://developer.apple.com/documentation/backgroundtasks/performing-long-running-tasks-on-ios-and-ipados.md), [background inference entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.background-tasks.continued-processing.inference.md), and [iOS/iPadOS 27 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes.md).*
