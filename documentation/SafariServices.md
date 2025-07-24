# Safari Services

Enable web views and services in your app.

**Platforms:** iOS 7.0+ | iPadOS 7.0+ | Mac Catalyst 13.0+ | macOS 10.12+ | visionOS 1.0+

## Overview

Use the Safari Services framework to integrate Safari behaviors into your iOS or macOS app, or to extend the behavior of Safari.

You can:

- Provide a user interface that is almost identical to the user interface that the Safari app provides. Users can browse the web in this view and then return to your app's content. This view is more consistent with the Safari user interface than implementing your own custom browsing solution and can be done using fewer lines of code. (iOS)
- Add items to the user's Safari Reading List. (iOS)
- Convert your existing Chrome, Firefox, or Edge extensions into a Safari web extension, or create a new Safari web extension that can work in other browsers. (iOS and macOS)
- Determine from your app whether your content blocker extension is loaded, and if it is, tell it to refresh its contents. (iOS and macOS)
- Implement Safari app extensions. Determine from your app whether a Safari app extension is loaded. (macOS)
- Allow the user to share cookies and website data between an app and Safari for a single sign-on (SSO) experience with ASWebAuthenticationSession.

## Topics

### Safari web extensions
- **Safari web extensions** - Create web extensions that work in Safari and other browsers.

### Content blockers
- [Creating a content blocker](https://developer.apple.com/documentation/safariservices/creating_a_content_blocker) - Create a content blocker for Safari in Xcode.
- **SFContentBlockerManager** - A class that your app uses to interact with a content blocker extension.
- **SFContentBlockerState** - The state of a content blocker extension.

### Safari app extensions
- **Safari app extensions** - Learn how Safari app extensions extend the web-browsing experience in Safari by leveraging web technologies and native code.
- **SFSafariExtension** - A proxy for the Safari extension.
- **SFSafariApplication** - A proxy for the Safari app.
- **SFSafariWindow** - A proxy for a Safari window.
- **SFSafariPage** - A proxy for a Safari webpage.
- **SFSafariTab** - A proxy for a tab in a Safari window.

### Safari content in your app
- **SFSafariViewController** - An object that provides a visible standard interface for browsing the web.
- **CompletionHandler** - The completion handler for an authentication session when the user cancels or finishes the login.

### Importing data exported from Safari
- Transfer bookmarks, saved passwords, and other information between browsers.

### Associated domains
- [Supporting associated domains](https://developer.apple.com/documentation/safariservices/supporting_associated_domains) - Connect your app and a website to provide both a native app and a browser experience.
- **SFUniversalLink** - An object that provides browsers with the ability to discover associations between an app and a website.
- **Associated Domains Entitlement** - The associated domains for specific services, such as shared web credentials, universal links, and App Clips.

### Availability
- **SFSafariServicesAvailable** - Indicates whether a given version of Safari services is available.
- **SFSafariServicesVersion** - The version of Safari services.

### Safari Reading List
- **SSReadingList** - An object for adding items to a user's Safari Reading List.
- **SSReadingListErrorDomain** - The domain for Safari Reading List errors.
- **Code** - Messages that describe a Safari Reading List error.
- **SSReadingListError** - A Safari Reading List error.

### Home Screen bookmarks
- **SFAddToHomeScreenActivityItem** - A protocol that describes a bookmark someone can add to their Home Screen.

### Miscellaneous errors
- **SFError** - A content blocker or Safari app extension error.
- **Code** - Messages that describe a content blocker or Safari app extension error.
- **SFErrorDomain** - The domain for content blocker or Safari app extension errors.

### Deprecated
- **Deprecated symbols** - Review unsupported symbols and their replacements.

### Classes
- **SFSafariSettings** (Beta)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SafariServices)*