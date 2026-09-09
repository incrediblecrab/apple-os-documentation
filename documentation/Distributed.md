# Distributed

Build systems that run distributed code across multiple processes and devices.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 16.0+ | macOS 13.0+ | tvOS 16.0+ | watchOS 9.0+

## Overview

Distributed actors share many characteristics with Swift actors, and include additional isolation checks to ensure location transparency and safety in a distributed environment. Similar to how actors make it easier to write concurrent code that's safe and correct to run on a single computer, distributed actors make it easier to write code that runs across multiple computers.

You use three main parts when writing code with distributed actors:

- Swift language support for actors and distributed actors. For more information, see [Concurrency in The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency).

- The Distributed module, which includes the types and protocols you need to declare and use distributed actors. For example, it has protocols to which distributed actors and distributed actor systems conform, and structures that encapsulate information about calls to a distributed actor.

- A distributed actor system, also called a cluster runtime, provides an implementation of the DistributedActorSystem protocol and coordinates between the cluster's nodes. A distributed actor is always part of some distributed actor system; that distributed actor system handles the serialization and networking necessary to perform remote method calls. For local testing, you can use LocalTestingDistributedActorSystem. For production, you can use the distributed actor system from the Swift Distributed Actors library, use another library, or write your own distributed actor system.

## Topics

### Essentials
- [DistributedActorSystem](https://developer.apple.com/documentation/distributed/distributedactorsystem.md) - Review the protocol implemented by a distributed actor runtime.

### Distributed Actors
- **DistributedActor** - Common protocol to which all distributed actors conform implicitly.
- **DistributedActorSystem** - A distributed actor system underpins and implements all functionality of distributed actors.
- **Resolvable()** - Enables the attached protocol to be resolved as a remote distributed actor reference.
- [buildDefaultDistributedRemoteActorExecutor(_:)](https://developer.apple.com/documentation/distributed/builddefaultdistributedremoteactorexecutor(_:).md) - Returns the unowned serial executor used by remote distributed actor references. This shared executor traps if a job is enqueued on it; ensure an actor is local before scheduling work on its executor.

### Remote Calls
- **RemoteCallTarget** - Represents a 'target' of a distributed call, such as a distributed func or distributed computed property. Identification schemes may vary between systems, and are subject to evolution.
- **RemoteCallArgument** - Represents an argument passed to a distributed call target.
- **DistributedTargetInvocationEncoder** - Used to encode an invocation of a distributed target (method or computed property).
- **DistributedTargetInvocationDecoder** - Decoder that must be provided to executeDistributedTarget and is used by the Swift runtime to decode arguments of the invocation.
- **DistributedTargetInvocationResultHandler** - The protocol for a distributed invocation's result handler.

### Local Testing
- **LocalTestingDistributedActorSystem** - A DistributedActorSystem designed for local only testing.
- **LocalTestingActorID**
- **LocalTestingInvocationEncoder**
- **LocalTestingInvocationDecoder**
- **LocalTestingInvocationResultHandler**

### Deprecated
- **LocalTestingActorAddress** - Deprecated alias for `LocalTestingActorID`.

### Errors
- **DistributedActorCodingError** - Error thrown by distributed actor systems while encountering encoding/decoding issues.
- **DistributedActorSystemError** - Error protocol to which errors thrown by any DistributedActorSystem should conform.
- **ExecuteDistributedTargetError** - Error thrown by executeDistributedTarget(on:target:invocationDecoder:handler:).
- **LocalTestingDistributedActorSystemError**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Distributed)*
