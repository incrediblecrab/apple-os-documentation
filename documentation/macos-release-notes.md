# macOS Release Notes

Learn about changes to the macOS SDK.

## Overview

> **Checked September 8, 2026:** macOS Tahoe **26.6.2** (`25G83`, August 17) is shipping; macOS 27 **beta 8** (`26A5425a`) was released August 31. [Release listings](https://developer.apple.com/news/releases/) do not establish a general-availability date or a complete OS27 model list.

Release notes provide details on API changes, known issues, fixes, workarounds, and deprecations for recent software releases.

### OS27 Migration Priorities

- Test AppKit menu-image visibility, gestures, and document behavior with both a shipping binary and a 27-SDK rebuild.
- Audit Rosetta-dependent helpers and plug-ins. The notes describe native launch preference, Rosetta not being automatically restored after upgrade, and `arm64` defaults for installers without `hostArchitecture`.
- Mac Catalyst apps built with the latest SDK must adopt the [UIKit scene life cycle](https://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle). Re-test activation with no open windows.
- Audit [TLS for selected managed-system connections](https://support.apple.com/en-us/126655), not all app networking indiscriminately.
- Treat beta 8 fixes such as Accessory Access sandbox/VM support as resolved regression cases, not permanent limitations.

Source: [macOS 27 beta 8 notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes). See the [macOS 27 introduction](../os27-intro/macOS.md) for the selected changes and [Apple silicon](apple-silicon.md) for architecture planning.

**Xcode 27 beta 6 requires Apple silicon and macOS Tahoe 26.4 or later—not macOS 27.** Building universal apps or running Intel apps through Rosetta does not make Intel Macs eligible hosts. See [Xcode notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes).

### Bug Reporting

For issues not mentioned in release notes, send feedback through Feedback Assistant.

Include the version and build, for example **macOS 27 beta 8 (`26A5425a`)**, along with the Xcode/SDK build, architecture, and reproduction steps. Find the build in About This Mac and submit through [Feedback Assistant](https://feedbackassistant.apple.com/).

## Topics

### macOS 27
- [macOS 27 Golden Gate Beta 8 Release Notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes) - Pre-release API changes, known/resolved issues, and migrations; checked September 8, 2026.

### macOS 26
- [macOS Tahoe 26.6.2 security/release listing](https://support.apple.com/en-us/100100) - Shipping maintenance release, August 17, 2026.
- [macOS Tahoe 26.6.1 security/release listing](https://support.apple.com/en-us/100100) - Earlier maintenance release, August 6, 2026; superseded by 26.6.2.
- [macOS Tahoe 26.6 Release Notes](https://developer.apple.com/documentation/macos-release-notes/macos-26_6-release-notes) - SDK notes for the 26.6 line.
- [macOS Tahoe 26.5 Release Notes](https://developer.apple.com/documentation/macos-release-notes/macos-26_5-release-notes) - Earlier OS26 SDK changes and fixes.
- [macOS Tahoe 26.4 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-26_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Tahoe 26.3 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-26_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Tahoe 26.2 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-26_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Tahoe 26.1 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-26_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Tahoe 26 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-26-release-notes) - Update your apps to use new features, and test your apps against API changes.

### macOS 15
- [macOS Sequoia 15.6 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-15_6-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Sequoia 15.5 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-15_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Sequoia 15.4 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-15_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Sequoia 15.3 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-15_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Sequoia 15.2 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-15_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Sequoia 15.1 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-15_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Sequoia 15 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-15-release-notes) - Update your apps to use new features, and test your apps against API changes.

### macOS 14
- [macOS Sonoma 14.6 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-14_6-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14.5 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-14_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14.4 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-14_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14.3 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-14_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14.2 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-14_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14.1 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-14_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-14-release-notes) - Update your apps to use new features, and test your apps against API changes.

### macOS 13
- [macOS Ventura 13.5 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-13_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Ventura 13.4 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-13_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Ventura 13.3 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-13_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Ventura 13.2 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-13_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Ventura 13.1 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-13_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Ventura 13 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-13-release-notes) - Update your apps to use new features, and test your apps against API changes.

### macOS 12
- [macOS Monterey 12.5 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-12_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Monterey 12.4 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-12_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Monterey 12.3 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-12_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Monterey 12.2 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-12_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Monterey 12.1 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-12_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Monterey 12.0.1 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-12_0_1-release-notes) - Update your apps to use new features, and test your apps against API changes.

### macOS 11
- [macOS Big Sur 11.5 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-big-sur-11_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.4 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-big-sur-11_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.3 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-big-sur-11_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.2 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-big-sur-11_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.1 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-big-sur-11_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.0.1 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-big-sur-11_0_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.0.1 Universal Apps Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-big-sur-11_0_1-universal-apps-release-notes) - Update your apps to support Macs with Apple silicon.
- [macOS Big Sur 11.0.1 iOS & iPadOS Apps on Mac Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-big-sur-11_0_1-ios-ipados-apps-on-mac-release-notes) - Considerations for running iPhone and iPad apps on Macs with Apple silicon.

### macOS 10.15
- [macOS Catalina 10.15.6 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-catalina-10_15_6-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Catalina 10.15.5 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-catalina-10_15_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Catalina 10.15.4 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-catalina-10_15_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Catalina 10.15.3 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-catalina-10_15_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Catalina 10.15.2 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-catalina-10_15_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Catalina 10.15.1 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-catalina-10_15_1-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Catalina 10.15 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-catalina-10_15-release-notes) - Update your apps to use new features, and test your apps against API changes.

### macOS 10.14
- [macOS Mojave 10.14.6 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-mojave-10_14_6-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Mojave 10.14.5 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-mojave-10_14_5-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Mojave 10.14.4 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-mojave_10_14_4-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Mojave 10.14.3 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-mojave-10_14_3-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Mojave 10.14.2 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-mojave-10_14_2-release-notes) - Update your apps to use new features, and test your apps against API changes.
- [macOS Mojave 10.14 Release Notes](https://developer.apple.com/documentation/macOS-Release-Notes/macos-mojave-10_14-release-notes) - Update your apps to use new features, and test your apps against API changes.

### Articles
- [AppKit Release Notes for macOS 10.14](https://developer.apple.com/documentation/macos-release-notes/appkit-release-notes-for-macos-10_14) - Historical AppKit changes for macOS Mojave; this is not a macOS 14 article.
- [AppKit Release Notes for macOS Monterey 12](https://developer.apple.com/documentation/macOS-Release-Notes/appkit-release-notes-for-macos-12) - Update your apps to use new features, and test your apps against API changes.
- [AppKit Release Notes for macOS Ventura 13](https://developer.apple.com/documentation/macOS-Release-Notes/appkit-release-notes-for-macos-13) - Update your apps to use new features, and test your apps against API changes.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/macos-release-notes)*
