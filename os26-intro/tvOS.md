# tvOS 26.0 Developer Introduction

Maintain Apple TV apps with predictable focus navigation, readable media catalogs, and resilient playback. SwiftUI, UIKit, AVKit, and established Continuity features remain useful across the OS26 generation; check hardware support rather than assuming every television device exposes the same capabilities.

**Platform:** tvOS 26.0+

> **Status checked September 14, 2026:** the shipping release is **tvOS 26.6** (`23L773`), released July 27. tvOS 27.0 (`24J361`) shipped September 14; see the [tvOS 27 introduction](../os27-intro/tvOS.md).

## Overview

Design for viewing at a distance and interaction through a remote, controller, or accessibility feature. Keep focus visible over moving artwork and ensure network or account failures do not strand the user in a player or loading screen.

## Key Features

### User Interface and Navigation

**SwiftUI for tvOS**  
Use SwiftUI's supported tvOS controls and layouts, then test focus, viewing distance, and accessibility. Sharing UI code does not guarantee an appropriate television interface.

**Enhanced Sidebar Support**  
Customize your navigation experience to match your brand and catalog. Create immersive content browsing with dynamic sidebars that provide quick access to categories, recommendations, and user preferences.

**Focus-Based Navigation**  
Leverage tvOS's unique focus engine to create intuitive navigation experiences. Design interfaces that feel natural with the Siri Remote and support accessibility features.

### Media and Entertainment

**Video Player Enhancements**  
Use AVKit and AVFoundation for playback, and check supported media formats and output capabilities. Handle buffering, interruptions, subtitles, and playback errors explicitly.

**Spatial Audio Support**  
Offer supported Spatial Audio experiences on compatible Apple TV and audio-output configurations. Check the route and capabilities rather than assuming every headset or television supports them.

**Content Discovery**  
Evaluate the approved TV app integration route and supported Siri media capabilities for your service; ordinary App Store membership does not automatically grant every content-discovery integration.

### Connectivity and Integration

**Enhanced iPhone Integration**  
Use supported Continuity features to connect an iPhone or iPad for camera and microphone input. Handle connection loss and consent instead of assuming a second device is always available.

**Persistent Continuity Camera**  
Where supported, use persistent Continuity Camera connections to reduce repeated setup for calls or interactive experiences. Persistence does not eliminate availability and reconnection handling.

**Game Controller Support**  
Discover supported game controllers and test their input profiles. Handle the Siri Remote's navigation separately rather than assuming all remotes and controllers provide identical buttons or motion input.

### Performance and Capabilities

**Apple TV 4K Optimization**  
Take full advantage of Apple TV 4K hardware with optimized graphics performance, HDR support, and efficient memory management.

**Metal for tvOS**  
Create stunning visual experiences and games with Metal, optimized for television displays and living room viewing distances.

## OS26 Adoption and Maintenance

The following are adoption checks, not claims that every capability debuted in tvOS 26:

- Review system controls and custom navigation with the OS26 appearance.
- Test returning focus after player dismissal, profile changes, and failed authentication.
- Check audio, video, and game-controller capabilities before offering dependent features.
- Preserve accessible playback controls and meaningful loading/error states.
- The [tvOS 26.0 notes](https://developer.apple.com/documentation/tvos-release-notes/tvos-26-release-notes) describe design updates for Apple TV 4K second- and third-generation models, not first-generation and older devices. Do not equate OS installation support with support for every appearance feature.
- Use [26.6 notes](https://developer.apple.com/documentation/tvos-release-notes/tvos-26_6-release-notes) and [security updates](https://support.apple.com/en-us/100100) for the shipping baseline.

### Preparing an OS26 App for OS27

- UIKit apps built with the latest SDK must adopt [scenes](https://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle) or fail to launch on tvOS 27. Multiwindow UI is not required.
- Migrate ODR/`NSBundleResourceRequest` usage to Background Assets and test missing or evicted resources.
- Finish appearance work: [`UIDesignRequiresCompatibility`](https://developer.apple.com/documentation/bundleresources/information-property-list/uidesignrequirescompatibility) is ignored by tvOS 27 builds.
- Use the [tvOS 27 checklist](../os27-intro/tvOS.md) for scoped video and managed-network changes. Its exact supported-device list is not verified here.
- Xcode 27 (`27A266a`) requires **Apple silicon and macOS Tahoe 26.6 or later**, not macOS 27. Preserve OS26 tests and apply the [submission checklist](../guides/app-store-readiness.md) separately.

## Getting Started

**New to tvOS development?**  
Check out the [tvOS Pathway](https://developer.apple.com/tvos/get-started/), a collection of resources to get started with Apple TV app development.

### Development Considerations

**Living Room Experience**  
Design for viewing from across a room. Apple's HIG describes distances often around 8 feet or more; use readable text, clear focus, and simplified navigation rather than a fixed physical layout.

**Focus and Selection**  
Understand tvOS's focus-based navigation system. Users navigate using directional buttons and select items with the touch surface or button press.

**Content First**  
Prioritize content discovery and consumption. Users come to Apple TV primarily for entertainment, so make content easily accessible and beautifully presented.

## Resources

### Development Tools
- [Xcode](https://developer.apple.com/xcode/) - Complete development environment with tvOS simulators
- [TestFlight](https://developer.apple.com/testflight/) - Beta testing platform for tvOS apps
- [App Store Connect](https://developer.apple.com/app-store-connect/) - App management and analytics

### Documentation
- [tvOS Release Notes](https://developer.apple.com/documentation/tvos-release-notes)
- [TVUIKit Documentation](https://developer.apple.com/documentation/tvuikit/)
- [Focus-based navigation](https://developer.apple.com/documentation/uikit/focus-based-navigation)
- [AVKit](https://developer.apple.com/documentation/avkit/)

### Related Platforms
Build apps that integrate seamlessly across all Apple platforms:
- [iOS](iOS.md) - Mobile companion experiences
- [iPadOS](iPadOS.md) - Enhanced tablet experiences
- [macOS](macOS.md) - Desktop and laptop applications
- [visionOS](visionOS.md) - Spatial computing experiences
- [watchOS](watchOS.md) - Wearable integration

## Support

### Meet with Apple
Sharpen your skills through in-person and online activities around the world. Connect with Apple engineers and designers to create compelling living room experiences.

### Apple Developer Program
Join the [Apple Developer Program](Program.md) for TestFlight, App Store distribution for Apple TV, and capabilities that require membership. Developer beta access is separate.

### Design Guidelines
- **Human Interface Guidelines**: Design principles specific to tvOS and living room experiences
- **Content Presentation**: Best practices for displaying media and information on television screens
- **Navigation Patterns**: Effective focus-based navigation and user interaction patterns

---

*Platform requirements and feature availability may vary. Some capabilities and services may not be available in all regions or all languages.*

## Sources

[Apple's tvOS overview](https://developer.apple.com/tvos/), [Designing for tvOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos), and [Liquid Glass adoption](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass) support the platform guidance. [Apple Developer releases](https://developer.apple.com/news/releases/), [tvOS 27 notes](https://developer.apple.com/documentation/tvos-release-notes/tvos-27-release-notes), and [Xcode 27 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes) support the status and migration guidance checked September 8, 2026. Earlier platform capabilities remain context, not universal hardware guarantees.
