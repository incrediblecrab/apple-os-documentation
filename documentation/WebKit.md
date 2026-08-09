# WebKit

Integrate web content seamlessly into your app, and customize content interactions to meet your app's needs.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 13.1+ | macOS 10.2+ | visionOS 1.0+

## Overview

Use the WebKit framework to integrate richly styled web content into your app's native content. WebKit offers a full browsing experience for your content, offering a platform-native view and supporting classes to:

- Display rich web content using HTML, CSS, and JavaScript
- Handle the incremental loading of page content
- Display multiple MIME types and compound frame elements
- Navigate between pages of content
- Manage a forward-back list of recently visited pages

For more information about WebKit, go to https://webkit.org.

> **iOS 27+, iPadOS 27+, macOS Golden Gate 27+:** Safari 27 adds automatic tab grouping by topic, extension generation from a natural-language description, and webpage change monitoring that alerts people to changes such as price drops or restocks. Verify API-level detail against the [Safari release notes](safari-release-notes.md) before depending on it.

## Topics

### WebKit APIs
- **WebKit for AppKit and UIKit** - Display web content in AppKit or UIKit apps, or apps built with Objective-C.
- **WebKit for SwiftUI** - Integrate web content into your SwiftUI apps with new standard views you connect to webpages.

### Safari Support
- [Optimizing Your Website for Safari](https://developer.apple.com/documentation/WebKit/optimizing_your_website_for_safari) - Improve your website by optimizing it for Safari.
- [Delivering Video Content for Safari](https://developer.apple.com/documentation/WebKit/delivering_video_content_for_safari) - Improve the performance and appearance of video in your website in Safari.
- [Promoting Apps with Smart App Banners](https://developer.apple.com/documentation/WebKit/promoting_apps_with_smart_app_banners) - Create a banner to promote your app on the App Store from a website.

### WebDriver
- **WebDriver** - Create automated tests of your web content using WebDriver commands.
- [macOS WebDriver Commands for Safari 11.1 and earlier](https://developer.apple.com/documentation/WebKit/macos_webdriver_commands_for_safari_11_1_and_earlier) - Test your web content using the WebDriver commands supported by Safari 11.1 and earlier.
- [macOS WebDriver Commands for Safari 12 and later](https://developer.apple.com/documentation/WebKit/macos_webdriver_commands_for_safari_12_and_later) - Test your web content using the WebDriver commands supported by Safari 12 and later.
- [About WebDriver for Safari](https://developer.apple.com/documentation/WebKit/about_webdriver_for_safari) - Enhance testing of your web content using Safari's enhancements to WebDriver.
- [Testing with WebDriver in Safari](https://developer.apple.com/documentation/WebKit/testing_with_webdriver_in_safari) - Enable WebDriver and run a test.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/WebKit)*
