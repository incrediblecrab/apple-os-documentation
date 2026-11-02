# Apple Pay Merchant Token Management API

Retrieve and manage payment life-cycle events for your Apple Pay merchant tokens.

**Availability:** Apple Pay merchant-token server integration. This is not the App Store Connect API and does not impose an OS 27 app baseline.

## Overview

The Apple Pay Merchant Token Management API is a REST API that enables merchants to get the details of a life-cycle event after receiving a merchant token event notification. Merchants also use this API to inform Apple Pay servers to invalidate their merchant token when it's no longer in use.

A merchant token associates a payment card, merchant, and user. Merchant-specific token issuance depends on the payment request and payment-network support; not every Apple Pay purchase creates one. For example, an automatic-reload request falls back to a device token on an unsupported payment network.

Supply your server's notification base URL through `tokenNotificationURL` on the applicable request:
- PassKit: [`PKAutomaticReloadPaymentRequest`](https://developer.apple.com/documentation/passkit/pkautomaticreloadpaymentrequest), [`PKRecurringPaymentRequest`](https://developer.apple.com/documentation/passkit/pkrecurringpaymentrequest), or [`PKDeferredPaymentRequest`](https://developer.apple.com/documentation/passkit/pkdeferredpaymentrequest).
- Web: [`ApplePayAutomaticReloadPaymentRequest`](https://developer.apple.com/documentation/applepayontheweb/applepayautomaticreloadpaymentrequest), [`ApplePayRecurringPaymentRequest`](https://developer.apple.com/documentation/applepayontheweb/applepayrecurringpaymentrequest), or [`ApplePayDeferredPaymentRequest`](https://developer.apple.com/documentation/applepayontheweb/applepaydeferredpaymentrequest).

When a life-cycle event affects the token, Apple appends `/notification/merchantToken/{eventId}` to that base URL and sends a **GET** request. Retrieve the full event with [Get Details of a Merchant Token Event](https://developer.apple.com/documentation/merchanttokennotificationservices/merchant-token-event-retrieval); the notification is not a transaction payload.

The event response's optional [`MerchantTokenMetadata`](https://developer.apple.com/documentation/merchanttokennotificationservices/merchanttokenmetadata) can carry card art, card metadata, and an [`EncryptedTokenMetadata`](https://developer.apple.com/documentation/merchanttokennotificationservices/encryptedtokenmetadata) object. Its decrypted `data` is a [`TokenMetadata`](https://developer.apple.com/documentation/merchanttokennotificationservices/tokenmetadata) object holding the token's MPAN, its expiration date in `YYMMDD` form, and an `mpanId` that appears only when the MPAN identifier changed. The envelope also carries `publicKeyHash` and a detached PKCS #7 `signature`, plus `ephemeralPublicKey` when your merchant public key uses `EC_v1` or `wrappedKey` when it uses `RSA_v1`.

## Authorization and reliable delivery

Apple uses a notify-then-retrieve model: retrieve an event using its `eventId` while details remain available, which the service documents as **seven days**. Persist incoming work promptly and avoid treating a notification alone as the full event.

Merchant-to-Apple API calls require **mutual TLS**. Device-to-merchant usage-information retrieval instead uses TLS and the merchant-provided `authenticationToken`. Keep these authorization paths separate from App Store Connect JWTs and from Apple Pay payment processing.

For recurring, deferred, and automatic-reload arrangements, provide the notification URL through the corresponding payment-request API. Handle duplicate events idempotently and retain a retry path for transient retrieval failures. Inspect [`ErrorResponse`](https://developer.apple.com/documentation/merchanttokennotificationservices/errorresponse); authentication or certificate errors require configuration repair, not endless retries.

The inbound notification endpoint requires TLS 1.2 or later and the documented network configuration. Return `200` when you receive the notification, even if the token or event is unknown; return `500` if you cannot process the notification request. Apple immediately retries up to three times after a non-`200` response. Persist work before acknowledging it so a later event-fetch failure does not lose the notification.

The Apple-hosted event, invalidation, metadata, and usage-information operations require `Content-Type` and `x-request-id`. Follow each endpoint's response contract: invalidation succeeds with **`204` and no body**, rather than a JSON object or a refund. It prevents future transaction authorizations using that token.

## Merchant-token usage information

The related [Usage Information API](ApplePayMerchantTokenUsageInformationAPI.md) supplies the customer-visible package. Its delivery workflow uses:

- [Retrieve Merchant Token Public Key](https://developer.apple.com/documentation/merchanttokennotificationservices/retrieve-merchant-token-public-key)
- [MerchantToken Usage Data Availability Notification](https://developer.apple.com/documentation/merchanttokennotificationservices/merchanttoken-usage-data-availability-notification)
- [Get MerchantToken Usage Information Package](https://developer.apple.com/documentation/merchanttokennotificationservices/get-merchanttoken-usage-information-package)

Build the package as [Adding merchant token usage information](https://developer.apple.com/documentation/applepaymerchanttokenmanagementapi/adding-merchant-token-usage-information) describes: a `usageInformation.json` file, images, and optional `.lproj` localizations, at most 5 MB in total, compressed into a zip file.

Usage information describes payment activity; it does not itself authorize a charge or invalidate a token.

A public-key request can return `202` while the owner's device has not supplied the key; wait for the corresponding notification rather than parsing this as a completed key response. A `409` reports conflicting metadata and calls for updating `tokenNotificationURL`. The event model's `eventType` values are `UNLINK`, `UPDATED_METADATA`, `UPDATED_CARD_ART`, `UPDATED_MERCHANT_TOKEN_PUBLIC_KEY`, and `UPDATED_MERCHANT_TOKEN`.

## Topics

### Merchant token notification handling
- [Receiving and handling merchant token notifications](https://developer.apple.com/documentation/applepaymerchanttokenmanagementapi/receiving-and-handling-merchant-token-notifications) - Implement an endpoint to receive and handle merchant token life-cycle updates from Apple Pay.
- [Send Merchant Token Event](https://developer.apple.com/documentation/merchanttokennotificationservices/send-merchant-token-event) - Receive and handle merchant token life-cycle updates from Apple Pay.
- [Update Merchant Metadata](https://developer.apple.com/documentation/merchanttokennotificationservices/update-merchant-metadata) - Change a merchant token's notification URL.

### Merchant token event retrieval
- [Get Details of a Merchant Token Event](https://developer.apple.com/documentation/merchanttokennotificationservices/merchant-token-event-retrieval) - Get the details of a merchant token event after receiving a notification.
- [`MerchantTokenEventResponse`](https://developer.apple.com/documentation/merchanttokennotificationservices/merchanttokeneventresponse) - A response body that contains information about a life-cycle event for a merchant token.
- [`MerchantTokenMetadata`](https://developer.apple.com/documentation/merchanttokennotificationservices/merchanttokenmetadata) - The card information related to a merchant token, including its card art and metadata.
- [`CardArt`](https://developer.apple.com/documentation/merchanttokennotificationservices/cardart) - Data for displaying art to represent a card.
- [`CardMetadata`](https://developer.apple.com/documentation/merchanttokennotificationservices/cardmetadata) - Data about the card, including its expiration date and suffix.
- [`EncryptedTokenMetadata`](https://developer.apple.com/documentation/merchanttokennotificationservices/encryptedtokenmetadata) - Encrypted data about the merchant token, including its MPAN and expiration date.
- [`TokenMetadata`](https://developer.apple.com/documentation/merchanttokennotificationservices/tokenmetadata) - The decrypted form of that data: MPAN, expiration date, and a changed MPAN identifier when there is one.

### Merchant token invalidation
- [Invalidate a Merchant Token](https://developer.apple.com/documentation/merchanttokennotificationservices/unlinking-merchanttoken) - Invalidate a merchant token associated with your merchant identifier, making it invalid for future transaction authorizations.
- [`MerchantTokenUnlinkRequest`](https://developer.apple.com/documentation/merchanttokennotificationservices/merchanttokenunlinkrequest) - The request body you use to invalidate a merchant token.

### Error handling
- [`ErrorResponse`](https://developer.apple.com/documentation/merchanttokennotificationservices/errorresponse) - Structured status, substatus, and message fields used by the documented endpoint responses.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MerchantTokenNotificationServices)*
