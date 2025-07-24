# Advanced Commerce API

Support In-App Purchases through the App Store for exceptionally large catalogs of custom one-time purchases, subscriptions, and subscriptions with optional add-ons.

**Platforms:** Advanced Commerce API 1.0+

## Overview

Use this framework to offer an exceptionally large catalog of one-time purchases, subscriptions, and subscriptions with optional add-ons while using the App Store commerce system. Apps that use this API host and manage their own catalog of In-App Purchases, or SKUs. The App Store commerce system handles the end-to-end payment processing, global distribution, tax support, and customer service.

You can use the Advanced Commerce API and the StoreKit In-App Purchase API in the same app. Both APIs use the App Store commerce system, including the same signed JWS transactions and JWS renewal info. For products that you offer using the In-App Purchase API, you set up product identifiers in App Store Connect. For products that you offer using the Advanced Commerce API, you host and manage your own catalog of SKUs and add product details dynamically at runtime. For complete setup information, see Setting up your project for Advanced Commerce API.

Advanced Commerce API features are available through requests you make using StoreKit in your app and endpoint requests from your server. To authorize these requests, you generate JSON Web Tokens (JWTs). The App Store Server Library provides a client that makes it easier to create JWTs to authorize calls. For more information about the library, see Simplifying your implementation by using the App Store Server Library. For more information about authorizing calls, see Authorizing API requests from your server.

Your server must support the Transport Layer Security (TLS) protocol 1.2 or later to call the Advanced Commerce API.

**Important:** To learn more about eligiblity and apply for access to the Advanced Commerce API, see Advanced Commerce API.

## Topics

### Essentials
- [Setting up your project for Advanced Commerce API](https://developer.apple.com/documentation/advancedcommerceapi/setting_up_your_project_for_advanced_commerce_api) - Configure your app in App Store Connect, set up your server, and prepare your SKUs.
- [Creating SKUs for your In-App Purchases](https://developer.apple.com/documentation/advancedcommerceapi/creating_skus_for_your_in-app_purchases) - Define and manage one-time charges, subscriptions, and bundled subscriptions within your app.
- [Setting up a link to manage subscriptions](https://developer.apple.com/documentation/advancedcommerceapi/setting_up_a_link_to_manage_subscriptions) - Create a deep link to a subscription-management page for your app.
- [Advanced Commerce API changelog](https://developer.apple.com/documentation/advancedcommerceapi/advanced_commerce_api_changelog) - Learn about new features and updates in the Advanced Commerce API.

### Tax codes and pricing
- [Specifying prices for Advanced Commerce SKUs](https://developer.apple.com/documentation/advancedcommerceapi/specifying_prices_for_advanced_commerce_skus) - Provide prices for SKUs with the supported number of decimal places, in milliunits of currency.
- [Choosing tax codes for your SKUs](https://developer.apple.com/documentation/advancedcommerceapi/choosing_tax_codes_for_your_skus) - Select a tax code for each SKU that represents a product your app offers as an in-app purchase.
- [Handling subscription price changes](https://developer.apple.com/documentation/advancedcommerceapi/handling_subscription_price_changes) - Provide necessary customer communications to notify and gather applicable consent before you initiate a price change.

### API authorization and rate limits
- [Authorizing API requests from your server](https://developer.apple.com/documentation/advancedcommerceapi/authorizing_api_requests_from_your_server) - Create JSON Web Tokens (JWTs) to authorize Advanced Commerce requests from your server.
- [Identifying rate limits for Advanced Commerce APIs](https://developer.apple.com/documentation/advancedcommerceapi/identifying_rate_limits_for_advanced_commerce_apis) - Recognize and handle the rate limits that apply to Advanced Commerce API endpoints.

### In-app API requests
- [Sending Advanced Commerce API requests from your app](https://developer.apple.com/documentation/advancedcommerceapi/sending_advanced_commerce_api_requests_from_your_app) - Send Advanced Commerce API requests from your app that you authorize with a JSON Web Signature (JWS) you generate on your server.
- [Generating JWS to sign App Store requests](https://developer.apple.com/documentation/advancedcommerceapi/generating_jws_to_sign_app_store_requests) - Create signed JSON Web Signature (JWS) strings on your server to authorize your API requests in your app.

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
- **SubscriptionReactivateItem** - An item in a subscription to reactive.

### Subscription price change from the server
- [Change Subscription Price](https://developer.apple.com/documentation/advancedcommerceapi/change_subscription_price) - Increase or decrease the price of an auto-renewable subscription, a bundle, or individual items within a subscription at the next renewal.
- **SubscriptionPriceChangeRequest** - The request body you use to change the price of an auto-renewable subscription.
- **SubscriptionPriceChangeResponse** - A response that contains signed JWS renewal and JWS transaction information after a subscription price change request.

### Subscription cancellation from the server
- [Cancel a Subscription](https://developer.apple.com/documentation/advancedcommerceapi/cancel_a_subscription) - Turn off automatic renewal to cancel a customer's auto-renewable subscription.
- **SubscriptionCancelRequest** - The request body for turning off automatic renewal of a subscription.
- **SubscriptionCancelResponse** - The response body for a successful subscription cancellation.

### Subscription revocation from the server
- [Revoke Subscription](https://developer.apple.com/documentation/advancedcommerceapi/revoke_subscription) - Immediately cancel a customer's subscription and all the items that are included in the subscription, and request a full or prorated refund.
- **SubscriptionRevokeRequest** - The request body you provide to terminate a subscription and all its items immediately.
- **SubscriptionRevokeResponse** - The response body for a successful revoke-subscription request.

### Refund request from the server
- [Request Transaction Refund](https://developer.apple.com/documentation/advancedcommerceapi/request_transaction_refund) - Request a refund for a one-time charge or subscription transaction.
- **RequestRefundRequest** - The request body for requesting a refund for a transaction.
- **RequestRefundResponse** - The response body for a transaction refund request.
- **RequestRefundItem** - Information about the refund request for an item, such as its SKU, the refund amount, reason, and type.

### Subscription metadata changes from the server
- [Change Subscription Metadata](https://developer.apple.com/documentation/advancedcommerceapi/change_subscription_metadata) - Update the SKU, display name, and description associated with a subscription, without affecting the subscription's billing or its service.
- **SubscriptionChangeMetadataRequest** - The request body you provide to change the metadata of a subscription.
- **SubscriptionChangeMetadataResponse** - The response body for a successful subscription metadata change.
- **SubscriptionChangeMetadataDescriptors** - The subscription metadata to change, specifically the description and display name.
- **SubscriptionChangeMetadataItem** - The metadata to change for an item, specifically its SKU, description, and display name.

### Migration from the server
- [Migrate a Subscription to Advanced Commerce API](https://developer.apple.com/documentation/advancedcommerceapi/migrate_a_subscription_to_advanced_commerce_api) - Migrate a subscription that a customer purchased through In-App Purchase to a subscription you manage using the Advanced Commerce API.
- **SubscriptionMigrateRequest** - The subscription details you provide to migrate a subscription from In-App Purchase to the Advanced Commerce API, such as descriptors, items, storefront, and more.
- **SubscriptionMigrateResponse** - A response that contains signed renewal and transaction information after a subscription successfully migrates to the Advanced Commerce API.
- **SubscriptionMigrateItem** - The SKU, description, and display name to use for a migrated subscription item.
- **SubscriptionMigrateRenewalItem** - The item information that replaces a migrated subscription item when the subscription renews.
- **SubscriptionMigrateDescriptors** - The description and display name of the subscription to migrate to that you manage.

### Objects and types
- [Data types](https://developer.apple.com/documentation/advancedcommerceapi/data_types) - Objects and data types for the Advanced Commerce API.

### Signed transaction information
- **JWSRenewalInfo** - Subscription renewal information signed by the App Store, in JSON Web Signature (JWS) format.
- **JWSTransaction** - Transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format.

### Error handling
- [Error messages and codes](https://developer.apple.com/documentation/advancedcommerceapi/error_messages_and_codes) - Error messages and codes for the Advanced Commerce API.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AdvancedCommerceAPI)*