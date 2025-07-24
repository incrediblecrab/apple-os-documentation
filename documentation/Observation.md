# Observation

Make responsive apps that update the presentation when underlying data changes.

**Platforms:** iOS 17.0+ | iPadOS 17.0+ | Mac Catalyst 17.0+ | macOS 14.0+ | tvOS 17.0+ | visionOS 1.0+ | watchOS 10.0+

## Overview

Observation provides a robust, type-safe, and performant implementation of the observer design pattern in Swift. This pattern allows an observable object to maintain a list of observers and notify them of specific or general state changes. This has the advantages of not directly coupling objects together and allowing implicit distribution of updates across potential multiple observers.

The Observation frameworks provides the following capabilities:

- Marking a type as observable
- Tracking changes within an instance of an observable type
- Observing and utilizing those changes elsewhere, such as in an app's user interface

To declare a type as observable, attach the Observable() macro to the type declaration. This macro declares and implements conformance to the Observable protocol to the type at compile time.

```swift
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

To track changes, use the withObservationTracking(_:onChange:) function. For example, in the following code, the function calls the onChange closure when a car's name changes. However, it doesn't call the closure when a car's needsRepair flag changes. That's because the function only tracks properties read in its apply closure, and the closure doesn't read the needsRepair property.

```swift
func render() {
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

### Observable conformance
- **Observable()** - Defines and implements conformance of the Observable protocol.
- **Observable** - A type that emits notifications to observers when underlying data changes.

### Change tracking
- **withObservationTracking** - Tracks access to properties.
- **ObservationRegistrar** - Provides storage for tracking and access to data changes.

### Observation in SwiftUI
- [Managing model data in your app](https://developer.apple.com/documentation/observation/managing_model_data_in_your_app) - Create connections between your app's data model and views.
- [Migrating from the Observable Object protocol to the Observable macro](https://developer.apple.com/documentation/observation/migrating_from_the_observable_object_protocol_to_the_observable_macro) - Update your existing app to leverage the benefits of Observation in Swift.

### Structures
- **Observations** - An asychronous sequence generated from a closure that tracks the transactional changes of @Observable types. (Beta)

### Macros
- **ObservationIgnored()** - Disables observation tracking of a property.
- **ObservationTracked()** - Synthesizes a property for accessors.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Observation)*