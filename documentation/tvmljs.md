# TVMLKit JS

Create tvOS client-server apps using web technologies to stream media and respond to events.

**Platforms:** tvOS 10.0+

**Deprecated:** TVMLKit JS is deprecated in tvOS 18 and later. Instead, develop apps for tvOS with SwiftUI or UIKit. For more information, see Creating a tvOS media catalog app in SwiftUI.

## Overview

The TVMLKit JS framework provides you with the means to display client-server apps created with the Apple TV Markup Language (TVML) on tvOS. You use other classes in the framework to stream media and respond to events.

The TVMLKit JS framework incorporates the following standard Document Object Module classes, which are not documented here. For information on these classes, see World Wide Web Consortium.

**CharacterData**, **Comment**, **CustomEvent**, **Document**, **DocumentFragment**, **DOMException**, **DOMImplementation**, **DOMImplementationLS**, **DOMImplementationRegistry**, **DOMParser**, **Element**, **Event**, **EventException**, **HTMLCollection**, **LSException**, **LSInput**, **LSParser**, **LSSerializer**, **NamedNodeMap**, **Node**, **NodeList**, **ParentNode**, **ParsingElement**, **Text**, **XMLSerializer**, **XPathEvaluator**, **XPathException**, **XPathExpression**, **XPathResult**

## Topics

### Essentials
- [Creating a Client-Server TVML App](https://developer.apple.com/documentation/tvmljs/creating_a_client-server_tvml_app) - Display and navigate between TVML documents on Apple TV by retrieving and parsing information from a remote server.

### App Initialization
- **App** - An object that provides access to—and a means to respond to—app life-cycle events.
- **UserDefaults** - An object that contains the app's default preferences.
- **NavigationDocument** - A document stack that holds the individual TVML documents for a client-server app.

### Responding to User Interaction
- [Update onscreen information by adding event listeners to your Apple TV app](https://developer.apple.com/documentation/tvmljs/responding_to_user_interaction) - Update onscreen information by adding event listeners to your Apple TV app.
- **EventListenerObject** - An object that communicates events and allows other objects to add themselves as listeners.

### Device Settings
- **Device** - An object that provides information about an Apple TV and the host app installed on the device.
- **Settings** - An object that provides access to setting information for a device.
- **Restrictions** - An object used to retrieve rating restriction information.

### Media Playback
- [Playing Media in a Client-Server App](https://developer.apple.com/documentation/tvmljs/playing_media_in_a_client-server_app) - Play media items in a client-server app using the built-in media player for TVMLKit JS.
- **Player** - A media player that displays the UI for playing video and audio in an Apple TV client-server app.
- **Playlist** - An array of media items to be played in an Apple TV client-server app.
- **MediaItem** - A single audio or video item.
- **Slideshow** - An object used to display images on Apple TV in a slideshow format.
- **Browser** - An object used to configure and present a browsable full screen view.

### Element Access
- **Keyboard** - An object used to retrieve user input from search fields and text fields.
- **MenuBarDocument** - An object used for setting and retrieving documents associated with a menu item.

### Data Storage and Retrieval
- [Binding JSON data to TVML documents](https://developer.apple.com/documentation/tvmljs/binding_json_data_to_tvml_documents) - Create full-fledged TVML documents by using data binding and queries on simplified TVML files.
- **XMLHttpRequest** - An object used to retrieve data from a URL.
- **DataItem** - An object used to create observable objects from JSON objects for data binding.
- **Storage** - An object used to store key-value-pair information.
- **DataSource** - An interface that allows the system to detect and respond to changes in your data.
- **LoadIndexesRequest** - A request created when the loadindexes event is triggered.

### Errors
- **TVError** - Error codes for the TVError domain.
- **NSError** - Information about an error condition, including a domain, a domain-specific error code, and application-specific information.

### Reference
- **TVMLKit JS Functions** - The functions contained in this reference can be used globally in your app. They are not associated with a particular class.

### Classes
- **DOMException**
- **DOMImplementationLS**
- **DOMImplementationRegistry**
- **EventException**
- **LSException**
- **LSInput**
- **LSParser**
- **LSSerializer**
- **ParsingElement**
- **ViewModelLink**
- **XPathException**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/tvmljs)*