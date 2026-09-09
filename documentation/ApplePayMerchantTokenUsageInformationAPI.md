# Apple Pay Merchant Token Usage Information API

Describe merchant-token payment activity for presentation to the customer in Wallet.

**Availability:** An Apple Pay merchant-token service and package schema, not an OS 27-only framework. DocC versions the device retrieval operation as Merchant Token Management API 1.0.12, without an OS deployment minimum. Client availability depends on the relevant Apple Pay payment-request APIs and merchant-token support.

## Overview

Use this schema to supply context for an existing merchant token: past and upcoming payments, recurring or deferred payment details, automatic reloads, and payment issues. It complements the [Apple Pay Merchant Token Management API](MerchantTokenNotificationServices.md), which handles token events, public-key retrieval, availability notifications, and invalidation.

Providing usage information does not authorize a charge, create an App Store subscription, or replace your payment processor. Keep the information consistent with the actual merchant-token payment lifecycle.

## Prerequisites and authorization

Set up the appropriate Apple Pay merchant integration and token-notification workflow for recurring, deferred, or automatic-reload payments. Use the documented request types in [PassKit](PassKit.md) or [Apple Pay on the Web](ApplePayontheWeb.md); supplying a generic Wallet pass is not sufficient. Merchant-specific tokens depend on payment-network support. For example, the [automatic-reload request](https://developer.apple.com/documentation/passkit/pkautomaticreloadpaymentrequest) falls back to a device token when that support is absent.

The management service distinguishes two trust relationships:

- Merchant-to-Apple API calls require **mutual TLS**.
- A customer's device retrieves usage information from your merchant server over **TLS**, using `Authorization: ApplePayMerchantTokenUsageInformation {authenticationToken}`.

Authenticate and authorize the device request for the relevant merchant token. Do not publish usage packages as unauthenticated customer transaction histories.

## Build and deliver a package

1. Follow [Adding merchant token usage information](https://developer.apple.com/documentation/applepaymerchanttokenmanagementapi/adding-merchant-token-usage-information) to assemble `usageInformation.json`, images, and optional localization resources. The uncompressed source must not exceed **5 MB**; package it as a ZIP file.
2. Retrieve the token owner's public key through [Retrieve Merchant Token Public Key](https://developer.apple.com/documentation/merchanttokennotificationservices/retrieve-merchant-token-public-key). A `200` response supplies the key and `supportedCiphersuite`; `202` means the key is not yet available, and Apple will notify your `tokenNotificationURL` when it is ready.
3. Implement the encryption contract in [`GetMerchantTokenUsageInformationPackageResponse`](https://developer.apple.com/documentation/merchanttokennotificationservices/getmerchanttokenusageinformationpackageresponse), including its HPKE mode, key relationship, and token-specific `info` value. A plain ZIP or arbitrary JSON encoding is not the encrypted response.
4. Use [MerchantToken Usage Data Availability Notification](https://developer.apple.com/documentation/merchanttokennotificationservices/merchanttoken-usage-data-availability-notification) to notify Apple that an update is available. Its [`MerchantTokenUsageMetadata`](https://developer.apple.com/documentation/merchanttokennotificationservices/merchanttokenusagemetadata) carries encrypted retrieval metadata, including the `webServiceURL` and `authenticationToken`, and the merchant's public key.
5. Serve [Get MerchantToken Usage Information Package](https://developer.apple.com/documentation/merchanttokennotificationservices/get-merchanttoken-usage-information-package) on your merchant server. The **user's device**, not your server, calls this operation using the `webServiceURL` supplied in metadata.

Localization can replace strings and images. Date/time fields use their standard formats; localization does not convert a monetary amount into a different currency.

The source-size ceiling and response-schema limits are separate. The current encrypted-package schema also specifies `maximumLength: 4000` for its `data` string. Do not interpret the 5 MB source ceiling as permission to send a 5 MB encrypted response, or invent a larger transport limit.

### Required usage data

The `UsageInformation` schema requires `schemaVersion` (currently `1`), `merchantName`, `merchantTokenIdentifier`, and `modificationDate`. The token identifier must match the token whose information is being served. Optional `pastPayments` and `upcomingPayments` arrays use the documented payment objects; an optional `expirationDate` may be at most one year in the future.

`CurrencyAmount` uses a string-valued `amount` and a three-character ISO 4217 currency code. An `UpcomingPayment` needs the details object corresponding to its `paymentType`: recurring, deferred, or automatic reload. Those conditional requirements still apply even though the individual details properties are marked optional in the general object schema.

## Topics

- [`UsageInformation`](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/usageinformation) — The package's merchant-token usage model.
- [`CurrencyAmount`](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/currencyamount) — Represent an amount in its currency.
- [`PastPayment`](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/pastpayment) and [`UpcomingPayment`](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/upcomingpayment) — Describe completed and expected payment activity.
- [`RecurringPaymentDetails`](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/recurringpaymentdetails) — Describe a recurring payment arrangement.
- [`AutomaticReloadPaymentDetails`](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/automaticreloadpaymentdetails) — Describe reload behavior.
- [`DeferredPaymentDetails`](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/deferredpaymentdetails) — Describe a payment deferred until a later event.
- [`PaymentIssueDetails`](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/paymentissuedetails) — Explain a payment issue without representing it as a successful charge.

## Failure handling

Validate the package's schema, size, assets, and localization before announcing availability. Verify that the private key used for the encrypted response corresponds to the public key supplied in the availability notification.

Use the required `Content-Type` and `x-request-id` headers for the Apple-hosted operations. Handle their HTTP results and [`ErrorResponse`](https://developer.apple.com/documentation/merchanttokennotificationservices/errorresponse) bodies according to each endpoint. A public-key lookup's `409` identifies a metadata conflict: repair the notification URL with [Update Merchant Metadata](https://developer.apple.com/documentation/merchanttokennotificationservices/update-merchant-metadata), rather than treating it as a missing key or a generic retry.

Separate certificate/authentication failures from transient delivery failures; retry transient work with bounds rather than rotating credentials or resending indefinitely. Do not log tokens, private keys, or unredacted payment histories.

The device retrieval contract documents `200` with an encrypted package, `401` for an unauthorized request, and `404` when not found. Return the appropriate result instead of exposing another token's package as a fallback.

Test the device-to-merchant retrieval path independently from merchant-to-Apple notifications. A successfully accepted availability notification alone does not prove that the device can authenticate, download, and decrypt the package.

## Sources

- [Apple Pay Merchant Token Usage Information API](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation)
- [Apple Pay Merchant Token Management API](https://developer.apple.com/documentation/merchanttokennotificationservices)
- [Package construction](https://developer.apple.com/documentation/applepaymerchanttokenmanagementapi/adding-merchant-token-usage-information)
- [Encrypted package response](https://developer.apple.com/documentation/merchanttokennotificationservices/getmerchanttokenusageinformationpackageresponse)
- [Device retrieval operation](https://developer.apple.com/documentation/merchanttokennotificationservices/get-merchanttoken-usage-information-package)
- [Device retrieval DocC data](https://developer.apple.com/tutorials/data/documentation/merchanttokennotificationservices/get-merchanttoken-usage-information-package.json)
- [UsageInformation DocC data](https://developer.apple.com/tutorials/data/documentation/applepaymerchanttokenusageinformation/usageinformation.json)
