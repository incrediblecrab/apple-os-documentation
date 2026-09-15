# Device Management

Manage your organization's devices remotely.

**Platform/service catalog baselines:** iOS 13.0+ | iPadOS 13.0+ | macOS 10.15+ | tvOS 13.0+ | visionOS 1.1+ | watchOS 6.0+ | Device Assignment Services 5.0+ | VPP License Management 1.0+

These umbrella catalog values are not universal MDM-protocol introduction dates. Check each command, payload, or declaration for its actual device and enrollment requirements; service API version numbers are not operating-system versions.

## Overview

A mobile device management (MDM) service remotely configures enrolled devices using commands, configuration profiles, and declarative management. Organization-owned and personally owned devices have different enrollment options. Enrollment mode, supervision, device channel, access rights, and OS version determine which settings, software updates, content installations, lock operations, or erase operations are permitted.

For example, the [Erase Device command](https://developer.apple.com/documentation/devicemanagement/erase-device-command) is device-channel-only, is unavailable with User Enrollment, requires `AllowDeviceErase`, and lists supervision as a macOS requirement. Enrollment alone does not give every administrator an unrestricted erase capability.

For traditional commands, an APNs notification prompts the device to contact the service for pending work; the device executes a command and reports its result. Declarative management instead lets devices apply synchronized declarations and report subscribed status changes. It can coexist with traditional MDM, but must first be enabled for the applicable enrollment channel.

MDM also works with [Managed App Distribution](ManagedAppDistribution.md) for managed app delivery and [ManagedApp](ManagedApp.md) for managed configuration and secrets. Apps, books, and subscriptions have their own content-management service APIs.

### OS 27: audit management-server TLS

**Reviewed September 8, 2026:** The 27 operating systems enforce stricter TLS requirements for selected processes handling MDM, DDM, Automated Device Enrollment, profile installation, app installation, and software updates. This includes enterprise app distribution; it does not apply indiscriminately to all traffic from managed apps.

Affected servers need **TLS 1.2 or later**, ATS-compliant ciphers, and valid ATS-compliant certificates. Apple's [deployment guidance](https://support.apple.com/en-us/126655) also specifies the stricter TLS 1.2 requirements, including ECDHE, AES-GCM, and Extended Master Secret. Prefer TLS 1.3 where supported.

Audit each environment, enrollment type, device role, and server involved in these workflows. Use the Network Diagnostics Logging Profile and representative 26.4-or-later devices to find warnings, then verify 27 devices where noncompliant connections are blocked. The documented `nscurl --ats-diagnostics` check includes an `FCP_v2.1` result for endpoint retesting.

The change excludes SCEP-server connections during profile installation or DDM-asset resolution, and content-caching-server connections. Fix failures with the relevant server or MDM vendor; changing an app's ATS exceptions is not a general repair for system management processes. See [Security](Security.md) for policy scope and certificate requirements.

## Topics

### Configuration Profiles
- [Configuring Multiple Devices Using Profiles](https://developer.apple.com/documentation/devicemanagement/configuring-multiple-devices-using-profiles) - Create and deploy configuration profiles to users within your organization.
- [Profile-Specific Payload Keys](https://developer.apple.com/documentation/devicemanagement/profile-specific-payload-keys) - Use the appropriate payload for your configuration needs.

### MDM Protocol
- [Device management essentials](https://developer.apple.com/documentation/devicemanagement/device-management-essentials) - Configure service connections, certificates, push notifications, and command handling.
- [Commands and Queries](https://developer.apple.com/documentation/devicemanagement/commands-and-queries) - Manage the configuration and behavior of your devices.
- [Check-in](https://developer.apple.com/documentation/devicemanagement/check-in) - Authenticate devices and maintain push tokens with these commands.
- [Onboarding users with account-driven enrollment](https://developer.apple.com/documentation/devicemanagement/onboarding-users-with-account-driven-enrollment) - Authenticate the person and authorize enrollment using identity-focused flows; access-token expiry or revocation can require renewed authentication.

### Declarative Management
- [Leveraging the declarative management data model to scale devices](https://developer.apple.com/documentation/devicemanagement/leveraging-the-declarative-management-data-model-to-scale-devices) - Describe configurations, assets, activations, management metadata, status, and advertised capabilities.
- [Integrating Declarative Management](https://developer.apple.com/documentation/devicemanagement/integrating-declarative-management) - Enable declarations and status alongside MDM, synchronize changes, and validate downloaded asset data; this is not a replacement enrollment protocol.
- [Declarations](https://developer.apple.com/documentation/devicemanagement/devicemanagement-declarations) - The available declarations for device management.
- [Status items](https://developer.apple.com/documentation/devicemanagement/status-items) - Device state available through declarative status reporting.

### Deployment Services
- [Device Assignment](https://developer.apple.com/documentation/devicemanagement/device-assignment) - Manage devices for your students and employees.
- [Roster Management](https://developer.apple.com/documentation/devicemanagement/roster-management) - Manage classes for your students and teachers.
- [App, Book, and Subscription Management](https://developer.apple.com/documentation/devicemanagement/app-book-and-subscription-management) - Manage organizational content licenses and assignments.

### Content Catalog Endpoints
- [Fetch an app resource's relationship](https://developer.apple.com/documentation/devicemanagement/fetch-a-apps-resource's-relationship)
- [Fetch a book resource's relationship](https://developer.apple.com/documentation/devicemanagement/fetch-a-books-resource's-relationship)
- [Get Multiple Genres](https://developer.apple.com/documentation/devicemanagement/get-multiple-genres) - Fetch metadata for genres from the content catalog by using their identifiers.
- [Get a Genre](https://developer.apple.com/documentation/devicemanagement/get-a-genre) - Fetch metadata for a genre from the content catalog by using its identifier.

### Enrollment Error Dictionaries
- [ErrorUnrecognizedDevice](https://developer.apple.com/documentation/devicemanagement/errorunrecognizeddevice) - A `403` response body for an unrecognized device that causes unenrollment; do not use a `401` response for that purpose.
- [ErrorWellKnownFailed](https://developer.apple.com/documentation/devicemanagement/errorwellknownfailed) - A `403` response body rejecting an account-driven enrollment service-discovery request.

### Dictionaries
- **ErrorCodePlatformSSORequired** - An error response that indicates Platform SSO is required.
- **ManifestURL** - The URL to the app manifest.
- **PasswordHash** - A dictionary that contains the password hash for the account.
- **RelationshipResponse**
- **ResponseErrorCode** - An error code.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/DeviceManagement)*

*27 sources: [network-environment preparation](https://support.apple.com/en-us/126655) and [iOS/iPadOS release notes — Network Security](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes.md).*
