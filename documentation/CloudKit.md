# CloudKit

Store structured app and user data in iCloud containers that all users of your app can share.

**Platforms:** iOS 8.0+ | iPadOS 8.0+ | Mac Catalyst 13.0+ | macOS 10.10+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 3.0+

## Overview

The CloudKit framework provides interfaces for moving data between your app and your iCloud containers. You use CloudKit to store your app's existing data in the cloud so that the user can access it on multiple devices. You can also store data in a public area where all users can access it.

### Using the CloudKit framework

CloudKit isn't a replacement for your app's existing data objects. Instead, CloudKit provides complementary services for managing the transfer of data to and from iCloud servers. Because it provides minimal offline caching support, CloudKit relies on the presence of the network and, optionally, a valid iCloud account. A valid iCloud account is only necessary when you want to save data that is specific to a single user. Apps can always store data in a public area that is readable by all users.

Records are at the heart of all data transactions in CloudKit. A record is a dictionary of key-value pairs that represents the data you want to save. You can add new keys and values to records at any time, and you can create links between related records to organize your data. The CKRecord class defines the interfaces for managing the contents of records. CloudKit also relies heavily on the use of Operation objects to manage the asynchronous transfer of data to and from the server.

Before using CloudKit, make sure it's the most suitable option for your app. For more information, see Deciding whether CloudKit is right for your app.

Note: The classes of the CloudKit framework aren't for subclassing. Use these classes as-is to save, retrieve, and manipulate data in iCloud. In addition, many of the protocols of this framework aren't for adoption by classes outside of CloudKit and UIKit. Each protocol reference document includes information about whether you can adopt the protocol in your own classes.

## Topics

### Essentials
- [Deciding whether CloudKit is right for your app](https://developer.apple.com/documentation/CloudKit/deciding_whether_cloudkit_is_right_for_your_app) - Explore the various options you have for using iCloud to store and sync your app's data.
- [Enabling CloudKit in Your App](https://developer.apple.com/documentation/CloudKit/enabling_cloudkit_in_your_app) - Configure your app to store data in iCloud using CloudKit.

### Schemas
- [Designing and Creating a CloudKit Database](https://developer.apple.com/documentation/CloudKit/designing_and_creating_a_cloudkit_database) - Create a schema to store your app's objects as records in iCloud using CloudKit.
- [Managing iCloud Containers with CloudKit Database App](https://developer.apple.com/documentation/CloudKit/managing_icloud_containers_with_cloudkit_database_app) - Inspect and modify the schema and data for your app's iCloud container.
- **CKRecordZone** - A database partition that contains related records.
- **CKRecord** - A collection of key-value pairs that store your app's data.
- **Reference** - A relationship between two records in a record zone.
- **CKAsset** - An external file that belongs to a record.
- [Integrating a Text-Based Schema into Your Workflow](https://developer.apple.com/documentation/CloudKit/integrating_a_text-based_schema_into_your_workflow) - Define and update your schema with the CloudKit Schema Language.

### Records
- **Local Records** - Manipulate records on-device and save changes to the server.
- **Remote Records** - Use subscriptions and change tokens to efficiently manage modifications to remote records.
- **CKSyncEngine** - An object that manages the synchronization of local and remote record data.
- **Shared Records** - Share one or more records with other iCloud users.

### User discovery
- **CKUserIdentity** - The identity of a user.
- **LookupInfo** - The criteria to use when searching for discoverable iCloud users.

### Core objects
- **CKContainer** - A conduit to your app's databases.
- **CKDatabase** - An object that represents a collection of record zones and subscriptions.
- **CKOperationGroup** - An explicit association between two or more operations.

### Privacy
- [Encrypting User Data](https://developer.apple.com/documentation/CloudKit/encrypting_user_data) - Deploy industry-standard security technologies using CloudKit encryption.
- [Providing User Access to CloudKit Data](https://developer.apple.com/documentation/CloudKit/providing_user_access_to_cloudkit_data) - Provide users access to the data your app stores on their behalf.
- [Changing Access Controls on User Data](https://developer.apple.com/documentation/CloudKit/changing_access_controls_on_user_data) - Restrict access to or remove restrictions from a user's data at their request.
- **CKFetchWebAuthTokenOperation** - An operation that creates an authentication token for use with CloudKit web services.
- [Responding to Requests to Delete Data](https://developer.apple.com/documentation/CloudKit/responding_to_requests_to_delete_data) - Provide options for users to delete their CloudKit data from your app.
- [Identifying an App's Containers](https://developer.apple.com/documentation/CloudKit/identifying_an_app_s_containers) - Use Xcode's Project navigator to find the identifiers of active CloudKit containers.

### Errors
- **CKErrorDomain** - The error domain for CloudKit errors.
- **CKError** - A type that describes a CloudKit error.
- **Code** - The error codes that CloudKit returns.
- **CKErrorRetryAfterKey** - The key to retrieve the number of seconds to wait before you retry a request.
- **CKErrorUserDidResetEncryptedDataKey** - The key that determines whether CloudKit deletes a record zone because of a user action.
- **CKPartialErrorsByItemIDKey** - The key to retrieve partial errors.
- **Record Changed Error Keys** - Constants that represent conflicting records in a save operation.

### Deprecated
- **Deprecated Symbols** - Review unsupported symbols and their replacements.

### Classes
- **CKShareRequestAccessOperation** - Beta

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