# CrashReportExtension

Inspect a crashed app from a separate extension process.

**Platforms:** iOS 27.0+ | iPadOS 27.0+ | macOS 27.0+

**Status:** Beta APIs as of September 8, 2026. Not available to Mac Catalyst apps or iOS apps running on Apple silicon Macs.

## Overview

CrashReportExtension provides an out-of-process alternative to running crash-analysis code inside a failing app. The system invokes an embedded extension that conforms to `CrashReporterExtension`; the extension inspects the supplied `CrashedProcess` and produces the app's own crash report.

This is distinct from [MetricKit](MetricKit.md), which delivers system-collected metric and diagnostic reports. Use the extension when you need the documented crash-time inspection facilities, not as a general-purpose process debugger or a replacement for everyday performance monitoring.

## Configuration and lifecycle

Create the target using Xcode's Crash Report Extension template. Its bundle identifier must be a child of the containing app's identifier. The extension's Info.plist declares `EXExtensionPointIdentifier` as `com.apple.crash-reporter.extension` inside `EXAppExtensionAttributes`.

Implement [`processCrashReport(process:)`](https://developer.apple.com/documentation/crashreportextension/crashreporterextension/processCrashReport(process:)). The supplied [`CrashedProcess`](https://developer.apple.com/documentation/crashreportextension/crashedprocess) exposes crash information, symbolication facilities, and a **read-only** Mach port for inspection. It does not authorize arbitrary modification of the crashed process.

## Failure and privacy considerations

Design report collection for incomplete data: a failed process may not have the state your normal application code expects. Keep the extension independent of the app's live objects and avoid treating a crash callback as guaranteed background execution.

If reports are sent to your service, handle upload failures separately from collection and minimize the data retained. Process memory and crash context can contain credentials or personal content; prefer the smallest diagnostic record needed to investigate the failure.

The documented platform exclusions still apply even when an app can import related SDK symbols. Test the extension on each supported deployment target rather than using a Catalyst or iOS-on-Mac run as evidence of support.

## Topics

- [CrashReporterExtension](https://developer.apple.com/documentation/crashreportextension/crashreporterextension) — Extension entry point.
- [processCrashReport(process:)](https://developer.apple.com/documentation/crashreportextension/crashreporterextension/processCrashReport(process:)) — Crash processing callback.
- [CrashedProcess](https://developer.apple.com/documentation/crashreportextension/crashedprocess) — Read-only inspection of the crashed app.
- [MetricKit](MetricKit.md) and [StateReporting](StateReporting.md) — System reports and application-state context.

## Sources

- [Apple framework reference](https://developer.apple.com/documentation/crashreportextension)
- [Readable framework documentation](https://developer.apple.com/documentation/crashreportextension.md)
- [Platform metadata](https://developer.apple.com/tutorials/data/documentation/crashreportextension.json)
