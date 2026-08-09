# Notification Center

Create and manage widgets for the Today view.

**Platforms:** iOS 8.0+ | iPadOS 8.0+ | Mac Catalyst 8.0+ | macOS 10.10+ (Deprecated)

> **Use WidgetKit instead.**

## Overview

The Notification Center framework helps you create and manage app extensions that implement Today widgets. The framework provides an API you can use to specify whether a Today widget has content to display, and to customize aspects of its appearance and behavior. In macOS, the Notification Center framework also provides ways to customize the editing and searching experience in a widget.

## Topics

### Core Widget
- **NCWidgetProviding** - The interface for customizing the appearance and behavior of a Today widget.
- **NCWidgetController** - An object used to specify whether a Today widget has content to display.

### Search View
- **NCWidgetSearchViewController** - An object that provides a default search view within a macOS Today widget.
- **NCWidgetSearchViewDelegate** - The interface for enabling user searches in the search view controller of a macOS Today widget.

### List View
- **NCWidgetListViewController** - An object that provides a list view for displaying content in a macOS Today widget.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/NotificationCenter)*