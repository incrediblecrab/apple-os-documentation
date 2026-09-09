# iTunes Library

Retrieve the properties of the media in the user's iTunes library.

**Platforms:** Mac Catalyst 14.0+ | macOS 10.13+

## Overview

With this framework, you can retrieve media information, such as track and playlist metadata, directly from the user's iTunes library, eliminating the need to query the iTunes XML file.

To use this framework, create an `ITLibrary` object using the Objective-C `libraryWithAPIVersion:error:` class method or its Swift initializer. Inspect the returned library's properties and media items, and handle initialization errors.

**Important:** You must code sign your app to retrieve information with this framework, and library access is read-only. Apple's reference retains the historical iTunes 11-or-later prerequisite and iTunes terminology; this local-library API is distinct from Apple Music catalog, subscription, and streaming authorization.

The [ITLibrary overview](https://developer.apple.com/documentation/ituneslibrary/itlibrary) also requires the person's permission and an `NSAppleMusicUsageDescription` entry explaining your use of the library. The system terminates an app that attempts access without that usage-description key. Code signing does not replace user authorization.

## Topics

### Essentials
- **ITLibrary** - This class serves as the entry point to the iTunesLibrary framework.

### Albums and Playlists
- **ITLibAlbum** - This class provides information about an album in the iTunes library.
- **ITLibPlaylist** - This class describes a playlist in the iTunes library.

### Media Items
- **ITLibMediaItem** - This class describes a media item (a track) in the iTunes library, such as a song, a video, or a podcast.
- **ITLibMediaEntity** - This class describes a media entity, which can be a media item, such as an audio track.
- **ITLibArtist** - This class represents an artist, such as the performer of a song.
- **ITLibArtwork** - This class represents the artwork for a media item.
- **ITLibMediaItemVideoInfo** - This class encapsulates the video information of a video media item.

### Structures
- **DidChangeLibraryMessage**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/iTunesLibrary)*
