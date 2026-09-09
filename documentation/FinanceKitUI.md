# FinanceKitUI

Add orders to Apple Wallet.

**Platforms:** iOS 17.0+ | iPadOS 17.0+ | Mac Catalyst 17.0+

## Overview

FinanceKitUI supplies SwiftUI interfaces for adding orders to Wallet, authorizing financial connections in an extension, and selecting FinanceKit transactions.

Use [`AddOrderToWalletButton`](https://developer.apple.com/documentation/financekitui/addordertowalletbutton) with its signed-archive initializer to offer an order to Apple Wallet. Its documented styles include `black` and `blackOutline`; presenting an order button isn't financial-data authorization.

## Integration and availability

[`FinancialConnectionUIExtensionAuthorizationScene`](https://developer.apple.com/documentation/financekitui/financialconnectionuiextensionauthorizationscene) receives a request and hosts your authorization UI. Read the request's parameters and complete it with an authorization result or an error. It is documented from the framework's 17.0 baseline. [`TransactionPicker`](https://developer.apple.com/documentation/financekitui/transactionpicker), by contrast, requires iOS/iPadOS 18+. Do not infer Mac Catalyst support for the picker or assume every FinanceKitUI symbol has the same minimum.

Use [FinanceKit](FinanceKit.md) for the underlying data/authorization model and [ExtensionKit](ExtensionKit.md) for extension UI infrastructure. Displaying a button or picker does not by itself grant data access.

## Topics

### Adding an order to Apple Wallet
- [`AddOrderToWalletButton`](https://developer.apple.com/documentation/financekitui/addordertowalletbutton) - A SwiftUI order-addition button.
- [`AddOrderToWalletButtonStyle`](https://developer.apple.com/documentation/financekitui/addordertowalletbuttonstyle) - A structure containing the supported button styles.

### Protocols
- [`FinancialConnectionUIExtension`](https://developer.apple.com/documentation/financekitui/financialconnectionuiextension) - An `AppExtension` with a financial-connection scene body.
- [`FinancialConnectionUIExtensionProviding`](https://developer.apple.com/documentation/financekitui/financialconnectionuiextensionproviding) - Declares the `authorize(_:)` requirement.
- [`FinancialConnectionUIExtensionScene`](https://developer.apple.com/documentation/financekitui/financialconnectionuiextensionscene) - An `AppExtensionScene` protocol for this extension.

### Structures
- [`FinancialConnectionExtensionAuthorizationRequest`](https://developer.apple.com/documentation/financekitui/financialconnectionextensionauthorizationrequest) - Supplies parameters and completion methods for a result or error.
- [`FinancialConnectionExtensionAuthorizationResult`](https://developer.apple.com/documentation/financekitui/financialconnectionextensionauthorizationresult) - A codable, sendable authorization-result value.
- [`FinancialConnectionUIExtensionAuthorizationScene`](https://developer.apple.com/documentation/financekitui/financialconnectionuiextensionauthorizationscene) - Hosts a SwiftUI view for an authorization request.
- [`TransactionPicker`](https://developer.apple.com/documentation/financekitui/transactionpicker) - A view for selecting a collection of FinanceKit transactions.

### Type Aliases
- [`FinancialConnectionExtensionAuthorizationParams`](https://developer.apple.com/documentation/financekitui/financialconnectionextensionauthorizationparams) - A `[String: String]` type alias.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/FinanceKitUI)*
