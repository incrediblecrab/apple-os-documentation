# EventKit UI

Display an interface for viewing, selecting, and editing calendar events and reminders.

**Platforms:** iOS 4.0+ | iPadOS 4.0+ | Mac Catalyst 13.0+ | visionOS 1.0+

## Overview

On iOS, use the EventKitUI framework to show calendar and reminder information to the user modally. EventKitUI provides view controllers for viewing and editing calendar and reminder information, choosing which calendar to view, and for determining whether to present calendars as read-only or readable and writeable.

The view controllers you'll use on iOS are:

- **EKEventViewController**, for displaying existing events.
- **EKEventEditViewController**, for creating, editing, or deleting events.
- **EKCalendarChooser**, for selecting one or more calendars, and to determine whether a calendar has read-only or read-write access.

You present these interfaces from within your app. Upon presentation, the system manages all interactions with the user, notifying you when the interfaces are dismissed.

EventKitUI also provides several configurable classes for selecting a default calendar, displaying buttons, or to enabling the user to select one or more calendars.

> **Note:** To access the event store, which contains calendar and reminder data, use EventKit. For more information, see Accessing the event store.

## Topics

### Calendar Views
- **EKEventViewController** - A view controller for displaying existing calendar and reminder events, and for optionally editing those events.

### Calendar Edits
- **EKEventEditViewController** - A view controller for creating, editing, and deleting calendar events.

### Calendar Selection
- **EKCalendarChooser** - A view controller for determining whether a user may select one or more calendars.

### EventKit Bundle Access
- **EventKitUIBundle()** - Use to access resources within the app bundle.

### Reference
- **EventKitUI Constants**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/EventKitUI)*