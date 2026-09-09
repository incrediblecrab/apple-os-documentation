# BrowserKit

Transfer browser data and check eligibility to use an alternative browser engine.

**Platforms:** iOS 18.4+ | iPadOS 18.4+

## Overview

Use BrowserKit in a WebKit-based browser to check whether the device is eligible for an alternative-engine version of your browser. The asynchronous eligibility check returns a Boolean and can throw; this helper preserves the distinction between ineligibility and an error:

```swift
import BrowserKit

@available(iOS 18.4, *)
func canOfferAlternativeBrowser() async throws -> Bool {
    try await BEAvailability.isEligible(for: .webBrowser)
}
```

The [eligibility method](https://developer.apple.com/documentation/browserkit/beavailability/iseligible(for:completionhandler:)) also has a completion-handler form that reports a Boolean and an optional error. The `.webBrowser` check requires the `com.apple.developer.web-browser` default-browser entitlement. A positive result does not itself grant alternative-engine distribution entitlements. See [BrowserEngineKit](BrowserEngineKit.md) for regional requirements and [Designing your browser architecture](https://developer.apple.com/documentation/browserenginekit/designing-your-browser-architecture) for process isolation.

## Browser data transfer (iOS/iPadOS 26.4+)

[`BEBrowserDataExportManager`](https://developer.apple.com/documentation/browserkit/bebrowserdataexportmanager) and [`BEBrowserDataImportManager`](https://developer.apple.com/documentation/browserkit/bebrowserdataimportmanager) present system sheets for user-directed transfer of history, bookmarks, reading lists, and extension information between browsers. These APIs are newer than BrowserKit's 18.4 eligibility API but predate OS 27.

- Initialize the managers with a window scene; the export initializer is [`init(scene:)`](https://developer.apple.com/documentation/browserkit/bebrowserdataexportmanager/init(scene:)), not `init(window:)`.
- Register `BEBrowserDataExchangeExportActivity` and `BEBrowserDataExchangeImportActivity` in `NSUserActivityTypes`. Handle both launch activities, including a relaunch of an already-running importer.
- Retrieve the request's UUID token from the activity's `userInfo` using the manager's token key. Return it when responding to the transfer; an app-initiated export starts with a `nil` token.
- Export only the selected data categories. Receive imported items through `importBrowserData(token:)`; preserve bookmark hierarchy and history redirects. Extension information can help recommend an equivalent extension, but does not install its executable code.
- If the returned options select files, there is no browser-to-browser exchange. Your app implements file selection, import, or export in its chosen format.

Follow [Transferring browsing data to another browser](https://developer.apple.com/documentation/browserkit/transferring-browsing-data-to-another-browser). The app must meet the [default-browser criteria](https://developer.apple.com/documentation/xcode/preparing-your-app-to-be-the-default-browser); this is not a statement that the person must currently have selected it as their default.

This is not a generic browser-profile cloning API or [AppMigrationKit](AppMigrationKit.md)'s cross-platform device migration. Safari's version number does not establish BrowserKit native API availability.

## Topics

### Testing eligibility to use alternative browser engines
- [`BEAvailability`](https://developer.apple.com/documentation/browserkit/beavailability) - The eligibility-checking class, available from iOS/iPadOS 18.4.
- [`BEAvailability.Context`](https://developer.apple.com/documentation/browserkit/beavailability/context) - The app-category enumeration; `.webBrowser` checks browser eligibility.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/BrowserKit)*
