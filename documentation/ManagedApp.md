# ManagedApp

Customize your app for managed deployments by providing configurable features that rely on secure access to secrets and data that an administrator provisions.

**Provider API availability:** iOS 18.4+ | iPadOS 18.4+ | visionOS 2.4+ | macOS 27.0 beta. The individual configuration, secret-provider, and error declarations add Mac support in 27; the framework overview still lists the earlier mobile platforms.

## Overview
This framework defines API to configure managed deployments of your app for installation on multiple devices, using mobile device management (MDM). An administrator determines the configuration of, or manages, your app for a specific company, school, or government by creating unique configurations for people within an organization.

The framework works in conjunction with Device Management to provide streamlined and secure access to secrets and configuration. Secrets include passwords, certificates, and identities. Configuration includes general information, for example a server URL and its timeout in seconds.

Enabling managed secrets and configuration lets an MDM admin customize the behavior of your app. For example, an MDM admin could configure an app to skip first-time setup and launch ready to use, with a person already logged in, and their app preferences or job-specific information present.

### Use secrets to implement managed features

The server-provisioned secrets and configuration available in ManagedApp enable you to add the following kinds of common Device Management features to your app:

- Enforcing the role of a person
- Receiving identities provisioned by an administrator for authentication and signing
- Receiving API access tokens
- Acquiring certificates for custom trust, for example, pinning certificates
- Using hardware-bound keys and Managed Device Attestation for strong device authentication

### Provision your app or app extension

ManagedApp works with apps and app extensions. Any framework use that the documentation describes in an app also applies in app extensions.

An MDM admin can provision your app and each of its app extensions differently depending on their intended functions. For example, an MDM admin can provision your app's Packet tunnel provider extension using a VPN authentication identity that your app can't access, which enhances security.

You architect the unique provisioning requirements of your app and its app extensions and communicate the requirements to MDM admins, so they can prepare accordingly.

### Configuration changes and failures

The documented declarative-management path supplies `AppConfig` or `ExtensionConfigs` in an `AppManaged` declaration. Publish the supported schema, decode and validate it, and observe later updates rather than assuming the first configuration is permanent.

`configurations(_:)` yields `nil` when decoding fails. Use appropriate default behavior without granting privileges from invalid configuration, and keep observing for a corrected value. Decoding has a timeout; perform decoding work there rather than unrelated operations. Custom decoding errors may be reported to management and device logs, so their messages must not include secrets.

Secret identifiers are exposed as changing asynchronous sequences. Fetch a password, certificate, or identity when needed, handle `invalidIdentifier`, `serverError`, and `internalError`, and do not treat a failed lookup as an empty but valid credential. Avoid retaining or logging secret material unnecessarily; an app extension's provisioned identity need not be accessible to its containing app.

## Topics

### Configuration
- [Specifying and decoding a configuration](https://developer.apple.com/documentation/managedapp/specifying-and-decoding-a-configuration) - Publish a configuration specification and implement a decoder that parses and validates configuration provided by an MDM admin.
- **ManagedAppConfigurationProvider** - A class that provides configurations that an MDM admin provisions for a managed app or extension.
### Secrets and identifiers
- [Accessing provisioned secrets with identifiers](https://developer.apple.com/documentation/managedapp/accessing-provisioned-secrets-with-identifiers) - Specify the secrets your app requires for device management features, receive secrets from MDM servers and use secrets in your app.
- **ManagedAppCertificatesProvider** - A class that provides certificates that an MDM admin provisions for a managed app or extension.
- **ManagedAppIdentitiesProvider** - A class that provides identities that an MDM admin provisions for a managed app or extension.
- **ManagedAppPasswordsProvider** - A class that provides passwords that an MDM admin provisions for a managed app or extension.
### Errors
- **ManagedAppError** - Errors that functions in the ManagedApp framework can throw.
- **ManagedAppConfigurationDecodingError** - A protocol for an error that describes an issue with decoding the configuration.
- **ManagedAppConfigurationDecodingErrorCode** - A code for an error that occurs during configuration decoding.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ManagedApp)*
