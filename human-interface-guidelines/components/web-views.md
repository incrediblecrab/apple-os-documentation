# Web views

A web view loads and displays rich web content, such as embedded HTML and websites, directly within your app.

**Platforms:** iOS | iPadOS | macOS | visionOS

## Overview

For example, Mail uses a web view to show HTML content in messages.

## Topics

### Best Practices

- **Support forward and back navigation when appropriate** - Web views support forward and back navigation, but this behavior isn't available by default. If people are likely to use your web view to visit multiple pages, allow forward and back navigation, and provide corresponding controls to initiate these features.

- **Avoid using a web view to build a web browser** - Using a web view to let people briefly access a website without leaving the context of your app is fine, but Safari is the primary way people browse the web. Attempting to replicate the functionality of Safari in your app is unnecessary and discouraged.

### Platform Considerations

**iOS, iPadOS, macOS, visionOS**

No additional considerations.

**tvOS, watchOS**

Not supported.

### Related Resources

- [Webkit.org](https://webkit.org) - WebKit documentation and resources

### Developer Documentation

- [WKWebView](https://developer.apple.com/documentation/webkit/wkwebview) - WebKit

### Videos

- [Explore WKWebView additions](https://developer.apple.com/videos/play/wwdc2023/10118/)

---

*Design baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Reviewed 2026-08-09.*

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/web-views)*