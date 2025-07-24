# Combine

Customize handling of asynchronous events by combining event-processing operators.

**Platforms:** iOS 13.0+ | iPadOS 13.0+ | Mac Catalyst 13.0+ | macOS 10.15+ | tvOS 13.0+ | visionOS 1.0+ | watchOS 6.0+

## Overview

The Combine framework provides a declarative Swift API for processing values over time. These values can represent many kinds of asynchronous events. Combine declares publishers to expose values that can change over time, and subscribers to receive those values from the publishers.

The Publisher protocol declares a type that can deliver a sequence of values over time. Publishers have operators to act on the values received from upstream publishers and republish them.

At the end of a chain of publishers, a Subscriber acts on elements as it receives them. Publishers only emit values when explicitly requested to do so by subscribers. This puts your subscriber code in control of how fast it receives events from the publishers it's connected to.

Several Foundation types expose their functionality through publishers, including Timer, NotificationCenter, and URLSession. Combine also provides a built-in publisher for any property that's compliant with Key-Value Observing.

You can combine the output of multiple publishers and coordinate their interaction. For example, you can subscribe to updates from a text field's publisher, and use the text to perform URL requests. You can then use another publisher to process the responses and use them to update your app.

By adopting Combine, you'll make your code easier to read and maintain, by centralizing your event-processing code and eliminating troublesome techniques like nested closures and convention-based callbacks.

## Topics

### Essentials
- [Receiving and Handling Events with Combine](https://developer.apple.com/documentation/Combine/receiving_and_handling_events_with_combine) - Customize and receive events from asynchronous sources.

### Publishers
- **Publisher** - Declares that a type can transmit a sequence of values over time.
- **Publishers** - A namespace for types that serve as publishers.
- **AnyPublisher** - A publisher that performs type erasure by wrapping another publisher.
- **Published** - A type that publishes a property marked with an attribute.
- **Cancellable** - A protocol indicating that an activity or action supports cancellation.
- **AnyCancellable** - A type-erasing cancellable object that executes a provided closure when canceled.

### Convenience Publishers
- **Future** - A publisher that eventually produces a single value and then finishes or fails.
- **Just** - A publisher that emits an output to each subscriber just once, and then finishes.
- **Deferred** - A publisher that awaits subscription before running the supplied closure to create a publisher for the new subscriber.
- **Empty** - A publisher that never publishes any values, and optionally finishes immediately.
- **Fail** - A publisher that immediately terminates with the specified error.
- **Record** - A publisher that allows for recording a series of inputs and a completion, for later playback to each subscriber.

### Connectable Publishers
- [Controlling Publishing with Connectable Publishers](https://developer.apple.com/documentation/Combine/controlling_publishing_with_connectable_publishers) - Coordinate when publishers start sending elements to subscribers.
- **ConnectablePublisher** - A publisher that provides an explicit means of connecting and canceling publication.

### Subscribers
- [Processing Published Elements with Subscribers](https://developer.apple.com/documentation/Combine/processing_published_elements_with_subscribers) - Apply back pressure to precisely control when publishers produce elements.
- **Subscriber** - A protocol that declares a type that can receive input from a publisher.
- **Subscribers** - A namespace for types that serve as subscribers.
- **AnySubscriber** - A type-erasing subscriber.
- **Subscription** - A protocol representing the connection of a subscriber to a publisher.
- **Subscriptions** - A namespace for symbols related to subscriptions.

### Subjects
- **Subject** - A publisher that exposes a method for outside callers to publish elements.
- **CurrentValueSubject** - A subject that wraps a single value and publishes a new element whenever the value changes.
- **PassthroughSubject** - A subject that broadcasts elements to downstream subscribers.

### Schedulers
- **Scheduler** - A protocol that defines when and how to execute a closure.
- **ImmediateScheduler** - A scheduler for performing synchronous actions.
- **SchedulerTimeIntervalConvertible** - A protocol that provides a scheduler with an expression for relative time.

### Combine Migration
- [Routing Notifications to Combine Subscribers](https://developer.apple.com/documentation/Combine/routing_notifications_to_combine_subscribers) - Deliver notifications to subscribers by using notification centers' publishers.
- [Replacing Foundation Timers with Timer Publishers](https://developer.apple.com/documentation/Combine/replacing_foundation_timers_with_timer_publishers) - Publish elements periodically by using a timer.
- [Performing Key-Value Observing with Combine](https://developer.apple.com/documentation/Combine/performing_key-value_observing_with_combine) - Expose KVO changes with a Combine publisher.
- [Using Combine for Your App's Asynchronous Code](https://developer.apple.com/documentation/Combine/using_combine_for_your_app_s_asynchronous_code) - Apply common patterns to migrate your closure-based, event-handling code.

### Observable Objects
- **ObservableObject** - A type of object with a publisher that emits before the object has changed.
- **ObservableObjectPublisher** - A publisher that publishes changes from observable objects.

### Asynchronous Publishers
- **AsyncPublisher** - A publisher that exposes its elements as an asynchronous sequence.
- **AsyncThrowingPublisher** - A publisher that exposes its elements as a throwing asynchronous sequence.

### Encoders and Decoders
- **TopLevelEncoder** - A type that defines methods for encoding.
- **TopLevelDecoder** - A type that defines methods for decoding.

### Debugging Identifiers
- **CustomCombineIdentifierConvertible** - A protocol for uniquely identifying publisher streams.
- **CombineIdentifier** - A unique identifier for identifying publisher streams.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Combine)*