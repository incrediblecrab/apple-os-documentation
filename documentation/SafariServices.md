# Safari Services

Enable web views and services in your app.

**Platforms:** iOS 7.0+ | iPadOS 7.0+ | Mac Catalyst 13.1+ | macOS 10.12+ | visionOS 1.0+

## Overview

Use the Safari Services framework to integrate Safari behaviors into your iOS or macOS app, or to extend the behavior of Safari.

You can:

- Present a system browsing interface on iOS/iPadOS without implementing your own browser controls.
- Add items to Safari Reading List on the platforms supported by `SSReadingList`.
- Package shared browser-extension code as a Safari web extension, while checking manifest and API compatibility.
- Query whether a content blocker is enabled and request a rule reload; the app does not force-enable it.
- Implement native Safari app extensions on macOS, or query extension state using the platform-appropriate APIs.
- Use [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession) from [AuthenticationServices](AuthenticationServices.md) for browser-based sign-in. It is not a SafariServices type or permission to read Safari's arbitrary website data.

## Browsing, embedding, and Safari 27 extensions

[`SFSafariViewController`](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller) presents a system browsing interface without exposing browsing history, AutoFill, or website data to the containing app. Present it modally, not as a child view controller. Mac Catalyst and compatible iPhone/iPad apps running in visionOS open the default browser instead. Native visionOS supports context-menu link previews, but opening a preview's URL also redirects to the default browser. Use [WebKit](WebKit.md#native-embedding-apis) when you need a controlled embedded web view.

Safari **web extensions** use browser-extension manifests and JavaScript/HTML/CSS. Safari **app extensions** use a native Mac app-extension model; the two are not interchangeable.

- Safari 27 adds `runtime.getDocumentId()`, uncaught-exception/unhandled-rejection reporting, and user-activation propagation through `sendMessage()`, `connect()`, `postMessage()`, and `executeScript()`. Test permission prompts and gesture-dependent actions; a message does not grant new website permissions.
- The [Safari web extension packager in App Store Connect](https://developer.apple.com/documentation/safariservices/packaging-and-distributing-safari-web-extensions-with-app-store-connect) packages uploads from a browser on any host OS, without requiring a Mac or Xcode. Developer Program enrollment, an app record, required metadata, testing, and App Review still apply.
- Upload the manifest and all web-extension resources. The packager generates macOS and/or iOS apps; its iOS package is usable on iPadOS and visionOS as well. Packaging consumes Xcode Cloud compute time.
- Xcode packaging remains available for native containing-app integration. Web extensions can also use [native messaging](https://developer.apple.com/documentation/safariservices/messaging-a-web-extension-s-native-app); native communication is not exclusive to Safari app extensions. The web resource packager is not a general native-app build service.

See [Safari web extensions](https://developer.apple.com/documentation/safariservices/safari-web-extensions), [WWDC26 web sessions](https://webkit.org/blog/17974/web-technology-sessions-at-wwdc26/), and the [Safari 27 migration guide](../guides/safari27-migration.md). The browser release also runs on supported older macOS hosts; check extension APIs and host capabilities independently.

## Selected native API availability

The framework baseline does not apply to every type:

| API | Declaration minima |
| --- | --- |
| `SSReadingList` and its error domain/code | iOS/iPadOS 7; Mac Catalyst 14; visionOS 1; no native macOS declaration |
| `SFSafariViewController` | iOS/iPadOS 9; Mac Catalyst 13.1; visionOS 1, subject to the presentation differences above |
| `SFContentBlockerManager` / `SFContentBlockerState` | iOS/iPadOS 9 / 10; both Mac Catalyst 13.4, macOS 10.12, visionOS 1 |
| Native Safari window/page/tab proxies | macOS 10.12; `SFSafariExtension` itself starts at 10.14.4 |
| `SFUniversalLink` | macOS 10.15 |
| `SFAddToHomeScreenActivityItem` | iOS/iPadOS/Mac Catalyst 17.4; visionOS 1.1 |
| `SFSafariExtensionManager` / `SFSafariExtensionState` | macOS 10.12; iOS/iPadOS/Mac Catalyst/visionOS 26.2 |
| `SFSafariSettings` | iOS/iPadOS/visionOS 26; macOS/Mac Catalyst 27 |

The extension-state APIs cover app **or** web extensions on macOS, but web extensions on iOS and visionOS. Their newer mobile declarations do not make native Safari app extensions available there.

## Topics

### Safari web extensions
- [Safari web extensions](https://developer.apple.com/documentation/safariservices/safari-web-extensions) - Share extension code across browsers. [Assess compatibility](https://developer.apple.com/documentation/safariservices/assessing-your-safari-web-extension-s-browser-compatibility); conversion does not implement unsupported APIs.
- [Packaging and distributing with App Store Connect](https://developer.apple.com/documentation/safariservices/packaging-and-distributing-safari-web-extensions-with-app-store-connect) - Package extension resources in the browser.

### Content blockers
- [Creating a content blocker](https://developer.apple.com/documentation/safariservices/creating-a-content-blocker) - Supply declarative blocking rules; the extension does not inspect the user's browsing history.
- [`SFContentBlockerManager`](https://developer.apple.com/documentation/safariservices/sfcontentblockermanager) - Queries state and requests a rules reload.
- [`SFContentBlockerState`](https://developer.apple.com/documentation/safariservices/sfcontentblockerstate) - Reports whether the blocker is enabled.

### Safari app extensions
- [Safari app extensions](safari-app-extensions.md) - The native Mac extension model.
- [`SFSafariExtension`](https://developer.apple.com/documentation/safariservices/sfsafariextension) - A proxy for an extension.
- [`SFSafariApplication`](https://developer.apple.com/documentation/safariservices/sfsafariapplication) - Class-level access to Safari windows, toolbar updates, and containing-app messages; do not construct an instance.
- [`SFSafariWindow`](https://developer.apple.com/documentation/safariservices/sfsafariwindow), [`SFSafariPage`](https://developer.apple.com/documentation/safariservices/sfsafaripage), and [`SFSafariTab`](https://developer.apple.com/documentation/safariservices/sfsafaritab) - Proxies for Safari's window, page, and tab objects.
- [`SFSafariExtensionManager`](https://developer.apple.com/documentation/safariservices/sfsafariextensionmanager) and [`SFSafariExtensionState`](https://developer.apple.com/documentation/safariservices/sfsafariextensionstate) - Query extension enablement with the platform distinctions above.

### Safari content in your app
- [`SFSafariViewController`](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller) - System browsing presentation, rather than a customizable DOM container.

### Importing data exported from Safari
- [Importing data exported from Safari](https://developer.apple.com/documentation/safariservices/importing-data-exported-from-safari) - Read an archive the person chooses to share with your browser. Safari's export can include passwords and payment cards; it is not the same data model as [BrowserKit](BrowserKit.md)'s browser-to-browser transfer. File names are localized and history/extension files can be profile-specific, so do not hard-code only the English examples.

### Associated domains
- [Supporting associated domains](https://developer.apple.com/documentation/xcode/supporting-associated-domains) - Configure app/website associations.
- [`SFUniversalLink`](https://developer.apple.com/documentation/safariservices/sfuniversallink) - Browser-side discovery on macOS. This API requires the separately approved `com.apple.developer.associated-domains.applinks.read-write` entitlement.
- [Associated Domains Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.associated-domains) - Declare services such as universal links, shared web credentials, and App Clips; this is distinct from the browser discovery entitlement.

### Availability
- [`SFSafariServicesAvailable(_:)`](https://developer.apple.com/documentation/safariservices/sfsafariservicesavailable(_:)) - Legacy macOS compatibility query; the function declares macOS 10.11 availability.
- [`SFSafariServicesVersion`](https://developer.apple.com/documentation/safariservices/sfsafariservicesversion) - Safari Services version constants, not OS version numbers. The enum's reference declares macOS 10.12, unlike the query function.

### Safari Reading List
- [`SSReadingList`](https://developer.apple.com/documentation/safariservices/ssreadinglist) - Adds items to Reading List; not an API to enumerate Safari history.
- [`SSReadingListErrorDomain`](https://developer.apple.com/documentation/safariservices/ssreadinglisterrordomain), [`SSReadingListError.Code`](https://developer.apple.com/documentation/safariservices/ssreadinglisterror/code), and [`SSReadingListError`](https://developer.apple.com/documentation/safariservices/ssreadinglisterror) - The domain, codes, and Swift error wrapper.

### Home Screen bookmarks
- [`SFAddToHomeScreenActivityItem`](https://developer.apple.com/documentation/safariservices/sfaddtohomescreenactivityitem) - A browser-only activity-item protocol. In a WebKit browser it represents a bookmark; to offer a web app, supply the `WKWebView` itself to the activity controller. Alternative engines provide web-app information and a manifest through the protocol's callbacks.

### Miscellaneous errors
- [`SFError`](https://developer.apple.com/documentation/safariservices/sferror), [`SFError.Code`](https://developer.apple.com/documentation/safariservices/sferror/code), and [`SFErrorDomain`](https://developer.apple.com/documentation/safariservices/sferrordomain) - Content-blocker and extension errors.
- [`SFSafariSettingsError`](https://developer.apple.com/documentation/safariservices/sfsafarisettingserror) and [`SFSafariSettingsErrorDomain`](https://developer.apple.com/documentation/safariservices/sfsafarisettingserrordomain) - Settings errors with macOS/Mac Catalyst 27 declarations.

### Deprecated
- [Deprecated symbols](https://developer.apple.com/documentation/safariservices/deprecated-symbols) - Legacy APIs and replacements; deprecation is not removal.
- [`SFAuthenticationSession`](https://developer.apple.com/documentation/safariservices/sfauthenticationsession) and its [`CompletionHandler`](https://developer.apple.com/documentation/safariservices/sfauthenticationsession/completionhandler) belong to the older authentication flow, not `SFSafariViewController`. The session was introduced in iOS 11 and deprecated in 12; use `ASWebAuthenticationSession` for new work. The callback type's older catalog labels do not establish an earlier session introduction.

### Classes
- [`SFSafariSettings`](https://developer.apple.com/documentation/safariservices/sfsafarisettings) - Presents Safari's extension settings or Export Browsing Data sheet. It does not grant unrestricted access to Safari settings or data.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SafariServices)*
