# App Store Server API

Retrieve signed App Store purchase information and manage supported transaction and subscription operations from your server.

**Availability:** An existing server-to-server REST service with its own release cadence; it has no OS 27 deployment minimum. Requires App Store Connect authorization and TLS 1.2 or later.

## Overview

The App Store Server API complements [StoreKit](StoreKit.md) in the app and [App Store Server Notifications](AppStoreServerNotifications.md) on the server. It can look up purchase history even when the customer has removed the app. Use it to reconcile entitlements, inspect subscription status, recover missed notifications, and perform documented transaction-management operations.

This is a server-integration choice, not a requirement for every StoreKit app. StoreKit automatically verifies its signed values; optional additional verification can occur on the device or on a server. See [`VerificationResult`](https://developer.apple.com/documentation/storekit/verificationresult).

Transaction and renewal information arrive as signed JSON Web Signature (JWS) data. Decoding a payload is not signature verification. Verify it before granting access, and interpret expiration, revocation, and subscription status rather than treating every historical purchase as an active entitlement.

## Prerequisites and authorization

- Create an **In-App Purchase key**, not an arbitrary App Store Connect API key, using [Creating API keys to authorize API requests](https://developer.apple.com/documentation/appstoreserverapi/creating-api-keys-to-authorize-api-requests).
- Generate an ES256-signed JWT following [Generating JSON Web Tokens for API requests](https://developer.apple.com/documentation/appstoreserverapi/generating-json-web-tokens-for-api-requests), with the documented issuer, bundle ID, audience, and at most 60-minute validity, then send it as a bearer token. Never ship the private key in the app.
- Consider Apple's [App Store Server Library](https://developer.apple.com/documentation/appstoreserverapi/simplifying-your-implementation-by-using-the-app-store-server-library) for request authorization and signed-data verification.
- Keep production and sandbox records separate. Use the environment in verified transaction data to select the server.

## Topics

### Purchase and subscription state

- [Get Transaction Info](https://developer.apple.com/documentation/appstoreserverapi/get-transaction-info) — Inspect one transaction.
- [Get Transaction History](https://developer.apple.com/documentation/appstoreserverapi/get-transaction-history) — Reconcile a customer's in-app purchase history, including finished consumables; process all pages.
- [Get All Subscription Statuses](https://developer.apple.com/documentation/appstoreserverapi/get-all-subscription-statuses) — Resolve the current states of the customer's auto-renewable subscriptions.
- [Get App Transaction Info](https://developer.apple.com/documentation/appstoreserverapi/get-app-transaction-info) — Retrieve signed information about acquisition of the app itself.
- [Set App Account Token](https://developer.apple.com/documentation/appstoreserverapi/set-app-account-token) — Associate or update a UUID using the original transaction identifier. Family-shared transactions are unsupported; subscription updates affect the current and subsequent renewals, not past ones.
- [Finish Transaction](https://developer.apple.com/documentation/appstoreserverapi/finish-transaction) — Finish from the server after fulfillment. No additional server call is needed if the app already called `finish()`.

### Refunds and service recovery

- [Get Refund History](https://developer.apple.com/documentation/appstoreserverapi/get-refund-history) — Reconcile refunded transactions.
- [Send Consumption Information](https://developer.apple.com/documentation/appstoreserverapi/send-consumption-information) — Respond to a consumption request using the applicable consent and data requirements.
- [Extending subscription renewal dates](https://developer.apple.com/documentation/appstoreserverapi/extending-the-renewal-date-for-auto-renewable-subscriptions) — Compensate eligible subscriptions for a service interruption; check eligibility rather than assuming every subscription can be extended.

### Notification recovery and testing

- [Get Notification History](https://developer.apple.com/documentation/appstoreserverapi/get-notification-history) — Retrieve attempted notifications from the past 180 days in production or 30 days in sandbox.
- [Request a Test Notification](https://developer.apple.com/documentation/appstoreserverapi/request-a-test-notification) and [Get Test Notification Status](https://developer.apple.com/documentation/appstoreserverapi/get-test-notification-status) — Verify end-to-end delivery to your configured HTTPS receiver.
- [JWS transaction payload](https://developer.apple.com/documentation/appstoreserverapi/jwstransactiondecodedpayload) and [JWS renewal payload](https://developer.apple.com/documentation/appstoreserverapi/jwsrenewalinfodecodedpayload) — Use the documented schema rather than deriving field names from Swift properties.

## Service updates reviewed through September 8, 2026

The [service changelog](https://developer.apple.com/documentation/appstoreserverapi/app-store-server-api-changelog) records `Finish Transaction` in version 1.20 on April 13, 2026, and commitment/billing-plan fields in version 1.21 on April 27. These are server releases, not features gated on an OS 27 app binary.

The May 5 server update recommends `https://api.storekit.apple.com/` and `https://api.storekit-sandbox.apple.com/`. Apple states that the previous `itunes.apple.com` domains remain supported; the change is not an announced removal.

StoreKit's OS 27 volume-assignment and subscription Bundle/Suite changes require corresponding entitlement-model review, but do not imply undocumented REST endpoints or notification types. Consult the current server schemas and each service's changelog independently.

## Failure handling and testing

- Handle [rate limits](https://developer.apple.com/documentation/appstoreserverapi/identifying-rate-limits) and [structured error codes](https://developer.apple.com/documentation/appstoreserverapi/error-codes). Back off on `429`; this API documents `Retry-After` as a UNIX timestamp in milliseconds. Do not retry invalid authorization or malformed requests indefinitely.
- If the transaction environment is unknown, Apple's documented fallback is production first, then sandbox specifically for `4040010` (`TransactionIdNotFoundError`). A generic failure is not a reason to change environments.
- All endpoints except `Look Up Order ID` support sandbox testing. Use sandbox transaction identifiers with sandbox endpoints.
- TestFlight In-App Purchases use the sandbox. Local Xcode StoreKit-configuration tests are not sandbox server-integration tests, even when the configuration imports product information from App Store Connect. See [StoreKit testing contexts](StoreKit.md#testing-contexts).
- Make fulfillment and notification processing idempotent. After a timeout on a state-changing request, reconcile the purchase before repeating the operation.
- Test expired, revoked, refunded, missing, and unverifiable transactions, as well as delayed or repeated notifications. Never turn signature-verification failure into a successful purchase.

## Related documentation

- [App Store Receipts](appstorereceipts.md) — Migration considerations for deprecated receipt validation.
- [Advanced Commerce API](AdvancedCommerceAPI.md) — Related SKU and subscription-management workflows with their own request contracts.
- [App Store readiness](../guides/app-store-readiness.md) and [Regional distribution](../guides/regional-distribution.md) — Submission and distribution policy guidance, separate from this API contract.

## Sources

- [App Store Server API](https://developer.apple.com/documentation/appstoreserverapi)
- [App Store Server API changelog](https://developer.apple.com/documentation/appstoreserverapi/app-store-server-api-changelog)
- [App Store Server Library](https://developer.apple.com/documentation/appstoreserverapi/simplifying-your-implementation-by-using-the-app-store-server-library)
- [StoreKit verification results](https://developer.apple.com/documentation/storekit/verificationresult)
