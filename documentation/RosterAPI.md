# Roster API

Read information about people and classes from an Apple School Manager organization.

**Platforms:** Roster API 1.0.0+

## Overview

Roster API provides access to people and class information in Apple School Manager (ASM). Use this REST API if you need to support a workflow within your app to automatically create student or teacher records in advance of the first day of school. A typical use case is when your app requires teachers to input assignments and due dates for students in each class.

Accessing the user and class information requires authorization from an administrator of the ASM organization. When you begin the Roster API authorization flow, use the scopes defined below to request the appropriate level of access:

**edu.users.read**  
Request read access to ASM users

**edu.classes.read**  
Request read access to ASM classes

At the end of the authorization flow, use the access token you receive to access the Roster API endpoints, which you use to fetch people and class information. For more information on requesting an access token, see Generate and validate tokens.

Include the access token you receive in the Authorization header for every request. The Roster API associates the access token with an ASM organization. The endpoints return user and class information contained within that ASM organization. The unique account identifier from Sign in with Apple at Work & School is the same identifier provided in the Roster API user information. You may use this identifier to associate user information from the Roster API with a user signing in to your app.

## Topics

### Essentials
- [Obtaining information about people and classes](https://developer.apple.com/documentation/rosterapi/obtaining_information_about_people_and_classes) - Prepare your app to request organizational information from a server.
- [Validating with the Roster API test scope](https://developer.apple.com/documentation/rosterapi/validating_with_the_roster_api_test_scope) - Use test data to ensure your integration with the Roster API works correctly.

### Authentication
- [Integrating with Roster API and Sign in with Apple](https://developer.apple.com/documentation/rosterapi/integrating_with_roster_api_and_sign_in_with_apple) - Associate someone's Managed Apple ID with their identity in Apple School Manager.

### Information about users
- [Read a user](https://developer.apple.com/documentation/rosterapi/read_a_user) - Read a user in an Apple School Manager organization.
- **User** - A user in an Apple School Manager organization.
- **RoleLocation** - A mapping between a role assumed by a user in an Apple School Manager organization, and the corresponding location.
- [List users](https://developer.apple.com/documentation/rosterapi/list_users) - List users in an Apple School Manager organization.
- [List users in a class](https://developer.apple.com/documentation/rosterapi/list_users_in_a_class) - List users in a class of an Apple School Manager organization.
- **Users** - A list of users, with a token for pagination.

### Information about classes
- [Read a class](https://developer.apple.com/documentation/rosterapi/read_a_class) - Read a class from an Apple School Manager organization.
- **Class** - A class in an Apple School Manager organization.
- [List classes](https://developer.apple.com/documentation/rosterapi/list_classes) - List classes in an Apple School Manager organization.
- **Classes** - A list of classes, with a token for pagination.

### Information about locations
- [Read a location](https://developer.apple.com/documentation/rosterapi/read_a_location) - Returns a specific location in an Apple School Manager organization.
- **Location** - A location in an Apple School Manager organization.
- [List locations](https://developer.apple.com/documentation/rosterapi/list_locations) - Returns a list of locations in an Apple School Manager organization.
- **Locations** - A list of locations, with a token for pagination.

### Information about the organization
- [Read the organization](https://developer.apple.com/documentation/rosterapi/read_the_organization) - Returns information about the Apple School Manager organization.
- **Organization** - Information about an Apple School Manager organization.
- **Domain** - A DNS domain name associated with an Apple School Manager organization.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/RosterAPI)*