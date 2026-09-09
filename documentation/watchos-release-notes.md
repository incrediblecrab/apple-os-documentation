# watchOS Release Notes

Learn about changes to the watchOS SDK and new features for Apple Watch app development.

## Overview

> **Checked September 8, 2026:** watchOS **26.6** (`23U67`, July 27) is shipping; watchOS 27 **beta 8** (`24R5360a`) was released August 31. [Release listings](https://developer.apple.com/news/releases/) do not establish a general-availability date or complete Watch/iPhone pairing requirements.

Use these notes for watch-specific SDK changes, deprecations, and beta fixes. See the [Apple Developer Program](../os27-intro/Program.md) for testing and distribution requirements.

For issues not mentioned in release notes, file bugs through [Feedback Assistant](https://feedbackassistant.apple.com/).

### OS27 Migration Priorities

- HealthKit adds heart-rate and cycling-power zones. Check authorization and unavailable data rather than assuming every device produces every measurement.
- `WKExtension` and `WKExtensionDelegate` are deprecated for apps whose **minimum deployment target is watchOS 9.2 or later**. Review the SwiftUI app life cycle; the UIKit scene requirement on other platforms does not apply here.
- Re-test SwiftUI `@State` initialization and `AsyncImage` caching with Xcode 27, including on older supported targets.
- Audit the relevant [system-process TLS](https://support.apple.com/en-us/126655) flows using Apple's watch-specific guidance. Complication, connectivity, and workout fixes listed as resolved in beta 8 are not enduring limitations.

Source: [watchOS 27 beta 8 notes](https://developer.apple.com/documentation/watchos-release-notes/watchos-27-release-notes). See [watchOS apps](watchOS-Apps.md) and the [OS27 introduction](../os27-intro/watchOS.md).

[Xcode 27 beta 6](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes) requires **Apple silicon and macOS Tahoe 26.4 or later**, not macOS 27. Hardware support, companion-device requirements, SDK availability, and submission policy are separate checks.

## Topics

### watchOS 27
- [watchOS 27 Beta 8 Release Notes](https://developer.apple.com/documentation/watchos-release-notes/watchos-27-release-notes) - Pre-release changes and known/resolved issues; checked September 8, 2026.

### watchOS 26
- [watchOS 26.6 Release Notes](https://developer.apple.com/documentation/watchos-release-notes/watchos-26_6-release-notes) - Shipping release dated July 27, 2026.
- [watchOS 26.5 Release Notes](https://developer.apple.com/documentation/watchos-release-notes/watchos-26_5-release-notes) - Earlier OS26 SDK changes and fixes.
- [watchOS 26.4 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-26_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 26.3 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-26_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 26.2 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-26_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 26.1 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-26_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 26 Release Notes](https://developer.apple.com/documentation/watchos-release-notes/watchos-26-release-notes) - Update your apps to use new features, and test your apps against API changes.

### watchOS 11
- [watchOS 11.6 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-11_6-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 11.5 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-11_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 11.4 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-11_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 11.3 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-11_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 11.2 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-11_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 11.1 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-11_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 11 Release Notes](https://developer.apple.com/documentation/watchos-release-notes/watchos-11-release-notes) - Update your apps to use new features, and test your apps against API changes.

### watchOS 10
- [watchOS 10.6 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-10_6-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 10.5 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-10_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 10.4 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-10_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 10.3 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-10_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 10.2 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-10_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 10.1 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-10_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 10 Release Notes](https://developer.apple.com/documentation/watchos-release-notes/watchos-10-release-notes) - Update your apps to use new features, and test your apps against API changes.

### watchOS 9
- [watchOS 9.6 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-9_6-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 9.5 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-9_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 9.4 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-9_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 9.3 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-9_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 9.2 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-9_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 9.1 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-9_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 9 Release Notes](https://developer.apple.com/documentation/watchos-release-notes/watchos-9-release-notes) - Update your apps to use new features, and test your apps against API changes.

### watchOS 8
- [watchOS 8.7 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-8_7-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 8.6 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-8_6-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 8.5 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-8_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 8.4 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-8_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 8.3 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-8_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 8.1 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-8_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 8 Release Notes](https://developer.apple.com/documentation/watchos-release-notes/watchos-8-release-notes) - Update your apps to use new features, and test your apps against API changes.

### watchOS 7
- [watchOS 7.6 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-7_6-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 7.5 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-7_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 7.4 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-7_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 7.3 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-7_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 7.2 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-7_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 7.1 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-7_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 7 Release Notes](https://developer.apple.com/documentation/watchos-release-notes/watchos-7-release-notes) - Update your apps to use new features, and test your apps against API changes.

### watchOS 6
- [watchOS 6.2.8 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-6_2_8-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 6.2.5 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-6_2_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 6.2 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-6_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 6.1.2 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-6_1_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 6.1.1 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-6_1_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 6.1 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-6_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 6 Release Notes](https://developer.apple.com/documentation/watchos-release-notes/watchos-6-release-notes) - Update your apps to use new features, and test your apps against API changes.

### watchOS 5
- [watchOS 5.3 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-5_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 5.1.3 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-5_1_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 5.1 Release Notes](https://developer.apple.com/documentation/watchOS-Release-Notes/watchos-5_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [watchOS 5 Release Notes](https://developer.apple.com/documentation/watchos-release-notes/watchos-5-release-notes) - Update your apps to use new features, and test your apps against API changes.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/watchos-release-notes)*
