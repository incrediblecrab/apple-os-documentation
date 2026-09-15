# tvOS Release Notes

Learn about changes to the tvOS SDK.

**Platform:** tvOS; the historical index below includes tvOS 12 and later.

## Overview

> **Checked September 8, 2026:** tvOS **26.6** (`23L773`, July 27) was the shipping 26-generation release. **Update September 14, 2026:** tvOS **27.0** (`24J361`) is shipping. [Release listings](https://developer.apple.com/news/releases/) do not establish an OS27 device list.

Use these notes for SDK changes, deprecations, and known/resolved issues. For distribution and testing membership, see the [Apple Developer Program](../os27-intro/Program.md).

### OS27 Migration Priorities

- UIKit apps built with the latest SDK must adopt [scenes](https://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle) or fail to launch on tvOS 27.
- Migrate ODR/`NSBundleResourceRequest` to Background Assets; localized packs add language-aware delivery. Test missing assets and interrupted downloads.
- Query VideoToolbox support before offering the new low-latency scaling/interpolation configurations.
- Review custom focus/navigation surfaces and [system-process TLS requirements](https://support.apple.com/en-us/126655) for managed deployments.

Source: [tvOS 27 release notes](https://developer.apple.com/documentation/tvos-release-notes/tvos-27-release-notes). Resolved earlier-beta issues should become regression tests, not lasting limitations. See the [tvOS 27 introduction](../os27-intro/tvOS.md).

[Xcode 27](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes) requires **Apple silicon and macOS Tahoe 26.6 or later**, not macOS 27. Keep its host requirements separate from Apple TV hardware eligibility and your app's deployment target.

### Bug Reporting

For issues not mentioned in release notes, file bugs through [Feedback Assistant](https://feedbackassistant.apple.com/), including OS/SDK builds, Apple TV model, and reproduction steps.

## Topics

### tvOS 27
- [tvOS 27 Release Notes](https://developer.apple.com/documentation/tvos-release-notes/tvos-27-release-notes) - Shipping release dated September 14, 2026.

### tvOS 26
- [tvOS 26.6 Release Notes](https://developer.apple.com/documentation/tvos-release-notes/tvos-26_6-release-notes) - Shipping release dated July 27, 2026.
- [tvOS 26.5 Release Notes](https://developer.apple.com/documentation/tvos-release-notes/tvos-26_5-release-notes) - Earlier OS26 SDK changes and fixes.
- [tvOS 26.4 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-26_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 26.3 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-26_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 26.2 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-26_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 26.1 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-26_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 26 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-26-release-notes) - Update your apps to use new features, and test your apps against API changes.

### tvOS 18
- [tvOS 18.6 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-18_6-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 18.5 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-18_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 18.4 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-18_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 18.3 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-18_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 18.2 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-18_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 18.1 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-18_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 18 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-18-release-notes) - Update your apps to use new features, and test your apps against API changes.

### tvOS 17
- [tvOS 17.6 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-17_6-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 17.5 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-17_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 17.4 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-17_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 17.3 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-17_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 17.2 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-17_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 17.1 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-17_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 17 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-17-release-notes) - Update your apps to use new features, and test your apps against API changes.

### tvOS 16
- [tvOS 16.6 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-16_6-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 16.5 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-16_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 16.4 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-16_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 16.3 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-16_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 16.2 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-16_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 16.1 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-16_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 16 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-16-release-notes) - Update your apps to use new features, and test your apps against API changes.

### tvOS 15
- [tvOS 15.6 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-15_6-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 15.5 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-15_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 15.4 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-15_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 15.3 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-15_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 15.2 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-15_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 15.1 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-15_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 15 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-15-release-notes) - Update your apps to use new features, and test your apps against API changes.

### tvOS 14
- [tvOS 14.7 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-14_7-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 14.6 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-14_6-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 14.5 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-14_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 14.4 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-14_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 14.3 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-14_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 14.2 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-14_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 14 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-14-release-notes) - Update your apps to use new features, and test your apps against API changes.

### tvOS 13
- [tvOS 13.4.8 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-13_4_8-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 13.4.5 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-13_4_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 13.4 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-13_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 13.3.1 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-13_3_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 13.3 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-13_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 13.2 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-13_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 13 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-13-release-notes) - Update your apps to use new features, and test your apps against API changes.

### tvOS 12
- [tvOS 12.4 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-12_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 12.2 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-12_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 12.1.2 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-12_1_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 12.1.1 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-12_1_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [tvOS 12 Release Notes](https://developer.apple.com/documentation/tvOS-Release-Notes/tvos-12-release-notes) - Update your apps to use new features, and test your apps against API changes.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/tvos-release-notes)*
