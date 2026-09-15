# CloudKit

Store structured app and user data in iCloud containers that all users of your app can share.

**Platforms:** iOS 8.0+ | iPadOS 8.0+ | Mac Catalyst 13.0+ | macOS 10.10+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 3.0+

## Overview

The CloudKit framework provides interfaces for moving data between your app and your iCloud containers. You use CloudKit to store your app's existing data in the cloud so that the user can access it on multiple devices. You can also store data in a public area where all users can access it.

### Using the CloudKit framework

CloudKit transfers records to and from iCloud; your app still needs an offline-data strategy. Native clients can query permitted public records without a signed-in iCloud account, but **saving records to the public database also requires an active account**. Private-database access requires an account, and public record permissions can be restricted. See [`CKContainer`](https://developer.apple.com/documentation/cloudkit/ckcontainer) and [`publicCloudDatabase`](https://developer.apple.com/documentation/cloudkit/ckcontainer/publicclouddatabase).

[`CKRecord`](https://developer.apple.com/documentation/cloudkit/ckrecord) stores typed key-value fields and relationships. Development can infer a schema from records, but production rejects undeployed record types and fields; prepare and deploy compatible schema changes before clients use them. Database APIs, operation objects, and `CKSyncEngine` provide different levels of transfer/synchronization support.

Before using CloudKit, make sure it's the most suitable option for your app. For more information, see Deciding whether CloudKit is right for your app.

Note: The classes of the CloudKit framework aren't for subclassing. Use these classes as-is to save, retrieve, and manipulate data in iCloud. In addition, many of the protocols of this framework aren't for adoption by classes outside of CloudKit and UIKit. Each protocol reference document includes information about whether you can adopt the protocol in your own classes.

## OS 27 sharing regression check

The [iOS & iPadOS 27 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes) mark administrator self-demotion in a `CKShare` as **resolved** (177621316): saving a change of the administrator's own role to `CKShareParticipantRole.privateUser` previously had no effect. Retest sharing and permission transitions instead of treating self-demotion as permanently unavailable.

Keep CloudKit synchronization separate from local persistence and schema migration. [SwiftData's OS 27 observers](SwiftData.md#os-27-queries-and-change-observation) can respond to external/store changes, but do not remove the need to handle offline data, conflicts, and account state.

## Topics

### Essentials
- [Deciding whether CloudKit is right for your app](https://developer.apple.com/documentation/cloudkit/deciding-whether-cloudkit-is-right-for-your-app) - Explore the various options you have for using iCloud to store and sync your app's data.
- [Enabling CloudKit in Your App](https://developer.apple.com/documentation/cloudkit/enabling-cloudkit-in-your-app) - Configure your app to store data in iCloud using CloudKit.

### Schemas
- [Designing and Creating a CloudKit Database](https://developer.apple.com/documentation/cloudkit/designing-and-creating-a-cloudkit-database) - Create a schema to store your app's objects as records in iCloud using CloudKit.
- [Managing iCloud Containers with CloudKit Database App](https://developer.apple.com/documentation/cloudkit/managing-icloud-containers-with-cloudkit-database-app) - Inspect and modify the schema and data for your app's iCloud container.
- **CKRecordZone** - A database partition that contains related records.
- **CKRecord** - A collection of key-value pairs that store your app's data.
- **Reference** - A relationship between two records in a record zone.
- **CKAsset** - An external file that belongs to a record.
- [Integrating a Text-Based Schema into Your Workflow](https://developer.apple.com/documentation/cloudkit/integrating-a-text-based-schema-into-your-workflow) - Define and update your schema with the CloudKit Schema Language.

### Records
- **Local Records** - Manipulate records on-device and save changes to the server.
- **Remote Records** - Use subscriptions and change tokens to efficiently manage modifications to remote records.
- [`CKSyncEngine`](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5) - Manages private/shared-database synchronization, not public-database sync. Introduced in the iOS 17/macOS 14 generation; your app must persist its state between launches.
- **Shared Records** - Share one or more records with other iCloud users.

### User discovery
- **CKUserIdentity** - The identity of a user.
- **LookupInfo** - The criteria to use when searching for discoverable iCloud users.

### Core objects
- **CKContainer** - A conduit to your app's databases.
- **CKDatabase** - An object that represents a collection of record zones and subscriptions.
- **CKOperationGroup** - An explicit association between two or more operations.

### Privacy
- [Encrypting User Data](https://developer.apple.com/documentation/cloudkit/encrypting-user-data) - Deploy industry-standard security technologies using CloudKit encryption.
- [Providing User Access to CloudKit Data](https://developer.apple.com/documentation/cloudkit/providing-user-access-to-cloudkit-data) - Provide users access to the data your app stores on their behalf.
- [Changing Access Controls on User Data](https://developer.apple.com/documentation/cloudkit/changing-access-controls-on-user-data) - Restrict access to or remove restrictions from a user's data at their request.
- **CKFetchWebAuthTokenOperation** - An operation that creates an authentication token for use with CloudKit web services.
- [Responding to Requests to Delete Data](https://developer.apple.com/documentation/cloudkit/responding-to-requests-to-delete-data) - Provide options for users to delete their CloudKit data from your app.
- [Identifying an App's Containers](https://developer.apple.com/documentation/cloudkit/identifying-an-app-s-containers) - Use Xcode's Project navigator to find the identifiers of active CloudKit containers.

### Errors
- **CKErrorDomain** - The error domain for CloudKit errors.
- **CKError** - A type that describes a CloudKit error.
- **Code** - The error codes that CloudKit returns.
- **CKErrorRetryAfterKey** - The key to retrieve the number of seconds to wait before you retry a request.
- **CKErrorUserDidResetEncryptedDataKey** - The key that determines whether CloudKit deletes a record zone because of a user action.
- **CKPartialErrorsByItemIDKey** - The key to retrieve partial errors.
- **Record Changed Error Keys** - Constants that represent conflicting records in a save operation.

### Deprecated
- **Deprecated Symbols** - Review deprecation guidance and replacements; deprecation alone does not mean an API has been removed.

### Classes
- [`CKShareRequestAccessOperation`](https://developer.apple.com/documentation/cloudkit/cksharerequestaccessoperation) - A `CKOperation` subclass that requests access using share URLs; available from version 26 on supported platforms.

### Variables
- **CKRecordParentKey**
- **CKRecordShareKey**
- **CKRecordTypeShare**
- **CKRecordTypeUserRecord**
- **CKRecordZoneDefaultName**
- **CKShareThumbnailImageDataKey**
- **CKShareTitleKey**
- **CKShareTypeKey**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CloudKit)*
