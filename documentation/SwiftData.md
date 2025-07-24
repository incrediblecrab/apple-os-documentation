# SwiftData

Write your model code declaratively to add managed persistence and efficient model fetching.

**Platforms:** iOS 17.0+ | iPadOS 17.0+ | Mac Catalyst 17.0+ | macOS 14.0+ | tvOS 17.0+ | visionOS 1.0+ | watchOS 10.0+

## Overview

Combining Core Data's proven persistence technology and Swift's modern concurrency features, SwiftData enables you to add persistence to your app quickly, with minimal code and no external dependencies. Using modern language features like macros, SwiftData enables you to write code that is fast, efficient, and safe, enabling you to describe the entire model layer (or object graph) for your app. The framework handles storing the underlying model data, and optionally, syncing that data across multiple devices.

SwiftData has uses beyond persisting locally created content. For example, an app that fetches data from a remote web service might use SwiftData to implement a lightweight caching mechanism and provide limited offline functionality.

SwiftData is unintrusive by design and supplements your app's existing model classes. Attach the **Model()** macro to any model class to make it persistable. Customize the behavior of that model's properties with the **Attribute()** and **Relationship()** macros. Use the **ModelContext** class to insert, update, and delete instances of that model, and to write unsaved changes to disk.

To display models in a SwiftUI view, use the **Query()** macro and specify a predicate or fetch descriptor. SwiftData performs the fetch when the view appears, and tells SwiftUI about any subsequent changes to the fetched models so the view can update accordingly. You can access the model context in any SwiftUI view using the modelContext environment value, and specify a particular model container or context for a view with the **modelContainer()** and **modelContext()** view modifiers.

## Topics

### Essentials
- [Preserving your app's model data across launches](https://developer.apple.com/documentation/swiftdata/preserving_your_app_s_model_data_across_launches) - Describe your model classes to SwiftData using the framework's macros, and store instances of those models so they exist beyond the app's runtime
- [Adding and editing persistent data in your app](https://developer.apple.com/documentation/swiftdata/adding_and_editing_persistent_data_in_your_app) - Create a data entry form for collecting and changing data managed by SwiftData
- [Adopting SwiftData for a Core Data app](https://developer.apple.com/documentation/swiftdata/adopting_swiftdata_for_a_core_data_app) - Persist data in your app intuitively with the Swift native persistence framework (Beta)
- [SwiftData updates](https://developer.apple.com/documentation/swiftdata/swiftdata_updates) - Learn about important changes to SwiftData
- [Adopting inheritance in SwiftData](https://developer.apple.com/documentation/swiftdata/adopting_inheritance_in_swiftdata) - Add flexibility to your models using class inheritance

### Model Definition
- **@Model** macro - Converts a Swift class into a stored model that's managed by SwiftData
- **@Attribute** macro - Specifies the custom behavior that SwiftData applies to the annotated property when managing the owning class
- **@Unique** macro - Specifies the key-paths that SwiftData uses to enforce the uniqueness of model instances
- **@Index** macro - Specifies the key-paths that SwiftData uses to create one or more binary indices for the associated model
- [Defining data relationships with enumerations and model classes](https://developer.apple.com/documentation/swiftdata/defining_data_relationships_with_enumerations_and_model_classes) - Create relationships for static and dynamic data stored in your app
- **@Relationship** macro - Specifies the options that SwiftData needs to manage the annotated property as a relationship between two models
- **@Transient** macro - Tells SwiftData not to persist the annotated property when managing the owning class

### Model Life Cycle
- **ModelContainer** - An object that manages an app's schema and model storage configuration
- **ModelContext** - An object that enables you to fetch, insert, and delete models, and save any changes to disk
- [Fetching and filtering time-based model changes](https://developer.apple.com/documentation/swiftdata/fetching_and_filtering_time-based_model_changes) - Track all inserts, updates, and deletes that occur in a data store and process them as a series of chronological transactions
- **HistoryDescriptor** - A type that describes the criteria, and, optionally, sort order, to use when fetching history data
- [Deleting persistent data from your app](https://developer.apple.com/documentation/swiftdata/deleting_persistent_data_from_your_app) - Explore different ways to use SwiftData to delete persistent data
- [Reverting data changes using the undo manager](https://developer.apple.com/documentation/swiftdata/reverting_data_changes_using_the_undo_manager) - Automatically record data change operations that people perform in your SwiftUI app, and let them undo and redo those changes
- [Syncing model data across a person's devices](https://developer.apple.com/documentation/swiftdata/syncing_model_data_across_a_person_s_devices) - Add the required capabilities and define a compatible schema to enable SwiftData to automatically sync your app's model data using iCloud

### Concurrency Support
Types you use to access model attributes and perform storage-related tasks in a safe and isolated way.

### Model Fetch
- [Filtering and sorting persistent data](https://developer.apple.com/documentation/swiftdata/filtering_and_sorting_persistent_data) - Manage data store presentation using predicates and dynamic queries
- **@Query** macro - Fetches all instances of the attached model type
- Additional query macros - Supplementary macros that enable you to narrow query results and tell SwiftData how to sort and order those results
- **Query** - A type that fetches models using the specified criteria, and manages those models so they remain in sync with the underlying data
- **FetchDescriptor** - A type that describes the criteria, sort order, and any additional configuration to use when performing a fetch

### Model Storage
- [Maintaining a local copy of server data](https://developer.apple.com/documentation/swiftdata/maintaining_a_local_copy_of_server_data) - Create and update a persistent store to cache read-only network data
- **DefaultStore** - A data store that uses Core Data as its underlying storage mechanism
- **DataStore** protocol - An interface that enables SwiftData to read and write model data without knowledge of the underlying storage mechanism
- **DataStoreBatching** protocol - An interface that enables a custom data store to support batch requests
- **HistoryProviding** protocol - An interface that enables a custom data store to provide the history of changes for its persisted models
- [Building a document-based app using SwiftData](https://developer.apple.com/documentation/swiftdata/building_a_document-based_app_using_swiftdata) - Code along with the WWDC presenter to transform an app with SwiftData
- **ModelDocument** - A document type that uses SwiftData to manage its storage

### History Life Cycle
- **HistoryChange** - Values that describe data history transactions
- **HistoryDelete** protocol - An interface that enables a custom data store to delete items from the history of changes to its persisted models
- Various history-related protocols and structures for managing data change history

### Codeable Support
- **DataStoreSnapshotCodingKey** - The key space to use when implementing custom coders and decoders for data store snapshots

### Errors
- **SwiftDataError** - A type that describes a SwiftData error
- **DataStoreError** - A type that describes a data store error

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SwiftData)*