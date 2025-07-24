# File Provider

An extension other apps use to access files and folders managed by your app and synced with a remote storage.

**Platforms:** iOS 11.0+ | iPadOS 11.0+ | Mac Catalyst 11.0+ | macOS 10.15+ | visionOS 1.0+

## Overview

If your app focuses on providing and syncing user documents from remote storage, you can implement a File Provider extension to give users access to those documents when they're using other apps. If you just need to share local documents, see Share files locally below.

A diagram that depicts the interaction between an app and your server facilitated by a File Provider extension. The app communicates with the document browser, which requests data to the File Provider extension. The File Provider extension syncs updates with the remote server.

The framework has two different starting points for building your File Provider extension.

**NSFileProviderReplicatedExtension**  
The system manages the content accessed through the File Provider extension. Available in macOS 11+ and iOS 16+.

**NSFileProviderExtension**  
The extension hosts and manages the files accessed through the File Provider extension. Available in iOS 11+.

The replicated extension takes responsibility for monitoring and managing the local copies of your documents. The file provider focuses on syncing data between the local copy and the remote storage—uploading any local changes and downloading any remote changes. For more information, see Replicated File Provider extension.

The nonreplicated extension manages a local copy of the extension's content, including creating and managing placeholders for remote files. It also syncs the content with your remote storage. For more information, see Nonreplicated File Provider extension.

### Share files locally

You don't need a File Provider extension to allow access to documents that your app stores locally.

In iOS, to give other apps access to the files in your Documents directory, set the following keys in your app's Info tab or its Info.plist file. For document browser-based apps, set the UISupportsDocumentBrowser key. For all other apps, set both the UIFileSharingEnabled and LSSupportsOpeningDocumentsInPlace keys.

After you set these keys, other apps can open and edit the contents of your Documents directory in place. Your files also appear in both the Files app and the document browser. For more information, see the UIDocumentBrowserViewController class.

## Topics

### Essentials
- [File Provider updates](https://developer.apple.com/documentation/fileprovider/fileprovider_updates) - Learn about important changes to File Provider.

### Extension types
- [Replicated File Provider extension](https://developer.apple.com/documentation/fileprovider/replicated_file_provider_extension) - Build a File Provider extension that syncs the local copies of your files with your remote storage.
- [Nonreplicated File Provider extension](https://developer.apple.com/documentation/fileprovider/nonreplicated_file_provider_extension) - Build a File Provider extension that hosts and manages the user's local files.

### Extension management
- **class NSFileProviderManager** - A manager object that you use to communicate with the file provider from either your app or your File Provider extension.

### Provided items
- **typealias NSFileProviderItem** - An item the File Provider extension manages.
- **protocol NSFileProviderItemProtocol** - A protocol that defines the properties of an item managed by the File Provider extension.
- **struct NSFileProviderItemIdentifier** - A unique identifier for an item managed by the File Provider extension.
- **struct NSFileProviderItemCapabilities** - An item's capabilities, which define the actions that the user can perform in the document browser.
- **struct NSFileProviderTypeAndCreator** - A structure that contains the file type and file creator codes for an item.

### Cloud search
- **protocol NSFileProviderSearching** - A protocol you implement to support searching in your file provider.

### Domains
- **class NSFileProviderDomain** - A File Provider extension's domain.

### Errors
- **struct NSFileProviderError** - A structure that contains information about File Provider extension errors.
- **enum Code** - The error codes for the File Provider extension.
- **let NSFileProviderErrorDomain: String** - The error domain for the File Provider extension.
- **let NSFileProviderErrorItemKey: String** - The key for accessing information about sync-related errors.
- **let NSFileProviderErrorNonExistentItemIdentifierKey: String** - The key for accessing the specified item's identifier when the item doesn't exist.
- **let NSFileProviderErrorCollidingItemKey: String** - The key for accessing the existing item from a filename collision error's user info dictionary.

### Data export
- [Exporting file provider metrics data](https://developer.apple.com/documentation/fileprovider/exporting_file_provider_metrics_data) - Download and analyze usage, consistency, and error data.

### Global variables and macros
- **Global variables and macros**

### Structures
- **struct NSFileProviderUserInfoKey**
- **struct NSFileProviderVolumeUnsupportedReason** - Constants that describe why an external volume might not be eligible for storing a domain.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/FileProvider)*