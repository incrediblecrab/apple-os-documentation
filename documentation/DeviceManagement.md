# Device Management

Manage your organization's devices remotely.

**Platforms:** iOS 13.0+ | iPadOS 13.0+ | macOS 10.15+ | tvOS 13.0+ | visionOS 1.1+ | watchOS 6.0+ | Device Assignment Services 5.0+ | VPP License Management 1.0+

## Overview

Deploying a mobile device management (MDM) solution allows administrators to securely and remotely configure enrolled devices. Administrators use Apple School Manager or Apple Business Manager to enroll organization-owned devices, and users can enroll their own devices. Once a device is enrolled, administrators can update software and device settings, monitor compliance with organizational policies, remotely erase or lock devices, and install apps and books developed in-house or purchased through Apple School Manager or Apple Business Manager.

MDM works with Managed App Distribution to provide a great download and launch experience. For more information, see Managed App Distribution.

## Topics

### Configuration Profiles
- [Configuring Multiple Devices Using Profiles](https://developer.apple.com/documentation/devicemanagement/configuring_multiple_devices_using_profiles) - Create and deploy configuration profiles to users within your organization.
- [Profile-Specific Payload Keys](https://developer.apple.com/documentation/devicemanagement/profile-specific_payload_keys) - Use the appropriate payload for your configuration needs.

### MDM Protocol
- [Implementing Device Management](https://developer.apple.com/documentation/devicemanagement/implementing_device_management) - Set up an MDM server and send commands to managed devices.
- [Commands and Queries](https://developer.apple.com/documentation/devicemanagement/commands_and_queries) - Manage the configuration and behavior of your devices.
- [Check-in](https://developer.apple.com/documentation/devicemanagement/check-in) - Authenticate devices and maintain push tokens with these commands.
- [Account-driven enrollment](https://developer.apple.com/documentation/devicemanagement/account-driven_enrollment) - Authenticate devices using a user identity-focused workflow.

### Declarative Management
- [Leveraging the declarative management data model to scale devices](https://developer.apple.com/documentation/devicemanagement/leveraging_the_declarative_management_data_model_to_scale_devices) - Use declarative management to make devices more autonomous and proactive.
- [Integrating Declarative Management](https://developer.apple.com/documentation/devicemanagement/integrating_declarative_management) - Use the declarative management protocol to manage MDM features such as device enrollment and un-enrollment and device and user authentication.
- [Declarations](https://developer.apple.com/documentation/devicemanagement/declarations) - The available declarations for device management.
- [Status Reports](https://developer.apple.com/documentation/devicemanagement/status_reports) - Reports from the device about its current state.

### Deployment Services
- [Device Assignment](https://developer.apple.com/documentation/devicemanagement/device_assignment) - Manage devices for your students and employees.
- [Roster Management](https://developer.apple.com/documentation/devicemanagement/roster_management) - Manage classes for your students and teachers.
- [App and Book Management](https://developer.apple.com/documentation/devicemanagement/app_and_book_management) - Manage apps and books for your students and employees.

### Endpoints
- **Fetch a apps resource's relationship**
- **Fetch a books resource's relationship**
- [Get Multiple Genres](https://developer.apple.com/documentation/devicemanagement/get_multiple_genres) - Fetch metadata for genres from the catalog by using their identifiers.
- [Get a Genre](https://developer.apple.com/documentation/devicemanagement/get_a_genre) - Fetch metadata for a genre from the catalog by using its identifier.

### Objects
- **ErrorUnrecognizedDevice**
- **ErrorWellKnownFailed**

### Dictionaries
- **ErrorCodePlatformSSORequired** - An error response that indicates Platform SSO is required.
- **ManifestURL** - The URL to the app manifest.
- **PasswordHash** - A dictionary that contains the password hash for the account.
- **RelationshipResponse**
- **ResponseErrorCode** - An error code.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/DeviceManagement)*