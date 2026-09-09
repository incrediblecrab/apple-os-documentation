# FinanceKit

Access financial data and interact with Apple Card, Apple Cash, and orders in Wallet.

**Framework catalog:** iOS 17.0+ | iPadOS 17.0+ | Mac Catalyst 17.0+. Financial-data APIs and background delivery have later introductions and additional runtime restrictions.

## Overview

Use FinanceKit to access on-device financial data, Apple Cash, and interact with orders in Apple Wallet.

Use [`FinanceStore`](https://developer.apple.com/documentation/financekit/financestore) for data access and FinanceKitUI for system-provided presentation. Available workflows include financial accounts, balances and transactions, and adding or updating Wallet orders; these do not all have identical authorization requirements.

**Important**

An Account Holder requests the [FinanceKit managed entitlement](https://developer.apple.com/contact/request/financekit/) for an eligible organization-level developer account; this is a developer-enrollment role, not a requirement that the app's customer be an Account Holder. Apple grants access per bundle ID after review. The app needs the approved capability, `NSFinancialDataUsageDescription`, and the person's consent.

The [current availability and eligibility requirements](https://developer.apple.com/financekit/) specify eligible iPhones in the United States on iOS 17.4+ and in the United Kingdom on iOS 18.4+, with product, institution, and account-participation restrictions. The framework's iPadOS and Mac Catalyst catalog labels do not promise financial-data access on those devices. People control which accounts and what time range they share.

## Authorization and synchronization

Check [`FinanceStore.isDataAvailable(_:)`](https://developer.apple.com/documentation/financekit/financestore/isdataavailable(_:)) for `.financialData`, then use [`authorizationStatus()`](https://developer.apple.com/documentation/financekit/financestore/authorizationstatus()) and [`requestAuthorization()`](https://developer.apple.com/documentation/financekit/financestore/requestauthorization()) for the person's consent. These financial authorization APIs begin at 17.4 in their declarations. Authorization can be granted even when no accounts are available; do not display an unavailable balance as zero.

For incremental updates, consume the appropriate account, balance, or transaction `History` asynchronous sequence. Apply inserted and updated objects, remove the objects identified by the batch's deleted identifiers, and persist those changes consistently with its `newToken`. Reuse the framework-issued `HistoryToken` rather than treating it as a caller-created timestamp. Preserve currency information and distinguish pending transactions from posted ones. Handle denied authorization, unavailable data, and thrown errors separately.

A [background delivery extension](https://developer.apple.com/documentation/financekit/implementing-a-background-delivery-extension) is a 26.0 API. Enable delivery through the finance store and configure the app and extension's shared App Group as the sample describes. Background delivery does not remove authorization or error handling.

The reviewed [FinanceKit updates](https://developer.apple.com/documentation/updates/financekit) describe June 2024 features. This reference does not relabel those features as OS 27 introductions or promise universal bank/country coverage.

## Topics

### Essentials
- [Implementing a background delivery extension](https://developer.apple.com/documentation/financekit/implementing-a-background-delivery-extension) - Receive financial-data changes in your app and extensions.
- [FinanceKit updates](https://developer.apple.com/documentation/updates/financekit) - Notable changes and their actual release dates.

### Data storage
- [**FinanceStore**](https://developer.apple.com/documentation/financekit/financestore) - The entry point for authorized financial-data queries and Wallet-order operations.

### Authorization
- **func authorizationStatus() async throws -> AuthorizationStatus** - Checks the authorization status for the calling application.
- **func requestAuthorization() async throws -> AuthorizationStatus** - Prompts a person to give FinanceKit authorization to access financial data.
- [**AuthorizationStatus**](https://developer.apple.com/documentation/financekit/authorizationstatus) - Authorized, denied, or not yet determined.

### Accounts
- **func accounts(query: AccountQuery) async throws -> [Account]** - Returns a list of accounts a person added to their Wallet that meet the criteria in the provided account query.
- **func accountHistory(since: FinanceStore.HistoryToken?, isMonitoring: Bool) -> FinanceStore.History<Account>** - Returns an asynchronous account-history sequence from an optional resume token, with optional ongoing monitoring.
- **struct AssetAccount** - A structure that describes the characteristics of an asset account.
- **struct LiabilityAccount** - A structure that describes the characteristics of a liability account.
- **enum Account** - An asset or liability financial account.

### Balances
- **func accountBalances(query: AccountBalanceQuery) async throws -> [AccountBalance]** - Returns a list of balances that meet the criteria in the provided account query.
- **func accountBalanceHistory(forAccountID: UUID, since: FinanceStore.HistoryToken?, isMonitoring: Bool) -> FinanceStore.History<AccountBalance>** - Returns an asynchronous balance-history sequence for an account, starting from an optional history token.
- **struct AccountBalance** - A structure that describes the financial balance of an account at a specific point in time.
- **struct AccountBalanceQuery** - A structure that defines an account balance query.
- **struct Balance** - A structure that describes an account balance.
- **enum CreditDebitIndicator** - Values that the framework uses to describe transactions as credits or debits.
- **enum CurrentBalance** - An available balance, a booked balance, or both.

### Orders
- **struct FullyQualifiedOrderIdentifier** - The order-type identifier and merchant's identifier for a specific order.
- **func saveOrder(signedArchive: Data) async throws -> FinanceStore.SaveOrderResult** - Adds or updates a Wallet order from a valid, signed order archive.

### Transactions
- **func transactionHistory(forAccountID: UUID, since: FinanceStore.HistoryToken?, isMonitoring: Bool) -> FinanceStore.History<Transaction>** - Returns an asynchronous transaction-history sequence for an account, with an optional resume token and ongoing monitoring.
- **func transactions(query: TransactionQuery) async throws -> [Transaction]** - Returns transactions that match the provided transaction query.
- **struct AccountQuery** - A structure that defines an account query.
- **struct AccountCreditInformation** - A structure that describes the credit information associated with an account.
- **struct CurrencyAmount** - A structure that describes a monetary amount and its currency.
- **struct Transaction** - A structure that represents a transaction relating to a specific financial account.
- **struct TransactionQuery** - A structure that describes the parameters to use for a transaction query.
- **enum TransactionType** - Values that describe kinds of transactions.
- **enum TransactionStatus** - Values that describe the status of a transaction.

### Queries
- [**FinanceStore.HistoryToken**](https://developer.apple.com/documentation/financekit/financestore/historytoken) - A framework-issued, encodable history-resumption token returned in change batches.

### Merchant categories
- [**MerchantCategoryCode**](https://developer.apple.com/documentation/financekit/merchantcategorycode) - A merchant category code with an integer raw value.

### Errors
- **enum FinanceError** - Values that describe errors that may occur when accessing financial data.

### Protocols
- **protocol BackgroundDeliveryExtension** - An extension used to receive updates about changes to data within the finance store.
- [**BackgroundDeliveryExtensionProviding**](https://developer.apple.com/documentation/financekit/backgrounddeliveryextensionproviding) - Callbacks for data changes and impending extension termination.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/FinanceKit)*
