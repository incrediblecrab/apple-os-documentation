# VisionEntitlementServices

Check at runtime whether a visionOS app's enterprise API license is valid and which managed entitlements it approves for the app.

**Platforms:** visionOS 26.0+

## Overview

Enterprise APIs for visionOS, such as main camera access, barcode detection, and the App Compute Category, are managed entitlements that an app unlocks with a signed license from Apple. The app needs both the entitlement in its `.entitlements` file and the license file. VisionEntitlementServices reads the state of that license at runtime, so the app can check whether the license is valid and covers an entitlement before using the feature.

Apple describes access to the license state as read-only, and the framework has no API to request, install, or renew a license. For the other visionOS enterprise resources, see [visionOS](visionOS.md).

## License requirements

The Account Holder of an organization's Apple Developer Program or Apple Developer Enterprise Program membership requests the license and entitlements; individual memberships can't. To be eligible, an app must be for use in a business setting only and meet each API's own usage criteria. Such apps can be distributed privately, as proprietary in-house apps or as custom apps through Apple Business Manager.

A Development Only license covers the whole team's apps on registered test devices, while a distribution license covers a single App ID. After approval, team members download the license file from the Services tab of Certificates, Identifiers & Profiles and add it to the Xcode project. The license expires, so renew it before the expiration date to keep the entitlements working.

## Checking the license

[`EnterpriseLicenseDetails.shared`](https://developer.apple.com/documentation/visionentitlementservices/enterpriselicensedetails/shared) is the single instance for the current process. Its [`licenseStatus`](https://developer.apple.com/documentation/visionentitlementservices/enterpriselicensedetails/licensestatus) is one of `valid`, `notFound`, `invalidFormat`, `expired`, or `notAuthorized`. [`expirationTimestamp`](https://developer.apple.com/documentation/visionentitlementservices/enterpriselicensedetails/expirationtimestamp) gives the license's expiration as a `Date`, and [`approvedEntitlements`](https://developer.apple.com/documentation/visionentitlementservices/enterpriselicensedetails/approvedentitlements) lists the entitlements the license approves.

[`isApproved(for:)`](https://developer.apple.com/documentation/visionentitlementservices/enterpriselicensedetails/isapproved(for:)) returns `true` only when the app is licensed for the entitlement and was also built with it. An entitlement that appears in `approvedEntitlements` but is missing from the app's `.entitlements` file still fails this check.

```swift
import VisionEntitlementServices

func canUseMainCamera() -> Bool {
    let license = EnterpriseLicenseDetails.shared
    guard license.licenseStatus == .valid else { return false }
    return license.isApproved(for: .mainCameraAccess)
}

func highComputeIsActive() -> Bool {
    AppComputeCategory.shared.status == .high
}
```

## Compute category status

The App Compute Category entitlement lets an app use more CPU and GPU power at the cost of more heat and shorter battery life. Holding the entitlement doesn't mean the higher settings are already in effect: the system enables them while a properly licensed app with the entitlement is open. [`AppComputeCategory.shared`](https://developer.apple.com/documentation/visionentitlementservices/appcomputecategory/shared) exposes [`status`](https://developer.apple.com/documentation/visionentitlementservices/appcomputecategory/status-swift.property), which is `high` once the system has finished enabling those settings and they're in force, `normal` otherwise, and `notAuthorized` when the app's license doesn't allow it to read this information.

## Entitlement cases

[`EnterpriseLicenseDetails.EnterpriseEntitlement`](https://developer.apple.com/documentation/visionentitlementservices/enterpriselicensedetails/enterpriseentitlement) has twelve cases: `appComputeCategory`, `appProtectedContent`, `barcodeDetection`, `cameraRegion`, `mainCameraAccess`, `neuralEngineAccess`, `objectTrackingAdjustment`, `screenCapturePassthrough`, `sharedCoordinateSpace`, `uvcDeviceAccess`, `visualFidelity`, and `windowBodyFollow`. [`allCases`](https://developer.apple.com/documentation/visionentitlementservices/enterpriselicensedetails/enterpriseentitlement/allcases) returns only the cases available on the running OS.

Apple's reference lists `visualFidelity` as visionOS 27.0+ and every other case as visionOS 26.0+. The visionOS 27.0 SDK doesn't mark that case with its own availability, so the compiler accepts it in an app that deploys to visionOS 26; check `allCases` before relying on it there.

## Topics

### Reading license state
- [`EnterpriseLicenseDetails`](https://developer.apple.com/documentation/visionentitlementservices/enterpriselicensedetails) - Reads the enterprise license's status, expiration, and approved managed entitlements.
- [`EnterpriseLicenseDetails.EnterpriseEntitlement`](https://developer.apple.com/documentation/visionentitlementservices/enterpriselicensedetails/enterpriseentitlement) - The managed entitlements a license can approve.
- [`EnterpriseLicenseDetails.Status`](https://developer.apple.com/documentation/visionentitlementservices/enterpriselicensedetails/status) - The validity states of the license.

### App Compute Category
- [`AppComputeCategory`](https://developer.apple.com/documentation/visionentitlementservices/appcomputecategory) - Reports whether the system has finished enabling the App Compute Category settings.
- [`AppComputeCategory.Status`](https://developer.apple.com/documentation/visionentitlementservices/appcomputecategory/status-swift.enum) - The `normal`, `high`, and `notAuthorized` states.

## Sources

- [Apple framework reference](https://developer.apple.com/documentation/visionentitlementservices)
- [Building spatial experiences for business apps with enterprise APIs for visionOS](https://developer.apple.com/documentation/visionos/building-spatial-experiences-for-business-apps-with-enterprise-apis)
- [EnterpriseLicenseDetails](https://developer.apple.com/documentation/visionentitlementservices/enterpriselicensedetails)
- [AppComputeCategory](https://developer.apple.com/documentation/visionentitlementservices/appcomputecategory)
