# QuickTime File Format

An object-oriented file format for the storage and exchange of digital media between devices, applications, and operating systems.

## Overview

The **QuickTime File Format (QTFF)** accommodates storing and accessing many kinds of digital multimedia data. The QTFF is an ideal format for the exchange of digital media between devices, applications, and operating systems, because you can use it to describe almost any media structure.

The file format is object-oriented, consisting of a flexible collection of objects that you can easily parse. The format's design allows for easy extension, as parsers can skip or ignore unknown objects, allowing considerable forward compatibility for new object types.

QuickTime provides a number of high-level functions that you can use to create and manipulate QuickTime files, without requiring you to understand the actual file format. These functions serve to insulate developers from the low-level details of operation. Use this documentation to create QuickTime files beyond the basic types.

**Important:** The QuickTime File Format is the basis of the MPEG-4 standard and the JPEG-2000 standard, developed by the International Organization for Standardization (ISO). Although these file types have similar structures and contain many functionally identical elements, they are distinct file types.

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
- [Basic QuickTime data types](https://developer.apple.com/documentation/quicktime-file-format/basic_quicktime_data_types) - Express values in QuickTime files with common data types.

### Change log
- [QuickTime File Format change log](https://developer.apple.com/documentation/quicktime-file-format/quicktime_file_format_change_log) - Changes to the QuickTime File Format.

### Deprecated
- [Deprecated atoms](https://developer.apple.com/documentation/quicktime-file-format/deprecated_atoms) - Review unsupported atoms.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/quicktime-file-format)*