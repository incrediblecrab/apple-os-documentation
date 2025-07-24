# ClockKit

Display app-specific data on the clock face.

**Platforms:** iOS 14.0+ | iPadOS 14.0+ | Mac Catalyst 14.0+ | watchOS 10.0+

## Overview

Important: ClockKit-based complications are deprecated in watchOS 10 and later. Use WidgetKit to create complications. For more information, see Migrating to WidgetKit.

Use the ClockKit framework to implement complications for your app. Complications are small interface elements that appear on a watch face and provide quick access to data that people frequently use. Your app defines complications using timeline entries that provide a template for the complication's appearance and the date ClockKit displays it. The system updates the appearance of your complication based on the timeline.

ClockKit defines the size and placement of the complications on each watch face. The following image depicts the layout of the Modular watch face, which has space for five different complications: one large and four small.

ClockKit organizes complications into families based on their size and style, and provides a variety of templates for each family. Use the templates to display text, images, and graphical gauges.

### Improve your app with complications

Complications provide a unique way to interact with your users. Consider creating complications, even if they only act as a launcher for your watchOS app. A complication on the active watch face provides:

- Vital information when the user glances at their watch.
- A rapid launch of your app to a specific screen when the user taps on the complications.
- The ability to perform background tasks, keeping your complication and app up to date.

When your app has a complication on the active watch face, watchOS tries to keep your watch app suspended in memory. The system can wake your app from the background quickly when the user wants to interact with it. ClockKit also wakes your app when the user taps your complication. If you use a user activity configuration, ClockKit passes the user activity to your app after waking it.

The system also gives apps with active complications more opportunities for background refresh tasks. You can use these tasks to keep the content of your watchOS app and your complications up to date and accurate.

## Topics

### Migration Support
- [Migrating ClockKit complications to WidgetKit](https://developer.apple.com/documentation/ClockKit/migrating_clockkit_complications_to_widgetkit) - Leverage WidgetKit's API to create watchOS complications using SwiftUI.
- **CLKComplicationDataSource** - A protocol that provides ClockKit with information about your complication.
- **CLKDefaultComplicationIdentifier** - An identifier representing a default complication.
- **CLKComplicationDescriptor** - A descriptor that defines a complication and the families that it supports.

### Face Sharing
- [Sharing an Apple Watch face](https://developer.apple.com/documentation/ClockKit/sharing_an_apple_watch_face) - Distribute a customized watch face to Apple Watch users.
- **CLKWatchFaceLibrary** - An object for importing watch faces that the app provides.

### Deprecated
- **Deprecated articles and symbols**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ClockKit)*