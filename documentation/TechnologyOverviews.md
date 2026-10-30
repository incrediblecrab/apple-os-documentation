# Technology Overviews

Learn about the wide range of technologies you use to develop software for Apple platforms.

## Overview

Whether you're new to Apple platforms or you've been working with them for years, finding the technology you need is an important first step. With so many technologies available to you, it's sometimes difficult to know where to start. The following topics offer a high-level view of the technologies available to you, and guidance about which technologies you might choose to solve particular problems.

## Platform Planning — September 8, 2026

Use the platform introductions for version-specific adoption work while retaining the earlier-platform references below. A framework's presence in this repository is not a claim that every API requires OS27 or works on every device.

| Platform | Previous-generation context | Current OS27 adoption focus |
|---|---|---|
| iPhone | [iOS 26](../os26-intro/iOS.md) | [iOS 27](../os27-intro/iOS.md): UIKit scenes and launch screens, assets, metrics, and data permissions |
| iPad | [iPadOS 26](../os26-intro/iPadOS.md) | [iPadOS 27](../os27-intro/iPadOS.md): scene restoration, external displays, menus, and document I/O |
| Mac | [macOS Tahoe 26](../os26-intro/macOS.md) | [macOS 27](../os27-intro/macOS.md): AppKit behavior, native dependencies, installers, and Rosetta |
| Apple TV | [tvOS 26](../os26-intro/tvOS.md) | [tvOS 27](../os27-intro/tvOS.md): scenes, downloadable assets, playback, and focus |
| Apple Watch | [watchOS 26](../os26-intro/watchOS.md) | [watchOS 27](../os27-intro/watchOS.md): HealthKit zones and deployment-scoped WatchKit deprecations |
| Apple Vision Pro | [visionOS 26](../os26-intro/visionOS.md) | [visionOS 27](../os27-intro/visionOS.md): scenes, spatial regression testing, and document/asset handling |

The six OS27 platforms shipped September 14, 2026: iOS/iPadOS 27.0 (`24A437`), macOS 27 Golden Gate 27.0 (`26A428`), tvOS 27.0 (`24J361`), watchOS 27.0 (`24R364`), and visionOS 27.0 (`24M362`). Xcode 27 (`27A266a`) shipped September 14; it requires **Apple silicon and macOS Tahoe 26.6 or later**, not macOS 27. See [releases](https://developer.apple.com/news/releases/) and [Xcode requirements](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes). Neither the release table nor a chip family alone establishes a complete device list.

**October 29, 2026 update:** All six platforms shipped 27.2 on October 26, 2026: iOS/iPadOS (`24B119`), macOS Golden Gate (`26B123`), tvOS (`24K122`), watchOS (`24S118`), and visionOS (`24N120`). The [release feed](https://developer.apple.com/news/releases/rss/releases.rss) also lists iOS 27.2 build `24B91020`, without identifying its device scope.

Apple's [security-release list](https://support.apple.com/en-us/100100) dates Xcode 27.2 to October 29, 2026; the feed still lists only the October 19, 2026 RC (`27B48`), so a final build number is not established by these captures. [Xcode 27.2](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes) supplies Swift 6.4 and SDKs for all six 27.2 platforms and requires macOS Tahoe 26.6 or later. [Xcode 27.1](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes) and 27.2 have a known Mac Catalyst compilation issue for code using iOS 27.1-specific APIs; Xcode 27.2 also incorrectly offers 27.1 deployment targets for macOS, watchOS, tvOS, and visionOS.

Choose an implementation and then verify its individual availability, entitlements, and failure modes. Keep [App Store readiness](../guides/app-store-readiness.md), [regional distribution](../guides/regional-distribution.md), and [PCC approval/privacy](../guides/private-cloud-compute.md) separate from API definitions.

## Topics

### Get Started
Start your exploration with the foundational technologies you use to build your app or game, and make your interface shine by adopting Liquid Glass.

- [App design and UI](https://developer.apple.com/documentation/technologyoverviews/app-design-and-ui) - Build accessible interfaces using technologies such as SwiftUI and UIKit
- [Games](https://developer.apple.com/documentation/technologyoverviews/games) - Create immersive gaming experiences with Apple's game development frameworks

### Discover Apple Technologies
Explore the technologies you use to build your app's unique experience. Whether you're building core features like your app's data model, accessing device-specific hardware, making your app more intelligent, or adopting features unique to Apple devices, Apple frameworks help you do so easily and efficiently.

- [Data management](https://developer.apple.com/documentation/technologyoverviews/data-management) - Store, sync, and manage data with Core Data, CloudKit, and other frameworks
- [Core experiences](https://developer.apple.com/documentation/technologyoverviews/core-experiences) - Implement essential app functionality and user interactions
- [Apple Intelligence and machine learning](https://developer.apple.com/documentation/technologyoverviews/ai-machine-learning) - Integrate AI and machine learning capabilities into your app
- [Audio and video](https://developer.apple.com/documentation/technologyoverviews/audio-and-video) - Work with multimedia content using AVFoundation and related frameworks

### Explore the Apple Developer Documentation
Consult the Apple Developer Documentation for in-depth information about individual technologies. The developer documentation includes API reference, articles, sample code, and tutorials to help you learn how to use a given technology. It also offers guidance about the best way to solve specific challenges.

---

*Sources: [Apple Developer Documentation](https://developer.apple.com/documentation/technologyoverviews), [release feed](https://developer.apple.com/news/releases/rss/releases.rss), [Apple security releases](https://support.apple.com/en-us/100100), [Xcode 27.1 release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes), [Xcode 27.2 release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes).*
