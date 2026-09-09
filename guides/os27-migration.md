# Preparing an existing app for OS 27

An ordered adoption checklist for the September 8, 2026 beta snapshot. Keep the
shipping OS 26 path while evaluating OS 27; do not turn a compiler upgrade into
an unnecessary deployment-target or hardware migration.

## Establish the compatibility matrix

Record the build host, Xcode build, Swift compiler, Swift language mode, linked
SDK, minimum deployment target, test runtime, hardware, and account/region constraints.
These are independent columns, not one "OS version."

Xcode 27 beta 6 requires **Apple silicon and macOS Tahoe 26.4 or later**, and
includes Swift 6.4. Its Intel Deprecation notes explicitly restrict the IDE's host
hardware while preserving universal-app back-deployment to macOS 12+. Do not infer
host eligibility from a statement about Rosetta applications or the output binary.
Use the [release snapshot](../README.md#release-snapshot), [Xcode reference](../documentation/Xcode.md),
and each [platform introduction](../os27-intro/) for scoped evidence.

Build the existing application with its existing shipping toolchain before changing
settings. Then select the beta with a per-command `DEVELOPER_DIR`, retaining the old
toolchain for comparison. Do not globally replace the machine's selected Xcode or
change `SWIFT_VERSION = 6.0` to the compiler's point release.

## Address launch and build blockers first

1. **Check UIKit scene adoption.** Apps linked with the current UIKit SDK must use
   the scene-based lifecycle. Inspect scene configuration and restoration, not just
   the presence of an application delegate. For iOS/iPadOS SDK 27 builds, also declare
   a launch screen using one of `UILaunchStoryboardName`, `UILaunchStoryboards`,
   `UILaunchScreen`, or `UILaunchScreens`: the release notes say apps without one
   will be rejected when the App Store begins accepting that SDK.
   See [UIKit](../documentation/UIKit.md).
2. **Remove reliance on the design compatibility key.** Apple's key documentation
   lists the OS 27 build targets that ignore it. Test the actual linked-SDK/runtime
   combination and custom controls rather than applying a universal appearance rule.
   See [Liquid Glass adoption](../liquid-glass/adopting-liquid-glass.md).
3. **Resolve compiler and initializer changes.** Review SwiftUI's new `@State`
   implementation and source compatibility, and separate Swift 6.3 features from 6.4
   additions. See [SwiftUI](../documentation/SwiftUI.md) and
   [Swift concurrency migration](swift-concurrency-migration.md).
4. **Audit downloads and managed-system connections.** On Demand Resources migration
   and the affected system processes' stronger TLS/ATS requirements can break delivery
   even when UI code compiles. See [Background Assets migration](background-assets-migration.md)
   and [Device Management](../documentation/DeviceManagement.md).

## Review feature domains without duplicating their contracts

| Domain | Adoption decision | Canonical entry points |
|---|---|---|
| UI and interaction | Check navigation, documents, controls, image loading, and accessibility on supported runtimes | [SwiftUI](../documentation/SwiftUI.md), [UIKit](../documentation/UIKit.md), [AppKit](../documentation/AppKit.md), [HIG](../human-interface-guidelines/README.md) |
| Intelligence and actions | Choose the model/runtime integration; preserve unavailable, offline, and denied paths | [Intelligence integration](intelligence-integration.md), [App Intents migration](app-intents-migration.md) |
| Data and persistence | Exercise migration, cancellation, storage constraints, and portability with representative data | [Foundation](../documentation/Foundation.md), [SwiftData](../documentation/SwiftData.md), [App Migration Kit](../documentation/AppMigrationKit.md) |
| Media, spatial, and games | Check capture/playback, rendering capabilities, hardware, and platform-specific beta issues | [AVFoundation](../documentation/AVFoundation.md), [RealityKit](../documentation/RealityKit.md), [Metal](../documentation/Metal.md) |
| Trust and permissions | Recheck authorization, revocation, credentials, and age-range semantics | [Authentication Services](../documentation/AuthenticationServices.md), [PermissionKit](../documentation/PermissionKit.md), [Declared Age Range](../documentation/DeclaredAgeRange.md) |
| Systems and devices | Separate app execution, asset delivery, managed-device policy, accessories, and diagnostics | [Background Assets](../documentation/BackgroundAssets.md), [Network](../documentation/Network.md), [MetricKit](../documentation/MetricKit.md) |
| Domain services and commerce | Verify transactions in the app and, when used, on the server; review health/business/service contracts on their own release cadence | [StoreKit](../documentation/StoreKit.md), [App Store Server API](../documentation/AppStoreServerAPI.md), [HealthKit](../documentation/HealthKit.md) |
| Browser and web | Use feature detection, fallback behavior, and separate Safari host/browser versions | [Safari 27 migration](safari27-migration.md), [WebKit](../documentation/WebKit.md) |

New APIs are optional adoption opportunities unless a source identifies a requirement
for the app's actual linked SDK or supported environment. A beta release note's
resolved defect is not a permanent limitation or a new platform promise.

## Validate across platforms and failure paths

Keep an explicit result matrix instead of saying "tested on OS 27" after one build.
Include iPhone and iPad layout/input differences, Mac window and keyboard behavior,
tvOS focus, watchOS glanceability and lifecycle, and visionOS spatial comfort when
those are actual product destinations.

Exercise unavailable model/provider hardware, denied or revoked permissions,
cancellation, network loss, migration rollback/recovery, and service authorization
failures. Use appropriate test tools and representative data, not only launch success.
The [Landmarks sample](../os26-liquid-glass-example/README.md) demonstrates a bounded
build/model-check workflow and states which checks were not performed.

Review VoiceOver, Dynamic Type, contrast/transparency preferences, Reduce Motion,
localization/RTL, and input alternatives. Those checks are distinct from compiler,
unit, simulator, and physical-device results.

## Recheck submission separately

Use [App Store readiness](app-store-readiness.md) and
[regional distribution](regional-distribution.md) for SDK upload minimums, age-rating
questionnaires, privacy/AI consent, entitlements, and country-specific mechanisms.
Runtime age-range APIs do not replace the App Store questionnaire.

No OS 27 SDK submission deadline appeared in the checked requirements index.
Recheck the live source before making a submission commitment; a dated absence
is not proof that Apple cannot announce a later deadline or release date.

## Sources

- [Xcode 27 release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes)
- [iOS and iPadOS 27 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- [macOS 27 release notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes)
- [Design compatibility key](https://developer.apple.com/documentation/bundleresources/information-property-list/uidesignrequirescompatibility)
- [Upcoming submission requirements](https://developer.apple.com/news/upcoming-requirements/)
- [StoreKit verification](https://developer.apple.com/documentation/storekit/verificationresult)
