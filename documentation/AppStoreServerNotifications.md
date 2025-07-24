# App Store Server Notifications

Monitor In-App Purchase events in real time and learn of unreported external purchase tokens, with server notifications from the App Store.

**Platforms:** App Store Server Notifications 1.0+

## Overview

App Store Server Notifications is a server-to-server service that sends real-time notifications for In-App Purchase events, and notifications for unreported external purchase tokens. Use the data in the notifications to update your user-account database, and to monitor and respond to in-app purchase refunds. For notifications related to the External Purchase API, see externalPurchaseToken.

Important: The App Store Server Notifications V1 endpoint and version 1 notifications, notification_type, are deprecated. Implement the App Store Server Notifications V2 endpoint on your server to receive version 2 notifications instead.

To receive server notifications from the App Store, provide your server's HTTPS URL in App Store Connect. Opt in to receive notifications for the production environment and the sandbox environment. For more information, see Enabling App Store Server Notifications.

Your server is responsible for parsing, interpreting, and responding to all server-to-server notification posts. For more information, see Receiving App Store Server Notifications and Responding to App Store Server Notifications.

### Process in-app purchase notifications

Notifications cover events in the in-app purchase life cycle, including purchases, subscription renewals, offer redemptions, refunds, and more. For a complete list of notification types, see notificationType for App Store Server Notifications V2.

Use the notification type, along with the transaction and subscription renewal information, to update a customer's service or to present promotional offers according to your business logic.

### Process external purchase token notifications

A notificationType of EXTERNAL_PURCHASE_TOKEN with an UNREPORTED subtype indicates that Apple generated an external purchase token for your app but hasn't received a report for the token. The notification includes the token in the externalPurchaseToken field of the responseBodyV2DecodedPayload. Use the token information to report it to Apple, including if you don't recognize the token in your system. To report tokens, with or without associated transactions, call the External Purchase Server API's Send External Purchase Report endpoint.

For more information about token reporting requirements, see Using alternative payment options on the App Store in the European Union.

### Test your server setup

To determine whether your server is receiving notifications, call the Request a Test Notification endpoint in the App Store Server API to ask the App Store server to send a notification with the notificationType TEST. Use the testNotificationToken you receive to call the Get Test Notification Status endpoint to learn how your server responds to the test notification.

The App Store server sends the TEST notification in the version 2 notification format, however, it sends it to your server regardless of whether you configure a version 1 or version 2 notification URL in App Store Connect. For more information about configuring your URL in App Store Connect, see Enter a URL for App Store server notifications.

## Topics

### Essentials
- [Enabling App Store Server Notifications](https://developer.apple.com/documentation/AppStoreServerNotifications/enabling_app_store_server_notifications) - Configure your server and provide an HTTPS URL to receive notifications about in-app purchase events and unreported external purchase tokens.
- [Receiving App Store Server Notifications](https://developer.apple.com/documentation/AppStoreServerNotifications/receiving_app_store_server_notifications) - Implement server-side code to receive and parse notification posts.
- [Responding to App Store Server Notifications](https://developer.apple.com/documentation/AppStoreServerNotifications/responding_to_app_store_server_notifications) - Send HTTP status codes to indicate the success of a notification post.
- [App Store Server Notifications changelog](https://developer.apple.com/documentation/AppStoreServerNotifications/app_store_server_notifications_changelog) - Learn about changes to the App Store Server Notifications service.

### Server notifications version 2
- [App Store Server Notifications V2](https://developer.apple.com/documentation/AppStoreServerNotifications/app_store_server_notifications_v2) - Specify your secure server's URL in App Store Connect to receive version 2 notifications.
- **responseBodyV2** - The response body the App Store sends in a version 2 server notification.
- **responseBodyV2DecodedPayload** - A decoded payload that contains the version 2 notification data.
- **notificationType** - The type that describes the in-app purchase or external purchase event for which the App Store sends the version 2 notification.
- **subtype** - A string that provides details about select notification types in version 2.

### Deprecated
- [App Store Server Notifications Version 1](https://developer.apple.com/documentation/AppStoreServerNotifications/app_store_server_notifications_version_1) - Receive, parse, and interpret App Store Server Notifications version 1.

## See Also

### Related Documentation
- **In-App Purchase** - Offer content and services in your app across Apple platforms using a Swift-based interface.
- **App Store Server API** - Manage your customers' App Store transactions from your server.
- **App Store Receipts** - Validate app and In-App Purchase receipts with the App Store. (Deprecated)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AppStoreServerNotifications)*