# Foundation

Access essential data types, collections, and operating-system services to define the base layer of functionality for your app.

**Platforms:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 13.0+ | macOS 10.0+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 2.0+

## Overview

The Foundation framework provides a base layer of functionality for apps and frameworks, including data storage and persistence, text processing, date and time calculations, sorting and filtering, and networking. The classes, protocols, and data types defined by Foundation are used throughout the macOS, iOS, watchOS, and tvOS SDKs.

## OS 27 compatibility checks

### URLs and available capacity

The [iOS & iPadOS 27 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes) document two distinct changes:

- [`volumeAvailableCapacityKey`](https://developer.apple.com/documentation/foundation/urlresourcekey/volumeavailablecapacitykey) now truncates capacity to three significant decimal digits **at the block-count level**. The API still reports bytes; do not interpret a reported value as exact free space or a reservation. Allow headroom and handle failed writes. Use also requires an appropriate required-reason API declaration in the privacy manifest.
- `+[NSURL URLWithString:]` no longer double-encodes a valid percent escape's `%` when encoding other invalid characters. Apple lists this as **resolved**, also in the [macOS 27 notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes). Retest URLs containing both valid escapes and unescaped characters, especially signed URLs, and remove workarounds only after checking older supported runtimes.

The capacity note is specifically listed in the iOS/iPadOS notes; it is not a blanket statement about every Foundation capacity API on every platform.

### Concurrency and UI integration

Foundation's [typed notification APIs](https://developer.apple.com/documentation/updates/foundation) arrived in the **26 generation**. [`NotificationCenter.MainActorMessage`](https://developer.apple.com/documentation/foundation/notificationcenter/mainactormessage) delivers synchronously on the main actor; [`NotificationCenter.AsyncMessage`](https://developer.apple.com/documentation/foundation/notificationcenter/asyncmessage) requires sendable messages and delivers asynchronously. Do not substitute asynchronous delivery where observers must finish before the posting operation proceeds. `UndoManager` is main-actor isolated.

For OS 27 document I/O, see [SwiftUI's URL-based document protocols](SwiftUI.md#url-based-documents): reader/writer work uses `@concurrent`, while `URLDocumentConfiguration` and document factories belong on the main actor. These rules do not make every Foundation reference type safe to share across isolation boundaries. See [Swift](Swift.md) for language changes rather than treating compiler features as new Foundation APIs.

### Persistence versus data transport

Use [Core Data](CoreData.md) or [SwiftData](SwiftData.md) to evolve an on-device store, and [AppMigrationKit](AppMigrationKit.md) for a system-managed, one-time transfer to or from a non-Apple platform. These frameworks do not make arbitrary database formats portable.

## Topics

### Fundamentals
- [Numbers, Data, and Basic Values](https://developer.apple.com/documentation/foundation/numbers-data-and-basic-values) - Work with primitive values and other fundamental types used throughout Cocoa.
- [Strings and Text](https://developer.apple.com/documentation/foundation/strings-and-text) - Create and process strings of Unicode characters, use regular expressions to find patterns, and perform natural language analysis of text.
- [Collections](https://developer.apple.com/documentation/foundation/collections) - Use arrays, dictionaries, sets, and specialized collections to store and iterate groups of objects or values.
- [Dates and Times](https://developer.apple.com/documentation/foundation/dates-and-times) - Compare dates and times, and perform calendar and time zone calculations.
- [Units and Measurement](https://developer.apple.com/documentation/foundation/units-and-measurement) - Label numeric quantities with physical dimensions to allow locale-aware formatting and conversion between related units.
- [Data Formatting](https://developer.apple.com/documentation/foundation/data-formatting) - Convert numbers, dates, measurements, and other values to and from locale-aware string representations.
- [Filters and Sorting](https://developer.apple.com/documentation/foundation/filters-and-sorting) - Use predicates, expressions, and sort descriptors to examine elements in collections and other services.

### App Support
- [Task Management](https://developer.apple.com/documentation/foundation/task-management) - Manage your app's work and how it interacts with system services like Handoff and Shortcuts.
- [Resources](https://developer.apple.com/documentation/foundation/resources) - Access assets and other data bundled with your app.
- [Notifications](https://developer.apple.com/documentation/foundation/notifications) - Design patterns for broadcasting information and for subscribing to broadcasts.
- [App Extension Support](https://developer.apple.com/documentation/foundation/app-extension-support) - Manage the interaction between an app extension and its hosting app.
- [Errors and Exceptions](https://developer.apple.com/documentation/foundation/errors-and-exceptions) - Respond to problem situations in your interactions with APIs, and fine-tune your app for better debugging.
- [Scripting Support](https://developer.apple.com/documentation/foundation/scripting-support) - Allow users to control your app with AppleScript and other automation technologies, or run scripts from within your app.

### Files and Data Persistence
- [File System](https://developer.apple.com/documentation/foundation/file-system) - Create, read, write, and examine files and folders in the file system.
- [Archives and Serialization](https://developer.apple.com/documentation/foundation/archives-and-serialization) - Convert objects and values to and from property list, JSON, and other flat binary representations.
- [Settings](https://developer.apple.com/documentation/foundation/settings) - Store configuration locally with `UserDefaults`, or share it through iCloud with `NSUbiquitousKeyValueStore`.
- [Spotlight](https://developer.apple.com/documentation/foundation/spotlight) - Search for files and other items on the local device, and index your app's content for searching.
- [iCloud](https://developer.apple.com/documentation/foundation/icloud) - Manage files and key-value data that automatically synchronize among a user's iCloud devices.
- [Optimizing Your App's Data for iCloud Backup](https://developer.apple.com/documentation/foundation/optimizing-your-app-s-data-for-icloud-backup) - Exclude appropriate caches and re-downloadable resources without excluding irreplaceable user content.

### Networking
- [URL Loading System](https://developer.apple.com/documentation/foundation/url-loading-system) - Interact with URLs and communicate with servers using standard Internet protocols.
- [Bonjour](https://developer.apple.com/documentation/foundation/bonjour) - Advertise services for easy discovery on local networks, or discover services advertised by others.

### Low-Level Utilities
- [XPC](https://developer.apple.com/documentation/foundation/xpc) - Manage secure interprocess communication.
- [Object Runtime](https://developer.apple.com/documentation/foundation/object-runtime) - Get low-level support for basic Objective-C features, Cocoa design patterns, and Swift integration.
- [Processes and Threads](https://developer.apple.com/documentation/foundation/processes-and-threads) - Manage your app's interaction with the host operating system and other processes, and implement low-level concurrency features.
- [Streams, Sockets, and Ports](https://developer.apple.com/documentation/foundation/streams-sockets-and-ports) - Use low-level Unix features to manage input and output among files, processes, and the network.

### Reference
- **Foundation Enumerations**
- **Foundation Data Types** - This document describes the data types and constants found in the Foundation framework.

### Structures
- [`DiscontiguousAttributedSubstring`](https://developer.apple.com/documentation/foundation/discontiguousattributedsubstring) - A structure representing a discontiguous portion of an attributed string; requires version 26 on supported platforms.

### Macros
- [`#bundle`](https://developer.apple.com/documentation/foundation/bundle()) - An expression macro that selects the calling code's likely resource bundle, including app, extension, framework, and Swift package contexts. Added with the 26-generation SDKs; back-deploys to iOS/iPadOS/Mac Catalyst/tvOS 15, macOS 12, watchOS 8, and visionOS 1.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Foundation)*
