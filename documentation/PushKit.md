# PushKit

Respond to push notifications related to your app's complications, file providers, and VoIP services.

**Platforms:** iOS 8.0+ | iPadOS 8.0+ | Mac Catalyst 13.0+ | macOS 10.15+ | visionOS 1.0+ | watchOS 6.0+

## Overview

The PushKit framework supports specialized notifications for updating your watchOS complications, responding to file provider changes, and receiving incoming Voice-over-IP (VoIP) calls. PushKit notifications differ from the ones you handle with the User Notifications framework. Instead of displaying an alert, badging your app's icon, or playing a sound, PushKit notifications wake up or launch your app and give it time to respond. Both PushKit and User Notifications use the Apple Push Notification service (APNs) to deliver push notifications to user devices.

To receive PushKit notifications, your app creates a PKPushRegistry object and uses it to configure the notification types it supports. When registration is successful, PushKit delivers a unique data token to your app that contains the identity of the current device and the push type. Forward that token along to the server, and include it in any notifications you send to the user. APNs uses the token to deliver the correct type of notification to the user's device.

For information about how to configure your server to work with APNs, see [Setting up a remote notification server](https://developer.apple.com/documentation/usernotifications/setting-up-a-remote-notification-server).

**Note:** PushKit doesn't support some special use cases in which access to Apple Push Notification service (APNs) isn't possible. For information about when you might need to support these cases, see iOS 10 and the Legacy VoIP Architecture.

### Type-specific delivery and VoIP reporting

The framework's platform list does not mean every push type is available on every platform. [`complication`](https://developer.apple.com/documentation/pushkit/pkpushtype/complication) sends updates directly to Apple Watch on watchOS 6 and later; its iOS companion use is deprecated from iOS 13. Complication delivery requires an active complication on the current clock face and is limited to **50 pushes per day**. [`fileProvider`](https://developer.apple.com/documentation/pushkit/pkpushtype/fileprovider) updates File Provider extension content.

VoIP pushes are for incoming calls, not general background work. The older [VoIP handling guide](https://developer.apple.com/documentation/pushkit/responding-to-voip-notifications-from-pushkit) describes the CallKit requirement for apps linked against the iOS 13 SDK or later. The [26.4 VoIP delegate method](https://developer.apple.com/documentation/pushkit/pkpushregistrydelegate/pushregistry(_:didreceiveincomingvoippushwith:metadata:withcompletionhandler:)) has a more specific contract: inspect the supplied `mustReport` metadata and report a required incoming call/conversation through **CallKit or LiveCommunicationKit**.

When `mustReport` is false, that callback does not require reporting a call. Do not infer the value from your own foreground-state check. Failing to report when required can terminate the app and eventually stop VoIP delivery. Complete notification processing and handle report errors; reporting a call does not guarantee that its UI appears, for example when Do Not Disturb intervenes.

## Topics

### Registration

- [Supporting PushKit Notifications in Your App](https://developer.apple.com/documentation/pushkit/supporting-pushkit-notifications-in-your-app) - Declare the types of PushKit notifications your app supports and configure objects to respond to them.
- **PKPushRegistry** - An object that requests the delivery and handles the receipt of PushKit notifications.
- **PKPushRegistryDelegate** - The methods that you use to handle incoming PushKit notifications and registration events.
- **PKPushCredentials** - An object that encapsulates the device token you use to deliver push notifications to your app.

### Push Types

- [Responding to VoIP Notifications from PushKit](https://developer.apple.com/documentation/pushkit/responding-to-voip-notifications-from-pushkit) - Receive incoming Voice-over-IP (VoIP) push notifications and use them to display the system call interface to the user.
- **PKPushType** - Constants reflecting the push types you want to support.

### Payload

- **PKPushPayload** - An object that contains information about a received PushKit notification.

### Data export

- [Exporting delivery metrics logs](https://developer.apple.com/documentation/pushkit/exporting-delivery-metrics-logs) - Download and analyze push-notification metrics.
- [Exporting broadcast push notification metrics](https://developer.apple.com/documentation/pushkit/exporting-broadcast-push-notification-metrics) - Discover how many people subscribe to your broadcast channels, and how many messages they receive.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/PushKit)*
