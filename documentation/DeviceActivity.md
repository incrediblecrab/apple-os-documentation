# DeviceActivity

Monitor device activity with your app extension while maintaining user privacy.

**Platforms:** iOS 15.0+ | iPadOS 15.0+ | Mac Catalyst 15.0+

## Overview

Device Activity provides a privacy-preserving way for an application to monitor a user's application and website activity. For instance, you can set up a bedtime schedule that monitors device activity while the user is supposed to be asleep. Your app extension can receive warnings before an activity's schedule starts or ends, or when an activity is about to reach a predefined threshold. You can monitor the time spent on websites and apps to warn the user once they have reached their threshold.

### Authorization and scheduling limits

Coordinate monitoring with [FamilyControls](FamilyControls.md) authorization and respond when approval is denied or revoked. Selected activity tokens preserve privacy; they are not an unrestricted inventory of another person's app or web usage.

[`DeviceActivityCenter`](https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter) starts and stops named monitoring activities. Handle failures from `startMonitoring(_:during:events:)` and stop obsolete schedules explicitly.

Schedule boundaries are not exact background timers. The system invokes interval-start and interval-end callbacks when the device is in use within or outside the interval, respectively. Do not use them as a promise of continuous runtime or immediate execution at a wall-clock deadline.

The report view and report-extension APIs start at 16.0, later than monitoring's 15.0 minimum. A report extension uses the extension point `com.apple.deviceactivityui.report-extension` and runs in a privacy sandbox that prevents network requests and moving sensitive content outside the extension's address space. The system supplies report data only for appropriately authorized devices.

The separately listed authorization class/protocol have iOS/iPadOS/Catalyst 17 and macOS 14 declaration metadata; that does not establish native macOS support for every monitoring or reporting API.

## Topics

### Manage Activities
- **DeviceActivityEvent** - An event that represents an application, category, or website activity.
- **DeviceActivityName** - The unique name of an activity.
- **DeviceActivitySchedule** - A calendar-based schedule for when to monitor a device's activity.
- **DeviceActivityCenter** - A structure that manages scheduled activity monitoring.

### Monitor Activity
- **DeviceActivityMonitor** - The object that monitors scheduled device activity.

### Errors
- **DeviceActivityCenter.MonitoringError** - Errors that may occur when starting to monitor an activity.

### Classes
- **DeviceActivityAuthorization**

### Protocols
- **DeviceActivityAuthorizing**
- **DeviceActivityReportExtension** - An app extension that reports device activity data.
- **DeviceActivityReportScene** - Defines a custom device activity report scene.

### Structures
- **DeviceActivityData** - Represents the activity of a DeviceActivityData.User on a particular DeviceActivityData.Device.
- **DeviceActivityFilter** - A type that filters the device activity data to include in a report.
- **DeviceActivityReport** - A view that reports the user's application, category, and web domain activity in a privacy-preserving way.
- **DeviceActivityReportBuilder** - A result builder that combines one or more DeviceActivityReportScenes into a single scene.
- **DeviceActivityResults** - An asynchronous sequence of filtered device activity results.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/DeviceActivity)*

*Changed-content source, reviewed September 8, 2026: [DeviceActivityCenter](https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter.md).*
