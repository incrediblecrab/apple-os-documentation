# Observation

Make responsive apps that update the presentation when underlying data changes.

**Platforms:** iOS 17.0+ | iPadOS 17.0+ | Mac Catalyst 17.0+ | macOS 14.0+ | tvOS 17.0+ | visionOS 1.0+ | watchOS 10.0+

## Overview

Observation provides a robust, type-safe, and performant implementation of the observer design pattern in Swift. This pattern allows an observable object to maintain a list of observers and notify them of specific or general state changes. This has the advantages of not directly coupling objects together and allowing implicit distribution of updates across potential multiple observers.

The Observation framework provides the following capabilities:

- Marking a type as observable
- Tracking changes within an instance of an observable type
- Observing and utilizing those changes elsewhere, such as in an app's user interface

Attach `@Observable` to a model class to synthesize observation support and `Observable` conformance:

```swift
import Observation

@Observable
class Car {
    var name: String = ""
    var needsRepairs: Bool = false
    
    init(name: String, needsRepairs: Bool = false) {
        self.name = name
        self.needsRepairs = needsRepairs
    }
}
```

`withObservationTracking(_:onChange:)` tracks the properties read by its `apply` closure. Here, changing `name` invalidates the registration; changing `needsRepairs` does not. The callback is one-shot: [SE-0395](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0395-observability.md) specifies the first change to a tracked property. Schedule a new render/registration to continue observing.

```swift
@MainActor
func render(cars: [Car]) {
    withObservationTracking {
        for car in cars {
            print(car.name)
        }
    } onChange: {
        print("Schedule renderer.")
    }
}
```

## Topics

### Concurrency and framework integration
- [`Observations`](https://developer.apple.com/documentation/observation/observations) is an asynchronous sequence of transactional changes on iOS/iPadOS/Mac Catalyst/macOS/tvOS/visionOS/watchOS 26+. Its element must be `Sendable`; the sequence does not make the observed model automatically thread-safe.
- The original [`withObservationTracking(_:onChange:)`](https://developer.apple.com/documentation/observation/withobservationtracking(_:onchange:)) API remains available at this framework's earlier minimums and tracks the properties actually read by its closure.
- Xcode 27 changes SwiftUI's `@State` implementation and initialization rules, with behavior back-deployed to the iOS 17-aligned systems. See [SwiftUI state initialization](SwiftUI.md#state-initialization-in-xcode-27); do not describe this as a new OS 27 minimum for `@Observable`.
- [AppKit](AppKit.md#controls-input-and-observation) and [UIKit](UIKit.md#text-and-framework-integration) integrate automatic tracking into supported view/layout update paths. Use their documented hooks rather than assuming every arbitrary closure is tracked.

### Observable conformance
- **Observable()** - Defines and implements conformance of the Observable protocol.
- **Observable** - A type that emits notifications to observers when underlying data changes.

### Change tracking
- **withObservationTracking** - Tracks access to properties.
- **ObservationRegistrar** - Provides storage for tracking and access to data changes.

### Observation in SwiftUI
- [Managing model data in your app](https://developer.apple.com/documentation/swiftui/managing-model-data-in-your-app) - Create connections between your app's data model and views.
- [Migrating from the Observable Object protocol to the Observable macro](https://developer.apple.com/documentation/swiftui/migrating-from-the-observable-object-protocol-to-the-observable-macro) - Update your existing app to leverage the benefits of Observation in Swift.

### Structures
- **Observations** - An asynchronous sequence generated from a closure that tracks the transactional changes of @Observable types.
### Macros
- **ObservationIgnored()** - Disables observation tracking of a property.
- **ObservationTracked()** - Synthesizes property accessors as part of the framework's implementation; ordinary clients normally use `@Observable` rather than applying this macro directly.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Observation)*
