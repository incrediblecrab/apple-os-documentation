# Swift

Build apps using a powerful open language.

**Platforms:** iOS 8.0+ | iPadOS 8.0+ | Mac Catalyst 13.0+ | macOS 10.10+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 2.0+

## Overview

Swift combines type inference, optionals, closures, memory-safety features, and native error handling. It is designed for efficient native execution and supports interactive coding in Swift Playgrounds, Xcode playgrounds, and the REPL.

```swift
var interestingNumbers = [
    "primes": [2, 3, 5, 7, 11, 13, 17],
    "triangular": [1, 3, 6, 10, 15, 21, 28],
    "hexagonal": [1, 6, 15, 28, 45, 66, 91]
]

for key in interestingNumbers.keys {
    interestingNumbers[key]?.sort(by: >)
}

print(interestingNumbers["primes"]!)
// Prints "[17, 13, 11, 7, 5, 3, 2]"
```

### Learn Swift

If you're new to Swift, read The Swift Programming Language for a quick tour, a comprehensive language guide, and a full reference manual. If you're new to programming, check out Swift Playgrounds on iPad.

Swift is developed in the open. To learn more about the open source Swift project and community, visit Swift.org.

## Swift 6.4 in Xcode 27

[Xcode 27](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes.md) (build `27A266a`, shipped September 14, 2026) includes the Swift 6.4 compiler. The compiler version is separate from a target's **Swift language mode**: installing a new compiler does not by itself migrate a Swift 5-mode target to Swift 6.

The following changes are recorded in the [Swift `release/6.4.x` changelog](https://raw.githubusercontent.com/swiftlang/swift/release/6.4.x/CHANGELOG.md). An accepted evolution proposal alone is not evidence that a feature is included in this toolchain.

| Feature | What it does |
|---|---|
| `anyAppleOS` availability | Shorthand for Apple OS versions **26.0 and later**; an explicitly listed platform version takes precedence |
| `@diagnose(GroupID, as: ...)` | Override an existing compiler **warning group's** severity within a declaration's lexical scope; optionally document the reason |
| `~Sendable` | Explicitly opt a type out of `Sendable` inference |
| Async `defer` | Allow asynchronous cleanup with the enclosing scope's isolation |
| `withTaskCancellationShield` | Temporarily prevent observation of cancellation during bounded cleanup; not a lock or a transaction |
| Noncopyable/non-escapable associated types | Permit protocol associated-type requirements with `~Copyable` and/or `~Escapable` |
| Throwing tasks | Unstructured throwing task initializers use typed throws and warn about implicitly unused tasks; retain and handle their results |

Migration-sensitive changes in the same changelog include:

- Library-evolution module interfaces use **module selectors** by default to reduce name collisions and ambiguity; review flags previously used to work around those issues.
- Forward references to local variables are checked consistently inside closures, including previously accepted lazy-local and local-computed-variable cases.
- Raw-span accessors and generic raw-output append operations gain missing `@unsafe` annotations; review code that reinterprets values with padding as initialized bytes.
- The `SwiftImportAs` API note can import C structs as `OpaquePointer`, helping keep imported pointer types consistent across platform headers.

For example, a platform-specific minimum overrides the `anyAppleOS` shorthand:

```swift
@available(anyAppleOS 26.0, macOS 26.4, *)
func performPlatformSpecificWork() { }
```

`weak let` is a **Swift 6.3** feature, not new in 6.4: [SE-0481](https://raw.githubusercontent.com/swiftlang/swift-evolution/main/proposals/0481-weak-let.md) records that implementation version. An immutable weak reference still becomes `nil` when its referent is destroyed.

**Toolchain requirements**

Xcode 27 requires **Apple silicon and macOS Tahoe 26.6 or later**, not macOS 27. The release notes explicitly state the IDE's hardware restriction; it is not inferred from the host OS. Host requirements, SDK versions, deployment targets, language mode, and runtime API availability are separate constraints. See [Xcode](Xcode.md), [Swift packages](swift-packages.md), and the [concurrency migration recipe](../guides/swift-concurrency-migration.md).

**Source compatibility:** The Xcode release notes identify a source break for a computed property with an `init` accessor and an array/dictionary literal initializer when the getter precedes the `init` accessor (180969028). The documented workaround is to put the `init` accessor first.

## Topics

### Essentials
- [Swift updates](https://developer.apple.com/documentation/updates/swift.md) - Learn about important changes to Swift
- [Adopting strict concurrency in Swift 6 apps](https://developer.apple.com/documentation/swift/adoptingswift6.md) - Enable strict concurrency checking to find data races at compile time

### Standard Library
- **Int** - A signed integer value type
- **Double** - A double-precision, floating-point value type
- **String** - A Unicode string value that is a collection of characters
- **Array** - An ordered, random-access collection
- **Dictionary** - A collection whose elements are key-value pairs
- **Swift Standard Library** - Solve complex problems and write high-performance, readable code

### Observation
- **Observation**

### Distributed Actors
- **Distributed** - Build systems that run distributed code across multiple processes and devices

### Regular Expression DSL
- **RegexBuilder** - Use an expressive domain-specific language to build regular expressions, for operations like searching and replacing in text

### Low-Level Atomic Operations
- **Synchronization** - Build synchronization constructs using low-level, primitive operations

### Data Modeling
- [Choosing Between Structures and Classes](https://developer.apple.com/documentation/swift/choosing-between-structures-and-classes.md) - Decide how to store data and model behavior
- [Adopting Common Protocols](https://developer.apple.com/documentation/swift/adopting-common-protocols.md) - Make your custom types easier to use by ensuring that they conform to Swift protocols

### Data Flow and Control Flow
- [Maintaining State in Your Apps](https://developer.apple.com/documentation/swift/maintaining-state-in-your-apps.md) - Use enumerations to capture and track the state of your app
- [Preventing Timing Problems When Using Closures](https://developer.apple.com/documentation/swift/preventing-timing-problems-when-using-closures.md) - Understand how different API calls to your closures can affect your app

### Language Interoperability with Objective-C and C
- [Objective-C and C Code Customization](https://developer.apple.com/documentation/swift/objective-c-and-c-code-customization.md) - Apply macros to your Objective-C APIs to customize how they're imported into Swift
- [Migrating Your Objective-C Code to Swift](https://developer.apple.com/documentation/swift/migrating-your-objective-c-code-to-swift.md) - Learn the recommended steps to migrate your code
- [Cocoa Design Patterns](https://developer.apple.com/documentation/swift/cocoa-design-patterns.md) - Adopt and interoperate with Cocoa design patterns in your Swift apps
- [Handling Dynamically Typed Methods and Objects in Swift](https://developer.apple.com/documentation/swift/handling-dynamically-typed-methods-and-objects-in-swift.md) - Cast instances of the Objective-C id type to a specific Swift type
- [Using Objective-C Runtime Features in Swift](https://developer.apple.com/documentation/swift/using-objective-c-runtime-features-in-swift.md) - Use selectors and key paths to interact with dynamic Objective-C APIs
- [Imported C and Objective-C APIs](https://developer.apple.com/documentation/swift/imported-c-and-objective-c-apis.md) - Use native Swift syntax to interoperate with types and functions in C and Objective-C
- [Calling Objective-C APIs Asynchronously](https://developer.apple.com/documentation/swift/calling-objective-c-apis-asynchronously.md) - Learn how functions and methods that take a completion handler are converted to Swift asynchronous functions

### Language Interoperability with C++
- [Mixing Languages in an Xcode project](https://developer.apple.com/documentation/swift/mixinglanguagesinanxcodeproject.md) - Use C++ APIs in Swift – and Swift APIs in C++ – in a single framework target, and consume the framework's APIs in a separate app target
- [Calling APIs Across Language Boundaries](https://developer.apple.com/documentation/swift/callingapisacrosslanguageboundaries.md) - Use a variety of C++ APIs in Swift – and vice-versa – across multiple targets and frameworks in an Xcode project

### Functions (Deprecated)
- **async** functions - Deprecated, available only for source compatibility reasons
- **asyncDetached** functions - Deprecated, available only for source compatibility reasons
- **detach** functions - Deprecated, available only for source compatibility reasons

The [Swift 6.4 task initializer source](https://raw.githubusercontent.com/swiftlang/swift/release/6.4.x/stdlib/public/Concurrency/Task+init.swift.gyb) retains these legacy task-creation helpers. Use `Task.init` or `Task.detached` in new code. This deprecation does not apply to the `async` and `await` language keywords.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Swift)*
