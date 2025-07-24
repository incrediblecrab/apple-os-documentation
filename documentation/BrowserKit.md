# BrowserKit

Check a device's eligibility to run alternative browser engines.

**Platforms:** iOS 18.4+ | iPadOS 18.4+

## Overview

Use BrowserKit to test whether a device is eligible to run a browser that uses an alternative browser engine, so your app can offer the alternative browser engine to a person. In your browser that uses WebKit, call isEligible(for:completionHandler:) to test whether the device can run a version of your app that uses an alternative browser engine:

```swift
do {
  guard await BEAvailability.isEligible(for: .webBrowser) else {
    return
  }
  // Offer a person a marketplace link to your browser that uses an alternative browser engine.
}
catch let error {
  // Handle the error.
}
```

For more information on creating alternative browser engines, see Designing your browser architecture.

## Topics

### Testing eligibility to use alternative browser engines
- **BEAvailability** - A class that tests whether a device is eligible to run an alternative browser engine.
- **Context** - The category of app for which you determine eligibility.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/BrowserKit)*