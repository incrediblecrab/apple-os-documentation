# Foundation

Access essential data types, collections, and operating-system services to define the base layer of functionality for your app.

**Platforms:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 13.0+ | macOS 10.0+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 2.0+

## Overview

The Foundation framework provides a base layer of functionality for apps and frameworks, including data storage and persistence, text processing, date and time calculations, sorting and filtering, and networking. The classes, protocols, and data types defined by Foundation are used throughout the macOS, iOS, watchOS, and tvOS SDKs.

## Topics

### Fundamentals
- [Numbers, Data, and Basic Values](https://developer.apple.com/documentation/foundation/numbers_data_and_basic_values) - Work with primitive values and other fundamental types used throughout Cocoa.
- [Strings and Text](https://developer.apple.com/documentation/foundation/strings_and_text) - Create and process strings of Unicode characters, use regular expressions to find patterns, and perform natural language analysis of text.
- [Collections](https://developer.apple.com/documentation/foundation/collections) - Use arrays, dictionaries, sets, and specialized collections to store and iterate groups of objects or values.
- [Dates and Times](https://developer.apple.com/documentation/foundation/dates_and_times) - Compare dates and times, and perform calendar and time zone calculations.
- [Units and Measurement](https://developer.apple.com/documentation/foundation/units_and_measurement) - Label numeric quantities with physical dimensions to allow locale-aware formatting and conversion between related units.
- [Data Formatting](https://developer.apple.com/documentation/foundation/data_formatting) - Convert numbers, dates, measurements, and other values to and from locale-aware string representations.
- [Filters and Sorting](https://developer.apple.com/documentation/foundation/filters_and_sorting) - Use predicates, expressions, and sort descriptors to examine elements in collections and other services.

### App Support
- [Task Management](https://developer.apple.com/documentation/foundation/task_management) - Manage your app's work and how it interacts with system services like Handoff and Shortcuts.
- [Resources](https://developer.apple.com/documentation/foundation/resources) - Access assets and other data bundled with your app.
- [Notifications](https://developer.apple.com/documentation/foundation/notifications) - Design patterns for broadcasting information and for subscribing to broadcasts.
- [App Extension Support](https://developer.apple.com/documentation/foundation/app_extension_support) - Manage the interaction between an app extension and its hosting app.
- [Errors and Exceptions](https://developer.apple.com/documentation/foundation/errors_and_exceptions) - Respond to problem situations in your interactions with APIs, and fine-tune your app for better debugging.
- [Scripting Support](https://developer.apple.com/documentation/foundation/scripting_support) - Allow users to control your app with AppleScript and other automation technologies, or run scripts from within your app.

### Files and Data Persistence
- [File System](https://developer.apple.com/documentation/foundation/file_system) - Create, read, write, and examine files and folders in the file system.
- [Archives and Serialization](https://developer.apple.com/documentation/foundation/archives_and_serialization) - Convert objects and values to and from property list, JSON, and other flat binary representations.
- [Preferences](https://developer.apple.com/documentation/foundation/preferences) - Persistently store domain-scoped pieces of information for configuring your app.
- [Spotlight](https://developer.apple.com/documentation/foundation/spotlight) - Search for files and other items on the local device, and index your app's content for searching.
- [iCloud](https://developer.apple.com/documentation/foundation/icloud) - Manage files and key-value data that automatically synchronize among a user's iCloud devices.
- [Optimizing Your App's Data for iCloud Backup](https://developer.apple.com/documentation/foundation/optimizing_your_apps_data_for_icloud_backup) - Minimize the space and time that backups take to create by excluding purgeable and nonpurgeable data from backups.

### Networking
- [URL Loading System](https://developer.apple.com/documentation/foundation/url_loading_system) - Interact with URLs and communicate with servers using standard Internet protocols.
- [Bonjour](https://developer.apple.com/documentation/foundation/bonjour) - Advertise services for easy discovery on local networks, or discover services advertised by others.

### Low-Level Utilities
- [XPC](https://developer.apple.com/documentation/foundation/xpc) - Manage secure interprocess communication.
- [Object Runtime](https://developer.apple.com/documentation/foundation/object_runtime) - Get low-level support for basic Objective-C features, Cocoa design patterns, and Swift integration.
- [Processes and Threads](https://developer.apple.com/documentation/foundation/processes_and_threads) - Manage your app's interaction with the host operating system and other processes, and implement low-level concurrency features.
- [Streams, Sockets, and Ports](https://developer.apple.com/documentation/foundation/streams_sockets_and_ports) - Use low-level Unix features to manage input and output among files, processes, and the network.

### Reference
- **Foundation Enumerations**
- **Foundation Data Types** - This document describes the data types and constants found in the Foundation framework.

### Structures
- **struct DiscontiguousAttributedSubstring** - A discontiguous portion of an attributed string.

### Macros
- **macro bundle() -> Bundle** - Returns the bundle most likely to contain resources for the calling code.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Foundation)*