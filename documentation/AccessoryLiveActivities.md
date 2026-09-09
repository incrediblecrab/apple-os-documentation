# Accessory Live Activities

Reflect iPhone Live Activity updates and alerts on a paired accessory.

**Platforms:** iOS 26.5+; iPhone only

**Status:** Reviewed September 8, 2026. Developer testing is available in any region; customer use requires an iPhone in the EU and an Apple Account with an EU country or region. Broader SDK symbol listings do not override this runtime restriction.

## Overview

AccessoryLiveActivities adds Live Activity forwarding to the notification-forwarding extension model. Adopt [AccessoryNotifications](AccessoryNotifications.md) first, then extend the existing data provider to receive activity state and alerts.

The companion app requests authorization, but does not gain direct access to forwarded content. Data-provider and transport extensions handle that content within the system's secure forwarding path.

## Configuration and authorization

In the data-provider extension's `EXAppExtensionAttributes`, retain the `com.apple.accessory-data-provider` extension point and add `AccessoryLiveActivities.LiveActivityForwarding` to the `EXCapabilities` string array alongside `AccessoryNotifications.NotificationsForwarding`.

Authorization is **per physical accessory**. Check [`LiveActivityForwarding.authorization(forAccessory:)`](https://developer.apple.com/documentation/accessoryliveactivities/liveactivityforwarding/authorization(forAccessory:)) before claiming forwarding is active. The person may allow all apps, allow a subset, deny access, or change the choice later in Settings.

The initial notification-forwarding prompt covers both features. Use [`presentAuthorizationSheet(forAccessory:)`](https://developer.apple.com/documentation/accessoryliveactivities/liveactivityforwarding/presentAuthorizationSheet(forAccessory:)) when the person chooses to adjust Live Activity permissions; do not equate limited authorization with unrestricted access.

## Session and alert handling

Implement [`AccessoryLiveActivitiesHandler`](https://developer.apple.com/documentation/accessoryliveactivities/liveactivityforwarding/accessoryliveactivitieshandler). On activation, load the session's `liveActivities` snapshot; receive later changes through the update callbacks. Clear session references and accessory display state when the session is invalidated, and remove activities whose state is dismissed.

The return value from `activityUpdatedForAlert(_:)` affects whether iPhone displays the alert. Return `true` only after confirming that the accessory displayed it. If the accessory cannot confirm delivery, return `false` rather than suppressing the phone's alert.

Source-app icon URLs are ephemeral. Read their content when provided instead of persisting the URL as durable storage.

## Topics

- [Receiving Live Activity updates and alerts on an accessory](https://developer.apple.com/documentation/accessoryliveactivities/receiving-live-activities-on-an-accessory)
- [LiveActivityForwarding](https://developer.apple.com/documentation/accessoryliveactivities/liveactivityforwarding)
- [AccessoryAuthorizationResult](https://developer.apple.com/documentation/accessoryliveactivities/accessoryauthorizationresult)
- [AccessoryLiveActivity](https://developer.apple.com/documentation/accessoryliveactivities/accessoryliveactivity)
- [AccessoryTransportExtension](AccessoryTransportExtension.md)

## Sources

- [Apple framework reference](https://developer.apple.com/documentation/accessoryliveactivities)
- [Readable framework documentation](https://developer.apple.com/documentation/accessoryliveactivities.md)
- [Integration and permission requirements](https://developer.apple.com/documentation/accessoryliveactivities/receiving-live-activities-on-an-accessory.md)
