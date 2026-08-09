# Exception Handling

Monitor and debug exceptional conditions in code.

**Platforms:** Mac Catalyst 13.0+ | macOS 10.0+

## Overview

This collection of documents provides the API reference for the Exception Handling framework. This framework provides facilities for monitoring and debugging exceptional conditions in Objective-C code.

Currently only one class reference is part of this collection: the reference for the NSExceptionHandler class, which is defined in NSExceptionHandler.h.

## Topics

### Classes
- **NSExceptionHandler** - The NSExceptionHandler class provides facilities for monitoring and debugging exceptional conditions in Objective-C programs. It works by installing a special uncaught exception handler via the NSSetUncaughtExceptionHandler(_:) function. Consequently, to use the services of NSExceptionHandler, you must not install your own custom uncaught exception handler.

### Protocols
- **NSExceptionHandlerDelegate** - The NSExceptionHandlerDelegate informal protocol describes methods that NSExceptionHandler objects call on their delegates when exceptions occur. An NSExceptionHandler object does not need to have a delegate. When one does, these delegate methods are asked to approve exception handling and logging for each monitored NSExceptionHandler object.

### Reference
- **ExceptionHandling Enumerations**
- **ExceptionHandling Constants**
- **ExceptionHandling Functions**

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ExceptionHandling)*