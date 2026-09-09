# Core Data

Persist or cache data on a single device, or sync data to multiple devices with CloudKit.

**Platforms:** iOS 3.0+ | iPadOS 3.0+ | Mac Catalyst 13.0+ | macOS 10.4+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 2.0+

## Overview

Use Core Data to persist data for offline use, cache temporary data, and support undo. Cloud synchronization requires a configured `NSPersistentCloudKitContainer` and compatible store descriptions; it is not enabled merely by using Core Data.

Through Core Data's Data Model editor, you define your data's types and relationships, and generate respective class definitions. Core Data can then manage object instances at runtime to provide the following features.

### Persistence
Core Data abstracts the details of mapping your objects to a store, making it easy to save data from Swift and Objective-C without administering a database directly.

### Undo and redo of individual and batched changes
Set a context's [`undoManager`](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/undomanager) to enable undo support; its default is `nil`. An undo manager can group changes and integrate context edits with the rest of your app's undo/redo actions.

### Background data tasks
Perform potentially UI-blocking data tasks, like parsing JSON into objects, in the background. You can then cache or store the results to reduce server roundtrips.

### View synchronization
[`NSFetchedResultsController`](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller) organizes fetched objects into sections and can report changes to its delegate. Your app uses that information to update a table or collection view's data source.

### Versioning and migration
Core Data includes mechanisms for versioning your data model and migrating user data as your app evolves.

Choose a migration strategy based on the model change, not the SDK version. [`NSStagedMigrationManager`](https://developer.apple.com/documentation/coredata/nsstagedmigrationmanager), available from iOS/iPadOS/Mac Catalyst/tvOS 17, macOS 14, watchOS 10, and visionOS 1, sequences lightweight and custom stages. Preserve historical model versions and test upgrades from shipped stores before release.

Core Data context confinement and explicit CloudKit configuration still matter when rebuilding for OS 27. [`NSPersistentCloudKitContainer`](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer) enables mirroring; a normal persistent container does not automatically sync. See [SwiftData](SwiftData.md#concurrency-and-migration) for coexistence and [AppMigrationKit](AppMigrationKit.md) for one-time transfer to a non-Apple device. Those are different operations from migrating a Core Data schema.

## Topics

### Essentials
- [Creating a Core Data model](https://developer.apple.com/documentation/coredata/creating-a-core-data-model) - Define your app's object structure with a data model file.
- [Setting up a Core Data stack](https://developer.apple.com/documentation/coredata/setting-up-a-core-data-stack) - Set up the classes that manage and persist your app's objects.
- [Core Data stack](https://developer.apple.com/documentation/coredata/core-data-stack) - Manage and persist your app's model layer.
- [Handling Different Data Types in Core Data](https://developer.apple.com/documentation/coredata/handling-different-data-types-in-core-data) - Create, store, and present records for a variety of data types.
- [Linking Data Between Two Core Data Stores](https://developer.apple.com/documentation/coredata/linking-data-between-two-core-data-stores) - Organize data in two different stores and implement a link between them.

### Data modeling
- [Modeling data](https://developer.apple.com/documentation/coredata/modeling-data) - Configure the data model file to contain your app's object graph.
- [Core Data model](https://developer.apple.com/documentation/coredata/core-data-model) - Describe your app's object structure.

### Fetch requests
Core Data retrieves persisted data to be used by your app.

- **NSFetchRequest** - A description of search criteria used to retrieve data from a persistent store.
- **NSAsynchronousFetchRequest** - A fetch request that retrieves results asynchronously and supports progress notification.
- **NSAsynchronousFetchResult** - A fetch result object that encompasses the response from an executed asynchronous fetch request.
- **NSFetchedResultsController** - A controller that you use to manage the results of a Core Data fetch request and to display data to the user.

### SwiftData migration and coexistence
- [Adopting SwiftData for a Core Data app](https://developer.apple.com/documentation/coredata/adopting-swiftdata-for-a-core-data-app) - Persist data in your app intuitively with the Swift native persistence framework.

### CloudKit mirroring
- [Mirroring a Core Data store with CloudKit](https://developer.apple.com/documentation/coredata/mirroring-a-core-data-store-with-cloudkit) - Back user interfaces with a local replica of a CloudKit private database.
- [Synchronizing a local store to the cloud](https://developer.apple.com/documentation/coredata/synchronizing-a-local-store-to-the-cloud) - Share data between a user's devices and other iCloud users.
- **NSPersistentCloudKitContainer** - A container that encapsulates the Core Data stack in your app, and mirrors select persistent stores to a CloudKit private database.
- **NSPersistentCloudKitContainerOptions** - An object that customizes how a store description aligns with a CloudKit database.
- [Sharing Core Data objects between iCloud users](https://developer.apple.com/documentation/coredata/sharing-core-data-objects-between-icloud-users) - Use Core Data and CloudKit to synchronize data between devices of an iCloud user and share data between different iCloud users.

### Change processing
- [Accessing data when the store changes](https://developer.apple.com/documentation/coredata/accessing-data-when-the-store-changes) - Use query generations with a SQLite/WAL store to control which store changes a context sees.
- [Consuming relevant store changes](https://developer.apple.com/documentation/coredata/consuming-relevant-store-changes) - Filter store transactions for changes relevant to the current view.
- [Persistent history](https://developer.apple.com/documentation/coredata/persistent-history) - Use persistent history tracking to determine what changes have occurred in the store since the enabling of persistent history tracking.

### Background tasks
- [Using Core Data in the background](https://developer.apple.com/documentation/coredata/using-core-data-in-the-background) - Use Core Data in both a single-threaded and multithreaded app.
- [Loading and Displaying a Large Data Feed](https://developer.apple.com/documentation/swiftui/loading-and-displaying-a-large-data-feed) - Consume data in the background, and lower memory use by batching imports and preventing duplicate records.
- [Conflict resolution](https://developer.apple.com/documentation/coredata/conflict-resolution) - Detect and resolve conflicts that occur when data is changed on multiple threads.
- [Batch processing](https://developer.apple.com/documentation/coredata/batch-processing) - Use batch processes to manage large data changes.

### Data model migration
Core Data has built-in data migration tools to help synchronize your app's data with the current data model.
- [Migrating your data model automatically](https://developer.apple.com/documentation/coredata/migrating-your-data-model-automatically) - Enable lightweight migrations to keep your data model and the underlying data in a consistent state.
- [Staged migrations](https://developer.apple.com/documentation/coredata/staged-migrations) - Migrate complex data models containing changes that are incompatible with lightweight migrations.
- [Manual migrations](https://developer.apple.com/documentation/coredata/manual-migrations) - Migrate elaborate data models with changes that go beyond the capabilities of both lightweight and staged migrations.

### Related types
- [Core Data Constants](https://developer.apple.com/documentation/coredata/core-data-constants) - Keys to use with persistent stores and notifications from Core Data.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreData)*
