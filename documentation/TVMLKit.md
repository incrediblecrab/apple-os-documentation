# TVMLKit

Create client-server apps by incorporating JavaScript and TVML files in your binary app.

**Platforms:** tvOS 9.0+

**Deprecated:** TVMLKit is deprecated in tvOS 18 and later. Instead, develop apps for tvOS with SwiftUI or UIKit. For more information, see Creating a tvOS media catalog app in SwiftUI.

## Overview

The TVMLKit framework enables you to evaluate TVMLKit JS and TVML files from within your tvOS app. You can create TVML elements, styles, views, and view controllers through the JavaScript environment.

## Topics

### JavaScript Environment
- [Implementing a Hybrid TV App with TVMLKit](https://developer.apple.com/documentation/tvmlkit/implementing_a_hybrid_tv_app_with_tvmlkit) - Display content options with document view controllers and fetch and populate content with TVMLKit JS.
- **TVApplicationController** - An object that bridges the UI, navigation stack, storage, and event handling from JavaScript.
- **TVApplicationControllerContext** - Launch information provided to the TV application controller.

### Views and View Controllers
- **TVViewElement** - A representation of a read-only DOM node.
- **TVInterfaceCreating** - A protocol that defines methods used to create views and view controllers.
- **TVInterfaceFactory** - A factory for the creation of views and view controllers.
- **TVBrowserViewController** - A view controller that presents content in a browsable, full-screen format.
- **TVDocumentViewController** - A view controller that represents a TVMLKit document.

### Custom Elements
- **TVElementFactory** - An object used to register new elements to extend the Apple TV Markup Language (TVML).
- **TVImageElement** - A representation of a read-only DOM node containing the attributes that describe an image element.
- **TVTextElement** - The textual content for the DOM element.
- [Creating TVML Elements](https://developer.apple.com/documentation/tvmlkit/creating_tvml_elements) - Avoid rewriting complex and often used elements by creating a simplified custom element.

### Custom Styles
- **TVViewElementStyle** - A style applied to a view element.
- **TVStyleFactory** - An object used to register custom style properties.
- **TVColor** - The color data used by styles.

### Custom Player
- **TVMediaItem** - A single audio or video item associated with the Apple TV JavaScript player.
- **TVPlaylist** - A collection of media items associated with the Apple TV JavaScript player.
- **TVPlayer** - A customizable native media player used to control playback from the JavaScript player used in an Apple TV client-server app.

### Errors
- **TVMLKitErrorDomain** - An error occurred in TVMLKit.
- **TVMLKitError** - Error codes for the TVMLKit error domain.
- **TVDocumentError**

### Reference
- **TVMLKit Enumerations**
- **TVMLKit Constants** - This document defines constants in the TVMLKit framework that are not associated with a particular class.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/TVMLKit)*