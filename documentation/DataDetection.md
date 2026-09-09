# DataDetection

Access and utilize common types of data that the data detection system matches.

**Platforms:** iOS 15.0+ | iPadOS 15.0+ | Mac Catalyst 15.0+ | macOS 12.0+ | tvOS 15.0+ | visionOS 1.0+ | watchOS 8.0+

## Overview

Data detection methods in other frameworks detect common types of data represented in text, and return DataDetection framework classes that provide semantic meaning for matches. Get relevant, domain-specific information from matches of the following types:

- Calendar events
- Email addresses
- Flight numbers
- Web links
- Amounts of money, with currencies
- Phone numbers
- Postal addresses
- Shipment tracking numbers

Detection runs through APIs in other frameworks. This UIKit example counts email-address matches on iOS/iPadOS 15+; it is not a pasteboard API for every platform in the framework header. Invoke it in response to an appropriate user action:

```swift
import UIKit
import DataDetection

@MainActor
func detectEmailAddressCount() {
    UIPasteboard.general.detectValues(for: [\.emailAddresses]) { result in
        switch result {
        case .success(let values):
            print("Email matches: \(values.emailAddresses.count)")
        case .failure(let error):
            print("Detection failed: \(error.localizedDescription)")
        }
    }
}
```

[`detectValues(for:completionHandler:)`](https://developer.apple.com/documentation/uikit/uipasteboard/detectvalues(for:completionhandler:)-6adre) exposes detected content and can trigger a system pasteboard-read notification. Pattern-only APIs report whether a match exists without exposing the contents and do not trigger that read notification.

## Topics

### Matched Strings
- **DDMatch** - A base class for common types of data that the data detection system matches.
- [`DataDetector`](https://developer.apple.com/documentation/datadetection/datadetector) - A namespace enum for string-scanning match types and options, used by `StringProtocol.dataDetectorMatches(_:options:)`. Requires version 26 on supported platforms, unlike the original `DDMatch` APIs.

### Matched Data Types
- **DDMatchCalendarEvent** - An object that represents a calendar date or date range that the data detection system matches.
- **DDMatchEmailAddress** - An object that contains an email address that the data detection system matches.
- **DDMatchFlightNumber** - An object that contains a flight number that the data detection system matches.
- **DDMatchLink** - An object that contains a web link that the data detection system matches.
- **DDMatchMoneyAmount** - An object that contains an amount of money that the data detection system matches.
- **DDMatchPhoneNumber** - An object that contains a phone number that the data detection system matches.
- **DDMatchPostalAddress** - An object that contains a postal address that the data detection system matches.
- **DDMatchShipmentTrackingNumber** - An object that contains parcel tracking information that the data detection system matches.

### Pasteboard Detectors
- **detectPatterns(for keyPaths: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, completionHandler: @escaping (Result<Set<PartialKeyPath<UIPasteboard.DetectedValues>>, any Error>) -> ())** - Requests that the data detection system identify the patterns that you specify for the pasteboard, and provide the patterns that it matches to your closure.
- **detectedPatterns(for keyPaths: Set<PartialKeyPath<UIPasteboard.DetectedValues>>) async throws -> Set<PartialKeyPath<UIPasteboard.DetectedValues>>** - Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard, and return the patterns that it matches.
- **detectPatterns(for keyPaths: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet itemSet: IndexSet?, completionHandler: @escaping (Result<[Set<PartialKeyPath<UIPasteboard.DetectedValues>>], any Error>) -> ())** - Requests that the data detection system identify the patterns that you specify for the pasteboard items, and provide the patterns that it matches to your closure.
- **detectedPatterns(for keyPaths: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet itemSet: IndexSet?) async throws -> [Set<PartialKeyPath<UIPasteboard.DetectedValues>>]** - Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard items, and return the patterns that it matches.
- **detectValues(for keyPaths: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, completionHandler: @escaping (Result<UIPasteboard.DetectedValues, any Error>) -> ())** - Requests that the data detection system identify the types of data that you specify for the pasteboard, and provide the values that it matches to your closure.
- **detectedValues(for keyPaths: Set<PartialKeyPath<UIPasteboard.DetectedValues>>) async throws -> UIPasteboard.DetectedValues** - Requests that the data detection system asynchronously identify the types of values that you specify for the pasteboard, and return the values that it matches.
- **detectValues(for keyPaths: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet itemSet: IndexSet?, completionHandler: @escaping (Result<[UIPasteboard.DetectedValues], any Error>) -> ())** - Requests that the data detection system identify the types of data that you specify for the pasteboard items, and provide the values that it matches to your closure.
- **detectedValues(for keyPaths: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet itemSet: IndexSet?) async throws -> [UIPasteboard.DetectedValues]** - Returns matched values for the selected items within one pasteboard.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/DataDetection)*
