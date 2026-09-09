# Apple TV Feed

Download bulk Apple TV catalog metadata for offline indexing and analysis.

**Availability:** Authorized web service, not an OS-specific SDK. Access requires participation in the Apple Services Performance Partners Program and the credentials Apple supplies through its partner portal.

**Status:** Reviewed September 8, 2026. Inclusion in this refresh does not imply introduction in OS 27 or a tvOS deployment requirement.

## Overview

Apple TV Feed exports metadata for movies, shows, seasons, episodes, and sporting events. The catalog refreshes every 24 hours and is distributed as Parquet data. It suits batch ingestion and discovery indexes, not real-time playback control.

Metadata access is not access to video streams or a viewer's subscription. Apple's documentation examples use JSON to explain the records, but the downloaded feed files are Parquet.

## Topics

### Access and ingestion

- [Generating developer tokens](https://developer.apple.com/documentation/appletvfeed/generating-developer-tokens) — Sign and authorize requests using the partner-provided Team ID, Key ID, and private key.
- [Requesting a feed export](https://developer.apple.com/documentation/appletvfeed/requesting-a-feed-export) — Resolve the current export, enumerate its parts, and download them.
- [Interpreting responses](https://developer.apple.com/documentation/appletvfeed/interpreting-responses) — Distinguish resource collections from authorization and request errors.
- [Apple's feed examples](https://github.com/apple/music-feed-examples) — The Apple TV Feed overview points to these Music Feed scripts for the shared export/download workflow.

### Catalog records

- [Movie](https://developer.apple.com/documentation/appletvfeed/movie)
- [TvShow](https://developer.apple.com/documentation/appletvfeed/tvshow)
- [TvSeason](https://developer.apple.com/documentation/appletvfeed/tvseason)
- [TvEpisode](https://developer.apple.com/documentation/appletvfeed/tvepisode)
- [SportingEvent](https://developer.apple.com/documentation/appletvfeed/sportingevent)

## Export workflow

The service root is `https://api-feeds.tv.apple.com/v1`.

1. Request `/feed/{feedId}/latest`, where `feedId` is `movies`, `tv-shows`, `tv-seasons`, `tv-episodes`, or `sporting-events`.
2. Retain the returned export identifier. Enumerate `/feed/exports/{id}/parts`, using the documented `limit` and `offset` pagination.
3. Download each part from its returned `exportLocation`. These URLs expire; retrieve fresh links when necessary instead of treating them as permanent asset addresses.
4. Read the files with a Parquet-capable tool. Track which export and parts have completed before replacing a usable local index.

Keep private signing keys on a trusted service, not in a distributed client. Developer tokens use ES256 and the `Authorization: Bearer` header as described in Apple's token guide.

## Failure and applicability guidance

- **401/403:** Check token validity and the authorized partner credentials. Repeating the same unauthorized request is not an ingestion recovery strategy.
- **429:** Lower the request rate; Apple's token guide documents temporary throttling when a token exceeds the service's rate allowance.
- **404 or empty data:** A missing single resource and an empty collection have different documented responses. Do not assume every successful response contains a record.
- **Partial download or server error:** Retain the last complete local dataset while retrying failed parts. Do not combine parts from different export identifiers by accident.
- **Freshness:** A daily export is not a live availability signal. Preserve locale and storefront distinctions in records rather than assuming one title, price, or URL applies everywhere.

## Sources

- [Apple TV Feed reference](https://developer.apple.com/documentation/appletvfeed)
- [Requesting a feed export](https://developer.apple.com/documentation/appletvfeed/requesting-a-feed-export)
- [Generating developer tokens](https://developer.apple.com/documentation/appletvfeed/generating-developer-tokens)
- [Interpreting responses](https://developer.apple.com/documentation/appletvfeed/interpreting-responses)
