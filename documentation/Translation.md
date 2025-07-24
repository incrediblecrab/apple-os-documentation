# Translation

Translate text in your app from one language to another.

**Platforms:** iOS 17.4+ | iPadOS 17.4+ | macOS 14.4+

## Overview

Offer in-app translations with the **Translation** framework. You can use the built-in UI and let the system offer a translation to users on your behalf. Or you can use the framework to customize the translation experience.

To offer the built-in system translation experience, anchor the **translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)** view modifier to the SwiftUI view containing the text to translate. Set **isPresented** to **true** when you want to the built-in system translation UI to appear. Pass the text to translate to the **text** parameter.

To customize the translation experience use one of the translation tasks such as **translationTask(_:action:)**. These functions provides you with a **TranslationSession** that you can use to translate strings of text one at a time, or in a batch. You can check language availability before offering a translation with the **LanguageAvailability** class.

## Topics

### Essentials
- [Translating text within your app](https://developer.apple.com/documentation/translation/translating_text_within_your_app) - Display simple system translations and create custom translation experiences.
- **translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)** - Presents a translation popover when a given condition is true.
- **translationTask(_:action:)** - Adds a task to perform before this view appears or when the translation configuration changes.
- **translationTask(source:target:action:)** - Adds a task to perform before this view appears or when the specified source or target languages change.
- **TranslationSession** - A class that performs translations between a pair of languages.

### Availability
- **LanguageAvailability** - A check for language support and status.

### Errors
- **TranslationError** - Error codes describing why the framework can't perform a translation.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Translation)*