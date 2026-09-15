# FSKit

Implement a file system that runs in user space.

**Platforms:** macOS 15.4+

## Overview

With FSKit, you can extend macOS by enabling access to new types of file systems. You do this by developing an FSKit module (FSModule), which you deliver as an app extension that runs in user space, and is compatible with Mac App Store distribution. FSKit connects your module to the system's existing frameworks and tools, like Disk Arbitration, NetFS, and the mount(8) command.

### FSKit Modules

An FSKit module consists of two main parts:

- A set of module attributes that you define in the module's Info.plist file. These attributes provide metadata like Boolean keys that indicate feature support and dictionaries that describe command-line interface access.

- The code that implements the file system functionality. The supported entry point conforms to `UnaryFileSystemExtension` and supplies a subclass of `FSUnaryFileSystem`; the file-system class and the extension protocol are distinct types.

The FSKit framework defines three key file storage concepts that FSModule supports:

**Volume**  
A directory structure for files and folders.

**Resource**  
A source of data, such as a block storage device or a network resource you identify with a URL.

**Container**  
An abstract object that uses one or more resources to deliver one or more volumes, similar to an APFS container. Typically, a container uses only one resource, but some formats like Xsan (Apple's cluster file system) use multiple disks to store contents for one volume.

### Design Flows

Apple documents two file-system designs, but only the unary design is currently implemented:

- **FSFileSystem** describes a full-featured design that can employ multiple resources and deliver multiple volumes. It is not currently supported.

- **FSUnaryFileSystem** is a simpler file system that uses one resource and provides one volume, with the volume and container sharing their state and lifetime. HFS, msdosfs, ExFAT, and NTFS are examples of this storage pattern; that does not mean their built-in implementations are FSKit modules.

**Implementation scope, reviewed September 8, 2026:** Apple's overview describes both designs but explicitly says the current implementation supports only `FSUnaryFileSystem`. Do not read the broader design discussion as a promise that every multi-resource/multi-volume path is available.

For the documented unary workflow, implement `UnaryFileSystemExtension`, return your `FSUnaryFileSystem` subclass, and conform to `FSUnaryFileSystemOperations`, including resource loading. A volume is an `FSVolume` subclass. The pre-27 volume API uses `FSVolume.Operations`, which also requires `FSVolume.PathConfOperations`; the 27 SDK provides the replacement below.

### macOS 27 handler protocols

[`FSVolume.Handler`](https://developer.apple.com/documentation/fskit/fsvolume/handler) is new in macOS 27 and replaces [`FSVolume.Operations`](https://developer.apple.com/documentation/fskit/fsvolume/operations), deprecated in 27 rather than removed. Both require `FSVolume.PathConfOperations`. Adopt the appropriate additional handler protocols for optional volume capabilities.

The handler APIs use specialized results derived from [`FSVolumeHandlerResult`](https://developer.apple.com/documentation/fskit/fsvolumehandlerresult). Relevant replies can include item attributes and free-space information. This is a change to the volume-operation interface, not support for the currently unavailable multi-resource `FSFileSystem` design.

The macOS 26 passthrough sample uses the older operations protocols. It remains an example of that API generation, not a completed migration to the 27 handlers.

### Permissions and resources

The module needs Boolean [`com.apple.developer.fskit.fsmodule`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.fskit.fsmodule) set to `true`. The passthrough sample also requires the person to enable its File System Extension in System Settings before mounting it. Neither step grants arbitrary access to source files or devices.

`FSPathURLResource` can carry a security-scoped URL into the extension. Check whether access succeeds, propagate access errors, and balance successful security-scope acquisition with release, including failed-load cleanup. Keep resource loading and unloading paired, and handle resource disappearance during operations. A proxy `FSBlockDeviceResource` describes a disk without transferring privileged access to an unentitled caller.

For a unary filesystem backed by `FSBlockDeviceResource`, also implement `FSManageableResourceMaintenanceOperations`; the system requires a filesystem check before mounting a block-device filesystem. Do not mix direct I/O with cached metadata I/O on the same ranges, which can produce stale or inconsistent data.

## Topics

### Essentials
- [Building a passthrough file system](https://developer.apple.com/documentation/fskit/building-a-passthrough-file-system) - A concrete starting point for a user-space filesystem.

### App Extensions
- **UnaryFileSystemExtension** - A protocol for implementing a minimal file system as an app extension.

### File Systems
- **FSUnaryFileSystem** - An abstract base class for implementing a minimal file system.
- **FSFileSystemBase** - A protocol containing functionality supplied by FSKit to file system implementations.
- **FSFileName** - The name of a file, expressed as a data buffer.

### Containers
- **FSContainerIdentifier** - A type that identifies a container.
- **FSContainerStatus** - A type that represents a container's status.

### Resources
- **FSResource** - An abstract resource a file system uses to provide data for a volume.
- **FSBlockDeviceResource** - A resource that represents a block storage disk partition.

### Volumes
- **FSVolume** - A directory structure for files and folders.

### Items
- **FSItem** - A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.

### Maintenance and Management
- **FSManageableResourceMaintenanceOperations** - Maintenance operations for a file system's resources.

### Operations
- **FSOperationID** - A unique identifier for an operation.

### Tasks
- **FSTask** - A class that enables a file system module to pass log messages and completion notifications to clients.
- **FSTaskOptions** - A class that passes command options to a task, optionally providing security-scoped URLs.

### Errors and Logging
- **fs_errorForCocoaError(Int32) -> any Error** - Creates an error object for the given Cocoa error code.
- **fs_errorForMachError(Int32) -> any Error** - Creates an error object for the given Mach error code.
- **fs_errorForPOSIXError(Int32) -> any Error** - Creates an error object for the given POSIX error code.
- **FSError** - An error encountered when performing an FSKit operation.
- [FSError.Code](https://developer.apple.com/documentation/fskit/fserror/code) - A code that indicates a specific FSKit error.
- **FSKitErrorDomain** - An error domain for FSKit errors.

### FSKit Interactions
- **FSClient** - An interface for apps and daemons to interact with FSKit.

### Supporting Types
- **FSBlockmapFlags** - Flags that describe the behavior of a blockmap operation.
- **FSCompleteIOFlags** - Flags that describe the behavior of an I/O completion operation.
- **FSEntityIdentifier** - A base type that identifies containers and volumes.
- **FSExtentPacker** - A type that directs the kernel to map space on disk to a specific file managed by this file system.
- **FSExtentType** - An enumeration of types of extents.
- **FSMatchResult** - A type that represents the recognition and usability of a probed resource.
- **FSMetadataRange** - A range that describes contiguous metadata segments on disk.
- **FSProbeResult** - An object that represents the results of a specific probe.

### Classes
- [FSGenericURLResource](https://developer.apple.com/documentation/fskit/fsgenericurlresource) - A resource representing an abstract URL whose interpretation belongs to the implementation; macOS 26+.
- [FSPathURLResource](https://developer.apple.com/documentation/fskit/fspathurlresource) - A resource representing a filesystem path and, when provided, preserving its security-scoped URL; macOS 26+.

### Entitlements
- [com.apple.developer.fskit.fsmodule](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.fskit.fsmodule) - Boolean filesystem-module capability; macOS 15.4+.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/FSKit)*

*Implementation sources: [current framework scope](https://developer.apple.com/documentation/fskit.md) and [passthrough sample](https://developer.apple.com/documentation/fskit/building-a-passthrough-file-system.md). The sample requires macOS 26/Xcode 26 rather than the framework's original macOS 15.4 minimum.*
