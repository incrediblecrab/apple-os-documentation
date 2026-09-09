# WebKit

Integrate web content seamlessly into your app, and customize content interactions to meet your app's needs.

**Platforms:** iOS 8.0+ | iPadOS 8.0+ | Mac Catalyst 13.1+ | macOS 10.2+ (legacy framework), 10.10+ (`WKWebView`) | visionOS 1.0+

## Overview

WebKit hosts HTML, CSS, and JavaScript alongside native app content. Its views, configuration objects, and delegates support:

- Loading pages and their embedded resources
- Rendering supported web content and frames
- Deciding navigation policy and responding to page interactions
- Managing back/forward navigation

Your app supplies its browsing controls; an embedded web view is not Safari's full browser interface. The older `WKWebView` declarations establish the mobile baseline above, not the current framework catalog's iOS 16 aggregate. See [WebKit.org](https://webkit.org/) for engine and standards development.

## Safari 27 web-platform changes

The [WebKit announcement](https://webkit.org/blog/17967/news-from-wwdc26-webkit-in-safari-27-beta/) and [Safari 27 beta notes](https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes) describe developer-facing changes:

- **Customizable select:** `appearance: base-select`, `::picker(select)`, `::picker-icon`, `::checkmark`, and `<selectedcontent>` extend native form controls without replacing their semantics.
- **Scroll anchoring:** the browser adjusts scrolling when content changes above the viewport. `overflow-anchor: auto` is the default; opt out selectively with `none` where application-controlled scrolling requires it.
- **Anchor positioning:** transformed anchors are tracked, `position-anchor: normal` becomes the default, and `position-visibility` uses singular `anchor-valid`/`anchor-visible` names while retaining the older plural aliases.
- **JavaScript and Wasm:** module-loader fixes address top-level-await execution ordering; JavaScript Promise Integration (JSPI) lets Wasm suspend for asynchronous JavaScript work.
- **Accessibility and streams:** `ariaNotify()` enables announcements; readable-stream async iteration, `ReadableStream.from()`, and transferable streams expand streaming workflows.
- **Spatial web:** `<model>` expands to iOS/iPadOS/macOS. Immersive website environments and spatial/panorama image controls are specifically visionOS 27 features, not promises for every Safari host.

Safari 27 beta is also available on **macOS 26 and macOS Sequoia**, according to its release notes. A Safari version is not an OS version, and a browser's feature list does not establish availability of a native WebKit symbol on an older host. Use feature detection and test actual Safari, web-app, and embedded-view environments. See the [Safari 27 migration guide](../guides/safari27-migration.md).

## Native embedding APIs

[`WKWebView`](https://developer.apple.com/documentation/webkit/wkwebview) remains the UIKit/AppKit embedding API: **iOS/iPadOS 8, Mac Catalyst 13.1, macOS 10.10, and visionOS 1**. For SwiftUI, [`WebView`](https://developer.apple.com/documentation/webkit/webview-swift.struct) and [`WebPage`](https://developer.apple.com/documentation/webkit/webpage) are **WebKit** types available on iOS/iPadOS/Mac Catalyst/macOS/visionOS 26+, not new SwiftUI-framework types in 27. `WebPage` is observable and controls the content; `WebView` presents it.

The following verified additions require iOS/iPadOS/Mac Catalyst/macOS/visionOS **27+**:

| API | Integration consideration |
| --- | --- |
| [`WKJSHandle`](https://developer.apple.com/documentation/webkit/wkjshandle) | Retains a JavaScript object reference when handle creation is enabled for the content world/page. The referenced object stays alive while the native handle exists; release handles when finished. |
| [`WKDOMNodeSnapshot`](https://developer.apple.com/documentation/webkit/wkdomnodesnapshot) | An opaque DOM-node snapshot that can be passed to later JavaScript calls, including in another frame or after navigation. Unlike a handle, it does not keep the original live JavaScript object alive. |
| [`WKContentWorld.Configuration`](https://developer.apple.com/documentation/webkit/wkcontentworld/configuration) | Configures capabilities for application scripts in a content world. It does not change what ordinary webpage JavaScript can do. |
| [`WKWebpagePreferences.alternateRequest`](https://developer.apple.com/documentation/webkit/wkwebpagepreferences/alternaterequest) | An optional request used to change this navigation's **main resource** load, not a blanket rewrite of all subresource requests. This scope is documented in the [public header](https://github.com/WebKit/WebKit/blob/main/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.h). |
| [`WKNavigationAction.mainFrameNavigation`](https://developer.apple.com/documentation/webkit/wknavigationaction/mainframenavigation) | Associates the action with the enclosing main-frame navigation. It is `nil` for requests opening a new web view and for subframe loads. |
| [`WKFormInfo`](https://developer.apple.com/documentation/webkit/wkforminfo) | Describes an in-progress form submission. It is transient data, not a stable form identifier across callbacks. |

Choose the [`WKWebsiteDataStore`](https://developer.apple.com/documentation/webkit/wkwebsitedatastore) before creating the web view: the default persists data to disk; `nonPersistent()` keeps that store's data in memory. The store API starts at iOS/iPadOS 9 and macOS 10.11, with Mac Catalyst 13.1 and visionOS 1 support.

[`WKContentWorld`](https://developer.apple.com/documentation/webkit/wkcontentworld) separates JavaScript variables, **not the DOM**: DOM changes remain visible across worlds, and variables do not persist through navigation. It starts at iOS/iPadOS/Mac Catalyst 14, macOS 11, and visionOS 1; the configuration class above is newer. Validate messages crossing into native code. Use [SafariServices](SafariServices.md) for system browsing or Safari extensions rather than assuming a `WKWebView` gives access to Safari's browsing state.

For standards demonstrations, see [Web technology sessions at WWDC26](https://webkit.org/blog/17974/web-technology-sessions-at-wwdc26/). For debugging and release history, use [Safari developer tools](safari-developer-tools.md) and the [Safari release index](safari-release-notes.md).

## Topics

### WebKit APIs
- [WebKit for AppKit and UIKit](https://developer.apple.com/documentation/webkit/webkit-for-appkit-and-uikit) - Display web content in AppKit or UIKit apps, or apps built with Objective-C.
- [WebKit for SwiftUI](https://developer.apple.com/documentation/webkit/webkit-for-swiftui) - Integrate web content into SwiftUI apps.

### Safari Support
- [Optimizing Your Website for Safari](https://developer.apple.com/documentation/webkit/optimizing-your-website-for-safari) - Improve your website by optimizing it for Safari.
- [Delivering Video Content for Safari](https://developer.apple.com/documentation/webkit/delivering-video-content-for-safari) - Improve the performance and appearance of video in your website in Safari.
- [Promoting Apps with Smart App Banners](https://developer.apple.com/documentation/webkit/promoting-apps-with-smart-app-banners) - Create a banner to promote your app on the App Store from a website.

### WebDriver

Use the command set appropriate to the Safari version being tested:

- [macOS WebDriver Commands for Safari 11.1 and earlier](https://developer.apple.com/documentation/webkit/macos-webdriver-commands-for-safari-11-1-and-earlier) - The older Safari command reference.
- [macOS WebDriver Commands for Safari 12 and later](https://developer.apple.com/documentation/webkit/macos-webdriver-commands-for-safari-12-and-later) - The later command reference.
- [About WebDriver for Safari](https://developer.apple.com/documentation/webkit/about-webdriver-for-safari) - Safari's browser automation integration.
- [Testing with WebDriver in Safari](https://developer.apple.com/documentation/webkit/testing-with-webdriver-in-safari) - Enable WebDriver and run a test.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/WebKit)*
