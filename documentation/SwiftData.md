# SwiftData

Write your model code declaratively to add managed persistence and efficient model fetching.

**Platforms:** iOS 17.0+ | iPadOS 17.0+ | Mac Catalyst 17.0+ | macOS 14.0+ | tvOS 17.0+ | visionOS 1.0+ | watchOS 10.0+

## Overview

SwiftData supplies persistent models, contexts, fetches, and schema tools. Its default store uses Core Data, while custom stores can provide other persistence implementations. Cloud synchronization is an optional, separately configured capability, not a guarantee for every model or store.

SwiftData has uses beyond persisting locally created content. For example, an app that fetches data from a remote web service might use SwiftData to implement a lightweight caching mechanism and provide limited offline functionality.

Annotate a class with `@Model` when its stored properties meet SwiftData's schema requirements. Customize attributes and relationships with `@Attribute` and `@Relationship`. Use `ModelContext` to insert, update, delete, and save model instances.

Use `@Query` in a SwiftUI view and choose an overload for the required predicate, sorting, or fetch descriptor. SwiftData keeps the fetched models synchronized so the view can respond to changes. Supply the environment's model context using [`modelContainer(_:)`](https://developer.apple.com/documentation/swiftui/view/modelcontainer(_:)) or [`modelContext(_:)`](https://developer.apple.com/documentation/swiftui/view/modelcontext(_:)); these are not parameterless modifiers.

## OS 27 queries and change observation

The [June 2026 SwiftData update](https://developer.apple.com/documentation/updates/swiftdata) adds these APIs on iOS/iPadOS/Mac Catalyst/macOS/tvOS/visionOS/watchOS 27+:

- [Query macros with `sectionBy`](https://developer.apple.com/documentation/swiftdata/additionalquerymacros) group fetched results into sections.
- [`Schema.Attribute.Option.codable`](https://developer.apple.com/documentation/swiftdata/schema/attribute/option/codable) stores a property's `Codable` representation, including types owned by another module.
- [`ResultsObserver`](https://developer.apple.com/documentation/swiftdata/resultsobserver) maintains fetched results and optional sections as local, other-context, or external changes arrive.
- [`HistoryObserver`](https://developer.apple.com/documentation/swiftdata/historyobserver) tracks relevant remote history changes with tokens and an observable `eventCounter`. This signals work to process; it does not replace the app's conflict-resolution or sync design.

The [iOS/iPadOS](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes) and [macOS](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes) 27 beta 8 notes mark the `@Query` deadlock involving a background `ModelContext` save and newly scheduled `ModelActor` tasks as **resolved** (178113288). Keep a regression test, but do not present it as a permanent restriction against background saves.

## Concurrency and migration

Keep model access on its owning context/actor; [`ModelActor`](https://developer.apple.com/documentation/swiftdata/modelactor) provides mutually exclusive access, not permission to share mutable model instances arbitrarily. Separate reading UI state from background storage work.

[`SchemaMigrationPlan`](https://developer.apple.com/documentation/swiftdata/schemamigrationplan), `VersionedSchema`, and `MigrationStage` describe store evolution and remain available from SwiftData's original minimums. Test migrations against copies of stores produced by shipped versions, including relationships, uniqueness, and encoded values. Rebuilding with a new SDK does not by itself require replacing the persistence architecture. [AppMigrationKit](AppMigrationKit.md) addresses cross-platform data transport, not SwiftData schema migration.

## Topics

### Essentials
- [Preserving your app's model data across launches](https://developer.apple.com/documentation/swiftdata/preserving-your-apps-model-data-across-launches) - Describe your model classes to SwiftData using the framework's macros, and store instances of those models so they exist beyond the app's runtime
- [Adding and editing persistent data in your app](https://developer.apple.com/documentation/swiftdata/adding-and-editing-persistent-data-in-your-app) - Create a data entry form for collecting and changing data managed by SwiftData
- [Adopting SwiftData for a Core Data app](https://developer.apple.com/documentation/coredata/adopting-swiftdata-for-a-core-data-app) - Plan adoption alongside an existing Core Data store.
- [SwiftData updates](https://developer.apple.com/documentation/updates/swiftdata) - Learn about important changes to SwiftData.
- [Adopting inheritance in SwiftData](https://developer.apple.com/documentation/swiftdata/adopting-inheritance-in-swiftdata) - Add flexibility to your models using class inheritance

### Model Definition
- **@Model** macro - Converts a Swift class into a stored model that's managed by SwiftData
- **@Attribute** macro - Specifies the custom behavior that SwiftData applies to the annotated property when managing the owning class
- [`#Unique`](https://developer.apple.com/documentation/swiftdata/unique(_:)) - A freestanding declaration inside a model, not an `@Unique` attribute. Declares single or compound uniqueness constraints.
- [`#Index`](https://developer.apple.com/documentation/swiftdata/index(_:)-74ia2) - A freestanding declaration for indexes. The [typed overload](https://developer.apple.com/documentation/swiftdata/index(_:)-7d4z0) supports binary or R-tree indexes.

`#Unique` and both `#Index` declarations list iOS/iPadOS/Mac Catalyst/tvOS 18+, macOS 15+, watchOS 11+, and visionOS 1+, separately from the framework's original minimums.

- [Defining data relationships with enumerations and model classes](https://developer.apple.com/documentation/swiftdata/defining-data-relationships-with-enumerations-and-model-classes) - Create relationships for static and dynamic data stored in your app
- **@Relationship** macro - Specifies the options that SwiftData needs to manage the annotated property as a relationship between two models
- **@Transient** macro - Tells SwiftData not to persist the annotated property when managing the owning class

### Model Life Cycle
- **ModelContainer** - An object that manages an app's schema and model storage configuration
- **ModelContext** - An object that enables you to fetch, insert, and delete models, and save any changes to disk
- [Fetching and filtering time-based model changes](https://developer.apple.com/documentation/swiftdata/fetching-and-filtering-time-based-model-changes) - Track all inserts, updates, and deletes that occur in a data store and process them as a series of chronological transactions
- **HistoryDescriptor** - A type that describes the criteria, and, optionally, sort order, to use when fetching history data
- [Deleting persistent data from your app](https://developer.apple.com/documentation/swiftdata/deleting-persistent-data-from-your-app) - Explore different ways to use SwiftData to delete persistent data
- [Reverting data changes using the undo manager](https://developer.apple.com/documentation/swiftdata/reverting-data-changes-using-the-undo-manager) - Configure undo support for data changes in a SwiftUI app
- [Syncing model data across a person's devices](https://developer.apple.com/documentation/swiftdata/syncing-model-data-across-a-persons-devices) - Add the required capabilities and define a compatible schema to enable SwiftData to automatically sync your app's model data using iCloud

### Concurrency Support
Types you use to access model attributes and perform storage-related tasks in a safe and isolated way.

### Model Fetch
- [Filtering and sorting persistent data](https://developer.apple.com/documentation/swiftdata/filtering-and-sorting-persistent-data) - Manage data store presentation using predicates and dynamic queries
- **@Query()** macro - The unfiltered form fetches all instances of the model type; other overloads accept filtering and sorting.
- Additional query macros - Supplementary macros that enable you to narrow query results and tell SwiftData how to sort and order those results
- **Query** - A type that fetches models using the specified criteria, and manages those models so they remain in sync with the underlying data
- **FetchDescriptor** - A type that describes the criteria, sort order, and any additional configuration to use when performing a fetch

### Model Storage

The public `DataStore` and `DefaultStore` types require iOS/iPadOS/Mac Catalyst/tvOS 18+, macOS 15+, watchOS 11+, and visionOS 2+. Basic SwiftData persistence remains available at the framework's earlier minimums.

- [Maintaining a local copy of server data](https://developer.apple.com/documentation/swiftdata/maintaining-a-local-copy-of-server-data) - Create and update a persistent store to cache read-only network data
- **DefaultStore** - A data store that uses Core Data as its underlying storage mechanism
- **DataStore** protocol - An interface that enables SwiftData to read and write model data without knowledge of the underlying storage mechanism
- **DataStoreBatching** protocol - An interface that enables a custom data store to support batch requests
- **HistoryProviding** protocol - An interface that enables a custom data store to provide the history of changes for its persisted models
- [Building a document-based app using SwiftData](https://developer.apple.com/documentation/swiftui/building-a-document-based-app-using-swiftdata) - Code along with the WWDC presenter to transform an app with SwiftData
- [`ModelDocument`](https://developer.apple.com/documentation/swiftdata/modeldocument) - A structure used by SwiftUI's `DocumentGroup` initializers; don't instantiate it directly. Available on iOS/iPadOS/Mac Catalyst 17+, macOS 14+, and visionOS 1+, not tvOS/watchOS.

### History Life Cycle

`HistoryDescriptor` and the following history types require iOS/iPadOS/Mac Catalyst/tvOS 18+, macOS 15+, watchOS 11+, and visionOS 2+.

- [`HistoryChange`](https://developer.apple.com/documentation/swiftdata/historychange) - Insert, update, or delete changes within history transactions.
- [`HistoryDelete`](https://developer.apple.com/documentation/swiftdata/historydelete) - A protocol for a recorded model deletion's identifiers and tombstone. It is not the operation that prunes stored history; that request belongs to [`HistoryProviding`](https://developer.apple.com/documentation/swiftdata/historyproviding).
- Related protocols: [`HistoryInsert`](https://developer.apple.com/documentation/swiftdata/historyinsert), [`HistoryUpdate`](https://developer.apple.com/documentation/swiftdata/historyupdate), and [`HistoryTransaction`](https://developer.apple.com/documentation/swiftdata/historytransaction).

### Codable Support
- **DataStoreSnapshotCodingKey** - The key space to use when implementing custom coders and decoders for data store snapshots

### Errors
- **SwiftDataError** - A type that describes a SwiftData error
- **DataStoreError** - A type that describes a data store error

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SwiftData)*
