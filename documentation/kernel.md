# Kernel

Develop kernel-resident device drivers and kernel extensions.

**Platforms:** macOS 10.0+

## Overview

The Kernel Framework provides the APIs and support for kernel-resident device drivers and other kernel extensions. It defines the base class for I/O Kit device drivers (IOService), several helper classes, and the families that support many types of devices.

### Deployment and debugging boundaries

Prefer [DriverKit](DriverKit.md) or [SystemExtensions](SystemExtensions.md) when they provide the required functionality. The Kernel framework is not blanket-deprecated, but its historical macOS 10.0 baseline does not imply that every listed declaration or kernel extension can run on every later system.

Apple's [current installation guide](https://developer.apple.com/documentation/apple-silicon/installing-a-custom-kernel-extension) describes a user-managed workflow with approval and, for executable kexts on macOS 11+, an auxiliary kernel collection and restart. On Apple silicon, that workflow also requires Reduced Security and allowing third-party kexts in Recovery. This is not the normal DriverKit installation model. Load kexts as the final installer step so a restart does not interrupt the rest of installation.

Updating or unloading an executable kext can remain pending until restart; the previous code may still be running. The guide distinguishes codeless kexts, which require approval but do not require that restart. It identifies `kmutil` as the replacement for older kext-management tools, rather than claiming that all older command names were removed.

Apple-silicon kexts require the `arm64e` architecture and its pointer-authentication rules. Kernel Integrity Protection restricts modification of kernel and driver code after initialization. For debugging, use logs, a kernel core file, or the [Kernel Debug Kit workflow](https://developer.apple.com/documentation/apple-silicon/debugging-a-custom-kernel-extension) matching the target macOS version. Two-machine debugging requires separately configured target and debugger Macs; NMI instructions are development-target procedures, not ordinary app debugging.

## Topics

### Kernel Extensions
- [Implementing drivers, system extensions, and kexts](https://developer.apple.com/documentation/kernel/implementing_drivers_system_extensions_and_kexts) - Create drivers and system extensions to communicate with hardware and provide low-level services, and only use kernel extensions for a few tasks.
- [Installing a custom kernel extension](https://developer.apple.com/documentation/apple-silicon/installing-a-custom-kernel-extension) - Approval, collection updates, restart requirements, and the codeless-kext exception.
- [Debugging a custom kernel extension](https://developer.apple.com/documentation/apple-silicon/debugging-a-custom-kernel-extension) - Logs, core files, and matching-KDK two-machine debugging.
- [Generating a Non-Maskable Interrupt](https://developer.apple.com/documentation/kernel/generating_a_non-maskable_interrupt) - Interrupt the kernel on a target Mac and attach a remote debugger to it.

### IOKit Drivers
- [IOKit Fundamentals](https://developer.apple.com/documentation/kernel/iokit_fundamentals) - Legacy I/O Kit architecture for kernel drivers and application-side device interfaces, not a DriverKit implementation guide.

### Hardware Families
Add support for specific hardware protocols such as USB, and for standard network, serial, audio, and graphics interfaces.

### Driver Support
Explore the device registry and access power-management utilities and other shared driver features.

### libkern
Access the runtime support and base classes of the kernel library.

### BSD
- **architecture** - Access machine-level and architectural information about the current platform.
- [bsm](https://developer.apple.com/documentation/kernel/bsm) - Audit event, class, user-identity, and session data types.
- **hfs** - Access HFS file-system data structures.
- **kern** - Access kernel-level interfaces including clock, task, kernel extension, lock, and compression utilities.
- [Math](https://developer.apple.com/documentation/kernel/math) - Mathematical routines and numeric declarations in the kernel reference.
- **miscfs** - Access device nodes and other file-system entities.
- **net** - Access network-related utilities.
- **Strings** - Compare, convert, and catenate strings and access the resulting content of those strings.
- **sys** - Access general system utilities for time, file systems, and system information.
- **vfs** - Access the virtual file-system interfaces.
- **vm** - Interact with the virtual memory system.

### Mach
- **mach** - Access Mach interfaces including processor, memory, thread, and semaphore support.
- [mach-o](https://developer.apple.com/documentation/kernel/mach-o) - Mach-O image, loader, and dynamic-library structures.

### Utilities

#### Debugging
Debug your kernel extensions using the kernel debugger, assertions, exceptions, backtraces, and logging.

#### AppleDSP
Perform digital signal processing on data.

### Deprecated
- **Deprecated Symbols** - Review deprecated interfaces and their replacements; deprecation alone does not establish that a symbol has been removed.

### Additional Reference
- **Kernel Functions**
- **Kernel Structures**
- **Kernel Data Types**
- **Kernel Enumerations**
- **Kernel Constants**

### Classes
- **IOCatalogue** - In-kernel database for IOKit driver personalities.
- **IOEventLink**
- **IOEventLinkInterface**
- **IOGuardPageMemoryDescriptor**
- **IOHIDTranslationService**
- **IOServiceStateNotificationDispatchSource**
- **IOServiceStateNotificationDispatchSourceInterface**
- **IOWorkGroup**
- **IOWorkGroupInterface**
- **OSAction_IOHIDEventService__CopyEvent**
- **OSAction_IOHIDEventService__CopyEventInterface**
- **OSAction_IOHIDEventService__SetLED**
- **OSAction_IOHIDEventService__SetLEDInterface**
- **OSAction_IOHIDEventService__SetUserProperties**
- **OSAction_IOHIDEventService__SetUserPropertiesInterface**

### See Also
#### Related Documentation
- [IOKit Fundamentals](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/IOKitFundamentals/Introduction/Introduction.html)
- [Kernel Programming Guide — About This Document](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/About/About.html#//apple_ref/doc/uid/TP30000905-CH204)

These archived guides provide architectural background. Their historical toolchain and hardware discussions are not current deployment or macOS 27 host-eligibility requirements.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/kernel)*
