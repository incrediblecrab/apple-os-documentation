# BrowserEngineKit

Create a browser that renders content using an alternative browser engine.

**Platforms:** iOS 17.4+ | iPadOS 18.0+

## Overview

A web browser loads content and code from remote — and potentially untrusted — servers. Design your browser app to isolate access to operating system resources, the data of the person using the app, and untrusted data from the web. Code defensively to reduce the risk posed by vulnerabilities in your browser code.

If you use WKWebView to render web content in your browser app, WebKit automatically distributes its work to extensions that isolate their access to important resources and data.

Whether you use WebKit or write your own alternative browser engine, you need to request the entitlement to act as a person's default web browser. For more information, see Preparing your app to be the default web browser.

### Build a multi-process browser

If you use an alternative browser engine in your app, you must design your secure browser infrastructure to separate different components into extensions that your browser manages. Design a limited inter-process communication (IPC) protocol that coordinates work across the extensions. Separating your alternative browser engine into distinct extensions limits the impact of security vulnerabilities in any one process.

For more information on designing your browser extensions, see Designing your browser architecture. For information on using the extensions in your browser, see Managing the browser extension life cycle.

### Render websites

Your browser app can get significant benefits by integrating closely with UIKit. You can customize the way your app handles many low-level user interface events, ensure that your browser app correctly renders CSS, and that it properly manipulates the Javascript DOM. You can use view classes in BrowserEngineKit to handle scrolling, drag interactions, and the context menu in your browser app.

For information on integrating a custom text view with the UIKit text system, see Integrating custom browser text views with UIKit.

In your browser app, launch extensions as the person browses web content to make network requests, load the web content, and render media. For more information, see Managing the browser extension life cycle. Use XPC to communicate between your browser app and extension processes. For more information, see Using XPC to communicate with browser extensions.

For information on installing alternative app marketplaces from their company websites within your browser app, see Enabling alternative distribution app installation in a browser.

**Important:** To distribute an app that uses an alternative browser engine, you need to request the relevant entitlements for your developer account. For more information and to request the entitlements, see Using alternative browser engines in the European Union.

## Topics

### Essentials
- [Developing a browser app that uses an alternative browser engine](https://developer.apple.com/documentation/browserenginekit/developing-a-browser-app-that-uses-an-alternative-browser-engine) - Create a web browser app and associated extensions.
- [Designing your browser architecture](https://developer.apple.com/documentation/browserenginekit/designing-your-browser-architecture) - Isolate privileged access to operating system resources and private data from untrusted code.
- [Preparing your app to be the default web browser](https://developer.apple.com/documentation/browserenginekit/preparing-your-app-to-be-the-default-web-browser) - Configure your browser app so users can set it as the default on their device instead of Safari.

### Browser extensions
- [Creating browser extensions in Xcode](https://developer.apple.com/documentation/browserenginekit/creating-browser-extensions-in-xcode) - Configure your Xcode project to support your alternative browser engine.
- **Extension lifecycle** - Launch, communicate with, and invalidate browser extensions.
- **Extension resources** - Control access to files and memory in browser extensions.

### Web content
- **View coordination** - Display content in the browser's UI that an extension renders.
- **Text interaction** - Integrate your web browser engine asynchronously with the text system.
- **BEWebAppManifest** - An object that represents a web app manifest.

### Scroll view interaction
- **BEScrollView** - A scroll view that works with its delegate to handle nesting, and customize scroll interactions.
- **BEScrollViewScrollUpdate** - An object that represents a change in a scroll view's scroll state.
- **BEScrollViewDelegate** - The protocol that browser scroll view delegates conform to.

### Drag interaction
- **BEDragInteraction** - A UIDragInteraction subclass with features specific to browsers to enable asynchronous preparations and behaviours.
- **BEDragInteractionDelegate** - A protocol to which the drag interaction delegates conform.

### Context menus
- **BEContextMenuConfiguration** - A specialized UIContextMenuConfiguration object to defer a context menu presentation when the when the context menu gestures are first recognized and a possible menu presentation is not immediately known.

### Accessibility
- **BEAccessibilityTextMarkerSupport** - A set of methods that provide information about text offsets to support assistive features.
- **valueChangedNotification** - The notification you post when the value of an element changes.
- **selectionChangedNotification** - The notification you post when the selection inside an element changes.
- **BEAccessibilityContainerType** - An enumeration that indicates the type of container in which an element is located.
- **BEAccessibilityPressedState** - An enumeration that indicates whether an element is pressed.
- **menuItem** - The accessibility element behaves like a menu item.
- **popUpButton** - The accessibility element behaves like a pop-up button.
- **radioButton** - The accessibility element behaves like a radio button.
- **readOnly** - The accessibility element is read-only.
- **visited** - The accessibility element behaves like a link that someone previously visited.

### Just-in-time code compilation
- [Protecting code compiled just in time](https://developer.apple.com/documentation/browserenginekit/protecting-code-compiled-just-in-time) - Toggle memory between being writable and executable.
- [Improving control flow integrity with pointer authentication](https://developer.apple.com/documentation/browserenginekit/improving-control-flow-integrity-with-pointer-authentication) - Increase confidence that your code uses pointers correctly.
- **BE_JIT_WRITE_PROTECT_TAG** - A discriminator value the system uses to generate pointer authentication codes for just-in-time compilation.

### Downloads
- [Downloading files in a web browser with an alternative browser engine](https://developer.apple.com/documentation/browserenginekit/downloading-files-in-a-web-browser-with-an-alternative-browser-engine) - Report download progress to the system to keep your networking extension active.
- **BEDownloadMonitor** - An object that reports the status of web downloads to the system.

### Classes
- **BEAccessibilityRemoteElement** (Beta)
- **BEAccessibilityRemoteHostElement** (Beta)
- **BEMediaEnvironment**
- **BEProcessCapability**

### Protocols
- **BEExtensionProcess** (Beta)

### Structures
- **BEAccessibility**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/BrowserEngineKit)*