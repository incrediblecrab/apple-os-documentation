# Dispatch

Execute code concurrently on multicore hardware by submitting work to dispatch queues managed by the system.

**Platforms (current Swift API catalog):** iOS 8.0+ | iPadOS 8.0+ | Mac Catalyst 13.0+ | macOS 10.10+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 2.0+

These catalog minima are not GCD's introduction dates. For example, the C [`dispatch_retain`](https://developer.apple.com/documentation/dispatch/dispatch_retain) API dates to iOS 4 and macOS 10.6; individual Swift interfaces can require later versions.

## Overview

Dispatch, also known as Grand Central Dispatch (GCD), contains language features, runtime libraries, and system enhancements that provide systemic, comprehensive improvements to the support for concurrent code execution on multicore hardware in macOS, iOS, watchOS, and tvOS.

The BSD subsystem, Core Foundation, and Cocoa APIs have all been extended to use these enhancements to help both the system and your application to run faster, more efficiently, and with improved responsiveness. Consider how difficult it is for a single application to use multiple cores effectively, let alone to do it on different computers with different numbers of computing cores or in an environment with multiple applications competing for those cores. GCD, operating at the system level, can better accommodate the needs of all running applications, matching them to the available system resources in a balanced fashion.

### Dispatch Objects and ARC

With Objective-C dispatch-object support enabled, ARC retains and releases dispatch objects automatically. The C reference describes this as the usual behavior for deployment targets of iOS 6/macOS 10.8 and later. In manually managed Objective-C/C code, balance `dispatch_retain` and `dispatch_release`; do not substitute Core Foundation retain/release functions. Global main and concurrent dispatch queues do not require manual retention.

For compatibility with manually managed C/Objective-C code, `-DOS_OBJECT_USE_OBJC=0` disables Objective-C dispatch-object support. This is not a Swift compiler option or a requirement for ordinary Swift `DispatchQueue` use.

## Topics

### Queues and Tasks
- **DispatchQueue** - An object that manages the execution of tasks serially or concurrently on your app's main thread or on a background thread.
- **DispatchWorkItem** - The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- **DispatchGroup** - A group of tasks that you monitor as a single unit.
- **Dispatch Queue** - An object that manages the execution of tasks serially or concurrently on your app's main thread or on a background thread.
- **Dispatch Work Item** - The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- **Dispatch Group** - A group of tasks that you monitor as a single unit.
- **Workloop** - A dispatch object that prioritizes the execution of tasks based on their quality-of-service (QoS) level.

### Thread Scheduling
- **DispatchQoS** - The quality of service, or the execution priority, to apply to tasks.

### System Event Monitoring
- **DispatchSource** - An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- **Dispatch Source** - An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- **DispatchIO** - An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- **DispatchData** - An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- **DispatchDataIterator** - A byte-by-byte iterator over the contents of a dispatch data object.
- **Dispatch I/O** - An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- **Dispatch Data** - An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- **DispatchSourceProtocol** - Defines a common set of properties and methods that are shared with all dispatch source types.

### Task Synchronization
- **DispatchSemaphore** - An object that controls access to a resource across multiple execution contexts through use of a traditional counting semaphore.
- **Dispatch Semaphore** - An object that controls access to a resource across multiple execution contexts through use of a traditional counting semaphore.
- **Dispatch Barrier** - A synchronization point for tasks executing in a concurrent dispatch queue.

### Time Constructs
- **DispatchTime** - A point in time relative to the default clock, with nanosecond precision.
- **DispatchWallTime** - An absolute point in time according to the wall clock, with microsecond precision.
- **DispatchTimeInterval** - A number of seconds, milliseconds, microseconds, or nanoseconds.
- **DispatchTimeoutResult** - A result value indicating whether a dispatch operation finished before a specified time.
- `typealias dispatch_time_t = UInt64` - An abstract representation of time.
- `var DISPATCH_WALLTIME_NOW: UInt { get }` - The current time; iOS/iPadOS/tvOS 12+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1+, watchOS 5+.
- **Wall Time Constants** - Constants for wall time values.

### Dispatch Objects
- **DispatchObject** - The base class for most dispatch types.
- **DispatchPredicate** - Logical conditions to evaluate within a given execution context.
- `func dispatchPrecondition(condition: @autoclosure () -> DispatchPredicate)` - Checks a dispatch condition necessary for further execution.
- **Dispatch Objects** - The basic behaviors supported by all dispatch types.

### Deprecated
- **Deprecated Symbols**

### Classes
- **DispatchWorkloop**

### Reference
- **Dispatch Constants**
- **Dispatch Data Types**
- **Dispatch Functions**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Dispatch)*
