# App Store Server Notifications

Monitor In-App Purchase events in real time and learn of unreported external purchase tokens, with server notifications from the App Store.

**Availability:** Server-to-server service with production and sandbox environments. Use version 2; version 1 is formally deprecated. Service changes are not tied to an OS 27 deployment minimum.

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

For regional reporting and distribution requirements, see [Regional distribution](../guides/regional-distribution.md) and the applicable [External Purchase Server API](ExternalPurchaseServerAPI.md) documentation.

### Test your server setup

To determine whether your server is receiving notifications, call the Request a Test Notification endpoint in the App Store Server API to ask the App Store server to send a notification with the notificationType TEST. Use the testNotificationToken you receive to call the Get Test Notification Status endpoint to learn how your server responds to the test notification.

The App Store server sends the TEST notification in the version 2 notification format, however, it sends it to your server regardless of whether you configure a version 1 or version 2 notification URL in App Store Connect. For more information about configuring your URL in App Store Connect, see Enter a URL for App Store server notifications.

## Current service changes and reliable processing

Reviewed September 8, 2026 against the service's own changelog:

- The April 27, 2026 update adds transaction and renewal commitment information and billing-plan fields for monthly subscriptions with a 12-month commitment.
- Earlier updates add `revocationType`/`revocationPercentage`, `RESCIND_CONSENT` with `appData`, and additional external-purchase-token subtypes. Preserve support for these documented payload variants; not every notification contains the same transaction data.
- OS 27 StoreKit volume assignments and subscription Bundles/Suites are separate SDK changes. Do not invent matching notification names or assume the REST service shares the SDK's version number.

Verify the outer `signedPayload` and any nested signed transaction/renewal data before updating entitlements. Make processing idempotent and reconcile current state with [App Store Server API](AppStoreServerAPI.md), especially after delayed or repeated delivery.

Return HTTP **200–206** after successful processing or durable acceptance. Apple's [response contract](https://developer.apple.com/documentation/appstoreservernotifications/responding-to-app-store-server-notifications) treats other codes as unsuccessful. Production V2 retries occur five times, at 1, 12, 24, 48, and 72 hours after the preceding attempt; **sandbox sends only once**. Do not use sandbox behavior to infer production retry coverage.

After an outage, use [Get Notification History](https://developer.apple.com/documentation/appstoreserverapi/get-notification-history), transaction history, and subscription status to reconcile missing work. A successful `TEST` notification establishes delivery, not the correctness of fulfillment or signature-verification logic.

## Topics

### Essentials
- [Enabling App Store Server Notifications](https://developer.apple.com/documentation/appstoreservernotifications/enabling-app-store-server-notifications) - Configure your server and provide an HTTPS URL to receive notifications about in-app purchase events and unreported external purchase tokens.
- [Receiving App Store Server Notifications](https://developer.apple.com/documentation/appstoreservernotifications/receiving-app-store-server-notifications) - Implement server-side code to receive and parse notification posts.
- [Responding to App Store Server Notifications](https://developer.apple.com/documentation/appstoreservernotifications/responding-to-app-store-server-notifications) - Send HTTP status codes to indicate the success of a notification post.
- [App Store Server Notifications changelog](https://developer.apple.com/documentation/appstoreservernotifications/app-store-server-notifications-changelog) - Learn about changes to the App Store Server Notifications service.

### Server notifications version 2
- [App Store Server Notifications V2](https://developer.apple.com/documentation/appstoreservernotifications/app-store-server-notifications-v2) - Specify your secure server's URL in App Store Connect to receive version 2 notifications.
- **responseBodyV2** - The response body the App Store sends in a version 2 server notification.
- **responseBodyV2DecodedPayload** - A decoded payload that contains the version 2 notification data.
- **notificationType** - The type that describes the in-app purchase or external purchase event for which the App Store sends the version 2 notification.
- **subtype** - A string that provides details about select notification types in version 2.

### Deprecated
- [App Store Server Notifications Version 1](https://developer.apple.com/documentation/appstoreservernotifications/app-store-server-notifications-version-1) - Legacy documentation for the deprecated format; deprecation is not an announcement of removal.

## See Also

### Related Documentation
- **In-App Purchase** - Offer content and services in your app across Apple platforms using a Swift-based interface.
- **App Store Server API** - Manage your customers' App Store transactions from your server.
- **App Store Receipts** - Validate app and In-App Purchase receipts with the App Store. (Deprecated)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AppStoreServerNotifications)*
