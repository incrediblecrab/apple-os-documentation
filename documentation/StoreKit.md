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

## Topics

### In-App Purchase
- [In-App Purchase](https://developer.apple.com/documentation/storekit/in-app_purchase) - Offer content and services in your app across Apple platforms using a Swift-based interface.
- [Understanding StoreKit workflows](https://developer.apple.com/documentation/storekit/understanding_storekit_workflows) - Implement an in-app store with several product types, using StoreKit views.
- [Getting started with In-App Purchase using StoreKit views](https://developer.apple.com/documentation/storekit/getting_started_with_in-app_purchase_using_storekit_views) - Set up an in-app store using SwiftUI and StoreKit views.

### App transaction
- [Supporting business model changes by using the app transaction](https://developer.apple.com/documentation/storekit/supporting_business_model_changes_by_using_the_app_transaction) - Access the app transaction to learn when a customer first purchased an app, to determine the app features they're entitled to.
- **AppTransaction** - Information that represents the customer's purchase of the app, cryptographically signed by the App Store.

### Messages
- **Message** - An instance for receiving and displaying App Store messages in your app.
- **Reason** - Reasons for the App Store messages.
- **DisplayMessageAction** - An instance that asks StoreKit to display an App Store message, if appropriate.

### Reviews
- [Requesting App Store reviews](https://developer.apple.com/documentation/storekit/requesting_app_store_reviews) - Implement best practices for prompting users to review your app in the App Store.
- **RequestReviewAction** - An instance that tells StoreKit to request an App Store rating or review, if appropriate.
- **SKStoreReviewController** - An object that controls the process of requesting App Store ratings and reviews from customers. *(Deprecated)*

### Recommendations
- [Offering media for sale in your app](https://developer.apple.com/documentation/storekit/offering_media_for_sale_in_your_app) - Allow users to purchase media in the App Store from within your app.
- **SKStoreProductViewController** - A view controller that provides a page where customers can purchase media from the App Store.
- **SKOverlay** - A class that displays an overlay you can use to recommend another app or an App Clip's corresponding full app.

### Background assets extension
- **StoreDownloaderExtension** - An app extension that uses the system implementation to schedule Apple-hosted asset-pack downloads automatically. *(Beta)*

### Payment method binding
- **PaymentMethodBinding** - A binding that makes payment methods available in apps for an Apple ID.

### Ad network attribution
- [Ad network attribution](https://developer.apple.com/documentation/storekit/ad_network_attribution) - Validate advertisement-driven app installations.

### External Purchase
- [External Purchase](https://developer.apple.com/documentation/storekit/external_purchase) - Enable qualifying apps to offer external purchases.

### External link account
- [External link account](https://developer.apple.com/documentation/storekit/external_link_account) - Enable qualifying apps to link to an external website for account creation or management.

### Deprecated
- **SKCloudServiceSetupViewController** - A view controller that helps people perform setup for a cloud service, like an Apple Music subscription. *(Deprecated)*
- **SKCloudServiceController** - An object that determines the current capabilities of a person's Music library. *(Deprecated)*

### Structures
- **AppStoreMerchandisingKind** - *(Beta)*

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