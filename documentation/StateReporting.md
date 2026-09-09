# StateReporting

Attach application-defined state to performance measurements and diagnostics.

**Platforms:** iOS 27.0+ | iPadOS 27.0+ | Mac Catalyst 27.0+ | macOS 27.0+ | tvOS 27.0+ | visionOS 27.0+ | watchOS 27.0+

**Status:** Beta APIs; availability checked in Apple's documentation JSON on September 8, 2026.

## Overview

StateReporting describes what an app is doing when a performance event occurs. Define separate domains for independent concerns, such as a playback mode and a rendering configuration. Each domain has at most one active state; several domains can be active together.

Instruments shows transitions in Points of Interest. [MetricKit](MetricKit.md) can associate reports with registered domains, enabling comparisons between app states rather than only whole-day averages. StateReporting's platform availability does not imply that MetricKit delivers performance metrics on every one of those platforms.

## Reporting model

Obtain a long-lived [`StateReporter`](https://developer.apple.com/documentation/statereporting/statereporter) for a stable reverse-DNS domain. Its stable metadata describes the categories used for aggregation; volatile metadata describes changing details without creating another category.

- Use [`reportTransition(to:stableMetadata:volatileMetadata:)`](https://developer.apple.com/documentation/statereporting/statereporter/reportTransition(to:stableMetadata:volatileMetadata:)) when a label or stable metadata changes.
- Clear the active state by passing `nil` as the label. An empty string is invalid and causes a fatal error.
- Use [`reportVolatileMetadataUpdate(_:)`](https://developer.apple.com/documentation/statereporting/statereporter/reportVolatileMetadataUpdate(_:)) for changing details. It has no effect without an active state.
- Define metadata with [`ReportableMetadata`](https://developer.apple.com/documentation/statereporting/reportablemetadata), or its macro, and omit unnecessary fields with [`ReportableMetadataIgnored()`](https://developer.apple.com/documentation/statereporting/ReportableMetadataIgnored()).

## Constraints and integration

Reusing a domain with different metadata types crashes at runtime. Keep type choices consistent throughout the process. Choose a small set of meaningful states: identifiers, timestamps, or continuously changing values in stable metadata fragment aggregation. Do not put sensitive user content into diagnostic labels or metadata.

Reporting is rate-limited. Emit changes at interaction or activity boundaries, not on every frame; excessive calls lose data.

Register the domains with `MetricManager` to obtain state-contextualized reports. MetricKit surfaces **stable** metadata; do not depend on volatile metadata appearing there. App extensions can emit diagnostic state, but do not receive metric reports. Each extension registers its own domains, and its diagnostic reports are delivered to the main app.

Check the receiving API separately: `MetricManager`'s state-domain initializer is available on iOS/iPadOS, Mac Catalyst, and macOS 27, not on every platform that supports StateReporting.

## Topics

- [Getting started with StateReporting](https://developer.apple.com/documentation/statereporting/getting-started-with-statereporting)
- [StateReporter](https://developer.apple.com/documentation/statereporting/statereporter) and [SRStateReporter](https://developer.apple.com/documentation/statereporting/srstatereporter)
- [ReportableMetadataValue](https://developer.apple.com/documentation/statereporting/reportablemetadatavalue)
- [Monitoring app performance with MetricKit](https://developer.apple.com/documentation/metrickit/monitoring-app-performance-with-metrickit)

## Sources

- [Apple framework reference](https://developer.apple.com/documentation/statereporting)
- [Getting-started documentation](https://developer.apple.com/documentation/statereporting/getting-started-with-statereporting.md)
- [Platform metadata](https://developer.apple.com/tutorials/data/documentation/statereporting.json)
