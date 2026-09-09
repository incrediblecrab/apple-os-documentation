# ClockKit

Display app-specific data on the clock face.

**Platforms:** watchOS 2.0+ (legacy complications); iOS/iPadOS/Mac Catalyst 14.0+ and watchOS 7.0+ (face-library declarations)

## Overview

**Legacy reference:** ClockKit-based complications are deprecated in watchOS 10 and later. Use [WidgetKit](WidgetKit.md) for new complications and follow [Migrating ClockKit complications to WidgetKit](https://developer.apple.com/documentation/widgetkit/converting-a-clockkit-app). The timeline/template discussion below describes existing ClockKit implementations, not new adoption guidance.

Existing ClockKit implementations supply dated timeline entries and templates for watch-face complications. The system selects the entry to display; the app supplies data for its supported complication families.

The watch face determines available positions and sizes. ClockKit groups them into families with templates for text, images, and gauges; there isn't one layout shared by every watch face.

The framework catalog currently labels watchOS 10, but `CLKComplication` and `CLKComplicationDataSource` declare watchOS 2. The complication workflow's watchOS 10 deprecation and the concrete `CLKComplication` declaration's watchOS 27 deprecation label are distinct source annotations, not runtime removal dates.

### Improve your app with complications

The following describes legacy ClockKit behavior. Use WidgetKit when adding new complications. An active complication can provide:

- Glanceable information on the watch face.
- A route into the app when tapped, optionally with a configured user activity.
- Additional opportunities for budgeted background refresh, not unrestricted execution.

When your app has a complication on the active watch face, watchOS tries to keep your watch app suspended in memory. The system can wake your app from the background quickly when the user wants to interact with it. ClockKit also wakes your app when the user taps your complication. If you use a user activity configuration, ClockKit passes the user activity to your app after waking it.

WidgetKit complications are available from watchOS 9. Once your WidgetKit extension begins supplying complications, the system disables that app's ClockKit complications and stops requesting their timelines. It may still call the ClockKit data source's migrator to map installed complications to WidgetKit replacements.

## Topics

### Migration Support
- [Migrating ClockKit complications to WidgetKit](https://developer.apple.com/documentation/widgetkit/converting-a-clockkit-app) - Leverage WidgetKit's API to create watchOS complications using SwiftUI.
- [`CLKComplicationDataSource`](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource) - The system-instantiated timeline data source, also used to provide a WidgetKit migrator.
- [`CLKDefaultComplicationIdentifier`](https://developer.apple.com/documentation/clockkit/clkdefaultcomplicationidentifier) - A watchOS 7+ fallback identifier when a specific identity isn't available; handle it with generic entries for the requested family.
- [`CLKComplicationDescriptor`](https://developer.apple.com/documentation/clockkit/clkcomplicationdescriptor) - A watchOS 7+ identifier and supported-family definition, allowing multiple complication choices per family.

### Face Sharing
- [Sharing an Apple Watch face](https://developer.apple.com/documentation/clockkit/sharing-an-apple-watch-face) - Share configured `.watchface` files; this doesn't create a new system watch-face design.
- [`CLKWatchFaceLibrary`](https://developer.apple.com/documentation/clockkit/clkwatchfacelibrary) - Imports existing face files. Adding faces has a compatible-device/pairing requirement; the declared iPadOS or Catalyst API doesn't make those devices watch-face hosts.

### Deprecated
- [Deprecated articles and symbols](https://developer.apple.com/documentation/clockkit/deprecated-articles-and-symbols) - The historical timeline, template, and complication API reference.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ClockKit)*
