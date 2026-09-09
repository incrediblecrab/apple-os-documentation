# QuickTime File Format

An object-oriented file format for the storage and exchange of digital media between devices, applications, and operating systems.

## Overview

The **QuickTime File Format (QTFF)** stores different kinds of digital multimedia data and the metadata needed to interpret them. Its extensible structure supports media interchange between applications and systems, subject to each consumer's supported tracks, codecs, and atoms.

The format uses a hierarchy of typed, sized objects called atoms. A parser can skip unrecognized atoms using their declared sizes, allowing extensions without requiring every reader to understand every atom. Validate sizes and container boundaries; extensibility does not mean an arbitrary file is safe or trivial to parse.

This is a file-format reference, not a recommendation to adopt the legacy QuickTime application APIs discussed in older material. For current application-level media reading and writing, start with [AVFoundation](AVFoundation.md) and [Core Media](CoreMedia.md); use the atom reference when implementing or inspecting a format-level workflow.

**Important:** Related ISO-standardized media container formats, including those used for MPEG-4 and JPEG-2000 media, share structural heritage with QTFF but remain distinct file formats. Similar atoms do not make a QuickTime file interchangeable with another container, or establish support for its codecs.

QuickTime files are used to store QuickTime movies, as well as other data. If you are writing an application that parses QuickTime files, you should recognize that there may be non-movie data in the files.

## Topics

### Essentials
- [Storing and sharing media with QuickTime files](https://developer.apple.com/documentation/quicktime-file-format/storing_and_sharing_media_with_quicktime_files) - Build QuickTime files with atoms, QT atoms, and atom containers.

### Movies
- [Movie atoms](https://developer.apple.com/documentation/quicktime-file-format/movie_atoms) - Atoms that act as a container for the information that describes a movie's data.
- [Track atoms](https://developer.apple.com/documentation/quicktime-file-format/track_atoms) - Atoms that define a single track of a movie.
- [Media atoms](https://developer.apple.com/documentation/quicktime-file-format/media_atoms) - Atoms that describe and define a track's media type and sample data.
- [Sample atoms](https://developer.apple.com/documentation/quicktime-file-format/sample_atoms) - Atoms that describe samples, which are single elements in a sequence of time-ordered data.
- [Structuring movie data and features](https://developer.apple.com/documentation/quicktime-file-format/structuring_movie_data_and_features) - Build movies with compressed or reference data, and add features like effect descriptions and alternate subtitle tracks.

### Metadata
- [Metadata atoms and types](https://developer.apple.com/documentation/quicktime-file-format/metadata_atoms_and_types) - Store metadata in QuickTime Movie files.

### Media data
- [Media data atom types](https://developer.apple.com/documentation/quicktime-file-format/media_data_atom_types) - Store different types of media data, including video, sound, subtitles, and more.

### Data types
- [Basic QuickTime data types](https://developer.apple.com/documentation/quicktime-file-format/basic_data_types) - Express values in QuickTime files with common data types.

### Change log
- [QuickTime File Format change log](https://developer.apple.com/documentation/quicktime-file-format/revision_history) - Changes to the QuickTime File Format.

### Deprecated
- [Deprecated atoms](https://developer.apple.com/documentation/quicktime-file-format/deprecated_atoms) - Review unsupported atoms.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/quicktime-file-format)*
