# User Notifications UI

Customize the interface that displays local and remote notifications.

**Platforms:** iOS 10.0+ | iPadOS 10.0+ | Mac Catalyst 14.0+ | macOS 11.0+ | visionOS 1.0+

## Overview

Customize how local and remote notifications appear on the user's device by adding a notification content app extension to the bundle of your iOS app. Your extension manages a custom view controller, which you use to present the content from incoming notifications. When a notification arrives, the system displays your view controller in addition to, or in place of, the default system interface.

## Topics

### Notification Content App Extension
- [Customizing the Appearance of Notifications](https://developer.apple.com/documentation/usernotificationsui/customizing_the_appearance_of_notifications) - Customize the appearance of your iOS app's notification alerts with a notification content app extension.
- **UNNotificationContentExtension** - An object that presents a custom interface for a delivered local or remote notification.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/UserNotificationsUI)*