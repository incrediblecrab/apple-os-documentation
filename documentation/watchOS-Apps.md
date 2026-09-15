# watchOS apps

Build watchOS apps that combine complications, notifications, and Siri to create a personal experience on Apple Watch.

## Overview

Apple Watch provides easy access to vital information on someone's wrist. The watchOS experience focuses on quick actions that achieve useful tasks through brief, punctuated interactions.

On Apple Watch, keep interactions as short as possible. Provide vital information at a glance, letting the wearer respond with a few taps and move on. Design appropriate status updates and notifications rather than making people wait; notification delivery still depends on authorization and system behavior.

For watchOS, expect to spend more time planning, designing, and refining your app's experience than writing the actual code. For design guidance, see Designing for watchOS.

### OS26 and OS27 planning

**Checked September 8, 2026:** watchOS **26.6** (`23U67`, July 27) was the shipping 26-generation release. **Update September 14, 2026:** watchOS **27.0** (`24R364`) is shipping. [Release listings](https://developer.apple.com/news/releases/) do not establish complete Watch/iPhone pairing requirements.

- Preserve the older-platform guidance below and the [OS26 introduction](../os26-intro/watchOS.md) when maintaining older deployment targets.
- The [watchOS 27 notes](https://developer.apple.com/documentation/watchos-release-notes/watchos-27-release-notes) add HealthKit heart-rate/cycling-power zones and deprecate `WKExtension`/`WKExtensionDelegate` for apps whose **minimum deployment target is watchOS 9.2 or later**. This is not the UIKit scene migration required on other platforms.
- Re-test SwiftUI `@State` initializers and `AsyncImage` caching with Xcode 27. Keep complications and workouts useful when the phone or network is unavailable.
- Treat fixed complication, connectivity, and workout issues as regression tests—not permanent restrictions. Check authorization and unavailable health samples separately.
- **Xcode 27** requires **Apple silicon and macOS Tahoe 26.6 or later**, not macOS 27. The macOS 27 SDK supports back deploying Universal apps to macOS 12 and later, and Intel development remains possible with Rosetta-supporting macOS such as macOS 27. See the [Xcode notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes).

The exact watchOS 27 model and companion-device list is not verified here. See the [OS27 introduction](../os27-intro/watchOS.md) for migration checks and [App Store readiness](../guides/app-store-readiness.md) for submission policy.

When designing a watchOS app, mix a combination of the following technologies to create a richer experience.

### The watchOS app

The main app serves as the foundation for your watchOS app experience. Anyone can launch and interact with your app directly. However, the app's interface isn't necessarily the primary way people interact with your app. Many may prefer to interact through complications or notifications, and may never explicitly launch your app.

### Complications

Complications provide small glimpses into your app's data directly on the watch face. People can add complications to most watch faces, but space is limited. Design complications to show information that is timely, up to date, and useful. People can also launch the watchOS app quickly and easily by tapping a complication.

### Notifications

Use notifications to alert people of significant events. You can also provide actions so that people can respond immediately without opening your app. You can use either local or remote notifications to communicate, even when your app isn't running.

### Siri

Use App Intents for modern Siri, Shortcuts, and Apple Intelligence integration. [Apple's SiriKit documentation](https://developer.apple.com/documentation/sirikit) says SiriKit, Intents, and IntentsUI retain legacy support for Shortcuts actions, widget configuration, and most existing Siri interactions. Preserve working legacy paths while migrating; do not treat this as a blanket deprecation or shutdown.

## Topics

### Essentials
- [Creating an intuitive and effective UI in watchOS 10](https://developer.apple.com/documentation/watchos-apps/creating-an-intuitive-and-effective-ui-in-watchos-10) - Provide an even more streamlined, consistent, and glanceable user experience with new design features.
- [Updating your app and widgets for watchOS 10](https://developer.apple.com/documentation/watchos-apps/updating-your-app-and-widgets-for-watchos-10) - Integrate SwiftUI elements and watch-specific features, and build widgets for the Smart Stack.
- [Building a watchOS app](https://developer.apple.com/documentation/watchOS-Apps/building_a_watchos_app) - Set up your app's life cycle and create its user interface with SwiftUI.
- [watchOS updates](https://developer.apple.com/documentation/updates/watchos) - Learn about important changes to watchOS.

### App experience
- [Setting up a watchOS project](https://developer.apple.com/documentation/watchos-apps/setting-up-a-watchos-project) - Create a new watchOS project or add a watch target to an existing iOS project.
- [Creating independent watchOS apps](https://developer.apple.com/documentation/watchos-apps/creating-independent-watchos-apps) - Set up a watchOS app that installs and runs without a companion iOS app.
- [Keeping your watchOS content up to date](https://developer.apple.com/documentation/watchOS-Apps/keeping-your-watchos-app-s-content-up-to-date) - Ensure that your app's content is relevant and up to date.
- [Updating watchOS apps with timelines](https://developer.apple.com/documentation/watchos-apps/updating-watchos-apps-with-timelines) - Seamlessly schedule updates to your user interface, even while it's inactive.
- [Authenticating users on Apple Watch](https://developer.apple.com/documentation/watchos-apps/authenticating-users-on-apple-watch) - Create an account sign-up and sign-in strategy for your app.
- [Responding to the Action button on Apple Watch Ultra](https://developer.apple.com/documentation/appintents/actionbuttonarticle) - Use App Intents to register actions for your app.
- [Enabling the double-tap gesture on Apple Watch](https://developer.apple.com/documentation/watchOS-Apps/enabling-double-tap) - Customize your app's response to the double-tap gesture on Apple Watch.

### Accessibility
- [Create accessible experiences for watchOS](https://developer.apple.com/documentation/watchos-apps/create-accessible-experiences-for-watchos) - Learn how to make your watchOS app more accessible.

### User interface
- [Building a productivity app for Apple Watch](https://developer.apple.com/documentation/watchos-apps/building-a-productivity-app-for-apple-watch) - Create a watch app to manage and share a task list and visualize the status with a chart.
- [Supporting multiple watch sizes](https://developer.apple.com/documentation/watchos-apps/supporting-multiple-watch-sizes) - Customize the layout of your user interface to support all Apple Watch sizes.
- [Designing your app for the Always On state](https://developer.apple.com/documentation/watchos-apps/designing-your-app-for-the-always-on-state) - Customize your watchOS app's user interface for continuous display.
- [Setting the app's accent color](https://developer.apple.com/documentation/watchos-apps/setting-the-app-s-accent-color) - Set your app's accent color.

### Complications
- [Creating accessory widgets and watch complications](https://developer.apple.com/documentation/widgetkit/creating-accessory-widgets-and-watch-complications) - Support accessory widgets that appear on the Lock Screen and as complications on Apple Watch.
- [Migrating ClockKit complications to WidgetKit](https://developer.apple.com/documentation/widgetkit/converting-a-clockkit-app) - Leverage WidgetKit's API to create watchOS complications using SwiftUI.
- [Creating a widget extension](https://developer.apple.com/documentation/widgetkit/creating-a-widget-extension) - Display your app's content in a convenient, informative widget on various devices.
- [Keeping a widget up to date](https://developer.apple.com/documentation/widgetkit/keeping-a-widget-up-to-date) - Plan your widget's timeline to show timely, relevant information using dynamic views, and update the timeline when things change.
- [Increasing the visibility of widgets in Smart Stacks](https://developer.apple.com/documentation/widgetkit/widget-suggestions-in-smart-stacks) - Provide contextual information and donate intents to the system to make sure your widget appears prominently in Smart Stacks.

### Notifications
- [Notifications](https://developer.apple.com/documentation/watchOS-Apps/notifications) - Communicate with users even when your app isn't running.

### Siri
- [App Intents](https://developer.apple.com/documentation/appintents) - Expose app actions and entities to supported Siri, Shortcuts, Spotlight, widget, and control experiences.
- [Creating an Intents App Extension](https://developer.apple.com/documentation/sirikit/creating-an-intents-app-extension) - Add and configure an Intents app extension in your Xcode project.

### Health and fitness
- [Setting up HealthKit](https://developer.apple.com/documentation/healthkit/setting-up-healthkit) - Set up and configure your HealthKit store.
- [Authorizing access to health data](https://developer.apple.com/documentation/healthkit/authorizing-access-to-health-data) - Request permission to read and share data in your app.
- [Saving data to HealthKit](https://developer.apple.com/documentation/healthkit/saving-data-to-healthkit) - Create and share HealthKit samples.
- [Reading data from HealthKit](https://developer.apple.com/documentation/healthkit/reading-data-from-healthkit) - Use queries to request sample data from HealthKit.
- [Build a workout app for Apple Watch](https://developer.apple.com/documentation/healthkit/build-a-workout-app-for-apple-watch) - Create your own workout app, quickly and easily, with HealthKit and SwiftUI.

### Runtime management
- [Background execution](https://developer.apple.com/documentation/watchkit/background-execution) - Manage background sessions and tasks.
- [Life cycles](https://developer.apple.com/documentation/watchkit/life-cycles) - Receive and respond to life-cycle notifications.
- [Using extended runtime sessions](https://developer.apple.com/documentation/watchkit/using-extended-runtime-sessions) - Create an extended runtime session that continues running your app after the user stops interacting with it.
- [Interacting with Bluetooth peripherals during background app refresh](https://developer.apple.com/documentation/watchkit/interacting-with-bluetooth-peripherals-during-background-app-refresh) - Keep your complications up-to-date by reading values from a Bluetooth peripheral while your app is running in the background.

### Network requests
- [Making default and ephemeral requests](https://developer.apple.com/documentation/watchOS-Apps/making-default-and-ephemeral-requests) - Send requests from your app when it's running in the foreground.
- [Making background requests](https://developer.apple.com/documentation/watchOS-Apps/making-background-requests) - Send requests from your app when it's running in the background.

### Unit tests
- [Setting up tests for your watchOS app](https://developer.apple.com/documentation/watchOS-Apps/setting-up-tests-for-your-watchos-app) - Configure your watch-only project with unit tests and user interface tests.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/watchOS-Apps)*
