# System

Perform low-level file operations using type-safe APIs.

**Platforms:** iOS 14.0+ | iPadOS 14.0+ | Mac Catalyst 14.0+ | macOS 11.0+ | tvOS 14.0+ | visionOS 1.0+ | watchOS 7.0+

## Topics

### Adopting System
- [Adopting Swift File Operations](https://developer.apple.com/documentation/system/adopting_swift_file_operations) - Migrate existing C code to Swift, using the file operations provided by the System module
- [Adopting Swift File Options](https://developer.apple.com/documentation/system/adopting_swift_file_options) - Migrate existing C code to Swift, using the file-operation options provided by the System module
- [Adopting Swift Error Constants](https://developer.apple.com/documentation/system/adopting_swift_error_constants) - Migrate existing C code to Swift, using the error constants provided by the System module

### Files
- **FileDescriptor** - An abstract handle to an input or output data resource, such as a file or a socket
- **FilePath** - Represents a location in the file system
- **FilePermissions** - The access permissions for a file

### Errors
- **Errno** - An error number used by system calls to communicate what kind of error occurred

### Protocols
- **MachPortRight**

### Enumerations
- **CInterop** - A namespace for C and platform types
- **Mach**

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/System)*