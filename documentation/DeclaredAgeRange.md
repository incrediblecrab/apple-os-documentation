# Declared Age Range

Create age-appropriate experiences in your app by asking people to share their age range.

**Platforms:** iOS 26.0+ | iPadOS 26.0+ | Mac Catalyst 26.0+ | macOS 26.0+

## Overview

Declared Age Range supplies an age range without disclosing an exact birthday. A request defines age gates relevant to the app; a successful response includes range bounds and declaration information. Parents or guardians can control sharing for children in Family Sharing. Account and regional conditions can affect both the sharing flow and the returned ranges.

### Entitlement and response handling

Enable `com.apple.developer.declared-age-range`, a **Boolean** entitlement, through the target's Declared Age Range capability. Request an age range using `AgeRangeService` or the SwiftUI `DeclaredAgeRangeAction`.

Handle `.sharing` and `.declinedSharing` distinctly. A `nil` lower bound means the person is below the lowest age gate; a `nil` upper bound means they meet or exceed the highest gate. Interpret these bounds using the applicable gates rather than treating either missing value as an error or an unconditional adult signal. Declined sharing and service errors do not establish adulthood. In some regulated regions, the system supplies the range automatically and may use different gates from those requested by the app.

The system can cache range information and may not immediately move a person into a new range on their birthday. Do not calculate an exact birthdate from a range or assume a saved response remains current after account or sharing-setting changes. Reevaluate the relevant flow when needed, while respecting the system's caching behavior.

### Feature-specific availability

**Reviewed September 8, 2026:** These are separate additions to the 26-generation API, not blanket new OS 27 requirements:

- [`isEligibleForAgeFeatures`](https://developer.apple.com/documentation/declaredagerange/agerangeservice/iseligibleforagefeatures) starts at 26.2. It describes the current person's eligibility for the age-related system flow; it is not an age value. Apple's guide says it returns `false` on macOS, where apps can still request a declared range.
- [`requiredRegulatoryFeatures`](https://developer.apple.com/documentation/declaredagerange/agerangeservice/requiredregulatoryfeatures) starts at 26.4. Inspect its returned feature set instead of hard-coding one region's behavior for everyone.
- [`AgeRangeDeclaration.confirmed`](https://developer.apple.com/documentation/declaredagerange/agerangeservice/agerangedeclaration/confirmed) starts at 26.5. It indicates a scrutinized declaration method; it does not disclose which identity document or payment credential was used.
- [`SignificantUpdateAction`](https://developer.apple.com/documentation/declaredagerange/significantupdateaction) starts at 26.4 on iOS, iPadOS, and Mac Catalyst. Its declaration does not list native macOS, despite the framework's broader platform list.
- [PermissionKit](PermissionKit.md) supplies permission questions and responses for significant app updates. Asking a parent is not the same as receiving approval.

Guard each newer symbol on supported targets. Keep denial, unavailable-service, and parental-response paths explicit; this framework reference does not define App Review or legal requirements.

For parental app-use consent, Apple's request guide also describes App Store Server Notifications V2 `RESCIND_CONSENT` notifications. Handle withdrawal by updating the app's state and restricting consent-dependent access. This consent channel is distinct from a cached age-range response or its sharing settings.

## Topics

### Essentials
- [com.apple.developer.declared-age-range](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.declared-age-range) - The age-range request entitlement.
- [Requesting people's age range information](https://developer.apple.com/documentation/declaredagerange/requesting-people-share-their-age-range-with-your-app) - Request, interpret, and handle failures without acquiring an exact birthday.

### Age Range Requests
- [AgeRangeService](https://developer.apple.com/documentation/declaredagerange/agerangeservice) - Requests and feature queries for the person using the device.
- [DeclaredAgeRangeAction](https://developer.apple.com/documentation/declaredagerange/declaredagerangeaction) - SwiftUI request action.
- [Implementing age assurance and permissions](https://developer.apple.com/documentation/declaredagerange/implementing-age-assurance-and-permissions) - A sample integrating age ranges and update permissions; check the individual APIs' availability.

### Significant change acknowledgment
- [SignificantUpdateAction](https://developer.apple.com/documentation/declaredagerange/significantupdateaction) - System presentation for significant-update acknowledgment.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/DeclaredAgeRange)*

*Changed-content sources: [request and response guidance](https://developer.apple.com/documentation/declaredagerange/requesting-people-share-their-age-range-with-your-app.md) and [AgeRangeService platform metadata](https://developer.apple.com/tutorials/data/documentation/declaredagerange/agerangeservice.json).*
