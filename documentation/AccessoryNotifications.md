# Accessory Notifications

Forward selected iPhone notifications securely to a companion accessory.

**Platforms:** iOS 26.5+; iPhone only

**Status:** Reviewed September 8, 2026. Developer testing is available in any region; customer use requires an iPhone located in the EU and an Apple Account with an EU country or region.

## Overview

AccessoryNotifications lets a companion app request notification forwarding for a paired accessory. People decide which apps may forward notifications. The system then delivers content to extensions that curate and securely transmit it to the accessory.

The companion app's authorization UI is not a general API for reading other apps' notifications. Content handling belongs in the extension architecture provided by [AccessoryTransportExtension](AccessoryTransportExtension.md), with separate data-provider, security, and transport responsibilities.

## Authorization and revocation

Pair the accessory using [AccessorySetupKit](AccessorySetupKit.md), then call [`requestForwarding(for:)`](https://developer.apple.com/documentation/accessorynotifications/accessorynotificationcenter/requestForwarding(for:)).

[`ForwardingDecision`](https://developer.apple.com/documentation/accessorynotifications/forwardingdecision) distinguishes `.allow`, `.limited`, `.deny`, and `.undetermined`. Limited access covers only the person's selected apps. Dismissal without a decision does not authorize forwarding.

Query [`forwardingStatus(for:)`](https://developer.apple.com/documentation/accessorynotifications/accessorynotificationcenter/forwardingStatus(for:)) instead of treating the initial choice as permanent. Offer the system's settings presentation when the person wants to change it. Handle denial, changed scope, removed notifications, and invalidated sessions without continuing to display stale content.

## Delivery and responses

Implement [`NotificationsForwarding.AccessoryNotificationsHandler`](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler) in the data-provider extension. Select only the fields needed by the accessory from `AccessoryNotification`.

Use `AlertingContext` to coordinate alerts. A successful transfer alone is not proof that the accessory alerted the person; return a successful alert result only when appropriate. Handle accessory disconnection and transmission failures so the system can still coordinate delivery.

For interactions such as a reply or dismissal, use [`NotificationResponse`](https://developer.apple.com/documentation/accessorynotifications/notificationresponse) and the forwarding session rather than fabricating an independent action in the source app.

## Topics

- [AccessoryNotificationCenter](https://developer.apple.com/documentation/accessorynotifications/accessorynotificationcenter) — Authorization and settings.
- [AccessoryNotification](https://developer.apple.com/documentation/accessorynotifications/accessorynotification) — Forwarded notification data.
- [AlertingContext](https://developer.apple.com/documentation/accessorynotifications/alertingcontext) — Alert coordination.
- [Responding to forwarded notifications](https://developer.apple.com/documentation/accessorynotifications/responding-to-forwarded-notifications)
- [Receiving iOS notifications on an accessory](https://developer.apple.com/documentation/accessorytransportextension/receiving-ios-notifications-on-an-accessory) — Required extension configuration and entitlements.
- [Accessory Live Activities](AccessoryLiveActivities.md) — The related, separately authorized forwarding feature.

## Sources

- [Apple framework reference](https://developer.apple.com/documentation/accessorynotifications)
- [Readable framework documentation](https://developer.apple.com/documentation/accessorynotifications.md)
- [Forwarding decisions](https://developer.apple.com/documentation/accessorynotifications/forwardingdecision.md)
