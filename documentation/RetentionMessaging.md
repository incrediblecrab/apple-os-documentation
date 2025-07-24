# Retention Messaging API

Provide a reason for customers to stay subscribed with a preconfigured message that you can choose in real time, appropriate to the product and locale.

**Platforms:** Retention Messaging API 1.0+

## Overview

The **Retention Messaging API** is a server-to-server service that enables you to select which message the system displays to customers when they view a subscription details page and might cancel. You upload and configure messages in advance for products and locales.

**Important:** To learn more about this pre-release and express interest, see [Request access to the Retention Messaging API](https://developer.apple.com/contact/request/retention-messaging-api/).

Your messages remind customers about the features or content they have access to with the subscription, or show them alternative offers. There are four types of retention messages:

- A text-based message
- A text-based message with an image
- A switch-plan message, which contains text and a suggested subscription the customer may choose to switch to
- A promotional-offer message, which contains text and a promotional offer to continue service at a discounted price, either at the same or a different tier of service

The system displays the retention message to the customer after they tap Cancel Subscription on a subscription details page. The system displays a Confirm Cancellation page where the customer can continue to cancel by tapping Cancel Subscription. They can also tap Don't Cancel, or, depending on the retention message, they can choose to redeem an offer or subscribe to a subscription you suggest.

You use the API to select retention messages for customers in two ways:

- By configuring default messages, which are text-based messages, with or without an image, that apply to specific products and locales.
- By choosing a retention message in real time, when you respond to a server-to-server call from the App Store server.

### Upload images and messages

All retention messages start with text that you upload, and optional images. For more information, see [Upload Image](https://developer.apple.com/documentation/retentionmessaging/upload_image) and [Upload Message](https://developer.apple.com/documentation/retentionmessaging/upload_message).

Don't upload content that is misleading or inaccurate.

### Configure default retention messages

The simplest way to use this API is to configure default messages. Start by uploading images and messages. Then, specify the messages to use as default messages. For more information, see [Setting up retention messages](https://developer.apple.com/documentation/retentionmessaging/setting_up_retention_messages).

The default messaging option supports only text-based messages with or without an image. For retention messages that include offers, use the real-time messaging flow.

### Provide real-time messages, including offers

The real-time messaging flow calls your server when an active subscriber views a subscription details page with a Cancel button. For example, customers might consider canceling on the Apple Account > Subscriptions page, or when viewing the subscription details page on the App Store.

The real-time call informs you about the subscription, including the original transaction ID, and the customer's locale. You respond by selecting an appropriate preconfigured message for the system to display. You can choose from all the retention message types, including those with switch-plan or promotional offers.

Follow these steps to implement the real-time flow:

1. Upload and prepare your retention messages. For more information, see [Setting up retention messages](https://developer.apple.com/documentation/retentionmessaging/setting_up_retention_messages).
2. Optionally, configure default retention messages. The system uses default messages as a fallback if a real-time call to your server fails for any reason.
3. Implement the Get Retention Message endpoint on your server. For more information, see [Setting up your Get Retention Message endpoint](https://developer.apple.com/documentation/retentionmessaging/setting_up_your_get_retention_message_endpoint).
4. Respond to App Store requests by selecting a retention message to display in real-time. For more information, see [Responding to real-time retention messaging requests](https://developer.apple.com/documentation/retentionmessaging/responding_to_real-time_retention_messaging_requests).

## Topics

### Essentials
- [Setting up retention messages](https://developer.apple.com/documentation/retentionmessaging/setting_up_retention_messages) - Upload images and messages for retention messaging, configure default messages, and complete the setup for promotional-offer and switch-plan messages.
- [Identifying rate limits](https://developer.apple.com/documentation/retentionmessaging/identifying_rate_limits) - Recognize the rate limits that apply to Retention Messaging API endpoints, and handle them in your code.
- [Retention Messaging API changelog](https://developer.apple.com/documentation/retentionmessaging/retention_messaging_api_changelog) - Learn about new features and updates in the Retention Messaging API.

### Image configuration
- [Upload Image](https://developer.apple.com/documentation/retentionmessaging/upload_image) - Upload an image to use for retention messaging.
- [Delete Image](https://developer.apple.com/documentation/retentionmessaging/delete_image) - Delete a previously uploaded image.
- [Get Image List](https://developer.apple.com/documentation/retentionmessaging/get_image_list) - Get the image identifier and state for all uploaded images.
- **GetImageListResponse** - A response that contains status information for all images.
- **GetImageListResponseItem** - An image identifier and state information for an image.

### Message configuration
- [Upload Message](https://developer.apple.com/documentation/retentionmessaging/upload_message) - Upload a message to use for retention messaging.
- [Delete Message](https://developer.apple.com/documentation/retentionmessaging/delete_message) - Delete a previously uploaded message.
- [Get Message List](https://developer.apple.com/documentation/retentionmessaging/get_message_list) - Get the message identifier and state of all uploaded messages.
- **UploadMessageRequestBody** - The request body for uploading a message, which includes the message text and an optional image reference.
- **UploadMessageImage** - The definition of an image with its alternative text.
- **GetMessageListResponse** - A response that contains status information for all messages.
- **GetMessageListResponseItem** - A message identifier and status information for a message.

### Default message configuration
- [Configure Default Message](https://developer.apple.com/documentation/retentionmessaging/configure_default_message) - Configure a default message for a specific product in a specific locale.
- [Delete Default Message](https://developer.apple.com/documentation/retentionmessaging/delete_default_message) - Delete a default message for a product in a locale.
- **DefaultConfigurationRequest** - The request body that contains the default configuration information.

### Real-time retention messaging
- [Setting up your Get Retention Message endpoint](https://developer.apple.com/documentation/retentionmessaging/setting_up_your_get_retention_message_endpoint) - Choose retention messages for customers in real time by implementing an endpoint on your server that responds to requests from the App Store server.
- [Responding to real-time retention messaging requests](https://developer.apple.com/documentation/retentionmessaging/responding_to_real-time_retention_messaging_requests) - Select retention messages for customers in real time by responding to requests on your Get Retention Message endpoint.
- **RealtimeRequestBody** - The request body the App Store server sends to your Get Retention Message endpoint.
- **DecodedRealtimeRequestBody** - The decoded request body the App Store sends to your server to request a real-time retention message.
- **RealtimeResponseBody** - A response you provide to choose, in real time, a retention message the system displays to the customer.

### Data types
- [Data types](https://developer.apple.com/documentation/retentionmessaging/data_types) - Refer to these data types for request and response payloads.

### Error information
- [Error codes](https://developer.apple.com/documentation/retentionmessaging/error_codes) - Understand the error codes that Retention Messaging API responses return.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/RetentionMessaging)*