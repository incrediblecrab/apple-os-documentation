# AlarmKit

Schedule prominent alarms and countdowns to help people manage their time.

**Platforms:** iOS 26.0+ | iPadOS 26.0+ | Mac Catalyst 26.0+

## Overview

Use AlarmKit to create custom alarms and timers in your app. AlarmKit provides a framework for managing alarms with customizable schedules and UI. It supports one-time and repeating alarms, with the option for countdown durations and snooze functionality. AlarmKit handles alarm authorization and provides UI for both templated and widget presentations. It supports traditional alarms, timers, or both, and provides methods to schedule, pause, resume, and cancel alarms.

Use [`AlarmManager`](https://developer.apple.com/documentation/alarmkit/alarmmanager) for alarm authorization and scheduling, and [`AlarmPresentationState`](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate) for the system-managed state of an alarm Live Activity. AlarmKit remains a 26-generation framework; consumer notification-grouping behavior is not an AlarmKit API contract. Keep alarm scheduling separate from ordinary [UserNotifications](UserNotifications.md) and from app-managed [ActivityKit](ActivityKit.md) updates.

Provide a nonempty [`NSAlarmKitUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsalarmkitusagedescription) and obtain alarm authorization. Without the required description or authorization, alarms aren't scheduled. `pause(id:)` applies to a countdown-state alarm; `resume(id:)` applies to a paused alarm.

Countdown presentations require a widget extension. The scheduling guide warns that omitting it can cause alarms to be dismissed without alerting.

## Topics

### Alarm management
- [Scheduling an alarm with AlarmKit](https://developer.apple.com/documentation/alarmkit/scheduling-an-alarm-with-alarmkit) - Create prominent alerts at specified dates for your iOS app.
- **AlarmManager** - An object that exposes functions to work with alarms: scheduling, snoozing, cancelling.
- [`Alarm`](https://developer.apple.com/documentation/alarmkit/alarm) - A structure describing a one-time or repeating alarm and its state.

### Buttons
- **AlarmButton** - A structure that defines the appearance of buttons.

### Views
- [`AlarmPresentation`](https://developer.apple.com/documentation/alarmkit/alarmpresentation) - A structure describing the alarm's alert, countdown, and paused presentations.
- [`AlarmPresentationState`](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate) - System-managed dynamic content for an alarm Live Activity, not app-owned mutable activity state.
- [`AlarmAttributes`](https://developer.apple.com/documentation/alarmkit/alarmattributes) - Generic static attributes for the alarm UI.
- [`AlarmMetadata`](https://developer.apple.com/documentation/alarmkit/alarmmetadata) - A protocol for custom metadata conforming to `Codable`, `Hashable`, and `Sendable`; an implementation can be empty.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AlarmKit)*
