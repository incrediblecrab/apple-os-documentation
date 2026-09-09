# AppMigrationKit

Transfer an app's on-device data once between an Apple device and a device running another platform.

**Platforms:** iOS 26.1+ | iPadOS 26.1+

## Overview

AppMigrationKit participates in system-managed import and export through an app extension. It is for cross-platform migration, such as between an iPhone and an Android device, **not** migration between two iOS/iPadOS devices. It does not operate in compatible iOS apps on visionOS or macOS, and calls from Mac Catalyst apps have no effect.

The framework landing page and required entitlement list iOS/iPadOS 26.1; several individual protocol pages list 26.0. Follow the framework/entitlement requirements and verify the SDK declarations when choosing deployment targets. This is not an OS 27-only framework.

## Extension and authorization

Adopt [`AppMigrationExtension`](https://developer.apple.com/documentation/appmigrationkit/appmigrationextension) plus at least one import/export subprotocol. The base protocol alone does not supply an operation. Access the containing app's data through `appContainer`.

The extension needs [`com.apple.developer.app-migration.data-container-access`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.app-migration.data-container-access). Its value is a one-element string array containing **the containing app's bundle identifier**, not an arbitrary list of containers.

## Export

Use [`ResourcesExporting`](https://developer.apple.com/documentation/appmigrationkit/resourcesexporting) when the destination needs no special options, or [`ResourcesExportingWithOptions`](https://developer.apple.com/documentation/appmigrationkit/resourcesexportingwithoptions) when it does. Both are for resources that can be copied in their existing format; they are not database-format converters.

Provide a size estimate and format version, then feed files incrementally to the asynchronous, throwing [`ResourcesArchiver.appendItem(at:pathInArchive:)`](https://developer.apple.com/documentation/appmigrationkit/resourcesarchiver/appenditem(at:pathinarchive:)) method. The system prevents the app and its extensions from launching during export. Keep making progress rather than building a second complete archive locally, which can exhaust storage.

[`ResourcesArchiver`](https://developer.apple.com/documentation/appmigrationkit/resourcesarchiver) propagates cancellation errors. Do not catch and suppress them: Apple documents that doing so causes the extension to be killed.

## Import and recovery

Adopt [`ResourcesImporting`](https://developer.apple.com/documentation/appmigrationkit/resourcesimporting), implement [`importResources(at:request:)`](https://developer.apple.com/documentation/appmigrationkit/resourcesimporting/importresources(at:request:)), and report [`resourcesImportProgress`](https://developer.apple.com/documentation/appmigrationkit/resourcesimporting/resourcesimportprogress). Import runs after installation and before the app becomes launchable.

On an import error, the system clears the containing app's data container to prevent partial state, **but not app group containers**. Design cleanup for migration-owned group data without deleting unrelated shared data. Retrieve cloud-hosted content after migration rather than including it merely because the source app can access it.

At the app's first launch, inspect [`MigrationStatus.importStatus`](https://developer.apple.com/documentation/appmigrationkit/migrationstatus/importstatus). After handling and communicating a successful import, call [`clearImportStatus()`](https://developer.apple.com/documentation/appmigrationkit/migrationstatus/clearimportstatus()) to avoid repeating the notification.

## Testing and related technologies

[`AppMigrationTester`](https://developer.apple.com/documentation/appmigrationkit/appmigrationtester) exercises export/import controllers from unit tests hosted by the containing app. It is test-only and does not operate in production. Cover interruption, invalid input, low storage, format-version changes, and import recovery. See [XCTest](XCTest.md) for host-test tooling.

- [Core Data](CoreData.md) and [SwiftData](SwiftData.md) migrate persistent-store schemas; this framework transports compatible data between platforms.
- [App Data Transfer](AppDataTransfer.md) and [Account Data Transfer](AccountDataTransfer.md) cover different transfer services.
- [Extension Foundation](ExtensionFoundation.md) supplies the extension infrastructure.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/appmigrationkit)*
