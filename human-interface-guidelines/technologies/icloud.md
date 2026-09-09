# iCloud

iCloud helps people access the content they care about — photos, videos, documents, and more — across their supported devices without manually initiating each synchronization.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

A fundamental design goal for iCloud integration is transparency: people shouldn't need to manage where content resides. Aim to provide the latest content while handling offline access, pending updates, and conflicts explicitly when necessary.

## Topics

### Best Practices

- **Make it easy to use your app with iCloud** - People turn on iCloud in Settings and expect apps to work with it automatically. If you think people might want to choose whether to use iCloud with your app, show a simple option the first time your app opens that provides a choice between using iCloud for all data or not at all.
- **Avoid asking which documents to keep in iCloud** - Most people expect all of their content to be available in iCloud and don't want to manage the storage of individual documents. Consider how your app handles and exposes content, and try to perform more file-management tasks automatically.
- **Keep content up to date when possible** - In an app that supports iCloud, it's best when people always have access to the most recent content. However, you need to balance this experience with respect to device storage and bandwidth constraints. If your app works with very large documents, it may be better to let people control when updated content is downloaded.
- **Respect iCloud storage space** - iCloud storage is limited, with additional capacity available through paid plans. Store information people create and understand rather than app resources or regenerable content. On devices using iCloud Backup, eligible app data can be backed up even if your app doesn't implement iCloud synchronization; not every file is necessarily included. Follow [Apple's backup guidance](https://developer.apple.com/documentation/foundation/optimizing-your-app-s-data-for-icloud-backup) for regenerable data and backup exclusions.
- **Make sure your app behaves appropriately when iCloud is unavailable** - If someone turns off iCloud or loses connectivity, you don't need an intrusive alert merely to announce the condition. Unobtrusively explain when changes are waiting to sync.
- **Keep app state information in iCloud** - In addition to storing documents and other files, you can use iCloud to store settings and information about the state of your app. For example, a magazine app might store the last page viewed so when the app is opened on another device, someone can continue reading from where they left off.
- **Warn about the consequences of deleting a document** - When someone deletes a document in an app that supports iCloud, the document is removed from iCloud and all other devices too. Show a warning and ask for confirmation before performing the deletion.
- **Make conflict resolution prompt and easy** - To the extent possible, try to detect and resolve version conflicts automatically. If this can't be done, display an unobtrusive notification that makes it easy to differentiate and choose between the conflicting versions.
- **Include iCloud content in search results** - People with iCloud accounts assume their content is universally available, and they expect search results to reflect this perspective.
- **For games, consider saving player progress in iCloud** - Although you can implement this functionality yourself, the GameSave framework offers an efficient solution. It synchronizes save data across devices and offers built-in alerts you can use to help players handle syncing issues during offline play or when conflicts arise.

### Platform Considerations

No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.

### Developer Documentation

- [CloudKit](https://developer.apple.com/documentation/cloudkit) - CloudKit
- [GameSave](https://developer.apple.com/documentation/gamesave) - GameSave

## Changelog

### June 9, 2025
- Added guidance for synchronizing game data through iCloud.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/icloud)*
