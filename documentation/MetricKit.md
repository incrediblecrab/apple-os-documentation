# MetricKit

Aggregate and analyze per-device reports on exception and crash diagnostics and on power and performance metrics.

**Platforms:** iOS 13.0+ | iPadOS 13.0+ | Mac Catalyst 13.0+ | macOS 12.0+ | visionOS 1.0+

## Overview

With MetricKit, you can receive on-device app diagnostics and power and performance metrics the system captures. The system delivers metric reports about the previous 24 hours to a registered app at most once per day, and delivers diagnostic reports immediately in iOS 15 and later and macOS 12 and later. This framework supports diagnostics for crashes, hangs, energy, and disk writes for apps running in visionOS but doesn't report metrics for apps running in visionOS. This includes apps built for visionOS or compatible iPhone and iPad apps running in visionOS.

Use the data in the reports to help improve the performance of your iOS app, macOS app, or Mac app built with Mac Catalyst. The framework includes the following:

- A manager class and a subscriber protocol
- Payload classes for reported data
- Classes for each category of metrics and diagnostics
- Classes for measurement units, such as bars of cellular connectivity
- Classes for representing accumulated data, such as histograms
- A class for capturing stack traces in diagnostics

## Topics

### Essentials
- **MXMetricManager** - The shared object that registers you to receive metrics, creates logs for custom metrics, and gives access to past reports.
- **MXMetricPayload** - An object that encapsulates a daily metrics report.
- **MXDiagnosticPayload** - An object that encapsulates a diagnostic report.
- **MXMetricManagerSubscriber** - A protocol defining a method for receiving a daily metrics report.

### Performance improvements
- [Improving your app's performance](https://developer.apple.com/documentation/metrickit/improving_your_app_s_performance) - Model, measure, and boost the performance of your app by using a continuous-improvement cycle.

### Battery metrics
- **MXCellularConditionMetric** - An object representing metrics about the condition of the cellular network.
- **MXCPUMetric** - An object representing metrics about the use of the CPU.
- **MXDisplayMetric** - An object representing metrics about the power used to display the app on the screen.
- **MXGPUMetric** - An object representing metrics about the use of the GPU.
- **MXLocationActivityMetric** - An object representing metrics about the use of location-tracking features of a device.
- **MXNetworkTransferMetric** - An object representing metrics about network transfers.
- **MXCPUExceptionDiagnostic** - An object representing a diagnostic report for a fatal or nonfatal CPU exception.

### Performance metrics
- **MXAppLaunchDiagnostic** - A diagnostic subclass that encapsulates app launch diagnostic reports.
- **MXAppExitMetric** - An object representing metrics about the types of foreground and background app exits.
- **MXAppRunTimeMetric** - An object representing metrics about the amount of time the app is active.
- **MXMemoryMetric** - An object representing metrics about the app's memory use.
- **MXCrashDiagnostic** - An object representing a diagnostic report for an app crash.

### Responsiveness metrics
- **MXAnimationMetric** - An object representing metrics about the responsiveness of animation in the app.
- **MXAppLaunchMetric** - An object representing metrics about app launch time.
- **MXAppResponsivenessMetric** - An object representing metrics about the responsiveness of the app to user interaction.
- **MXHangDiagnostic** - An object representing a diagnostic report for an app that is too busy to handle user input responsively.

### Disk usage metrics
- **MXDiskIOMetric** - An object representing metrics about disk usage.
- **MXDiskSpaceUsageMetric** - An object representing metrics about your app's disk space usage. (Beta)
- **MXDiskWriteExceptionDiagnostic** - An object representing a diagnostic report for a disk write exception.

### Custom metrics
- **MXSignpostMetric** - An object representing a custom metric.

### Data types
- **MXCallStackTree** - An object representing the call stack for an exception.
- **MXMetaData** - An object containing system-level information about the device.
- **MXAverage** - A unit of measure for an average.
- **MXHistogram** - An object representing a histogram of data values of the same type of unit.
- **MXDiagnostic** - An abstract data class for a diagnostic.
- **MXMetric** - An abstract data class for a metric.
- **Code** - Error codes for error values from app metrics.
- **MXErrorDomain** - Error domain for error values from app metrics.
- **MXError** - Error domain for error handling of app metrics.
- **MXCrashDiagnosticObjectiveCExceptionReason** - An object that represents the exception reason for an uncaught ObjC exception.
- **MXSignpostRecord** - An object representing the record for a signpost interval or event.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MetricKit)*