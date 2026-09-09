# StoreKit Test

Create and automate tests in Xcode for your app's subscription and in-app purchase transactions, and SKAdNetwork implementations.

**Platforms:** iOS 14.0+ | iPadOS 14.0+ | Mac Catalyst 14.0+ | macOS 11.0+ | tvOS 14.0+ | visionOS 1.0+ | watchOS 7.4+

## Overview

The StoreKitTest framework makes StoreKit testing in Xcode available for automation. Use this framework to write unit tests and continuous integration tests. Use SKTestSession and SKAdTestSession to control the test environment.

For testing in-app purchase transactions, use SKTestSession. Each instance of SKTestSession gives you access to the same settings you manually change for StoreKit testing in Xcode. Use this class to test a variety of in-app purchase scenarios, such as subscription renewals and Ask to Buy transactions, and maintain control over the transactions in the testing environment.

For testing ad impressions and postbacks, use SKAdTestSession. Each instance of SKAdTestSession holds a set of test postbacks that you create and can use in multiple unit tests. Ad networks that use SKAdNetwork APIs can use this class to validate the ad impressions that they sign, and test receiving postbacks on their server. Advertised apps can test their conversion value updates.

Apple's original StoreKit-testing baseline is Xcode 12 with macOS 10.15 or later for iOS, watchOS, and tvOS tests, and macOS 11 or later for macOS app tests. These historical minimums do not override the host requirements of a newer Xcode; see [Xcode](Xcode.md) for the Xcode 27 requirements.

**Related session from WWDC20**

[Session 10659: Introducing StoreKit testing in Xcode](https://developer.apple.com/videos/play/wwdc2020/10659/)

## Topics

### StoreKit transaction testing
- [Setting up StoreKit Testing in Xcode](https://developer.apple.com/documentation/xcode/setting-up-storekit-testing-in-xcode.md) - Prepare your test environment to test in-app purchases with data you configure locally.
- **SKTestSession** - The controls and environment configuration you use to test StoreKit transactions in Xcode.
- **SKTestTransaction** - A transaction that occurs in the testing environment.

### StoreKit transaction testing errors
- **SKTestErrorDomain** - A constant that represents the domain for error codes in the testing environment.
- **SKTestError** - Information about an error that the testing environment returns.

### Ad impression and postback testing
- [Testing and validating ad impression signatures and postbacks for SKAdNetwork](https://developer.apple.com/documentation/storekittest/testing-and-validating-ad-impression-signatures-and-postbacks-for-skadnetwork.md) - Validate your ad impressions and test your postbacks by creating unit tests using the StoreKit Test framework.
- **SKAdTestSession** - The class you use to test ad impressions and postbacks in Xcode.
- **SKAdTestPostback** - A test postback that contains ad conversion information in the testing environment.
- **SKAdTestPostbackResponse** - The status and error information for a postback that the system sends in the testing environment.
- **SKAdTestPostbackVersion** - A constant that indicates the postback version.

### Ad impression and postback errors
- **SKAdTestErrorDomain** - A string that identifies the error domain for SKAdNetwork testing in the testing environment.
- **SKAdTestError** - An error the testing environment returns for SKAdNetwork testing errors.

### Structures
- **StoreKitAppStoreSyncAPI**
- **StoreKitAppTransactionAPI**
- **StoreKitLoadProductsAPI**
- **StoreKitManageSubscriptionsAPI**
- **StoreKitOfferCodeRedeemAPI**
- **StoreKitPurchaseAPI**
- **StoreKitRefundRequestAPI**
- **StoreKitSubscriptionStatusAPI**
- **StoreKitVerificationAPI**

### Enumerations
- **SKTestFailures**

### Protocols
- **FailableStoreKitAPI**
- **SKTestFailure**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/StoreKitTest)*
