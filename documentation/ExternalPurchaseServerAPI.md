# External Purchase Server API

Send and manage reports you send to Apple for tokens you receive when your app provides external purchases for digital goods and services.

**Availability:** Server API, initially released in March 2024. The reviewed changelog lists version 1.2.0 on June 26, 2025; this is not an OS 27 baseline.

## Overview

Call this REST API from your server to report external purchase tokens and your customers' transactions related to the tokens. Use this API if your app uses External Purchase API and provides alternative payment options for digital goods and services, using any of the following:

- **Payment service providers:** Process an eligible external purchase within the app.
- **Linking out:** Direct the customer to an eligible external purchase destination.

Report all applicable tokens, including those without transactions, and report associated purchases. The API is a reporting mechanism, not authorization to offer a payment flow in every storefront. Use [Regional distribution](../guides/regional-distribution.md) and [App Store readiness](../guides/app-store-readiness.md) for eligibility, policy sources, fees, and reporting obligations.

### Authorize your API calls

Calls require JSON Web Tokens (JWTs) signed with an In-App Purchase key from your organization's App Store Connect account. Follow [Creating API keys](https://developer.apple.com/documentation/appstoreserverapi/creating-api-keys-to-authorize-api-requests) and [Generating JSON Web Tokens](https://developer.apple.com/documentation/appstoreserverapi/generating-json-web-tokens-for-api-requests), rather than substituting an unrelated App Store Connect API key or another service's token.

### Report external purchase tokens and transactions

When customers initiate an external purchase, your app or website receives a token. You need to report the token and the transactions associated with the token. For more information on how you receive tokens, see Receiving and decoding external purchase tokens. To send a report, call the Send External Purchase Report endpoint for each token. Send reports in all of the following cases:

- A token with line items for completed transactions.
- A token without line items when no transaction occurred.
- An unrecognized token identified by a server notification.
- Duplicate `ACQUISITION` and `SERVICES` tokens, using the documented duplicate-reporting rules.

For more information, see Reporting tokens with transactions and Reporting unrecognized and transactionless tokens.

If you successfully send a report that you later find to be incorrect, you need to correct your submission. For more information, see Reporting corrections.

### Retrieve reports

Call the Retrieve External Purchase Report endpoint to get reports you previously sent to Apple. Specify which report to retrieve by using the same requestIdentifier value that you provide when you send the report.

### Receive notifications for unreported tokens

The App Store server sends an EXTERNAL_PURCHASE_TOKEN notificationType to your App Store Server Notifications V2 endpoint in the following cases:

- `UNREPORTED`: an unreported token.
- `ACTIVE_TOKEN_REMINDER`: an active custom-link token requiring reporting.

If you receive the EXTERNAL_PURCHASE_TOKEN notification, send a report for the token the notification specifies. To check for notifications you might have missed — for example, due to a server outage — send a request to the Get Notification History endpoint to get a list of notifications that App Store Server Notifications attempted to send to your server.

For more information on notifications, see Enabling App Store Server Notifications. Configure the App Store Server Notifications V2 endpoint on your server to receive version 2 notifications.

### Test using the sandbox environment

When you test your app in the sandbox environment, the External Purchase API returns tokens that are valid only in that environment. These tokens have an externalPurchaseId that starts with the string "SANDBOX". To test your server's token reporting implementation, send reports for sandbox tokens to the Sandbox URL of the Send External Purchase Report endpoint.

**Important**

External purchase tokens generated in the sandbox environment are for testing only. The sandbox tokens and any test transaction data you submit through the sandbox URLs of the External Purchase Server API are not actual transactions.

## Failure handling and reconciliation

Keep signing keys on the server and persist each report's `requestIdentifier`. HTTP `200` means the report passed validation. HTTP `400` with `SendReportErrorResponse` means none of the report data was accepted: fix the listed errors and resubmit the full report with the same `requestIdentifier`. A malformed or duplicate request can also return `400`, so inspect the response rather than assuming partial line-item acceptance.

Retrieve prior reports to resolve uncertain outcomes. To correct an already accepted report, follow [Reporting corrections](https://developer.apple.com/documentation/externalpurchaseserverapi/reportcorrections): use a new report `requestIdentifier`, preserve the affected `lineItemId`, and include the complete corrected line item with the appropriate restatement fields.

Verify [V2 server notifications](AppStoreServerNotifications.md) and use [notification history](https://developer.apple.com/documentation/appstoreserverapi/get-notification-history) after outages. Treat an unrecognized token as a reconciliation/reporting case, not proof of a paid transaction. The [service changelog](https://developer.apple.com/documentation/externalpurchaseserverapi/changelog) is the source for token-type and report-schema changes.

## Topics

### Essentials
- [Creating API keys](https://developer.apple.com/documentation/appstoreserverapi/creating-api-keys-to-authorize-api-requests) - Create keys for authorized server calls.
- [Generating JSON Web Tokens](https://developer.apple.com/documentation/appstoreserverapi/generating-json-web-tokens-for-api-requests) - Sign authorization tokens.
- [External Purchase Server API changelog](https://developer.apple.com/documentation/externalpurchaseserverapi/changelog) - Service changes.

### External purchase tokens
- [Receiving and decoding external purchase tokens](https://developer.apple.com/documentation/storekit/receiving-and-decoding-external-purchase-tokens) - Obtain the tokens needed for reporting.

### External purchase reporting
- [Send External Purchase Report](https://developer.apple.com/documentation/externalpurchaseserverapi/send-external-purchase-report) - Submit token and transaction information.
- **object ExternalPurchaseReport** - The contents of an external purchase report for a single token.
- **object SendReportSuccessResponse** - A response that contains the request identifier and indicates the server successfully received your external purchase report.
- **object SendReportErrorResponse** - An error response that indicates your external purchase report didn't succeed, including error details for the line items in your report.

### External purchase report transactions
- [Reporting tokens with transactions](https://developer.apple.com/documentation/externalpurchaseserverapi/reportwithtransactions) - Report purchases, subscriptions, renewals, and refunds.
- [Reporting corrections](https://developer.apple.com/documentation/externalpurchaseserverapi/reportcorrections) - Correct an accepted transaction report.
- **object OneTimeBuyLineItem** - The line item that indicates a one-time charge transaction.
- **object RefundLineItem** - The line item that indicates a refund transaction.
- **object SubscriptionBuyLineItem** - The line item that indicates a subscription-related event or transaction.
- [Line item fields](https://developer.apple.com/documentation/externalpurchaseserverapi/lineitems) - Transaction and correction properties.

### External purchase report without transactions
- [Reporting unrecognized and transactionless tokens](https://developer.apple.com/documentation/externalpurchaseserverapi/reportwithouttransactions) - Report transactionless, duplicate, and unrecognized tokens.

### External purchase report retrieval
- [Retrieve External Purchase Report](https://developer.apple.com/documentation/externalpurchaseserverapi/retrieve-external-purchase-report) - Retrieve a report by request identifier.
- **object RetrieveReportSuccessResponse** - A response that indicates success and includes your external purchase report data.

### Error handling
- [Error messages and codes](https://developer.apple.com/documentation/externalpurchaseserverapi/errorcodes) - Report and endpoint errors.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ExternalPurchaseServerAPI)*
