# Xcode

Build, test, and submit your app with Apple's integrated development environment.

## Overview

Xcode is a suite of tools developers use to build apps for Apple platforms. Use Xcode to manage your entire development workflow — from creating your app to testing, optimizing, and submitting it to the App Store.

The documentation's illustration shows SwiftUI code and an iOS device preview in Xcode on a MacBook Pro.

Xcode includes a world-class code editor, built in SwiftUI preview tools that show the UI of your app as you modify code, and a powerful debugger with conditional breakpoints.

Xcode also includes tools for prototyping, testing, and measurement. Use Simulator when a physical device isn't needed, and Instruments to investigate performance and resource use. See [Reality Composer Pro](RealityComposerPro.md) for 3D content authoring, [Create ML](CreateML.md) for model training, and Accessibility Inspector for accessibility diagnostics.

Note

Download the latest version of Xcode from the Mac App Store. Download beta versions of Xcode from the Apple Developer website.

## Xcode 27

Xcode 27 (`27A266a`) shipped September 14, 2026. The [release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes.md) specify an **Apple silicon Mac running macOS Tahoe 26.6 or later**. The Overview establishes the host OS; the Intel Deprecation section explicitly states that Xcode 27 installs and runs only on Apple silicon, that the macOS 27 SDK supports back deploying Universal apps to macOS 12 and later, and that Intel development remains possible with Rosetta-supporting macOS such as macOS 27. This is not an inference from Rosetta or a macOS 27 deployment requirement. Consult [Xcode Support](https://developer.apple.com/support/xcode/) for compatible hosts and deployment targets.

The macOS 27 SDK still supports universal-app back-deployment to macOS 12 and later. Separately, `ARCHS_STANDARD` no longer includes `x86_64` by default when the minimum deployment target is macOS 27 or DriverKit 27; the notes permit adding it explicitly to `ARCHS` when needed (161837535). A universal output binary does not make Intel hardware an eligible IDE host.

**Toolchain**

Xcode 27 includes the **Swift 6.4 compiler** and iOS, iPadOS, macOS, tvOS, watchOS, and visionOS 27 SDKs. Compiler version is not Swift language mode. Record both, together with SDK and run-destination versions, in local and [CI](Xcode-Cloud.md) results.

**Testing**

Use [Swift Testing](Testing.md) for new Swift unit tests, [XCTest](XCTest.md) with [XCUIAutomation](XCUIAutomation.md) for UI tests, and XCTest for performance tests. [App Intents Testing](AppIntentsTesting.md) exercises registered intents and queries out-of-process from a UI testing bundle. [Evaluations](Evaluations.md) adds dataset-based quality measurement and Swift Testing integration; it complements deterministic tests.

### Profiling

- The Foundation Models instrument inspects instructions, prompts, responses, token use, and inference timing. [Core AI](CoreAI.md) has its own debug gauge and instrument.
- Swift Executors shows the cooperative thread pool, Main Actor, and custom executors. Executor names are properly captured on OS 27; older runtimes can show “Unknown executor.”
- Record Swift Concurrency together with Time Profiler or CPU Profiler to enable its **Profile** call-tree detail. Use this to distinguish CPU work from queued or suspended tasks.
- `xctrace record` accepts `--show-recording-options` and `--recording-options <json path>` for template-specific recording settings. `xctrace export` can read `.atrc` and `.logarchive` inputs directly.
- Instruments requires at least iOS 17, tvOS 17, or watchOS 10 on those target devices. A new instrument's richer data may require a newer runtime.

**Outstanding release-note limitations**

The release notes still list delayed multi-process console output (165098287), unreliable input extraction from Core AI prediction events (172502576), and limitations in Device Hub input and device visualization. These affect diagnosis, not just app code. In Xcode 27, `xctrace record` failing to start for simulator targets is listed as **fixed** (183624872). Verify against the selected toolchain rather than treating every earlier beta issue as current.

## Topics

### Essentials
- [Creating an Xcode project for an app](https://developer.apple.com/documentation/xcode/creating-an-xcode-project-for-an-app.md) - Start developing your app by creating an Xcode project from a template.
- [Interacting with previews in the canvas](https://developer.apple.com/documentation/xcode/interacting-with-previews-in-the-canvas.md) - Exercise an interface and adjust preview configurations in the canvas.
- [Adding previews to your interface files](https://developer.apple.com/documentation/xcode/adding-previews-to-your-interface-files.md) - Add previews for SwiftUI, UIKit, or AppKit interface code.
- [Running your app on simulated or physical devices](https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices.md) - Build and launch the app on a selected run destination.
- [Xcode updates](https://developer.apple.com/documentation/updates/xcode.md) - Learn about important changes to Xcode.

### Xcode IDE
- [Projects and workspaces](https://developer.apple.com/documentation/xcode/projects-and-workspaces.md) - Manage the code and resources you use to build apps, libraries, and other software for Apple platforms.
- [Source control management](https://developer.apple.com/documentation/xcode/source-control-management.md) - Back up your files, collaborate with others, and tag your releases with source control support in Xcode.
- [Capabilities](https://developer.apple.com/documentation/xcode/capabilities) - Enable services that Apple provides, such as In-App Purchase, Push Notifications, Apple Pay, iCloud, and many others.
- [Build system](https://developer.apple.com/documentation/xcode/build-system.md) - Compile your code into a binary format, and customize your project settings to build your code.

### Code
- [Source Editor](https://developer.apple.com/documentation/xcode/source-editor.md) - Edit your source files, locate issues, and make necessary changes using the Source Editor.
- [Bundles and frameworks](https://developer.apple.com/documentation/xcode/bundles-and-frameworks.md) - Organize code and resources in bundles and frameworks.
- [Swift packages](https://developer.apple.com/documentation/xcode/swift-packages.md) - Create reusable code, organize it in a lightweight way, and share it across Xcode projects and with other developers.

### Interface
- [Asset management](https://developer.apple.com/documentation/xcode/asset-management.md) - Add app icons, images, strings, data files, machine learning models, and other resources to your projects, and manage how you load them at runtime.
- [Localization](https://developer.apple.com/documentation/xcode/localization) - Expand the market for your app by supporting multiple languages and regions.
- [Accessibility Inspector](https://developer.apple.com/documentation/accessibility/accessibility-inspector.md) - Reveal how your app represents itself to people using accessibility features.

### Documentation
- [Writing documentation](https://developer.apple.com/documentation/xcode/writing-documentation.md) - Produce rich and engaging developer documentation for your apps, frameworks, and packages.

### Tuning and debugging
- [Device Hub](https://developer.apple.com/documentation/xcode/device-hub.md) - Manage physical devices and simulators and inspect supported device interactions.
- [Debugging](https://developer.apple.com/documentation/xcode/debugging) - Identify and address issues in your app using the Xcode debugger, Xcode Organizer, Metal debugger, and Instruments.
- [Performance and metrics](https://developer.apple.com/documentation/xcode/performance-and-metrics.md) - Measure, investigate, and address the use of system resources and issues impacting performance using Instruments and Xcode Organizer.
- [Testing](https://developer.apple.com/documentation/xcode/testing) - Develop and run tests to detect logic failures, UI problems, and performance regressions.

### Distribution and continuous integration
- [Distribution](https://developer.apple.com/documentation/xcode/distribution) - Prepare your app and share it with your team, beta testers, and customers.
- [Xcode Cloud](https://developer.apple.com/documentation/xcode/xcode-cloud.md) - Automatically build, test, and distribute your apps with Xcode Cloud to verify changes and create high-quality apps.

### Hardware considerations
- [Apple silicon](https://developer.apple.com/documentation/apple-silicon.md) - Get the resources you need to create software for Macs with Apple silicon.
- [Application binary interfaces](https://developer.apple.com/documentation/xcode/application-binary-interfaces.md) - Write assembly instructions that adhere to the application binary interfaces of Apple platforms.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Xcode)*
