# Searching

People use various search techniques to find content on their device, within an app, and within a document or file.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

To search for content within an app, people generally expect to use a search field. When it makes sense, you can personalize the search experience by using what you know about how people interact with your app. For example, you might display recent searches, search suggestions, completions, or corrections based on terms people searched earlier in your app.

In some cases, people appreciate the ability to scope a search or filter the results. For example, people might want to search for items by specifying attributes like creation date, file size, or file type. For guidance, see Scope controls and tokens. You can also help people find content within an open document or file by implementing ways to find content in a window or page in your iOS, iPadOS, or macOS app.

In iOS, iPadOS, and macOS, Spotlight helps people find content across all apps in the system and on the web. When you index and provide information about your app's content, people can use Spotlight to find content your app contains without opening it first. For guidance, see Systemwide search.

For discovery outside your app, [App Intents](https://developer.apple.com/documentation/appintents) can describe relevant actions and entities for system experiences such as Spotlight, Siri, and Shortcuts. Choose the documented integration for each entrypoint rather than assuming an entity is automatically indexed everywhere.

## Topics

### Best Practices

- **Make search prominent when it is important** - Apple's examples include dedicated search tabs in Photos and Apple TV, and a bottom-toolbar search field in Notes.

- **Provide a clear primary search location** - Aim to let people find the app's content from one place. A local search can still help in distinct sections, such as filtering songs and albums in Music.

- **Use descriptive placeholder text** - Clarify the searchable content when its scope might otherwise be unclear.

- **Display current search scope clearly** - Use a descriptive placeholder text, a scope control, or a title to help reinforce what someone is currently searching. For example, in the Mail app there is always a clear reference to the mailbox someone is searching.

- **Provide search suggestions** - When you display a person's recent searches or offer search suggestions both before and while they're typing, you can help people search faster and type less. For developer guidance, see [searchSuggestions(_:)](https://developer.apple.com/documentation/swiftui/view/searchsuggestions(_:)).

- **Consider privacy for search history** - People might not appreciate having their search history appear where others might see it. Depending on the context, consider providing other ways to narrow the search instead. If you do show search history, provide a way for people to clear it if they want.

### Systemwide Search

- **Make content searchable in Spotlight** - You can share content with Spotlight by making it indexable and specifying descriptive attributes known as metadata. Spotlight extracts, stores, and organizes this information to allow for fast, comprehensive searches.

- **Define metadata for custom file types** - A [CSImportExtension](https://developer.apple.com/documentation/corespotlight/csimportextension) supplies searchable attributes through a Spotlight File Import extension. Its developer documentation explicitly says these extensions provide no functionality on macOS: use a Spotlight importer plug-in there instead.

- **Offer advanced file-search capabilities** - For example, you might include a button that instantly initiates a Spotlight search based on the current selection. You might then display a custom view that presents the search results or a filtered subset of them.

- **Use system-provided open and save views** - The system-provided open and save views generally include a built-in search field that people can use to search and filter the entire system. For related guidance, see [File management](https://developer.apple.com/design/human-interface-guidelines/file-management).

- **Implement Quick Look generator for custom file types** - A Quick Look generator helps Spotlight and other apps show previews of your documents. For developer guidance, see [Quick Look](https://developer.apple.com/documentation/quicklook).

### Platform Considerations

No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.

### Related Components

- [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields) - UI component for search input

### Developer Documentation

- [Adding your app's content to Spotlight indexes](https://developer.apple.com/documentation/corespotlight/adding-your-app-s-content-to-spotlight-indexes) - Core Spotlight

### Videos

- [Design intuitive search experiences](https://developer.apple.com/videos/play/wwdc2026/292)

## Changelog

### June 9, 2025
- Updated best practices with general guidance from Search fields, and reorganized guidance for systemwide search.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/searching)*
