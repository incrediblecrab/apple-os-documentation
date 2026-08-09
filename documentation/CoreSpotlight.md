# Core Spotlight

Add search capabilities to your app, and index your content so people can find it from Spotlight and Safari.

**Platforms:** iOS 9.0+ | iPadOS 9.0+ | Mac Catalyst 13.0+ | macOS 10.13+ | visionOS 1.0+

## Overview

Help people access activities and items within your app by adding details about those items to a Core Spotlight index. The framework provides APIs to add your content to an index, and search for items in that index. You decide what content makes sense to index, but typically you index anything that someone might look for in your app. For example, you might index photos, contacts, the items someone purchased, or data they see in your interface. You can then use Core Spotlight to search for your indexed content and display those results in your app.

Your app is responsible for indexing your app's content and maintaining those indexes. You can index content when your app runs, or provide an app extension to index content when the system requests it. You can index any content your app manages, including files and other content that your app isn't currently displaying. The indexes you create using Core Spotlight remain on device, and are private to the owner of the device. Devices don't share indexed data with Apple, or synchronize that data with the person's other devices.

In addition to indexing content, iOS provides additional strategies for making your app's content searchable:

- Use the search-related properties of NSUserActivity to add items to the on-device index, with the option to identify the items as eligible for public indexing. Learn more about NSUserActivity in Index Activities and Navigation Points.

- Use web markup to index content on your web server in Apple's server-side index, which makes the data available to all iOS users in Spotlight and Safari search results. For more information, see Mark Up Web Content in App Search Programming Guide.

## What's New in the OS 27 SDK

App Intents entity schemas can contribute app content to Spotlight's semantic index. On macOS Golden Gate 27, Siri AI is built into Spotlight with rebuilt search infrastructure for natural-language queries, plus an "Ask Siri" escalation path for complex queries.

## Topics

### Essentials
- [Adding your app's content to Spotlight indexes](https://developer.apple.com/documentation/corespotlight/adding_your_app_s_content_to_spotlight_indexes) - Create a description for your app's content and add it to a Spotlight index to make it searchable.
- [Enabling Apple Intelligence summarization and prioritization](https://developer.apple.com/documentation/corespotlight/enabling_apple_intelligence_summarization_and_prioritization) - Summarize and prioritize app content using Spotlight extensions.

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
- [Regenerating your app's indexes on demand](https://developer.apple.com/documentation/corespotlight/regenerating_your_app_s_indexes_on_demand) - Create an app extension to maintain your app's indexes and regenerate them as needed.
- **CSIndexExtensionRequestHandler** - An interface that implements an index-maintenance app extension.
- **CSImportExtension** - An object that provides searchable attributes for file types that the app supports.

### Queries
- [Building a search interface for your app](https://developer.apple.com/documentation/corespotlight/building_a_search_interface_for_your_app) - Add a search interface to your app to execute Spotlight queries and offer suggested text completions.
- [Searching for information in your app](https://developer.apple.com/documentation/corespotlight/searching_for_information_in_your_app) - Search for app-specific content and refine search results using predicates and filters.
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

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreSpotlight)*