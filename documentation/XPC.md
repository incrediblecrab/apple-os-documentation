# XPC

Access a low-level interprocess communication mechanism.

**Platforms:** iOS 17.4+ | iPadOS 17.4+ | Mac Catalyst 13.0+ | macOS 10.10+

These are Apple's framework-catalog entries, not the introduction versions of every XPC type or method. The helper-process installation model below is for macOS.

## Overview

XPC provides structured interprocess communication. On macOS, `launchd` can start a configured service when a client connects and reclaim an idle service process. Restart and continued execution depend on the service kind and job configuration, not merely on using XPC.

- Isolate work and privileges in separate processes.
- Mediate shared resources through a service with the appropriate user or system scope.
- Exchange requests and replies without assuming the helper survives its client.

Clients that make use of these services rely on peer-to-peer XPC connections to communicate across process boundaries. There are two sides to each connection. One side, the listener or server, responds to incoming connection requests and performs tasks. The other side, the client, initiates connections to an XPC service by creating a session with a listener. Once a client establishes a connection to the listener, it sends messages and receives replies from the service.

Choose the service's macOS deployment and lifetime model separately from its message transport:

**Service Type** | **Process Environment**
--- | ---
**Launch Agent** | A job in a user's context. Multiple user sessions can have separate instances, but load conditions and demand determine whether a process is currently running.
**Launch Daemon** | A system-domain job. Its configured `UserName`/`GroupName` may select an identity other than root. Bootstrap namespaces and connection policy matter; there is no universal rule that all daemon IPC must be initiated by a user process.
**Embedded per-client XPC service** | An app- or framework-bundled service launched on demand for a client. Its process lifetime is tied to that client; do not use this model to promise work continues after the client exits.

Launch agents and daemons require installation and configuration. In macOS 13+, [Service Management](ServiceManagement.md) provides bundled-helper registration and authorization APIs; earlier deployments commonly use installer-managed property lists. Successful registration is not proof that a helper is running or still approved.

Use the C APIs in libxpc/libSystem, Swift's listener and session interfaces, or Foundation's higher-level `NSXPCConnection`, according to the API generation and message model you need. `NSXPCConnection` uses a defined object-oriented protocol for remote method dispatch.

### API and platform boundaries

| Interface | macOS / Mac Catalyst minimum |
| --- | --- |
| `XPCListener` service construction, `XPCSession` service construction, and the original Swift message types | macOS 14 / Mac Catalyst 17 |
| `XPCEndpoint`, anonymous listeners, and endpoint-based Swift sessions | macOS 15 / Mac Catalyst 18 |
| `XPCPeerRequirement` and its Swift session requirement API | macOS 26 / Mac Catalyst 26 |

The type declarations for `XPCListener`, `XPCSession`, and `XPCReceivedMessage` also list mobile platforms, but the public Swift service constructors used in the linked example are macOS/Mac Catalyst APIs. A type-level iOS, tvOS, watchOS, or visionOS listing does not make every initializer available or permit arbitrary bundled helper installation there.

### Peer and message validation

Authenticate the peer and validate the requested operation and payload separately. With the macOS 26 Swift API, set [`XPCSession.setPeerRequirement(_:)`](https://developer.apple.com/documentation/xpc/xpcsession/setpeerrequirement(_:)) while the session is **inactive**, and do not set it repeatedly on the same session. If an expected reply comes from a peer that fails the requirement, the session is canceled with a code-signing error delivered to its cancellation handler.

An entitlement-presence check is different from requiring a particular Boolean, string, or integer value. Use the appropriate [`XPCPeerRequirement`](https://developer.apple.com/documentation/xpc/xpcpeerrequirement) constructor for the policy; a matching identity alone does not validate a message's contents. Handle rejected requests, decoding failures, cancellation, and lost helpers instead of treating an endpoint or successful connection as permanent authorization.

## Topics

### Essentials
- [XPC updates](https://developer.apple.com/documentation/updates/xpc) - Learn about important changes to XPC.

### Interprocess communication
- [Creating XPC services](https://developer.apple.com/documentation/xpc/creating-xpc-services) - Configure a macOS listener, establish a client session, and exchange messages between processes.
- **XPCListener** - A type that performs tasks for clients across process boundaries.
- **XPCSession** - A type that sends messages to a server process.
- **XPCReceivedMessage** - A type that represents a message sent between a session and a listener.
- **xpc_listener_t** - A C type that performs tasks for clients across process boundaries.
- **xpc_session_t** - A C type that sends messages to a server process.

### Tasks
- [XPC activities](https://developer.apple.com/documentation/xpc/xpc-activities) - macOS activity scheduling according to system criteria, not guaranteed continuous runtime. The C registration API dates to macOS 10.9, independently of the framework catalog's displayed baseline.

### Events
- [XPC events](https://developer.apple.com/documentation/xpc/xpc-events) - Respond on demand to IOKit events and notifications.

### Additional Types
- [XPC objects](https://developer.apple.com/documentation/xpc/xpc-objects) - Encapsulate data in objects that represent primitive types, collections, and more.

### Utilities
- [Browse debugging utilities and constants to use with the XPC APIs](https://developer.apple.com/documentation/xpc/utilities).

### XPC connections
- [Create and manage connections to services using connection-based APIs](https://developer.apple.com/documentation/xpc/xpc-connections). These remain useful when an API supplies `xpc_connection_t`; new protocols can generally use listeners and sessions instead.

### Classes
- **OS_xpc_session**

### Structures
- [XPCEndpoint](https://developer.apple.com/documentation/xpc/xpcendpoint) - An inert, serializable reference from which a recipient may create sessions. Passing it does not itself create a live connection or guarantee that a later session succeeds.
- [XPCPeerRequirement](https://developer.apple.com/documentation/xpc/xpcpeerrequirement) - Requirements for peer identity or entitlements; macOS 26 / Mac Catalyst 26.

### Type Aliases
- **xpc_peer_requirement_t**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/XPC)*
