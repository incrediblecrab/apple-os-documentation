# iAd

The Apple Search Ads iAd Attribution API is a legacy framework for attributing app data that originates from Apple Search Ads campaigns on iOS devices.

**Historical framework-catalog introduction labels:** iOS 4.0 | iPadOS 4.0 | Mac Catalyst 13.0. These labels are not a promise that legacy symbols remain available in a current SDK.

## Overview

> **Warning:** After February 7, 2023, requests to the Apple Search Ads iAd Attribution API return `"iad-attribution" = false` or errors. Use [AdServices](AdServices.md) for current Apple Ads attribution on supported devices using iOS 14.3 and later. Attribution isn't available for downloads and redownloads from devices using iOS 14.2 or earlier.

Historically, attribution responses supplied campaign metadata for app downloads and redownloads following taps on Apple Search Ads. The legacy integration documentation below describes that historical protocol, not a currently functioning attribution workflow.

All Apple Search Ads data that Apple collects is subject to the Apple Privacy Policy.

## Lifecycle and migration

Apple's [iAd changelog](https://developer.apple.com/documentation/iad/iad-changelog) calls the attribution API deprecated. Its February 2023 cutoff is a **service behavior change**, not a newly announced OS 27 framework removal. A false legacy response is no longer reliable evidence of an organic installation. Use [AdServices](AdServices.md) and handle unavailable attribution without inventing a campaign match.

Attribution is separate from campaign management. [Apple Ads Platform API](AppleAdsPlatformAPI.md) is the newer management service; [Apple Ads Campaign Management API](apple_ads.md) has its own published migration/sunset schedule. Do not conflate that schedule with the already-ended iAd attribution service.

## Topics

### Essentials
- [iAd Changelog](https://developer.apple.com/documentation/iad/iad-changelog) - Legacy attribution-service history.
- [Setting Up Apple Search Ads Attribution](https://developer.apple.com/documentation/iad/setting-up-apple-search-ads-attribution) - Legacy integration details.
- [`ADClient`](https://developer.apple.com/documentation/iad/adclient) - The legacy class used to request an attribution response.

### Attribution Errors
- [`ADClientErrorDomain`](https://developer.apple.com/documentation/iad/adclienterrordomain) - The legacy error domain used by errors passed to the completion handler.
- [`ADClientError`](https://developer.apple.com/documentation/iad/adclienterror) - The legacy error-code enumeration documented by the Objective-C reference.

### Deprecated Symbols
- [Deprecated Symbols](https://developer.apple.com/documentation/iad/deprecated-symbols) - Reference for legacy advertising SDK symbols.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/iAd)*
