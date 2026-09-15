# Apple silicon

Get the resources you need to create software for Macs with Apple silicon.

## Overview

Build apps, libraries, frameworks, plug-ins, and other executable code that run natively on Apple silicon. When you build executables on top of Apple frameworks and technologies, the only significant step you might need to take is to recompile your code for the arm64 architecture. If you rely on hardware-specific details or make assumptions about low-level features, modify your code as needed to support Apple silicon.

Getting the best performance on Apple silicon sometimes requires making adjustments to the way you use hardware resources. Minimize your dependence on the hardware by using higher-level technologies whenever possible. For example, use Grand Central Dispatch instead of creating and managing threads yourself. Test your changes on Apple silicon to verify that your code behaves optimally.

## OS27 Toolchain and Rosetta Planning

**Checked September 8, 2026; updated for September 14 GA:** macOS 27 Golden Gate 27.0 (`26A428`) and Xcode 27 (`27A266a`) shipped September 14, 2026. macOS Tahoe 26.6.2, released August 17, is the previous macOS shipping baseline. See [Apple's release list](https://developer.apple.com/news/releases/).

| Question | Verified distinction |
|---|---|
| Can this Mac host Xcode 27? | It must be an **Apple silicon Mac running macOS Tahoe 26.6 or later**. macOS 27 is not required; Intel Macs are not eligible hosts. |
| Can Xcode 27 build for older Intel Macs? | Its macOS 27 SDK supports universal Intel/Apple-silicon apps that back-deploy to **macOS 12 or later**. Choose your deployment target and architectures independently. |
| Can an Intel executable run on an Apple silicon Mac? | Rosetta is a translation environment, not a way to make Intel hardware satisfy Xcode's host requirement. Test each executable and its dependencies. |

Source for the host and universal-build requirements: [Xcode 27 release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes), including “Intel Deprecation.”

With a minimum macOS or DriverKit deployment target of 27 or later, `ARCHS_STANDARD` omits `x86_64`. The notes permit an explicit `ARCHS` setting to include it; do not confuse that build choice with Intel-host eligibility or an OS supported-model list (161837535).

The [macOS 27 notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes) say that Rosetta is not automatically restored after an OS upgrade, apps previously set to open with Rosetta launch natively, and installer packages without `hostArchitecture` default to `arm64`. Audit installer scripts, plug-ins, helper executables, and build tools—not just the main app.

Apple also states that Intel-based software will not be compatible with macOS 28, excluding legacy games. That documented future direction is not a claim that every Intel app is already unusable on macOS 27. The precise macOS 27 model list is not verified here; do not derive one solely from an Apple-silicon chip family. Retain universal builds and earlier-platform tests where your supported audience still needs them.

## Topics

### Essentials
- [Porting your macOS apps to Apple silicon](https://developer.apple.com/documentation/Apple-Silicon/porting-your-macos-apps-to-apple-silicon) - Create a version of your macOS app that runs on both Apple silicon and Intel-based Mac computers.
- [Building a universal macOS binary](https://developer.apple.com/documentation/Apple-Silicon/building-a-universal-macos-binary) - Create macOS apps and other executables that run natively on both Apple silicon and Intel-based Mac computers.

### General porting tips
- [Addressing architectural differences in your macOS code](https://developer.apple.com/documentation/Apple-Silicon/addressing-architectural-differences-in-your-macos-code) - Fix problems that stem from architectural differences between Apple silicon and Intel-based Mac computers.
- [Porting your audio code to Apple silicon](https://developer.apple.com/documentation/Apple-Silicon/porting-your-audio-code-to-apple-silicon) - Eliminate issues in your audio-specific code when running on Apple silicon Mac computers.
- [Porting just-in-time compilers to Apple silicon](https://developer.apple.com/documentation/Apple-Silicon/porting-just-in-time-compilers-to-apple-silicon) - Update your just-in-time (JIT) compiler to work with the Hardened Runtime capability, and with Apple silicon.

### Graphics
- [Porting your Metal code to Apple silicon](https://developer.apple.com/documentation/Apple-Silicon/porting-your-metal-code-to-apple-silicon) - Create a version of your Metal app that runs on both Apple silicon and Intel-based Mac computers.

### Performance
- [Tuning your code's performance for Apple silicon](https://developer.apple.com/documentation/apple-silicon/tuning-your-code-s-performance-for-apple-silicon) - Improve your code to get the best performance from both Apple silicon and Intel-based Mac computers.
- [Apple Silicon CPU Optimization Guide](https://developer.apple.com/documentation/apple-silicon/cpu-optimization-guide) - Identify performance optimization strategies for Apple silicon M-series and A-series chips.

### Rosetta
- [About the Rosetta translation environment](https://developer.apple.com/documentation/Apple-Silicon/about-the-rosetta-translation-environment) - Learn how Rosetta translates executables, and understand what Rosetta can't translate.

### iOS apps on Mac
- [Running your iOS apps in macOS](https://developer.apple.com/documentation/Apple-Silicon/running-your-ios-apps-in-macos) - Modernize the iOS apps you choose to run on a Mac with Apple silicon, or opt out of running on a Mac altogether.
- [Adapting iOS code to run in the macOS environment](https://developer.apple.com/documentation/Apple-Silicon/adapting-ios-code-to-run-in-the-macos-environment) - Support modern iOS features that result in a better user experience when running on Apple silicon.
- [Providing touch gesture equivalents using Touch Alternatives](https://developer.apple.com/documentation/Apple-Silicon/providing-touch-gesture-equivalents-using-touch-alternatives) - Enable Touch Alternatives to provide keyboard, mouse, and trackpad equivalents to your iOS app when it runs on a Mac with Apple silicon.
- [Providing an edge-to-edge, full-screen experience in your iPad app running on a Mac](https://developer.apple.com/documentation/Apple-Silicon/providing-an-edge-to-edge-full-screen-experience-in-your-ipad-app-running-on-a-mac) - Take advantage of the true native resolution of a Mac display when running your iPad app in full-screen mode on a Mac.

### Kernel and drivers
- [Implementing drivers, system extensions, and kexts](https://developer.apple.com/documentation/kernel/implementing_drivers_system_extensions_and_kexts) - Create drivers and system extensions to communicate with hardware and provide low-level services, and only use kernel extensions for a few tasks.
- [Installing a custom kernel extension](https://developer.apple.com/documentation/Apple-Silicon/installing-a-custom-kernel-extension) - Install kernel extensions using a custom installer package, and help users understand the installation process.
- [Debugging a custom kernel extension](https://developer.apple.com/documentation/Apple-Silicon/debugging-a-custom-kernel-extension) - Configure your system to enable the debugging of custom kernel extensions from a second Mac.

### Security
- [Improving control flow integrity with pointer authentication](https://developer.apple.com/documentation/Apple-Silicon/improving-control-flow-integrity-with-pointer-authentication) - Increase confidence that your code uses pointers correctly.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/apple-silicon)*
