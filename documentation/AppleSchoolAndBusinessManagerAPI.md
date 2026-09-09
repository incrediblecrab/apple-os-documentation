# Apple School Manager and Apple Business APIs

Automate organization device inventory, management assignments, and supported Apple Business administration.

**Availability:** Server-to-server APIs for authorized Apple School Manager and Apple Business organizations, not an OS 27 framework. The service changelog includes releases from 2025. As of September 8, 2026, it lists Apple Business 2.4 and Apple School Manager 1.6.

## Overview

Use this collection to discover devices enrolled through Automated Device Enrollment, inspect their assigned device management service, and request supported management changes. Apple Business additionally exposes resources for users, groups, organizational units, configurations, and Blueprints. Do not assume the two services have identical resources or permissions.

These APIs manage organization resources. They are distinct from the [Enterprise Program API](EnterpriseProgramAPI.md), which manages developer-team provisioning, and the [Roster API](RosterAPI.md), which supplies authorized education roster data.

## Prerequisites and authorization

1. Have an Apple School Manager **Administrator** or Apple Business **Organization Administrator** create an API account.
2. Follow [Implementing OAuth](https://developer.apple.com/documentation/apple-school-and-business-manager-api/implementing-oauth-for-the-apple-school-manager-and-apple-business-api). Sign the client assertion with the account's private key; keep that key on your server.
3. Request an access token using the client-credentials flow and the appropriate `school.api` or `business.api` scope. Use the returned bearer token for API requests.
4. Renew the access token according to `expires_in`; Apple's documented lifetime is one hour. On `401`, refresh authorization rather than repeatedly submitting the same expired token.

Use the authorization guide's current token endpoint and claim definitions; these credentials are not App Store Connect API keys.

## Topics and workflow

| Task | Primary reference | Implementation consideration |
|---|---|---|
| School device inventory | [Get Org Devices](https://developer.apple.com/documentation/appleschoolmanagerapi/get-org-devices) | Follow response paging links rather than assuming one response contains the organization. |
| Business device inventory | [Get Org Devices](https://developer.apple.com/documentation/applebusinessapi/get-org-devices) | Keep organization and device identifiers associated with the account that supplied them. |
| Assign or migrate school devices | [Create an OrgDeviceActivity](https://developer.apple.com/documentation/appleschoolmanagerapi/create-an-orgdeviceactivity) | Submit only supported activity types and inspect the resulting activity. |
| Assign, migrate, or release business devices | [Create an OrgDeviceActivity](https://developer.apple.com/documentation/applebusinessapi/create-an-orgdeviceactivity) | Treat release as a separate administrative operation, not an ordinary reassignment. |
| Track a requested change | [Get OrgDeviceActivity Information](https://developer.apple.com/documentation/applebusinessapi/get-orgdeviceactivity-information) | Receiving an activity resource is not proof that every device has completed the change. |
| Business administration | [Apple Business API](https://developer.apple.com/documentation/applebusinessapi) | Consult the specific users, user groups, Blueprints, and configurations operations before choosing a write workflow. |
| Error and paging models | [School API resources](https://developer.apple.com/documentation/appleschoolmanagerapi) | Parse `ErrorResponse`, `PagedDocumentLinks`, and `PagingInformation` instead of discarding response bodies. |

## Changes reviewed through September 8, 2026

- The August 12 service releases add device management migration activities and the read-only device fields `isMdmMigrationCapable`, `mdmMigrationStatus`, and `mdmMigrationDeadlineDateTime`. Check device capability and activity status; an organization-level API release does not make every enrolled device migration-capable.
- Apple Business 2.4, released August 26, adds device release through `Create an OrgDeviceActivity`. This addition is not documented as an equivalent Apple School Manager release.
- The OS 27 release notes separately require stricter TLS for selected managed-device system processes, including Automated Device Enrollment. Audit the management infrastructure against those requirements; do not describe that client-network change as a new version of these REST APIs.

## Failure handling

Retain structured error details and the affected resource identifiers for administrative diagnosis, without logging keys or tokens. Separate authorization failures from invalid activity requests. For a timeout during a management change, inspect the activity and current assignment before resubmitting a potentially destructive operation. Use bounded retries for transient failures and respect any server-provided retry instructions.

## Sources

- [Apple School Manager and Apple Business APIs](https://developer.apple.com/documentation/apple-school-and-business-manager-api)
- [OAuth authorization](https://developer.apple.com/documentation/apple-school-and-business-manager-api/implementing-oauth-for-the-apple-school-manager-and-apple-business-api)
- [Service changelog](https://developer.apple.com/documentation/apple-school-and-business-manager-api/apple-school-manager-and-apple-business-api-changelog)
- [Apple School Manager API](https://developer.apple.com/documentation/appleschoolmanagerapi)
- [Apple Business API](https://developer.apple.com/documentation/applebusinessapi)
- [iOS and iPadOS 27 release notes — Network Security](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
