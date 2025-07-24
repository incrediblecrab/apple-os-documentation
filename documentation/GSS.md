# GSS

Conduct secure, authenticated network transactions.

**Platforms:** iOS 5.0+ | iPadOS 5.0+ | Mac Catalyst 13.0+ | macOS 10.14+ | visionOS 1.0+

## Overview

The open source Generic Security Service Application Programming Interface (GSS-API) defines a standardized interface through which the operating system vends secure data transport operations. The GSS framework provides an implementation of the interface and the underlying libraries.

Using GSS-API, you can:

- Create a security context in which data can be passed between applications. A context represents a "state of trust" between two applications. Applications that share a context recognize each other and permit data transfers as long as the context lasts.

- Apply one or more types of protection, known as security services, to the data to be transmitted. For more on security services, see Security.

- Perform data conversion, error-checking, delegation of user privileges, information display, and identity comparison.

See RFC 2743 for the definitive description of the GSS-API 2, and RFC 2744 for a description of the related C bindings.

## Topics

### Memory and Context
- [Allocating and Releasing Objects](https://developer.apple.com/documentation/gss/allocating_and_releasing_objects) - Manage memory and object lifetimes.

### Function Status
- [Evaluate return values](https://developer.apple.com/documentation/gss/function_status) - Evaluate return values that most GSS-API functions use to indicate the outcome of an operation.

### Buffer Management
- [Buffer Management](https://developer.apple.com/documentation/gss/buffer_management) - Allocate and deallocate buffers with structures that hold a variety of data.

### Context Services
- [Context Services](https://developer.apple.com/documentation/gss/context_services) - Use context services to manage secure operations between endpoints.

### Credentials
- [Credential Management](https://developer.apple.com/documentation/gss/credential_management) - Securely establish connections between endpoints.

### Security Mechanisms
- [Security Mechanisms](https://developer.apple.com/documentation/gss/security_mechanisms) - Provide a security mechanism for your implementation.

### Names and Object Identifiers
- [Name Handling](https://developer.apple.com/documentation/gss/name_handling) - Manage names for GSS-API principals such as a person, a machine, or an application.
- [Object Identifiers](https://developer.apple.com/documentation/gss/object_identifiers) - Store security mechanisms, QOPs (Quality of Protection values), and name types.

### Messages
- [Token Management](https://developer.apple.com/documentation/gss/token_management) - Establish secure communication with tokens.
- [Message Protection](https://developer.apple.com/documentation/gss/message_protection) - Provide cryptographic protection to secure message integrity.

### Kerberos Implementation
- [Kerberos Implementation](https://developer.apple.com/documentation/gss/kerberos_implementation) - Establish secure connections using the Kerberos implementation of GSS-API.

### Structure and Macros
- [Structures and macros](https://developer.apple.com/documentation/gss/structures_and_macros)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/GSS)*