# Apple Pay Merchant Token Management API

Retrieve and manage payment life-cycle events for your Apple Pay merchant tokens.

**Platforms:** App Store Connect API 1.0+

## Overview

The Apple Pay Merchant Token Management API is a REST API that enables merchants to get the details of a life-cycle event after receiving a merchant token event notification. Merchants also use this API to inform Apple Pay servers to invalidate their merchant token when it's no longer in use.

A merchant token associates a payment card, merchant, and user. Apple Pay issues a merchant token when a customer initiates a purchase using Apple Pay in your app or on your website. When your app or website creates a payment request for a recurring payment or an automatic-reload payment, it passes your server's notification URL in the `tokenNotificationURL` parameter. For more information about `tokenNotificationURL`, see **PKAutomaticReloadPaymentRequest**, **PKRecurringPaymentRequest**, **ApplePayAutomaticReloadPaymentRequest**, and **ApplePayRecurringPaymentRequest**.

If a life-cycle event affects the token — for example, the card's expiration date changes, or the user or issuer deletes the token — Apple Pay sends you a notification with an event identifier to that `tokenNotificationURL`. You retrieve the details of the event by calling Get Details of a Merchant Token Event with the event identifier.

## Topics

### Merchant token notification handling
- [Receiving and handling merchant token notifications](https://developer.apple.com/documentation/MerchantTokenNotificationServices/receiving_and_handling_merchant_token_notifications) - Implement an endpoint to receive and handle merchant token life-cycle updates from Apple Pay.
- **Send Merchant Token Event** - Receive and handle merchant token life-cycle updates from Apple Pay.

### Merchant token event retrieval
- **Get Details of a Merchant Token Event** - Get the details of a merchant token event after receiving a notification.
- **MerchantTokenEventResponse** - A response body that contains information about a life-cycle event for a merchant token.
- **MerchantTokenMetadata** - The card information related to a merchant token, including its card art and metadata.
- **CardArt** - Data for displaying art to represent a card.
- **CardMetadata** - Data about the card, including its expiration date and suffix.

### Merchant token invalidation
- **Invalidate a Merchant Token** - Invalidate a merchant token associated with your merchant identifier, making it invalid for future transaction authorizations.
- **MerchantTokenUnlinkRequest** - The request body you use to invalidate a merchant token.

### Error handling
- **ErrorResponse** - Information about errors that the API returns in the response body whenever an API request is unsuccessful.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MerchantTokenNotificationServices)*