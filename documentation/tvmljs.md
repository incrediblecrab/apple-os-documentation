# TVMLKit JS

Create tvOS client-server apps using web technologies to stream media and respond to events.

**Platforms:** tvOS 9.0+ for the core runtime APIs; later API generations are listed below.

**Deprecated:** TVMLKit JS is deprecated in tvOS 18 and later, not declared removed. Use SwiftUI or UIKit for new apps. See [Creating a tvOS media catalog app in SwiftUI](https://developer.apple.com/documentation/swiftui/creating-a-tvos-media-catalog-app-in-swiftui).

## Overview

TVMLKit JS supplies lifecycle, navigation, playback, input, and data APIs to [TVML](TVML.md) apps hosted by [TVMLKit](TVMLKit.md). It is not a Safari browser environment; shared JavaScript interface names do not imply support for modern browser DOM/CSS or Safari 27 features.

The legacy catalog includes the following **Document Object Model**-related names. This mixes DOM interfaces, historical DOM Load/Save and XPath interfaces, and helper labels; it is not a list of current standard JavaScript constructors. Compare the [current DOM standard](https://dom.spec.whatwg.org/) and the historical [DOM Level 3 Load and Save specification](https://www.w3.org/TR/DOM-Level-3-LS/) when maintaining such code.

**CharacterData**, **Comment**, **CustomEvent**, **Document**, **DocumentFragment**, **DOMException**, **DOMImplementation**, **DOMImplementationLS**, **DOMImplementationRegistry**, **DOMParser**, **Element**, **Event**, **EventException**, **HTMLCollection**, **LSException**, **LSInput**, **LSParser**, **LSSerializer**, **NamedNodeMap**, **Node**, **NodeList**, **ParentNode**, **ParsingElement**, **Text**, **XMLSerializer**, **XPathEvaluator**, **XPathException**, **XPathExpression**, **XPathResult**

## API generations

The framework catalog's tvOS 10 label does not date every API:

| tvOS introduction | APIs |
| --- | --- |
| 9 | `App`, `NavigationDocument`, event/device/settings/restrictions APIs, `Player`, `Playlist`, `MediaItem`, `Keyboard`, `MenuBarDocument`, `Storage`, `XMLHttpRequest`, `TVError` |
| 10 | `UserDefaults`, `Slideshow` |
| 11 | `DataItem`, the JavaScript `NSError` interface |
| 13 | `Browser`, `DataSource`, `LoadIndexesRequest`, `ViewModelLink` |
| 14 | The additional DOM/Load-Save/exception references in the Classes section, except `ViewModelLink` |

These are the published reference labels for this runtime, not introduction dates for the corresponding web standards in other browsers.

## Topics

### Essentials
- [Creating a Client-Server TVML App](https://developer.apple.com/documentation/tvmljs/creating_a_client-server_tvml_app) - Display and navigate between TVML documents on Apple TV by retrieving and parsing information from a remote server.

### App Initialization
- [`App`](https://developer.apple.com/documentation/tvmljs/app) - The system-provided global lifecycle object; do not construct one.
- [`UserDefaults`](https://developer.apple.com/documentation/tvmljs/userdefaults) - Preferences exposed as the global `userDefaults`.
- [`NavigationDocument`](https://developer.apple.com/documentation/tvmljs/navigationdocument) - The system-provided document stack at `navigationDocument`; do not construct one.

### Responding to User Interaction
- [Responding to User Interaction](https://developer.apple.com/documentation/tvmljs/responding_to_user_interaction) - Update content in response to focus/navigation events, not only selection.
- [`EventListenerObject`](https://developer.apple.com/documentation/tvmljs/eventlistenerobject) - Event dispatch and listener registration.

### Device Settings
- [`Device`](https://developer.apple.com/documentation/tvmljs/device) - The global device/host-app information object.
- [`Settings`](https://developer.apple.com/documentation/tvmljs/settings) - The global settings-information object.
- [`Restrictions`](https://developer.apple.com/documentation/tvmljs/restrictions) - Rating restriction information obtained from `Settings`. These are supplied objects, not constructors for changing system parental controls.

### Media Playback
- [Playing Media in a Client-Server App](https://developer.apple.com/documentation/tvmljs/playing_media_in_a_client-server_app) - Play media items in a client-server app using the built-in media player for TVMLKit JS.
- [`Player`](https://developer.apple.com/documentation/tvmljs/player) - Playback UI and control; assign a `Playlist` containing at least one `MediaItem` to play media.
- [`Playlist`](https://developer.apple.com/documentation/tvmljs/playlist) - The playback sequence.
- [`MediaItem`](https://developer.apple.com/documentation/tvmljs/mediaitem) - An audio or video item.
- [`Slideshow`](https://developer.apple.com/documentation/tvmljs/slideshow) - Start an image slideshow through its `start` method; there is no constructor.
- [`Browser`](https://developer.apple.com/documentation/tvmljs/browser) - Configure and present a full-screen content browser using `present`; there is no constructor, and this is not a web browser.

### Element Access
- [`Keyboard`](https://developer.apple.com/documentation/tvmljs/keyboard) - Obtain the keyboard feature from a `searchField` or `textField` element with `getFeature('Keyboard')`.
- [`MenuBarDocument`](https://developer.apple.com/documentation/tvmljs/menubardocument) - Obtain a menu bar's document-management feature with `getFeature('MenuBarDocument')`.

### Data Storage and Retrieval
- [Binding JSON data to TVML documents](https://developer.apple.com/documentation/tvmljs/binding_json_data_to_tvml_documents) - Create full-fledged TVML documents by using data binding and queries on simplified TVML files.
- [`XMLHttpRequest`](https://developer.apple.com/documentation/tvmljs/xmlhttprequest) - Retrieves URL resources.
- [`DataItem`](https://developer.apple.com/documentation/tvmljs/dataitem) - Observable data for TVML bindings.
- [`Storage`](https://developer.apple.com/documentation/tvmljs/storage) - The supplied `localStorage` and `sessionStorage` objects, not a constructor. Session data is in memory and is purged when the app exits; local storage writes to disk.
- [`DataSource`](https://developer.apple.com/documentation/tvmljs/datasource) - Tracks changes to array-backed data and supports lazy loading without repopulating the entire interface.
- [`LoadIndexesRequest`](https://developer.apple.com/documentation/tvmljs/loadindexesrequest) - A request associated with a `loadindexes` event.

### Errors
- [`TVError`](https://developer.apple.com/documentation/tvmljs/tverror) - An error object with a domain, code, and user information, not merely an enum of codes.
- [`NSError`](https://developer.apple.com/documentation/tvmljs/nserror) - The tvOS 11+ JavaScript error-information interface; distinguish it from Foundation's native API history.

### Reference
- [TVMLKit JS Functions](https://developer.apple.com/documentation/tvmljs/tvmlkit_js_functions) - Global functions supplied by this app environment.

### Classes
These links retain the legacy catalog's interface labels and per-entry declarations, not a promise that each name is a constructible global in every DOM implementation.

- [`DOMException`](https://developer.apple.com/documentation/tvmljs/domexception)
- [`DOMImplementationLS`](https://developer.apple.com/documentation/tvmljs/domimplementationls)
- [`DOMImplementationRegistry`](https://developer.apple.com/documentation/tvmljs/domimplementationregistry)
- [`EventException`](https://developer.apple.com/documentation/tvmljs/eventexception)
- [`LSException`](https://developer.apple.com/documentation/tvmljs/lsexception)
- [`LSInput`](https://developer.apple.com/documentation/tvmljs/lsinput)
- [`LSParser`](https://developer.apple.com/documentation/tvmljs/lsparser)
- [`LSSerializer`](https://developer.apple.com/documentation/tvmljs/lsserializer)
- [`ParsingElement`](https://developer.apple.com/documentation/tvmljs/parsingelement)
- [`ViewModelLink`](https://developer.apple.com/documentation/tvmljs/viewmodellink)
- [`XPathException`](https://developer.apple.com/documentation/tvmljs/xpathexception)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/tvmljs)*
