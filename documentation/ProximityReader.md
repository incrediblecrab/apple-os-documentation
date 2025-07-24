# ProximityReader

Read contactless physical and digital wallet cards using your iPhone.

**Platforms:** iOS 15.4+ | iPadOS 15.4+ | Mac Catalyst 15.4+

## Overview

The ProximityReader framework supports Tap to Pay on iPhone, which allows a person's iPhone to act as a point-of-sale device without additional hardware. ProximityReader also supports the reading of loyalty cards from the Wallet app. Use this framework to initiate the payment process from your app.

The use of this framework requires you to coordinate with a participating payment service provider that is Level 3 certified. Contact your payment provider and work with them to set up a workflow for handling payments. When you're ready, contact Apple and request the entitlement you need to integrate Tap to Pay on iPhone support into your app. For information on requesting this entitlement, see Setting up Tap to Pay on iPhone.

**Note:** Tap to Pay on iPhone follows the PCI CPoC Standard, which uses Level 2 certified payment kernels and a user interface for reading contactless payment cards.

## Topics

### Payment card reader

- [Setting up Tap to Pay on iPhone](https://developer.apple.com/documentation/proximityreader/setting_up_tap_to_pay_on_iphone) - Request and configure the required entitlement to support Tap to Pay on iPhone.
- [Adding support for Tap to Pay on iPhone to your app](https://developer.apple.com/documentation/proximityreader/adding_support_for_tap_to_pay_on_iphone_to_your_app) - Configure your app to use Tap to Pay on iPhone to read contactless payment cards.
- **PaymentCardReader** - An object you use to configure Tap to Pay on iPhone on the current device.
- **PaymentCardReaderSession** - The object you use to start reading a contactless payment or loyalty card.

### Payment requests

- **PaymentCardTransactionRequest** - A request for a contactless purchase or refund that includes the purchase amount and currency information.
- **PaymentCardVerificationRequest** - A request to verify details for a contactless payment card.
- **PaymentCardReadResult** - The result of a payment card read operation.

### Store and Forward mode

- **StoreAndForwardBatch** - A structure that stores the data to send to the payment service provider to process.
- **StoreAndForwardBatchDeletionToken** - A secure token that you use to delete a Store and Forward batch.
- **StoreAndForwardPaymentCardReaderSession** - The object you use to start reading a contactless payment or loyalty card in Store and Forward mode.
- **StoreAndForwardStatus** - A structure that describes the Store and Forward session status.
- **PaymentCardReaderStore** - A structure that manages the store that contains all the Store and Forward reads.

### Loyalty card requests

- [Accepting loyalty passes from Wallet](https://developer.apple.com/documentation/proximityreader/accepting_loyalty_passes_from_wallet) - Set up the necessary components so your app can begin using Tap to Pay on iPhone to read and issue loyalty passes.
- **VASRequest** - A request to read a contactless loyalty card and retrieve loyalty program identifiers for the person.
- **VASReadResult** - The result of a request to read loyalty card information.

### Merchant discovery

- **ProximityReaderDiscovery** - An object that presents a UI with information about how to use Tap to Pay on iPhone.

### Mobile document reader

- [Adopting the Verifier API in your iPhone app](https://developer.apple.com/documentation/proximityreader/adopting_the_verifier_api_in_your_iphone_app) - Configure and test ID Verifier support in your app for reading mobile documents.
- [Generating reader tokens for the Verifier API](https://developer.apple.com/documentation/proximityreader/generating_reader_tokens_for_the_verifier_api) - Configure your server to generate reader tokens to prepare a device for mobile document reading.
- [Checking IDs with the Verifier API](https://developer.apple.com/documentation/proximityreader/checking_ids_with_the_verifier_api) - Read and verify mobile driver's license information without any additional hardware.
- **MobileDocumentReader** - An object for configuring mobile document reading on the current device.
- **MobileDocumentReaderSession** - The object you use to start reading a mobile document.

### Mobile document requests

- **MobileDriversLicenseDisplayRequest** - A mobile driver's license request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- **MobileDriversLicenseDataRequest** - A mobile driver's license request that retrieves elements from the holder and returns the validated document elements.
- **MobileDriversLicenseRawDataRequest** - A mobile driver's license request which retrieves elements from the holder and returns the raw response data for processing.
- **MobileNationalIDCardDisplayRequest** - A mobile national ID card request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- **MobileNationalIDCardDataRequest** - A mobile national ID card request that retrieves elements from the holder and returns the validated document elements.
- **MobileNationalIDCardRawDataRequest** - A mobile national ID card request which retrieves elements from the holder and returns the raw response data for processing.
- **MobileDocumentDisplayRequest** - A mobile document request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- **MobileDocumentRequest** (Beta) - A type that represents a mobile document request.
- **MobileDocumentDataRequest** (Beta) - A type that represents a mobile document data request.
- **MobileDocumentRawDataRequest** (Beta) - A type that represents a mobile document raw data request.
- **MobilePhotoIDDataRequest** (Beta) - A photo ID request that retrieves elements from the holder and returns the validated document elements.
- **MobilePhotoIDRawDataRequest** (Beta) - A mobile driver's license request which retrieves elements from the holder and returns the raw response data for processing.
- **MobileDocumentAnyOfDataRequest** (Beta) - A type that describes a data request for any mobile document from a group of requests.
- **MobileDocumentAnyOfRawDataRequest** (Beta) - A type that describes a raw data request for any mobile document from a group of requests.

### Errors

- **PaymentCardReaderError** - An error type that indicates problems with the configuration of the reader.
- **MobileDocumentReaderError** - An error type that indicates problems when preparing a mobile document reader session and performing document requests.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ProximityReader)*