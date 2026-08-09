# IOSurface

Share hardware-accelerated buffer data (framebuffers and textures) across multiple processes. Manage image memory more efficiently.

**Platforms:** iOS 11.0+ | iPadOS 11.0+ | Mac Catalyst 13.0+ | macOS 10.6+ | tvOS 11.0+ | visionOS 1.0+

## Overview

The IOSurface framework provides a framebuffer object suitable for sharing across process boundaries. It is commonly used to allow applications to move complex image decompression and draw logic into a separate process to enhance security.

## Topics

### Classes
- **IOSurface** - Data type representing an IOSurface opaque object.
- **IOSurfaceRef** - Data type representing an IOSurface opaque object.

### Structures
- **IOSurfaceLockOptions**
- **IOSurfacePropertyKey**
- **IOSurfacePurgeabilityState**

### Reference
- [IOSurface Structures](https://developer.apple.com/documentation/iosurface/iosurface_structures)
- [IOSurface Enumerations](https://developer.apple.com/documentation/iosurface/iosurface_enumerations)
- [IOSurface Constants](https://developer.apple.com/documentation/iosurface/iosurface_constants)
- [IOSurface Functions](https://developer.apple.com/documentation/iosurface/iosurface_functions)
- [IOSurface Data Types](https://developer.apple.com/documentation/iosurface/iosurface_data_types)

### Variables
- **kIOSurfaceContentHeadroom**
- **kIOSurfaceCopybackCache**
- **kIOSurfaceCopybackInnerCache**
- **kIOSurfaceDefaultCache**
- **kIOSurfaceInhibitCache**
- **kIOSurfaceMapCacheShift**
- **kIOSurfaceMapCopybackCache**
- **kIOSurfaceMapCopybackInnerCache**
- **kIOSurfaceMapDefaultCache**
- **kIOSurfaceMapInhibitCache**
- **kIOSurfaceMapWriteCombineCache**
- **kIOSurfaceMapWriteThruCache**
- **kIOSurfaceWriteCombineCache**
- **kIOSurfaceWriteThruCache**

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/IOSurface)*