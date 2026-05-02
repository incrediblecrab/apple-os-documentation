# iOS 26.0 Developer Introduction

Create great apps and games for the world's most advanced mobile operating system. Take advantage of the new design, which elevates the content people care about most — and creates a unified design across Apple platforms. And with Apple Intelligence, you can bring personal intelligence into your apps to deliver new capabilities, all with great performance and built-in privacy.

**Platform:** iOS 26.0+

## Overview

iOS 26.0 introduces groundbreaking features and design improvements that enhance user experiences across iPhone devices. This release focuses on Liquid Glass design, Apple Intelligence integration, and powerful new capabilities for developers.

## Key Features

### New Design

**Say hello to Liquid Glass**  
Experience the revolutionary new design system that combines the optical properties of glass with fluid dynamics. Liquid Glass creates a translucent material that reflects and refracts its surroundings while dynamically transforming to bring greater focus to content.

### Apple Intelligence

**Tap into the on-device large language model**  
Integrate Apple's powerful on-device AI capabilities to deliver intelligent features with privacy at the core. Apple Intelligence enables natural language processing, content generation, and smart automation without compromising user data.

### Enhanced App Capabilities

**App Intents**  
Make your app's core functions available throughout the system with App Intents. Enable users to access your app's features through Siri, Shortcuts, and system-wide search.

**Live Activities**  
Provide important information right now with Live Activities. Keep users updated with real-time information that appears on the Lock Screen and in the Dynamic Island.

**Widgets**  
Deliver timely and relevant information with enhanced widget capabilities. iOS 26.0 expands widget functionality and customization options.

**Notifications**  
Communicate with users even when your app isn't running. Enhanced notification features provide richer, more interactive experiences.

### Gaming and Graphics

**Metal-powered games**  
Create games with astonishing realism and incredible creativity. Metal provides low-level access to GPU capabilities for maximum performance.

### Security

**Powerful passkeys**  
Implement secure, easy, and unphishable authentication with passkeys. Replace passwords with biometric authentication and cryptographic security.

## What's New in iOS 26

Dive into the latest key technologies and capabilities:

- **Liquid Glass Design System**: Revolutionary visual effects and materials
- **Apple Intelligence**: On-device AI capabilities with privacy protection
- **Enhanced Widgets**: More customization and functionality
- **Advanced Live Activities**: Real-time information display
- **Improved App Intents**: System-wide app integration
- **Metal 4**: Next-generation graphics performance
- **Enhanced Security**: Advanced authentication and privacy features

### iOS 26.1 Updates (November 2025)
- Interface refinements and performance improvements
- Bug fixes and stability enhancements

### iOS 26.2 Updates
- **Hypertension Notifications API**: Authorize `HKCategoryTypeIdentifierHypertensionEvent` to read hypertension notifications from Apple Watch
- **StoreKit `AppStore.ageRatingCode`**: Fetch the current age rating code for your app to detect rating changes
- **DeclaredAgeRange fixes**: Recompile against the 26.2 SDK to resolve runtime crashes in age-range APIs
- **TLS Client Hello updated**: Servers with strict bot-detection should adopt resilient policies that handle TLS fingerprint changes

### iOS 26.3 Updates
- **StoreKit fix**: `Product.products(for:)` now throws errors instead of failing silently

### iOS 26.4 Updates
- **Memory Integrity Enforcement (MIE)**: Apps can opt in to full MIE protections for enhanced memory safety (previously limited to Soft Mode)
- **Background Assets offline status**: Check asset-pack status offline via `localStatus(ofAssetPackWithID:)` and `assetPackIsAvailableLocally(withID:)`
- **Background Assets latest version**: Use `ensureLocalAvailability(of:requireLatestVersion:)` to keep asset packs current
- **StoreKit revocation fields**: New `Transaction.revocationType` and `Transaction.revocationPercentage` properties
- **RCS end-to-end encryption (developer testing)**: Cross-platform RCS E2EE available in beta between Apple and Android devices
- **AudioAccessoryKit (developer testing)**: Third-party audio accessory makers can provide headphone information for automatic audio switching
- **Accessory Notifications Framework (developer testing)**: Accessory companion apps can request notification forwarding via an extension model
- **SwiftUI fix**: `.userActivity` now correctly surfaces as the current user activity
- **Networking fix**: Resolves `CFRunLoopSource` leaks when PAC or Auto proxy discovery is configured

### iOS 26.5 (Developer Beta — Beta 4 as of May 2026)
- Update your apps to use the new features and test against API changes
- See the [iOS & iPadOS 26.5 Beta 4 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-26_5-release-notes) for the latest changes

## Getting Started

**New to iOS development?**  
Check out the [iOS Pathway](https://developer.apple.com/ios/), an easy-to-navigate collection of resources to get started with iOS app development.

## Developer Success Stories

### Learning to fly
Find out how Ryan Jones built the all-in-one travel companion Flighty, taking advantage of iOS features for seamless travel tracking.

### A gentler approach
Learn how the Gentler Streak team took advantage of iOS features to approach fitness with "humanity," creating a more inclusive fitness experience.

### A photo finish
Here's how the Halide Mark II team brought the power of DSLR photography to iOS with advanced camera controls and professional editing capabilities.

## Resources

### Development Tools
- [Xcode](https://developer.apple.com/xcode/) - Complete development environment
- [TestFlight](https://developer.apple.com/testflight/) - Beta testing platform
- [App Store Connect](https://developer.apple.com/app-store-connect/) - App management and analytics

### Documentation
- [iOS Developer Documentation](https://developer.apple.com/documentation/ios/)
- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)

### Related Platforms
Build apps that integrate seamlessly across all Apple platforms:
- [iPadOS](iPadOS.md) - Enhanced iPad experiences
- [macOS](macOS.md) - Desktop and laptop applications  
- [tvOS](tvOS.md) - Living room entertainment
- [visionOS](visionOS.md) - Spatial computing
- [watchOS](watchOS.md) - Wearable experiences

## Support

### Meet with Apple
Sharpen your skills through in-person and online activities around the world. Connect directly with Apple engineers and designers to create your best apps and games.

### Apple Developer Program
Join the [Apple Developer Program](Program.md) to access beta software, advanced app capabilities, extensive beta testing tools, and App Store distribution.

---

*Platform requirements and feature availability may vary. Some capabilities and services may not be available in all regions or all languages.*