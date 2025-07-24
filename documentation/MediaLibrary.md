# Media Library

Access read-only collections of the user's multimedia content.

**Platforms:** Mac Catalyst 13.0+ | macOS 10.9+ *Deprecated*

Use the PhotoKit and iTunes Library frameworks instead.

## Overview

The Media Library framework provides a read-only Objective-C data model representing a user's collections of images, audio, and video. The initial access point of the Media Library framework is MLMediaLibrary, which loads the user's media into a hierarchical structure consisting of media sources, groups, and objects.

At the highest level, all content within a media library instance is categorized by media source. Conceptually, a media source respresents a single app, such as iTunes or Aperture. Each source contains a hierarchy of media groups that originates from a root group. These groups consist of media objects—individual files containing a piece of media such as a photo, song, or movie. Only one copy of each object exists within a media library instance, but an object can be referenced by multiple groups from a single source. The structure of the group hierarchy is specific to each media source.

## Topics

### Classes
- **MLMediaGroup** - The MLMediaGroup class provides groupings for media objects from a single source of media, such as iTunes or Aperture. The media objects—individual files containing a piece of media such as a photo, song, or movie—are referenced by one or more groups within each media source. These groupings serve as filters, providing hierarchical structure to the collection of objects in each source.
- **MLMediaLibrary** - The MLMediaLibrary class provides an interface for accessing a collection of media objects from various sources. It serves as the initial access point of the Media Library framework.
- **MLMediaObject** - The MLMediaObject class describes a single media file, such as a photo, song, or movie. Each media object contains basic metadata including a name, media type, URL, and so on. Additional information about each object is stored in its list of attributes. For a list of possible object attribute keys, see Media Object Attribute Keys.
- **MLMediaSource** - The MLMediaSource class identifies a specific provider of media. Conceptually, a media source respresents a single app, such as iTunes or Aperture. Each media source contains multiple groups of media objects—individual files containing a piece of media such as a photo, song, or movie.

### Reference
- [MediaLibrary Constants](https://developer.apple.com/documentation/medialibrary/medialibrary_constants)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MediaLibrary)*