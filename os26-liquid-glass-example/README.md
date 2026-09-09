# Landmarks: Building an app with Liquid Glass

An iOS, iPadOS, and macOS sample demonstrating system controls and custom Liquid Glass.
The deployment minimums remain **26.0**; the project remains in **Swift 6 language
mode**. There are no watchOS, tvOS, visionOS, or Mac Catalyst product targets.

## Overview

The app retains SwiftUI `@State` ownership of an `@Observable`, `@MainActor` model.
Its collection and favorite changes are in-memory sample behavior, not a production
persistence implementation.

| Example | Source |
|---|---|
| App lifecycle and model ownership | [LandmarksApp.swift](Landmarks/Landmarks/LandmarksApp.swift) |
| Collections, favorites, navigation, map lookups | [ModelData.swift](Landmarks/Landmarks/Model/ModelData.swift) |
| Glass containers, identifiers, and badge transitions | [BadgesView.swift](Landmarks/Landmarks/Views/Badges/BadgesView.swift) |
| Bounded model regression tests | [ModelDataTests.swift](Landmarks/LandmarksTests/ModelDataTests.swift) |
| Independent type-check fixtures | [Liquid Glass](Snippets/LiquidGlass.swift) and [Swift 6.3 weak let](Snippets/WeakLet.swift) |

## Build and run

Use an Xcode toolchain containing the required SDKs. The recorded local baseline
is Xcode 26.6 (`17F113`), Swift 6.3.3, and macOS/iOS 26.5 SDKs on an arm64
macOS 26.6.2 host. Do not mistake the SDK version for the compiler or host version.

```bash
open os26-liquid-glass-example/Landmarks/Landmarks.xcodeproj

xcodebuild -project os26-liquid-glass-example/Landmarks/Landmarks.xcodeproj \
  -scheme Landmarks -destination 'platform=macOS,arch=arm64' \
  CODE_SIGNING_ALLOWED=NO build

xcodebuild -project os26-liquid-glass-example/Landmarks/Landmarks.xcodeproj \
  -scheme Landmarks -destination 'generic/platform=iOS Simulator' \
  CODE_SIGNING_ALLOWED=NO build
```

These commands run from the repository root and avoid provisioning for local builds.
Device distribution still needs appropriate signing, capabilities, and review.

Pass `--offline-demo` as a launch argument to disable the sample's startup map-item
lookups. Bundled landmarks, favorites, and collections remain usable without that
service. The argument does not emulate a denied location permission, prevent a
MapKit view from requesting map tiles, or turn every network operation into a mock.
Normal map lookup failures now produce diagnostic messages instead of being silently
discarded. Badge expansion suppresses its explicit animation when Reduce Motion is enabled.

## Repeatable checks

The shared scheme contains a hosted test target. Its test action uses
`--offline-demo`; the tests also construct models with `loadMapItems: false`.
They cover the actual app module rather than copies of its model or generated
localization symbols.

```bash
# Use a new output directory; existing result bundles are never deleted by the script.
bash scripts/check_sample.sh /tmp/landmarks-xcode26-check
```

The script checks the selected Xcode major version, type-checks both independent
fixtures, runs at least seven model tests on macOS, and builds the iOS simulator
application. The `weak let` fixture requires Swift 6.3 or later; it is not compiled
into the app and does not raise the app's deployment target.

For a separately installed beta, select it only for the command:

```bash
DEVELOPER_DIR=/Applications/Xcode-beta.app/Contents/Developer \
  EXPECTED_XCODE_MAJOR=27 \
  bash scripts/check_sample.sh /tmp/landmarks-xcode27-check
```

Replace that example path with the actual installed bundle. Xcode 27 beta 6
requires Apple silicon and macOS Tahoe 26.4 or later, not macOS 27. The script fails if the selected
toolchain is not the requested major version; it does not silently test Xcode 26
and report a beta success.

The [sample workflow](../.github/workflows/sample.yml) uses the officially listed
`macos-26` runner with Xcode 26.6. A manual `run_beta` option uses the documented
`xcode-27` preview runner. Runner availability was checked against the
[official image inventory](https://github.com/actions/runner-images);
writing a workflow is not evidence that a hosted run passed.

## Recorded scope and remaining work

As of September 8, 2026, local macOS builds, the iOS simulator build, both Swift
fixture type-checks, and all seven model tests on both macOS and an isolated iPhone 17
simulator running iOS 26.5 passed under the baseline above.
The earliest 26.0 runtime and OS 27 toolchain were not exercised in that local run.
No physical-device, real-service, or comprehensive visual-accessibility pass is claimed.

Before release, explicitly exercise:

- iPhone/iPad navigation, collection editing, layout resizing, and Mac keyboard navigation.
- VoiceOver labels and order, largest Dynamic Type, RTL/localization, and focus visibility.
- Reduce Motion, Reduce Transparency, Increase Contrast, and badge appearance over varied content.
- Location denied/revoked, network failures, and map-service recovery on real destinations.

The model checks do not substitute for those interaction and accessibility checks.
Do not add unrelated platform or intelligence targets merely to increase framework coverage.

## Attribution

Retain [Apple's sample license](LICENSE.txt). Its software grant excludes accompanying
photographs; [asset provenance and rights](../metadata/assets.json) remain separate
from whether the app builds. No replacement images or blanket redistribution license
were added.

*Source: [Landmarks: Building an app with Liquid Glass](https://developer.apple.com/documentation/swiftui/landmarks-building-an-app-with-liquid-glass)*
