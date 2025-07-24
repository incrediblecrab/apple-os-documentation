# XPC

Access a low-level interprocess communication mechanism.

**Platforms:** iOS 17.4+ | iPadOS 17.4+ | Mac Catalyst 13.0+ | macOS 10.10+

## Overview

XPC provides a lightweight mechanism for basic interprocess communication. It allows you to create lightweight helper tools, called XPC services, that perform work on behalf of your app. The launchd system daemon manages these services, launching them on demand, shutting them down when idle, and restarting them if they crash. Benefits of XPC services include:

Centralize work from multiple processes or mediate access to a shared resource.

Delegate work so it continues beyond a client's life cycle.

Privilege isolation to narrow the scope of access for different functionality.

Clients that make use of these services rely on peer-to-peer XPC connections to communicate across process boundaries. There are two sides to each connection. One side, the listener or server, responds to incoming connection requests and performs tasks. The other side, the client, initiates connections to an XPC service by creating a session with a listener. Once a client establishes a connection to the listener, it sends messages and receives replies from the service.

The type of XPC service you build depends on the requirements of the work it performs. The following table summarizes the types of services available and some differences in how they behave:

**Service Type** | **Process Environment**
--- | ---
**Launch Agent** | One process per logged-in user, running as that user. If multiple users log in using fast user switching, each user has their own running process.
**Launch Daemon** | One systemwide process that runs at a higher privilege level, as the root user. LaunchDaemons can't initiate connections to user processes but can respond to requests from them.
**XPC Service** | One process per client of the service, tied to the lifetime of the client. When a client process connects to the service, launchd starts a process for the XPC service. When the client process exits, so does the XPC service. You bundle this type of service inside of an app or framework.

Note

The LaunchAgent and LaunchDaemon types require special installation and configuration. Prior to macOS 13, apps typically used installation scripts to configure these service types. In macOS 13 and later, the Service Management framework provides a new structure for packaging and installing these service types.

You can build an XPC service using C, Swift, or Objective-C. There are both high- and low-level APIs for using XPC. If your project uses the Foundation framework, NSXPCConnection provides a high-level object-oriented API that enables a transparent remote method dispatch mechanism between processes. Using NSXPCConnection in the Foundation framework lets you design a well-defined protocol for clients to use. If your project doesn't or can't link against Foundation, use the lower-level libSystem APIs in the XPC framework.

## Topics

### Essentials
- [XPC updates](https://developer.apple.com/documentation/xpc/xpc_updates) - Learn about important changes to XPC.

### Interprocess communication
- [Creating XPC services](https://developer.apple.com/documentation/xpc/creating_xpc_services) - Configure a listener, establish a client session, and exchange messages between processes.
- **XPCListener** - A type that performs tasks for clients across process boundaries.
- **XPCSession** - A type that sends messages to a server process.
- **XPCReceivedMessage** - A type that represents a message sent between a session and a listener.
- **xpc_listener_t** - A C type that performs tasks for clients across process boundaries.
- **xpc_session_t** - A C type that sends messages to a server process.

### Tasks
- [XPC activities](https://developer.apple.com/documentation/xpc/xpc_activities) - Schedule background activities for the system to execute.

### Events
- [XPC events](https://developer.apple.com/documentation/xpc/xpc_events) - Respond on demand to IOKit events and notifications.

### Additional Types
- [XPC objects](https://developer.apple.com/documentation/xpc/xpc_objects) - Encapsulate data in objects that represent primitive types, collections, and more.

### Utilities
- [Browse debugging utilities and constants to use with the XPC APIs](https://developer.apple.com/documentation/xpc/utilities).

### XPC connections
- [Create and manage connections to services using connection-based APIs](https://developer.apple.com/documentation/xpc/xpc_connections).

### Classes
- **OS_xpc_session**

### Structures
- **XPCEndpoint** - An XPCEndpoint represents a connection in serialized form. Unlike a connection, an endpoint is an inert object that does not have any runtime activity associated with it. Thus, it is safe to pass an endpoint in a message. Upon receiving an endpoint, the recipient can use XPCSession to create as many distinct sessions as desired.
- **XPCPeerRequirement** (Beta)

### Type Aliases
- **xpc_peer_requirement_t**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/XPC)*
