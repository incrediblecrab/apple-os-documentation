# Background Assets

Schedule background downloads of large assets during or after app installation, when the app updates, and periodically while the app remains on-device.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 16.0+ | macOS 13.0+ | tvOS 18.4+ | visionOS 2.4+

## Overview

With the Background Assets framework, you can improve the experience of your app or game by reducing or eliminating the time people have to wait while your app downloads any required assets at first launch. For example, a game might use the Background Assets framework to download additional content immediately after installation, such as level packs, 3D character models, and textures.

### visionOS availability

For compatible iPad and iPhone apps, Background Assets is available in visionOS 1.0 and later. For apps built for visionOS, Background Assets is available in visionOS 2.4 and later.

Add a Background Assets extension to your app's target, and let the system notify that extension about an app installation or subsequent update. Then use the download manager to schedule background downloads of required content from your servers or content delivery network (CDN), and have those downloads finish even when the app isn't running. Check for updated content when the system periodically launches the extension (dependent on app usage) and, when content is available, schedule it for immediate download. The framework leverages ExtensionKit and common types like URLRequest. For more information see, [2022 WWDC session 110403: Meet Background Assets](https://developer.apple.com/videos/play/wwdc2022/110403/).

**Important**: Use the framework only to download additional assets for your app; don't use it for any other purposes. For example, don't collect or transmit data to identify a user or device or to perform advertising or advertising measurement.

### The Background Assets extension life cycle

The system launches the extension during the first install and subsequent updates, before a person launches the app, and periodically in the background when the app isn't running. The sequence of events are:

1. A person installs or updates your app on the device.
2. The system prevents the app from launching and begins downloading your manifest file using the URL you provide.
3. During the manifest download, the system reports progress to the App Store.
4. When the download completes, the system launches your app extension, sending it a content request with the location of the manifest file on disk.
5. The extension uses the manifest file, which contains the asset URLs and file sizes, to return a set of download requests to the system.
6. The system pauses, or terminates, the extension and begins the downloads.
7. When the downloads complete, the system notifies the extension and allows the app to launch.

The flow for periodic content requests is identical to the app install and updates, except the system determines when periodic events occur, depending on a person's usage and their system settings. For example, the system factors in whether a person enables the Low Power Mode and Background App Refresh settings.

## Topics

### Essentials
- [Creating managed asset packs](https://developer.apple.com/documentation/backgroundassets/creating_managed_asset_packs) - Create managed asset packs, choose download options, and upload Apple-hosted asset packs to App Store Connect.
- [Downloading Apple-hosted asset packs](https://developer.apple.com/documentation/backgroundassets/downloading_apple-hosted_asset_packs) - Configure your project and write the code to download asset packs hosted by Apple.
- [Testing asset packs locally](https://developer.apple.com/documentation/backgroundassets/testing_asset_packs_locally) - Test your system-managed asset packs using a mock server on your Mac.

### Managed Asset Packs
- **AssetPack** - An archive of assets that the system downloads together. (Beta)
- **AssetPackManager** - An actor that manages asset packs. (Beta)
- **ManagedDownloaderExtension** - An app extension that uses the system implementation to schedule asset-pack downloads automatically. (Beta)
- **BAAppGroupID** - The app group identifier that you share between your app and the extension that uses asset packs.
- **BAHasManagedAssetPacks** - A Boolean value that indicates whether you let the system automatically manage your asset packs.

### Apple-hosted Managed Asset Packs
- **BAUsesAppleHosting** - A Boolean value that indicates whether you use Apple's service to host your asset packs.

### Self-hosted Unmanaged Asset Packs
- **AssetPackManifest** - A representation of a manifest that lists asset packs that are available to download. (Beta)

### Unmanaged Asset Downloads
- [Configuring your Background Assets project](https://developer.apple.com/documentation/backgroundassets/configuring_your_background_assets_project) - Edit your app and extension targets in your Xcode project to use Background Assets.
- [Downloading essential assets in the background](https://developer.apple.com/documentation/backgroundassets/downloading_essential_assets_in_the_background) - Fetch the assets your app requires before its first launch using an app extension and the Background Assets framework.
- **BAManifestURL** - The location URL of the app's manifest file that contains the names and sizes of assets.
- **BAInitialDownloadRestrictions** - The restrictions that apply to the set of assets that download immediately after app installation.
- **BAEssentialMaxInstallSize** - The combined, maximum size of the essential assets that the system downloads before it launches your app in bytes.
- **BAMaxInstallSize** - The combined, maximum size, in bytes, of the non-essential assets that download immediately after app installation.
- **BADownloadManager** - An object that manages the queue of scheduled asset downloads.
- **BADownloaderExtension** - An interface for reacting to app life-cycle events and processing concluded asset downloads while your app isn't running.
- **BADownloaderExtensionConfiguration**
- **BAURLDownload** - An object that represents a remote asset to download.
- **BADownload** - An object that represents an in-progress or concluded asset download.

### Errors
- **ManagedBackgroundAssetsError** - An error for a managed asset pack. (Beta)
- **BAErrorDomain**
- **BAErrorCode**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/BackgroundAssets)*