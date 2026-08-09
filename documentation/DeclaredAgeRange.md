# Declared Age Range

Create age-appropriate experiences in your app by asking people to share their age range.

**Platforms:** iOS 26.0+ | iPadOS 26.0+ | Mac Catalyst 26.0+ | macOS 26.0+ | visionOS 26.0+ | watchOS 26.0+

## Overview

Use the Declared Age Range framework to request people to share their age range with your app. For children in a Family Sharing group, a Family Organizer can decide whether to always share a child's age information with your app, ask the child every time, or never share their age information. Along with an age range, the system returns an AgeRangeService.AgeRangeDeclaration for the age range a person provides.

> **iOS 27+, iPadOS 27+, macOS Golden Gate 27+:** The 2026 App Store Review Guidelines tighten age handling. **1.2.1(a)** requires apps with user-generated content to provide a way to flag content exceeding the app's age rating plus an age restriction mechanism based on verified or declared age, and **4.7.5** extends the same requirement to HTML5/JavaScript mini apps and mini games. DeclaredAgeRange returns age **ranges** only and is parent-controlled for children in Family Sharing.

## Topics

### Essentials
- **com.apple.developer.declared-age-range** - A Boolean value indicating whether your app may request a person's age range.

### Age Range Requests
- **AgeRangeService** - A request for the age range of a person logged onto iCloud on the device.
- **DeclaredAgeRangeAction** - Provides an action to request a person's declared age range.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/DeclaredAgeRange)*
