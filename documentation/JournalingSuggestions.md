# Journaling Suggestions

Display a set of recent, personal events that inspire someone to contribute to your app's creative workflow.

**Platforms:** iOS 17.2+ | iPadOS 26.0+

## Overview

Journaling Suggestions provides a visual picker for iPhone apps and, from iPadOS 26, iPad apps. The [June 2025 update](https://developer.apple.com/documentation/updates/journalingsuggestions) explains that suggestions generated on a person's iPhone sync over iCloud to their iPad. The picker can display places they visited, people they connected with, photos, or music they listened to.

If your app facilitates personal writing, display the picker to provide people with ideas for their creative content. When someone chooses a suggestion from the picker, the system makes high-level details about the event available to your app. For example, a journaling app uses the details to display the beginning of a new journal entry about the selected suggestion.

To incorporate a suggestions picker (JournalingSuggestionsPicker) in your app, declare it using SwiftUI, and choose the text for a button that presents the picker.

For the picker to appear, the code signature needs [`com.apple.developer.journal.allow`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.journal.allow) with the string value `suggestions`; enable the Journaling Suggestions capability in Xcode. The system handles its own enrollment and selected-item sharing UI. The picker does not require a separate app-wide personal-data permission, and the app receives details only after the person chooses to share a suggestion.

**Note:** Mac apps built with Mac Catalyst ignore input if someone taps a suggestions picker button.

## Topics

### Essentials
- [Journaling Suggestions updates](https://developer.apple.com/documentation/updates/journalingsuggestions) - Learn about important changes in Journaling Suggestions.
- [Presenting the suggestions picker and processing a selection](https://developer.apple.com/documentation/journalingsuggestions/presenting-the-suggestions-picker-and-processing-a-selection) - Display the journaling suggestions picker and process a suggestion that someone chooses.
- **com.apple.developer.journal.allow** - The entitlement that enables an app to present the journaling suggestions picker.

### Implementation
- **JournalingSuggestionsPicker** - A view that lists different types of recent events in a person's life.
- **JournalingSuggestion** - High-level information about a suggestion that a person chooses in the journaling suggestions picker.
- **JournalingSuggestionAsset** - An interface for the content that the suggestions picker presents.

### Notifications

The notification configuration and presentation-token APIs begin at 26.0. Set [`JSNotificationURLFormat`](https://developer.apple.com/documentation/bundleresources/information-property-list/jsnotificationurlformat) to an appropriate universal-link format to make the app eligible for the person's **Open Notifications With** selection. A notification tap can supply a suggestion identifier for prepopulating the picker, not permission to bypass the picker. General reminder notifications may have no suggestion identifier.

- [Receiving journaling suggestions system notifications](https://developer.apple.com/documentation/journalingsuggestions/receiving-journaling-suggestions-from-system-notifications) - Register your app to receive journaling suggestions when a person taps a system notification.
- **JournalingSuggestionPresentationToken** - A container for a Journaling Suggestion identifier.
- **JournalingSuggestionsConfiguration** - A read-only view of the person's notification schedule in Settings, not an API to change that schedule.

## Privacy and failure handling

Treat picker cancellation or an unavailable suggestion as a normal outcome. [`content(forType:)`](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestion/content(fortype:)) has an asynchronous, nonthrowing declaration and returns an array of matching assets; it can be empty. Handle failures when loading the returned media, and do not assume every suggestion has every asset type.

A notification schedule of `.off` can also indicate incomplete setup or that this is not the person's preferred journal app, rather than only a deliberate notifications-off choice. The entitlement permits the picker workflow, not unrestricted access to personal events. These platform and privacy rules remain distinct from OS 27 SDK adoption.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/JournalingSuggestions)*
