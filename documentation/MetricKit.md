# MetricKit

Aggregate and analyze per-device reports on exception and crash diagnostics and on power and performance metrics.

**Platforms:** iOS 13.0+ | iPadOS 13.0+ | Mac Catalyst 13.1+ | macOS 12.0+ | visionOS 1.0+. Report types have additional availability limits.

## Overview

MetricKit delivers system-collected performance information from real device usage. Daily metric reports summarize a reporting period; diagnostics describe events such as crashes, hangs, and resource exceptions. Delivery is not a general-purpose live telemetry feed or a guarantee of a report at a particular time.

The legacy manager documents daily performance metrics on macOS 26 and later, while diagnostic delivery is available from macOS 12. It can receive more than one metric payload in a day when different system sources report separately; “daily” is not a guarantee of exactly one callback or payload.

The framework supports diagnostics on visionOS, including compatible iPhone and iPad apps, but **does not deliver performance metric reports there**. This remains true for the new Swift API.

### 27 beta: Swift report delivery

**Reviewed September 8, 2026:** Adopt [`MetricManager`](https://developer.apple.com/documentation/metrickit/metricmanager) for new integrations on iOS/iPadOS 27.0+, Mac Catalyst 27.0+, macOS 27.0+, and visionOS 27.0+ where the requested report type is supported.

The release notes describe **AsyncStream-based** delivery of `MetricReport` and `DiagnosticReport`. The public [`metricReports`](https://developer.apple.com/documentation/metrickit/metricmanager/metricreports) and [`diagnosticReports`](https://developer.apple.com/documentation/metrickit/metricmanager/diagnosticreports) properties expose nonthrowing asynchronous sequences; consume them with `for await` rather than assuming a concrete stream type. Keep the manager and observation tasks alive for the intended subscription lifetime, and observe metrics and diagnostics independently so one long-lived loop does not prevent the other from starting.

`MetricReport` contains a full-day aggregate and interval breakdowns, typically spanning a few hours each. Use its reported time range rather than assuming fixed boundaries. A `DiagnosticReport` represents an individual diagnostic event. The metric sequence is unavailable on visionOS; the diagnostic sequence is supported.

### State and diagnostic integration

Register domains with `MetricManager(enabledStateReportingDomains:)` and emit transitions using [StateReporting](StateReporting.md). Reports can then include state-segmented entries and diagnostic state context. Without registered or active states, do not expect populated state entries. MetricKit surfaces stable metadata, not volatile metadata.

The state-domain initializer is documented for iOS/iPadOS, Mac Catalyst, and macOS 27. It is not the initializer for visionOS's diagnostic-only subscription; use the supported `MetricManager()` path there.

New 27-generation diagnostics and metrics include `MemoryExceptionDiagnostic`, `MetalFrameRateMetric`, and `CrashDiagnostic.terminationCategory`. `MemoryExceptionDiagnostic` is specifically declared for iOS/iPadOS 27, not native macOS, Mac Catalyst, or visionOS. Treat optional or unavailable measurements as missing data rather than zero. Handle future metric and diagnostic cases when switching over results.

The beta release notes also replace `ScrollHitchTimeMetric` and `MetricResult.scrollHitchTime(_:)` with `HitchTimeMetric` and `.hitchTime(_:)`. `HitchTimeRatio` expresses milliseconds of hitching per second of tracked duration. Recompile code using changed beta symbols to avoid missing-symbol or type-change failures.

[CrashReportExtension](CrashReportExtension.md) is a separate out-of-process crash-inspection facility, not the report subscription API. Its platform exclusions differ from MetricKit's.

### Compatibility and testing

The original `MXMetricManager`, `MXMetricManagerSubscriber`, `MXMetricPayload`, and `MXDiagnosticPayload` interfaces are **no longer recommended for new adoption** in the 27 release notes and carry 27.0 deprecation annotations. Deprecation is not removal. Retain the [MX API](https://developer.apple.com/documentation/metrickit/mxmetricmanager-api) where needed for older deployment targets; its presence below does not mean the new Swift APIs are available at the framework's historical minimum.

Use Xcode's **Debug > Simulate MetricKit Payloads** to exercise report handling. Simulated values are sample data, not measurements of the running app. Apple's state-reporting sample requires Xcode 27 and a physical iOS 27 device; MetricKit does not deliver its reports on simulated devices. Minimize personal data in state metadata and in any reports sent to a backend.

## Topics

### Current Swift API
- [Monitoring app performance with MetricKit](https://developer.apple.com/documentation/metrickit/monitoring-app-performance-with-metrickit)
- [Analyzing app performance with MetricKit](https://developer.apple.com/documentation/metrickit/analyzing-app-performance-with-metrickit)
- [MetricManager](https://developer.apple.com/documentation/metrickit/metricmanager)
- [MetricReport](https://developer.apple.com/documentation/metrickit/metricreport)
- [DiagnosticReport](https://developer.apple.com/documentation/metrickit/diagnosticreport)
- [Track performance by app state using MetricKit](https://developer.apple.com/documentation/metrickit/track-performance-by-app-state-using-metrickit)

### Legacy MX API essentials
- **MXMetricManager** - The shared object that registers you to receive metrics, creates logs for custom metrics, and gives access to past reports.
- **MXMetricPayload** - An object that encapsulates a daily metrics report.
- **MXDiagnosticPayload** - An object that encapsulates a diagnostic report.
- **MXMetricManagerSubscriber** - A protocol for receiving metric payloads and, where supported, diagnostic payloads.

### Performance improvements
- [Improving your app's performance](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance) - Model, measure, and boost the performance of your app using a continuous-improvement cycle.

### Battery metrics
- **MXCellularConditionMetric** - An object representing metrics about the condition of the cellular network.
- **MXCPUMetric** - An object representing metrics about the use of the CPU.
- **MXDisplayMetric** - Display metrics, including average pixel luminance, useful when analyzing screen-related energy use.
- **MXGPUMetric** - An object representing metrics about the use of the GPU.
- **MXLocationActivityMetric** - An object representing metrics about the use of location-tracking features of a device.
- **MXNetworkTransferMetric** - An object representing metrics about network transfers.

### Performance metrics
- **MXAppExitMetric** - An object representing metrics about the types of foreground and background app exits.
- **MXAppRunTimeMetric** - An object representing metrics about the amount of time the app is active.
- **MXMemoryMetric** - An object representing metrics about the app's memory use.

### Responsiveness metrics
- **MXAnimationMetric** - An object representing metrics about the responsiveness of animation in the app.
- **MXAppLaunchMetric** - An object representing metrics about app launch time.
- **MXAppResponsivenessMetric** - An object representing metrics about the responsiveness of the app to user interaction.

### Disk usage metrics
- **MXDiskIOMetric** - An object representing metrics about disk usage.
- **MXDiskSpaceUsageMetric** - An object representing metrics about your app's disk space usage.

### Performance diagnostics
- **MXAppLaunchDiagnostic** - An app-launch diagnostic report.
- **MXCPUExceptionDiagnostic** - A report for a fatal or nonfatal CPU exception.
- **MXCrashDiagnostic** - An app-crash diagnostic report.
- **MXHangDiagnostic** - A report for an app that is too busy to handle user input responsively.
- **MXDiskWriteExceptionDiagnostic** - A report for a disk-write exception.

### Custom metrics
- **MXSignpostMetric** - An object representing a custom metric.

### Data types
- **MXCallStackTree** - An object representing the call stack for an exception.
- **MXMetaData** - An object containing system-level information about the device.
- **MXAverage** - A generic object containing an average measurement, parameterized by its unit type.
- **MXHistogram** - An object representing a histogram of data values of the same type of unit.
- **MXDiagnostic** - An abstract data class for a diagnostic.
- **MXMetric** - An abstract data class for a metric.
- **MXError.Code** - Error codes for error values from app metrics.
- **MXErrorDomain** - Error domain for error values from app metrics.
- **MXError** - A Swift error value for MetricKit failures, distinct from the domain string.
- **MXCrashDiagnosticObjectiveCExceptionReason** - An object that represents the exception reason for an uncaught ObjC exception.
- **MXSignpostRecord** - An object representing the record for a signpost interval or event.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MetricKit)*

*Changed-content sources: [Swift reporting guide](https://developer.apple.com/documentation/metrickit/monitoring-app-performance-with-metrickit.md), [framework overview](https://developer.apple.com/documentation/metrickit.md), and [iOS/iPadOS 27 release notes — MetricKit](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes.md).*
