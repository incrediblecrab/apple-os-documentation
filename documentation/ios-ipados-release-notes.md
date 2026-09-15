# iOS & iPadOS Release Notes

Learn about changes to the iOS & iPadOS SDK.

**Platforms:** iOS | iPadOS

## Overview

> **Checked September 8, 2026:** iOS **26.6.2** (`23G90`, September 8) and iPadOS **26.7** (`23H24`, September 9) are the last 26-generation releases; iOS/iPadOS **27.0** (`24A437`) shipped September 14.

Release notes provide details on API changes, known issues, fixes, workarounds, and deprecations for recent software releases.

### OS27 Migration Priorities

- Adopt the [UIKit scene-based life cycle](https://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle): apps built with the latest SDK fail to launch on iOS/iPadOS 27 without it. Multiple-window support is optional.
- The 27 SDK requires a launch-screen declaration. Review new external-display scene registration, presentation trait propagation, and menu behavior.
- Migrate ODR/`NSBundleResourceRequest` to Background Assets; test localized packs and unavailable/offline assets.
- Audit [stricter TLS for selected system processes](https://support.apple.com/en-us/126655), including management, enrollment, installation, and updates. This is not a universal change to every app socket.
- Re-test resolved issues in the 27.0 notes rather than documenting them as permanent restrictions. See the [iOS](../os27-intro/iOS.md) and [iPadOS](../os27-intro/iPadOS.md) introductions for selected API migrations and current known-issue scope.

The [iOS/iPadOS 27 notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes) are the feature source. [Xcode 27](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes) (`27A266a`, September 14) requires **Apple silicon and macOS Tahoe 26.6 or later**, not macOS 27. Keep host, linked SDK, deployment target, and [submission policy](../guides/app-store-readiness.md) separate.

### Bug Reporting

For issues not mentioned in release notes, send feedback through Feedback Assistant.

Include the OS version and build, for example **iOS 27.0 (`24A437`)**, as well as the Xcode/SDK build and reproduction steps. Find the device build under Settings > General > About and submit through [Feedback Assistant](https://feedbackassistant.apple.com/).

## Topics

### iOS & iPadOS 27
- [iOS & iPadOS 27 Release Notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes) - API changes, resolved/known issues, and migrations.

### iOS & iPadOS 26
- [iOS 26.6.2 and iPadOS 26.7 security/release listings](https://developer.apple.com/news/releases/) - Final 26-generation maintenance releases, September 8 and 9, 2026; not separate SDK feature pages.
- [iOS & iPadOS 26.6 Release Notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-26_6-release-notes) - SDK notes for the 26.6 line.
- [iOS & iPadOS 26.5 Release Notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-26_5-release-notes) - Earlier OS26 SDK changes and fixes.
- [iOS & iPadOS 26.4 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-26_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 26.3 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-26_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 26.2 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-26_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 26.1 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-26_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 26 Release Notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-26-release-notes) - Update your apps to use new features, and test your apps against API changes.

### iOS & iPadOS 18
- [iOS & iPadOS 18.6 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-18_6-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 18.5 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-18_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 18.4 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-18_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 18.3 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-18_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 18.2 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-18_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 18.1 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-18_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 18 Release Notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-18-release-notes) - Update your apps to use new features, and test your apps against API changes.

### iOS & iPadOS 17
- [iOS & iPadOS 17.6 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-17_6-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.5 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-17_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.4 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-17_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.3 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-17_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.2 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-17_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.1 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-17_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17 Release Notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-17-release-notes) - Update your apps to use new features, and test your apps against API changes.

### iOS & iPadOS 16
- [iOS & iPadOS 16.6 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-16_6-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 16.5 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-16_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 16.4 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-16_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 16.3 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-16_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 16.2 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-16_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS 16.1 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-16_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS 16 Release Notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-16-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iPadOS 16 Release Notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ipados-16-release-notes) - Update your apps to use new features, and test your apps against API changes.

### iOS & iPadOS 15
- [iOS & iPadOS 15.6 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-15_6-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 15.5 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-15_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 15.4 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-15_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 15.3 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-15_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 15.2 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-15_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 15.1 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-15_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 15 Release Notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-15-release-notes) - Update your apps to use new features, and test your apps against API changes.

### iOS & iPadOS 14
- [iOS & iPadOS 14.7 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-14_7-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14.6 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-14_6-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14.5.1 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-14_5_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14.5 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-14_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14.4 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-14_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14.3 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-14_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14.2 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-14_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 14 Release Notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-14-release-notes) - Update your apps to use new features, and test your apps against API changes.

### iOS & iPadOS 13
- [iOS & iPadOS 13.7 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-13_7-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 13.6 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-13_6-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 13.5 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-13_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 13.4 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-13_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 13.3.1 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-13_3_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 13.3 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-13_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 13.2 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-13_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 13.1 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-ipados-13_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS 13 Release Notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-13-release-notes) - Update your apps to use new features, and test your apps against API changes.

### iOS 12
- [iOS 12.4 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-12_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS 12.3 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-12_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS 12.2 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-12_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS 12.1.3 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-12_1_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS 12.1.1 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-12_1_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS 12.1 Release Notes](https://developer.apple.com/documentation/iOS-iPadOS-Release-Notes/ios-12_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [iOS 12 Release Notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-12-release-notes) - Update your apps to use new features, and test your apps against API changes.

### See Also
- [Apple Documentation Archive](https://developer.apple.com/library/archive/navigation/) - Browse archived developer material for earlier SDKs; the verified release-note entries above cover iOS 12 and later.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ios-ipados-release-notes)*
