# SKAdNetwork for Web Ads

Attribute app-install campaigns that originate on the web.

**Service reference:** SKAdNetwork for Web Ads 1.0+. The browser integration below starts with iOS 16.1; service, SKAdNetwork payload, and OS versions are distinct.

## Overview

The SKAdNetwork for Web Ads API enables advertisers to measure the success of ad campaigns that initiate on the web, while maintaining user privacy. In iOS 16.1 and later, ad networks can use this API to get SKAdNetwork attributions for web ad clicks in Safari that lead to app installations from the App Store.

To use the API, follow these steps:

1. Register your ad network; see Registering an ad network.
2. Configure and display your web ad link; see Creating an attributable ad link.
3. Implement an endpoint to provide a signed web ad payload that the advertised app uses to attribute app installations to your ad campaign; see Generating a signature for attributable web ads.
4. Validate any attributions you receive; see Verifying an install-validation postback.

For more information about the ad network API, see **SKAdNetwork**.

**Note:** Ad networks can only use this API to get attributions for web ad clicks in Safari; the API doesn't get attributions for web ad clicks in **SFSafariViewController** or **WKWebView**.

The device calls your network's `POST /.well-known/skadnetwork/get-signed-payload` endpoint, which must support TLS 1.2 or later. Keep the nonce consistent across the ad link, request, and response, but use the documented encoding for each: the response uses the dash-separated UUID representation. The `signature` topic describes the parameters to sign, while the response carries the resulting cryptographic signature.

## Topics

### Essentials
- [Creating an attributable ad link](https://developer.apple.com/documentation/skadnetworkforwebads/creating-an-attributable-ad-link) - Create click-through web ads that attribute App Store app installations to your ad network.

### Receiving a request for a web ad payload
- [Get a signed SKAdNetwork ad payload for a web ad](https://developer.apple.com/documentation/skadnetworkforwebads/get-a-signed-skadnetwork-ad-payload-for-a-web-ad.) - Your server's endpoint for device requests for signed ad interactions.
- **AdImpressionRequest** - The request body that devices send to fetch the web ad impression from the ad network's server.

### Providing the web ad signature and response
- [Generating a signature for attributable web ads](https://developer.apple.com/documentation/skadnetworkforwebads/generating-a-signature-for-attributable-web-ads) - Initiate install-validation by providing the signed parameters for an attributable web ad.
- **AdImpressionResponse** - The response you provide that contains a signed payload for a clicked web ad.
- **signature** - The key-value pairs that ad networks use to cryptographically sign a web ad.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SKAdNetworkforWebAds)*
