# RelevanceKit

Provide on-device intelligence with contextual clues that increase your widget's visibility on Apple Watch.

**Platforms:** iOS 26.0+ (Beta) | iPadOS 26.0+ (Beta) | Mac Catalyst 26.0+ (Beta) | macOS 26.0+ (Beta) | visionOS 26.0+ (Beta) | watchOS 26.0+ (Beta)

## Overview

On Apple Watch, widgets appear in the Smart Stack in an order that best fits a person's context. To order the widgets that appear in the Smart Stack, watchOS attempts to determine a widget's relevance based on several factors, including contextual clues your app provides to the system.

To give your widget additional visibility in the watchOS Smart Stack and ensure it appears when a person needs it, use **RelevanceKit** to provide contextual clues that signal the widget's relevance to the system. For example, your widget might be most useful at a specific location or time, or every time a person starts a workout.

Note that you use RelevanceKit in combination with **WidgetKit** and **App Intents** to provide interactive and contextually relevant widgets in the Smart Stack, including iPhone widgets that appear on Apple Watch. When you add an import statement for App Intents to your code, App Intents implicitly adds a dependence to RelevanceKit. You don't need to explicitly add import RelevanceKit to your code.

For more information, refer to [Increasing the visibility of widgets in Smart Stacks](https://developer.apple.com/documentation/watchos-apps/increasing-the-visibility-of-widgets-in-smart-stacks).

**Note:** Smart Stacks are available in iOS, iPadOS, and watchOS. However, functionality provided by RelevanceKit is only available in watchOS. Calling its API on other platforms doesn't have any effect.

## Topics

### Providing relevance information
- [Increasing the visibility of widgets in Smart Stacks](https://developer.apple.com/documentation/relevancekit/increasing_the_visibility_of_widgets_in_smart_stacks) - Provide contextual information and donate intents to the system to make sure your widget appears prominently in Smart Stacks.
- **RelevantContext** - Contextual clues the system uses to show relevant widgets in the Smart Stack on watchOS.

### Fitness clues
- **fitness(RelevantContext.FitnessCondition) -> RelevantContext** - Tells the system a widget is relevant because of a person's fitness activity.
- **FitnessCondition** - Values that represent a person's fitness activity.

### Hardware clues
- **hardware(headphones: RelevantContext.HeadphonesCondition) -> RelevantContext** - Tells the system a widget is relevant when a person's headphones are connected.
- **HeadphonesCondition** - A structure that indicates whether a person's headphones are connected.

### Location clues
- **location(CLRegion) -> RelevantContext** - Tells the system a widget is relevant at a specific location.
- **location(inferred: RelevantContext.InferredLocation) -> RelevantContext** - Tells the system a widget is relevant at a person's inferred location.
- **InferredLocation** - A structure with values for a person's inferred home, work, school, and commute locations.

### Sleep clues
- **sleep(RelevantContext.SleepCondition) -> RelevantContext** - Tells the system a widget is relevant because of a person's sleep schedule.
- **SleepCondition** - Values that represent a person's typical bedtime or wakeup time.

### Time clues
- **date(Date) -> RelevantContext** - Tells the system a widget is relevant at a specific date.
- **date(Date, kind: RelevantContext.DateKind) -> RelevantContext** - Tells the system a widget is relevant at a specific date and provides an additional contextual hint.
- **date(interval: DateInterval, kind: RelevantContext.DateKind) -> RelevantContext** - Tells the system a widget is relevant for a time interval and provides an additional contextual hint.
- **date(range: ClosedRange<Date>, kind: RelevantContext.DateKind) -> RelevantContext** - Tells the system a widget is relevant for a known date range and provides an additional contextual hint.
- **DateKind** - Values the system uses as additional context for time-based relevance clues.
- **date(from: Date, to: Date) -> RelevantContext** - Tells the system a widget is relevant between two dates. (Deprecated)

---

**Beta Software**

This documentation contains preliminary information about an API or technology in development. This information is subject to change, and software implemented according to this documentation should be tested with final operating system software.

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/RelevanceKit)*