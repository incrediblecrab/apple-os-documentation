# iTunes Library

Retrieve the properties of the media in the user's iTunes library.

**Platforms:** Mac Catalyst 14.0+ | macOS 10.13+

## Overview

With this framework, you can retrieve media information, such as track and playlist metadata, directly from the user's iTunes library, eliminating the need to query the iTunes XML file.

To use this framework, create an ITLibrary object by calling the libraryWithAPIVersion:error: class method. You can interrogate the instance that returns to obtain its properties and the properties of its media items. For example:

**Important:** You must code sign your app to retrieve information with this framework, and iTunes library access is read-only. This framework is available to users with iTunes 11 or later.

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

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/iTunesLibrary)*