# ProximityReader

Read contactless physical and digital wallet cards using your iPhone.

**Base payment APIs (SDK availability):** iOS 15.4+ | iPadOS 15.4+ | Mac Catalyst 17.0+

## Overview

The ProximityReader framework supports Tap to Pay on iPhone, which allows a person's iPhone to act as a point-of-sale device without additional hardware. It also supports compatible NFC loyalty passes, mobile-document verification, and customer engagement. These features have separate availability and authorization requirements.

For **Tap to Pay payments**, coordinate with a participating, Level 3-certified payment service provider and establish the payment-processing workflow. Request Apple's managed entitlement as described in [Setting up Tap to Pay on iPhone](https://developer.apple.com/documentation/proximityreader/setting-up-the-entitlement-for-tap-to-pay-on-iphone). This payment-provider requirement is not a blanket prerequisite for the separate Verifier API.

**Note:** Tap to Pay on iPhone follows the PCI CPoC Standard, which uses Level 2 certified payment kernels and a user interface for reading contactless payment cards.

## Availability, authorization, and payments

The SDK's platform labels do not make an iPad or Mac a contactless payment terminal. For Tap to Pay, check [`PaymentCardReader.isSupported`](https://developer.apple.com/documentation/proximityreader/paymentcardreader/issupported). It checks the **device model, not the OS version**: the model must be iPhone XS or newer, while a region or provider may impose additional OS requirements.

The entitlement request requires an organization-level Apple Developer account and its Account Holder. Development approval is not distribution approval; TestFlight and App Store distribution require the distribution entitlement. Configure the managed capability and signed entitlements, obtain a valid provider token, and complete merchant terms acceptance.

Prepare a reader session in the foreground and recreate it after returning from the background. Hold the session while reading, and perform only one read at a time. Handle preparation and read errors separately.

A `PaymentCardReadResult` is **not settlement**. Its `paymentCardData` is an optional Base64-encoded encrypted payload. For ordinary reads, Apple's integration guide gives the encrypted data a **60-second** validity period: forward returned data immediately, including unsuccessful transaction outcomes, and use the provider's result for fulfillment. Store and Forward is a separate workflow, not permission to cache ordinary read results indefinitely.

## ID Verifier: requests and authorization

The [Verifier API](https://developer.apple.com/documentation/proximityreader/adopting-the-verifier-api-in-your-iphone-app) uses a supported iPhone with iOS 17 or later. Check `MobileDocumentReader.isSupported` and add the Verifier API capability. Tap to Pay authorization does not grant identity-data access:
- [ID Verifier — Display Only](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.proximity-reader.identity.display) is a Boolean entitlement.
- [ID Verifier — Data Transfer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.proximity-reader.identity.read) is a dictionary with document-type and document-element scopes, not an unrestricted Boolean switch.

Display requests show information for visual inspection; data requests return validated elements; raw-data requests return data for further processing. Request only necessary elements and accurately distinguish retained from nonretained data. National-ID requests also have region checks. For iOS, iPadOS, and Mac Catalyst, driver's-license request types start at 17.0, national-ID types at 18.0, and photo-ID/composite types at 26.0; they are not all new in 27.

[`MobileDocumentReader.prepare(using:)`](https://developer.apple.com/documentation/proximityreader/mobiledocumentreader/prepare(using:)) accepts an **optional** reader token. To display registered branding, generate a device-bound JWT on your server using the [reader-token guide](https://developer.apple.com/documentation/proximityreader/generating-reader-tokens-for-the-verifier-api). Its `exp` must be after `iat` and no more than **5 minutes** later. After successful initial preparation, the framework permits reuse for up to **48 hours**; that is not permission to issue a JWT with a 48-hour expiration. Handle invalid tokens, expired sessions, unavailable service/network, and user cancellation separately.

## OS 27: Tap to Share

[`CustomerEngagementSession`](https://developer.apple.com/documentation/proximityreader/customerengagementsession) is a 27.0 beta API in the reviewed SDK. [Tap to Share](https://developer.apple.com/documentation/proximityreader/adding-support-for-tap-to-share-to-your-app) exchanges customer information, shopping-cart state, and supported payment/pass interactions. Its merchant-device requirement is **iPhone 12 or later**, with the Tap to Share capability plus the Tap to Pay entitlement.

The concrete [`open(using:)`](https://developer.apple.com/documentation/proximityreader/customerengagementsession/open(using:)) parameter is `CustomerEngagement.Token?`. Create that token from a provider's `PaymentCardReader.Token` using [`CustomerEngagement.Token.init(using:)`](https://developer.apple.com/documentation/proximityreader/customerengagement/token/init(using:)). Omitting it requires an already valid `PaymentCardReaderSession`; it does not open an unauthenticated session.

Supply merchant/privacy-policy information, wait for the `.ready` event before sending requests, and account for the connected client's type/version. Handle declined information sharing, incompatible requests, cancellation, and disconnection without treating them as consent. Close the session when done.

Shopping-cart updates replace the **full** cart state. The Apple Pay flow requires the returned `CustomerEngagement.ShoppingCartToken` and a compatible `localWireless` client. [`requestPayment(for:using:delegate:)`](https://developer.apple.com/documentation/proximityreader/customerengagementsession/requestpayment(for:using:delegate:)) takes that token, a `PKPaymentRequest`, and a payment-authorization delegate; it is asynchronous, throwing, and returns `Bool`. If it returns `false`, offer another payment method. Presenting a sheet or obtaining customer information is not confirmation of a completed charge.

## Topics

### Payment card reader

- [Setting up Tap to Pay on iPhone](https://developer.apple.com/documentation/proximityreader/setting-up-the-entitlement-for-tap-to-pay-on-iphone) - Request the entitlement.
- [Adding support for Tap to Pay on iPhone](https://developer.apple.com/documentation/proximityreader/adding-support-for-tap-to-pay-on-iphone-to-your-app) - Prepare sessions and process read results.
- [`PaymentCardReader`](https://developer.apple.com/documentation/proximityreader/paymentcardreader) - An object you use to configure Tap to Pay on iPhone on the current device.
- [`PaymentCardReaderSession`](https://developer.apple.com/documentation/proximityreader/paymentcardreadersession) - The object you use to start reading a contactless payment or loyalty card.

### Payment requests

- [`PaymentCardTransactionRequest`](https://developer.apple.com/documentation/proximityreader/paymentcardtransactionrequest) - A request for a contactless purchase or refund that includes the purchase amount and currency information.
- [`PaymentCardVerificationRequest`](https://developer.apple.com/documentation/proximityreader/paymentcardverificationrequest) - A request to verify details for a contactless payment card.
- [`PaymentCardReadResult`](https://developer.apple.com/documentation/proximityreader/paymentcardreadresult) - The result of a payment card read operation.

### Store and Forward mode

These types are annotated iOS 18.4+, iPadOS 18.4+, and Mac Catalyst 18.4+. Resolve stored batches with the provider's deletion token after delivery to the provider; a successful read or an upload attempt alone is not authorization to delete them.

- [`StoreAndForwardBatch`](https://developer.apple.com/documentation/proximityreader/storeandforwardbatch) - A structure that stores the data to send to the payment service provider to process.
- [`StoreAndForwardBatchDeletionToken`](https://developer.apple.com/documentation/proximityreader/storeandforwardbatchdeletiontoken) - A provider-issued token confirming delivery and authorizing deletion of the batch.
- [`StoreAndForwardPaymentCardReaderSession`](https://developer.apple.com/documentation/proximityreader/storeandforwardpaymentcardreadersession) - The object you use to start reading a contactless payment or loyalty card in Store and Forward mode.
- [`StoreAndForwardStatus`](https://developer.apple.com/documentation/proximityreader/storeandforwardstatus) - A structure that describes the Store and Forward session status.
- [`PaymentCardReaderStore`](https://developer.apple.com/documentation/proximityreader/paymentcardreaderstore) - A structure that manages the store that contains all the Store and Forward reads.

### Loyalty card requests

- [Accepting loyalty passes from Wallet](https://developer.apple.com/documentation/proximityreader/accepting-loyalty-passes-from-wallet) - Configure NFC-enabled passes, existing pass type identifiers, and the loyalty provider's processing flow.
- [`VASRequest`](https://developer.apple.com/documentation/proximityreader/vasrequest) - A request to read a contactless loyalty card and retrieve loyalty program identifiers for the person.
- [`VASReadResult`](https://developer.apple.com/documentation/proximityreader/vasreadresult) - The result of a request to read loyalty card information.

### Merchant discovery

- [`ProximityReaderDiscovery`](https://developer.apple.com/documentation/proximityreader/proximityreaderdiscovery) - An object that presents a UI with information about how to use Tap to Pay on iPhone.

### Mobile document reader

- [Adopting the Verifier API](https://developer.apple.com/documentation/proximityreader/adopting-the-verifier-api-in-your-iphone-app) - Configure and test document-reading support.
- [Generating reader tokens](https://developer.apple.com/documentation/proximityreader/generating-reader-tokens-for-the-verifier-api) - Generate device-bound tokens for branded reader sessions.
- [Checking IDs](https://developer.apple.com/documentation/proximityreader/checking-ids-with-the-verifier-api) - Read and verify supported identity documents.
- [`MobileDocumentReader`](https://developer.apple.com/documentation/proximityreader/mobiledocumentreader) - An object for configuring mobile document reading on the current device.
- [`MobileDocumentReaderSession`](https://developer.apple.com/documentation/proximityreader/mobiledocumentreadersession) - The object you use to start reading a mobile document.
- [`MobileDocumentHolderName`](https://developer.apple.com/documentation/proximityreader/mobiledocumentholdername) - A holder's name as text and structured components; this type is a 27.0 beta addition.

### Mobile document requests

- [`MobileDriversLicenseDisplayRequest`](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedisplayrequest) - A mobile driver's license request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- [`MobileDriversLicenseDataRequest`](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedatarequest) - A mobile driver's license request that retrieves elements from the holder and returns the validated document elements.
- [`MobileDriversLicenseRawDataRequest`](https://developer.apple.com/documentation/proximityreader/mobiledriverslicenserawdatarequest) - A mobile driver's license request which retrieves elements from the holder and returns the raw response data for processing.
- [`MobileNationalIDCardDisplayRequest`](https://developer.apple.com/documentation/proximityreader/mobilenationalidcarddisplayrequest) - A mobile national ID card request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- [`MobileNationalIDCardDataRequest`](https://developer.apple.com/documentation/proximityreader/mobilenationalidcarddatarequest) - A mobile national ID card request that retrieves elements from the holder and returns the validated document elements.
- [`MobileNationalIDCardRawDataRequest`](https://developer.apple.com/documentation/proximityreader/mobilenationalidcardrawdatarequest) - A mobile national ID card request which retrieves elements from the holder and returns the raw response data for processing.
- [`MobileDocumentDisplayRequest`](https://developer.apple.com/documentation/proximityreader/mobiledocumentdisplayrequest) - A mobile document request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- [`MobileDocumentRequest`](https://developer.apple.com/documentation/proximityreader/mobiledocumentrequest) - A type that represents a mobile document request.
- [`MobileDocumentDataRequest`](https://developer.apple.com/documentation/proximityreader/mobiledocumentdatarequest) - A type that represents a mobile document data request.
- [`MobileDocumentRawDataRequest`](https://developer.apple.com/documentation/proximityreader/mobiledocumentrawdatarequest) - A type that represents a mobile document raw data request.
- [`MobilePhotoIDDataRequest`](https://developer.apple.com/documentation/proximityreader/mobilephotoiddatarequest) - A photo ID request that retrieves elements from the holder and returns the validated document elements.
- [`MobilePhotoIDRawDataRequest`](https://developer.apple.com/documentation/proximityreader/mobilephotoidrawdatarequest) - A photo ID request that returns raw response data for processing, not a driver's-license request.
- [`MobileDocumentAnyOfDataRequest`](https://developer.apple.com/documentation/proximityreader/mobiledocumentanyofdatarequest) - A type that describes a data request for any mobile document from a group of requests.
- [`MobileDocumentAnyOfRawDataRequest`](https://developer.apple.com/documentation/proximityreader/mobiledocumentanyofrawdatarequest) - A type that describes a raw data request for any mobile document from a group of requests.

### Tap to Share

- [Adding support for Tap to Share](https://developer.apple.com/documentation/proximityreader/adding-support-for-tap-to-share-to-your-app) - Connect with customers and exchange supported information.
- [`CustomerEngagement`](https://developer.apple.com/documentation/proximityreader/customerengagement) - Data exchanged between merchant and customer.
- [`CustomerEngagementSession`](https://developer.apple.com/documentation/proximityreader/customerengagementsession) - Manage the interaction lifecycle.

### Errors

- [`PaymentCardReaderError`](https://developer.apple.com/documentation/proximityreader/paymentcardreadererror) - An error type that indicates problems with the configuration of the reader.
- [`MobileDocumentReaderError`](https://developer.apple.com/documentation/proximityreader/mobiledocumentreadererror) - An error type that indicates problems when preparing a mobile document reader session and performing document requests.
- [`CustomerEngagementSession.Error`](https://developer.apple.com/documentation/proximityreader/customerengagementsession/error) - Tap to Share credential, connection, readiness, request, and customer-consent failures.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ProximityReader)*
