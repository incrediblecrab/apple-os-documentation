# macOS Tahoe 26.0 Developer Introduction

Maintain Mac apps using AppKit or SwiftUI, adopt Liquid Glass where appropriate, and expose useful actions through App Intents. macOS Tahoe 26 also provides on-device Foundation Models and new graphics capabilities; availability must be checked independently from the Mac's ability to run the OS.

**Platform:** macOS Tahoe 26.0+

> **Status checked September 8, 2026:** the shipping release is **macOS Tahoe 26.6.2** (`25G83`), released August 17. macOS Golden Gate 27 beta 8 was released August 31; see the [macOS 27 introduction](../os27-intro/macOS.md). Release listings do not establish a general-availability date or a complete supported-model list.

## Overview

Keep older-OS support and universal-binary decisions explicit. Rebuilding for a new SDK can change controls, menus, and window behavior without requiring you to discard your existing deployment targets. Profile on representative hardware and test permissions, keyboard navigation, and document recovery.

## Key Features

### New Design

**Say hello to Liquid Glass**  
Adopt system materials and review custom window chrome, toolbars, menus, and sidebars. Test contrast and transparency settings while preserving standard Mac interactions.

### Apple Intelligence

**Tap into the on-device large language model**  
Foundation Models gives eligible Macs on-device language-model access. Check model availability and handle unavailable or failed generation without blocking unrelated app features.

### Enhanced App Capabilities

**App Intents**  
Make your app's core functions available throughout macOS. Enable users to access your app's features through Spotlight, Shortcuts, and system-wide automation.

**Live Activities**  
Consider how an iPhone app's Live Activities appear on Mac through Continuity. Do not assume this provides a native macOS ActivityKit implementation with the same availability as the iPhone API.

**Enhanced Widgets**  
Use WidgetKit for supported desktop and Notification Center presentations. Test the OS26 appearance and timeline behavior without presenting earlier widget interactivity as a new Tahoe-only feature.

### Graphics and Performance

**Metal-powered games**  
Use Metal for graphics and compute workloads, and check the GPU requirements of Metal 4 features. Measure performance on the hardware you support.

**Video processing**

Use the documented AVFoundation and VideoToolbox APIs for capture, playback, and processing. Check codec and hardware support before offering an effect; “Video Effects” is not a substitute framework name.

### System Integration

**Menu Bar and Window Management**  
Adapt windows, menus, and custom chrome to the running system appearance and supported multitasking modes. Respect contrast and transparency settings instead of assuming an always-transparent menu bar.

**Desktop Customization**  
Respect system appearance, accent choices, and accessibility settings in your app's content and controls; app customization does not require changing the person's desktop.

## What's New in macOS Tahoe 26

Dive into the latest key technologies and capabilities:

- **Liquid Glass**: System appearance changes, with custom UI requiring review
- **Foundation Models**: On-device language-model access on eligible Macs
- **Metal 4**: Graphics features subject to GPU support
- **Widgets and App Intents**: Useful entry points outside your app's windows
- **Native Apple silicon builds**: Audit helpers and plug-ins as well as the main executable

### Maintenance and OS27 Preparation

- Use **26.6.2** as the current maintenance baseline while retaining the [26.0](https://developer.apple.com/documentation/macos-release-notes/macos-26-release-notes) and [26.6](https://developer.apple.com/documentation/macos-release-notes/macos-26_6-release-notes) notes for historical behavior.
- **Xcode 27 beta 6 runs on Apple silicon with macOS Tahoe 26.4 or later; macOS 27 is not required.** Intel Macs are not eligible Xcode 27 hosts, although its macOS SDK can build universal apps for older deployment targets.
- Plan for the [documented macOS 27 Rosetta and installer changes](../os27-intro/macOS.md). Running an Intel app under Rosetta and running Xcode on an Intel host are different questions.
- Audit [managed-service TLS](https://support.apple.com/en-us/126655), menu image visibility, and SwiftUI document migrations before upgrading production deployments. Mac Catalyst apps also need the UIKit scene life cycle when rebuilt with the latest SDK.
- Keep the [App Store readiness checklist](../guides/app-store-readiness.md) separate from Developer ID distribution and deployment-target choices.

## Getting Started

**New to macOS development?**  
Check out the [macOS Pathway](https://developer.apple.com/macos/get-started/), a collection of resources to get started with Mac app development.

## Developer Success Stories

### Masters of puppets
[Apple's Lies of P profile](https://developer.apple.com/news/?id=jimo1g6z) describes ROUND8 Studio's Mac game and features such as MetalFX upscaling.

### Assassin's Creed Shadows
[Apple's Ubisoft interview](https://developer.apple.com/news/?id=q2zte70j) discusses bringing Assassin's Creed Shadows to Mac using Apple silicon and Metal 3.

### The rise of Tide Guide
[Apple's Tide Guide profile](https://developer.apple.com/news/?id=4r9b23wx) follows Tucker MacDonald's development of a tide and weather app.

## Resources

### Development Tools
- [Xcode](https://developer.apple.com/xcode/) - Complete development environment for Mac apps
- [TestFlight](https://developer.apple.com/testflight/) - Beta testing platform for Mac applications
- [App Store Connect](https://developer.apple.com/app-store-connect/) - App management and analytics

### Documentation
- [macOS Release Notes](https://developer.apple.com/documentation/macos-release-notes)
- [AppKit Documentation](https://developer.apple.com/documentation/appkit/)
- [Metal Documentation](https://developer.apple.com/documentation/metal/)
- [VideoToolbox](https://developer.apple.com/documentation/videotoolbox/)

### Related Platforms
Build apps that integrate seamlessly across all Apple platforms:
- [iOS](iOS.md) - Mobile experiences
- [iPadOS](iPadOS.md) - Enhanced tablet experiences
- [tvOS](tvOS.md) - Living room entertainment
- [visionOS](visionOS.md) - Spatial computing
- [watchOS](watchOS.md) - Wearable experiences

## Support

### Meet with Apple
Sharpen your skills through in-person and online activities around the world. Connect with Apple engineers and designers to create powerful Mac experiences.

### Apple Developer Program
Join the [Apple Developer Program](Program.md) for TestFlight, Mac App Store distribution, Developer ID services, and other membership capabilities. Developer beta access is separate.

### Distribution Options
- **Mac App Store**: Reach customers worldwide with built-in discovery and payment processing
- **Developer ID**: Distribute outside the Mac App Store with notarization for user trust and security

---

*Platform requirements and feature availability may vary. Some capabilities and services may not be available in all regions or all languages.*

## Sources

[Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos), [Liquid Glass adoption](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass), and [SystemLanguageModel](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel) support the platform guidance. [Apple Developer releases](https://developer.apple.com/news/releases/), [security updates](https://support.apple.com/en-us/100100), [macOS 27 notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes), and [Xcode 27 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes) support the status and migration guidance checked September 8, 2026. Inline story sources describe historical examples.
