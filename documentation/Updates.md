# Updates

View major documentation updates and highlights from WWDC, browse ongoing updates from a set of framework releases over time, and jump to the latest release notes.

## OS27 Migration Snapshot — September 8, 2026

All six OS27 platforms shipped September 14: iOS/iPadOS **27.0** (`24A437`), macOS 27 Golden Gate **27.0** (`26A428`), tvOS **27.0** (`24J361`), watchOS **27.0** (`24R364`), and visionOS **27.0** (`24M362`). **Xcode 27** (`27A266a`) also shipped September 14. Previous 26-generation baselines are iOS **26.6.2** (September 8), iPadOS **26.7** (September 9), macOS **26.6.2** and visionOS **26.6.1** (August 17), and tvOS/watchOS **26.6** (July 27).

### Prioritize Verified Migration Work

- **Build hosts:** [Xcode 27](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes) includes Swift 6.4 and requires **an Apple silicon Mac on macOS Tahoe 26.6 or later**, not macOS 27. The macOS 27 SDK supports back deploying Universal apps to macOS 12 and later, and Intel development remains possible with Rosetta-supporting macOS such as macOS 27.
- **UIKit scenes:** apps built with the latest SDK must adopt the scene life cycle on iOS, iPadOS, Mac Catalyst, tvOS, and visionOS 27 or fail to launch. Multiple-window support is optional. See [scene migration](https://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle).
- **Launch screens and assets:** the [iOS/iPadOS 27 notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes) require launch screens for 27-SDK apps. ODR/`NSBundleResourceRequest` deprecation in the iOS/iPadOS, tvOS, and visionOS notes points to Background Assets; localized packs add language-aware delivery.
- **Design compatibility:** [`UIDesignRequiresCompatibility`](https://developer.apple.com/documentation/bundleresources/information-property-list/uidesignrequirescompatibility) is ignored when building for iOS, iPadOS, Mac Catalyst, macOS, or tvOS 27 or later. Do not extend that key's documented scope to watchOS or visionOS.
- **Mac behavior:** [macOS 27 notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes) cover menu-image visibility, Mac Catalyst activation without windows, native installer defaults, and Rosetta migration.
- **Watch life cycle:** [watchOS 27 notes](https://developer.apple.com/documentation/watchos-release-notes/watchos-27-release-notes) deprecate `WKExtension` and `WKExtensionDelegate` for apps with a minimum deployment target of watchOS 9.2 or later; this is not a UIKit scene requirement.
- **Managed networking:** [stricter TLS](https://support.apple.com/en-us/126655) affects selected system processes for management, enrollment, profiles, app installation, and updates. Audit ATS-compatible TLS 1.2-or-later servers and the documented exceptions, not every app socket indiscriminately.
- **Intelligence:** [SiriKit](https://developer.apple.com/documentation/sirikit) retains legacy Shortcuts, widget-configuration, and most existing Siri support. Use [App Intents](AppIntents.md) for modern integration. [PCC](../guides/private-cloud-compute.md) has separate entitlement, eligibility, privacy, and runtime-failure requirements.
- **Submission policy:** the SDK26 upload requirement and updated age-rating questionnaire are already in force. See [App Store readiness](../guides/app-store-readiness.md); the checked notice does not announce an OS27 SDK deadline.

OS 27 **Resolved Issues** are regression-test cases, not permanent API limitations. Validate SDK-linked behavior separately from running an older binary on the new OS. Exact OS27 device lists are not established by these summaries; do not extrapolate from OS26 lists.

## Topics

### WWDC
- [WWDC25](https://developer.apple.com/documentation/Updates/wwdc2025) - Highlights of new technologies introduced at WWDC25.
- [WWDC24](https://developer.apple.com/documentation/Updates/wwdc2024) - Highlights of new technologies introduced at WWDC24.
- [WWDC23](https://developer.apple.com/documentation/Updates/wwdc2023) - Highlights of new technologies introduced at WWDC23.
- [WWDC22](https://developer.apple.com/documentation/Updates/wwdc2022) - Highlights of new technologies introduced at WWDC22.
- [WWDC21](https://developer.apple.com/documentation/Updates/wwdc2021) - Highlights of new technologies introduced at WWDC21.

### Technology Updates
- [Accelerate updates](https://developer.apple.com/documentation/Updates/Accelerate) - Learn about important changes to Accelerate.
- [Accessibility updates](https://developer.apple.com/documentation/Updates/Accessibility) - Learn about important changes to Accessibility.
- [ActivityKit updates](https://developer.apple.com/documentation/Updates/ActivityKit) - Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](https://developer.apple.com/documentation/Updates/AdAttributionKit) - Learn about important changes to AdAttributionKit.
- [App Clips updates](https://developer.apple.com/documentation/Updates/AppClips) - Learn about important changes in App Clips.
- [App Intents updates](https://developer.apple.com/documentation/Updates/AppIntents) - Learn about important changes in App Intents.
- [AppKit updates](https://developer.apple.com/documentation/Updates/AppKit) - Learn about important changes to AppKit.
- [Apple Intelligence updates](https://developer.apple.com/documentation/Updates/Apple-Intelligence) - Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](https://developer.apple.com/documentation/Updates/AppleMapsServerAPI) - Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](https://developer.apple.com/documentation/Updates/ApplePencil) - Learn about important changes to Apple Pencil.
- [ARKit updates](https://developer.apple.com/documentation/Updates/ARKit) - Learn about important changes to ARKit.
- [Audio Toolbox updates](https://developer.apple.com/documentation/Updates/AudioToolbox) - Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](https://developer.apple.com/documentation/Updates/AuthenticationServices) - Learn about important changes to AuthenticationServices.
- [AVFAudio updates](https://developer.apple.com/documentation/Updates/AVFAudio) - Learn about important changes to AVFAudio.
- [AVFoundation updates](https://developer.apple.com/documentation/Updates/AVFoundation) - Learn about important changes to AVFoundation.
- [Background Tasks updates](https://developer.apple.com/documentation/Updates/BackgroundTasks) - Learn about important changes in Background Tasks.
- [Bundle Resources updates](https://developer.apple.com/documentation/Updates/BundleResources) - Learn about important changes to Bundle Resources.
- [BrowserEngineKit reference](https://developer.apple.com/documentation/browserenginekit) - Consult the framework's browser-engine integration APIs and their individual requirements.
- [CallKit updates](https://developer.apple.com/documentation/Updates/CallKit) - Learn about important changes to CallKit.
- [ContactsUI updates](https://developer.apple.com/documentation/Updates/ContactsUI) - Learn about important changes to ContactsUI.
- [Core Location updates](https://developer.apple.com/documentation/Updates/CoreLocation) - Learn about important changes to Core Location.
- [Core MIDI updates](https://developer.apple.com/documentation/Updates/CoreMIDI) - Learn about important changes to Core MIDI.
- [Core ML updates](https://developer.apple.com/documentation/Updates/CoreML) - Learn about important changes to Core ML.
- [Core Motion updates](https://developer.apple.com/documentation/Updates/CoreMotion) - Learn about important changes to Core Motion.
- [Core Spotlight updates](https://developer.apple.com/documentation/Updates/CoreSpotlight) - Learn about important changes to Core Spotlight.
- [DataDetection updates](https://developer.apple.com/documentation/Updates/DataDetection) - Learn about important changes in DataDetection.
- [Default apps updates](https://developer.apple.com/documentation/Updates/DefaultApps) - Learn about the latest changes to enabling your app to be the system default.
- [DockKit updates](https://developer.apple.com/documentation/Updates/DockKit) - Learn about important changes to DockKit.
- [File Provider updates](https://developer.apple.com/documentation/Updates/FileProvider) - Learn about important changes to File Provider.
- [FinanceKit updates](https://developer.apple.com/documentation/Updates/FinanceKit) - Learn more about changes to FinanceKit.
- [Foundation updates](https://developer.apple.com/documentation/Updates/Foundation) - Learn about important changes to Foundation.
- [Game Controller updates](https://developer.apple.com/documentation/Updates/GameController) - Learn about important changes to Game Controller.
- [GameKit updates](https://developer.apple.com/documentation/Updates/GameKit) - Learn about important changes to GameKit.
- [Group Activities updates](https://developer.apple.com/documentation/Updates/GroupActivities) - Learn about important changes to Group Activities.
- [HealthKit updates](https://developer.apple.com/documentation/Updates/HealthKit) - Learn about important changes to HealthKit.
- [Hypervisor updates](https://developer.apple.com/documentation/Updates/Hypervisor) - Learn about important changes to Hypervisor.
- [Journaling Suggestions updates](https://developer.apple.com/documentation/Updates/JournalingSuggestions) - Learn about important changes in Journaling Suggestions.
- [LightweightCodeRequirements updates](https://developer.apple.com/documentation/Updates/LightweightCodeRequirements) - Learn about important changes to LightweightCodeRequirements.
- [LiveCommunicationKit updates](https://developer.apple.com/documentation/Updates/LiveCommunicationKit) - Learn about important changes to LiveCommunicationKit.
- [MapKit updates](https://developer.apple.com/documentation/Updates/MapKit) - Learn about important changes to MapKit.
- [MapKitJS updates](https://developer.apple.com/documentation/Updates/MapKitJS) - Learn about important changes to MapKitJS.
- [Matter updates](https://developer.apple.com/documentation/Updates/Matter) - Learn about important changes to Matter.
- [Network updates](https://developer.apple.com/documentation/Updates/Network) - Learn about important changes to Network.
- [PassKit updates](https://developer.apple.com/documentation/Updates/PassKit) - Learn more about changes to PassKit.
- [PHASE updates](https://developer.apple.com/documentation/Updates/PHASE) - Learn about important changes to PHASE.
- [PhotoKit updates](https://developer.apple.com/documentation/Updates/PhotoKit) - Learn about important changes to PhotoKit and PhotosUI.
- [ProximityReader updates](https://developer.apple.com/documentation/Updates/ProximityReader) - Learn about important changes to ProximityReader.
- [RealityKit updates](https://developer.apple.com/documentation/Updates/RealityKit) - Learn about important changes in RealityKit.
- [SafariServices updates](https://developer.apple.com/documentation/Updates/SafariServices) - Learn about important changes in SafariServices.
- [ScreenCaptureKit updates](https://developer.apple.com/documentation/Updates/ScreenCaptureKit) - Learn about important changes to ScreenCaptureKit.
- [Security updates](https://developer.apple.com/documentation/Updates/Security) - Learn about important changes to Security.
- [SensorKit updates](https://developer.apple.com/documentation/Updates/SensorKit) - Learn about important changes to SensorKit.
- [ShazamKit updates](https://developer.apple.com/documentation/Updates/ShazamKit) - Learn about important changes in ShazamKit.
- [SiriKit updates](https://developer.apple.com/documentation/Updates/SiriKit) - Learn about important changes in SiriKit.
- [StoreKit updates](https://developer.apple.com/documentation/Updates/StoreKit) - Learn about important changes in StoreKit.
- [Swift updates](https://developer.apple.com/documentation/Updates/Swift) - Learn about important changes to Swift.
- [Swift Charts updates](https://developer.apple.com/documentation/Updates/SwiftCharts) - Learn about important changes to Swift Charts.
- [SwiftData updates](https://developer.apple.com/documentation/Updates/SwiftData) - Learn about important changes to SwiftData.
- [SwiftUI updates](https://developer.apple.com/documentation/Updates/SwiftUI) - Learn about important changes to SwiftUI.
- [Symbols updates](https://developer.apple.com/documentation/Updates/Symbols) - Learn about important changes to Symbols.
- [TipKit updates](https://developer.apple.com/documentation/Updates/TipKit) - Learn about important changes in TipKit.
- [ThreadNetwork updates](https://developer.apple.com/documentation/Updates/ThreadNetwork) - Learn about important changes in ThreadNetwork.
- [UIKit updates](https://developer.apple.com/documentation/Updates/UIKit) - Learn about important changes to UIKit.
- [User Notifications updates](https://developer.apple.com/documentation/Updates/UserNotifications) - Learn about important changes in User Notifications.
- [Video Subscriber Account updates](https://developer.apple.com/documentation/Updates/VideoSubscriberAccount) - Learn about important changes in Video Subscriber Account.
- [Virtualization updates](https://developer.apple.com/documentation/Updates/Virtualization) - Learn about important changes to Virtualization.
- [Vision updates](https://developer.apple.com/documentation/Updates/Vision) - Learn about important changes in Vision.
- [watchOS updates](https://developer.apple.com/documentation/Updates/watchos) - Learn about important changes to watchOS.
- [WeatherKit updates](https://developer.apple.com/documentation/Updates/WeatherKit) - Learn about important changes to WeatherKit.
- [WidgetKit updates](https://developer.apple.com/documentation/Updates/WidgetKit) - Learn about important changes in WidgetKit.
- [WorkoutKit updates](https://developer.apple.com/documentation/Updates/WorkoutKit) - Learn about important changes to WorkoutKit.
- [Xcode updates](https://developer.apple.com/documentation/Updates/Xcode) - Learn about important changes to Xcode.
- [XCUIAutomation updates](https://developer.apple.com/documentation/Updates/XCUIAutomation) - Learn about important changes to XCUIAutomation.
- [XPC updates](https://developer.apple.com/documentation/Updates/XPC) - Learn about important changes to XPC.

### Release Notes for SDKs, Xcode, and Safari
- [iOS & iPadOS Release Notes](https://developer.apple.com/documentation/ios-ipados-release-notes) - Learn about changes to the iOS & iPadOS SDK.
- [macOS Release Notes](https://developer.apple.com/documentation/macos-release-notes) - Learn about changes to the macOS SDK.
- [tvOS Release Notes](https://developer.apple.com/documentation/tvos-release-notes) - Learn about changes to the tvOS SDK.
- [watchOS Release Notes](https://developer.apple.com/documentation/watchos-release-notes) - Learn about changes to the watchOS SDK.
- [visionOS Release Notes](https://developer.apple.com/documentation/visionos-release-notes) - Learn about changes to the visionOS SDK.
- [Xcode Release Notes](https://developer.apple.com/documentation/xcode-release-notes) - Learn about changes to Xcode.
- [Safari Release Notes](https://developer.apple.com/documentation/safari-release-notes) - Review browser, embedded web-content, and Web Inspector changes; individual APIs have their own platform availability.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Updates)*
