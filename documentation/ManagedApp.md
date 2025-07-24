# ManagedApp

Customize your app for managed deployments by providing configurable features that rely on secure access to secrets and data that an administrator provisions.

**Platforms:** iOS 18.4+ | iPadOS 18.4+ | visionOS 2.4+

## Overview
This framework defines API to configure managed deployments of your app for installation on multiple devices, using mobile device management (MDM). An administrator determines the configuration of, or manages, your app for a specific company, school, or government by creating unique configurations for people within an organization.

The framework works in conjunction with Device Management to provide streamlined and secure access to secrets and configuration. Secrets include passwords, certificates, and identities. Configuration includes general information, for example a server URL and its timeout in seconds.

Enabling managed secrets and configuration lets an MDM admin customize the behavior of your app. For example, an MDM admin could configure an app to skip first-time setup and launch ready to use, with a person already logged in, and their app preferences or job-specific information present.

Two iPhone renderings side by side. A device on the left features the label Unmanaged App, and a device on the right features the label Managed app. A header for the unmanaged app reads Company Name. A login prompt resides in the center of the unmanaged app’s screen with two empty text fields that read username and password respectively. A callout extends from the empty fields that reads Login required. The managed app features a header that reads Company Name and a tabbed layout. The first tab reads Dashboard and is the selected tab. The second tab reads Sales. A callout extends from the Sales tab that reads Access-control roles automatically setup. A profile area resides in the tabbed pane that features an avatar next to the name Juan Chavez. A callout extends from the profile area that reads Automatically logged in. The tabbed pane also contains a settings area and features several sliders. Some of the sliders are switched on and some are off. A callout extends from the settings pane that reads Preconfigured. A final additional area within the tabbed pane has a title that reads To Do, which contains gray rectangles representing text. A callout extends from the rectangles that reads Info loaded immediately.

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

## Topics

### Configuration
- [Specifying and decoding a configuration](https://developer.apple.com/documentation/managedapp/specifying_and_decoding_a_configuration) - Publish a configuration specification and implement a decoder that parses and validates configuration provided by an MDM admin.
- **ManagedAppConfigurationProvider** - A class that provides configurations that an MDM admin provisions for a managed app or extension.
### Secrets and identifiers
- [Accessing provisioned secrets with identifiers](https://developer.apple.com/documentation/managedapp/accessing_provisioned_secrets_with_identifiers) - Specify the secrets your app requires for device management features, receive secrets from MDM servers and use secrets in your app.
- **ManagedAppCertificatesProvider** - A class that provides certificates that an MDM admin provisions for a managed app or extension.
- **ManagedAppIdentitiesProvider** - A class that provides identities that an MDM admin provisions for a managed app or extension.
- **ManagedAppPasswordsProvider** - A class that provides passwords that an MDM admin provisions for a managed app or extension.
### Errors
- **ManagedAppError** - Errors that functions in the ManagedApp framework can throw.
- **ManagedAppConfigurationDecodingError** - A protocol for an error that describes an issue with decoding the configuration.
- **ManagedAppConfigurationDecodingErrorCode** - A code for an error that occurs during configuration decoding.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ManagedApp)*
