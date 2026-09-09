# Core Spotlight

Add search capabilities to your app, and index your content so people can find it from Spotlight and Safari.

**Platforms:** iOS 9.0+ | iPadOS 9.0+ | Mac Catalyst 13.0+ | macOS 10.13+ | visionOS 1.0+

## Overview

Help people access activities and items within your app by adding details about those items to a Core Spotlight index. The framework provides APIs to add your content to an index, and search for items in that index. You decide what content makes sense to index, but typically you index anything that someone might look for in your app. For example, you might index photos, contacts, the items someone purchased, or data they see in your interface. You can then use Core Spotlight to search for your indexed content and display those results in your app.

Your app is responsible for indexing your app's content and maintaining those indexes. You can index content when your app runs, or provide an app extension to index content when the system requests it. You can index any content your app manages, including files and other content that your app isn't currently displaying. The indexes you create using Core Spotlight remain on device, and are private to the owner of the device. Devices don't share indexed data with Apple, or synchronize that data with the person's other devices.

Spotlight File Import extensions do not provide functionality on macOS. For custom file types there, use a Spotlight importer plug-in; this is distinct from maintaining a Core Spotlight index.

In addition to indexing content, iOS provides additional strategies for making your app's content searchable:

- Use the search-related properties of NSUserActivity to add items to the on-device index, with the option to identify the items as eligible for public indexing. Learn more about NSUserActivity in Index Activities and Navigation Points.

- Use web markup to index content on your web server in Apple's server-side index, which makes the data available to all iOS users in Spotlight and Safari search results. For more information, see Mark Up Web Content in App Search Programming Guide.

## App Intents and semantic search

[App Intents](AppIntents.md) connects entities to system discovery, but adopting a schema is not the same as indexing every entity. Follow [Making app entities available in Spotlight](https://developer.apple.com/documentation/appintents/making-app-entities-available-in-spotlight.md) and keep indexed content current when records change or are deleted.

On supported OS 27 test destinations, [App Intents Testing](AppIntentsTesting.md) provides `AppEntityDefinition.spotlightQuery(_:)` to verify the entities actually returned by Spotlight. The member declares iOS, iPadOS, Mac Catalyst, macOS, and visionOS 27.0+, not tvOS or watchOS. Test missing, stale, and deleted records rather than inferring success from a system-search announcement.

## Topics

### Essentials
- [Adding your app's content to Spotlight indexes](https://developer.apple.com/documentation/corespotlight/adding-your-app-s-content-to-spotlight-indexes.md) - Create a description for your app's content and add it to a Spotlight index to make it searchable.
- [Generating summary and priority data for indexed items](https://developer.apple.com/documentation/corespotlight/generating-summary-and-priority-data-for-indexed-items.md) - Generate summaries for supported mail, message, and audio-transcript items; consult the article for priority-classification requirements.

### Searchable Items
- **CSSearchableItem** - The details of your app-specific content that someone might search for on their devices.
- **CSSearchableItemAttributeSet** - The detailed metadata for a searchable item.
- **CSCustomAttributeKey** - A key associated with a custom attribute for a searchable item.
- **CSLocalizedString** - An object that displays localized text in search results related to your app.
- **CSPerson** - An object that represents a person in the context of search results.

### Indexes
- **CSSearchableIndex** - An on-device index for your app's searchable content.
- **CSSearchableIndexDelegate** - A protocol that defines methods a delegate object or app extension uses to handle communication from the on-device index.

### Spotlight App Extensions
- [Regenerating your app's indexes on demand](https://developer.apple.com/documentation/corespotlight/regenerating-your-app-s-indexes-on-demand.md) - Create an app extension to maintain your app's indexes and regenerate them as needed.
- **CSIndexExtensionRequestHandler** - An interface that implements an index-maintenance app extension.
- **CSImportExtension** - An object that provides searchable attributes for file types that the app supports.

### Queries
- [Building a search interface for your app](https://developer.apple.com/documentation/corespotlight/building-a-search-interface-for-your-app.md) - Add a search interface to your app to execute Spotlight queries and offer suggested text completions.
- [Searching for information in your app](https://developer.apple.com/documentation/corespotlight/searching-for-information-in-your-app.md) - Search for app-specific content and refine search results using predicates and filters.
- **CSUserQuery** - A type you use to initiate searches from your interface and offer suggested text completions.
- **CSUserQueryContext** - The configuration details to apply to a user query.
- **CSSearchQuery** - A type you use to programmatically search the indexed app content.
- **CSSearchQueryContext** - The behavior configuration to use for a search query.
- **CSSuggestion** - The kind of suggestion to use in a query.

### Errors
- **CSIndexError** - Index errors returned by Core Spotlight.
- **CSSearchQueryError** - Search query errors returned by Core Spotlight.
- **CSIndex Errors** - Index error codes and error domain.
- **CSSearchQuery Errors** - Search query error codes and error domain.

### Version
- **CoreSpotlightAPIVersion** - The API version number for Core Spotlight.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreSpotlight)*
