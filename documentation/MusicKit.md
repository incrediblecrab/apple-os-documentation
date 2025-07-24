# MusicKit

Integrate your app with Apple Music.

**Platforms:** iOS 15.0+ | iPadOS 15.0+ | Mac Catalyst 15.0+ | macOS 12.0+ | tvOS 15.0+ | visionOS 1.0+ | watchOS 8.0+

## Overview

Use MusicKit to integrate your app with Apple Music API, a web service you use to access information about music items in the Apple Music catalog. Using MusicKit, you can more easily build apps that tie into Apple Music.

The framework provides a model layer for accessing music items in Swift, as well as playback support so you can add music to your app. Additionally, it provides some related user interface elements, such as a view to display images that correspond to artwork for a music item, or a way to present music subscription offers to users who may not have an active Apple Music subscription.

**Important:** Users must grant permission for your app to access their music data. Add the `NSAppleMusicUsageDescription` key to your app's Info.plist file, and include a description of how you intend to use the user's media. If this key isn't present, the system terminates your app when it tries to access the user's music.

Request permission for your app to use MusicKit with **MusicAuthorization**. Check specific capabilities for the current **MusicSubscription** to ensure your music-related functionality is available to the user. Find music items using a search term with **MusicCatalogSearchRequest**, or find music items using a filter with **MusicCatalogResourceRequest**. Play music in your app with one of the two music players that MusicKit offers. Allow the user to begin a free trial for Apple Music from within your app by presenting a music subscription offer.

You can load content from an arbitrary Apple Music API endpoint with **MusicDataRequest** to take further advantage of additional functionality available in Apple Music API.

## Topics

### Essentials
- [Using Automatic Developer Token Generation for Apple Music API](https://developer.apple.com/documentation/musickit/using_automatic_developer_token_generation_for_apple_music_api) - Enable your app's integration with the MusicKit App Service in the developer portal
- [Using MusicKit to Integrate with Apple Music](https://developer.apple.com/documentation/musickit/using_musickit_to_integrate_with_apple_music) - Find an album in Apple Music that corresponds to a CD in a user's collection, and present the information for the album
- **NSAppleMusicUsageDescription** - A message that tells people why the app is requesting access to their media library

### Music Items
A set of value types represents each kind of music item.

- **Album** - A music item that represents an album
- **Artist** - A music item that represents an artist
- **Curator** - A music item that represents a curator
- **Genre** - A music item that represents a genre
- **MusicVideo** - A music item that represents a music video
- **Playlist** - A music item that represents a playlist
- **RadioShow** - A music item that represents a radio show
- **RecordLabel** - A music item that represents a record label
- **Song** - A music item that represents a song
- **Station** - A music item that represents a station
- **Track** - A music item that represents a track

### Music Item Attributes
A set of structured attributes for music items.

- **ContentRating** - The rating of the content that potentially plays while playing a resource
- **EditorialNotes** - An object that represents editorial notes
- **PreviewAsset** - An object that represents a preview for resources

### Catalog Search
The catalog search request allows your app to find music items in the Apple Music catalog.

- **MusicCatalogSearchRequest** - A request that your app uses to fetch items from the Apple Music catalog using a search term
- **MusicCatalogSearchResponse** - An object that contains results for a catalog search request
- **MusicCatalogSearchable** - A protocol for music items that your app can fetch by using a catalog search request

### Resource Loading Using Filters
The catalog resource request allows your app to load items using a specific filter.

- **MusicCatalogResourceRequest** - A request that your app uses to fetch items from the Apple Music catalog using a filter
- **MusicCatalogResourceResponse** - An object that contains results for a catalog resource request
- **AlbumFilter** - Album properties your app uses as a filter for a catalog resource request
- **ArtistFilter** - Artist properties your app uses as a filter for a catalog resource request
- **CuratorFilter** - Curator properties your app uses as a filter for a catalog resource request
- **GenreFilter** - Genre properties your app uses as a filter for a catalog resource request
- **MusicVideoFilter** - Music video properties your app uses as a filter for a catalog resource request
- **PlaylistFilter** - Playlist properties your app uses as a filter for a catalog resource request
- **RadioShowFilter** - Radio Show properties your app uses as a filter for a catalog resource request
- **RecordLabelFilter** - The set of record label properties your app uses as a filter for a catalog resource request
- **SongFilter** - Song properties your app uses as a filter for a catalog resource request
- **StationFilter** - The set of station properties your app uses as a filter for a catalog resource request
- **FilterableMusicItem** - A declaration of the associated type that contains the set of music item properties your app uses as a filter for a catalog resource request

### General Purpose Data Request
- **MusicDataRequest** - A request for loading data from an arbitrary Apple Music API endpoint
- **MusicDataResponse** - An object containing results for a data request

### Playback
- **ApplicationMusicPlayer** - An object your app uses to play music in a way that doesn't affect the Music app's state
- **SystemMusicPlayer** - An object your app uses to play music by controlling the Music app's state
- **MusicPlayer** - An object your app uses to play music
- **PlayableMusicItem** - A set of properties that a music player uses to initiate playback for a music item
- **PlayParameters** - An opaque object that represents parameters to initiate playback of a playable music item using a music player

### Artwork
- **Artwork** - An object that represents artwork for a music item
- **ArtworkImage** - A view that displays the image for a music item's artwork

### Authorization
Before you can use any of the functionality of the framework, you need to request the user's informed consent for your app to access their music data.

- **MusicAuthorization** - A type that allows you to request the user's informed consent for your app to access their music data

### Apple Music Subscription
- **MusicSubscription** - A representation of the current state of the user's subscription to Apple Music
- **MusicSubscriptionOffer** - A type for grouping other types for showing subscription offers for Apple Music

### Token Management
The framework manages tokens for accessing Apple Music API automatically by default, but you can generate your own developer token by creating a class that inherits from the token provider type alias.

- **MusicTokenProvider** - An object that music requests use to access Apple Music API
- **MusicDeveloperTokenProvider** - A set of methods that music requests use to access Apple Music API
- **MusicUserTokenProvider** - A class that music requests use to fetch user tokens your app requires to access Apple Music API
- **MusicTokenRequestOptions** - Options that music requests pass into token provider methods to fetch a required token for accessing Apple Music API
- **MusicTokenRequestError** - An error that the token provider or music requests can throw upon requesting any token necessary for accessing Apple Music API
- **DefaultMusicTokenProvider** - The default token provider that music requests use to access Apple Music API

### Utility
- **MusicItem** - A protocol with basic requirements for music items
- **MusicItemID** - An object that represents a unique identifier for a music item
- **MusicItemCollection** - A collection of music items
- **MusicPropertyContainer** - A protocol for music items that allow loading additional properties that you can fetch asynchronously
- Various music property classes for managing relationships and attributes

### Music Library
- **MusicLibrary** - An object your app uses to access the user's music library

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MusicKit)*