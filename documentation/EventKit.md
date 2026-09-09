# EventKit

Create, view, and edit calendar and reminder events.

**Platforms:** iOS 4.0+ | iPadOS 4.0+ | Mac Catalyst 13.1+ | macOS 10.8+ | visionOS 1.0+ | watchOS 2.0+

## Overview

The EventKit framework provides access to calendar and reminders data so people can create, retrieve, and edit calendar items in your app. In iOS, EventKit UI provides user interfaces you can implement in your app so people can create and edit calendar items.

You can use EventKit to set up alarms and create recurring events. And if a change to the Calendar database occurs from outside your app, EventKit detects the change and sends a notification, allowing your app to stay up to date.

## Choose the minimum access

The current [event-store authorization guide](https://developer.apple.com/documentation/eventkit/accessing-the-event-store) distinguishes write-only event access, full event access, and full reminder access. There is no separate read-only grant. Write-only access cannot read even the events your app created; empty fetch results therefore do not imply that the user's calendar is empty.

For the iOS 17-and-later flow:

- Use `requestWriteOnlyAccessToEvents(completion:)` with `NSCalendarsWriteOnlyAccessUsageDescription` when creating events directly is sufficient.
- Use `requestFullAccessToEvents(completion:)` with `NSCalendarsFullAccessUsageDescription` when the feature needs to read or edit calendar data.
- Use `requestFullAccessToReminders(completion:)` with `NSRemindersFullAccessUsageDescription` for reminders.
- For a user-controlled event-creation interface, consider `EKEventEditViewController`. Its out-of-process editor can save an event without giving your app calendar-database access; dismissal does not reveal the user's final edits to your app.

These permission changes predate OS 27. Keep availability branches and legacy usage descriptions for older deployment targets. Sandboxed macOS apps also need `com.apple.security.personal-information.calendars`.

## Failure and change handling

Check authorization before exposing data-dependent features and handle both the permission response and save/fetch errors. Retain the event store while its objects are in use. Refetch after database-change notifications rather than treating cached objects as a permanently current calendar. Do not infer successful persistence merely from presenting an editor.

## Topics

### Essentials
- [Accessing the event store](https://developer.apple.com/documentation/eventkit/accessing-the-event-store) - Request access to a person's calendar data through the event store.
- **EKEventStore** - An object that accesses a person's calendar events and reminders and supports the scheduling of new events.
- [Accessing Calendar using EventKit and EventKitUI](https://developer.apple.com/documentation/eventkit/accessing-calendar-using-eventkit-and-eventkitui) - Choose and implement the appropriate Calendar access level in your app.

### Events and reminders
- [Creating events and reminders](https://developer.apple.com/documentation/eventkit/creating-events-and-reminders) - Create and modify events and reminders in a person's database.
- [Retrieving events and reminders](https://developer.apple.com/documentation/eventkit/retrieving-events-and-reminders) - Fetch events and reminders from the Calendar database.
- [Updating with notifications](https://developer.apple.com/documentation/eventkit/updating-with-notifications) - Register for notifications about changes and keep your app up to date.
- [Managing location-based reminders](https://developer.apple.com/documentation/eventkit/managing-location-based-reminders) - Access reminders set up with geofence-enabled alarms on a person's calendars.
- **EKEvent** - A class that represents an event in a calendar.
- **EKReminder** - A class that represents a reminder in a calendar.

### Calendars
- **EKCalendar** - A class that represents a calendar in EventKit.
- **EKParticipant** - A class that represents person, group, or room invited to a calendar event.

### Recurrence
- [Creating a recurring event](https://developer.apple.com/documentation/eventkit/creating-a-recurring-event) - Set up an event or reminder that repeats.
- **EKRecurrenceDayOfWeek** - A class that represents the day of the week.
- **EKRecurrenceEnd** - A class that defines the end of a recurrence rule.
- **EKRecurrenceRule** - A class that describes the pattern for a recurring event.

### Alarms
- [Setting an alarm](https://developer.apple.com/documentation/eventkit/setting-an-alarm) - Alert users of events and reminders with an alarm.
- **EKAlarm** - A class that represents an alarm.
- **EKStructuredLocation** - A class that specifies a geofence to activate the alarm of a calendar item.

### Common objects
- **EKCalendarItem** - An abstract superclass for calendar events and reminders.
- **EKObject** - An abstract superclass for all EventKit classes that have persistent instances.
- [**EKSource**](https://developer.apple.com/documentation/eventkit/eksource) - Information about the account a calendar belongs to. Retrieve sources from the event store rather than constructing them directly.

### Virtual conferences
- **EKVirtualConferenceProvider** - An object that associates virtual conferencing details with an event object in a user's calendar.
- **EKVirtualConferenceDescriptor** - Details about a virtual conference that uses a custom room type.
- **EKVirtualConferenceRoomTypeDescriptor** - Details about a room where virtual conferences take place.

### Errors
- **EKError** - An EventKit error.
- [**EKError.Code**](https://developer.apple.com/documentation/eventkit/ekerror/code) - Error codes for EventKit errors.
- **EKErrorDomain** - A string that identifies the EventKit error domain.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/EventKit)*
