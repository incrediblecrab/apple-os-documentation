# StoreKit

Support In-App Purchases and interactions with the App Store.

**Platforms:** iOS 3.0+ | iPadOS 3.0+ | Mac Catalyst 13.0+ | macOS 10.7+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 6.2+

## Overview

Use the StoreKit framework to provide the following features and services for your apps and In-App Purchases:

**In-App Purchase**  
Offer and promote In-App Purchases for content and services.

**App transaction**  
Verify a customer's app purchase with an App Store-signed transaction.

**Messages**  
Control the display of App Store messages in your app.

**Reviews**  
Request App Store reviews and ratings from your customers.

**Recommendations**  
Provide recommendations for third-party content that customers can purchase from the App Store.

**Ad network attribution**  
Validate advertisement-driven app installations. See AdAttributionKit for app ad campaigns on the App Store and alternative marketplaces.

The StoreKit framework also provides functionality for External Purchase, External link account, PaymentMethodBinding, and StoreDownloaderExtension.

## OS 27 SDK changes reviewed September 8, 2026

The iOS/iPadOS, macOS, and watchOS 27 beta release notes identify changes to purchase ownership and subscription models. These are specific API changes, not a new minimum version for the entire StoreKit framework.

- **Volume-assigned purchases:** `Transaction.OwnershipType.assigned` identifies access through an organization, and [`Transaction.RevocationType.assignmentRevocation`](https://developer.apple.com/documentation/storekit/transaction/revocationtype-swift.struct/assignmentrevocation) represents revocation by its administrator. Transaction queries now include purchases assigned to a Managed Apple Account. Do not assume that ownership is limited to a direct purchase or Family Sharing, or that every revocation is a refund.
- **Availability nuance:** The [`assigned`](https://developer.apple.com/documentation/storekit/transaction/ownershiptype-swift.struct/assigned) accessor is explicitly back-deployed before the 27 releases. Distinguish an SDK addition from a strict runtime availability requirement; check each declaration.
- **Subscription Bundles and Suites:** [`Product.ProductType.subscriptionBundle`](https://developer.apple.com/documentation/storekit/product/producttype/subscriptionbundle) and [`subscriptionSuite`](https://developer.apple.com/documentation/storekit/product/producttype/subscriptionsuite) are 27.0 APIs. [`Product.SubscriptionInfo.BundledSubscription`](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/bundledsubscription) supplies merchandising information for subscriptions in a Bundle. Review the associated Transaction and RenewalInfo fields instead of equating a Bundle's purchase with an independent purchase of every component.
- **Offer-code verification:** The iOS/iPadOS and macOS notes document redemption APIs returning `VerificationResult<Transaction>` and throwing on failure. The [UIKit overload](https://developer.apple.com/documentation/storekit/appstore/presentoffercoderedeemsheet(from:options:)-89agc) takes a view controller and options; use the corresponding platform API rather than applying that signature to macOS or watchOS.
- **Advanced Commerce metadata:** The beta notes use the labels `partnerName` and `partnerId`. Current Swift DocC exposes [`Item.Details.partners`](https://developer.apple.com/documentation/storekit/transaction/advancedcommerceinfo-swift.struct/item/details-swift.struct), an array of [`Partner`](https://developer.apple.com/documentation/storekit/transaction/advancedcommerceinfo-swift.struct/partner) values with `id` and optional `name` properties. Renewal-item `Details` aliases that same details type. Follow these declarations rather than assuming flat properties on `AdvancedCommerceInfo`. The server-side [Advanced Commerce API](AdvancedCommerceAPI.md) remains independently versioned.

**Source naming difference:** The beta release notes call the revocation member `assignmentRevoked`, but the current symbol declaration names it `assignmentRevocation`. That accessor is back-deployed before the 27 releases on the 26.4 `RevocationType` API. Use the declaration in your SDK, not the release-note spelling, when writing code.

## Verification and entitlement handling

StoreKit **automatically verifies** its `Transaction`, subscription `RenewalInfo`, and `AppTransaction` values. Inspect [`VerificationResult`](https://developer.apple.com/documentation/storekit/verificationresult): `.verified` passed those checks, while `.unverified` did not. Merely reading `unsafePayloadValue` does not establish a valid purchase.

Additional verification of the JWS is optional and can take place **on the device or on a server**. StoreKit does not require every app to operate its own transaction-verification server. If you choose server-side verification, Apple's App Store Server Library provides verification helpers.

### Product loading and purchase outcomes

[`Product.products(for:)`](https://developer.apple.com/documentation/storekit/product/products(for:)) is asynchronous and throwing. It can also return fewer products than requested because invalid or unfound identifiers are omitted. Handle loading, thrown errors, and missing products separately; do not assume the result has one entry per requested identifier. Product availability is not proof of purchase ownership.

Handle each [`Product.PurchaseResult`](https://developer.apple.com/documentation/storekit/product/purchaseresult):
- `.success` contains a verification result, not an unconditional instruction to grant access.
- `.pending` requires further customer action. Do not grant the pending purchase; if it succeeds later, StoreKit delivers its transaction through `Transaction.updates`.
- `.userCancelled` means the customer canceled the purchase. Do not turn it into a completed purchase or automatically restart checkout.

### Entitlement refresh and restoration

Reconcile [`Transaction.currentEntitlements`](https://developer.apple.com/documentation/storekit/transaction/currententitlements) with [`Transaction.updates`](https://developer.apple.com/documentation/storekit/transaction/updates). Current entitlements exclude refunded or revoked products and consumables; a verified revocation update is a reason to withdraw access, not grant it again. Start the update listener at launch, and also process the successful purchase result for a purchase made on the same device. For fulfilled purchases, call [`finish()`](https://developer.apple.com/documentation/storekit/transaction/finish()) after delivering content or enabling the service. Keep handling idempotent across app and server updates.

StoreKit normally keeps transaction and subscription information up to date, including after reinstalling the app or moving to a new device. Refresh your app's access model from the verified entitlement results instead of relying only on an in-memory “purchase succeeded” flag. Disabling future renewal is not the same as revocation or current expiration: [`willAutoRenew`](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/willautorenew) describes the **next** period.

Provide a user-initiated restore mechanism. [`AppStore.sync()`](https://developer.apple.com/documentation/storekit/appstore/sync()) forces a refresh and displays an App Store authentication prompt, so call it only after an explicit user action—not routinely at launch or before every entitlement query. After successful synchronization, reevaluate the verified entitlements. Restoration does not turn refunded or revoked purchases into valid access, nor recreate a consumable balance from `currentEntitlements`.

### Testing contexts

[Apple's testing comparison](https://developer.apple.com/documentation/storekit/testing-at-all-stages-of-development-with-xcode-and-the-sandbox) distinguishes the tools and their data:

| Context | StoreKit behavior to verify |
| --- | --- |
| Xcode StoreKit configuration | An active local or synced `.storekit` file supplies local test data. Receipts, JWS transactions, and renewal information are signed by Xcode, not the App Store. A configuration synced from App Store Connect is still local testing. |
| App Store sandbox | Uses product information configured in App Store Connect and App Store-signed test transactions. Purchases do not incur charges; use this environment for App Store server integration tests. |
| TestFlight | **Uses the sandbox for In-App Purchases**. It is a beta-distribution channel, not a third purchase backend or a production purchase test. Follow the TestFlight-specific account instructions when enabling sandbox controls. |
| Production | The shipping App Store purchase flow. Keep production records and server routing separate from sandbox and local test data. |

To move a development run from local testing to sandbox, set the scheme's StoreKit Configuration to **None**, as described in [Setting up StoreKit Testing in Xcode](https://developer.apple.com/documentation/xcode/setting-up-storekit-testing-in-xcode), and complete the [sandbox setup](https://developer.apple.com/documentation/storekit/testing-in-app-purchases-with-sandbox). TestFlight's sandbox designation applies to In-App Purchases; it does not configure your app's own backend.

Account setup is mode-specific:
- **Development-signed iOS/iPadOS apps:** The Sandbox Apple Account entry appears under Settings > Developer after a purchase attempt. Sign in there; there is no need to sign out of the non-Sandbox Apple Account.
- **TestFlight sandbox controls on iOS:** In-App Purchases already use sandbox. To access the Sandbox Apple Account's controls, Apple's guide instructs you to sign out of **Media & Purchases**, then sign in to the Sandbox Apple Account under Settings > Developer. Apple warns that this can affect access to purchased content in production apps and suggests considering a dedicated testing device.

The TestFlight control-setup steps are not a blanket sign-out prerequisite for sandbox purchases, and signing out of Media & Purchases is not signing out of iCloud.

Test product-loading failures, missing identifiers, verified and unverifiable results, pending approval, cancellation, restoration, managed-account assignment and withdrawal, Bundle/Suite state, refunds, and renewal changes. The beta notes also identify StoreKit Testing fixes and remaining limitations. A local success does not establish sandbox or production readiness.

For server-schema changes, use [App Store Server API](AppStoreServerAPI.md) and [App Store Server Notifications](AppStoreServerNotifications.md). For policy and regional eligibility, see [App Store readiness](../guides/app-store-readiness.md) and [Regional distribution](../guides/regional-distribution.md), not an inferred OS-version rule.

## Topics

### In-App Purchase
- [In-App Purchase](https://developer.apple.com/documentation/storekit/in-app-purchase) - Offer content and services in your app across Apple platforms using a Swift-based interface.
- [Understanding StoreKit workflows](https://developer.apple.com/documentation/storekit/understanding-storekit-workflows) - Implement an in-app store with several product types, using StoreKit views.
- [Getting started with In-App Purchase using StoreKit views](https://developer.apple.com/documentation/storekit/getting-started-with-in-app-purchases-using-storekit-views) - Set up an in-app store using SwiftUI and StoreKit views.

### App transaction
- [Supporting business model changes by using the app transaction](https://developer.apple.com/documentation/storekit/supporting-business-model-changes-by-using-the-app-transaction) - Access the app transaction to learn when a customer first purchased an app, to determine the app features they're entitled to.
- **AppTransaction** - Information that represents the customer's purchase of the app, cryptographically signed by the App Store.

### Messages
- **Message** - An instance for receiving and displaying App Store messages in your app.
- [`Message.Reason`](https://developer.apple.com/documentation/storekit/message/reason-swift.struct) - Reasons for the App Store messages.
- **DisplayMessageAction** - An instance that asks StoreKit to display an App Store message, if appropriate.

### Reviews
- [Requesting App Store reviews](https://developer.apple.com/documentation/storekit/requesting-app-store-reviews) - Implement best practices for prompting users to review your app in the App Store.
- **RequestReviewAction** - An instance that tells StoreKit to request an App Store rating or review, if appropriate.
- **SKStoreReviewController** - An object that controls the process of requesting App Store ratings and reviews from customers. *(Deprecated)*

### Recommendations
- [Offering media for sale in your app](https://developer.apple.com/documentation/storekit/offering-media-for-sale-in-your-app) - Allow users to purchase media in the App Store from within your app.
- **SKStoreProductViewController** - A view controller that provides a page where customers can purchase media from the App Store.
- **SKOverlay** - A class that displays an overlay you can use to recommend another app or an App Clip's corresponding full app.

### Background assets extension
- **StoreDownloaderExtension** - An app extension that uses the system implementation to schedule Apple-hosted asset-pack downloads automatically.

### Payment method binding
- **PaymentMethodBinding** - A binding that makes payment methods available in apps for an Apple Account.

### Ad network attribution
- [Ad network attribution](https://developer.apple.com/documentation/storekit/ad-network-attribution) - Validate advertisement-driven app installations.

### External Purchase
- [External Purchase](https://developer.apple.com/documentation/storekit/external-purchase) - Enable qualifying apps to offer external purchases.

### External link account
- [External link account](https://developer.apple.com/documentation/storekit/external-link-account) - Enable qualifying apps to link to an external website for account creation or management.

### Deprecated
- **SKCloudServiceSetupViewController** - A view controller that helps people perform setup for a cloud service, like an Apple Music subscription. *(Deprecated)*
- **SKCloudServiceController** - An object that determines the current capabilities of a person's Music library. *(Deprecated)*

## See Also

### Related Documentation
- [App Store Server API](https://developer.apple.com/documentation/appstoreserverapi) - Manage your customers' App Store transactions from your server.
- [StoreKit Test](https://developer.apple.com/documentation/storekittest) - Create and automate tests in Xcode for your app's subscription and in-app purchase transactions, and SKAdNetwork implementations.
- [App Store Server Notifications](https://developer.apple.com/documentation/appstoreservernotifications) - Monitor In-App Purchase events in real time and learn of unreported external purchase tokens, with server notifications from the App Store.
- [App Store Connect API](https://developer.apple.com/documentation/appstoreconnectapi) - Automate the tasks you perform on the Apple Developer website and in App Store Connect.
- [Advanced Commerce API](https://developer.apple.com/documentation/advancedcommerceapi) - Support In-App Purchases through the App Store for exceptionally large catalogs of custom one-time purchases, subscriptions, and subscriptions with optional add-ons.
- [App Store Receipts](https://developer.apple.com/documentation/appstorereceipts) - Validate app and In-App Purchase receipts with the App Store. *(Deprecated)*

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/StoreKit)*

### Additional reviewed sources

- [iOS and iPadOS 27 release notes — StoreKit](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- [macOS 27 release notes — StoreKit](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes)
- [watchOS 27 release notes — StoreKit](https://developer.apple.com/documentation/watchos-release-notes/watchos-27-release-notes)
- [Transaction](https://developer.apple.com/documentation/storekit/transaction)
- [VerificationResult](https://developer.apple.com/documentation/storekit/verificationresult)
