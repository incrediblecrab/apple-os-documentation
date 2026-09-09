# BrowserEngineKit

Create a browser that renders content using an alternative browser engine.

**Platforms:** iOS 17.4+ | iPadOS 18.0+

## Overview

A web browser loads content and code from remote — and potentially untrusted — servers. Design your browser app to isolate access to operating system resources, the data of the person using the app, and untrusted data from the web. Code defensively to reduce the risk posed by vulnerabilities in your browser code.

For ordinary [`WKWebView`](WebKit.md#native-embedding-apis) embedding, WebKit manages its own content-process isolation. Your app does not build BrowserEngineKit extensions for that path.

To let a person choose your browser as the default, request the default-browser entitlement, whether the browser uses WebKit or an alternative engine. See [Preparing your app to be the default web browser](https://developer.apple.com/documentation/xcode/preparing-your-app-to-be-the-default-browser); ordinary in-app web content does not by itself require that role.

### Build a multi-process browser

If you use an alternative browser engine in your app, you must design your secure browser infrastructure to separate different components into extensions that your browser manages. Design a limited inter-process communication (IPC) protocol that coordinates work across the extensions. Separating your alternative browser engine into distinct extensions limits the impact of security vulnerabilities in any one process.

See [Designing your browser architecture](https://developer.apple.com/documentation/browserenginekit/designing-your-browser-architecture) and [Managing the browser extension life cycle](https://developer.apple.com/documentation/browserenginekit/managing-the-browser-extension-lifecycle).

### Render websites

BrowserEngineKit connects an alternative engine's views and asynchronous work to UIKit scrolling, drag interactions, text input, and contextual menus. Your engine remains responsible for CSS layout, JavaScript, and DOM behavior; using these UIKit integration types does not implement those standards for you.

See [Integrating custom browser text views with UIKit](https://developer.apple.com/documentation/browserenginekit/integrating-custom-browser-text-views-with-uikit).

Coordinate networking, content, and rendering extensions through a limited communication interface. [Using XPC to communicate with browser extensions](https://developer.apple.com/documentation/browserenginekit/using-xpc-to-communicate-with-browser-extensions) covers connections to those separate processes.

For marketplace installation flows, see [Enabling alternative distribution app installation in a browser](https://developer.apple.com/documentation/marketplacekit/enabling-alternative-distribution-app-installation-in-a-browser).

### Regional and embedding requirements

The [current framework documentation](https://developer.apple.com/documentation/browserenginekit) and regional requirements distinguish **EU iOS 17.4+/iPadOS 18+** from **Japan iOS 26.2+**. Distribution requires the applicable alternative-engine entitlements. The embedded-engine entitlement is for authorized non-browser apps, not apps holding the default-browser entitlement. Japan additionally requires checked allocations; embedded-engine apps there must come from a browser-engine steward and use their own engine under the engine-association rules.

The [engine-association entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.embedded-web-browser-engine.engine-association) distinguishes `third-party` engines, whose apps can install only in the EU, from `first-party` engines, whose apps can install in the EU and Japan. This is not a universal ban on third-party engines in EU embedding apps.

Consult [EU requirements](https://developer.apple.com/support/alternative-browser-engines) or [Japan requirements](https://developer.apple.com/support/alternative-browser-engines-jp), not just an OS-version check. [BrowserKit](BrowserKit.md) checks device eligibility; [BrowserEngineCore](BrowserEngineCore.md) supplies low-level support. None of these frameworks enables an arbitrary app to replace the system's WebKit engine. Safari 27 web standards and native WebKit additions are covered separately in [WebKit](WebKit.md).

### API availability is not engine eligibility

Selected **iOS declaration minima** differ from the framework baseline:

| APIs | iOS minimum |
| --- | --- |
| Scroll, drag, context-menu, media-environment, and process-capability types below | 17.4 |
| `BEWebAppManifest` | 17.5 |
| Accessibility value/selection notifications, traits, container type, and pressed state | 18 |
| `BEAccessibilityTextMarkerSupport`, `BEDownloadMonitor` | 18.2 |
| Remote accessibility elements and `BEExtensionProcess` | 26 |

Individual references also contain iPadOS and, for some integration types, other platform declarations. For example, scroll-view references list iPadOS 17.4, tvOS 17.4, and visionOS 1.1. Those declarations do not authorize an alternative browser engine on those platforms or override the regional runtime requirements above.

## Topics

### Essentials
- [Developing a browser app that uses an alternative browser engine](https://developer.apple.com/documentation/browserenginekit/developing-a-browser-app-that-uses-an-alternative-browser-engine) - Create a web browser app and associated extensions.
- [Designing your browser architecture](https://developer.apple.com/documentation/browserenginekit/designing-your-browser-architecture) - Isolate privileged access to operating system resources and private data from untrusted code.
- [Preparing your app to be the default web browser](https://developer.apple.com/documentation/xcode/preparing-your-app-to-be-the-default-browser) - Configure your browser app so users can set it as the default on their device instead of Safari.

### Browser extensions
- [Creating browser extensions in Xcode](https://developer.apple.com/documentation/browserenginekit/creating-browser-extensions-in-xcode) - Configure your Xcode project to support your alternative browser engine.
- [Extension life cycle](https://developer.apple.com/documentation/browserenginekit/extension-lifecycle) - Launch, connect to, and invalidate helper processes.
- [Extension resources](https://developer.apple.com/documentation/browserenginekit/extension-resources) - Restrict file, memory, and sandbox access.

### Web content
- [View and input coordination](https://developer.apple.com/documentation/browserenginekit/view-coordination) - Coordinate hosted layers, visibility, and input-device changes across processes.
- [Text interaction](https://developer.apple.com/documentation/browserenginekit/text-interaction) - Connect asynchronous browser text handling to the system.
- [`BEWebAppManifest`](https://developer.apple.com/documentation/browserenginekit/bewebappmanifest) - Represents a website's manifest for the [Add to Home Screen activity](https://developer.apple.com/documentation/safariservices/sfaddtohomescreenactivityitem). Supply `nil` to its manifest callback when no manifest is available.

### Scroll view interaction
- [`BEScrollView`](https://developer.apple.com/documentation/browserenginekit/bescrollview) - Supports custom scrolling and DOM nesting that differs from the view hierarchy.
- [`BEScrollViewScrollUpdate`](https://developer.apple.com/documentation/browserenginekit/bescrollviewscrollupdate) - A reused, non-thread-safe update object. Read the needed values immediately on the main queue, rather than retaining the object for later processing.
- [`BEScrollViewDelegate`](https://developer.apple.com/documentation/browserenginekit/bescrollviewdelegate) - Extends `UIScrollViewDelegate` with browser scroll-update handling.

### Drag interaction
- [`BEDragInteraction`](https://developer.apple.com/documentation/browserenginekit/bedraginteraction) - Adds asynchronous preparation to `UIDragInteraction`; use the UIKit class when asynchronous support is unnecessary.
- [`BEDragInteractionDelegate`](https://developer.apple.com/documentation/browserenginekit/bedraginteractiondelegate) - Prepares the drag and supplies items, including when that work requires JavaScript.

### Context menus
- [`BEContextMenuConfiguration`](https://developer.apple.com/documentation/browserenginekit/becontextmenuconfiguration) - Briefly defers presentation, for example while an XPC response arrives. Fulfill it with the real configuration or `nil`. Use `UIDeferredMenuElement` for ordinary asynchronous menu content.

### Accessibility
- [`BEAccessibilityTextMarkerSupport`](https://developer.apple.com/documentation/browserenginekit/beaccessibilitytextmarkersupport) - Supplies text-offset information for DOM-backed accessibility elements.
- [`valueChangedNotification`](https://developer.apple.com/documentation/browserenginekit/beaccessibility/valuechangednotification) - Post when input text or an ARIA value changes.
- [`selectionChangedNotification`](https://developer.apple.com/documentation/browserenginekit/beaccessibility/selectionchangednotification) - Post when a text selection or editing position changes; when both notifications are needed, post the value change first.
- [`BEAccessibilityContainerType`](https://developer.apple.com/documentation/browserenginekit/beaccessibilitycontainertype) - A Swift structure of container-type values, not a Swift enum.
- [`BEAccessibilityPressedState`](https://developer.apple.com/documentation/browserenginekit/beaccessibilitypressedstate) - The pressed-state enumeration.
- [`menuItem`](https://developer.apple.com/documentation/browserenginekit/beaccessibility/menuitem), [`popUpButton`](https://developer.apple.com/documentation/browserenginekit/beaccessibility/popupbutton), and [`radioButton`](https://developer.apple.com/documentation/browserenginekit/beaccessibility/radiobutton) - Traits describing the control's role.
- [`readOnly`](https://developer.apple.com/documentation/browserenginekit/beaccessibility/readonly) and [`visited`](https://developer.apple.com/documentation/browserenginekit/beaccessibility/visited) - Traits for read-only elements and visited links.

### Just-in-time code compilation
- [Protecting code compiled just in time](https://developer.apple.com/documentation/browserenginekit/protecting-code-compiled-just-in-time) - Toggle memory between being writable and executable.
- [Improving control flow integrity with pointer authentication](https://developer.apple.com/documentation/apple-silicon/improving-control-flow-integrity-with-pointer-authentication) - Protect control-flow pointers against unintended modification.
- [`BE_JIT_WRITE_PROTECT_TAG`](https://developer.apple.com/documentation/browserenginecore/be_jit_write_protect_tag) - A discriminator declared in BrowserEngineCore, used by the JIT protection mechanism.

### Downloads
- [Downloading files in a web browser with an alternative browser engine](https://developer.apple.com/documentation/browserenginekit/downloading-files-in-a-web-browser) - Register an active download and report progress so the system can keep the networking extension running.
- [`BEDownloadMonitor`](https://developer.apple.com/documentation/browserenginekit/bedownloadmonitor-9bwls) - Reports `Progress` and optionally coordinates a Downloads-folder placeholder. Your networking code still downloads the file and reports completion or cancellation.

### Classes
- [`BEAccessibilityRemoteElement`](https://developer.apple.com/documentation/browserenginekit/beaccessibilityremoteelement) - Exposes an accessibility hierarchy from the peripheral process.
- [`BEAccessibilityRemoteHostElement`](https://developer.apple.com/documentation/browserenginekit/beaccessibilityremotehostelement) - Connects that hierarchy in the main process using the same identifier.
- [`BEMediaEnvironment`](https://developer.apple.com/documentation/browserenginekit/bemediaenvironment-n91a) - Identifies a media playback or streaming environment.
- [`BEProcessCapability`](https://developer.apple.com/documentation/browserenginekit/beprocesscapability-7av05) - Describes a helper-process capability; see the lifecycle collection for capability grants.

### Protocols
- [`BEExtensionProcess`](https://developer.apple.com/documentation/browserenginekit/beextensionprocess) - The common protocol for making an extension's XPC connection and invalidating the process.

### Structures
- [`BEAccessibility`](https://developer.apple.com/documentation/browserenginekit/beaccessibility) - A structure grouping browser accessibility notifications and traits.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/BrowserEngineKit)*
