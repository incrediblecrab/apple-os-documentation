# watchOS apps

Build watchOS apps that combine complications, notifications, and Siri to create a personal experience on Apple Watch.

## Overview

Apple Watch provides easy access to vital information on someone's wrist. The watchOS experience focuses on quick actions that achieve useful tasks through brief, punctuated interactions.

On Apple Watch, keep interactions as short as possible. Provide vital information at a glance, encouraging the wearer to respond with just a few taps, and then drop their wrist and move on. They don't need to wait to see if the action succeeds; instead, the watchOS app automatically notifies them of any important updates.

For watchOS, expect to spend more time planning, designing, and refining your app's experience than writing the actual code. For design guidance, see Designing for watchOS.

When designing a watchOS app, mix a combination of the following technologies to create a richer experience.

### The watchOS app

The main app serves as the foundation for your watchOS app experience. Anyone can launch and interact with your app directly. However, the app's interface isn't necessarily the primary way people interact with your app. Many may prefer to interact through complications or notifications, and may never explicitly launch your app.

### Complications

Complications provide small glimpses into your app's data directly on the watch face. People can add complications to most watch faces, but space is limited. Design complications to show information that is timely, up to date, and useful. People can also launch the watchOS app quickly and easily by tapping a complication.

### Notifications

Use notifications to alert people of significant events. You can also provide actions so that people can respond immediately without opening your app. You can use either local or remote notifications to communicate, even when your app isn't running.

### Siri

Use SiriKit and App intents to expand the ways people can interact with your app. If your app uses domains like messaging or media, use SiriKit to add Siri support to your app. For other features, use App Intents to expose your app's functionality to system services like Siri and the Shortcuts app.

## Topics

### Essentials
- [Creating an intuitive and effective UI in watchOS 10](https://developer.apple.com/documentation/watchos-apps/creating-an-intuitive-and-effective-ui-in-watchos-10) - Provide an even more streamlined, consistent, and glanceable user experience with new design features.
- [Updating your app and widgets for watchOS 10](https://developer.apple.com/documentation/watchos-apps/updating-your-app-and-widgets-for-watchos-10) - Integrate SwiftUI elements and watch-specific features, and build widgets for the Smart Stack.
- [Building a watchOS app](https://developer.apple.com/documentation/watchos-apps/building-a-watchos-app) - Set up your app's life cycle and create its user interface with SwiftUI.
- [watchOS updates](https://developer.apple.com/documentation/watchos-apps/watchos-updates) - Learn about important changes to watchOS.

### App experience
- [Setting up a watchOS project](https://developer.apple.com/documentation/watchos-apps/setting-up-a-watchos-project) - Create a new watchOS project or add a watch target to an existing iOS project.
- [Creating independent watchOS apps](https://developer.apple.com/documentation/watchos-apps/creating-independent-watchos-apps) - Set up a watchOS app that installs and runs without a companion iOS app.
- [Keeping your watchOS content up to date](https://developer.apple.com/documentation/watchos-apps/keeping-your-watchos-content-up-to-date) - Ensure that your app's content is relevant and up to date.
- [Updating watchOS apps with timelines](https://developer.apple.com/documentation/watchos-apps/updating-watchos-apps-with-timelines) - Seamlessly schedule updates to your user interface, even while it's inactive.
- [Authenticating users on Apple Watch](https://developer.apple.com/documentation/watchos-apps/authenticating-users-on-apple-watch) - Create an account sign-up and sign-in strategy for your app.
- [Responding to the Action button on Apple Watch Ultra](https://developer.apple.com/documentation/watchos-apps/responding-to-the-action-button-on-apple-watch-ultra) - Use App Intents to register actions for your app.
- [Enabling the double-tap gesture on Apple Watch](https://developer.apple.com/documentation/watchos-apps/enabling-the-double-tap-gesture-on-apple-watch) - Customize your app's response to the double-tap gesture on Apple Watch.

### Accessibility
- [Create accessible experiences for watchOS](https://developer.apple.com/documentation/watchos-apps/create-accessible-experiences-for-watchos) - Learn how to make your watchOS app more accessible.

### User interface
- [Building a productivity app for Apple Watch](https://developer.apple.com/documentation/watchos-apps/building-a-productivity-app-for-apple-watch) - Create a watch app to manage and share a task list and visualize the status with a chart.
- [Supporting multiple watch sizes](https://developer.apple.com/documentation/watchos-apps/supporting-multiple-watch-sizes) - Customize the layout of your user interface to support all Apple Watch sizes.
- [Designing your app for the Always On state](https://developer.apple.com/documentation/watchos-apps/designing-your-app-for-the-always-on-state) - Customize your watchOS app's user interface for continuous display.
- [Setting the app's accent color](https://developer.apple.com/documentation/watchos-apps/setting-the-app-s-accent-color) - Set your app's accent color.

### Complications
- [Creating accessory widgets and watch complications](https://developer.apple.com/documentation/watchos-apps/creating-accessory-widgets-and-watch-complications) - Support accessory widgets that appear on the Lock Screen and as complications on Apple Watch.
- [Migrating ClockKit complications to WidgetKit](https://developer.apple.com/documentation/watchos-apps/migrating-clockkit-complications-to-widgetkit) - Leverage WidgetKit's API to create watchOS complications using SwiftUI.
- [Creating a widget extension](https://developer.apple.com/documentation/watchos-apps/creating-a-widget-extension) - Display your app's content in a convenient, informative widget on various devices.
- [Keeping a widget up to date](https://developer.apple.com/documentation/watchos-apps/keeping-a-widget-up-to-date) - Plan your widget's timeline to show timely, relevant information using dynamic views, and update the timeline when things change.
- [Increasing the visibility of widgets in Smart Stacks](https://developer.apple.com/documentation/watchos-apps/increasing-the-visibility-of-widgets-in-smart-stacks) - Provide contextual information and donate intents to the system to make sure your widget appears prominently in Smart Stacks.

### Notifications
- [Notifications](https://developer.apple.com/documentation/usernotifications) - Communicate with users even when your app isn't running.

### Siri
- [Making actions and content discoverable and widely available](https://developer.apple.com/documentation/appintents/making-actions-and-content-discoverable-and-widely-available) - Adopt App Intents to make your app discoverable with Spotlight, controls, widgets, and the Action button.
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
- [Making default and ephemeral requests](https://developer.apple.com/documentation/foundation/urlsession/making-default-and-ephemeral-requests) - Send requests from your app when it's running in the foreground.
- [Making background requests](https://developer.apple.com/documentation/foundation/urlsession/making-background-requests) - Send requests from your app when it's running in the background.

### Unit tests
- [Setting up tests for your watchOS app](https://developer.apple.com/documentation/xctest/setting-up-tests-for-your-watchos-app) - Configure your watch-only project with unit tests and user interface tests.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/watchOS-Apps)*