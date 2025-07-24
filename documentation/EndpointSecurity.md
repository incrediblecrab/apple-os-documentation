# Endpoint Security

Develop system extensions that enhance user security.

**Platforms:** Mac Catalyst 13.0+ | macOS 10.15+

## Overview

Endpoint Security is a C API for monitoring system events for potentially malicious activity. You can write your client in any language that supports native calls. Your client registers with Endpoint Security to authorize pending events, or receive notifications of events that already occurred. These events include process executions, mounting file systems, forking processes, and raising signals.

Develop your system extension with Endpoint Security and package it in an app that uses the System Extensions framework to install and upgrade the extension on the user's Mac.

## Topics

### Event Monitoring
- **Client** - An opaque type that maintains Endpoint Security client state, and functions related to this type.
- **Message** - A type used by Endpoint Security to notify your client when a monitored action occurs.
- **Event Types** - Types used by messages to deliver details specific to different kinds of Endpoint Security events.
- [Monitoring System Events with Endpoint Security](https://developer.apple.com/documentation/endpointsecurity/monitoring-system-events-with-endpoint-security) - Receive notifications and authorization requests for sensitive operations by creating an Endpoint Security client for your app.

### Entitlements
- **com.apple.developer.endpoint-security.client** - The entitlement required to monitor system events for potentially malicious activity.

### Reference
- **EndpointSecurity Constants**
- **EndpointSecurity Data Types**
- **EndpointSecurity Functions**
- **EndpointSecurity Structures**
- **EndpointSecurity Enumerations**

### Structures
- **es_cs_validation_category_t**
- **es_cs_validation_category**
- **es_event_tcc_modify_t**
- **es_tcc_authorization_reason_t**
- **ess_tcc_authorization_reason_t**
- **es_tcc_authorization_right_t**
- **ess_tcc_authorization_right_t**
- **es_tcc_event_type_t**
- **es_tcc_identity_type_t**
- **es_tcc_identity_type_t**

### Variables
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
- `var ES_TCC_AUTHORIZATION_REASON_APP_TYPE_POLICY: es_tcc_authorization_reason_t` - A system process changed the authorization right
- `var ES_TCC_AUTHORIZATION_REASON_ENTITLED: es_tcc_authorization_reason_t` - A system process changed the authorization right
- `var ES_TCC_AUTHORIZATION_REASON_ERROR: es_tcc_authorization_reason_t`
- `var ES_TCC_AUTHORIZATION_REASON_MDM_POLICY: es_tcc_authorization_reason_t` - A system process changed the authorization right
- `var ES_TCC_AUTHORIZATION_REASON_MISSING_USAGE_STRING: es_tcc_authorization_reason_t` - A system process changed the authorization right
- `var ES_TCC_AUTHORIZATION_REASON_NONE: es_tcc_authorization_reason_t`
- `var ES_TCC_AUTHORIZATION_REASON_PREFLIGHT_UNKNOWN: es_tcc_authorization_reason_t` - A system process changed the authorization right
- `var ES_TCC_AUTHORIZATION_REASON_PROMPT_CANCEL: es_tcc_authorization_reason_t` - A system process changed the authorization right
- `var ES_TCC_AUTHORIZATION_REASON_PROMPT_TIMEOUT: es_tcc_authorization_reason_t` - A system process changed the authorization right
- `var ES_TCC_AUTHORIZATION_REASON_SERVICE_OVERRIDE_POLICY: es_tcc_authorization_reason_t` - A system process changed the authorization right
- `var ES_TCC_AUTHORIZATION_REASON_SERVICE_POLICY: es_tcc_authorization_reason_t` - A system process changed the authorization right
- `var ES_TCC_AUTHORIZATION_REASON_SYSTEM_SET: es_tcc_authorization_reason_t` - User changed the authorization right via Preferences
- `var ES_TCC_AUTHORIZATION_REASON_USER_CONSENT: es_tcc_authorization_reason_t`
- `var ES_TCC_AUTHORIZATION_REASON_USER_SET: es_tcc_authorization_reason_t` - User answered a prompt
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