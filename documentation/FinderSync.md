# Finder Sync

Modify the Finder's user interface to express file synchronization and control.

**Platforms:** macOS 10.10+

## Overview

Use Finder Sync to cleanly and safely modify the Finder's user interface to express file synchronization status and control. Unlike most extension points, Finder Sync doesn't add features to a host app. Instead, it lets you modify the behavior of the Finder itself.

Use this framework when you need to synchronize the contents of a local folder with a remote data source. Then provide visual feedback to the Finder by extending the FIFinderSync class and overriding appearance methods defined within the FIFinderSyncProtocol protocol.

To learn more about creating a Finder Sync extension, see Finder Sync in App Extension Programming Guide.

## Topics

### Classes
- **class FIFinderSync** - A type to subclass to add badges, custom shortcut menus, and toolbar buttons to the Finder.
- **class FIFinderSyncController** - A controller that acts as a bridge between your Finder Sync extension and the Finder itself.

### Protocols
- **protocol FIFinderSyncProtocol** - The group of methods to implement for modifying the Finder user interface to express file synchronization status and control.

### Reference
- **FinderSync Enumerations**

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/FinderSync)*