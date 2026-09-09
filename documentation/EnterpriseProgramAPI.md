# Enterprise Program API

Automate the tasks you perform on the Apple Developer website.

## Overview

The Enterprise Program API automates developer-team provisioning and account administration through a REST interface. It has its own release cadence, rather than a device OS 27 minimum.

Calls require JSON Web Tokens signed using keys from your organization's Enterprise Program account. Follow [Creating API Keys](https://developer.apple.com/documentation/enterpriseprogramapi/creating-api-keys-for-enterprise-program-api) and [Generating Tokens](https://developer.apple.com/documentation/enterpriseprogramapi/generating-tokens-for-api-requests); keep the private key in your controlled server environment.

An Admin creates the API key and assigns its role. An Admin key can manage users; a Developer key is restricted to provisioning tasks. The JWT uses this service's `apple-developer-enterprise-v1` audience, not an App Store or organization-device-management token.

> **Important:** Changes you make using the Enterprise Program API affect the production data you use for development and distribution.

The API provides resources to automate the following areas of the Apple Developer website:

- **Provisioning.** Manage bundle IDs, capabilities, signing certificates, devices, and provisioning profiles.
- **Users and Roles.** Send invitations for users to join your team. Adjust their level of access or remove users.

The Enterprise Program API returns responses from resources that are consistent JSON data and contain links to additional related resources.

## Scope and failure handling

This service is distinct from [Apple School Manager and Apple Business APIs](AppleSchoolAndBusinessManagerAPI.md), which manage organization resources and device-management assignments. Do not reuse their OAuth scopes or infer Enterprise Program endpoints from similarly named resources.

Follow pagination links, inspect structured `ErrorResponse` details when present, and honor rate-limit responses. Not every failure includes a response body; retain the HTTP status as well. Repair authorization failures before retrying; key revocation or profile deletion can disrupt production distribution and should not be used as a generic recovery action. Review [service release notes](https://developer.apple.com/documentation/enterpriseprogramapi/enterprise-api-release-notes) separately from OS release notes.

## Topics

### Essentials
- [Creating API Keys for Enterprise Program API](https://developer.apple.com/documentation/enterpriseprogramapi/creating-api-keys-for-enterprise-program-api) - Create signing keys for authorized requests.
- [Generating Tokens for API Requests](https://developer.apple.com/documentation/enterpriseprogramapi/generating-tokens-for-api-requests) - Sign request JWTs.
- [Revoking API Keys](https://developer.apple.com/documentation/enterpriseprogramapi/revoking-api-keys) - Revoke unused, lost, or compromised keys.
- [Identifying Rate Limits](https://developer.apple.com/documentation/enterpriseprogramapi/identifying-rate-limits) - Recognize and handle rate limits.
- [Enterprise Program API Release Notes](https://developer.apple.com/documentation/enterpriseprogramapi/enterprise-api-release-notes) - Service changes.

### Provisioning
- [Bundle IDs](https://developer.apple.com/documentation/enterpriseprogramapi/bundle-ids) - Manage app identifiers.
- [Bundle ID Capabilities](https://developer.apple.com/documentation/enterpriseprogramapi/bundle-id-capabilities) - Manage capabilities for a bundle ID.
- [Certificates](https://developer.apple.com/documentation/enterpriseprogramapi/certificates) - Create, download, and revoke signing certificates for app development and distribution.
- [Devices](https://developer.apple.com/documentation/enterpriseprogramapi/devices) - Register devices for development and testing.
- [Pass Type Ids](https://developer.apple.com/documentation/enterpriseprogramapi/passtypeids) - Manage pass type identifiers.
- [Profiles](https://developer.apple.com/documentation/enterpriseprogramapi/profiles) - Create, delete, and download provisioning profiles for development and distribution.

### Users and Roles
- [Users](https://developer.apple.com/documentation/enterpriseprogramapi/users) - Manage users on your Enterprise Program team.
- [User Invitations](https://developer.apple.com/documentation/enterpriseprogramapi/user-invitations) - Email team invitations.

### Error Handling
- [Interpreting and Handling Errors](https://developer.apple.com/documentation/enterpriseprogramapi/interpreting-and-handling-errors) - Handle structured API errors.
- **ErrorResponse** - Structured details for an unsuccessful API request, when an error body is provided.

### Paging
- [Large Data Sets](https://developer.apple.com/documentation/enterpriseprogramapi/large-data-sets) - Retrieve paginated results.

### Dictionaries
- **JsonPointer** - An object that contains the JSON pointer that indicates the location of the error.
- **Parameter** - An object that contains the query parameter that produced the error.
- **RelationshipLinks** - The links to the related data and the relationship's self-link.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/EnterpriseProgramAPI)*
