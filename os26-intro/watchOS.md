# watchOS 26.0 Developer Introduction

Maintain focused Apple Watch experiences using SwiftUI, HealthKit, notifications, and WidgetKit complications. Design for short interactions, intermittent connectivity, and limited background execution while adopting the OS26 appearance.

**Platform:** watchOS 26.0+

> **Status checked September 8, 2026:** the shipping release is **watchOS 26.6** (`23U67`), released July 27. watchOS 27 beta 8 was released August 31; see the [watchOS 27 introduction](../os27-intro/watchOS.md). Release listings do not establish a general-availability date or complete pairing requirements.

## Overview

Keep the most useful information available without a long interaction or a freshly connected phone. Health data requires authorization, and background updates have scheduling constraints. The capabilities below include earlier watchOS features as well as OS26 adoption work.

## Key Features

### New Design Language

**Say hello to Liquid Glass**  
Review system materials and custom controls under the OS26 appearance. Preserve contrast, readable text, and clear focus rather than adding translucent surfaces to every view.

**Refined Interface Elements**  
Use supported system controls and navigation, then test custom content under the current appearance and accessibility settings.

### Development Framework

**SwiftUI for watchOS**  
Build watch interfaces with SwiftUI's supported layouts, navigation, and controls. Check watchOS availability for individual view types rather than assuming every iPad-style container applies.

**Digital Crown Integration**  
Leverage the Digital Crown for precise input and navigation, providing users with tactile feedback and smooth scrolling experiences.

### Health and Fitness

**Advanced Health APIs**  
Use HealthKit for authorized workout, heart-rate, and route data, and Core Motion for supported motion-sensor data. Continuous measurements depend on the relevant session, permissions, hardware, and runtime conditions.

**Workout Integration**  
Use authorized workout sessions and supported measurements for your app's metrics or coaching features. Handle unavailable measurements without inventing health data.

**Health Data Sharing**  
Request HealthKit authorization for the data types your feature needs. Permission to read a health record is not, by itself, permission to share it outside the app.

### Smart Integration

**Widgets in the Smart Stack**  
Provide WidgetKit timelines and relevance information for the Smart Stack. The system controls placement and scheduling; relevance is not an unlimited background-execution grant.

**Enhanced Complications**  
Provide quick access to your watchOS app with sophisticated complications that display rich, contextual information on the watch face.

**Live Activities and the Smart Stack**

Consider how your iPhone Live Activity is presented on Apple Watch and customize supported WidgetKit presentations. Do not assume a standalone watch app gains unlimited background updates or a native copy of every ActivityKit API.

### Connectivity and Communication

**Device Connectivity**  
Use supported Bluetooth peripheral connections, checking availability and handling disconnections. Do not assume a peripheral or paired iPhone remains reachable.

**Interactive Notifications**  
Provide rich, actionable notifications that let users respond and interact without opening your app.

**Continuity Features**  
Choose supported continuity workflows for the task and device pair. Preserve useful watch behavior when the phone or network is unavailable.

## OS26 Adoption and Maintenance

Use these checks alongside the [watchOS 26 notes](https://developer.apple.com/documentation/watchos-release-notes/watchos-26-release-notes):

- Review system controls and custom workout views under the updated appearance.
- Test HealthKit authorization denial and unavailable measurements.
- Validate WidgetKit timelines, notifications, and Smart Stack content while disconnected from iPhone.
- Check dimmed/Always-On rendering only on hardware that supports it.
- Measure launch, refresh, and workout behavior rather than promising uniform performance gains.
- Test VoiceOver, text sizes, and Digital Crown interaction on supported watch sizes.
- Use [watchOS 26.6 notes](https://developer.apple.com/documentation/watchos-release-notes/watchos-26_6-release-notes) for the current maintenance line.

### Preparing an OS26 App for OS27

- The watchOS 27 notes deprecate `WKExtension` and `WKExtensionDelegate` for apps whose minimum deployment target is **watchOS 9.2 or later**. Review the SwiftUI app life cycle without discarding an older-target path prematurely.
- Check HealthKit zone support and Xcode 27's `@State` changes using the [watchOS 27 checklist](../os27-intro/watchOS.md). The exact OS27 Watch/iPhone pairing list is not verified here.
- Preserve SiriKit legacy behavior while using App Intents for modern integrations; see [Apple's SiriKit guidance](https://developer.apple.com/documentation/sirikit).
- Xcode 27 beta 6 requires **Apple silicon and macOS Tahoe 26.4 or later**, not macOS 27. Keep deployment targets separate from [submission SDK requirements](../guides/app-store-readiness.md).

## Getting Started

**New to watchOS development?**  
Get started with the [watchOS Pathway](https://developer.apple.com/watchos/get-started/) for Apple Watch development.

### Development Considerations

**Glanceable Interactions**  
Design for quick, focused interactions that deliver essential information in seconds. Users typically interact with Apple Watch for very brief periods.

**Digital Crown Navigation**  
Implement Digital Crown support for scrolling and selection to provide users with precise, tactile control over your interface.

**Always-On Display**  
Adapt to the Always On state's reduced update frequency and protect sensitive content. Test supported hardware and the person's settings; the display mode can be disabled.

## Developer Success Stories

### Air time
[Apple's Paku story](https://developer.apple.com/articles/paku/) describes Kyle Bashour's air-quality app and glanceable presentation of external sensor data.

### Anyone for tennis?
[Apple's SwingVision profile](https://developer.apple.com/news/?id=0pg4dthn) describes wrist-based scoring and tennis-performance information.

### Hitting the Slopes
[Apple's Slopes profile](https://developer.apple.com/news/?id=wq48r7mj) explains Curtis Herbert's ski-tracking app and starting recordings from iPhone or Apple Watch.

## Resources

### Development Tools
- [Xcode](https://developer.apple.com/xcode/) - Complete development environment with watchOS simulators
- [TestFlight](https://developer.apple.com/testflight/) - Beta testing platform for watchOS apps
- [App Store Connect](https://developer.apple.com/app-store-connect/) - App management and analytics

### Documentation
- [Developing watchOS Apps](https://developer.apple.com/documentation/watchos-apps)
- [HealthKit Documentation](https://developer.apple.com/documentation/healthkit/)
- [WatchKit Documentation](https://developer.apple.com/documentation/watchkit/)
- [WidgetKit for watchOS](https://developer.apple.com/documentation/widgetkit/)

### Related Platforms
Build apps that integrate seamlessly across all Apple platforms:
- [iOS](iOS.md) - Companion iPhone experiences
- [iPadOS](iPadOS.md) - Enhanced tablet experiences
- [macOS](macOS.md) - Desktop and laptop applications
- [tvOS](tvOS.md) - Living room entertainment
- [visionOS](visionOS.md) - Spatial computing experiences

## Support

### Meet with Apple
Sharpen your skills through in-person and online activities around the world. Connect with Apple engineers and designers to create compelling wrist experiences.

### Apple Developer Program
Join the [Apple Developer Program](Program.md) for TestFlight, App Store distribution for Apple Watch, and capabilities that require membership. Developer beta access is separate.

### Design Guidelines
- **Human Interface Guidelines**: Design principles specific to watchOS and wrist-worn devices
- **Health and Fitness**: Best practices for health-related apps and data presentation
- **Complications Design**: Effective strategies for watch face integration

---

*Platform requirements and feature availability may vary. Some health features may require specific Apple Watch models. Health data access requires user permission.*

## Sources

[Designing for watchOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos), [Always On behavior](https://developer.apple.com/documentation/watchos-apps/designing-your-app-for-the-always-on-state), and [Core Motion](https://developer.apple.com/documentation/coremotion) support the platform guidance. [Apple Developer releases](https://developer.apple.com/news/releases/), [watchOS 27 notes](https://developer.apple.com/documentation/watchos-release-notes/watchos-27-release-notes), and [Xcode 27 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes) support the status and migration guidance checked September 8, 2026. Inline story sources describe historical examples.
