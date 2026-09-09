# Notification Center

Create and manage widgets for the Today view.

**Historical framework baseline:** iOS 8.0+ | iPadOS 8.0+ | macOS 10.10+

The reviewed Today-widget APIs are deprecated from iOS/iPadOS/Mac Catalyst 14 and macOS 11. Their catalog assigns Catalyst introductions of 8 or 10; those inconsistent labels aren't usable Catalyst deployment targets.

> **Legacy Today-widget framework:** Use [WidgetKit](WidgetKit.md) for new widgets. This framework is unrelated to Foundation's [`NotificationCenter`](Foundation.md#concurrency-and-ui-integration), which broadcasts in-process notifications.

## Overview

This legacy extension model lets a widget and its containing app coordinate whether the widget has content to display. It also defines appearance/update callbacks and, on macOS, list and search controllers. These are historical Today-widget contracts, not the lifecycle or timeline APIs for modern WidgetKit widgets.

## Topics

### Core Widget
- [`NCWidgetProviding`](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding) - Appearance and update callbacks for Today widgets.
- [`NCWidgetController`](https://developer.apple.com/documentation/notificationcenter/ncwidgetcontroller) - Coordinates the widget-has-content flag; it isn't a general notification broadcaster and shouldn't be subclassed.

### Search View
- [`NCWidgetSearchViewController`](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewcontroller) - The macOS Today-widget search interface.
- [`NCWidgetSearchViewDelegate`](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewdelegate) - Performs the app-specific search and supplies the results.

### List View
- [`NCWidgetListViewController`](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller) - Displays content objects using views supplied by a delegate.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/NotificationCenter)*
