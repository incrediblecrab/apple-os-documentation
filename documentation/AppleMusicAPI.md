# Apple Music API

Integrate streaming music with catalog and personal content.

**Platforms:** Apple Music 1.0+

## Overview

Use Apple Music API to access information about media in the Apple Music Catalog and a user's personal iCloud Music Library.

Apple Music Catalog includes all resources available in Apple Music.

iCloud Music Library contains only those resources the user adds to their personal library. For example, it contains items from Apple Music, songs purchased from iTunes Store, and imports from discs and other apps. This library can include content that's not in the Apple Music Catalog.

Use this API to retrieve information about albums, songs, artists, playlists, music videos, Apple Music stations, ratings, charts, recommendations, and the user's most-recently played content. With proper authorization from the user, you can also create or modify playlists and apply ratings to the user's content.

**Note:** Use the Apple Music Feed to access the Apple Music Catalog in bulk.

## Topics

### Essentials
- [Generating Developer Tokens](https://developer.apple.com/documentation/applemusicapi/generating_developer_tokens) - Generate a developer token needed to make requests to Apple Music API.
- [User Authentication for MusicKit](https://developer.apple.com/documentation/musickit/user_authentication_for_musickit) - Authenticate requests for user data using the Music User Token.
- [Handling Requests and Responses](https://developer.apple.com/documentation/applemusicapi/handling_requests_and_responses) - Write a request and handle responses from the API.
- [Handling Resource Representation and Relationships](https://developer.apple.com/documentation/applemusicapi/handling_resource_representation_and_relationships) - Fetch resources with extended attributes and included relationships and relationship views.
- [Storefronts and Localization](https://developer.apple.com/documentation/applemusicapi/storefronts_and_localization) - Pick a region-specific geographic location from which to retrieve catalog information, or retrieve information from the user's personal library.
- [Common Objects](https://developer.apple.com/documentation/applemusicapi/common_objects) - Understand the common JSON objects that framework responses contain.
- [Managing Content Ratings, Alternate Versions, and Equivalencies](https://developer.apple.com/documentation/applemusicapi/managing_content_ratings_alternate_versions_and_equivalencies) - Handle multiple and alternate versions of content.
- [Fetching Resources by Page](https://developer.apple.com/documentation/applemusicapi/fetching_resources_by_page) - Use pagination to fetch the next set of objects.

### Albums, Artists, Songs, and Videos
- [Albums](https://developer.apple.com/documentation/applemusicapi/albums) - Get an album's name, artist, list of tracks, artwork, release date, and recording information, and add new albums to the user's library.
- [Artists](https://developer.apple.com/documentation/applemusicapi/artists) - Get information about an artist, including the content they created and references to them in playlists and radio stations.
- [Songs](https://developer.apple.com/documentation/applemusicapi/songs) - Get information about a particular song, including the artist who created it and the album on which it appeared.
- [Music Videos](https://developer.apple.com/documentation/applemusicapi/music_videos) - Get information about a music video, including the artist who created it and the associated album, and add new videos to the user's library.

### Playlists and Stations
- [Playlists](https://developer.apple.com/documentation/applemusicapi/playlists) - Get the contents of playlists, add new playlists to the user's library, and add tracks to an existing playlist.
- [Apple Music Stations](https://developer.apple.com/documentation/applemusicapi/apple_music_stations) - Get information about streaming content offered by Apple Music.

### Search
- [Search](https://developer.apple.com/documentation/applemusicapi/search) - Search for albums, songs, artists, and other information in the user's personal library or the Apple Music Catalog.

### Ratings, Genres, and Charts
- [Ratings](https://developer.apple.com/documentation/applemusicapi/ratings) - Get and set ratings for albums, songs, playlists, music videos, and stations.
- [Music Genres](https://developer.apple.com/documentation/applemusicapi/music_genres) - Get information about the genres of the user's music or items in the Apple Music Catalog.
- [Charts](https://developer.apple.com/documentation/applemusicapi/charts) - Get chart information that shows the popularity of albums, songs, and music videos.

### Activities, Curators, and Record Labels
- [Activities](https://developer.apple.com/documentation/applemusicapi/activities) - Get request and response activities associated with the Apple Music Catalog.
- [Curators](https://developer.apple.com/documentation/applemusicapi/curators) - Get information about the person who curated a playlist or station.
- [Record Labels](https://developer.apple.com/documentation/applemusicapi/record_labels) - Get information on record labels in the Apple Music Catalog.

### Adding a resource to favorites
- [Add resource to favorites](https://developer.apple.com/documentation/applemusicapi/add_resource_to_favorites) - Add the user's resource to favorites.

### Getting a user's replay data
- [Get the user's replay data](https://developer.apple.com/documentation/applemusicapi/get_the_user_s_replay_data) - Fetch the user's replay data for the latest eligible year.

### Recommendations and history
- [Recommendations](https://developer.apple.com/documentation/applemusicapi/recommendations) - Get music recommendations based on the user's library and purchase history.
- [History](https://developer.apple.com/documentation/applemusicapi/history) - Get historical information about the songs and stations the user played recently.

### Fetching Multiple Resource Types
- [Get Multiple Catalog Resources Using Resource-Typed ID Parameters](https://developer.apple.com/documentation/applemusicapi/get_multiple_catalog_resources_using_resource-typed_id_parameters) - Fetch one or more catalog resources by using their identifiers.
- [Get Multiple Library Resources Using Resource-Typed ID Parameters](https://developer.apple.com/documentation/applemusicapi/get_multiple_library_resources_using_resource-typed_id_parameters) - Fetch one or more library resources by using their identifiers.

### Endpoints
- [Placeholder Endpoint to Test Connectivity](https://developer.apple.com/documentation/applemusicapi/placeholder_endpoint_to_test_connectivity)
- [Get a User's Storefront](https://developer.apple.com/documentation/applemusicapi/get_a_user_s_storefront) - Fetch a storefront for a specific user.

### Dictionaries
- **AlbumPeriodSummaries** - The album for the period summary.
- **ArtistPeriodSummaries** - The artist for the period summary.
- **Artwork** - An object that represents artwork.
- **DescriptionAttribute** - An object that represents a description attribute.
- **EditorialNotes** - An object that represents a notes attribute.
- **LangageTagResponse** - The response to a language tag request.
- **MusicSummaries** - The music for the period summary.
- **MusicSummariesResponse**
- **PaginatedResourceCollectionResponse** - A response object composed of paginated resource objects for the request.
- **PlayParameters** - An object that represents play parameters for resources.
- **Preview** - An object that represents a preview for resources.
- **RelationshipResponse** - The response for a direct resource relationship fetch.
- **RelationshipViewResponse** - The response for a direct resource view fetch.
- **SongPeriodSummaries** - The song for the period summary.
- **StorefrontsResponse** - The response to a storefront request.
- **View** - A to-one or to-many relationship view from one resource object to others representing interesting associations.

### See Also
- [Media Player](https://developer.apple.com/documentation/mediaplayer) - Find and play songs, audio podcasts, audio books, and more from within your app.
- [StoreKit](https://developer.apple.com/documentation/storekit) - Support In-App Purchases and interactions with the App Store.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AppleMusicAPI)*