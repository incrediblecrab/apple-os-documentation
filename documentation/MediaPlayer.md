# Media Player

Find and play songs, audio podcasts, audio books, and more from within your app.

**Platforms:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 13.1+ | macOS 10.12.1+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 5.0+

## Overview

Use Media Player for media-library queries and playback interfaces that complement the separate MusicKit framework and support older deployment targets. If your app incorporates music, you can use this framework to search for audio content, such as songs, podcasts, and books, in the user's library. You can then play that content directly or ask the system Music app to play it. For example, a game might give users the option to play their own music while completing a particular game level.

**Important:** To protect user privacy, users need to grant permission for your app to access their media library. Add the NSAppleMusicUsageDescription key to your app's Info.plist file, and include a description of how you intend to use the user's library. If this key isn't present, the system terminates your app when it tries to access the user's library.

To play content from the user's library using the Media Player framework, use one of the built-in MPMusicPlayerController objects:

- An **application player** plays music locally within your app. Use this player when you want greater control over the audio you play for the user. This player doesn't change the state of the built-in Music app.

- The **system player** employs the Music app to play audio on your behalf. Use this player when you want audio to continue playing even when the user switches away from your app.

Use media queries to retrieve the items you want to play and to populate the selected player's queue. Apple Music library and playback operations also depend on authorization and the person's subscription capabilities. When appropriate, present a subscription offer; being a nonsubscriber does not by itself establish free-trial eligibility.

Media Player is not an in-app video renderer. For app-managed video playback, use AVFoundation with a usable media URL or asset. [`MPMediaItem.assetURL`](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/asseturl) is optional and can supply a URL for an AVFoundation object; handle a missing URL rather than passing an `MPMediaItem` directly to a player. The system music player has a separate path for playing video through system apps.

**Important:** Only use this framework to facilitate playback of the user's audio content within your app. Don't gather information about the user's audio content for any other purpose. For more information about accessing Apple Music content, see the App Store review guidelines.

## OS 27 Now Playing migration

[Now Playing](NowPlaying.md) provides an observable-model API for publishing metadata and playback commands on OS 27. It is not a replacement for media-library authorization or every Media Player playback API.

Apple's [Now Playing overview](https://developer.apple.com/documentation/nowplaying) warns that combining the new framework with `MPNowPlayingInfoCenter` and `MPRemoteCommandCenter` for local playback produces undefined behavior. Choose one publication system for local playback in the app, not separately for each track or player. Keep a separate legacy branch for older systems rather than registering both.

Remote-session publication has narrower availability than the new local session API. Consult the individual types before adopting it on macOS, tvOS, visionOS, or watchOS.

## Topics

### Essentials

- **NSAppleMusicUsageDescription** - A message that tells people why the app is requesting access to their media library.

### Built-in Music Playback

- [Playing audio using the built-in music player](https://developer.apple.com/documentation/mediaplayer/playing-audio-using-the-built-in-music-player) - Create a media player inside your app to play audio from the user's media library.
- **MPMusicPlayerController** - An object that plays audio media items from the device's Music app library.
- **MPMediaPlayback** - A protocol that defines the interface for controlling audio media playback.
- **MPSystemMusicPlayerController** - A protocol for playing videos in the Music app.

### Media Library Synchronization

- **MPMediaLibrary** - An object that represents the state of synced media items on a device.

### Media Item Queries

- [Using filters to create specialized queries](https://developer.apple.com/documentation/mediaplayer/using-filters-to-create-specialized-queries) - Add a filter set to a query before populating a music player queue.
- **MPMediaQuery** - A query that specifies a set of media items from the device's media library using a filter and a grouping type.
- **MPMediaQuerySection** - A range of media items or media item collections from within a media query.
- **MPMediaPropertyPredicate** - A set of predicates for defining a filter in a media query.
- **MPMediaPredicate** - An abstract class that defines classes for filtering media in a media query.

### Media Player Queues

- **MPMusicPlayerControllerQueue** - An immutable queue containing the media items to play.
- **MPMusicPlayerControllerMutableQueue** - A mutable queue containing the media items to play.
- **MPMusicPlayerApplicationController** - A media player object that you use to revise the queue that's currently playing.
- **MPMusicPlayerMediaItemQueueDescriptor** - A set of properties and methods for modifying audio media items in the player's media queue.
- **MPMusicPlayerStoreQueueDescriptor** - A set of properties and methods for modifying items, based on their store identifier, in the player's queue.
- **MPMusicPlayerPlayParametersQueueDescriptor** - A set of properties and methods for modifying how to play items, based on play parameters the framework returns.
- **MPMusicPlayerQueueDescriptor** - The abstract base class for audio media item and store queue descriptors.

### Media Items and Playlists

- [Providing animated artwork for media items](https://developer.apple.com/documentation/mediaplayer/providing-animated-artwork-for-media-items) - Display animated artwork for your app's media in system views, such as the lock screen, by providing video assets through your now playing info.
- **MPMediaItem** - A collection of properties that represents a single item in the media library.
- **MPMediaItemArtwork** - A graphical image, such as music album cover art, associated with a media item.
- **MPMediaItemAnimatedArtwork** - An animated image, such as an animated music album cover art, for a media item.
- **MPMediaItemCollection** - A sorted set of media items from the media library.
- **MPMediaPlaylist** - A playable collection of related media items.
- **MPMediaPlaylistCreationMetadata** - A set of attributes for describing a playlist when creating it.
- **MPMediaEntity** - The abstract superclass for media items, media item collections, and media playlist instances.

### Media Player User Interface

- [Displaying a media picker from your app](https://developer.apple.com/documentation/mediaplayer/displaying-a-media-picker-from-your-app) - Let users choose the music they want to play by displaying a media picker interface from within your app.
- **MPMediaPickerController** - A specialized view controller that provides a graphical interface for selecting media items.
- **MPVolumeView** - A slider control for setting the system audio output volume, and a button for choosing the audio output route.

### Now Playing Information

- [Provide information about the current track](https://developer.apple.com/documentation/mediaplayer#Now-Playing-information)
- [Becoming a now playable app](https://developer.apple.com/documentation/mediaplayer/becoming-a-now-playable-app) - Ensure your app is eligible to become the Now Playing app by adopting best practices for providing Now Playing info and registering for remote command center actions.
- **MPNowPlayingSession** - An object that manages Now Playing information and remote commands for multiple players.
- **MPNowPlayingInfoCenter** - An object for setting the Now Playing information for media that your app plays.
- **MPNowPlayingInfoLanguageOption** - A set of interfaces for setting the language option for the Now Playing item.
- **MPNowPlayingInfoLanguageOptionGroup** - A grouped set of language options where only a single language option can be active at a time.
- **Language option characteristic constants** - The constants for defining language characteristics.

### External Player and System Event Handling
Support playback controls on external media players or system-provided controls.
- [Handling external player events notifications](https://developer.apple.com/documentation/mediaplayer/handling-external-player-events-notifications) - Handle events for external media players.
- [Remote command center events](https://developer.apple.com/documentation/mediaplayer/remote-command-center-events) - Set up the remote command center to handle media player events.
- [Track navigation events](https://developer.apple.com/documentation/mediaplayer/track-navigation-events) - Respond to requests to change which part of a media item plays.
- [Media playback mode events](https://developer.apple.com/documentation/mediaplayer/media-playback-mode-events) - Respond to changes in the way media items play.
- [Feedback and rating events](https://developer.apple.com/documentation/mediaplayer/feedback-and-rating-events) - Respond to incoming feedback and rating events.

### External Media Player Items

- [External media player items](https://developer.apple.com/documentation/mediaplayer#External-media-player-items) - Provide content and interact with external media players.
- **MPContentItem** - An object that contains the information for a displayed media item.

### Media Player Errors

- **MPError** - A structure that represents a framework error.
- **MPError.Code** - An enumeration that represents error codes for framework operations.
- **MPErrorDomain** - The Media Player framework error domain.

### Deprecated

- [Deprecated types](https://developer.apple.com/documentation/mediaplayer/deprecated-types) - Review deprecated symbols and avoid using them in your app.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MediaPlayer)*
