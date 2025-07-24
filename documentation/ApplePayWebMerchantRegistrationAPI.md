# Apple Pay Web Merchant Registration API

Manage merchant registration through your web platform.

**Platforms:** Apple Pay Web Merchant Registration API 1.0+

## Overview

The Apple Pay Web Merchant Registration API is a REST API that enables platform integrators such as payment-service providers and e-commerce platforms to register web merchants who want to offer Apple Pay on the web.

As a platform integrator, you manage Apple Pay configuration on the merchants' behalf when you call Register Merchant. Merchants aren't required to set up an Apple Developer account or configure their own keys and certificates — you set up a shared set of keys and certificates for your entire merchant portfolio. Register merchants with their own website domains, or with web pages hosted by your platform.

Note: This API is available in production and in sandbox environments. To use this API in the sandbox environment, call the endpoints using the domain apple-pay-gateway-cert.apple.com. For example, the sandbox endpoint for Register Merchant is: POST https://apple-pay-gateway-cert.apple.com/paymentservices/registerMerchant.

### API Requirements for Use

To use the Apple Pay Web Merchant Registration API, you must meet the following requirements:

- Your organization must be enrolled in the Apple Developer program. For more information about enrollment, see the "Enrolling as an Organization" section in What You Need To Enroll.
- You must apply for access to the API. For more information about applying, see Registering with Apple Pay and Applying to Use the API.
- Your server must call the API using mutual authentication with Transport Layer Security (TLS) 1.2 or later, and one of the supported cipher suites. For a list of supported cipher suites, see Setting Up Your Server.

## Topics

### Essentials
- [Registering with Apple Pay and Applying to Use the API](https://developer.apple.com/documentation/ApplePayWebMerchantRegistrationAPI/registering_with_apple_pay_and_applying_to_use_the_api) - Register a commerce partner with Apple Pay and apply to use the web service.

### Web Merchant Registration
- [Preparing Merchant Domains for Verification](https://developer.apple.com/documentation/ApplePayWebMerchantRegistrationAPI/preparing_merchant_domains_for_verification) - Host a domain verification file on each domain before requesting registration.
- [Register Merchant](https://developer.apple.com/documentation/ApplePayWebMerchantRegistrationAPI/register_merchant) - Register a merchant and its corresponding set of fully qualified domains.
- **RegisterMerchantRequest** - The request body you use to register merchants.

### Web Merchant Unregistration
- [Unregister Merchant](https://developer.apple.com/documentation/ApplePayWebMerchantRegistrationAPI/unregister_merchant) - Unregister one or more domains associated with a previously registered merchant.
- **UnregisterMerchantRequest** - The request body you use to unregister one or more merchant domains.

### Web Merchant Details
- [Get Merchant Details](https://developer.apple.com/documentation/ApplePayWebMerchantRegistrationAPI/get_merchant_details) - Retrieve information about a registered merchant's current state by using the merchant's internal merchant identifier.
- **MerchantDetails** - Detailed information for a single registered merchant.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ApplePayWebMerchantRegistrationAPI)*