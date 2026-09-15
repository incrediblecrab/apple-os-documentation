# PassKit (Apple Pay and Wallet)

Process Apple Pay payments in your app, and create and distribute passes for the Wallet app.

**Framework SDK availability:** iOS 6.0+ | iPadOS 6.0+ | Mac Catalyst 13.0+ | macOS 11.0+ | visionOS 1.0+ | watchOS 2.0+. Individual payment, pass, and identity features have later requirements.

## Overview

The **PassKit** framework lets you:

- Add Apple Pay to your app
- Manage passes in the user's Wallet app

**Apple Pay** is a secure and easy way for users to make purchases in stores, in apps, and on the web. When you use PassKit APIs to support Apple Pay in your iOS and watchOS apps, your users can purchase real-world goods and services, or donate to nonprofit organizations, without ever leaving your app.

**Note:** To add Apple Pay to your web applications, see [Apple Pay on the Web](ApplePayontheWeb.md).

For digital goods and services delivered within the app, see [In-App Purchase](https://developer.apple.com/documentation/storekit/in-app-purchase) and the applicable [App Store readiness guidance](../guides/app-store-readiness.md).

The **Wallet** app allows users to organize their boarding passes, tickets, gift cards, and loyalty cards. It also lets users manage their payment cards for Apple Pay. Using the PassKit framework, you can add passes to Wallet and provide time and location information for relevance. For updates, push notifications prompt the device to retrieve a newly signed pass; the notification itself is not the replacement pass.

## Integration boundaries

Use the [Apple Pay](https://developer.apple.com/documentation/passkit/apple-pay) APIs for payment requests and authorization, and [Wallet Passes](WalletPasses.md) for pass packages and updates. Device Wallet features do not automatically establish new public pass keys or PassKit methods.

[Native Apple Pay setup](https://developer.apple.com/documentation/passkit/setting-up-apple-pay) requires a merchant identifier, a payment processing certificate, and the Apple Pay capability. Web integration adds merchant validation and domain configuration. Coordinate payment-token processing with your processor; a sample that leaves processing as a placeholder is not a working charge implementation.

Ordinary pass-library access is scoped by the Wallet capability and the [Pass Type IDs entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.pass-type-identifiers) to the team's permitted pass types. It is not unrestricted access to every payment card or identity document in Wallet.

For recurring, deferred, and automatic-reload payments, consult the relevant request type and capability checks. Merchant tokens require a separate server lifecycle: [Merchant Token Management](MerchantTokenNotificationServices.md) handles events and invalidation, while [Merchant Token Usage Information](ApplePayMerchantTokenUsageInformationAPI.md) describes customer-visible payment history.

Do not treat presentation or dismissal of a payment sheet as proof that a payment processor accepted a charge. Handle authorization results, cancellation, and processing errors, and keep pass updates distinct from payment fulfillment. Check individual symbols for availability; the framework's platform header does not promise every Apple Pay or Wallet feature on every device.

## OS 27: payment-option merchandising

[`ApplePayMerchandisingView`](https://developer.apple.com/documentation/passkit/applepaymerchandisingview) is a SwiftUI view with **iOS 27 and iPadOS 27** availability in the reviewed reference. It displays promotional payment information, not a payment authorization result.

Its initializer accepts a `Decimal` amount, `Locale.Currency`, and `Locale.Region`. [`ApplePayMerchandisingAction`](https://developer.apple.com/documentation/passkit/applepaymerchandisingaction), [`ApplePayMerchandisingStyle`](https://developer.apple.com/documentation/passkit/applepaymerchandisingstyle), and [`ApplePayMerchandisingPartnerConfiguration`](https://developer.apple.com/documentation/passkit/applepaymerchandisingpartnerconfiguration) configure the interaction and presentation. Provide an appropriate fallback view for cases where the content cannot render; do not infer that every partner or payment option is available in every region.

## Topics

### Apple Pay support
- [Apple Pay](https://developer.apple.com/documentation/passkit/apple-pay) - Request and process Apple Pay payments in your app.

### Wallet support
- [Wallet](https://developer.apple.com/documentation/passkit/wallet) - Manage tickets, boarding passes, payment cards and other passes in the Wallet app.

## See Also

### Related Documentation
- [Wallet Passes](https://developer.apple.com/documentation/walletpasses) - Create, distribute, and update passes for the Wallet app.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/PassKit)*
