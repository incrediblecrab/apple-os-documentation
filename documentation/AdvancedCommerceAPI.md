# Advanced Commerce API

Support In-App Purchases through the App Store for exceptionally large catalogs of custom one-time purchases, subscriptions, and subscriptions with optional add-ons.

**Availability:** Authorized App Store commerce integrations, through StoreKit and server APIs. The service first shipped in January 2025 and follows its own changelog, not an OS 27 baseline.

## Overview

Use this API to offer an exceptionally large catalog of one-time purchases, subscriptions, and subscriptions with optional add-ons while using the App Store commerce system. Apps that use this API host and manage their own catalog of In-App Purchases, or SKUs. The App Store commerce system handles the end-to-end payment processing, global distribution, tax support, and customer service.

You can use the Advanced Commerce API and the StoreKit In-App Purchase API in the same app. Both APIs use the App Store commerce system, including the same signed JWS transactions and JWS renewal info. For products that you offer using the In-App Purchase API, you set up product identifiers in App Store Connect. For products that you offer using the Advanced Commerce API, you host and manage your own catalog of SKUs and add product details dynamically at runtime. For complete setup information, see Setting up your project for Advanced Commerce API.

Advanced Commerce API features are available through requests you make using StoreKit in your app and endpoint requests from your server. To authorize these requests, you generate JSON Web Tokens (JWTs). The App Store Server Library provides a client that makes it easier to create JWTs to authorize calls. For more information about the library, see Simplifying your implementation by using the App Store Server Library. For more information about authorizing calls, see Authorizing API requests from your server.

Your server must support the Transport Layer Security (TLS) protocol 1.2 or later to call the Advanced Commerce API.

**Important:** Review eligibility and apply through [Advanced Commerce API](https://developer.apple.com/in-app-purchase/advanced-commerce-api/). Approval, generic product identifiers, a server-managed SKU catalog, and request signing are prerequisites; adding StoreKit alone does not grant access.

## Current integration guidance

The OS 27 release notes describe partner metadata using `partnerName` and `partnerId`. Current Swift declarations represent it with [`Item.Details.partners`](https://developer.apple.com/documentation/storekit/transaction/advancedcommerceinfo-swift.struct/item/details-swift.struct), an array of [`Partner`](https://developer.apple.com/documentation/storekit/transaction/advancedcommerceinfo-swift.struct/partner) values exposing `id` and optional `name`; renewal-item details use the same type. See [StoreKit](StoreKit.md) for the naming distinction. Do not assume flat Swift members from release-note labels or tie this SDK change to the REST service's version.

The [service changelog](https://developer.apple.com/documentation/advancedcommerceapi/changelog), reviewed through September 8, 2026, records version 1.2's dependent-SKU price-change support and subsequent 2026 validation/error updates. Follow [Handling subscription price changes](https://developer.apple.com/documentation/advancedcommerceapi/handling-subscription-price-changes) for the current communication flow, rather than assuming that developers must always send every price-change notice themselves.

Sign requests on your server and verify returned JWS data. Do not reuse a REST bearer JWT as an in-app request: the [in-app signing contract](https://developer.apple.com/documentation/storekit/generating-jws-to-sign-app-store-requests) uses the `advanced-commerce-api` audience, a one-time nonce, base64-encoded request data, and no `exp` claim.

Cancellation turns off renewal while preserving access through the current period. For [Revoke Subscription](https://developer.apple.com/documentation/advancedcommerceapi/revoke-subscription), Apple instructs you to wait for the `REFUND` notification and use its `revocationDate` before turning off service; an HTTP response alone is not that notification. Cancel, revoke, and refund operations also require the Account Holder to accept the current Advanced Commerce API Addendum.

Handle [rate limits](https://developer.apple.com/documentation/advancedcommerceapi/ratelimits) and [structured errors](https://developer.apple.com/documentation/advancedcommerceapi/errorcodes). After a timeout, reconcile the subscription before repeating a state-changing operation. Policy and country-specific requirements belong in [App Store readiness](../guides/app-store-readiness.md) and [Regional distribution](../guides/regional-distribution.md).

## Topics

### Essentials
- [Setting up your project for Advanced Commerce API](https://developer.apple.com/documentation/advancedcommerceapi/setting-up-your-project-for-advanced-commerce) - Configure your app in App Store Connect, set up your server, and prepare your SKUs.
- [Setting up generic product identifiers](https://developer.apple.com/documentation/advancedcommerceapi/setting-up-generic-product-identifiers) - Configure the product IDs required for Advanced Commerce.
- [Creating SKUs for your In-App Purchases](https://developer.apple.com/documentation/advancedcommerceapi/creating-your-purchases) - Define and manage one-time charges, subscriptions, and bundled subscriptions within your app.
- [Setting up a link to manage subscriptions](https://developer.apple.com/documentation/advancedcommerceapi/setupmanagesubscriptions) - Create a deep link to a subscription-management page for your app.
- [Advanced Commerce API changelog](https://developer.apple.com/documentation/advancedcommerceapi/changelog) - Learn about new features and updates in the Advanced Commerce API.

### Tax codes and pricing
- [Specifying prices for Advanced Commerce SKUs](https://developer.apple.com/documentation/advancedcommerceapi/prices) - Provide prices for SKUs with the supported number of decimal places, in milliunits of currency.
- [Choosing tax codes for your SKUs](https://developer.apple.com/documentation/advancedcommerceapi/taxcodes) - Select a tax code for each SKU that represents a product your app offers as an in-app purchase.
- [Handling subscription price changes](https://developer.apple.com/documentation/advancedcommerceapi/handling-subscription-price-changes) - Initiate price changes and manage subscriber communications through the App Store.

### API authorization and rate limits
- [Authorizing API requests from your server](https://developer.apple.com/documentation/advancedcommerceapi/authorizing-server-calls) - Create JSON Web Tokens (JWTs) to authorize Advanced Commerce requests from your server.
- [Identifying rate limits for Advanced Commerce APIs](https://developer.apple.com/documentation/advancedcommerceapi/ratelimits) - Recognize and handle the rate limits that apply to Advanced Commerce API endpoints.

### In-app API requests
- [Sending Advanced Commerce API requests from your app](https://developer.apple.com/documentation/storekit/sending-advanced-commerce-api-requests-from-your-app) - Send requests authorized by a JWS generated on your server.
- [Generating JWS to sign App Store requests](https://developer.apple.com/documentation/storekit/generating-jws-to-sign-app-store-requests) - Create signed JWS strings on your server to authorize in-app requests.

### One-time charge creation in the app
- **OneTimeChargeCreateRequest** - The request data your app provides when a customer purchases a one-time-charge product.
- **OneTimeChargeItem** - The details of a one-time charge product, including its display name, price, SKU, and metadata.

### Subscription creation in the app
- **SubscriptionCreateRequest** - The request data your app provides when a customer purchases an auto-renewable subscription.
- **SubscriptionCreateItem** - The data that describes a subscription item.

### Subscription modification in the app
- **SubscriptionModifyInAppRequest** - The request data your app provides to make changes to an auto-renewable subscription.
- **SubscriptionModifyAddItem** - The data your app provides to add items when it makes changes to an auto-renewable subscription.
- **SubscriptionModifyChangeItem** - The data your app provides to change an item of an auto-renewable subscription.
- **SubscriptionModifyRemoveItem** - The data your app provides to remove an item from an auto-renewable subscription.
- **SubscriptionModifyPeriodChange** - The data your app provides to change the period of an auto-renewable subscription.

### Subscription reactivation in the app
- **SubscriptionReactivateInAppRequest** - The request your app provides to reactivate a subscription that has automatic renewal turned off.
- **SubscriptionReactivateItem** - An item in a subscription to reactivate.

### Subscription price change from the server
- [Change Subscription Price](https://developer.apple.com/documentation/advancedcommerceapi/change-subscription-price) - Schedule price changes for a subscription or its items, subject to the documented renewal, notice, and consent rules.
- **SubscriptionPriceChangeRequest** - The request body you use to change the price of an auto-renewable subscription.
- **SubscriptionPriceChangeResponse** - A response that contains signed JWS renewal and JWS transaction information after a subscription price change request.

### Subscription cancellation from the server
- [Cancel a Subscription](https://developer.apple.com/documentation/advancedcommerceapi/cancel-a-subscription) - Turn off automatic renewal to cancel a customer's auto-renewable subscription.
- **SubscriptionCancelRequest** - The request body for turning off automatic renewal of a subscription.
- **SubscriptionCancelResponse** - The response body for a successful subscription cancellation.

### Subscription revocation from the server
- [Revoke Subscription](https://developer.apple.com/documentation/advancedcommerceapi/revoke-subscription) - Immediately cancel a customer's subscription and all the items that are included in the subscription, and request a full or prorated refund.
- **SubscriptionRevokeRequest** - The request body you provide to terminate a subscription and all its items immediately.
- **SubscriptionRevokeResponse** - The response body for a successful revoke-subscription request.

### Refund request from the server
- [Request Transaction Refund](https://developer.apple.com/documentation/advancedcommerceapi/request-transaction-refund) - Request a refund for a one-time charge or subscription transaction.
- **RequestRefundRequest** - The request body for requesting a refund for a transaction.
- **RequestRefundResponse** - The response body for a transaction refund request.
- **RequestRefundItem** - Information about the refund request for an item, such as its SKU, the refund amount, reason, and type.

### Subscription metadata changes from the server
- [Change Subscription Metadata](https://developer.apple.com/documentation/advancedcommerceapi/change-subscription-metadata) - Update the SKU, display name, and description associated with a subscription, without affecting the subscription's billing or its service.
- **SubscriptionChangeMetadataRequest** - The request body you provide to change the metadata of a subscription.
- **SubscriptionChangeMetadataResponse** - The response body for a successful subscription metadata change.
- **SubscriptionChangeMetadataDescriptors** - The subscription metadata to change, specifically the description and display name.
- **SubscriptionChangeMetadataItem** - The metadata to change for an item, specifically its SKU, description, and display name.

### Migration from the server
- [Migrate a Subscription to Advanced Commerce API](https://developer.apple.com/documentation/advancedcommerceapi/migrate-subscription-to-advanced-commerce-api) - Migrate a subscription that a customer purchased through In-App Purchase to a subscription you manage using the Advanced Commerce API.
- **SubscriptionMigrateRequest** - The subscription details you provide to migrate a subscription from In-App Purchase to the Advanced Commerce API, such as descriptors, items, storefront, and more.
- **SubscriptionMigrateResponse** - A response that contains signed renewal and transaction information after a subscription successfully migrates to the Advanced Commerce API.
- **SubscriptionMigrateItem** - The SKU, description, and display name to use for a migrated subscription item.
- **SubscriptionMigrateRenewalItem** - The item information that replaces a migrated subscription item when the subscription renews.
- **SubscriptionMigrateDescriptors** - The description and display name of the subscription to migrate to that you manage.

### Objects and types
- [Data types](https://developer.apple.com/documentation/advancedcommerceapi/datatypes) - Objects and data types for the Advanced Commerce API.

### Signed transaction information
- **JWSRenewalInfo** - Subscription renewal information signed by the App Store, in JSON Web Signature (JWS) format.
- **JWSTransaction** - Transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format.

### Error handling
- [Error messages and codes](https://developer.apple.com/documentation/advancedcommerceapi/errorcodes) - Error messages and codes for the Advanced Commerce API.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AdvancedCommerceAPI)*
