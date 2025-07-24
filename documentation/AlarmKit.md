# AlarmKit

Schedule prominent alarms and countdowns to help people manage their time.

**Platforms:** iOS 26.0+ *Beta* | iPadOS 26.0+ *Beta* | Mac Catalyst 26.0+ *Beta*

## Overview

Use AlarmKit to create custom alarms and timers in your app. AlarmKit provides a framework for managing alarms with customizable schedules and UI. It supports one-time and repeating alarms, with the option for countdown durations and snooze functionality. AlarmKit handles alarm authorization and provides UI for both templated and widget presentations. It supports traditional alarms, timers, or both, and provides methods to schedule, pause, resume, and cancel alarms.

**Beta Software:** This documentation contains preliminary information about an API or technology in development. This information is subject to change, and software implemented according to this documentation should be tested with final operating system software.

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

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AlarmKit)*