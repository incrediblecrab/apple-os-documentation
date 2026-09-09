# Roster API

Read information about people and classes from an Apple School Manager organization.

**Service version:** Roster API 1.0.0+. No Apple OS or compiler baseline is implied.

## Overview

Roster API reads people and class information from Apple School Manager (ASM). Use the results to populate student and teacher records in your own app, such as the roster for an assignment workflow; these read operations do not create accounts or classes in ASM.

An ASM administrator or site manager must authorize the integration. Configure Account & Organizational Data Sharing for your primary App ID, return URLs, key, and notification endpoint as described in [Obtaining information about people and classes](https://developer.apple.com/documentation/rosterapi/obtaining-information-about-people-and-classes). Request only the production scopes you need:

**edu.users.read**  
Request read access to ASM users

**edu.classes.read**  
Request read access to ASM classes

Use the resulting access token for Roster requests. The [Roster token/test flow](https://developer.apple.com/documentation/rosterapi/validating-with-the-roster-api-test-scope) documents the one-hour access-token lifetime and refresh-token flow. The separate `edu.rosterapi.test.read` scope returns synthetic records; it is not production organization access.

Include the access token in each request's `Authorization` header. Access is organization-scoped. When associating a Sign in with Apple identity with a roster, compare its `org_id` with the authorized organization's ID before using `sub` as the Roster user identifier, following the [identity-integration guide](https://developer.apple.com/documentation/rosterapi/integrating-with-roster-api-and-sign-in-with-apple).

Handle authorization expiry separately from roster changes. Apple's integration guide requires removing an organization's associated data after receiving its consent-revocation notification; track the organization ID so this does not affect another tenant's records.

## Topics

### Essentials
- [Obtaining information about people and classes](https://developer.apple.com/documentation/rosterapi/obtaining-information-about-people-and-classes) - Prepare your app to request organizational information from a server.
- [Validating with the Roster API test scope](https://developer.apple.com/documentation/rosterapi/validating-with-the-roster-api-test-scope) - Use test data to ensure your integration with the Roster API works correctly.

### Authentication
- [Integrating with Roster API and Sign in with Apple](https://developer.apple.com/documentation/rosterapi/integrating-with-roster-api-and-sign-in-with-apple) - Associate a Managed Apple Account with its identity in an authorized Apple School Manager organization.

### Information about users
- [Read a user](https://developer.apple.com/documentation/rosterapi/returns-a-specific-user-in-an-apple-school-manager-organization) - Read a user in an Apple School Manager organization.
- **User** - A user in an Apple School Manager organization.
- **RoleLocation** - A mapping between a role assumed by a user in an Apple School Manager organization, and the corresponding location.
- [List users](https://developer.apple.com/documentation/rosterapi/returns-a-list-of-users-in-an-apple-school-manager-organization) - List users in an Apple School Manager organization.
- [List users in a class](https://developer.apple.com/documentation/rosterapi/returns-a-users-for-an-apple-school-manager-class) - List users in a class of an Apple School Manager organization.
- **Users** - A list of users, with a token for pagination.

### Information about classes
- [Read a class](https://developer.apple.com/documentation/rosterapi/returns-a-specific-class-in-an-apple-school-manager-organization.) - Read a class from an Apple School Manager organization.
- **Class** - A class in an Apple School Manager organization.
- [List classes](https://developer.apple.com/documentation/rosterapi/returns-a-list-of-classes-for-an-apple-school-manager-organization) - List classes in an Apple School Manager organization.
- **Classes** - A list of classes, with a token for pagination.

### Information about locations
- [Read a location](https://developer.apple.com/documentation/rosterapi/returns-a-specific-location-in-an-apple-school-manager-organization) - Returns a specific location in an Apple School Manager organization.
- **Location** - A location in an Apple School Manager organization.
- [List locations](https://developer.apple.com/documentation/rosterapi/returns-a-list-of-locations-for-an-apple-school-manager-organization) - Returns a list of locations in an Apple School Manager organization.
- **Locations** - A list of locations, with a token for pagination.

### Information about the organization
- [Read the organization](https://developer.apple.com/documentation/rosterapi/returns-organization-infrmation) - Returns information about the Apple School Manager organization.
- **Organization** - Information about an Apple School Manager organization.
- **Domain** - A DNS domain name associated with an Apple School Manager organization.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/RosterAPI)*
