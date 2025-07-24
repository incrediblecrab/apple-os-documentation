# FSKit

Implement a file system that runs in user space.

**Platforms:** macOS 15.4+

## Overview

With FSKit, you can extend macOS by enabling access to new types of file systems. You do this by developing an FSKit module (FSModule), which you deliver as an app extension that runs in user space, and is compatible with Mac App Store distribution. FSKit connects your module to the system's existing frameworks and tools, like Disk Arbitration, NetFS, and the mount(8) command.

### FSKit Modules

An FSKit module consists of two main parts:

- A set of module attributes that you define in the module's Info.plist file. These attributes provide metadata like Boolean keys that indicate feature support and dictionaries that describe command-line interface access.

- The code that implements the file system functionality. Your app extension conforms to one of two protocols, depending on its design flow, as described below.

The FSKit framework defines three key file storage concepts that FSModule supports:

**Volume**  
A directory structure for files and folders.

**Resource**  
A source of data, such as a block storage device or a network resource you identify with a URL.

**Container**  
An abstract object that uses one or more resources to deliver one or more volumes, similar to an APFS container. Typically, a container uses only one resource, but some formats like Xsan (Apple's cluster file system) use multiple disks to store contents for one volume.

### Design Flows

FSKit provides two design flows, with different trade-offs of functionality and complexity:

- **FSFileSystem** is a conventional, full-featured file system that can employ multiple resources and deliver multiple volumes.

- **FSUnaryFileSystem** is a simpler file system where containers use only one resource and provide only one volume. Most file systems shipping in macOS fit this pattern, including HFS, msdosfs, ExFAT, ntfs, and others.

**Note:** The current version of FSKit supports only FSUnaryFileSystem.

When you choose a design flow, write an app extension that conforms to either FileSystemExtension or UnaryFileSystemExtension, based on your chosen flow. These protocols declare a fileSystem delegate object that your extension creates and returns. This delegate object subclasses either FSFileSystem or FSUnaryFileSystem as appropriate, and conforms to either the FSFileSystemOperations or FSUnaryFileSystemOperations protocol. These protocols define a loadResource method, which FSKit uses to make a resource available to the module.

## Topics

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
- **Code** - A code that indicates a specific FSKit error.
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
- **FSGenericURLResource** - A resource representing an abstract URL (Beta)
- **FSPathURLResource** - A resource representing a path (Beta)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/FSKit)*