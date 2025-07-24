# App Store Receipts

Validate app and In-App Purchase receipts with the App Store.

**Platforms:** App Store Receipts 1.0–1.7

**Deprecated**

Receipts are deprecated. To validate In-App Purchases on your server without using receipts, call the App Store Server API to get Apple-signed transaction and subscription information for your customers, or verify the AppTransaction and Transaction signed data that your app obtains. You can also get the same signed transaction and subscription information from the App Store Server Notifications V2 endpoint.

## Overview

Important: The verifyReceipt endpoint is deprecated. To validate receipts on your server, follow the steps in Validating receipts on the device on your server.

Your server can access the verifyReceipt endpoint to validate app and in-app transaction receipts. Submit a receipt to the App Store with your shared secret to receive a JSON response containing the app information and in-app purchase details in the fields that make up the receipt. Each field or combination of fields provides insight you can use to deliver service and content to the user, as you define.

In-app transactions that your app doesn't mark as finished using finishTransaction(_:) or finish() remain in the App Store receipt. Auto-renewable subscriptions, non-renewing subscriptions, and non-consumables remain in the receipt indefinitely, and appear in the customer transaction history when you call the Get Transaction History V1 endpoint.

The responseBody.Latest_receipt_info object for auto-renewable subscriptions can grow over time because the renewal transactions stay in the receipt indefinitely. To optimize performance, the App Store may truncate receipts in the sandbox environment to remove old transactions.

You can test validating receipts in the sandbox environment. For more information, see Testing In-App Purchases with sandbox and Test in-app purchases.

You can validate receipts from the App Store using server-side receipt validation or on-device validation. For more information about receipt validation options, see Choosing a receipt validation technique.

### Related sessions from WWDC22

Session 110404: Implement proactive in-app purchase restore.

## Topics

### Receipt data
- [App Store receipt data types](https://developer.apple.com/documentation/appstorereceipts/app_store_receipt_data_types) - Data types of objects that return in the receipt.

### Local receipt validation
- [Validating receipts on the device](https://developer.apple.com/documentation/appstorereceipts/validating_receipts_on_the_device) - Verify the contents of app receipts by decoding and parsing the receipt on the device.

### Deprecated
- [verifyReceipt](https://developer.apple.com/documentation/appstorereceipts/verifyreceipt) - Send a receipt to the App Store for verification.
- **requestBody** - The JSON contents you submit with the request to the App Store.
- **responseBody** - The JSON data that returns in the response from the App Store.
- **error** - Error information that returns in the response body when a request isn't successful.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/appstorereceipts)*