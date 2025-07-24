# Dispatch

Execute code concurrently on multicore hardware by submitting work to dispatch queues managed by the system.

**Platforms:** iOS 8.0+ | iPadOS 8.0+ | Mac Catalyst 13.0+ | macOS 10.10+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 2.0+

## Overview

Dispatch, also known as Grand Central Dispatch (GCD), contains language features, runtime libraries, and system enhancements that provide systemic, comprehensive improvements to the support for concurrent code execution on multicore hardware in macOS, iOS, watchOS, and tvOS.

The BSD subsystem, Core Foundation, and Cocoa APIs have all been extended to use these enhancements to help both the system and your application to run faster, more efficiently, and with improved responsiveness. Consider how difficult it is for a single application to use multiple cores effectively, let alone to do it on different computers with different numbers of computing cores or in an environment with multiple applications competing for those cores. GCD, operating at the system level, can better accommodate the needs of all running applications, matching them to the available system resources in a balanced fashion.

### Dispatch Objects and ARC

When you build your app using the Objective-C compiler, all dispatch objects are Objective-C objects. As such, when automatic reference counting (ARC) is enabled, dispatch objects are retained and released automatically, just like any other Objective-C object. When ARC is not enabled, use the dispatch_retain and dispatch_release functions (or Objective-C semantics) to retain and release your dispatch objects. You cannot use the Core Foundation retain and release functions.

If you need to use retain and release semantics in an ARC-enabled app with a later deployment target (for maintaining compatibility with existing code), you can disable Objective-C-based dispatch objects by adding -DOS_OBJECT_USE_OBJC=0 to your compiler flags.

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
- **DispatchTimeInterval** - A number of seconds, millisconds, microseconds, or nanoseconds.
- **DispatchTimeoutResult** - A result value indicating whether a dispatch operation finished before a specified time.
- `typealias dispatch_time_t` - An abstract representation of time.
- `var DISPATCH_WALLTIME_NOW: UInt` - The current time.
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