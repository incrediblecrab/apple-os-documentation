# RelevanceKit

Supply contextual clues for widget relevance on Apple Watch.

**Platforms:** iOS 26.0+ | iPadOS 26.0+ | Mac Catalyst 26.0+ | macOS 26.0+ | visionOS 26.0+ | watchOS 26.0+

## Overview

watchOS considers contextual clues alongside other signals when ordering widgets in the Smart Stack. Your widget can describe when its content is useful, such as near a location, during a workout, or around a scheduled event. A matching clue doesn't guarantee visibility or a particular position.

Provide these values through the widget's timeline-provider relevance workflow or a `RelevanceEntriesProvider`, as described in [WidgetKit](WidgetKit.md). Constructing a `RelevantContext` value alone doesn't request placement. Contextual watch relevance is distinct from the behavioral App Intent donations used for iPhone and iPad widgets.

Use RelevanceKit with WidgetKit and [App Intents](AppIntents.md), including supported iPhone-widget experiences on Apple Watch. App Intents makes the relevance types available when you `import AppIntents`; a separate `import RelevanceKit` isn't required for that workflow.

For the platform-specific workflows, see [Increasing the visibility of widgets in Smart Stacks](https://developer.apple.com/documentation/widgetkit/widget-suggestions-in-smart-stacks).

**Note:** Smart Stacks are available in iOS, iPadOS, and watchOS. However, functionality provided by RelevanceKit is only available in watchOS. Calling its API on other platforms doesn't have any effect.

### Availability and permissions

The framework catalog lists the 26 generation. `RelevantContext` and its basic fitness, hardware, location, sleep, and single-date declarations retain older iOS/iPadOS/Mac Catalyst/tvOS 17, macOS 14, watchOS 10, and usually visionOS 1 labels; the exact `CLRegion` location overload has no visionOS declaration. `DateKind` and the date overloads accepting a `kind` require 26. These annotations don't turn the framework into a ranking API for other platforms.

Fitness clues require the corresponding HealthKit authorization: workout access for an active workout, and the documented activity-time types for incomplete rings. Sleep clues require `sleepAnalysis` permission. Exact and inferred location clues require When in Use or Always authorization. If the required contextual information isn't available, those clues have no effect; a clue isn't a permission bypass.

## Topics

### Providing relevance information
- [Increasing the visibility of widgets in Smart Stacks](https://developer.apple.com/documentation/widgetkit/widget-suggestions-in-smart-stacks) - Choose the appropriate contextual or behavioral relevance workflow for each platform.
- [`RelevantContext`](https://developer.apple.com/documentation/relevancekit/relevantcontext) - A value representing a watch widget's contextual relevance.

### Fitness clues
- [`fitness(_:)`](https://developer.apple.com/documentation/relevancekit/relevantcontext/fitness(_:)) - Creates a clue from a `RelevantContext.FitnessCondition`.
- [`FitnessCondition`](https://developer.apple.com/documentation/relevancekit/relevantcontext/fitnesscondition) - A structure describing supported fitness conditions.

### Hardware clues
- [`hardware(headphones:)`](https://developer.apple.com/documentation/relevancekit/relevantcontext/hardware(headphones:)) - Creates a clue from a `RelevantContext.HeadphonesCondition`.
- [`HeadphonesCondition`](https://developer.apple.com/documentation/relevancekit/relevantcontext/headphonescondition) - Describes connected-headphone context.

### Location clues
- [`location(_:)`](https://developer.apple.com/documentation/relevancekit/relevantcontext/location(_:)) - Creates a clue for a supplied `CLRegion`.
- [`location(inferred:)`](https://developer.apple.com/documentation/relevancekit/relevantcontext/location(inferred:)) - Creates a clue for a `RelevantContext.InferredLocation`.
- [`InferredLocation`](https://developer.apple.com/documentation/relevancekit/relevantcontext/inferredlocation) - Describes inferred home, work, school, and commute contexts.

### Sleep clues
- [`sleep(_:)`](https://developer.apple.com/documentation/relevancekit/relevantcontext/sleep(_:)) - Creates a clue from a `RelevantContext.SleepCondition`.
- [`SleepCondition`](https://developer.apple.com/documentation/relevancekit/relevantcontext/sleepcondition) - Describes typical bedtime or wakeup context.

### Time clues
- [`date(_:)`](https://developer.apple.com/documentation/relevancekit/relevantcontext/date(_:)) - Creates a clue for a `Date`.
- [`date(_:kind:)`](https://developer.apple.com/documentation/relevancekit/relevantcontext/date(_:kind:)) - Adds a `DateKind` hint to a date.
- [`date(interval:kind:)`](https://developer.apple.com/documentation/relevancekit/relevantcontext/date(interval:kind:)) - Uses a `DateInterval` and explicit kind.
- [`date(range:kind:)`](https://developer.apple.com/documentation/relevancekit/relevantcontext/date(range:kind:)) - Uses a `ClosedRange<Date>` and explicit kind.
- [`DateKind`](https://developer.apple.com/documentation/relevancekit/relevantcontext/datekind) - Supplies additional time-context information.
- [`date(from:to:)`](https://developer.apple.com/documentation/relevancekit/relevantcontext/date(from:to:)) - The two-date form is deprecated in the 26 generation; use a supported interval/range overload instead.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/RelevanceKit)*
