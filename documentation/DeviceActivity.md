# DeviceActivity

Monitor device activity with your app extension while maintaining user privacy.

**Platforms:** iOS 15.0+ | iPadOS 15.0+ | Mac Catalyst 15.0+

## Overview

Device Activity provides a privacy-preserving way for an application to monitor a user's application and website activity. For instance, you can set up a bedtime schedule that monitors device activity while the user is supposed to be asleep. Your app extension can receive warnings before an activity's schedule starts or ends, or when an activity is about to reach a predefined threshold. You can monitor the time spent on websites and apps to warn the user once they have reached their threshold.

## Topics

### Manage Activities
- **DeviceActivityEvent** - An event that represents an application, category, or website activity.
- **DeviceActivityName** - The unique name of an activity.
- **DeviceActivitySchedule** - A calendar-based schedule for when to monitor a device's activity.
- **DeviceActivityCenter** - A class that enables an application's extension to start monitoring scheduled device activity.

### Monitor Activity
- **DeviceActivityMonitor** - The object that monitors scheduled device activity.

### Errors
- **MonitoringError** - Errors that may occur when starting to monitor an activity.

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

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/DeviceActivity)*