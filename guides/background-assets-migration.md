# Migrating On Demand Resources to Background Assets

**Review cutoff:** September 14, 2026; OS 27 release documentation and Xcode 27.

## Overview

The 27 SDK deprecates **On Demand Resources (ODR) and `NSBundleResourceRequest`** and directs developers to Background Assets. Deprecation does not mean immediate removal or automatic conversion of an existing ODR catalog.

Choose an asset-delivery design independently from your background-computation design. A managed asset pack, a background file transfer, and a continued-processing task solve different problems; none is a promise of unlimited background runtime.

## Choose the right mechanism

| Work | Appropriate mechanism | Important boundary |
| --- | --- | --- |
| Download and update additional app content as packs | Managed [Background Assets](../documentation/BackgroundAssets.md) | The system manages pack delivery; availability still needs checking. |
| Manage individual self-hosted app-asset downloads | Original Background Assets download APIs | Requires the unmanaged downloader configuration and lifecycle. |
| Transfer ordinary files while the app is inactive | Background `URLSession` | Transfer work runs outside the suspended app; it does not keep arbitrary application computation running. |
| Continue an export or other user-started computation after backgrounding | `BGContinuedProcessingTask` | Starts from a foreground user action; submission can queue or fail, and running work can expire or be cancelled. |
| Defer maintenance or refresh | `BGProcessingTask` or `BGAppRefreshTask` | Scheduling is discretionary, not an exact timer or a completion guarantee. |

## Availability and deployment planning

- Original download types such as `BADownloadManager` and `BAURLDownload` start at iOS/iPadOS/Mac Catalyst **16.1**, macOS 13, tvOS 18.4, and native visionOS 2.4. The umbrella framework's 16.0 catalog entry is not a valid availability guard for those classes.
- Managed asset-pack APIs start at version **26.0** on their supported iOS, iPadOS, Mac Catalyst, macOS, tvOS, and visionOS targets.
- Localized asset packs are a **27 SDK** addition. Guard their APIs separately from basic managed packs.
- Continued-processing APIs start at iOS/iPadOS 26.0, not BackgroundTasks' older framework minimum. The DocC Catalyst listing conflicts with explicit Catalyst exclusions in the public macOS 26.5 SDK; do not plan a Catalyst processing path from that catalog entry alone. See [BackgroundTasks](../documentation/BackgroundTasks.md).
- WatchOS is not an Apple-hosted managed Background Assets target. The `NSBundleResourceRequest` metadata also records watchOS deprecation, but this does not make the proposed pack replacement available there.
- Keep an availability-gated legacy delivery path when supporting operating systems that cannot use the replacement you choose. Do not raise every deployment target to 27 merely because a deprecation appears in that SDK.
- Do not assume ODR is that fallback on Mac Catalyst: Foundation explicitly documents that `NSBundleResourceRequest` ignores calls made by Catalyst apps, despite its Catalyst availability metadata.

Xcode 27 requires an **Apple silicon Mac running macOS Tahoe 26.6 or later**, not macOS 27. Building Universal or Intel app output, back-deploying Universal apps to macOS 12 and later, and Intel development with Rosetta-supporting macOS such as macOS 27 do not make an Intel Mac eligible to host Xcode 27.

## Map content and lifecycle explicitly

1. **Inventory ODR dependencies.** Record tags, files, launch-critical content, prefetch behavior, localization, and the code that assumes a bundle resource exists. ODR access follows successful request completion, and retaining the request protects its resources until access ends or the request is deallocated; do not assume managed packs inherit that retention contract.
2. **Design packs rather than renaming tags.** Group files that are downloaded together, assign stable pack IDs, and define how the app finds each resource. Review overlapping file paths and version compatibility.
3. **Choose download policies.** `essential` participates in installation; `prefetch` can continue after installation; `onDemand` waits for an explicit request. Even essential packs can require a later availability request after network failures.
4. **Configure the correct extension.** For Apple hosting, use the appropriate managed Background Download template and StoreKit's [`StoreDownloaderExtension`](https://developer.apple.com/documentation/storekit/storedownloaderextension), which inherits from `ManagedDownloaderExtension`. Share an App Group, set the string `BAAppGroupID`, and enable the Boolean keys `BAHasManagedAssetPacks` and `BAUsesAppleHosting`. Self-hosted managed packs use `ManagedDownloaderExtension`. Do not carry unmanaged-download keys or callback overrides into the Apple-hosted configuration.
5. **Replace access and readiness checks.** Use `AssetPackManager` to obtain packs, ensure local availability, observe progress, and locate content. A previously requested download is not a substitute for a successful availability check.
6. **Plan updates and removal.** Test app/pack version combinations. Managed packs are not automatically removed simply because they become unused; remove unneeded packs explicitly. Do not translate ODR retention behavior into an assumed identical eviction policy.
7. **Keep failure recoverable.** Account for offline launch, interrupted downloads, cancelled progress, unavailable files, storage failures, and partial batch success. Preserve enough state for a retry without presenting missing content as ready.

Follow Apple's [pack creation](https://developer.apple.com/documentation/backgroundassets/creating-managed-asset-packs) and [download integration](https://developer.apple.com/documentation/backgroundassets/downloading-apple-hosted-asset-packs) guides for the packaging commands and exact API signatures.

## Add localized packs on supported 27 targets

Xcode 27's `ba-package` manifest template includes `language`. Use an ISO-639 language identifier with optional BCP-47 region and script subtags; variant subtags and extensions are unsupported.

Use the manifest's `localizedAssetPacks` to find the system-preferred packs. If the app offers its own language selection, update `AssetPackManager.resolvedLanguage`; assigning `nil` restores the system preference. Changing the property alone does not change downloaded content. Call `reconcilePreferredLanguages()` when you want the manager to download needed packs and remove unneeded ones. This operation does not remove localized packs you downloaded manually.

For simultaneous languages—for example, spoken audio and subtitles—request the required packs together and use language-aware content accessors. Handle `LocalAvailabilityError.successes` and `failures` independently. Show progress and a fallback when the selected language is not yet available.

## Keep downloads separate from inference

A downloaded model is an asset; executing it is computation. Background Assets does not grant CPU, GPU, or Neural Engine runtime.

On the 27 operating systems, **any background Neural Engine access** requires `com.apple.developer.background-tasks.continued-processing.inference`, including inference through Core AI, Core ML, or Metal Performance Shaders Graph and work outside a continued-processing task. This entitlement does not schedule the work or guarantee hardware access.

For a user-initiated continued-processing task, choose a submission strategy, report progress, and stop promptly when its expiration handler runs. Device and system resource constraints still apply. The separate background GPU entitlement and supported-resource checks do not replace the inference entitlement.

## Validate the migration

- Test managed packs with Xcode's local mock server, then test the intended distribution and hosting configuration.
- Exercise first installation, upgrade, offline launch, failed essential downloads, interrupted downloads, explicit removal, and redownload.
- Test supported older OS versions without entering 26/27-only code.
- Change system and app-specific languages, including a batch where only some packs succeed.
- Test cancellation, resource-pressure submission failure, and app-switcher termination of continued processing.
- Confirm that file-transfer completion is not being used as an assumption of additional background compute time.

## Primary sources

- [iOS/iPadOS 27 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes.md)
- [NSBundleResourceRequest availability and deprecation](https://developer.apple.com/tutorials/data/documentation/foundation/nsbundleresourcerequest.json)
- [Background Assets overview](https://developer.apple.com/documentation/backgroundassets.md)
- [Managed asset-pack availability](https://developer.apple.com/tutorials/data/documentation/backgroundassets/assetpackmanager.json)
- [Localized asset packs](https://developer.apple.com/documentation/backgroundassets/reducing-download-and-storage-demands-with-localized-asset-packs.md)
- [Downloading files in the background](https://developer.apple.com/documentation/foundation/downloading-files-in-the-background.md)
- [Performing long-running tasks on iOS and iPadOS](https://developer.apple.com/documentation/backgroundtasks/performing-long-running-tasks-on-ios-and-ipados.md)
- [Background inference entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.background-tasks.continued-processing.inference.md)
- [Xcode 27 release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes.md)
