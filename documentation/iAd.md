# iAd

The Apple Search Ads iAd Attribution API is a legacy framework for attributing app data that originates from Apple Search Ads campaigns on iOS devices.

**Platforms:** iOS 4.0+ | iPadOS 4.0+ | Mac Catalyst 13.0+

## Overview

> **Warning:** After February 7, 2023, all requests made to the Apple Search Ads iAd Attribution API will return with a value of "iad-attribution" = false, or errors. See requestAttributionDetails(_:). Use the AdServices framework for current attribution integration with the Apple Search Ads Campaign Management API for devices using iOS 14.3 and later. Attribution isn't available for downloads and redownloads from devices using iOS 14.2 or earlier.

Attribution data consists of campaign metadata from app ads, such as app downloads and redownloads that result from taps on ads created through the Apple Search Ads user interface or the Apple Search Ads API.

All Apple Search Ads data that Apple collects is subject to the Apple Privacy Policy.

## Topics

### Essentials
- [iAd Changelog](https://developer.apple.com/documentation/iad/iad_changelog) - Learn what's new in the Apple Search Ads iAd Attribution API.
- [Setting Up Apple Search Ads Attribution](https://developer.apple.com/documentation/iad/setting_up_apple_search_ads_attribution) - Retrieve the attribution dictionary.
- **ADClient** - The parent class you use to request an attribution response.

### Deprecated

### Attribution Errors
- **ADClientErrorDomain** - The error domain that passes to the completion handler. (Deprecated)
- **ADClientError** - The group of error codes that pass from the attribution response to the completion handler block. (Deprecated)
- **Code** - The error codes that pass from the attribution response to the completion handler. (Deprecated)

### Deprecated Symbols
- [Deprecated Symbols](https://developer.apple.com/documentation/iad/deprecated_symbols) - Reference symbols from the legacy iAd framework.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/iAd)*