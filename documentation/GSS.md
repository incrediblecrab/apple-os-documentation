# GSS

Conduct secure, authenticated network transactions.

**Platforms:** iOS 5.0+ | iPadOS 5.0+ | Mac Catalyst 13.0+ | macOS 10.14+ | visionOS 1.0+

## Overview

The Generic Security Service Application Programming Interface (GSS-API) standardizes security-context establishment, peer authentication and message protection across security mechanisms. Apple's GSS framework implements this interface and its supporting libraries.

Applications carry the GSS-API tokens and protected messages over their chosen transport. A GSS security context is not itself a socket connection or a blanket authorization for other application operations.

Using GSS-API, you can:

- Establish a security context between peers and inspect the services actually negotiated for that context. Requesting a service does not guarantee that the mechanism provides it.

- Apply one or more types of protection, known as security services, to the data to be transmitted. For more on security services, see Security.

- Perform data conversion, error-checking, delegation of user privileges, information display, and identity comparison.

See [RFC 2743](https://www.rfc-editor.org/rfc/rfc2743.txt) for GSS-API Version 2, Update 1, and [RFC 2744](https://www.rfc-editor.org/rfc/rfc2744.txt) for its C bindings.

## Topics

### Memory and Context
- [Allocating and Releasing Objects](https://developer.apple.com/documentation/gss/allocating-and-releasing-objects) - Manage memory and object lifetimes.

### Function Status
- [Evaluate return values](https://developer.apple.com/documentation/gss/function-status) - Evaluate return values that most GSS-API functions use to indicate the outcome of an operation.

### Buffer Management
- [Buffer Management](https://developer.apple.com/documentation/gss/buffer-management) - Allocate and deallocate buffers with structures that hold a variety of data.

### Context Services
- [Context Services](https://developer.apple.com/documentation/gss/context-services) - Request context services and check the returned flags to determine which were enabled.

### Credentials
- [Credential Management](https://developer.apple.com/documentation/gss/credential-management) - Manage credentials used to establish security contexts.

### Security Mechanisms
- [Security Mechanisms](https://developer.apple.com/documentation/gss/security-mechanisms) - Work with the mechanisms used by the implementation.

### Names and Object Identifiers
- [Name Handling](https://developer.apple.com/documentation/gss/name-handling) - Manage names for GSS-API principals such as a person, a machine, or an application.
- [Object Identifiers](https://developer.apple.com/documentation/gss/object-identifiers) - Identify security mechanisms and GSS-API name types.

### Messages
- [Token Management](https://developer.apple.com/documentation/gss/token-management) - Exchange opaque tokens to establish and use security contexts.
- [Message Protection](https://developer.apple.com/documentation/gss/message-protection) - Apply the negotiated message-protection services.

### Kerberos Implementation
- [Kerberos Implementation](https://developer.apple.com/documentation/gss/kerberos-implementation) - Use the Kerberos implementation of GSS-API.

### Structure and Macros
- [Structures and macros](https://developer.apple.com/documentation/gss/structures-and-macros)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/GSS)*
