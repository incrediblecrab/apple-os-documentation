# DriverKit

Develop device drivers that run in user space.

**Platforms:** DriverKit 19.0+ | iOS 16.0+ | iPadOS 16.0+ | macOS 10.15+

## Overview

The DriverKit framework defines the fundamental behaviors for device drivers in macOS and iPadOS. The C++ classes of this framework define your driver's basic structure, and provide support for handling events and allocating memory. This framework also supports appropriate types for examining the numbers, strings, and other types of data in your driver's I/O registry entry. Other frameworks, such as USBDriverKit, HIDDriverKit, NetworkingDriverKit, PCIDriverKit, SerialDriverKit, and AudioDriverKit, provide the specific behaviors you need to support different types of devices.

The drivers you build with DriverKit run in user space, rather than as kernel extensions. This limits the impact of some faults but does not replace input validation or careful resource handling. Package the driver as a DriverKit extension (dext) inside a containing app.

In macOS, use the System Extensions framework to install and upgrade your driver. In iPadOS, the system discovers and updates drivers with their containing apps, but the person must enable the driver in Settings before it can run on demand. Installing the app is not that permission.

Services receive `init`/`Start` and `Stop`/`free` lifecycle calls. During shutdown, cancel outstanding asynchronous work and wait for cancellation to finish before calling the inherited `Stop`; release the instance-variable allocation in `free`, not prematurely in `Stop`.

**Note**: The base DriverKit framework is available in macOS for Apple silicon and Intel-based Mac computers, and in iPadOS for devices with an M-series chip. The availability of family frameworks like USBDriverKit and AudioDriverKit varies by platform.

### Availability and activation boundaries

The iOS 16 and Mac Catalyst 16 labels in Apple's catalog do not by themselves establish additional driver deployment targets. The documented mobile deployment is on supported M-series iPads, not iPhone. Likewise, historical Intel support in the base framework is separate from eligibility to run a particular macOS host release.

Driver entitlements must match the signed provisioning profile and the transport/family being used. The containing app's System Extension capability is separate from the driver's own entitlements. Activation can fail because of entitlement mismatches or remain pending for user approval; do not treat submitting an activation request as a usable driver connection.

For the 27 beta SDK, [VideoDriverKit](VideoDriverKit.md) is a new **macOS** video-driver family with DriverKit 27.0 availability. Do not infer iPadOS support from another family's availability. Its API replaces the need for the corresponding `IOVideoFamily`/DAL integration, not every legacy driver category.

### Client access and input validation

On macOS, `com.apple.developer.driverkit.userclient-access` belongs to the **client app** and identifies the driver extensions it may connect to. In contrast, `com.apple.developer.driverkit.allow-any-userclient-access` belongs to the **dext** and permits apps to connect without holding that client-side grant.

On iPadOS, clients need Boolean `com.apple.developer.driverkit.communicates-with-drivers`. By default, a driver accepts entitled clients from its own Team. Enabling `com.apple.developer.driverkit.allow-third-party-userclients` on the driver admits other Teams, but those clients still need the communicates-with-drivers entitlement. Handle a disabled driver, missing matching service, failed connection, and later service loss rather than assuming an entitlement guarantees a live device.

An entitled client is not a reason to trust its method selector, scalar count, buffer size, or contents. The linked client sample deliberately includes both checked and unchecked paths; use its validation discussion, not its unchecked path, as the production pattern. Its asynchronous callback uses a timer to simulate hardware work. Retain callbacks while they are needed and coordinate their cancellation with teardown.

Enable each required Boolean capability with `true` on its appropriate signed target; a capability's presence in an unsigned or mismatched entitlement file is not authorization.

## Topics

### Essentials
- [Implementing drivers, system extensions, and kexts](https://developer.apple.com/documentation/kernel/implementing_drivers_system_extensions_and_kexts) - Prefer user-space drivers and system extensions where equivalent functionality exists; retain kexts only for tasks that require them.
- [Creating drivers for iPadOS](https://developer.apple.com/documentation/driverkit/creating-drivers-for-ipados) - Bring your drivers to iPadOS by using the platform's DriverKit support.

### Entitlements
- [Requesting Entitlements for DriverKit Development](https://developer.apple.com/documentation/driverkit/requesting-entitlements-for-driverkit-development) - Request the entitlement for DriverKit development, and request other entitlements your driver needs to interact with specific devices and interfaces.
- [com.apple.developer.driverkit](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.driverkit) - Boolean permission on the dext to run as a user-space driver; requires Apple's grant and matching provisioning.
- [com.apple.developer.driverkit.userclient-access](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.driverkit.userclient-access) - An array of driver-extension bundle IDs on a macOS **client app**. Apple's reference also accepts a single string for one driver.
- [com.apple.developer.driverkit.allow-any-userclient-access](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.driverkit.allow-any-userclient-access) - Boolean permission on a macOS dext to accept connections without requiring each client to list the driver in its own userclient-access entitlement.
- [com.apple.developer.driverkit.communicates-with-drivers](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.driverkit.communicates-with-drivers) - Boolean permission on an iPadOS client app to communicate with drivers.
- [com.apple.developer.driverkit.allow-third-party-userclients](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.driverkit.allow-third-party-userclients) - Boolean permission on an iPadOS driver to accept clients from other Teams; it does not waive the client's required entitlement.

### Samples
- [DriverKit sample code](https://developer.apple.com/documentation/driverkit/driverkit-sample-code) - Family-specific projects for macOS and, where supported by the individual sample and family, iPadOS.

### Services
- [Creating a Driver Using the DriverKit SDK](https://developer.apple.com/documentation/driverkit/creating-a-driver-using-the-driverkit-sdk) - Create a driver that supports proprietary features of your company's hardware devices.
- [Debugging and testing system extensions](https://developer.apple.com/documentation/driverkit/debugging-and-testing-system-extensions) - Development-only debugging options; restore normal security checks before final validation and distribution.
- **IOService** - The base class for managing the setup and registration of your driver.

### Event management
- **IODispatchQueue** - An object that manages the serial execution of blocks.
- **IOInterruptDispatchSource** - A dispatch source that reports hardware-related interrupt events to your driver.
- **IOTimerDispatchSource** - A dispatch source that notifies your driver at a specific time.
- **IODataQueueDispatchSource** - A dispatch source that manages a shared-memory data queue.
- **IODispatchSource** - The common base class for dispatch sources.
- **OSAction** - An object that executes your driver's custom behavior.

### Memory management
- **IOBufferMemoryDescriptor** - A memory buffer allocated in the caller's address space.
- **IOMemoryDescriptor** - The base class for describing a location in memory.
- **IOMemoryMap** - A mapping created through an `IOMemoryDescriptor`. It does not own the underlying memory; do not free that memory through the mapping.
- **Memory Utilities** - Allocate and deallocate memory and manage memory pointers in different address spaces.

### Registry data types
- **OSArray** - A container for an ordered, random-access collection of objects.
- **OSDictionary** - A container for a collection with elements that are key-value pairs.
- **OSBoolean** - A container for a true or false value.
- **OSData** - A container for untyped data.
- **OSNumber** - A container for an integer value.
- **OSString** - A container for managing an array of characters.
- **OSSerialization** - A container for one or more objects, serialized in a binary data format that is suitable for messaging.
- **OSCollection** - The base class for DriverKit collection objects.
- **OSContainer** - The base class for DriverKit data objects.
- **OSObject** - The base class for DriverKit objects
- **OSSymbol** - A container for managing an array of characters.
- **IOFixed** - A fixed-point number.

### External drivers
- **IOUserClient** - Represents a client connection created through the service's `NewUserClient` path when an app opens the service.
- **IOUserServer** - System-managed service infrastructure; do not create or use instances directly.
- **com.apple.developer.driverkit.userclient-access** - Client-app permission to connect to the specified macOS driver-extension bundle IDs.
- [Communicating between a DriverKit extension and a client app](https://developer.apple.com/documentation/driverkit/communicating-between-a-driverkit-extension-and-a-client-app) - Send and receive different kinds of data securely by validating inputs and asynchronously by storing and using a callback.

### Runtime support
- **OSDynamicCast** - Casts an object to the specified type, returning null if it cannot do so safely.
- **OSRequiredCast** - Returns null for a null input; aborts when a non-null object is not of the required type. It is not a substitute for checking whether a required object exists.
- **IMPL** - Legacy IIG implementation wrapper used for kernel-superclass overrides. The public DriverKit 25.5 header discourages it in favor of ordinary full-argument method definitions with the generated `_Impl` suffix; this is not a formal deprecation annotation.
- **TYPE** - IIG callback-signature annotation. A custom callback may have a different name but must match the referenced parameters and return type.
- **QUEUENAME** - Selects a named, registered dispatch queue for method execution.
- **SUPERDISPATCH** - Bridges to an inherited kernel implementation; do not use it for a `LOCALONLY` superclass method.
- **IIG_KERNEL** - Marks Apple-supplied kernel-resident classes or methods; do not add it to custom driver classes.
- **LOCAL** - Runs the method in the driver process but still permits remote invocation.
- **LOCALONLY** - Restricts the class or method to local invocation; use ordinary superclass calls rather than kernel dispatch.
- **Error Codes** - Determine the reason an operation fails.
- **C++ Runtime Support** - Low-level runtime types used by DriverKit and its interactions with the kernel, not a claim that the dext itself resides in kernel space.

### Classes
- **IOHistogramReporter**
- **IOReportLegend**
- **IOReporter**
- **IOServiceStateNotificationDispatchSource**
- **IOSimpleReporter**
- **IOStateReporter**
- **OSBundle**
- **OSMappedFile**

### Reference
- **DriverKit Structures**
- **DriverKit Enumerations**
- **DriverKit Constants**
- **DriverKit Functions**
- **DriverKit Data Types**
- **DriverKit Namespaces**

### Macros
- **Macros**
- **kIOPropertyHashTypeKey**
- **kIOPropertySHA3256Key**
- **kIOPropertySHA3384Key**
- **kIOPropertySHA3512Key**

### Enumeration Cases
- **kIOServicePMAssertionCPUBit** - When set, PM kernel will prefer to leave the CPU and core hardware running in "Dark Wake" state, instead of sleeping.
- **kIOServicePMAssertionForceFullWakeupBit** - When set, the system will immediately do a full wakeup after going to sleep.
- **kIOServicePowerCapabilityLPW**
- **kSCSICmd_ATA_PASS_THROUGH**
- **kSCSICmd_ATA_PASS_THROUGH_EXT**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/DriverKit)*

*Changed-content sources, reviewed September 8, 2026: [DriverKit entitlement requirements](https://developer.apple.com/documentation/driverkit/requesting-entitlements-for-driverkit-development.md) and [VideoDriverKit](https://developer.apple.com/documentation/videodriverkit.md).*
