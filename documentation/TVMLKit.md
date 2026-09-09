# TVMLKit

Create client-server apps by incorporating JavaScript and TVML files in your binary app.

**Platforms:** tvOS 9.0+

**Deprecated:** TVMLKit is deprecated in tvOS 18 and later; deprecation is not removal. Use [SwiftUI](SwiftUI.md) or [UIKit](UIKit.md) for new tvOS work. See [Creating a tvOS media catalog app in SwiftUI](https://developer.apple.com/documentation/swiftui/creating-a-tvos-media-catalog-app-in-swiftui).

## Overview

TVMLKit hosts [TVMLKit JS](tvmljs.md) and turns [TVML](TVML.md) documents into native tvOS views. `TVApplicationController` coordinates the JavaScript environment with navigation and events. A hybrid app can instead use `TVDocumentViewController` for native navigation and event handling while JavaScript fetches data and populates documents.

The framework starts at **tvOS 9**, but its native media-player bridge starts at **12**, and document/browser controllers and document errors start at **13**. Most references below explicitly mark deprecation at 18. `TVBrowserViewController` currently lacks that per-class annotation; do not fabricate one from the framework-level migration guidance.

## Topics

### JavaScript Environment
- [Implementing a Hybrid TV App with TVMLKit](https://developer.apple.com/documentation/tvmlkit/implementing-a-hybrid-tv-app-with-tvmlkit) - Native document-controller navigation with JavaScript content population.
- [`TVApplicationController`](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontroller) - Establishes and coordinates the JavaScript environment.
- [`TVApplicationControllerContext`](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollercontext) - Supplies launch information.

### Views and View Controllers
- [`TVViewElement`](https://developer.apple.com/documentation/tvmlkit/tvviewelement) - A read-only DOM model traversed to create native views; dispatch user events back to JavaScript.
- [`TVInterfaceCreating`](https://developer.apple.com/documentation/tvmlkit/tvinterfacecreating) - Creates views/controllers from that model.
- [`TVInterfaceFactory`](https://developer.apple.com/documentation/tvmlkit/tvinterfacefactory) - Uses `extendedInterfaceCreator` for custom view creation.
- [`TVBrowserViewController`](https://developer.apple.com/documentation/tvmlkit/tvbrowserviewcontroller) - A tvOS 13+ full-screen content browser with cell transitions, not a web browser.
- [`TVDocumentViewController`](https://developer.apple.com/documentation/tvmlkit/tvdocumentviewcontroller) - A tvOS 13+ bridge to the JavaScript document lifecycle and native event handling.

### Custom Elements
- [`TVElementFactory`](https://developer.apple.com/documentation/tvmlkit/tvelementfactory) - Register custom element names **before** initializing `TVApplicationController`.
- [`TVImageElement`](https://developer.apple.com/documentation/tvmlkit/tvimageelement) - Read-only image-node information.
- [`TVTextElement`](https://developer.apple.com/documentation/tvmlkit/tvtextelement) - Text-node content.
- [Creating TVML Elements](https://developer.apple.com/documentation/tvmlkit/creating-tvml-elements) - Register an element and implement its native presentation.

### Custom Styles
- [`TVViewElementStyle`](https://developer.apple.com/documentation/tvmlkit/tvviewelementstyle) - Style data for an element.
- [`TVStyleFactory`](https://developer.apple.com/documentation/tvmlkit/tvstylefactory) - Registers custom style properties.
- [`TVColor`](https://developer.apple.com/documentation/tvmlkit/tvcolor) - Color data used by styles.

### Custom Player
- [`TVMediaItem`](https://developer.apple.com/documentation/tvmlkit/tvmediaitem) - Read-only information about an item associated with the JavaScript player.
- [`TVPlaylist`](https://developer.apple.com/documentation/tvmlkit/tvplaylist) - Read-only playlist information from that player.
- [`TVPlayer`](https://developer.apple.com/documentation/tvmlkit/tvplayer) - Connects a custom `AVPlayer` to JavaScript media playback. All three native bridge types start at tvOS 12, unlike the older JavaScript `Player`/`Playlist`/`MediaItem`.

### Errors
- [`TVMLKitErrorDomain`](https://developer.apple.com/documentation/tvmlkit/tvmlkiterrordomain) - The framework error-domain string.
- [`TVMLKitError`](https://developer.apple.com/documentation/tvmlkit/tvmlkiterror) - Framework error codes.
- [`TVDocumentError`](https://developer.apple.com/documentation/tvmlkit/tvdocumenterror-swift.struct) - The tvOS 13+ Swift document-error wrapper.

### Reference
- [TVMLKit Enumerations](https://developer.apple.com/documentation/tvmlkit/tvmlkit-enumerations) - Includes document-error codes.
- [TVMLKit Constants](https://developer.apple.com/documentation/tvmlkit/tvmlkit-constants) - Includes the document-error domain.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/TVMLKit)*
