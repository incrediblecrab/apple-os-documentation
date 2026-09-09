# Apple Pay on the Web

Support Apple Pay on your website with JavaScript-based APIs.

**Safari introduction:** Safari Desktop 10.0+ | Safari Mobile 10.0+. This is not a complete modern browser/device-support matrix; the JavaScript SDK also supports eligible third-party browsers.

## Overview

Safari supports two JavaScript APIs that let you accept Apple Pay payments from customers on your website:

- [Payment Request API](https://developer.apple.com/documentation/applepayontheweb/payment-request-api), using the W3C payment-request model.
- [Apple Pay JS API](https://developer.apple.com/documentation/applepayontheweb/apple-pay-js-api), Apple's payment-session API.

The current Apple Pay JS SDK also supports Apple Pay flows in third-party browsers. Do not infer payment support merely from a browser name, a Secure Element, or the existence of a button. Check runtime capabilities and the customer's supported payment credentials. See the [interactive demo](https://applepaydemo.apple.com) for an integration demonstration.

Keep three version systems separate: the customer's OS/browser, the Apple Pay API version selected for a session, and the downloaded SDK's semantic version. The reviewed [SDK change log](https://developer.apple.com/documentation/applepayontheweb/apple-pay-js-change-log) includes **1.3.8**; it is not an OS 27 baseline or Apple Pay API version 1.

### Safari availability by region and platform

Apple Pay requires a supported region, device, and payment setup. The following table preserves Apple's Safari API-introduction information; it does not describe every newer SDK/browser combination or guarantee service availability everywhere.

The primary reference lists:

| API | Worldwide (except China) | China |
|-----|-------------------------|--------|
| Apple Pay JS | iOS 10 and later<br>macOS 10.12 and later | iOS 11.2 and later<br>(Not available in macOS) |
| Payment Request API | iOS 11.3 and later<br>macOS 10.12.6 and later, in Safari 11.1 and later | iOS 11.3 and later<br>(Not available in macOS) |

On iOS, Safari and `SFSafariViewController` support Apple Pay. The [availability guide](https://developer.apple.com/documentation/applepayontheweb/checking-for-apple-pay-availability) retains additional China-specific device and OS checks; do not extrapolate the table to support Apple Pay on a Mac in China.

Check for `ApplePaySession`, test the required API version with [`supportsVersion`](https://developer.apple.com/documentation/applepayontheweb/applepaysession/supportsversion), and use the documented capability checks:
- [`canMakePayments`](https://developer.apple.com/documentation/applepayontheweb/applepaysession/canmakepayments) returns a Boolean about payment capability, not whether a card is provisioned.
- [`applePayCapabilities`](https://developer.apple.com/documentation/applepayontheweb/applepaysession/applepaycapabilities) asynchronously returns a response with `paymentCredentialStatus`. `paymentCredentialStatusUnknown` means capability is supported but Wallet information is unknown; it is not `applePayUnsupported`. Follow the guide's display rules for available, unavailable, and unknown credentials rather than collapsing them into a single Boolean.

For App Store distribution policy and country-specific rules, use the separate [regional distribution](../guides/regional-distribution.md) and [App Store readiness](../guides/app-store-readiness.md) guides; this API-availability table is not a distribution-policy table.

### Apple Pay requirements

The requirements for using Apple Pay on your website are:

- Follow the [Apple Pay acceptable-use guidelines](https://developer.apple.com/apple-pay/acceptable-use-guidelines-for-websites/).
- For direct integration, [configure a merchant ID, certificates, and verified domains](https://developer.apple.com/documentation/applepayontheweb/configuring-your-environment) in your Apple Developer account. An approved platform can instead onboard merchants through the [Web Merchant Registration API](ApplePayWebMerchantRegistrationAPI.md); those merchants do not each need their own developer account.
- Serve all Apple Pay pages over HTTPS. Follow [Setting Up Your Server](https://developer.apple.com/documentation/applepayontheweb/setting-up-your-server), including TLS 1.2 or later, SNI, and the appropriate allow lists.
- Keep payment processing certificates separate from the merchant identity certificate used to authenticate server communication, and maintain certificate/domain validity.

### Merchant validation and completion

Handle [`onvalidatemerchant`](https://developer.apple.com/documentation/applepayontheweb/applepaysession/onvalidatemerchant) through your server. The current event reference directs new integrations to the static regional gateway: `apple-pay-gateway.apple.com` globally or `cn-apple-pay-gateway.apple.com` in China. Use the documented Payment Session request and the merchant identity certificate for mutual TLS; never request the merchant session directly from client JavaScript.

The event reference explicitly retains the older `validationURL`-based flow for existing implementations. When using that flow, restrict server requests to Apple's documented validation destinations rather than accepting arbitrary client-supplied URLs.

Return the opaque session through `completeMerchantValidation`. It is single-use and expires after **five minutes**. Follow [Requesting an Apple Pay payment session](https://developer.apple.com/documentation/applepayontheweb/requesting-an-apple-pay-payment-session); that guide describes Start Session as being phased out in favor of Payment Session, not as removed at an OS 27 boundary.

[`onpaymentauthorized`](https://developer.apple.com/documentation/applepayontheweb/applepaysession/onpaymentauthorized) provides the customer's authorized payment. Process its token through your server or payment provider and respond with the version-appropriate [`completePayment`](https://developer.apple.com/documentation/applepayontheweb/applepaysession/completepayment) result before the **30-second** timeout. [`oncancel`](https://developer.apple.com/documentation/applepayontheweb/applepaysession/oncancel) can still occur after authorization; sheet dismissal alone is not successful fulfillment. Handle validation failures, processing failures, and cancellation separately.

### SDK loading and merchandising

Use the [SDK-loading guide](https://developer.apple.com/documentation/applepayontheweb/loading-the-latest-version-of-apple-pay-js). The `1.latest` URL auto-updates; a pinned semantic-version URL can use the corresponding integrity hash. Do not attach a fixed integrity hash to an auto-updating script.

The current [`apple-pay-merchandising` component](https://developer.apple.com/documentation/applepayontheweb/integrating-the-apple-pay-merchandising-component) displays installment options from participating payment providers. It does not approve a loan or authorize a charge. When specifying the SDK's `components` query parameter, explicitly include every component needed; merchandising is not among the default-loaded button components.

## Topics

### Essentials
- [Loading the latest version of the Apple Pay JS SDK](https://developer.apple.com/documentation/applepayontheweb/loading-the-latest-version-of-apple-pay-js) - Link to the most recent autoupdating version of the Apple Pay JS SDK or a version of your choice.

### Apple Pay setup
- [Setting Up Your Server](https://developer.apple.com/documentation/applepayontheweb/setting-up-your-server) - Set up your server for secure communications with Apple Pay.
- [Configuring Your Environment](https://developer.apple.com/documentation/applepayontheweb/configuring-your-environment) - Create your Apple Pay merchant ID and certificates, and verify your domain.
- [Maintaining Your Environment](https://developer.apple.com/documentation/applepayontheweb/maintaining-your-environment) - Prevent interruptions in your Apple Pay service by keeping certificates and domain verification current.

### Apple Pay merchandising
- [Integrating the Apple Pay merchandising component](https://developer.apple.com/documentation/applepayontheweb/integrating-the-apple-pay-merchandising-component) - Display installment-payment information from supported providers.

### Apple order tracking button
- [Adding a Track with Apple Wallet button](https://developer.apple.com/documentation/applepayontheweb/adding-a-track-with-apple-wallet-button) - Configure and style an Apple Wallet order-tracking button.

### Apple Pay buttons
- [Displaying Apple Pay Buttons Using JavaScript](https://developer.apple.com/documentation/applepayontheweb/displaying-apple-pay-buttons-using-javascript) - Load and configure the JavaScript Apple Pay button.
- [`ApplePayButton`](https://developer.apple.com/documentation/applepayontheweb/applepaybutton) - An object that displays a button either to trigger payments through Apple Pay or to prompt the user to set up a card.
- [Displaying Apple Pay Buttons Using CSS](https://developer.apple.com/documentation/applepayontheweb/displaying-apple-pay-buttons-using-css) - Use CSS templates to display Apple Pay buttons in Safari.

### Apple Pay JavaScript APIs
- [Choosing an API for Implementing Apple Pay on Your Website](https://developer.apple.com/documentation/applepayontheweb/choosing-an-api-for-implementing-apple-pay-on-your-website) - Compare API behavior, including Safari error-handling differences; use current SDK capability checks for broader browser support.
- [Apple Pay on the Web version history](https://developer.apple.com/documentation/applepayontheweb/apple-pay-on-the-web-version-history) - Review the listed historical API releases; the SDK change log is separate.
- [Apple Pay JS API](https://developer.apple.com/documentation/applepayontheweb/apple-pay-js-api) - Implement Apple Pay on the web using Apple's JavaScript API.
- [Payment Request API](https://developer.apple.com/documentation/applepayontheweb/payment-request-api) - Accept payments on your website with Apple Pay using the Payment Request API.

### Apple Pay JS SDK change log
- [Apple Pay JS change log](https://developer.apple.com/documentation/applepayontheweb/apple-pay-js-change-log) - Learn about new features and updates in the Apple Pay JS SDK.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ApplePayontheWeb)*
