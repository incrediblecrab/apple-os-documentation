# Journaling Suggestions

Display a set of recent, personal events that inspire someone to contribute to your app's creative workflow.

**Platforms:** iOS 17.2+ | iPadOS 26.0+ (Beta)

## Overview

Journaling Suggestions provides a visual picker interface for iPhone apps. The picker displays personal events that occur in someone's life, such as a place they visited, a person they connected with, a photo in their library, or a song that they play repeatedly.

If your app facilitates personal writing, display the picker to provide people with ideas for their creative content. When someone chooses a suggestion from the picker, the system makes high-level details about the event available to your app. For example, a journaling app uses the details to display the beginning of a new journal entry about the selected suggestion.

To incorporate a suggestions picker (JournalingSuggestionsPicker) in your app, declare it using SwiftUI, and choose the text for a button that presents the picker.

For the picker to appear, your app needs a special entitlement in your app's code signature. You don't need to ask for additional authorization because your app can't access the details for a suggestion until after a person chooses to share them by making a selection in the picker.

**Note:** Mac apps built with Mac Catalyst ignore input if someone taps a suggestions picker button.

## Topics

### Essentials
- [Journaling Suggestions updates](https://developer.apple.com/documentation/journalingsuggestions/journaling_suggestions_updates) - Learn about important changes in Journaling Suggestions.
- [Presenting the suggestions picker and processing a selection](https://developer.apple.com/documentation/journalingsuggestions/presenting_the_suggestions_picker_and_processing_a_selection) - Display the journaling suggestions picker and process a suggestion that someone chooses.
- **com.apple.developer.journal.allow** - The entitlement that enables an app to present the journaling suggestions picker.

### Implementation
- **JournalingSuggestionsPicker** - A view that lists different types of recent events in a person's life.
- **JournalingSuggestion** - High-level information about a suggestion that a person chooses in the journaling suggestions picker.
- **JournalingSuggestionAsset** - An interface for the content that the suggestions picker presents.

### Notifications
- [Receiving journaling suggestions system notifications](https://developer.apple.com/documentation/journalingsuggestions/receiving_journaling_suggestions_system_notifications) - Register your app to receive journaling suggestions when a person taps a system notification.
- **JournalingSuggestionPresentationToken** - A container for a Journaling Suggestion identifier. (Beta)
- **JournalingSuggestionsConfiguration** - The configuration for Journaling Suggestion notifications. (Beta)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/JournalingSuggestions)*