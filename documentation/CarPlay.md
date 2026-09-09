# CarPlay

Integrate CarPlay in apps related to audio, communication, navigation, parking, EV charging, food ordering, and more.

**Platforms:** CarPlay framework integration begins at iOS 12.0 on compatible iPhones and vehicles. Individual app categories and APIs require later releases.

## Overview

Use the CarPlay framework to create an in-car experience for your app. The framework provides templates for building a version of your app's interface suitable for presentation on a vehicle's displays. Add the templates you want to your app and customize them to suit your content. You control the content of the templates, but the framework controls certain aspects of the template interface elements, such as the touch target size, font size, font color, and highlights.

CarPlay is an iPhone-and-vehicle experience; iPadOS and Mac Catalyst labels in the SDK catalog do not make those devices CarPlay hosts. CarPlay handles variations in vehicle systems, letting you focus on your content. When a person runs your app from their vehicle, the system generates and hosts its template interface.

Request the entitlement for the app's category and include it in the provisioning profile. Apple's [June 2026 CarPlay Developer Guide](https://developer.apple.com/download/files/CarPlay-Developer-Guide.pdf), especially the entitlement and template tables on pages 13–14, is the current category matrix. An unsupported template can raise an exception; a template's presence in the SDK is not authorization to use it.

You can use other technologies to drive portions of your app's CarPlay interface. Messaging apps can include SiriKit support to allow someone to read or send messages. VoIP apps can use CallKit to manage incoming and outgoing calls, often in combination with SiriKit call support. Navigation apps can include MapKit support.

Apple's current [SiriKit guidance](https://developer.apple.com/documentation/sirikit) says SiriKit, Intents, and IntentsUI continue to provide legacy support for most existing Siri interactions. App Intents is the direction for modern integrations; that recommendation is not a declaration that existing SiriKit support has been removed.

### Related Sessions from WWDC20

Session 10635: Accelerate Your App with CarPlay

## iOS 27 beta integration checks

The [iOS 27 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes), reviewed September 8, 2026, document fixes for `CPNavigationSession` ETA tray focus and `CPMapPanel` dismissal, delegate, and button-handler behavior. Test these paths on a supported CarPlay system, including non-touch input, rather than assuming a Simulator-only test covers vehicle interaction.

The notes also identify potentially slower Siri responses under heat or poor connectivity. Keep navigation and communication interfaces usable when a voice request is delayed.

The June 2026 developer guide explicitly lists the video-app entitlement, `com.apple.developer.carplay-video`, with an iOS 27 minimum, and requires AirPlay video streaming support. Apple's [CarPlay developer overview](https://developer.apple.com/carplay/) describes playback while parked in supported cars. This category still requires approval and a matching profile; it is not a promise of video playback in every vehicle or while driving.

The guide also expands search and voice-control template support for additional categories in iOS 27. Check the matrix's per-category footnotes rather than treating the historical topic groupings below as exclusive entitlement lists.

## Topics

### CarPlay Integration
- [Requesting CarPlay Entitlements](https://developer.apple.com/documentation/carplay/requesting-carplay-entitlements) - Configure your CarPlay-enabled app with the entitlements it requires.
- [Displaying Content in CarPlay](https://developer.apple.com/documentation/carplay/displaying-content-in-carplay) - Use scenes to present your app's content on the vehicle's built-in screen.
- [Supporting Previous Versions of iOS](https://developer.apple.com/documentation/carplay/supporting-previous-versions-of-ios) - Make your CarPlay-enabled apps compatible with older system versions, such as iOS 13 and earlier.
- [Using the CarPlay Simulator](https://developer.apple.com/documentation/carplay/using-the-carplay-simulator) - Configure Simulator to run and debug your CarPlay-enabled app.
- **CPTemplateApplicationScene** - A CarPlay scene that controls your app's user interface.
- **CPTemplateApplicationSceneDelegate** - The methods for responding to the life cycle events of your app's scene.
- **CPSessionConfiguration** - An object that provides vehicle properties and configuration for the CarPlay environment.

Retain the scene's interface controller and, for navigation, its map window during the connection. Put map content in that window and use CarPlay templates for controls and alerts, not arbitrary UIKit overlays. Test on an actual CarPlay connection as well as Simulator: Simulator does not fully reproduce locked-iPhone operation, Siri, or vehicle audio and input behavior.

### General Purpose Templates
Display your app's content using a variety of templates that provide a consistent CarPlay layout and appearance.
- **CPListTemplate** - A template that displays and manages a list of items.
- **CPGridTemplate** - A template that displays and manages a grid of items.
- **CPTabBarTemplate** - A container template that displays and manages other templates, presenting them as tabs.
- **CPTemplate** - An abstract base class for interface templates.
- **CPBarButtonProviding** - The methods that templates use to provide buttons for the navigation bar.

### Audio
Now Playing is not audio-exclusive in the current category matrix: it also covers video and public-safety apps, and communication apps from iOS 17.
- [Integrating CarPlay with Your Music App](https://developer.apple.com/documentation/carplay/integrating-carplay-with-your-music-app) - Configure your music app to work with CarPlay by displaying a custom UI.
- **CPNowPlayingTemplate** - A shared system template that displays Now Playing information.

### Instrument cluster
Symbols that are available for managing the instrument cluster.
- **CPInstrumentClusterController**
- **CPInstrumentClusterControllerDelegate**
- **CPTemplateApplicationInstrumentClusterScene**
- **CPTemplateApplicationInstrumentClusterSceneDelegate**

### Navigation
Map and dashboard navigation require the navigation entitlement. Search and voice-control templates also serve other eligible categories under the current guide's availability rules.
- [Integrating CarPlay with Your Navigation App](https://developer.apple.com/documentation/carplay/integrating-carplay-with-your-navigation-app) - Configure your navigation app to work with CarPlay by displaying your custom map and directions.
- **CPTemplateApplicationDashboardScene** - A CarPlay scene that controls your app's dashboard navigation window.
- **CPTemplateApplicationDashboardSceneDelegate** - The methods for responding to the life-cycle events of your navigation app's dashboard scene.
- **CPMapTemplate** - CarPlay's control overlay above the base map that your app draws.
- **CPSearchTemplate** - A template that provides the ability to search for a destination and see a list of search results.
- **CPVoiceControlTemplate** - A template that displays a voice control indicator during audio input.

### Location and Information
Point-of-interest and information templates are available to several categories, not only parking, EV charging, or food ordering. Their entitlement sets differ; consult the guide's matrix.
- **CPPointOfInterestTemplate** - A template that displays a map with selectable points of interest.
- **CPInformationTemplate** - A template that provides information for a point of interest, food order, parking location, or charging location.
- **CPTextButton** - A button that displays a stylized title.
- [Integrating CarPlay with your quick-ordering app](https://developer.apple.com/documentation/carplay/integrating-carplay-with-your-quick-ordering-app) - Configure your food-ordering app to work with CarPlay.

### Maneuvers
- **CPManeuver** - An object that describes a single navigation instruction.
- **CPManeuverState** - Values that describe the state of a maneuver.
- **CPManeuverType** - Values that describe types of navigation maneuvers.

### Routes, lanes and junctions
- **CPRouteInformation** - A class that describes the characteristic elements of a route.
- **CPLane** - A class that describes characteristics of a lane on a roadway.
- **CPLaneGuidance** - A class that provides information that describes the number of lanes on a roadway and navigation instruction variants.
- **CPLaneStatus** - Values that describe the status or preferability of a lane.
- **CPJunctionType** - Values that represent types of roadway junctions.

### Communication
The contact template supports communication, navigation, and public-safety apps in the current category matrix.
- **CPContactTemplate** - A template that displays information about a person or a business.

### Actions and Alerts
- **CPActionSheetTemplate** - A template that displays a modal action sheet.
- **CPAlertTemplate** - A template that displays a modal alert.
- **CPAlertAction** - An object that encapsulates an action the user can perform on an action sheet or alert.

### Related Types
- **CPButton** - A button that displays an image and invokes a handler when the user taps it.
- **CPImageSet** - Light and dark representations of an image.
- **CarPlayErrorDomain** - The domain that CarPlay uses for any errors it provides.

### Deprecated
- [Deprecated Symbols](https://developer.apple.com/documentation/carplay/deprecated-symbols) - Review individual deprecation and replacement annotations; deprecation alone does not establish removal.

### Reference
- **CarPlay Enumerations**
- **CarPlay Constants**

### Classes
- **CPListImageRowItemCardElement**
- **CPListImageRowItemCondensedElement**
- **CPListImageRowItemElement** - Abstract superclass for a row item element object.
- **CPListImageRowItemGridElement**
- **CPListImageRowItemImageGridElement**
- **CPListImageRowItemRowElement**
- **CPMessageGridItemConfiguration**
- **CPNowPlayingMode**
- **CPNowPlayingModeSports** - The sports mode represents a layout for now playing suited to live-streaming or recorded playback of a sporting event that features exactly two teams.
- **CPNowPlayingSportsClock** - Represents elapsed time for a count-up clock, or remaining time for a count-down event or period.
- **CPNowPlayingSportsEventStatus** - A representation of the status of a sporting event.
- **CPNowPlayingSportsTeam** - A representation of a sports team for the now playing screen, in sports that have exactly two teams.
- **CPNowPlayingSportsTeamLogo** - A logo image or, if no image is available, an abbreviation or initialism for this team.

### Variables
- **CPMaximumMessageItemLeadingDetailTextImageSize** - Maximum size of an image for the detailed text leading image.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CarPlay)*

*Additional source: [CarPlay Developer Guide, June 2026](https://developer.apple.com/download/files/CarPlay-Developer-Guide.pdf), including category entitlements and template availability.*
