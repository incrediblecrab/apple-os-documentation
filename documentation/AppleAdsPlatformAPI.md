# Apple Ads Platform API

Manage App Store and Apple Maps advertising through a server-side REST interface.

**Availability:** Apple Ads Platform API 1.0, initially released in August 2026. This is a versioned web service, not an OS 27 SDK framework. Access depends on account roles, product features, and advertiser-resource delegations.

## Overview

The API manages ad accounts, campaigns, ad groups, keywords, ads, creative assets, and reporting. App Store campaigns promote apps; Apple Maps campaigns promote businesses and use brand and location resources.

This is distinct from the older [Apple Ads Campaign Management API](apple_ads.md). Apple's changelog explicitly says the Platform API supersedes that API and announces its sunset on **January 26, 2027**. As of the September 8, 2026 review cutoff, this is a future retirement, not an already completed removal.

Migration requires reviewing the new resources and contracts. Do not simply rename the old API or assume that its endpoint hierarchy, request bodies, and account identifiers are interchangeable.

## Authorization and account scope

1. Have an account administrator invite a user with an API role.
2. Generate the required key pair, register the public key, and keep the private key secure.
3. Follow [Implementing OAuth](https://developer.apple.com/documentation/apple-ads-platform-api/implementing-oauth-for-the-apple-ads-platform-api) to sign the client secret and request an access token with `searchadsorg` scope. Renew using `expires_in`.
4. Send the token as a bearer token. For ad-account-scoped operations, supply `X-AP-Context: adAccountId={adAccountId}`. Identity and account-discovery operations have documented exceptions.

The documented API base is `https://api.ads.apple.com/v1/`. Follow [Managing Ad Accounts and API Access](https://developer.apple.com/documentation/apple-ads-platform-api/access-overview) to discover the caller's permitted accounts instead of guessing an account ID.

App Store ad accounts need the `APPSTORE_APP_MANUAL` product feature and a `CONTENT_PROVIDER` delegation. Apple Maps ad accounts need `BUSINESS_BRAND_MANUAL` and a `BUSINESS_BRAND` delegation. Authorization for one placement does not authorize the other.

## Topics and workflows

- [Advertising an app on the App Store](https://developer.apple.com/documentation/apple-ads-platform-api/journey-app-store-ads) — Verify app/account eligibility, then configure targeting and reporting.
- [Advertising a business on Apple Maps](https://developer.apple.com/documentation/apple-ads-platform-api/journey-apple-maps-brand-ads) — Resolve the brand, creative assets, and location groups before configuring campaigns.
- [Campaign endpoints](https://developer.apple.com/documentation/apple-ads-platform-api/campaigns-endpoints) and [Ad group endpoints](https://developer.apple.com/documentation/apple-ads-platform-api/adgroups-endpoints) — Manage budgets, scheduling, and campaign structure.
- [Keywords and negative keywords](https://developer.apple.com/documentation/apple-ads-platform-api/keywords-and-negative-keywords) — Manage search matching and exclusions.
- [Creative endpoints](https://developer.apple.com/documentation/apple-ads-platform-api/creatives-endpoints) — Manage placement-specific creatives. [Asset endpoints](https://developer.apple.com/documentation/apple-ads-platform-api/assets-endpoints) upload and manage Apple Maps creative assets.
- [Managing reports](https://developer.apple.com/documentation/apple-ads-platform-api/reports) — Use the appropriate App Store or business reporting model.
- [Bulk operations](https://developer.apple.com/documentation/apple-ads-platform-api/bulk-operations-endpoints) — Match individual results to inputs using `correlationId`.
- [Client libraries](https://developer.apple.com/documentation/apple-ads-platform-api/client-libraries) — Evaluate Apple's maintained clients rather than duplicating every schema.

## Request semantics and failure handling

The [calling guide](https://developer.apple.com/documentation/apple-ads-platform-api/calling-apple-ads-platform-api) documents POST-based `/query` operations with filters, sorting, and pagination. Where an endpoint supports partial PUT updates, omitted properties are preserved, but an included array replaces that array's complete contents.

For bulk requests, `allowPartialSuccess: true` permits successful items to complete even if others fail. Inspect every result; do not retry a whole batch as though no writes occurred. When the option is absent or false, a failing item rejects the batch.

Read the [rate-limit headers](https://developer.apple.com/documentation/apple-ads-platform-api/rate-limits) on responses. On `429`, honor `Retry-After`, falling back to `RateLimit-Reset` and bounded backoff. Both describe delays in seconds, not absolute timestamps.

Correct invalid credentials, account scope, or eligibility before retrying. Begin integration checks with read operations: creating or enabling a campaign and applying budget recommendations can affect real advertising spend.

## Sources

- [Apple Ads Platform API](https://developer.apple.com/documentation/apple-ads-platform-api)
- [Platform API changelog](https://developer.apple.com/documentation/apple-ads-platform-api/changelog-apple-ads-platform-api)
- [OAuth authorization](https://developer.apple.com/documentation/apple-ads-platform-api/implementing-oauth-for-the-apple-ads-platform-api)
- [Calling the API](https://developer.apple.com/documentation/apple-ads-platform-api/calling-apple-ads-platform-api)
- [Rate limits](https://developer.apple.com/documentation/apple-ads-platform-api/rate-limits)
- [Older Apple Ads API](https://developer.apple.com/documentation/apple_ads)
