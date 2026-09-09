# Media Intents

Resolve Siri audio-search requests to playable content in your app.

**Framework platforms:** iOS 27.0+ | iPadOS 27.0+ | Mac Catalyst 27.0+ | macOS 27.0+ | tvOS 27.0+ | visionOS 27.0+ | watchOS 27.0+

## Overview

Media Intents supplies `AudioSearch`, which carries the system's interpretation of an audio request. [App Intents](AppIntents.md) delivers it to your query and returns matching entities to Siri. Your app remains responsible for searching its catalog and implementing authorized playback.

This is not an audio-analysis API; see [Music Understanding](MusicUnderstanding.md) for analysis. It is also not a declaration that every [SiriKit](SiriKit.md) or [SiriKit Cloud Media](SiriKitCloudMedia.md) integration has been removed.

## Topics

### Search and resolution

- [`AudioSearch`](https://developer.apple.com/documentation/mediaintents/audiosearch.md) — Inspect request criteria and search metadata.
- [`AudioSearch.Criteria`](https://developer.apple.com/documentation/mediaintents/audiosearch/criteria-swift.enum.md) — Handle a `searchQuery`, a set of `url` values, or an `unspecified` request.
- [Responding to audio search and playback requests](https://developer.apple.com/documentation/mediaintents/responding-to-audio-search-and-playback-requests.md) — Implement the complete query-to-playback flow.

### App Intents integration

1. Represent songs, albums, or artists as app entities with matching [audio-domain schemas](https://developer.apple.com/documentation/appintents/app-schema-domain-audio.md).
2. Implement [`IntentValueQuery.values(for:)`](https://developer.apple.com/documentation/appintents/intentvaluequery/values(for:).md) with an `AudioSearch` input and return matching playable entities.
3. Resolve explicit queries against your catalog, validate media URLs, and supply appropriate recommendations for unspecified requests. Do not treat a URL or natural-language match as authorization.
4. Implement an app intent matching [`AppSchema.AudioIntent.playAudio`](https://developer.apple.com/documentation/appintents/appschema/audiointent/playaudio.md) to perform playback for the selected content.

## Failure handling and validation

Keep normal in-app search and playback available when Siri, the region, or an OS 27 API is unavailable. Distinguish no matches from offline catalog access, unavailable subscriptions, and denied playback. Preserve existing supported SiriKit paths while verifying migration.

Use [App Intents Testing](AppIntentsTesting.md) for query results and entity transfer, and [XCTest](XCTest.md)/[XCUIAutomation](XCUIAutomation.md) for the resulting app behavior. Test ambiguous queries, stale identifiers, invalid URLs, unspecified requests, and unavailable content—not only one successful song request.

**Availability:** `AudioSearch`'s [versioned DocC metadata](https://developer.apple.com/tutorials/data/documentation/mediaintents/audiosearch.json) confirms Mac Catalyst 27.0+, despite the unversioned entry in its Markdown export. Framework availability does not guarantee Siri support for every runtime or region.

*Source: [Media Intents](https://developer.apple.com/documentation/mediaintents.md).*
