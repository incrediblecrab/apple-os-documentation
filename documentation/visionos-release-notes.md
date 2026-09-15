# visionOS Release Notes

Learn about changes to the visionOS SDK.

## Overview

> **Checked September 8, 2026:** visionOS **26.6.1** (`23O780`, August 17) was the shipping 26-generation release. **Update September 14, 2026:** visionOS **27.0** (`24M362`) is shipping. [Release listings](https://developer.apple.com/news/releases/) establish neither a public-beta program nor a complete OS27 model list.

Use these notes for spatial and shared-framework SDK changes. See the [Apple Developer Program](../os27-intro/Program.md) for testing and distribution requirements.

### OS27 Migration Priorities

- UIKit-based apps built with the latest SDK must adopt [scenes](https://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle) or fail to launch on visionOS 27.
- Plan ODR/`NSBundleResourceRequest` migration to Background Assets, including localized packs and unavailable downloads.
- Review asynchronous SwiftUI document APIs and the nullable PhotoKit resource filename replacement.
- Re-test permission denial, tracking loss, immersion transitions, and remote disconnection. The earlier `RemoteImmersiveSpace` discovery failure is **resolved**, not a permanent Compositor Services restriction.
- For managed installations, audit [selected system-process TLS](https://support.apple.com/en-us/126655) and its documented exceptions.

Source: [visionOS 27 release notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-27-release-notes). See the [OS27 introduction](../os27-intro/visionOS.md) and retain the [OS26 context](../os26-intro/visionOS.md) for older targets.

[Xcode 27](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes) requires **Apple silicon and macOS Tahoe 26.6 or later**, not macOS 27. Its physical-Vision-Pro Device Hub video/input limitation is specific to that tool release, not an OS-wide app limitation.

### Bug Reporting

For issues not mentioned in release notes, file bugs through [Feedback Assistant](https://feedbackassistant.apple.com/), including OS/SDK builds, device model, and reproduction steps.

## Topics

### visionOS 27
- [visionOS 27 Release Notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-27-release-notes) - Shipping release dated September 14, 2026.

### visionOS 26
- [visionOS 26.6.1 security/release listing](https://support.apple.com/en-us/100100) - Shipping maintenance release, August 17, 2026.
- [visionOS 26.6 Release Notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-26_6-release-notes) - SDK notes for the 26.6 line.
- [visionOS 26.5 Release Notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-26_5-release-notes) - Earlier OS26 SDK changes and fixes.
- [visionOS 26.4 Release Notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-26_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [visionOS 26.3 Release Notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-26_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [visionOS 26.2 Release Notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-26_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [visionOS 26.1 Release Notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-26_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [visionOS 26 Release Notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-26-release-notes) - Update your apps to use new features, and test your apps against API changes.

### visionOS 2
- [visionOS 2.6 Release Notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-2_6-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [visionOS 2.5 Release Notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-2_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [visionOS 2.4 Release Notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-2_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [visionOS 2.3 Release Notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-2_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [visionOS 2.2 Release Notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-2_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [visionOS 2.1 Release Notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-2_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [visionOS 2 Release Notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-2-release-notes) - Update your apps to use new features, and test your apps against API changes.

### visionOS
- [visionOS 1.3 Release Notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-1_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [visionOS 1.2 Release Notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-1_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [visionOS 1.1 Release Notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-1_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [visionOS Release Notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-release-notes) - Update your apps to use new features, and test your apps against API changes.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/visionos-release-notes)*
