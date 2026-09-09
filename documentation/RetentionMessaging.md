# Retention Messaging API

Provide a reason for customers to stay subscribed with a preconfigured message that you can choose in real time, appropriate to the product and locale.

**Availability:** Access-controlled, pre-release server service. Messages display on iOS/iPadOS 15.1+, macOS 14+, and visionOS 1+; they do not universally require OS 27.

## Overview

The **Retention Messaging API** is a server-to-server service that enables you to select which message the system displays to customers when they view a subscription details page and might cancel. You upload and configure messages in advance for products and locales.

**Important:** To learn more about this pre-release and express interest, see [Request access to the Retention Messaging API](https://developer.apple.com/contact/request/retention-messaging-api/).

Your messages remind customers about the features or content they have access to with the subscription, or show them alternative offers. There are four types of retention messages:

- A text-based message, optionally with bullet points
- A text-based message with an image, optionally with bullet points
- A switch-plan message, which contains text and a suggested subscription the customer may choose to switch to
- A promotional-offer message, which contains text and a promotional offer to continue service at a discounted price, either at the same or a different tier of service

The system displays the message on its cancellation-confirmation interface. The customer can continue canceling, keep the subscription, or choose an available offer. Providing a message does not authorize your server to prevent cancellation or change a subscription without the customer's choice.

You use the API to select retention messages for customers in two ways:

- By configuring default messages, which are text-based messages, with or without an image, that apply to specific products and locales.
- By choosing a retention message in real time when the App Store calls your server, with configured default messages as fallback.

**A product/locale without a default message does not display a retention message.** Defaults are required for the real-time flow, not merely an optional optimization.

### Upload images and messages

Upload text and optional images using [Upload Image](https://developer.apple.com/documentation/retentionmessaging/upload-image) and [Upload Message](https://developer.apple.com/documentation/retentionmessaging/upload-message). Both the message and any image must reach `APPROVED` before display. Switch-plan and promotional-offer messages use text without images.

Don't upload content that is misleading or inaccurate.

### Configure default retention messages

The simplest integration configures product/locale defaults after uploading messages. See [Setting up retention messages](https://developer.apple.com/documentation/retentionmessaging/setting-up-retention-messages).

The default messaging option supports only text-based messages with or without an image. For retention messages that include offers, use the real-time messaging flow.

### Provide real-time messages, including offers

The real-time messaging flow calls your server when an active subscriber views a subscription details page with a Cancel button. For example, customers might consider canceling on the Apple Account > Subscriptions page, or when viewing the subscription details page on the App Store.

The real-time call informs you about the subscription, including the original transaction ID, and the customer's locale. You respond by selecting an appropriate preconfigured message for the system to display. You can choose from all the retention message types, including those with switch-plan or promotional offers.

Follow these steps to implement the real-time flow:

1. Upload messages and images, and check their approval state.
2. Configure defaults for each product and locale.
3. Implement your HTTPS endpoint and use [Configure Realtime URL](https://developer.apple.com/documentation/retentionmessaging/configure-realtime-url) for sandbox setup.
4. Pass the sandbox [performance test](https://developer.apple.com/documentation/retentionmessaging/initiate-performance-test) before configuring a production URL.
5. [Verify and respond to requests](https://developer.apple.com/documentation/retentionmessaging/responding-to-realtime-retention-messaging-requests) using approved message identifiers.

### Verification, latency, and service changes

Configuration and upload calls require authorization JWTs. Follow the [JWT guide](https://developer.apple.com/documentation/appstoreserverapi/generating-json-web-tokens-for-api-requests) linked by the endpoints and keep signing keys on your server. API access approval remains a separate prerequisite; a `404` from Configure Realtime URL can indicate that the developer account lacks access.

Verify the incoming `signedPayload` JWS before trusting its subscription, environment, or locale. Base64URL decoding alone is not verification. Return the documented `RealtimeResponseBody` with HTTP `200`; the production deadline is **700 ms**. The endpoint requires a valid certificate and TLS 1.2. Slow or unsuccessful responses use the default message.

Image and message uploads use `PUT` but are not idempotent: reusing an existing identifier returns `409`. After an uncertain upload outcome, reconcile the identifier with the corresponding list endpoint before retrying. Handle `429` using the documented rate limits; this API's `Retry-After` value is a UNIX timestamp in **milliseconds**, not a relative delay in seconds.

The [changelog](https://developer.apple.com/documentation/retentionmessaging/retention-messaging-changelog) records service changes independently of OS releases: version 1.4 added real-time URL management and bullet points in March 2026; version 1.5 added `billingPlanType` for alternate products in April. Since May 2026, Apple recommends `api.storekit.apple.com` and `api.storekit-sandbox.apple.com`; the older `itunes.apple.com` domains remain supported.

## Topics

### Essentials
- [Setting up retention messages](https://developer.apple.com/documentation/retentionmessaging/setting-up-retention-messages) - Configure messages and defaults.
- [Identifying rate limits](https://developer.apple.com/documentation/retentionmessaging/identifying-rate-limits) - Handle endpoint rate limits.
- [Retention Messaging API changelog](https://developer.apple.com/documentation/retentionmessaging/retention-messaging-changelog) - Service changes.

### Image configuration
- [Upload Image](https://developer.apple.com/documentation/retentionmessaging/upload-image) - Upload an image.
- [Delete Image](https://developer.apple.com/documentation/retentionmessaging/delete-image) - Delete an image.
- [Get Image List](https://developer.apple.com/documentation/retentionmessaging/get-image-list) - Check identifiers and approval states.
- **GetImageListResponse** - A response that contains status information for all images.
- **GetImageListResponseItem** - An image identifier and state information for an image.

### Message configuration
- [Upload Message](https://developer.apple.com/documentation/retentionmessaging/upload-message) - Upload a message.
- [Delete Message](https://developer.apple.com/documentation/retentionmessaging/delete-message) - Delete a message.
- [Get Message List](https://developer.apple.com/documentation/retentionmessaging/get-message-list) - Check message identifiers and approval states.
- **UploadMessageRequestBody** - Message text, optional bullet points, and an optional image reference.
- **UploadMessageImage** - The definition of an image with its alternative text.
- **GetMessageListResponse** - A response that contains status information for all messages.
- **GetMessageListResponseItem** - A message identifier and status information for a message.

### Default message configuration
- [Configure Default Message](https://developer.apple.com/documentation/retentionmessaging/configure-default-message) - Set a product/locale default.
- [Get Default Message](https://developer.apple.com/documentation/retentionmessaging/get-default-message) - Inspect the configured default.
- [Delete Default Message](https://developer.apple.com/documentation/retentionmessaging/delete-default-message) - Delete a default.
- **DefaultConfigurationRequest** - The request body that contains the default configuration information.

### Real-time retention messaging
- [Setting up your Get Retention Message endpoint](https://developer.apple.com/documentation/retentionmessaging/setting-up-retention-messaging-endpoint) - Implement and register your endpoint.
- [Responding to real-time retention messaging requests](https://developer.apple.com/documentation/retentionmessaging/responding-to-realtime-retention-messaging-requests) - Verify requests and select messages.
- [Configure Realtime URL](https://developer.apple.com/documentation/retentionmessaging/configure-realtime-url) - Register sandbox/production URLs.
- [Get Realtime URL](https://developer.apple.com/documentation/retentionmessaging/get-realtime-url) - Inspect the registered URL.
- [Delete Realtime URL](https://developer.apple.com/documentation/retentionmessaging/delete-realtime-url) - Remove a URL from real-time use.
- **RealtimeRequestBody** - The request body the App Store server sends to your Get Retention Message endpoint.
- **DecodedRealtimeRequestBody** - The decoded request body the App Store sends to your server to request a real-time retention message.
- **RealtimeResponseBody** - A response you provide to choose, in real time, a retention message the system displays to the customer.

### Server performance testing
- [Initiate Performance Test](https://developer.apple.com/documentation/retentionmessaging/initiate-performance-test) - Test the sandbox endpoint.
- [Get Performance Test Results](https://developer.apple.com/documentation/retentionmessaging/get-performance-test-results) - Inspect the test outcome.

### Data types
- [Data types](https://developer.apple.com/documentation/retentionmessaging/data-types) - Request and response types.

### Error information
- [Error codes](https://developer.apple.com/documentation/retentionmessaging/error-codes) - Endpoint error information.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/RetentionMessaging)*
