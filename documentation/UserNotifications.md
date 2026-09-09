# User Notifications

Push user-facing notifications to the user's device from a server, or generate them locally from your app.

**Platforms:** iOS 10.0+ | iPadOS 10.0+ | Mac Catalyst 13.0+ | macOS 10.14+ | tvOS 10.0+ | visionOS 1.0+ | watchOS 3.0+

## Overview

User-facing notifications communicate important information to users of your app, regardless of whether your app is running on the user's device. For example, a sports app can let the user know when their favorite team scores. Notifications can also tell your app to download information and update its interface. Notifications can display an alert, play a sound, or badge the app's icon.

You can generate notifications locally from your app or remotely from a server that you manage. For local notifications, the app creates the notification content and specifies a condition, like a time or location, that triggers the delivery of the notification. For remote notifications, your company's server generates push notifications, and Apple Push Notification service (APNs) handles the delivery of those notifications to the user's devices.

Use this framework to do the following:

- Define the types of notifications that your app supports.
- Define any custom actions associated with your notification types.
- Schedule local notifications for delivery.
- Process already delivered notifications.
- Respond to user-selected actions.

Delivery isn't guaranteed. [PushKit](PushKit.md) has separate, specialized workflows, such as VoIP and supported complication updates; it isn't a general way to bypass notification authorization, delivery limits, or scheduling budgets.

Web push is a separate standards-based path using the Push, Notifications, and Service Worker APIs. Safari 16.1 added it on macOS Ventura; iOS/iPadOS 16.4 added support for Home Screen web apps. Browser version alone doesn't establish host or ordinary-tab support. See [Sending web push notifications](https://developer.apple.com/documentation/usernotifications/sending-web-push-notifications-in-web-apps-and-browsers).

**Note:** The system may use on-device notification information for Siri-related suggestions, subject to the person's settings. This isn't an app-controlled suggestion or delivery guarantee; settings labels vary by OS.

For design guidance, see the [Notifications HIG](https://developer.apple.com/design/human-interface-guidelines/notifications).

## Update channels and OS 27 testing

Keep ordinary notifications, [ActivityKit](ActivityKit.md) Live Activities, and [WidgetKit push updates](WidgetKit.md#api-and-os-27-migration-checks) distinct. They use different registration/update contracts; widget pushes remain budgeted requests for timeline reloads. A system notification-grouping change does not grant additional app authorization or delivery guarantees.

The [iOS & iPadOS 27 beta notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes) mark critical alerts being automatically enabled for any app requesting notification permission as **resolved** (179179362). Do not rely on that earlier-beta behavior: check current notification settings and test authorization on clean and upgraded installations. See [UserNotificationsUI](UserNotificationsUI.md) for content extensions and [SafariServices](SafariServices.md) for the separate browser/extension context.

## Topics

### Essentials
- [User Notifications updates](https://developer.apple.com/documentation/updates/usernotifications) - Learn about important changes in User Notifications.
- [Asking permission to use notifications](https://developer.apple.com/documentation/usernotifications/asking-permission-to-use-notifications) - Request permission to display alerts, play sounds, or badge the app's icon in response to a notification.

### Notification management
- **UNUserNotificationCenter** - The central object for managing notification-related activities for your app or app extension.
- **UNUserNotificationCenterDelegate** - An interface for processing incoming notifications and responding to notification actions.
- [`UNNotificationSettings`](https://developer.apple.com/documentation/usernotifications/unnotificationsettings) - The current settings and authorization status you read to adapt app behavior, not an object for changing the person's settings.

### Remote notifications
Generate server notifications and deliver them using APNs.

- [Setting up a remote notification server](https://developer.apple.com/documentation/usernotifications/setting-up-a-remote-notification-server) - Generate notifications and push them to user devices.
- [Sending push notifications using command-line tools](https://developer.apple.com/documentation/usernotifications/sending-push-notifications-using-command-line-tools) - Use basic macOS command-line tools to send push notifications to Apple Push Notification service (APNs).
- [Testing notifications using the Push Notification Console](https://developer.apple.com/documentation/usernotifications/testing-notifications-using-the-push-notification-console) - Send test notifications and access delivery logs to test your app's integration with Apple Push Notification service (APNs).

### Notification requests
Create local delivery requests and inspect delivered notifications.

- [Scheduling a notification locally from your app](https://developer.apple.com/documentation/usernotifications/scheduling-a-notification-locally-from-your-app) - Create and schedule notifications from your app when you want to get the user's attention.
- **UNNotificationRequest** - A request to schedule a local notification, which includes the content of the notification and the trigger conditions for delivery.
- **UNNotification** - The data for a local or remote notification the system delivers to your app.

### Push notifications in safari
- [Sending web push notifications in web apps and browsers](https://developer.apple.com/documentation/usernotifications/sending-web-push-notifications-in-web-apps-and-browsers) - Update your web server and website to send push notifications that work in Safari, other browsers, and web apps, following cross-browser standards.

### Notification content
Modify and examine notification payloads.

- [Implementing communication notifications](https://developer.apple.com/documentation/usernotifications/implementing-communication-notifications) - Configure and display your app's communication notifications by using intents.
- **UNNotificationContentProviding** - A protocol the system uses to provide context relevant to user notifications.
- **UNNotificationActionIcon** - An icon associated with an action.
- **UNMutableNotificationContent** - The editable content for a notification.
- **UNNotificationContent** - The uneditable content of a notification.
- **UNNotificationAttachment** - A media file associated with a notification.
- **UNNotificationSound** - The sound played upon delivery of a notification.
- **UNNotificationSoundName** - A string providing the name of a sound file.

### Triggers
Define local trigger conditions or identify APNs-delivered notifications.

- **UNCalendarNotificationTrigger** - A trigger condition that causes a notification the system delivers at a specific date and time.
- **UNTimeIntervalNotificationTrigger** - A trigger condition that causes the system to deliver a notification after the amount of time you specify elapses.
- **UNLocationNotificationTrigger** - A trigger condition that causes the system to deliver a notification when the user's device enters or exits a geographic region you specify.
- **UNPushNotificationTrigger** - A trigger condition that indicates Apple Push Notification Service (APNs) has sent the notification.
- **UNNotificationTrigger** - The common behavior for subclasses that trigger the delivery of a local or remote notification.

### Notification categories and user actions
Define notification types and the actions people can perform.

- [Declaring your actionable notification types](https://developer.apple.com/documentation/usernotifications/declaring-your-actionable-notification-types) - Differentiate your notifications and add action buttons to the notification interface.
- **UNNotificationCategory** - A type of notification your app supports and the custom actions that the system displays.
- **UNNotificationAction** - A task your app performs in response to a notification that the system delivers.
- **UNTextInputNotificationAction** - An action that accepts user-typed text.

### Notification responses
- [Handling notifications and notification-related actions](https://developer.apple.com/documentation/usernotifications/handling-notifications-and-notification-related-actions) - Respond to user interactions with the system's notification interfaces, including handling your app's custom actions.
- **UNNotificationResponse** - The user's response to an actionable notification.
- **UNTextInputNotificationResponse** - The user's response to an actionable notification, including any custom text that the user typed or dictated.

### Notification service app extension
Modify supported remote notification content before presentation.

- [Modifying content in newly delivered notifications](https://developer.apple.com/documentation/usernotifications/modifying-content-in-newly-delivered-notifications) - Modify the payload of a remote notification before it's displayed on the user's iOS device.
- **UNNotificationServiceExtension** - An object that modifies the content of a remote notification before it's delivered to the user.

### Entitlements
- [APS Environment Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/aps-environment) - The environment for push notifications.
- [APS Environment (macOS) Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.aps-environment) - The environment for push notifications in macOS apps.

### Sample code
- [Handling Communication Notifications and Focus Status Updates](https://developer.apple.com/documentation/usernotifications/handling-communication-notifications-and-focus-status-updates) - Create a richer calling and messaging experience in your app by implementing communication notifications and Focus status updates.
- [Implementing Alert Push Notifications](https://developer.apple.com/documentation/usernotifications/implementing-alert-push-notifications) - Add visible alert notifications to your app by using the UserNotifications framework.
- [Implementing Background Push Notifications](https://developer.apple.com/documentation/usernotifications/implementing-background-push-notifications) - Add background notifications to your app by using the UserNotifications framework.

### Reference
- [`UNNotificationDefaultActionIdentifier`](https://developer.apple.com/documentation/usernotifications/unnotificationdefaultactionidentifier) and [`UNNotificationDismissActionIdentifier`](https://developer.apple.com/documentation/usernotifications/unnotificationdismissactionidentifier) identify the default and dismissal responses.
- [`UNNotificationAttributedMessageContext`](https://developer.apple.com/documentation/usernotifications/unnotificationattributedmessagecontext) - A class conforming to `UNNotificationContentProviding`; iOS/iPadOS/Mac Catalyst 18+, macOS 15+, visionOS 2+, and watchOS 11+.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/UserNotifications)*
