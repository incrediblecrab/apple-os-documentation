# Endpoint Security

Develop system extensions that enhance user security.

**Platforms:** macOS 10.15+

**Platform qualification:** Apple's root catalog also lists Mac Catalyst, but `es_new_client` is explicitly unavailable to Catalyst in the public macOS 26.5 SDK, confirmed by a compiler check. This page describes native macOS clients, not a supported Catalyst monitoring workflow.

## Overview

Endpoint Security is a C API for monitoring system events for potentially malicious activity. You can write your client in any language that supports native calls. Your client registers with Endpoint Security to authorize pending events, or receive notifications of events that already occurred. These events include process executions, mounting file systems, forking processes, and raising signals.

Develop your system extension with Endpoint Security and package it in an app that uses the System Extensions framework to install and upgrade the extension on the user's Mac.

### Authorization and connection failures

Creating a client requires Apple's grant of Boolean [`com.apple.developer.endpoint-security.client`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.endpoint-security.client), enabled in the signed client, **root privilege**, and TCC approval through Full Disk Access. These are separate requirements; the entitlement does not replace the other two.

Check the result of [`es_new_client(_:_:)`](https://developer.apple.com/documentation/endpointsecurity/es_new_client(_:_:)) before subscribing or using the client. The result distinguishes missing entitlement, lack of permission, insufficient privilege, invalid arguments, internal failure, and too many clients. Do not report monitoring as active after a failed connection or when the required permission is no longer available.

The supported Full Disk Access check is the result of `es_new_client`, including `ES_NEW_CLIENT_RESULT_ERR_NOT_PERMITTED`; do not infer it from entitlement presence or unrelated file-access probes. `ES_NEW_CLIENT_RESULT_ERR_NOT_PRIVILEGED` specifically means the caller is not running as root.

### Messages, deadlines, and API generations

Callbacks are delivered serially **per client**. A borrowed message is valid only for the callback's lifetime. For asynchronous processing on macOS 11+, retain it with `es_retain_message` and balance that with `es_release_message`; do not free or manually copy the borrowed structure. The older `es_copy_message`/`es_free_message` pair is a 10.15 compatibility path deprecated in 11, not the preferred current API.

Reply to each `AUTH` event before that message's Mach-absolute-time deadline. Deadlines vary; missing one causes the client to be killed. `NOTIFY` events report occurrences and are not authorization requests. Keep processing bounded, and do not assume that removing default muting of critical system processes is safe.

Check a message's `version` before accessing version-gated fields. Event availability also varies: `ES_EVENT_TYPE_NOTIFY_TCC_MODIFY` begins in **macOS 15.4**, not the framework's 10.15 baseline. Its values describe TCC record changes; they are not APIs for granting privacy permissions.

Release the client with `es_delete_client` on the **same thread that created it**, checking the shutdown result. A remembered permission or client pointer is not permanent authorization.

## Topics

### Event Monitoring
- **Client** - An opaque type that maintains Endpoint Security client state, and functions related to this type.
- **Message** - A type used by Endpoint Security to notify your client when a monitored action occurs.
- **Event Types** - Types used by messages to deliver details specific to different kinds of Endpoint Security events.
- [Monitoring System Events with Endpoint Security](https://developer.apple.com/documentation/endpointsecurity/monitoring-system-events-with-endpoint-security) - A macOS 11+ sample configured for either notification or authorization handling; its minimum differs from the framework's 10.15 baseline.

### Entitlements
- **com.apple.developer.endpoint-security.client** - The entitlement required to monitor system events for potentially malicious activity.

### Reference
- **EndpointSecurity Constants**
- **EndpointSecurity Data Types**
- **EndpointSecurity Functions**
- **EndpointSecurity Structures**
- **EndpointSecurity Enumerations**

### Event and classification types
- **es_cs_validation_category_t**
- **es_event_tcc_modify_t**
- **es_tcc_authorization_reason_t**
- **es_tcc_authorization_right_t**
- **es_tcc_event_type_t**
- **es_tcc_identity_type_t**

### Variables

Imported C enumeration constants, shown with their Swift declaration types:

- `var ES_CS_VALIDATION_CATEGORY_APP_STORE: es_cs_validation_category_t`
- `var ES_CS_VALIDATION_CATEGORY_DEVELOPER_ID: es_cs_validation_category_t`
- `var ES_CS_VALIDATION_CATEGORY_DEVELOPMENT: es_cs_validation_category_t`
- `var ES_CS_VALIDATION_CATEGORY_ENTERPRISE: es_cs_validation_category_t`
- `var ES_CS_VALIDATION_CATEGORY_INVALID: es_cs_validation_category_t`
- `var ES_CS_VALIDATION_CATEGORY_LOCAL_SIGNING: es_cs_validation_category_t`
- `var ES_CS_VALIDATION_CATEGORY_NONE: es_cs_validation_category_t`
- `var ES_CS_VALIDATION_CATEGORY_OOPJIT: es_cs_validation_category_t`
- `var ES_CS_VALIDATION_CATEGORY_PLATFORM: es_cs_validation_category_t`
- `var ES_CS_VALIDATION_CATEGORY_ROSETTA: es_cs_validation_category_t`
- `var ES_CS_VALIDATION_CATEGORY_TESTFLIGHT: es_cs_validation_category_t`
- `var ES_EVENT_TYPE_NOTIFY_TCC_MODIFY: es_event_type_t`
- `var ES_TCC_AUTHORIZATION_REASON_APP_TYPE_POLICY: es_tcc_authorization_reason_t`
- `var ES_TCC_AUTHORIZATION_REASON_ENTITLED: es_tcc_authorization_reason_t`
- `var ES_TCC_AUTHORIZATION_REASON_ERROR: es_tcc_authorization_reason_t`
- `var ES_TCC_AUTHORIZATION_REASON_MDM_POLICY: es_tcc_authorization_reason_t`
- `var ES_TCC_AUTHORIZATION_REASON_MISSING_USAGE_STRING: es_tcc_authorization_reason_t`
- `var ES_TCC_AUTHORIZATION_REASON_NONE: es_tcc_authorization_reason_t`
- `var ES_TCC_AUTHORIZATION_REASON_PREFLIGHT_UNKNOWN: es_tcc_authorization_reason_t`
- `var ES_TCC_AUTHORIZATION_REASON_PROMPT_CANCEL: es_tcc_authorization_reason_t`
- `var ES_TCC_AUTHORIZATION_REASON_PROMPT_TIMEOUT: es_tcc_authorization_reason_t`
- `var ES_TCC_AUTHORIZATION_REASON_SERVICE_OVERRIDE_POLICY: es_tcc_authorization_reason_t`
- `var ES_TCC_AUTHORIZATION_REASON_SERVICE_POLICY: es_tcc_authorization_reason_t`
- `var ES_TCC_AUTHORIZATION_REASON_SYSTEM_SET: es_tcc_authorization_reason_t` - A system process changed the authorization right.
- `var ES_TCC_AUTHORIZATION_REASON_USER_CONSENT: es_tcc_authorization_reason_t` - The person answered an authorization prompt.
- `var ES_TCC_AUTHORIZATION_REASON_USER_SET: es_tcc_authorization_reason_t` - The person changed the authorization right in settings.
- `var ES_TCC_AUTHORIZATION_RIGHT_ADD_MODIFY_ADDED: es_tcc_authorization_right_t`
- `var ES_TCC_AUTHORIZATION_RIGHT_ALLOWED: es_tcc_authorization_right_t`
- `var ES_TCC_AUTHORIZATION_RIGHT_DENIED: es_tcc_authorization_right_t`
- `var ES_TCC_AUTHORIZATION_RIGHT_LEARN_MORE: es_tcc_authorization_right_t`
- `var ES_TCC_AUTHORIZATION_RIGHT_LIMITED: es_tcc_authorization_right_t`
- `var ES_TCC_AUTHORIZATION_RIGHT_SESSION_PID: es_tcc_authorization_right_t`
- `var ES_TCC_AUTHORIZATION_RIGHT_UNKNOWN: es_tcc_authorization_right_t`
- `var ES_TCC_EVENT_TYPE_CREATE: es_tcc_event_type_t`
- `var ES_TCC_EVENT_TYPE_DELETE: es_tcc_event_type_t`
- `var ES_TCC_EVENT_TYPE_MODIFY: es_tcc_event_type_t`
- `var ES_TCC_EVENT_TYPE_UNKNOWN: es_tcc_event_type_t`
- `var ES_TCC_IDENTITY_TYPE_BUNDLE_ID: es_tcc_identity_type_t`
- `var ES_TCC_IDENTITY_TYPE_EXECUTABLE_PATH: es_tcc_identity_type_t`
- `var ES_TCC_IDENTITY_TYPE_FILE_PROVIDER_DOMAIN_ID: es_tcc_identity_type_t`
- `var ES_TCC_IDENTITY_TYPE_POLICY_ID: es_tcc_identity_type_t`

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/EndpointSecurity)*

*Changed-content sources, reviewed September 8, 2026: [client creation and Full Disk Access](https://developer.apple.com/documentation/endpointsecurity/es_new_client(_:_:).md) and [client result codes](https://developer.apple.com/documentation/endpointsecurity/es_new_client_result_t.md).*
