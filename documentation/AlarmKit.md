# AlarmKit

Schedule prominent alarms and countdowns to help people manage their time.

**Platforms:** iOS 26.0+ | iPadOS 26.0+ | Mac Catalyst 26.0+

## Overview

Use AlarmKit to create custom alarms and timers in your app. AlarmKit provides a framework for managing alarms with customizable schedules and UI. It supports one-time and repeating alarms, with the option for countdown durations and snooze functionality. AlarmKit handles alarm authorization and provides UI for both templated and widget presentations. It supports traditional alarms, timers, or both, and provides methods to schedule, pause, resume, and cancel alarms.

> **iOS 27+, iPadOS 27+:** Alarm presentation renders against the refined Liquid Glass material. System notification grouping is smarter in OS 27, so re-check how alarm-related notifications read when the system aggregates them.

## Topics

### Alarm management
- [Scheduling an alarm with AlarmKit](https://developer.apple.com/documentation/alarmkit/scheduling_an_alarm_with_alarmkit) - Create prominent alerts at specified dates for your iOS app.
- **AlarmManager** - An object that exposes functions to work with alarms: scheduling, snoozing, cancelling.
- **Alarm** - An object that describes an alarm that can alert once or on a repeating schedule.

### Buttons
- **AlarmButton** - A structure that defines the appearance of buttons.

### Views
- **AlarmPresentation** - An object that describes the content required for the alarm UI.
- **AlarmPresentationState** - An object that describes the mutable content of the alarm.
- **AlarmAttributes** - An object that contains all information necessary for the alarm UI.
- **AlarmMetadata** - A metadata object that contains information about an alarm.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AlarmKit)*
