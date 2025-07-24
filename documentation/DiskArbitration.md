# Disk Arbitration

Provides mechanisms to register and block disk mount or unmount events.

**Platforms:** Mac Catalyst 13.0+ | macOS 10.4+

## Overview

For related documentation, see [Mac Technology Overview](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/OSX_Technology_Overview/About/About.html).

## Topics

### Reference
- **DADisk.h**
- **DADissenter.h**
- **DASession.h**
- **DiskArbitration.h** - Register for mount/unmount notifications, and block mount/unmount events.
- **DiskArbitration Enumerations**
- **DiskArbitration Constants**
- **DiskArbitration Functions**
- **DiskArbitration Data Types**

### Articles
- **DAReturn** - A return code.
- **kDADiskOptionEjectUponLogout**
- **kDADiskOptionMountAutomatic**
- **kDADiskOptionMountAutomaticNoDefer**
- **kDADiskOptionPrivate**

### Variables
- `let kDADiskDescriptionFSKitPrefix: CFString`
- `let kDADiskDescriptionRepairRunningKey: CFString` (Beta)
- `var kDADiskMountOptionNoFollow: Int`
- `var kDAReturnBadArgument: Int`
- `var kDAReturnBusy: Int`
- `var kDAReturnError: Int`
- `var kDAReturnExclusiveAccess: Int`
- `var kDAReturnNoResources: Int`
- `var kDAReturnNotFound: Int`
- `var kDAReturnNotMounted: Int`
- `var kDAReturnNotPermitted: Int`
- `var kDAReturnNotPrivileged: Int`
- `var kDAReturnNotReady: Int`
- `var kDAReturnNotWritable: Int`
- `var kDAReturnSuccess: Int`
- `var kDAReturnUnsupported: Int`

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/DiskArbitration)*