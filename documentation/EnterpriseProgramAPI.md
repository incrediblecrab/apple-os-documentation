# Enterprise Program API

Automate the tasks you perform on the Apple Developer website.

## Overview

The Enterprise Program API is a REST API that enables the automation of actions you take on the Apple Developer website. Click OpenAPI specification to download the specification file.

Calls to the API require JSON Web Tokens (JWT) for authorization; you obtain keys to create the tokens from your organization's Enterprise Program account. See Creating API Keys for Enterprise Program API to create your keys and tokens.

> **Important:** Changes you make using the Enterprise Program API affect the production data you use for development and distribution.

The API provides resources to automate the following areas of the Apple Developer website:

- **Provisioning.** Manage bundle IDs, capabilities, signing certificates, devices, and provisioning profiles.
- **Users and Roles.** Send invitations for users to join your team. Adjust their level of access or remove users.

The Enterprise Program API returns responses from resources that are consistent JSON data and contain links to additional related resources.

## Topics

### Essentials
- [Creating API Keys for Enterprise Program API](https://developer.apple.com/documentation/enterpriseprogramapi/creating_api_keys_for_enterprise_program_api) - Create API keys to sign JSON Web Tokens (JWTs) and authorize API requests.
- [Generating Tokens for API Requests](https://developer.apple.com/documentation/enterpriseprogramapi/generating_tokens_for_api_requests) - Create JSON Web Tokens (JWTs) signed with your private key to authorize API requests.
- [Revoking API Keys](https://developer.apple.com/documentation/enterpriseprogramapi/revoking_api_keys) - Revoke unused, lost, or compromised private keys.
- [Identifying Rate Limits](https://developer.apple.com/documentation/enterpriseprogramapi/identifying_rate_limits) - Recognize the rate limits that REST API responses provide and handle them in your code.
- [Enterprise Program API Release Notes](https://developer.apple.com/documentation/enterpriseprogramapi/enterprise_program_api_release_notes) - Learn about new features and updates in the Enterprise Program API.

### Provisioning
- [Bundle IDs](https://developer.apple.com/documentation/enterpriseprogramapi/bundle_ids) - Manage the bundle IDs that uniquely identify your apps.
- [Bundle ID Capabilities](https://developer.apple.com/documentation/enterpriseprogramapi/bundle_id_capabilities) - Manage the app capabilities for a bundle ID.
- [Certificates](https://developer.apple.com/documentation/enterpriseprogramapi/certificates) - Create, download, and revoke signing certificates for app development and distribution.
- [Devices](https://developer.apple.com/documentation/enterpriseprogramapi/devices) - Register devices for development and testing.
- [Pass Type Ids](https://developer.apple.com/documentation/enterpriseprogramapi/pass_type_ids) - Create, download, and revoke pass type ids for app development and distribution.
- [Profiles](https://developer.apple.com/documentation/enterpriseprogramapi/profiles) - Create, delete, and download provisioning profiles for development and distribution.

### Users and Roles
- [Users](https://developer.apple.com/documentation/enterpriseprogramapi/users) - Manage users on your Enterprise Program team.
- [User Invitations](https://developer.apple.com/documentation/enterpriseprogramapi/user_invitations) - Email invitations to join your Enterprise Program team.

### Error Handling
- [Interpreting and Handling Errors](https://developer.apple.com/documentation/enterpriseprogramapi/interpreting_and_handling_errors) - Learn how the Enterprise Program API returns errors and handle them in your code.
- **ErrorResponse** - The error details that an API returns in the response body whenever the API request isn't successful.

### Paging
- [Large Data Sets](https://developer.apple.com/documentation/enterpriseprogramapi/large_data_sets) - Retrieve large data sets with paging information.

### Dictionaries
- **JsonPointer** - An object that contains the JSON pointer that indicates the location of the error.
- **Parameter** - An object that contains the query parameter that produced the error.
- **RelationshipLinks** - The links to the related data and the relationship's self-link.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/EnterpriseProgramAPI)*