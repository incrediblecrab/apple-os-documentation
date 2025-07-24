# Declared Age Range

Create age-appropriate experiences in your app by asking people to share their age range.

**Platforms:** iOS 26.0+ (Beta) | iPadOS 26.0+ (Beta) | Mac Catalyst 26.0+ (Beta) | macOS 26.0+ (Beta)

## Overview

Use the Declared Age Range framework to request people to share their age range with your app. For children in a Family Sharing group, a Family Organizer can decide whether to always share a child's age information with your app, ask the child every time, or never share their age information. Along with an age range, the system returns an AgeRangeService.AgeRangeDeclaration for the age range a person provides.

## Topics

### Essentials
- **com.apple.developer.declared-age-range** - A Boolean value indicating whether your app may request a person's age range.

### Age Range Requests
- **AgeRangeService** - A request for the age range of a person logged onto iCloud on the device.
- **DeclaredAgeRangeAction** - Provides an action to request a person's declared age range.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/DeclaredAgeRange)*