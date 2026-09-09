# Safari app extensions

Learn how Safari app extensions extend the web-browsing experience in Safari by leveraging web technologies and native code.

## Overview

A Safari app extension combines native Swift or Objective-C code with injected JavaScript and CSS to work with authorized webpages in Safari. It can connect that content to a containing Mac app through shared resources and messages. Website access still depends on extension permissions and the person's choices.

> **Legacy migration:** The older Safari extension format is a separate model. See [Converting a legacy Safari extension to a Safari app extension](https://developer.apple.com/documentation/safariservices/converting-a-legacy-safari-extension-to-a-safari-app-extension).

Safari app extensions use the app-extension packaging model:

- Bundle the extension in a Mac or Mac Catalyst containing app; Apple documents App Store distribution for that bundle.
- Ship the app and extension together rather than requiring separate matching installations.
- Configure the shared resources and messages your app and extension need.

The core native handler/window/page/tab APIs require **macOS 10.12+**. `SFSafariExtension` itself starts at **10.14.4**. A Mac Catalyst containing app does not make this native extension model available in iOS.

## Choosing an extension model

This page describes the native Mac **app-extension** model. For shared Chrome/Firefox/Edge-style code, use [Safari web extensions](https://developer.apple.com/documentation/safariservices/safari-web-extensions), or follow [Converting a Safari app extension to a Safari web extension](https://developer.apple.com/documentation/safariservices/converting-a-safari-app-extension-to-a-safari-web-extension).

The WWDC26 [App Store Connect packager](https://developer.apple.com/documentation/safariservices/packaging-and-distributing-safari-web-extensions-with-app-store-connect) uploads a manifest and **web-extension resources** without a local Mac/Xcode installation. It does not replace native-code build requirements for a Safari app extension. Web extensions can also use [native messaging](https://developer.apple.com/documentation/safariservices/messaging-a-web-extension-s-native-app), so native communication alone does not determine the model. Keep the native app-extension model when its SafariServices APIs fit your architecture; it has not been removed by the new packaging workflow.

If converting, use the same developer account and the documented `SFSafariAppExtensionBundleIdentifiersToReplace` key. Safari replaces the listed old extensions when the new web extension installs. In **Safari 26.2+**, replacing exactly one app extension also migrates its Private Browsing setting and, if the new extension requests no additional website access, its website permissions. This conditional migration is not an automatic removal of all native extensions in Safari 27.

For Safari 27 `runtime.getDocumentId()`, user-activation propagation, feature detection, permissions, and host differences, see [SafariServices](SafariServices.md#browsing-embedding-and-safari-27-extensions) and the [migration guide](../guides/safari27-migration.md). Use [Safari developer tools](safari-developer-tools.md) for debugging.

## Topics

### Essentials
- [Building a Safari app extension](https://developer.apple.com/documentation/safariservices/building-a-safari-app-extension) - Add the Xcode target, build the containing app, and enable the extension in Safari.
- [Converting a legacy Safari extension to a Safari app extension](https://developer.apple.com/documentation/safariservices/converting-a-legacy-safari-extension-to-a-safari-app-extension) - Migrate the older extension format.
- [Troubleshooting your Safari app extension](https://developer.apple.com/documentation/safariservices/troubleshooting-your-safari-app-extension) - Check enablement, injection, and debugging.

### Injected style sheets and scripts

Injected scripts can run in subframes as well as the top-level page; do not assume one script instance per tab.

- [Using injected style sheets and scripts](https://developer.apple.com/documentation/safariservices/using-injected-style-sheets-and-scripts) - Apply styles and DOM behavior within permitted pages.
- [Injecting a script into a webpage](https://developer.apple.com/documentation/safariservices/injecting-a-script-into-a-webpage) - Configure script injection.
- [Injecting CSS style sheets into a webpage](https://developer.apple.com/documentation/safariservices/injecting-css-style-sheets-into-a-webpage) - Configure style injection.
- [Passing messages between Safari app extensions and injected scripts](https://developer.apple.com/documentation/safariservices/passing-messages-between-safari-app-extensions-and-injected-scripts) - Connect native extension handling and page scripts.
- [`SFSafariExtensionHandler`](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandler) - Subclass to handle native extension events.
- [`SFSafariExtensionManager`](https://developer.apple.com/documentation/safariservices/sfsafariextensionmanager) and [`SFSafariExtensionState`](https://developer.apple.com/documentation/safariservices/sfsafariextensionstate) - Query app or web extension state on macOS. Their iOS/iPadOS/visionOS 26.2 versions query web-extension state, not a new mobile native app-extension model; they also have Mac Catalyst 26.2 declarations.
- [`SFSafariPageProperties`](https://developer.apple.com/documentation/safariservices/sfsafaripageproperties) - Page URL, title, active state, and Private Browsing information.
- [`SFSafariExtensionHandling`](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling) - The event-handling protocol.
- [`SFExtensionProfileKey`](https://developer.apple.com/documentation/safariservices/sfextensionprofilekey) - A user-info key for a profile identifier. Its native Mac declaration starts at macOS 14, not 10.12; other declarations are iOS/iPadOS 17, Mac Catalyst 17.1, and visionOS 1.

### Information property list keys
- [Safari app extension information property list keys](https://developer.apple.com/documentation/safariservices/safari-app-extension-information-property-list-keys) - Configure capabilities, website access, scripts, styles, and interface items.

### Safari app extensions
- [`SFSafariExtension`](https://developer.apple.com/documentation/safariservices/sfsafariextension) - The extension proxy.
- [`SFSafariApplication`](https://developer.apple.com/documentation/safariservices/sfsafariapplication) - Class methods for Safari windows, toolbar updates, and containing-app messages; there is no object instance.
- [`SFSafariWindow`](https://developer.apple.com/documentation/safariservices/sfsafariwindow) - A window proxy.
- [`SFSafariPage`](https://developer.apple.com/documentation/safariservices/sfsafaripage) - A page proxy for script messaging, page properties, and reloads.
- [`SFSafariTab`](https://developer.apple.com/documentation/safariservices/sfsafaritab) - A tab proxy.

### See Also

#### Related Documentation
- [Safari web extensions](https://developer.apple.com/documentation/safariservices/safari-web-extensions) - The shared browser-extension model and its compatibility requirements.
- [WebKit](WebKit.md) - Native webpage embedding and browser web-platform updates, separate from the app-extension APIs above.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SafariServices/safari-app-extensions)*
