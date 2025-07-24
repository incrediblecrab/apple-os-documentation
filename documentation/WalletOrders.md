# Wallet Orders

Create, distribute, and update orders in Wallet.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | macOS 13.0+

## Overview

Use Wallet Orders to give users the ability to track and manage their purchases in Wallet. You can donate an order to Wallet seamlessly through Apple Pay after payment authorization.

To give people the ability to track their orders in Wallet, you need to:

1. Add order details to the payment authorization result.
2. Build an order package and provide access through your web service.
3. Update the order when the order's state has changed.

## Topics

### Essentials
- [Creating the source for an order](https://developer.apple.com/documentation/walletorders/creating-the-source-for-an-order) - Define an order by creating the directory structure, and adding source files and images.
- [Building a distributable order package](https://developer.apple.com/documentation/walletorders/building-a-distributable-order-package) - Prepare an order for distribution by building, signing, and compressing the source files.
- [Retrieve the registrations for a device](https://developer.apple.com/documentation/walletorders/retrieve-the-registrations-for-a-device) - Retrieves the identifiers of the orders that the device registered for.
- [Retrieve the latest version of an order](https://developer.apple.com/documentation/walletorders/retrieve-the-latest-version-of-an-order) - Retrieves the latest signed and compressed version of an order.
- **Order** - The order's details, including information about the products or services rendered, customer service, and fulfillment.
- [Example Order Packages](https://developer.apple.com/documentation/walletorders/example-order-packages) - Edit, build, and add example order packages to Wallet.

### Notifications
- [Register a device for update notifications](https://developer.apple.com/documentation/walletorders/register-a-device-for-update-notifications) - Registers a device to receive update notifications for an order.
- [Unregister a device from update notifications](https://developer.apple.com/documentation/walletorders/unregister-a-device-from-update-notifications) - Unregisters a device from receiving update notifications for an order.
- **PushToken** - The push token APNS uses to send update notifications to the device.

### Message logs
- [Receive log messages](https://developer.apple.com/documentation/walletorders/receive-log-messages) - Records log messages on your server.
- **LogEntries** - An array of log messages.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/WalletOrders)*