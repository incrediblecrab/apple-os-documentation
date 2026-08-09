# iOS 27.0 Developer Introduction

Build the next generation of iPhone apps with a rebuilt Siri, a refined Liquid Glass design, and a systemwide intelligence layer your app can plug directly into. iOS 27 makes app content understandable and actionable by the system through App Intents, opens the on-device foundation model to any model provider, and delivers substantial performance gains across every supported iPhone.

**Platform:** iOS 27.0+

> **Status:** iOS 27 is in developer and public beta as of August 2026 (developer beta 1 on June 8, 2026; public beta 1 on July 13, 2026). A public release is expected in September 2026. Apple has not announced a release date. The current shipping line is iOS 26.6, released July 27, 2026.

## Overview

iOS 27 is the second release in Apple's unified "26/27" versioning generation. Where iOS 26 introduced Liquid Glass, iOS 27 refines it and pairs it with a completely rebuilt Siri. For developers, the headline story is that the system now understands your app's content: App Intents entity schemas contribute to Spotlight's semantic index, and intent schemas let people act on that content in natural language without you shipping fixed phrases.

## Key Features

### Siri AI

**A rebuilt, conversational assistant**
Siri has been rebuilt on Apple Foundation Models. It holds extended natural conversations, understands context across apps, performs multi-step in-app actions, and answers with awareness of personal on-device data. A standalone Siri app lets people review and continue conversations, syncing across iPhone, iPad, Mac, Apple Watch, and Apple Vision Pro.

**Bring your own model**
The Foundation Models framework now exposes a generalized `LanguageModel` protocol. Apps can target Apple's on-device model or any conformant provider — including cloud models such as Claude and Google Gemini, which is available as an optional cloud model for certain Siri features.

**Write with Siri**
Systemwide writing assistance composes, proofreads, and gives feedback while matching the person's writing style. In Messages it appears as a dedicated button above the keyboard.

### New Design

**Liquid Glass, refined**
Liquid Glass now diffuses busy background content more aggressively, adds a subtle darkened edge ring for separation, and renders brighter, more defined specular highlights. Toolbars automatically become uniform and less translucent while content scrolls beneath them.

**People control the glass**
A transparency slider in Settings > Appearance replaces the binary Clear/Tinted toggle from iOS 26, letting people place translucency anywhere on a continuous spectrum. The material additionally responds to Reduce Transparency and Increase Contrast.

**Sharper app icons**
App icons gain sharper separation between layers, addressing feedback that iOS 26 icons looked soft at small sizes. Per-layer refraction effects are authored in Icon Composer 2.

### Enhanced App Capabilities

**App Intents**
Entity schemas contribute your app's content to Spotlight's semantic index so the system can reason about it. Intent schemas let people take action through natural language — with no specific phrases to memorize and no code changes as Siri's language model evolves. A new View Annotations API maps SwiftUI views to entities so people can reference and act on what's on screen conversationally.

**App Intents Testing**
A new testing framework validates your Siri, Shortcuts, and Spotlight integration through real system pathways rather than UI automation, surfacing problems far earlier.

**Shortcuts**
People can create a shortcut by describing the workflow in plain language. New Reminders actions include Create Group, Create List, Create Section, Delete Groups, Delete Lists, Delete Sections, and Get What's On Screen.

**Wallet**
Create a Pass lets people digitize tickets, memberships, gift cards, and loyalty cards using the camera or manual entry, with Standard, Membership, and Event templates, 12 background colors plus 7 themed backgrounds, up to two action buttons per pass, and a bold "Poster Generic" card style. Wallet Insights surfaces spending patterns, recurring transactions, and balances from connected accounts.

### Media and Photos

**AI photo editing**
Spatial Reframing changes a photo's apparent camera angle after capture using Portrait mode depth data. The Extend tool expands an image beyond its original borders, capped at 25% per side and allowed once per image. Clean Up gains substantially better background reconstruction. All AI-edited photos carry a SynthID watermark.

**Organization and sharing**
Photos adds keywords and star ratings. Shared Albums now work with Android and Windows users for the first time, alongside emoji reactions, expiring albums, and finer permissions. Image Playground becomes a standalone app with daily usage caps and additional usage through iCloud+.

### Safari and Passwords

Safari automatically groups open tabs by topic, can generate extensions from a natural-language description, and monitors webpages to alert people to changes such as price drops or restocks. Apple Intelligence can navigate to eligible sites, sign in, and update weak or compromised passwords automatically.

### Health and Fitness

Cycle Tracking notifies people when logged patterns suggest perimenopause and supports logging associated symptoms. Fitness+ adds perimenopause and menopause workout categories. The Health app's Browse tab is redesigned around colorful cards. GymKit now pairs with gym equipment directly from iPhone, without requiring Apple Watch.

### Family and Safety

Ask to Browse requires children to request approval before reaching certain websites. Setup Assistant lets parents choose which system apps a child can use — a few essentials, a recommended set, or a custom selection — and add more later through Ask to Buy. Parents can set per-app and per-category time allowances and schedules. Communication Safety now blurs gore and violence in Messages and FaceTime, not just nudity.

### CarPlay

CarPlay gains native video app support, with playback restricted to when the vehicle is parked, and brings the new Siri AI into the car.

## What's New in iOS 27

- **Siri AI**: rebuilt on Apple Foundation Models, with a standalone Siri app
- **Foundation Models**: generalized `LanguageModel` protocol, multimodal prompts, Dynamic Profiles
- **App Intents**: entity and intent schemas, View Annotations API, App Intents Testing
- **Evaluations framework**: validate AI feature behavior beyond unit tests
- **Liquid Glass refinements**: content diffusion, darkened edges, brighter speculars, transparency slider
- **Photos AI editing**: Spatial Reframing, Extend, improved Clean Up
- **Wallet**: Create a Pass, Wallet Insights
- **Performance**: Apple reports app launches up to 30% faster, photo loading up to 70% faster, and AirDrop transfers up to 80% faster, on a rebuilt CPU scheduler that benefits older devices including iPhone 11

> **Note:** The performance percentages above were reported from the WWDC 2026 keynote and are widely cited, but could not be verified against a published page on apple.com. Treat them as marketing claims rather than measured guarantees.

## Device Support

iOS 27 drops no iPhones — every device that ran iOS 26 is supported:

- iPhone 17, iPhone 17 Pro, iPhone 17 Pro Max, iPhone 17e, iPhone Air
- iPhone 16, iPhone 16 Plus, iPhone 16 Pro, iPhone 16 Pro Max, iPhone 16e
- iPhone 15, iPhone 15 Plus, iPhone 15 Pro, iPhone 15 Pro Max
- iPhone 14, iPhone 14 Plus, iPhone 14 Pro, iPhone 14 Pro Max
- iPhone 13, iPhone 13 mini, iPhone 13 Pro, iPhone 13 Pro Max
- iPhone 12, iPhone 12 mini, iPhone 12 Pro, iPhone 12 Pro Max
- iPhone 11, iPhone 11 Pro, iPhone 11 Pro Max
- iPhone SE (2nd generation) and later

iPhone XS, XS Max, XR, and older were already dropped before iOS 26.

### Apple Intelligence availability

| Tier | Devices |
|------|---------|
| Advanced on-device features | iPhone 17 Pro, iPhone 17 Pro Max, iPhone Air, and newer |
| Core Apple Intelligence | iPhone 15 Pro, iPhone 15 Pro Max, iPhone 16 line, iPhone 17 |
| iOS 27 without Apple Intelligence | iPhone 11 through iPhone 14, iPhone SE |

## Migrating to iOS 27

**Liquid Glass is no longer optional.** The `UIDesignRequiresCompatibility` Info.plist key is ignored by the iOS 27 SDK. Rebuilding with Xcode 27 opts your app fully into Liquid Glass with no supported override. The appearance is gated on the **linked SDK**, not the running OS — an app still built against the iOS 26 SDK keeps the legacy appearance on iOS 27 until you recompile.

**SiriKit is deprecated.** Migrate to App Intents. SiriKit-based intents are not recognized by the new Siri AI. Apple has not published a full deactivation timeline.

**Standard controls migrate for free; custom chrome does not.** Tab bars, navigation bars, sheets, alerts, and toolbars adopt Liquid Glass automatically on recompile. Custom blur views and bespoke navigation chrome must be migrated by hand using `glassEffect(_:in:)` and `GlassEffectContainer` in SwiftUI, or `UIGlassEffect` and `UIGlassContainerEffect` in UIKit.

**Submission requirements.** Uploads to App Store Connect have required the iOS 26 SDK or later since April 28, 2026. Apple has **not** announced the date by which submissions must use the Xcode 27 / iOS 27 SDK — watch [Upcoming Requirements](https://developer.apple.com/news/upcoming-requirements/).

## Getting Started

**New to iOS development?**
Check out the [iOS Pathway](https://developer.apple.com/ios/), an easy-to-navigate collection of resources to get started with iOS app development.

## Resources

### Development Tools
- [Xcode](https://developer.apple.com/xcode/) - Xcode 27 requires macOS 27 Golden Gate on Apple silicon
- [TestFlight](https://developer.apple.com/testflight/) - Beta testing platform
- [App Store Connect](https://developer.apple.com/app-store-connect/) - App management and analytics

### Documentation
- [iOS Developer Documentation](https://developer.apple.com/documentation/ios/)
- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)

### Related Platforms
- [iPadOS](iPadOS.md) - Enhanced iPad experiences
- [macOS](macOS.md) - macOS Golden Gate 27
- [tvOS](tvOS.md) - Living room entertainment
- [visionOS](visionOS.md) - Spatial computing
- [watchOS](watchOS.md) - Wearable experiences
- [Apple Developer Program](Program.md) - Membership, distribution, and policy

### Previous Generation
- [iOS 26 Developer Introduction](../os26-intro/iOS.md)

---

*Reviewed 2026-08-09. iOS 27 is pre-release software; features and availability may change before general release. Platform requirements and feature availability may vary, and some capabilities may not be available in all regions or languages.*
