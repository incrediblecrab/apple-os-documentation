# GameSave

Store and sync your application's save files in iCloud.

**Platforms:** iOS 26.0+ | iPadOS 26.0+ | Mac Catalyst 26.0+ | macOS 26.0+ | visionOS 26.0+

## Overview

GameSave uses iCloud Drive to synchronize your application's save data across devices. The framework provides a set of APIs for reading and writing one or more files to a directory, while abstracting away iCloud concepts. It handles common save syncing scenarios like conflict resolution and offline play. Additionally, it provides a set of convenience UI alerts for these typical scenarios. GameSave also supports local saving for when the device isn't signed into iCloud Drive.

**Important:** For GameSave to store the game data in the player's iCloud account, you need to provide an identifier for the iCloud container that stores the data. Add the iCloud capability to your project and select the iCloud Documents checkbox. For more information, see Configuring iCloud services.

## Topics

### Synced Directory (Objective-C)
- **GSSyncedDirectory** - A cloud-synced directory for game-save data.

### Classes
- **GameSaveSyncedDirectory** - A cloud-synced directory for game-save data.

### Variables
- **GameSaveErrorDomain** - The error domain for GameSave framework errors.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/GameSave)*