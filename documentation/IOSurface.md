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

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/IOSurface)*