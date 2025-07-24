# FinanceKitUI

Add orders to Apple Wallet.

## Overview

The FinanceKitUI framework contains a standardized UI that interacts securely with FinanceKit and the FinanceStore to support the addition of orders to a person's Apple Wallet.

FinanceKitUI provides an AddOrderToWalletButton for SwiftUI. Add this button to your UI when you want to allow someone to add an order to their Apple Wallet. The button's style options are consistent with the standard Apple Pay and Wallet design language, giving users a sense of familiarity and trust when they interact with it.

## Topics

### Adding an order to Apple Wallet
- **struct AddOrderToWalletButton** - A button you use to add an order to a person's Apple Wallet.
- **struct AddOrderToWalletButtonStyle** - Values that determine the style of an Add Order to Apple Wallet button.

### Protocols
- **protocol FinancialConnectionUIExtension**
- **protocol FinancialConnectionUIExtensionProviding**
- **protocol FinancialConnectionUIExtensionScene**

### Structures
- **struct FinancialConnectionExtensionAuthorizationRequest**
- **struct FinancialConnectionExtensionAuthorizationResult**
- **struct FinancialConnectionUIExtensionAuthorizationScene** - Implement this scene to authorize your app's Financial Connection
- **struct TransactionPicker** - A view that displays a transaction picker for choosing transactions from FinanceKit.

### Type Aliases
- **typealias FinancialConnectionExtensionAuthorizationParams**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/FinanceKitUI)*