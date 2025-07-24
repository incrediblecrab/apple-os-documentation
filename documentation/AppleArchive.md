# Apple Archive

Perform multithreaded lossless compression of directories, files, and data.

**Platforms:** iOS 14.0+ | iPadOS 14.0+ | Mac Catalyst 14.0+ | macOS 11.0+ | tvOS 14.0+ | visionOS 1.0+ | watchOS 7.0+

## Overview

Apple Archive provides fast compression that includes file attributes, such as, ownership, permissions, flags, times, extended attributes, and error correction. Apple Archive offers these features:

- Multithreaded processing that uses all cores, is energy efficient, and yields faster results
- An ability to transport files and their attributes and use Apple File System (APFS) features when they're available, for example, filesystem compression, full clones, and sparse files
- Flexible encoding formats, so you can use archives, for example, for error correction, digests, manifests, and external data storage
- API support for in-memory archive processing, streaming access, random access, and back-to-back archive and extraction

## Topics

### Apple Archive essentials
- [Compressing single files](https://developer.apple.com/documentation/applearchive/compressing_single_files) - Compress a single file and store the result on the file system.
- [Decompressing single files](https://developer.apple.com/documentation/applearchive/decompressing_single_files) - Recreate a single file from a compressed file.
- [Compressing file system directories](https://developer.apple.com/documentation/applearchive/compressing_file_system_directories) - Compress the contents of an entire directory and store the result on the file system.
- [Decompressing and extracting an archived directory](https://developer.apple.com/documentation/applearchive/decompressing_and_extracting_an_archived_directory) - Recreate an entire file system directory from an archive file.
- [Compressing and saving a string to the file system](https://developer.apple.com/documentation/applearchive/compressing_and_saving_a_string_to_the_file_system) - Compress the contents of a Unicode string and store the result on the file system.
- [Decompressing and Parsing an Archived String](https://developer.apple.com/documentation/applearchive/decompressing_and_parsing_an_archived_string) - Recreate a string from an archive file.

### Apple Encrypted Archive essentials
- [Encrypting and Decrypting a String](https://developer.apple.com/documentation/applearchive/encrypting_and_decrypting_a_string) - Encrypt the contents of a string and save the result to the file system, then decrypt and recreate the string from the archive file using Apple Encrypted Archive.
- [Encrypting and Decrypting a Single File](https://developer.apple.com/documentation/applearchive/encrypting_and_decrypting_a_single_file) - Encrypt a single file and save the result to the file system, then decrypt and recreate the original file from the archive file using Apple Encrypted Archive.
- [Encrypting and Decrypting Directories](https://developer.apple.com/documentation/applearchive/encrypting_and_decrypting_directories) - Compress and encrypt the contents of an entire directory or decompress and decrypt an archived directory using Apple Encrypted Archive.
- **ArchiveEncryptionContext** - An object that encapsulates all parameters, keys, and data necessary to open an encrypted archive for both encryption and decryption streams.

### Apple Archive headers
- **ArchiveHeader** - An AppleArchive entry header.

### Apple Archive streams
- **ArchiveStreamProtocol** - A set of methods that defines the interface for using an archive stream that reads from and writes to data blobs.
- **ArchiveStream** - An archive stream that reads from and writes to data blobs
- **ArchiveByteStreamProtocol** - A set of methods that defines the interface for using an archive stream that reads from and writes to buffers.
- **ArchiveByteStream** - An archive stream that reads from and writes to buffers.

### Apple Archive errors
- **ArchiveError** - Error codes for AppleArchive.

### Constants
- **APPLE_ARCHIVE_API_VERSION** - The version of the framework at compile time.

### Reference
- [Apple Archive structures](https://developer.apple.com/documentation/applearchive/apple_archive_structures)

### See Also
- [About Apple File System](https://developer.apple.com/documentation/foundation/file_system/about_apple_file_system) - Use high-level APIs to get the most out of Apple File System.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AppleArchive)*