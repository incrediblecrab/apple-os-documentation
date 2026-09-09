# CloudKit JS

Provide access from your web app to your CloudKit app's containers and databases.

**Platforms:** CloudKit JS 1.0+

## Overview

Use CloudKit JS to build a web interface to a CloudKit container's public, private, and shared databases. Apple's setup flow assumes a CloudKit-enabled app and container; configure web-service access before using the JavaScript client. Shared access uses [`sharedCloudDatabase`](https://developer.apple.com/documentation/cloudkitjs/cloudkit.container/sharedclouddatabase) for records other people have shared with the signed-in user.

### Before You Begin

Set up your app's containers and configure CloudKit JS.

#### Create your app's containers and schema

Configure your CloudKit-enabled app's containers and schema using Xcode and [CloudKit Console](https://icloud.developer.apple.com/). The archived [CloudKit Quick Start](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitQuickStart/Introduction/Introduction.html) describes the native-app workflow and uses the older “CloudKit Dashboard” name.

For current token setup, open the CloudKit Database app in the console, select the container, and choose **Settings > Tokens & Keys**.

Use an API token for website or embedded-web-view access that may authenticate a user. Follow [Obtaining an API Token for an iCloud Container](https://developer.apple.com/documentation/cloudkit/obtaining-an-api-token-for-an-icloud-container), including allowed-origin configuration.

Use a server-to-server key for administrative access to the public database from a trusted server process or script, not for a browser's user sign-in flow. See [Accessing CloudKit Using a Server-to-Server Key](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/SettingUpWebServices.html#//apple_ref/doc/uid/TP40015240-CH24-SW6).

#### Embed CloudKit JS in your webpage

Embed CloudKit JS using Apple's hosted script. The path is case-sensitive:

```html
<script src="https://cdn.apple-cloudkit.com/ck/2/cloudkit.js"></script>
```

The `/ck/2/` path selects the version 2 library line; it is not an exact patch-version pin.

This library version is independent of Safari or OS versions. Keep server-to-server keys on your server; a browser-delivered script must not embed a private signing key. For Safari 27 browser compatibility checks, see the [migration guide](../guides/safari27-migration.md).

#### Enable JavaScript strict mode

To enable strict mode for an entire script, put "use strict" before any other statements.

```javascript
"use strict";
```

#### Configure CloudKit JS

Use [`CloudKit.configure`](https://developer.apple.com/documentation/cloudkitjs/cloudkit/configure) to provide container identifiers, authentication configuration, and the development or production environment. See [CloudKit JS Data Types](https://developer.apple.com/documentation/cloudkitjs/cloudkit-js-data-types) for the configuration dictionaries.

[`CloudKit.getDefaultContainer()`](https://developer.apple.com/documentation/cloudkitjs/cloudkit/getdefaultcontainer) returns the first container in the configuration list. Obtain the required database from that `CloudKit.Container`; don't assume every configured container is the default.

### Next Steps

Explore the [hosted CloudKit Catalog](https://cdn.apple-cloudkit.com/cloudkit-catalog/) and use the API reference for individual contracts. The [archived Cocoa/JavaScript sample](https://developer.apple.com/library/archive/samplecode/CloudAtlas/Introduction/Intro.html) was last revised in September 2016; its old Xcode and Safari requirements are not current deployment guidance.

The following resources provide more information about CloudKit:

- [CloudKit Quick Start](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitQuickStart/Introduction/Introduction.html) provides the archived native-app setup walkthrough.
- [CloudKit](CloudKit.md) covers native APIs and production schema/sync responsibilities.
- [CloudKit Web Services Reference](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/) describes the HTTP interface to containers and databases.
- [iCloud Design Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/Chapters/Introduction.html) is an archived overview of CloudKit, key-value storage, and document storage.

## Topics

### Classes
- **CloudKit** - Use the CloudKit namespace to configure CloudKit JS, and to access app containers and global constants.
- **CloudKit.CKError** - A CloudKit.CKError object encapsulates an error that may occur when you use CloudKit JS. This includes CloudKit server errors and local errors.
- **CloudKit.Container** - A CloudKit.Container object provides access to an app container, and through the app container, access to its databases. It also contains methods for authenticating and fetching users.
- [`CloudKit.Database`](https://developer.apple.com/documentation/cloudkitjs/cloudkit.database) - Access to a container database; obtain the public, private, or shared instance from `CloudKit.Container`.
- **CloudKit.DatabaseChangesResponse** - A CloudKit.DatabaseChangesResponse object encapsulates the results of fetching changed record zones in a database.
- **CloudKit.Notification** - A push notification associated with a saved database subscription. Create subscriptions with [`CloudKit.Database.saveSubscriptions`](https://developer.apple.com/documentation/cloudkitjs/cloudkit.database/savesubscriptions), not `saveSubscription`.
- **CloudKit.QueryNotification** - A CloudKit.QueryNotification object represents a push notification that was generated by a subscription object. A query notification is triggered by subscriptions where the subscriptionType key is query. Use a CloudKit.QueryNotification object to get information about the record that changed. To create query subscriptions and handle push notifications, see the saveSubscriptions method in CloudKit.Database.
- **CloudKit.QueryResponse** - A CloudKit.QueryResponse object encapsulates the results of using a query to fetch records
- **CloudKit.RecordInfosResponse** - A CloudKit.RecordInfosResponse object encapsulates the results of fetching information about records in general and shared records in particular.
- [`CloudKit.RecordsBatchBuilder`](https://developer.apple.com/documentation/cloudkitjs/cloudkit.recordsbatchbuilder) - Builds a batch of record mutations; obtain it from `newRecordsBatch()`, add operations, then call `commit()`. It is not a completed-response object.
- **CloudKit.RecordsResponse** - A CloudKit.RecordsResponse object encapsulates the results of fetching records.
- **CloudKit.RecordZoneChangesResponse** - The CloudKit.RecordZoneChangesResponse object encapsulates the results of fetching changes to one or more record zones.
- [`CloudKit.RecordZoneNotification`](https://developer.apple.com/documentation/cloudkitjs/cloudkit.recordzonenotification) - Signals changes covered by a zone subscription (`subscriptionType: "zone"`). Fetch the zone's changes to discover the affected records; a notification is not a replacement for the change-fetch response.
- **CloudKit.RecordZonesResponse** - A CloudKit.RecordZonesResponse object encapsulates the results of database operations on a record zone.
- [`CloudKit.Response`](https://developer.apple.com/documentation/cloudkitjs/cloudkit.response) - Base response interface returned through specialized response objects, not a type to instantiate directly. Inspect `hasErrors` and `errors` even in a fulfilled promise; the subscription examples explicitly handle this case.
- [`CloudKit.ShareRecordType`](https://developer.apple.com/documentation/cloudkitjs/cloudkit.sharerecordtype) - Names for the share record type and its title, thumbnail, and type fields.
- **CloudKit.SubscriptionsResponse** - A CloudKit.SubscriptionsResponse object encapsulates the results of database operations on subscriptions.
- **CloudKit.UserIdentitiesResponse** - A CloudKit.UserIdentitiesResponse object encapsulates the results of fetching user identities.

### Reference
- [CloudKit JS Data Types](https://developer.apple.com/documentation/cloudkitjs/cloudkit-js-data-types) - Configuration and data dictionaries not described by individual class references.
- [CloudKit JS Enumerations](https://developer.apple.com/documentation/cloudkitjs/cloudkit-js-enumerations)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CloudKitJS)*
