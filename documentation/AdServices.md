# AdServices

Attribute Apple Ads app-download campaigns on the App Store.

**Platforms:** iOS 14.3+ | iPadOS 14.3+ | Mac Catalyst 14.3+ | macOS 11.1+ | visionOS 1.0+

## Overview

Apple Ads attribution combines a client-generated token with Apple's server-side attribution API. Its records describe Apple Ads campaigns and app conversions; this is separate from creating or managing campaigns.

### Token and attribution flow

1. Call [`AAAttribution.attributionToken()`](https://developer.apple.com/documentation/adservices/aaattribution/attributiontoken()), which can throw.
2. Send the returned token yourself or through a mobile measurement provider to Apple's documented attribution endpoint.
3. Inspect the response rather than treating an HTTP success as a matched ad conversion.
4. Correlate returned campaign identifiers with the appropriate [Apple Ads Platform API](AppleAdsPlatformAPI.md) reports.

The [token reference](https://developer.apple.com/documentation/adservices/aaattribution/attributiontoken()) specifies `POST https://api-adservices.apple.com/api/v1/`, a single token as the body, and `Content-Type: text/plain`. Tokens expire after **24 hours**. This token is not a campaign-management OAuth token.

### Failure handling

HTTP `200` can contain `attribution=false`; it does not establish that a paid conversion matched. `400` indicates an invalid token. `404` can occur for an expired token or shortly after issuing a valid one; for a valid token, Apple's guidance is **5-second retry intervals, at most three attempts**. A `500` indicates a temporary service problem.

Developer Mode produces test payloads. Keep those separate from production measurements, and do not infer a campaign match from a token, missing record, or failed request.

## Topics

### Essentials
- [Changelog](https://developer.apple.com/documentation/adservices/changelog) - AdServices framework updates.

### Tokens
- [`AAAttribution`](https://developer.apple.com/documentation/adservices/aaattribution) - The class used to request a token.

### Errors
- [`AAAttributionError`](https://developer.apple.com/documentation/adservices/aaattributionerror) - Token-generation errors.
- [`AAAttributionErrorDomain`](https://developer.apple.com/documentation/adservices/aaattributionerrordomain) - The attribution error domain.
- [`Code`](https://developer.apple.com/documentation/adservices/aaattributionerror/code) - Attribution error codes.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AdServices)*
