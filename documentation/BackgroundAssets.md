# Background Assets

Schedule background downloads of large assets during or after app installation, when the app updates, and periodically while the app remains on-device.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 16.0+ | macOS 13.0+ | tvOS 18.4+ | visionOS 2.4+

## Overview

Background Assets delivers additional app content, such as level data, models, textures, and videos. Managed asset packs let the system coordinate downloads, updates, and compression. Choose Apple hosting or a self-hosted configuration according to the distribution and delivery requirements of your app.

The umbrella catalog lists the versions above, but original download types such as `BADownloadManager`, `BAURLDownload`, and `BADownloaderExtension` require **iOS/iPadOS/Mac Catalyst 16.1**, not 16.0. Their macOS, tvOS, and native visionOS minima match the header. **Managed asset packs**, including `AssetPackManager`, require iOS/iPadOS 26.0, Mac Catalyst 26.0, macOS 26.0, tvOS 26.0, or visionOS 26.0 and later. Do not use the older framework minimum as an availability check for these newer APIs.

### visionOS availability

For compatible iPad and iPhone apps, Background Assets is available in visionOS 1.0 and later. For apps built for visionOS, Background Assets is available in visionOS 2.4 and later.

For managed downloads, create asset packs with `essential`, `prefetch`, or `onDemand` download policies and add the corresponding Background Download extension. Self-hosted packs use `ManagedDownloaderExtension`; Apple-hosted packs use StoreKit's [`StoreDownloaderExtension`](https://developer.apple.com/documentation/storekit/storedownloaderextension), which inherits from it. Follow each protocol's rules for inherited callbacks: `ManagedDownloaderExtension` allows the optional authentication-challenge handler `backgroundDownload(_:didReceive:)`, but otherwise supplies the unmanaged lifecycle implementation. `StoreDownloaderExtension` prohibits implementing the inherited `BADownloaderExtension` requirements for which it supplies defaults.

Apple-hosted projects share an app group between the app and extension, specify its string identifier with `BAAppGroupID`, and set the Boolean keys `BAHasManagedAssetPacks` and `BAUsesAppleHosting` to `YES`. Follow the [configuration guide](https://developer.apple.com/documentation/backgroundassets/downloading-apple-hosted-asset-packs); do not mix in unrelated unmanaged-download Info.plist settings. Configure the extension before first accessing `AssetPackManager`, because that first access opts the app into managed asset-pack behavior.

The original `BADownloadManager`, `BADownloaderExtension`, and `BAURLDownload` interfaces remain relevant for apps that manage individual downloads from their own servers. They are not interchangeable with the managed asset-pack lifecycle.

**Important**: Use the framework only to download additional assets for your app; don't use it for any other purposes. For example, don't collect or transmit data to identify a user or device or to perform advertising or advertising measurement.

### OS 27: ODR migration and localized asset packs

**Reviewed September 8, 2026:** The iOS/iPadOS, tvOS, and visionOS 27 release notes deprecate **On Demand Resources and `NSBundleResourceRequest`** and direct developers to Background Assets. This is migration guidance, not a claim that existing ODR content stops working immediately. See the [migration guide](../guides/background-assets-migration.md) for deployment fallbacks and the distinction between downloads and background computation.

Localized asset packs are new in the 27 generation for iOS/iPadOS, Mac Catalyst, macOS, tvOS, and visionOS. Xcode 27's `ba-package` manifest template adds a `language` key. It accepts an ISO-639 language identifier with optional region and script; variant subtags and other BCP-47 extensions are not supported.

The manifest's `localizedAssetPacks` and read-only `resolvedLanguage` describe packs matching language preferences. An app-specific language choice can override `AssetPackManager.resolvedLanguage`; setting it back to `nil` restores system selection. Changing this property alone does not download or remove packs: call `reconcilePreferredLanguages()` to reconcile storage. Reconciliation leaves manually downloaded localized packs in place.

For multiple languages, request the needed packs together and use language-aware content accessors to avoid ambiguous paths. Batch local-availability failures provide successful packs separately from the failures, so do not discard completed downloads or assume the entire batch succeeded.

### Scheduling and storage constraints

An essential download policy is not a guarantee that content is present when your code needs it. A successful `ensureLocalAvailability` call establishes readiness; handle network failures even for essential packs. Show download progress, allow cancellation through its `Progress` object, and provide retry or reduced-content behavior.

Background Assets is not a grant of arbitrary background CPU or Neural Engine time. The system controls scheduling; your app and extension can be suspended. Use [BackgroundTasks](BackgroundTasks.md) for eligible processing, or a background `URLSession` for ordinary file transfers.

Managed packs are not automatically purged merely because the app stops using them. Use `remove(assetPackWithID:)` when a pack is no longer needed, and reconcile localized packs deliberately.

## Topics

### Essentials
- [Creating managed asset packs](https://developer.apple.com/documentation/backgroundassets/creating-managed-asset-packs) - Package content and choose download policies.
- [Downloading Apple-hosted asset packs](https://developer.apple.com/documentation/backgroundassets/downloading-apple-hosted-asset-packs) - Configure the app and extension and access downloaded content.
- [Testing asset packs locally](https://developer.apple.com/documentation/backgroundassets/testing-asset-packs-locally) - Test managed packs with Xcode's local mock server.
- [Reducing download and storage demands with localized asset packs](https://developer.apple.com/documentation/backgroundassets/reducing-download-and-storage-demands-with-localized-asset-packs) - Configure language selection and language-aware content lookup.

### Managed Asset Packs
- **AssetPack** - An archive of assets that the system downloads together.
- **AssetPackManager** - An actor that manages asset packs.
- **ManagedDownloaderExtension** - An app extension that uses the system implementation to schedule asset-pack downloads automatically.
- **BAAppGroupID** - A string identifying the app group shared by the app and its asset-pack extension.
- **BAHasManagedAssetPacks** - A Boolean value that indicates whether you let the system automatically manage your asset packs.

### Apple-hosted Managed Asset Packs
- [StoreDownloaderExtension](https://developer.apple.com/documentation/storekit/storedownloaderextension) - StoreKit's managed-extension protocol for automatically scheduling Apple-hosted packs; available from 26.0.
- **BAUsesAppleHosting** - A Boolean value that indicates whether you use Apple's service to host your asset packs.

### Asset-pack Manifests
- **AssetPackManifest** - A representation of a manifest that lists asset packs that are available to download.

### Unmanaged Asset Downloads
- [Configuring an unmanaged Background Assets project](https://developer.apple.com/documentation/backgroundassets/configuring-an-unmanaged-background-assets-project) - Configure the original individual-download workflow.
- [Downloading essential assets in the background](https://developer.apple.com/documentation/backgroundassets/downloading-essential-assets-in-the-background) - Original-download sample requiring iOS/iPadOS/Mac Catalyst 16.4, macOS 13.3, tvOS 18.4, or visionOS 2.4 and later.
- **BAManifestURL** - The location URL of the app's manifest file that contains the names and sizes of assets.
- **BAInitialDownloadRestrictions** - The restrictions that apply to the set of assets that download immediately after app installation.
- **BAEssentialMaxInstallSize** - The combined maximum uncompressed size, in bytes, of essential assets downloaded before app launch.
- **BAMaxInstallSize** - The combined maximum uncompressed size, in bytes, of nonessential assets downloaded after the essential assets.
- **BADownloadManager** - An object that manages the queue of scheduled asset downloads.
- **BADownloaderExtension** - An interface for reacting to app life-cycle events and processing concluded asset downloads while your app isn't running.
- **BADownloaderExtensionConfiguration**
- **BAURLDownload** - An object that represents a remote asset to download.
- **BADownload** - An object that represents an in-progress or concluded asset download.

### Errors
- **ManagedBackgroundAssetsError** - An error for a managed asset pack.
- [AssetPackManager.LocalAvailabilityError](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/localavailabilityerror) - A 27.0+ batch-availability error with a set of successful packs and a dictionary mapping failed packs to their errors.
- **BAErrorDomain**
- **BAErrorCode**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/BackgroundAssets)*

*27 sources: [iOS/iPadOS release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes.md), [macOS release notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes.md), and [localized asset-pack documentation](https://developer.apple.com/documentation/backgroundassets/reducing-download-and-storage-demands-with-localized-asset-packs.md).*
