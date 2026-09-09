# Apple Ads

Drive app discovery by creating and managing campaigns with the Apple Ads Campaign Management API.

**Availability:** Server-side Apple Ads Campaign Management API. This reference covers the older API, including version 5; it is not an OS 27 framework.

## Overview

**Migration status, September 8, 2026:** Apple explicitly states that the [Apple Ads Platform API](AppleAdsPlatformAPI.md) supersedes the Campaign Management API, with sunset scheduled for **January 26, 2027**. This is a future retirement, not a claim that version 5 has already been removed. The new service adds Apple Maps advertising and has its own resources, account scoping, and version 1.0 contract; do not treat the names as interchangeable.

Campaign Management API 5 manages App Store campaigns, budgets, ad groups, keyword bidding, audience criteria, and scheduling. Search Match can match ads to relevant searches without individually specifying every keyword.

Check app eligibility for each intended market. Custom product pages supply ad variations and localized assets; creating a variation does not itself establish eligibility in additional countries. Use campaign and impression-share reports to evaluate performance.

**Version 5 contract:** The [5.6 changelog](https://developer.apple.com/documentation/apple_ads/apple-search-ads-campaign-management-api-5) records the June 2026 removal of `budgetAmount`; use `dailyBudgetAmount`. Older versioned examples that contain lifetime budgets are not the current v5 request contract.

## Topics

### Essentials
- [Implementing OAuth for the Apple Ads API](https://developer.apple.com/documentation/apple_ads/implementing-oauth-for-the-apple-search-ads-api) - Manage secure access to Ads accounts.
- [Calling the Apple Ads API](https://developer.apple.com/documentation/apple_ads/calling-the-apple-search-ads-api) - Pass your access token in the authorization header of HTTP requests.
- [Using Apple Ads API Functionality](https://developer.apple.com/documentation/apple_ads/using-apple-search-ads-api-functionality) - Call endpoints using CRUD methods.

### Apps
- [Search Apps](https://developer.apple.com/documentation/apple_ads/search-apps) - Search for iOS apps to promote in a campaign.
- [App Eligibility](https://developer.apple.com/documentation/apple_ads/app-eligibility) - Check whether your app is eligible to promote in a campaign.
- [App Details](https://developer.apple.com/documentation/apple_ads/app-details) - Fetch app metadata.

### Campaigns
- [Campaigns](https://developer.apple.com/documentation/apple_ads/campaigns) - Create and manage Apple Ads campaigns.
- [Budget Orders](https://developer.apple.com/documentation/apple_ads/budget-orders) - Cap spending across campaigns for eligible monthly-invoiced accounts; budget orders are unavailable with Pay as You Go billing.
- [Ad Groups](https://developer.apple.com/documentation/apple_ads/ad-groups) - Create and manage ad groups.
- [Targeting Keywords and Negative Keywords](https://developer.apple.com/documentation/apple_ads/targeting-keywords-and-negative-keywords) - Configure search targeting and keyword exclusions.
- [Search Geolocations](https://developer.apple.com/documentation/apple_ads/search-geolocations) - Find geographic criteria and location identifiers for ad targeting.

### Custom Product Page Ads
- [Ads](https://developer.apple.com/documentation/apple_ads/ads) - Assign an ad creative to an ad group.
- [Ad Rejection Reasons](https://developer.apple.com/documentation/apple_ads/ad-rejection-reasons) - Review reasons for an ad rejection.
- [Creatives](https://developer.apple.com/documentation/apple_ads/creatives) - Create and manage ad creatives within your organization.
- [Custom Product Pages](https://developer.apple.com/documentation/apple_ads/custom-product-pages) - View Custom Product Page details.

### Reports
- [Reports](https://developer.apple.com/documentation/apple_ads/reports) - Generate performance metrics for your campaigns.
- [Impression Share Reports](https://developer.apple.com/documentation/apple_ads/impression-share-reports) - Obtain metrics with impression share insights.

### Changelog
- [Apple Ads Campaign Management API 5](https://developer.apple.com/documentation/apple_ads/apple-search-ads-campaign-management-api-5) - Review version 5 and its announced sunset.
- [Apple Ads Campaign Management API 4](https://developer.apple.com/documentation/apple_ads/apple-search-ads-campaign-management-api-4) - Learn about changes to Apple Ads Campaign Management API 4.
- [Apple Ads Campaign Management API 3](https://developer.apple.com/documentation/apple_ads/apple-search-ads-campaign-management-api-3) - Apple no longer supports this API.
- [Apple Ads Campaign Management API 2](https://developer.apple.com/documentation/apple_ads/apple-search-ads-campaign-management-api-2) - Apple no longer supports this API.
- [Apple Ads Campaign Management API 1](https://developer.apple.com/documentation/apple_ads/apple-search-ads-campaign-management-api-1) - Apple no longer supports this API.

### Retired functionality
- [Creative Sets](https://developer.apple.com/documentation/apple_ads/creative-sets) - No longer supported and unavailable in API 5; use custom product page ads. Historical routes may return HTTP 200 with an invalid state, which does not indicate usable functionality.

## Migration and failure handling

Maintain the existing API's authorization and error handling until migration is complete. Validate account access, app eligibility, pagination, reporting differences, and write results against the new API contract before moving a production workflow. Start with read-only comparisons and avoid duplicating active campaigns or budgets during cutover.

The [legacy calling guide](https://developer.apple.com/documentation/apple_ads/calling-the-apple-search-ads-api) uses `https://api.searchads.apple.com/api/v5/` and `X-AP-Context: orgId={orgId}` for scoped requests. Those are not the Platform API's base URL or `adAccountId` context. Correct an invalid token (`401`) or insufficient privileges (`403`) before retrying; use bounded backoff for transient failures.

The [Platform API changelog](https://developer.apple.com/documentation/apple-ads-platform-api/changelog-apple-ads-platform-api) is the source for the August 2026 replacement and January 2027 sunset, not a platform release note.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/apple_ads)*
