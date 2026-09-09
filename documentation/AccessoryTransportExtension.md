# Accessory Transport Extension

Separate accessory content processing, key exchange, and transport.

**Platforms:** iOS/iPadOS 26.2+ SDK; individual features have narrower requirements

**Status:** Reviewed September 8, 2026. Calls are ignored for Mac Catalyst and for iOS apps running on visionOS or Apple silicon Macs. Developer testing is region-independent; customer use requires a device in the EU and an Apple Account with an EU country or region.

## Overview

AccessoryTransportExtension provides extensions for moving system-provided information to an accessory paired through [AccessorySetupKit](AccessorySetupKit.md). [Wi-Fi Infrastructure](WiFiInfrastructure.md) uses the transport extension to deliver shared networks. [Accessory Notifications](AccessoryNotifications.md) and [Accessory Live Activities](AccessoryLiveActivities.md) use a more compartmentalized forwarding path.

Importing the transport framework does not authorize all these features. Each feature retains its own permission, platform, and minimum-version requirements; notification and Live Activity forwarding are iPhone-only.

## Extension responsibilities

| Component | Responsibility |
| --- | --- |
| `AccessoryDataProvider` | Receives permitted notification/activity content and selects data appropriate for the accessory. |
| `AccessoryTransportSecurity` | Coordinates cryptographic key exchange with the accessory. |
| `AccessoryTransportAppExtension` | Carries transport messages to the accessory; forwarded notification content reaches it encrypted. |

For notification forwarding, configure the data provider with extension point `com.apple.accessory-data-provider` and capability `AccessoryNotifications.NotificationsForwarding` in the `EXCapabilities` string array. Its entitlement is `com.apple.developer.accessory-data-provider`. The security extension uses extension point `com.apple.accessory-transport-security` and entitlement `com.apple.developer.accessory-transport-security`.

The transport target separately needs `com.apple.developer.accessory-transport-extension`. All three entitlements are Boolean and must be `true` in the corresponding extension's signature. The transport entitlement starts at 26.2; the data-provider and security entitlements start at 26.5. Follow Apple's integration article for the complete target configuration rather than reusing one extension's privileges across all targets.

## Security and failure boundaries

The system encrypts curated notification content so the transport extension cannot read it. The accessory participates in the documented HPKE key-exchange workflow. Apple's integration guide requires XWing when using the internet or local-network transports; do not substitute a custom plaintext channel.

Accept only supported session requests, implement session invalidation, and discard obsolete session state. Respect the associated feature's current authorization and stop forwarding when access ends. A Bluetooth connection or successful pairing alone is not permission to forward notifications or disclose network credentials.

Design for disconnected accessories, rejected requests, key-exchange failures, and failed transmissions. Report completion accurately; do not claim an alert was shown merely because a message was queued.

Call message completion handlers on failure as well as success. The integration guide warns that omitting a key-exchange completion handler makes the system assume successful delivery.

## Topics

- [AccessoryTransportAppExtension](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportappextension)
- [AccessoryTransportSession](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession)
- [AccessoryDataProvider](https://developer.apple.com/documentation/accessorytransportextension/accessorydataprovider)
- [AccessoryTransportSecurity](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsecurity)
- [AccessorySecuritySession](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession)
- [Receiving iOS notifications on an accessory](https://developer.apple.com/documentation/accessorytransportextension/receiving-ios-notifications-on-an-accessory)

## Sources

- [Apple framework reference](https://developer.apple.com/documentation/accessorytransportextension)
- [Runtime and regional restrictions](https://developer.apple.com/documentation/accessorytransportextension.md)
- [Extension and transport-security integration](https://developer.apple.com/documentation/accessorytransportextension/receiving-ios-notifications-on-an-accessory.md)
