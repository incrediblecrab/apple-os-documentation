# SKAdNetwork for Web Ads

Attribute app-install campaigns that originate on the web.

**Platforms:** SKAdNetwork for Web Ads 1.0+

## Overview

The SKAdNetwork for Web Ads API enables advertisers to measure the success of ad campaigns that initiate on the web, while maintaining user privacy. In iOS 16.1 and later, ad networks can use this API to get SKAdNetwork attributions for web ad clicks in Safari that lead to app installations from the App Store.

To use the API, follow these steps:

1. Register your ad network; see Registering an ad network.
2. Configure and display your web ad link; see Creating an attributable ad link.
3. Implement an endpoint to provide a signed web ad payload that the advertised app uses to attribute app installations to your ad campaign; see Generating a signature for attributable web ads.
4. Validate any attributions you receive; see Verifying an install-validation postback.

For more information about the ad network API, see **SKAdNetwork**.

**Note:** Ad networks can only use this API to get attributions for web ad clicks in Safari; the API doesn't get attributions for web ad clicks in **SFSafariViewController** or **WKWebView**.

## Topics

### Essentials
- [Creating an attributable ad link](https://developer.apple.com/documentation/skadnetworkforwebads/creating_an_attributable_ad_link) - Create click-through web ads that attribute App Store app installations to your ad network.

### Receiving a request for a web ad payload
- [Get a Signed Web Ad Impression Payload](https://developer.apple.com/documentation/skadnetworkforwebads/get_a_signed_web_ad_impression_payload) - An endpoint you provide to receive requests from devices to serve signed ad interactions.
- **AdImpressionRequest** - The request body that devices send to fetch the web ad impression from the ad network's server.

### Providing the web ad signature and response
- [Generating a signature for attributable web ads](https://developer.apple.com/documentation/skadnetworkforwebads/generating_a_signature_for_attributable_web_ads) - Initiate install-validation by providing the signed parameters for an attributable web ad.
- **AdImpressionResponse** - The response you provide that contains a signed payload for a clicked web ad.
- **signature** - The key-value pairs that ad networks use to cryptographically sign a web ad.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SKAdNetworkforWebAds)*