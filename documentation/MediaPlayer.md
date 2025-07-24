# Media Player

Find and play songs, audio podcasts, audio books, and more from within your app.

**Platforms:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 13.1+ | macOS 10.12.1+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 5.0+

## Overview

Use the Media Player framework, which is part of MusicKit, to control playback of the user's media from your app. If your app incorporates music, you can use this framework to search for audio content, such as songs, podcasts, and books, in the user's library. You can then play that content directly or ask the system Music app to play it. For example, a game might give users the option to play their own music while completing a particular game level.

**Important:** To protect user privacy, users need to grant permission for your app to access their media library. Add the NSAppleMusicUsageDescription key to your app's Info.plist file, and include a description of how you intend to use the user's library. If this key isn't present, the system terminates your app when it tries to access the user's library.

To play content from the user's library using the Media Player framework, use one of the built-in MPMusicPlayerController objects:

- An **application player** plays music locally within your app. Use this player when you want greater control over the audio you play for the user. This player doesn't change the state of the built-in Music app.

- The **system player** employs the Music app to play audio on your behalf. Use this player when you want audio to continue playing even when the user switches away from your app.

Use media queries to retrieve the items you want to play and to populate the queue for the media player you select. After a user gives your app permission to access their Apple Music account, it can add songs, create playlists, and play songs from Apple Music. If your app detects that the user isn't an Apple Music subscriber, it can offer a trial.

You can't play video media items directly using the Media Player framework. To play videos containing MPMediaItem objects, use an AVPlayer object from AVFoundation. The system player also provides a way to play video items using the system apps.

**Important:** Only use this framework to facilitate playback of the user's audio content within your app. Don't gather information about the user's audio content for any other purpose. For more information about accessing Apple Music content, see the App Store review guidelines.

## Topics

### Essentials
- **NSAppleMusicUsageDescription** - A message that tells people why the app is requesting access to their media library.

### Built-in Music Playback
- [Playing audio using the built-in music player](https://developer.apple.com/documentation/mediaplayer/playing_audio_using_the_built-in_music_player) - Create a media player inside your app to play audio from the user's media library.
- **MPMusicPlayerController** - An object that plays audio media items from the device's Music app library.
- **MPMediaPlayback** - A protocol that defines the interface for controlling audio media playback.
- **MPSystemMusicPlayerController** - A protocol for playing videos in the Music app.

### Media Library Synchronization
- **MPMediaLibrary** - An object that represents the state of synced media items on a device.

### Media Item Queries
- [Using filters to create specialized queries](https://developer.apple.com/documentation/mediaplayer/using_filters_to_create_specialized_queries) - Add a filter set to a query before populating a music player queue.
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
- [Providing animated artwork for media items](https://developer.apple.com/documentation/mediaplayer/providing_animated_artwork_for_media_items) - Display animated artwork for your app's media in system views, such as the lock screen, by providing video assets through your now playing info.
- **MPMediaItem** - A collection of properties that represents a single item in the media library.
- **MPMediaItemArtwork** - A graphical image, such as music album cover art, associated with a media item.
- **MPMediaItemAnimatedArtwork** - An animated image, such as an animated music album cover art, for a media item. (Beta)
- **MPMediaItemCollection** - A sorted set of media items from the media library.
- **MPMediaPlaylist** - A playable collection of related media items.
- **MPMediaPlaylistCreationMetadata** - A set of attributes for describing a playlist when creating it.
- **MPMediaEntity** - The abstract superclass for media items, media item collections, and media playlist instances.

### Media Player User Interface
- [Displaying a media picker from your app](https://developer.apple.com/documentation/mediaplayer/displaying_a_media_picker_from_your_app) - Let users choose the music they want to play by displaying a media picker interface from within your app.
- **MPMediaPickerController** - A specialized view controller that provides a graphical interface for selecting media items.
- **MPVolumeView** - A slider control for setting the system audio output volume, and a button for choosing the audio output route.

### Now Playing Information
- [Provide information about the current track](https://developer.apple.com/documentation/mediaplayer/now_playing_information)
- [Becoming a now playable app](https://developer.apple.com/documentation/mediaplayer/becoming_a_now_playable_app) - Ensure your app is eligible to become the Now Playing app by adopting best practices for providing Now Playing info and registering for remote command center actions.
- **MPNowPlayingSession** - An object that manages Now Playing information and remote commands for multiple players.
- **MPNowPlayingInfoCenter** - An object for setting the Now Playing information for media that your app plays.
- **MPNowPlayingInfoLanguageOption** - A set of interfaces for setting the language option for the Now Playing item.
- **MPNowPlayingInfoLanguageOptionGroup** - A grouped set of language options where only a single language option can be active at a time.
- **Language option characteristic constants** - The constants for defining language characteristics.

### External Player and System Event Handling
Support playback controls on external media players or system-provided controls.
- [Handling external player events notifications](https://developer.apple.com/documentation/mediaplayer/handling_external_player_events_notifications) - Handle events for external media players.
- [Remote command center events](https://developer.apple.com/documentation/mediaplayer/remote_command_center_events) - Set up the remote command center to handle media player events.
- [Track navigation events](https://developer.apple.com/documentation/mediaplayer/track_navigation_events) - Respond to requests to change which part of a media item plays.
- [Media playback mode events](https://developer.apple.com/documentation/mediaplayer/media_playback_mode_events) - Respond to changes in the way media items play.
- [Feedback and rating events](https://developer.apple.com/documentation/mediaplayer/feedback_and_rating_events) - Respond to incoming feedback and rating events.

### External Media Player Items
- [External media player items](https://developer.apple.com/documentation/mediaplayer/external_media_player_items) - Provide content and interact with external media players.
- **MPContentItem** - An object that contains the information for a displayed media item.

### Media Player Errors
- **MPError** - A structure that represents a framework error.
- **Code** - An enumeration that represents error codes for framework operations.
- **MPErrorDomain** - The Media Player framework error domain.

### Deprecated
- [Deprecated types](https://developer.apple.com/documentation/mediaplayer/deprecated_types) - Review deprecated symbols and avoid using them in your app.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MediaPlayer)*