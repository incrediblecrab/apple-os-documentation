# Core Foundation

Access low-level functions, primitive data types, and various collection types that are bridged seamlessly with the Foundation framework.

**Platforms:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 13.0+ | macOS 10.0+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 2.0+

## Overview

Core Foundation is a framework that provides fundamental software services useful to application services, application environments, and to applications themselves. Core Foundation also provides abstractions for common data types, facilitates internationalization with Unicode string storage, and offers a suite of utilities such as plug-in support, XML property lists, URL resource access, and preferences.

For more about Core Foundation, see Core Foundation Design Concepts.

## Topics

### Utilities
- [Base Utilities](https://developer.apple.com/documentation/corefoundation/base-utilities)
- [Byte-Order Utilities](https://developer.apple.com/documentation/corefoundation/byte-order-utilities)
- [Core Foundation URL Access Utilities](https://developer.apple.com/documentation/corefoundation/core-foundation-url-access-utilities)
- [Preferences Utilities](https://developer.apple.com/documentation/corefoundation/preferences-utilities)
- [Socket Name Server Utilities](https://developer.apple.com/documentation/corefoundation/socket-name-server-utilities)
- [Time Utilities](https://developer.apple.com/documentation/corefoundation/time-utilities)

### Opaque Types
- **CFAllocator**
- **CFArray**
- **CFAttributedString**
- **CFBag**
- **CFBinaryHeap**
- **CFBitVector**
- **CFBoolean**
- **CFBundle**
- **CFCalendar**
- **CFCharacterSet**
- **CFData**
- **CFDate**
- **CFDateFormatter**
- **CFDictionary**
- **CFError**
- **CFFileDescriptor**
- **CFFileSecurity** - Encapsulates a file system object's security information in a Core Foundation object.
- **CFLocale**
- **CFMachPort**
- **CFMessagePort**
- **CFMutableArray**
- **CFMutableAttributedString**
- **CFMutableBag**
- **CFMutableBitVector**
- **CFMutableCharacterSet**
- **CFMutableData**
- **CFMutableDictionary**
- **CFMutableSet**
- **CFMutableString**
- **CFNotificationCenter**
- **CFNull**
- **CFNumber**
- **CFNumberFormatter**
- **CFPlugIn**
- **CFPlugInInstance**
- **CFPropertyList**
- **CFReadStream**
- **CFRunLoop**
- **CFRunLoopObserver**
- **CFRunLoopSource**
- **CFRunLoopTimer**
- **CFSet**
- **CFSocket**
- **CFString**
- **CFStringTokenizer**
- **CFTimeZone**
- **CFTree**
- **CFURL**
- **CFUserNotification**
- **CFURLEnumerator** - A reference to a CFURLEnumerator object.
- **CFUUID**
- **CFWriteStream**
- **CFXMLNode**
- **CFXMLParser**
- **CFXMLTree**

### Reference
- [CFStream](https://developer.apple.com/documentation/corefoundation/cfstream)
- **Core Foundation Structures**
- **Core Foundation Enumerations**
- **Core Foundation Constants**
- **Core Foundation Functions**
- **Core Foundation Data Types**
- **Core Foundation Macros**

### Variables
- [`kCFURLUbiquitousItemIsSyncPausedKey`](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemissyncpausedkey) — 26+ on supported platforms.
- [`kCFURLUbiquitousItemSupportedSyncControlsKey`](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemsupportedsynccontrolskey) — 26+ on supported platforms.

### Functions
- [`CFAttributedStringGetStatisticalWritingDirections(_:_:_:_:_:)`](https://developer.apple.com/documentation/corefoundation/cfattributedstringgetstatisticalwritingdirections(_:_:_:_:_:)) — 26+ on supported platforms.

For the documented OS 27 URL-encoding and capacity-reporting changes, see [Foundation](Foundation.md#urls-and-available-capacity). Do not assume those notes change every low-level CFURL function or its ownership rules.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreFoundation)*
