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

The system makes every attempt to deliver local and remote notifications in a timely manner, but delivery isn't guaranteed. The PushKit framework offers a more timely delivery mechanism for specific types of notifications, such as those VoIP and watchOS complications use. For more information, see PushKit.

For webpages in Safari version 16.0 and higher, generate remote notifications from a server that you manage using Push API code that works in Safari and other browsers.

**Note:** Siri can provide suggestions to users in search, News, Safari, and other apps using on-device information that your app contributes through the Notifications API. Users can change this functionality to allow at any time through Siri and Search settings for your app.

For design guidance, see Human Interface Guidelines > Notifications.

## Topics

### Essentials
- [User Notifications updates](https://developer.apple.com/documentation/usernotifications/user_notifications_updates) - Learn about important changes in User Notifications.
- [Asking permission to use notifications](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications) - Request permission to display alerts, play sounds, or badge the app's icon in response to a notification.

### Notification management
- **UNUserNotificationCenter** - The central object for managing notification-related activities for your app or app extension.
- **UNUserNotificationCenterDelegate** - An interface for processing incoming notifications and responding to notification actions.
- **UNNotificationSettings** - The object for managing notification-related settings and the authorization status of your app.

### Remote notifications
- [Generate notifications from your company's servers, and deliver those notifications using APNs](https://developer.apple.com/documentation/usernotifications/remote_notifications)
- [Setting up a remote notification server](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server) - Generate notifications and push them to user devices.
- [Sending push notifications using command-line tools](https://developer.apple.com/documentation/usernotifications/sending_push_notifications_using_command-line_tools) - Use basic macOS command-line tools to send push notifications to Apple Push Notification service (APNs).
- [Testing notifications using the Push Notification Console](https://developer.apple.com/documentation/usernotifications/testing_notifications_using_the_push_notification_console) - Send test notifications and access delivery logs to test your app's integration with Apple Push Notification service (APNs).

### Notification requests
- [Create delivery requests for local notifications, and access the content of delivered local and remote notifications](https://developer.apple.com/documentation/usernotifications/notification_requests)
- [Scheduling a notification locally from your app](https://developer.apple.com/documentation/usernotifications/scheduling_a_notification_locally_from_your_app) - Create and schedule notifications from your app when you want to get the user's attention.
- **UNNotificationRequest** - A request to schedule a local notification, which includes the content of the notification and the trigger conditions for delivery.
- **UNNotification** - The data for a local or remote notification the system delivers to your app.

### Push notifications in safari
- [Sending web push notifications in web apps and browsers](https://developer.apple.com/documentation/usernotifications/push_notifications_in_safari/sending_web_push_notifications_in_web_apps_and_browsers) - Update your web server and website to send push notifications that work in Safari, other browsers, and web apps, following cross-browser standards.

### Notification content
- [Modify and examine the payload of a notification](https://developer.apple.com/documentation/usernotifications/notification_content)
- [Implementing communication notifications](https://developer.apple.com/documentation/usernotifications/implementing_communication_notifications) - Configure and display your app's communication notifications by using intents.
- **UNNotificationContentProviding** - A protocol the system uses to provide context relevant to user notifications.
- **UNNotificationActionIcon** - An icon associated with an action.
- **UNMutableNotificationContent** - The editable content for a notification.
- **UNNotificationContent** - The uneditable content of a notification.
- **UNNotificationAttachment** - A media file associated with a notification.
- **UNNotificationSound** - The sound played upon delivery of a notification.
- **UNNotificationSoundName** - A string providing the name of a sound file.

### Triggers
- [Define the trigger conditions for delivering notifications. Detect when a remote notification was delivered from APNs](https://developer.apple.com/documentation/usernotifications/triggers)
- **UNCalendarNotificationTrigger** - A trigger condition that causes a notification the system delivers at a specific date and time.
- **UNTimeIntervalNotificationTrigger** - A trigger condition that causes the system to deliver a notification after the amount of time you specify elapses.
- **UNLocationNotificationTrigger** - A trigger condition that causes the system to deliver a notification when the user's device enters or exits a geographic region you specify.
- **UNPushNotificationTrigger** - A trigger condition that indicates Apple Push Notification Service (APNs) has sent the notification.
- **UNNotificationTrigger** - The common behavior for subclasses that trigger the delivery of a local or remote notification.

### Notification categories and user actions
- [Define the types of notifications that your app supports, and define how users can respond](https://developer.apple.com/documentation/usernotifications/notification_categories_and_user_actions)
- [Declaring your actionable notification types](https://developer.apple.com/documentation/usernotifications/declaring_your_actionable_notification_types) - Differentiate your notifications and add action buttons to the notification interface.
- **UNNotificationCategory** - A type of notification your app supports and the custom actions that the system displays.
- **UNNotificationAction** - A task your app performs in response to a notification that the system delivers.
- **UNTextInputNotificationAction** - An action that accepts user-typed text.

### Notification responses
- [Handling notifications and notification-related actions](https://developer.apple.com/documentation/usernotifications/handling_notifications_and_notification-related_actions) - Respond to user interactions with the system's notification interfaces, including handling your app's custom actions.
- **UNNotificationResponse** - The user's response to an actionable notification.
- **UNTextInputNotificationResponse** - The user's response to an actionable notification, including any custom text that the user typed or dictated.

### Notification service app extension
- [Use a notification service app extension to modify the content of a notification before it's delivered to your app](https://developer.apple.com/documentation/usernotifications/notification_service_app_extension)
- [Modifying content in newly delivered notifications](https://developer.apple.com/documentation/usernotifications/modifying_content_in_newly_delivered_notifications) - Modify the payload of a remote notification before it's displayed on the user's iOS device.
- **UNNotificationServiceExtension** - An object that modifies the content of a remote notification before it's delivered to the user.

### Entitlements
- [APS Environment Entitlement](https://developer.apple.com/documentation/usernotifications/aps_environment_entitlement) - The environment for push notifications.
- [APS Environment (macOS) Entitlement](https://developer.apple.com/documentation/usernotifications/aps_environment_macos_entitlement) - The environment for push notifications in macOS apps.

### Sample code
- [Handling Communication Notifications and Focus Status Updates](https://developer.apple.com/documentation/usernotifications/handling_communication_notifications_and_focus_status_updates) - Create a richer calling and messaging experience in your app by implementing communication notifications and Focus status updates.
- [Implementing Alert Push Notifications](https://developer.apple.com/documentation/usernotifications/implementing_alert_push_notifications) - Add visible alert notifications to your app by using the UserNotifications framework.
- [Implementing Background Push Notifications](https://developer.apple.com/documentation/usernotifications/implementing_background_push_notifications) - Add background notifications to your app by using the UserNotifications framework.

### Reference
- [UserNotifications Constants](https://developer.apple.com/documentation/usernotifications/usernotifications_constants)
- **UNNotificationAttributedMessageContext**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/UserNotifications)*