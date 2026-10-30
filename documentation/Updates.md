# Updates

View major documentation updates and highlights from WWDC, browse ongoing updates from a set of framework releases over time, and jump to the latest release notes.

## OS27 Migration Snapshot — September 8, 2026

**September 14, 2026 release update:**

All six OS27 platforms shipped September 14: iOS/iPadOS **27.0** (`24A437`), macOS 27 Golden Gate **27.0** (`26A428`), tvOS **27.0** (`24J361`), watchOS **27.0** (`24R364`), and visionOS **27.0** (`24M362`). **Xcode 27** (`27A266a`) also shipped September 14.

Earlier 26-generation entries in the [developer release feed](https://developer.apple.com/news/releases/rss/releases.rss) include iOS **26.6.2** (September 8, 2026), iPadOS **26.7** (September 9, 2026), macOS **26.6.2** and visionOS **26.6.1** (August 17, 2026), and tvOS/watchOS **26.6** (July 27, 2026).

**October 29, 2026 update:**

- **OS point releases:** iOS/iPadOS **27.2** (`24B119`), macOS Golden Gate **27.2** (`26B123`), tvOS **27.2** (`24K122`), watchOS **27.2** (`24S118`), and visionOS **27.2** (`24N120`) shipped October 26, 2026. The feed also lists iOS 27.2 build `24B91020` without stating its device scope.
- **Intermediate releases:** The feed dates iOS/iPadOS **27.0.1** (`24A446`), macOS **27.0.1** (`26A434`), watchOS **27.0.1** (`24R365`), and visionOS **27.0.1** (`24M372`) to September 28, 2026. The captured feed has no iOS 27.1 software-update item, but [Apple's security-release list](https://support.apple.com/en-us/100100) dates iOS **27.1** for iPhone Duo to October 23, 2026.
- **Xcode:** [Xcode 27.1](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes) (`27A9275`) shipped October 15, 2026, with Swift 6.4, the iOS 27.1 SDK, and version 27 SDKs for iPadOS, macOS, tvOS, watchOS, and visionOS. [Xcode 27.2](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes) includes Swift 6.4 and all six 27.2 SDKs; both Xcode versions require macOS Tahoe 26.6 or later. The security list dates Xcode 27.2 to October 29, 2026, while the captured feed still lists only its RC (`27B48`, October 19, 2026); the captures do not establish a final 27.2 build number.
- **Safari:** [Safari 27.1](https://developer.apple.com/documentation/safari-release-notes/safari-27_1-release-notes) (`20625.1.29`) was released October 23, 2026 for iOS 27.1. [Safari 27.2](https://developer.apple.com/documentation/safari-release-notes/safari-27_2-release-notes) (`20625.2.8`) was released October 26, 2026 for iOS, iPadOS, visionOS, and macOS 27.2, plus macOS 26 and macOS Sequoia.
- **26-generation maintenance:** The feed lists iPadOS **26.7.2** (`23H128`) on October 26, 2026. The security list dates macOS Tahoe **26.7** to September 14, 2026, **26.7.1** to September 28, 2026, and **26.7.2** to October 26, 2026; it also lists tvOS **26.6.1** on October 26, 2026 for Apple TV HD and Apple TV 4K 1st generation. Its iOS **26.7.2** entry is also dated October 26, 2026, although the captured developer feed has no iOS 26 update newer than **26.6.2**. The table supplies no build numbers for these iOS, macOS, or tvOS entries.

### Prioritize Verified Migration Work

- **Build hosts:** [Xcode 27](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes) includes Swift 6.4 and requires **an Apple silicon Mac on macOS Tahoe 26.6 or later**, not macOS 27. The macOS 27 SDK supports back deploying Universal apps to macOS 12 and later, and Intel development remains possible with Rosetta-supporting macOS such as macOS 27.
- **Point-release build issues:** Xcode 27.1 and 27.2 report Mac Catalyst compile errors for iOS 27.1-specific APIs; their notes recommend isolating affected code with build-time platform conditionals. Xcode 27.2 also incorrectly offers 27.1 deployment targets for macOS, watchOS, tvOS, and visionOS, and warns of problems accessing newly introduced APIs with Mac Catalyst deployment targets of 27.1 or 27.2.
- **UIKit scenes:** apps built with the latest SDK must adopt the scene life cycle on iOS, iPadOS, Mac Catalyst, tvOS, and visionOS 27 or fail to launch. Multiple-window support is optional. See [scene migration](https://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle).
- **Launch screens and assets:** the [iOS/iPadOS 27 notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes) require launch screens for 27-SDK apps. ODR/`NSBundleResourceRequest` deprecation in the iOS/iPadOS, tvOS, and visionOS notes points to Background Assets; localized packs add language-aware delivery.
- **Design compatibility:** [`UIDesignRequiresCompatibility`](https://developer.apple.com/documentation/bundleresources/information-property-list/uidesignrequirescompatibility) is ignored when building for iOS, iPadOS, Mac Catalyst, macOS, or tvOS 27 or later. Do not extend that key's documented scope to watchOS or visionOS.
- **Mac behavior:** [macOS 27 notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes) cover menu-image visibility, Mac Catalyst activation without windows, native installer defaults, and Rosetta migration.
- **Watch life cycle:** [watchOS 27 notes](https://developer.apple.com/documentation/watchos-release-notes/watchos-27-release-notes) deprecate `WKExtension` and `WKExtensionDelegate` for apps with a minimum deployment target of watchOS 9.2 or later; this is deprecation, not removal or a UIKit scene requirement.
- **Managed networking:** [stricter TLS](https://support.apple.com/en-us/126655) affects selected system processes for management, enrollment, profiles, app installation, and updates. Audit ATS-compatible TLS 1.2-or-later servers and the documented exceptions, not every app socket indiscriminately.
- **Intelligence:** [SiriKit](https://developer.apple.com/documentation/sirikit) retains legacy Shortcuts, widget-configuration, and most existing Siri support. Use [App Intents](AppIntents.md) for modern integration. [PCC](../guides/private-cloud-compute.md) has separate entitlement, eligibility, privacy, and runtime-failure requirements.
- **Submission policy:** the SDK26 upload requirement and updated age-rating questionnaire are already in force. Since September 9, 2026, uploaded iOS/iPadOS apps must also target iOS 13 or later. See [App Store readiness](../guides/app-store-readiness.md); the checked notice does not announce an OS27 SDK deadline.

OS 27 **Resolved Issues** are regression-test cases, not permanent API limitations. Validate SDK-linked behavior separately from running an older binary on the new OS. For release-specific OS27 device coverage, consult the platform-specific "Available for" entries in [Apple's security-release table](https://support.apple.com/en-us/100100) rather than extrapolating from OS26 lists.

## Topics

### WWDC
- [WWDC25](https://developer.apple.com/documentation/updates/wwdc2025) - Highlights of new technologies introduced at WWDC25.
- [WWDC24](https://developer.apple.com/documentation/updates/wwdc2024) - Highlights of new technologies introduced at WWDC24.
- [WWDC23](https://developer.apple.com/documentation/updates/wwdc2023) - Highlights of new technologies introduced at WWDC23.
- [WWDC22](https://developer.apple.com/documentation/updates/wwdc2022) - Highlights of new technologies introduced at WWDC22.
- [WWDC21](https://developer.apple.com/documentation/updates/wwdc2021) - Highlights of new technologies introduced at WWDC21.

### Technology Updates
- [Accelerate updates](https://developer.apple.com/documentation/updates/accelerate) - Learn about important changes to Accelerate.
- [Accessibility updates](https://developer.apple.com/documentation/updates/accessibility) - Learn about important changes to Accessibility.
- [ActivityKit updates](https://developer.apple.com/documentation/updates/activitykit) - Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](https://developer.apple.com/documentation/updates/adattributionkit) - Learn about important changes to AdAttributionKit.
- [App Clips updates](https://developer.apple.com/documentation/updates/appclips) - Learn about important changes in App Clips.
- [App Intents updates](https://developer.apple.com/documentation/updates/appintents) - Learn about important changes in App Intents.
- [AppKit updates](https://developer.apple.com/documentation/updates/appkit) - Learn about important changes to AppKit.
- [Apple Intelligence updates](https://developer.apple.com/documentation/updates/apple-intelligence) - Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](https://developer.apple.com/documentation/updates/applemapsserverapi) - Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](https://developer.apple.com/documentation/updates/applepencil) - Learn about important changes to Apple Pencil.
- [ARKit updates](https://developer.apple.com/documentation/updates/arkit) - Learn about important changes to ARKit.
- [Audio Toolbox updates](https://developer.apple.com/documentation/updates/audiotoolbox) - Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](https://developer.apple.com/documentation/updates/authenticationservices) - Learn about important changes to AuthenticationServices.
- [AVFAudio updates](https://developer.apple.com/documentation/updates/avfaudio) - Learn about important changes to AVFAudio.
- [AVFoundation updates](https://developer.apple.com/documentation/updates/avfoundation) - Learn about important changes to AVFoundation.
- [Background Tasks updates](https://developer.apple.com/documentation/updates/backgroundtasks) - Learn about important changes in Background Tasks.
- [Bundle Resources updates](https://developer.apple.com/documentation/updates/bundleresources) - Learn about important changes to Bundle Resources.
- [BrowserEngineKit reference](https://developer.apple.com/documentation/browserenginekit) - Consult the framework's browser-engine integration APIs and their individual requirements.
- [CallKit updates](https://developer.apple.com/documentation/updates/callkit) - Learn about important changes to CallKit.
- [ContactsUI updates](https://developer.apple.com/documentation/updates/contactsui) - Learn about important changes to ContactsUI.
- [Core Location updates](https://developer.apple.com/documentation/updates/corelocation) - Learn about important changes to Core Location.
- [Core MIDI updates](https://developer.apple.com/documentation/updates/coremidi) - Learn about important changes to Core MIDI.
- [Core ML updates](https://developer.apple.com/documentation/updates/coreml) - Learn about important changes to Core ML.
- [Core Motion updates](https://developer.apple.com/documentation/updates/coremotion) - Learn about important changes to Core Motion.
- [Core Spotlight updates](https://developer.apple.com/documentation/updates/corespotlight) - Learn about important changes to Core Spotlight.
- [DataDetection updates](https://developer.apple.com/documentation/updates/datadetection) - Learn about important changes in DataDetection.
- [Default apps updates](https://developer.apple.com/documentation/updates/defaultapps) - Learn about the latest changes to enabling your app to be the system default.
- [DockKit updates](https://developer.apple.com/documentation/updates/dockkit) - Learn about important changes to DockKit.
- [File Provider updates](https://developer.apple.com/documentation/updates/fileprovider) - Learn about important changes to File Provider.
- [FinanceKit updates](https://developer.apple.com/documentation/updates/financekit) - Learn more about changes to FinanceKit.
- [Foundation updates](https://developer.apple.com/documentation/updates/foundation) - Learn about important changes to Foundation.
- [Game Controller updates](https://developer.apple.com/documentation/updates/gamecontroller) - Learn about important changes to Game Controller.
- [GameKit updates](https://developer.apple.com/documentation/updates/gamekit) - Learn about important changes to GameKit.
- [Group Activities updates](https://developer.apple.com/documentation/updates/groupactivities) - Learn about important changes to Group Activities.
- [HealthKit updates](https://developer.apple.com/documentation/updates/healthkit) - Learn about important changes to HealthKit.
- [Hypervisor updates](https://developer.apple.com/documentation/updates/hypervisor) - Learn about important changes to Hypervisor.
- [Journaling Suggestions updates](https://developer.apple.com/documentation/updates/journalingsuggestions) - Learn about important changes in Journaling Suggestions.
- [LightweightCodeRequirements updates](https://developer.apple.com/documentation/updates/lightweightcoderequirements) - Learn about important changes to LightweightCodeRequirements.
- [LiveCommunicationKit updates](https://developer.apple.com/documentation/updates/livecommunicationkit) - Learn about important changes to LiveCommunicationKit.
- [MapKit updates](https://developer.apple.com/documentation/updates/mapkit) - Learn about important changes to MapKit.
- [MapKitJS updates](https://developer.apple.com/documentation/updates/mapkitjs) - Learn about important changes to MapKitJS.
- [Matter updates](https://developer.apple.com/documentation/updates/matter) - Learn about important changes to Matter.
- [Network updates](https://developer.apple.com/documentation/updates/network) - Learn about important changes to Network.
- [PassKit updates](https://developer.apple.com/documentation/updates/passkit) - Learn more about changes to PassKit.
- [PHASE updates](https://developer.apple.com/documentation/updates/phase) - Learn about important changes to PHASE.
- [PhotoKit updates](https://developer.apple.com/documentation/updates/photokit) - Learn about important changes to PhotoKit and PhotosUI.
- [ProximityReader updates](https://developer.apple.com/documentation/updates/proximityreader) - Learn about important changes to ProximityReader.
- [RealityKit updates](https://developer.apple.com/documentation/updates/realitykit) - Learn about important changes in RealityKit.
- [SafariServices updates](https://developer.apple.com/documentation/updates/safariservices) - Learn about important changes in SafariServices.
- [ScreenCaptureKit updates](https://developer.apple.com/documentation/updates/screencapturekit) - Learn about important changes to ScreenCaptureKit.
- [Security updates](https://developer.apple.com/documentation/updates/security) - Learn about important changes to Security.
- [SensorKit updates](https://developer.apple.com/documentation/updates/sensorkit) - Learn about important changes to SensorKit.
- [ShazamKit updates](https://developer.apple.com/documentation/updates/shazamkit) - Learn about important changes in ShazamKit.
- [SiriKit updates](https://developer.apple.com/documentation/updates/sirikit) - Learn about important changes in SiriKit.
- [StoreKit updates](https://developer.apple.com/documentation/updates/storekit) - Learn about important changes in StoreKit.
- [Swift updates](https://developer.apple.com/documentation/updates/swift) - Learn about important changes to Swift.
- [Swift Charts updates](https://developer.apple.com/documentation/updates/swiftcharts) - Learn about important changes to Swift Charts.
- [SwiftData updates](https://developer.apple.com/documentation/updates/swiftdata) - Learn about important changes to SwiftData.
- [SwiftUI updates](https://developer.apple.com/documentation/updates/swiftui) - Learn about important changes to SwiftUI.
- [Symbols updates](https://developer.apple.com/documentation/updates/symbols) - Learn about important changes to Symbols.
- [TipKit updates](https://developer.apple.com/documentation/updates/tipkit) - Learn about important changes in TipKit.
- [ThreadNetwork updates](https://developer.apple.com/documentation/updates/threadnetwork) - Learn about important changes in ThreadNetwork.
- [UIKit updates](https://developer.apple.com/documentation/updates/uikit) - Learn about important changes to UIKit.
- [User Notifications updates](https://developer.apple.com/documentation/updates/usernotifications) - Learn about important changes in User Notifications.
- [Video Subscriber Account updates](https://developer.apple.com/documentation/updates/videosubscriberaccount) - Learn about important changes in Video Subscriber Account.
- [Virtualization updates](https://developer.apple.com/documentation/updates/virtualization) - Learn about important changes to Virtualization.
- [Vision updates](https://developer.apple.com/documentation/updates/vision) - Learn about important changes in Vision.
- [watchOS updates](https://developer.apple.com/documentation/updates/watchos) - Learn about important changes to watchOS.
- [WeatherKit updates](https://developer.apple.com/documentation/updates/weatherkit) - Learn about important changes to WeatherKit.
- [WidgetKit updates](https://developer.apple.com/documentation/updates/widgetkit) - Learn about important changes in WidgetKit.
- [WorkoutKit updates](https://developer.apple.com/documentation/updates/workoutkit) - Learn about important changes to WorkoutKit.
- [Xcode updates](https://developer.apple.com/documentation/updates/xcode) - Learn about important changes to Xcode.
- [XCUIAutomation updates](https://developer.apple.com/documentation/updates/xcuiautomation) - Learn about important changes to XCUIAutomation.
- [XPC updates](https://developer.apple.com/documentation/updates/xpc) - Learn about important changes to XPC.

### Release Notes for SDKs, Xcode, and Safari
- [iOS & iPadOS Release Notes](https://developer.apple.com/documentation/ios-ipados-release-notes) - Learn about changes to the iOS & iPadOS SDK.
- [macOS Release Notes](https://developer.apple.com/documentation/macos-release-notes) - Learn about changes to the macOS SDK.
- [tvOS Release Notes](https://developer.apple.com/documentation/tvos-release-notes) - Learn about changes to the tvOS SDK.
- [watchOS Release Notes](https://developer.apple.com/documentation/watchos-release-notes) - Learn about changes to the watchOS SDK.
- [visionOS Release Notes](https://developer.apple.com/documentation/visionos-release-notes) - Learn about changes to the visionOS SDK.
- [Xcode Release Notes](https://developer.apple.com/documentation/xcode-release-notes) - Learn about changes to Xcode.
- [Safari Release Notes](https://developer.apple.com/documentation/safari-release-notes) - Review browser, embedded web-content, and Web Inspector changes; individual APIs have their own platform availability.

---

*Sources: [Apple Developer Documentation](https://developer.apple.com/documentation/updates); [developer release feed](https://developer.apple.com/news/releases/rss/releases.rss); [Apple security releases](https://support.apple.com/en-us/100100); [Xcode 27.1 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes); [Xcode 27.2 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes); [iOS/iPadOS 27.2 notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_2-release-notes); [macOS 27.2 notes](https://developer.apple.com/documentation/macos-release-notes/macos-27_2-release-notes); [Safari 27.1 notes](https://developer.apple.com/documentation/safari-release-notes/safari-27_1-release-notes); [Safari 27.2 notes](https://developer.apple.com/documentation/safari-release-notes/safari-27_2-release-notes); [Upcoming Requirements](https://developer.apple.com/news/upcoming-requirements/)*
