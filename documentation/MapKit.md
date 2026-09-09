# MapKit

Display map or satellite imagery within your app, call out points of interest, and determine placemark information for map coordinates.

**Framework catalog:** iOS 3.0+ | iPadOS 3.0+ | Mac Catalyst 13.0+ | macOS 10.9+ | tvOS 9.2+ | visionOS 1.0+ | watchOS 2.0+. Check individual declarations; for example, the legacy UIKit overlay views below use Mac Catalyst 13.1 annotations.

## Overview

Use MapKit to give your app a sense of place with maps and location information. You can use the MapKit framework to:

- Embed maps directly into your app's windows and views.
- Add annotations and overlays to a map to call out points of interest.
- Add LookAround capabilities to enable users to explore locations at street level.
- Respond to user interactions with well known points of interest, geographical features, and boundaries.
- Provide text completion to make it easy for users to search for a destination or point of interest.

## Current API guidance

The [MapKit updates](https://developer.apple.com/documentation/updates/mapkit) page documents geocoding requests, address representations, and cycling directions in its June 2025 update; these should not be relabeled as OS 27 introductions. Use [`MKGeocodingRequest`](https://developer.apple.com/documentation/mapkit/mkgeocodingrequest) and [`MKReverseGeocodingRequest`](https://developer.apple.com/documentation/mapkit/mkreversegeocodingrequest) when migrating from Core Location's deprecated `CLGeocoder`, with availability checks for older clients.

[`MKAddress`](https://developer.apple.com/documentation/mapkit/mkaddress) and [`MKAddressRepresentations`](https://developer.apple.com/documentation/mapkit/mkaddressrepresentations) support displayable place information. [Unified Maps URLs](https://developer.apple.com/documentation/mapkit/unified-map-urls) provide a separate way to open Maps experiences.

The geocoding-request and address classes above have 26.0 introductions across their declared platforms. Unified Maps URLs instead begin at iOS 18.4, macOS 15.4, and watchOS 11.4 in the URL guide. Neither is a blanket OS 27 feature.

Handle failed or canceled searches, unavailable directions, and ambiguous geocoding results. Showing a map does not itself authorize access to the person's location; request that access through [Core Location](CoreLocation.md) when needed. Test map annotations and controls with the supported accessibility settings.

## Topics

### The MapKit APIs
- [MapKit for AppKit and UIKit](https://developer.apple.com/documentation/mapkit/mapkit-for-appkit-and-uikit)
- [MapKit for SwiftUI](https://developer.apple.com/documentation/mapkit/mapkit-for-swiftui) - MapKit for SwiftUI allows you to build map-centric views and apps across Apple platforms. You can design expressive and highly interactive Maps with minimal code by composing views, using ViewBuilders and view modifiers.
- [Adopting unified Maps URLs](https://developer.apple.com/documentation/mapkit/unified-map-urls) - Access Maps URLs and options for displaying Maps information across Apple platforms.

### Articles
- [Deprecated Symbols](https://developer.apple.com/documentation/mapkit/deprecated-symbols) - Review individual replacement and deprecation annotations rather than treating the collection as a removal list.
- [Preparing your app to be the default navigation app](https://developer.apple.com/documentation/mapkit/preparing-your-app-to-be-the-default-navigation-app) - Configure the entitlement, URL scheme, and background support for default navigation where the platform and region support it.

### Classes

These legacy overlay views have formal deprecation annotations at iOS/iPadOS 13.0 and Mac Catalyst 13.1. Their articles recommend renderer replacements from iOS 7 onward; that earlier recommendation is not the formal deprecation date. The declarations do not mark them removed.

- [**MKCircleView**](https://developer.apple.com/documentation/mapkit/mkcircleview) - Draws an `MKCircle` overlay. *Deprecated; use `MKCircleRenderer`.*
- [**MKOverlayPathView**](https://developer.apple.com/documentation/mapkit/mkoverlaypathview) - Draws path-based overlays. *Deprecated; use `MKOverlayPathRenderer`.*
- [**MKOverlayView**](https://developer.apple.com/documentation/mapkit/mkoverlayview) - Provides overlay-view drawing infrastructure. *Deprecated; use `MKOverlayRenderer`.*
- [**MKPolygonView**](https://developer.apple.com/documentation/mapkit/mkpolygonview) - Fills and strokes an `MKPolygon` overlay. *Deprecated; use `MKPolygonRenderer`.*
- [**MKPolylineView**](https://developer.apple.com/documentation/mapkit/mkpolylineview) - Strokes an `MKPolyline` without filling it. *Deprecated; use `MKPolylineRenderer`.*

### Structures
- [**AnyMapContent**](https://developer.apple.com/documentation/mapkit/anymapcontent) - Type-erased map content; starts at iOS/iPadOS/Mac Catalyst/tvOS 17.5, macOS 14.5, visionOS 1.2, and watchOS 10.5.

## See Also

### Related Documentation
- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html) - Archived guidance; use current symbol references for availability.
- [MapKit JS](https://developer.apple.com/documentation/mapkitjs) - Embed interactive Apple Maps on your website, annotate points of interest, and perform georelated searches.
- [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi) - Reduce API calls and conserve device power by streamlining your app's georelated searches.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MapKit)*
