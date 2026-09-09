# Apple Pay Web Merchant Registration API

Manage merchant registration through your web platform.

**Service version:** Apple Pay Web Merchant Registration API 1.0+. This server API has its own versioning, not an OS 27 deployment target.

## Overview

The Apple Pay Web Merchant Registration API is a REST API that enables platform integrators such as payment-service providers and e-commerce platforms to register web merchants who want to offer Apple Pay on the web.

As a platform integrator, you manage Apple Pay configuration on merchants' behalf. Your merchants do not need their own Apple Developer accounts or certificate setup. Register their own checkout domains or pages hosted by your platform. The request's `encryptTo` identifies the integrator or merchant whose payment processing certificate should protect the payment data; this can identify another processor rather than always the calling platform.

Note: This API is available in production and in sandbox environments. To use this API in the sandbox environment, call the endpoints using the domain apple-pay-gateway-cert.apple.com. For example, the sandbox endpoint for Register Merchant is: POST https://apple-pay-gateway-cert.apple.com/paymentservices/registerMerchant.

### API Requirements for Use

To use the Apple Pay Web Merchant Registration API, you must meet the following requirements:

- Your organization must be enrolled in the Apple Developer Program and approved for API access.
- Follow [Applying to use the registration API and configuring IDs](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/applying-to-use-the-registration-api-and-configuring-ids). An Account Holder or Admin creates the payment platform integrator ID and its certificates.
- Keep certificate roles separate: the payment processing certificate protects payment data; the platform integrator identity certificate authenticates communication with Apple.
- Call the API using mutual TLS 1.2 or later and a supported cipher suite. Follow [Setting Up Your Server](https://developer.apple.com/documentation/applepayontheweb/setting-up-your-server), including SNI and the appropriate production or sandbox network configuration.

### Registration and failure handling

For production registration, host the verification file associated with the calling integrator ID and identity certificate at `https://[DOMAIN_NAME]/.well-known/apple-developer-merchantid-domain-association` on each submitted domain. The [verification guide](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/preparing-merchant-domains-for-verification) explicitly says sandbox does not require domain verification.

[`RegisterMerchantRequest`](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/registermerchantrequest) requires `domainNames`, `encryptTo`, `partnerInternalMerchantIdentifier`, and `partnerMerchantName`. The internal identifier is unique per merchant and is also used as the merchant identifier in the documented payment-session flow. The limit is **99 domains per internal merchant identifier**, not 99 per request with an unlimited cumulative total.

A successful registration returns `200` with **no response body**. The endpoints distinguish invalid requests (`400`), lack of API permission (`401`), an unregistered platform (`417`), and server failures (`500`). Get Merchant Details also uses `400` for an unregistered merchant. Repair configuration or input errors rather than retrying them indefinitely; use bounded retries for transient failures.

Removing a subset of registered domains keeps the merchant active. Removing its last domain deletes the merchant registration. [`MerchantDetails`](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/merchantdetails) reports the current domains and returns `encryptTo` as a **SHA-256 hash** of the configured ID, not the original identifier string.

## Topics

### Essentials
- [Applying to use the registration API and configuring IDs](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/applying-to-use-the-registration-api-and-configuring-ids) - Apply for access and create the integrator's ID and certificates.

### Web Merchant Registration
- [Preparing merchant domains for verification](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/preparing-merchant-domains-for-verification) - Host the correct domain-verification file before production registration.
- [Register Merchant](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/register-merchant) - Register a merchant and its corresponding set of fully qualified domains.
- [`RegisterMerchantRequest`](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/registermerchantrequest) - The request body you use to register merchants.

### Web Merchant Unregistration
- [Unregister Merchant](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/unregister-merchant) - Unregister one or more domains associated with a previously registered merchant.
- [`UnregisterMerchantRequest`](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/unregistermerchantrequest) - The request body you use to unregister one or more merchant domains.

### Web Merchant Details
- [Get Merchant Details](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/get-merchant) - Retrieve information about a registered merchant's current state by using the merchant's internal merchant identifier.
- [`MerchantDetails`](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/merchantdetails) - Detailed information for a single registered merchant.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ApplePayWebMerchantRegistrationAPI)*
