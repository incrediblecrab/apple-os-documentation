# Objective-C Runtime

Gain low-level access to the Objective-C runtime and the Objective-C root types.

**Platforms:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 13.0+ | macOS 10.0+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 2.0+

## Overview

The Objective-C Runtime module APIs define the base of the Objective-C language. These APIs include:

- Types such as the NSObject class and the NSObjectProtocol protocol that provide the root functionality of most Objective-C classes
- Functions and data structures that comprise the Objective-C runtime, which provides support for the dynamic properties of the Objective-C language

You typically don't need to use this module directly.

## Topics

### Classes
- **NSObject** - The root class of most Objective-C class hierarchies, from which subclasses inherit a basic interface to the runtime system and the ability to behave as Objective-C objects.
- **Protocol**

### Protocols
- **NSObjectProtocol** - The group of methods that are fundamental to all Objective-C objects.

### Reference
- **Objective-C Runtime** - Describes the macOS Objective-C runtime library support functions and data structures.
- **Objective-C Structures**
- **Objective-C Constants**
- **Objective-C Functions**
- **Objective-C Data Types**
- **Objective-C Macros**
- **Objective-C Enumerations**

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ObjectiveC)*