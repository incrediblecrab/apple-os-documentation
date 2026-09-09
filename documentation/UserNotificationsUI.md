# User Notifications UI

Customize the interface that displays local and remote notifications.

**Documented extension workflow:** iOS 10.0+ | iPadOS 10.0+

The framework catalog also lists Mac Catalyst 14+, macOS 11+, and visionOS 1+, while the content-extension guide explicitly scopes its workflow to iOS apps and the protocol metadata even lists Catalyst 10. These sources don't establish uniform extension-hosting support across the catalog platforms; don't treat those aggregate labels as a portable notification-UI recipe.

## Overview

Add a notification content app extension to customize the expanded interface for notifications in its supported categories. Adopt `UNNotificationContentExtension` in the extension's view controller and populate it from the delivered notification. The system still owns the abbreviated banner; the extension supplements or replaces the full interface when the person expands it.

Build the interface promptly from the payload and already available resources rather than blocking presentation on a network request. A [notification service extension](UserNotifications.md#notification-service-app-extension) serves a different purpose: modifying a remote payload before delivery.

## Topics

### Notification Content App Extension
- [Customizing the Appearance of Notifications](https://developer.apple.com/documentation/usernotificationsui/customizing-the-appearance-of-notifications) - Configure categories and the expanded notification interface.
- [`UNNotificationContentExtension`](https://developer.apple.com/documentation/usernotificationsui/unnotificationcontentextension) - The protocol adopted by the extension's custom view controller.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/UserNotificationsUI)*
