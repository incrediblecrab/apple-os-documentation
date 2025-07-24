# Pickers

A picker displays one or more scrollable lists of distinct values that people can choose from.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

The system provides several styles of pickers, each of which offers different types of selectable values and has a different appearance. The exact values shown in a picker, and their order, depend on the device language.

Pickers help people enter information by letting them choose single or multipart values. Date pickers specifically offer additional ways to choose values, like selecting a day in a calendar view or entering dates and times using a numeric keypad.

## Topics

### Best Practices

- **Consider using a picker to offer medium-to-long lists of items** - If you need to display a fairly short list of choices, consider using a pull-down button instead of a picker. Although a picker makes it easy to scroll quickly through many items, it may add too much visual weight to a short list of items. On the other hand, if you need to present a very large set of items, consider using a list or table. Lists and tables can adjust in height, and tables can include an index, which makes it much faster to target a section of the list.
- **Use predictable and logically ordered values** - Before people interact with a picker, many of its values can be hidden. It's best when people can predict what the hidden values are, such as with an alphabetized list of countries, so they can move through the items quickly.
- **Avoid switching views to show a picker** - A picker works well when displayed in context, below or in proximity to the field people are editing. A picker typically appears at the bottom of a window or in a popover.
- **Consider providing less granularity when specifying minutes in a date picker** - By default, a minute list includes 60 values (0 to 59). You can optionally increase the minute interval as long as it divides evenly into 60. For example, you might want quarter-hour intervals (0, 15, 30, and 45).

### Platform Considerations

**iOS, iPadOS**  
A date picker is an efficient interface for selecting a specific date, time, or both, using touch, a keyboard, or a pointing device. You can display a date picker in one of the following styles:

- **Compact** — A button that displays editable date and time content in a modal view.
- **Inline** — For time only, a button that displays wheels of values; for dates and times, an inline calendar view.
- **Wheels** — A set of scrolling wheels that also supports data entry through built-in or external keyboards.
- **Automatic** — A system-determined style based on the current platform and date picker mode.

A date picker has four modes, each of which presents a different set of selectable values:

- **Date** — Displays months, days of the month, and years.
- **Time** — Displays hours, minutes, and (optionally) an AM/PM designation.
- **Date and time** — Displays dates, hours, minutes, and (optionally) an AM/PM designation.
- **Countdown timer** — Displays hours and minutes, up to a maximum of 23 hours and 59 minutes. This mode isn't available in the inline or compact styles.

The exact values shown in a date picker, and their order, depend on the device location.

- **Use a compact date picker when space is constrained** - The compact style displays a button that shows the current value in your app's accent color. When people tap the button, the date picker opens a modal view, providing access to a familiar calendar-style editor and time picker. Within the modal view, people can make multiple edits to dates and times before tapping outside the view to confirm their choices.

**macOS**  
- **Choose a date picker style that suits your app** - There are two styles of date pickers in macOS: textual and graphical. The textual style is useful when you're working with limited space and you expect people to make specific date and time selections. The graphical style is useful when you want to give people the option of browsing through days in a calendar or selecting a range of dates, or when the look of a clock face is appropriate for your app.

**tvOS**  
Pickers are available in tvOS with SwiftUI.

**visionOS**  
No additional considerations for visionOS.

**watchOS**  
Pickers display lists of items that people navigate using the Digital Crown, which helps people manage selections in a precise and engaging way.

A picker can display a list of items using the wheels style. watchOS can also display date and time pickers using the wheels style.

You can configure a picker to display an outline, caption, and scrolling indicator.

For longer lists, the navigation link displays the picker as a button. When someone taps the button, the system shows the list of options. The person can also scrub through the options using the Digital Crown without tapping the button.

### Related Components

- [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons) - Alternative for short lists
- [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables) - Alternative for very large sets of items

### Developer Documentation

- [Picker](https://developer.apple.com/documentation/swiftui/picker) - SwiftUI
- [UIDatePicker](https://developer.apple.com/documentation/uikit/uidatepicker) - UIKit
- [UIPickerView](https://developer.apple.com/documentation/uikit/uipickerview) - UIKit
- [NSDatePicker](https://developer.apple.com/documentation/appkit/nsdatepicker) - AppKit
- [DatePicker](https://developer.apple.com/documentation/swiftui/datepicker) - SwiftUI (watchOS)
- [navigationLink](https://developer.apple.com/documentation/swiftui/navigationlink) - SwiftUI (watchOS)

## Changelog

### June 5, 2023
- Updated guidance for using pickers in watchOS.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/pickers)*