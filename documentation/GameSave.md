# GameSave

Store and sync your application's save files in iCloud.

**Platforms:** iOS 26.0+ | iPadOS 26.0+ | Mac Catalyst 26.0+ | macOS 26.0+ | visionOS 26.0+

## Overview

GameSave uses iCloud Drive to synchronize your application's save data across devices. The framework provides a set of APIs for reading and writing one or more files to a directory, while abstracting away iCloud concepts. It handles common save syncing scenarios like conflict resolution and offline play. Additionally, it provides a set of convenience UI alerts for these typical scenarios. GameSave also supports local saving for when the device isn't signed into iCloud Drive.

**Important:** For GameSave to store the game data in the player's iCloud account, you need to provide an identifier for the iCloud container that stores the data. Add the iCloud capability to your project and select the iCloud Documents checkbox. For more information, see Configuring iCloud services.

## Save-data integration

GameSave was introduced before OS 27 and is not listed for tvOS or watchOS. Use it for player-created save files, not for distributing game levels, textures, or other downloadable application assets.

Follow the directory lifecycle in [GameSaveSyncedDirectory](https://developer.apple.com/documentation/gamesave/gamesavesynceddirectory), and configure the iCloud container as described in the [framework overview](https://developer.apple.com/documentation/gamesave). Game Center authentication is not evidence that iCloud Drive synchronization is available.

Test offline play, local-only saving when signed out, conflicting saves from multiple devices, and recovery after synchronization resumes. Present a deliberate conflict-resolution experience rather than silently assuming that the newest local file is always the desired save.

## Topics

### Synced Directory (Objective-C)
- **GSSyncedDirectory** - A cloud-synced directory for game-save data.

### Classes
- **GameSaveSyncedDirectory** - A cloud-synced directory for game-save data.

### Variables
- **GameSaveErrorDomain** - The error domain for GameSave framework errors.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/GameSave)*
