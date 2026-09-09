# EventKit UI

Present system interfaces for calendar events and calendar selection.

**Platforms:** iOS 4.0+ | iPadOS 4.0+ | Mac Catalyst 13.0+ | visionOS 1.0+

## Overview

EventKitUI provides event viewers, editors, and calendar choosers. The event controllers work with `EKEvent`, not `EKReminder`; choosing a reminder calendar doesn't make them reminder-editing controllers.

The view controllers you'll use on iOS are:

- **EKEventViewController**, for displaying existing events.
- **EKEventEditViewController**, for creating, editing, or deleting events.
- **EKCalendarChooser**, for selecting one or more calendars. Its display style filters all calendars versus writable calendars; it doesn't change their permissions. Its entity-type initializer can choose event or reminder calendars.

Present the editor modally; the calendar chooser can also be pushed on a navigation stack. Handle delegate callbacks and dismiss the event interface yourself when the interaction completes.

On iOS 17+, the system hosts chooser/editor UI outside your app's process, allowing event creation with `EKEventEditViewController` without requesting write-only or full calendar access. This doesn't grant your app direct access to the calendar database.

For direct event/reminder data access, use [EventKit](EventKit.md) and follow [Accessing the event store](https://developer.apple.com/documentation/eventkit/accessing-the-event-store). Store authorization, required usage descriptions, and writable-calendar filtering are separate concerns; older OS versions have different requirements.

## Topics

### Calendar Views
- [`EKEventViewController`](https://developer.apple.com/documentation/eventkitui/ekeventviewcontroller) - Displays a calendar event with optional editing. Set its `event: EKEvent!` before presentation.

### Calendar Edits
- [`EKEventEditViewController`](https://developer.apple.com/documentation/eventkitui/ekeventeditviewcontroller) - Creates, edits, or deletes calendar events.

### Calendar Selection
- [`EKCalendarChooser`](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser) - Presents single or multiple calendar selection with an optional writable-calendar filter.

### EventKit Bundle Access
- [`EventKitUIBundle()`](https://developer.apple.com/documentation/eventkitui/eventkituibundle()) - A function returning `Bundle!`; don't substitute it for `Bundle.main` when locating your app's own resources.

### Reference
- [EventKitUI Constants](https://developer.apple.com/documentation/eventkitui/eventkitui-constants) - Reference availability/export macros.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/EventKitUI)*
