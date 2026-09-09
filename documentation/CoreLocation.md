# Core Location

Obtain the geographic location and orientation of a device.

**Platforms:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 13.1+ | macOS 10.6+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 2.0+

## Overview

Core Location provides services that determine a device's geographic location, altitude, and orientation, or its position relative to a nearby iBeacon device. It draws on available Wi-Fi, GPS, Bluetooth, magnetometer, barometer, and cellular hardware as needed; it does not activate every component for every update. Check service availability on the actual device rather than assuming every platform supports every sensor or service.

You use instances of the CLLocationManager class to configure, start, and stop the Core Location services. A location manager object supports the following location-related activities:

**Standard and significant location updates**  
Track large or small changes in the user's current location with a configurable degree of accuracy.

**Region monitoring**  
Monitor distinct regions of interest and generate location events when the user enters or leaves those regions.

**Beacon ranging**  
Detect and locate nearby beacons.

**Compass headings**  
Report heading changes from the onboard compass.

For the Swift asynchronous interface, call [`CLLocationUpdate.liveUpdates(_:)`](https://developer.apple.com/documentation/corelocation/cllocationupdate/liveupdates(_:)) and iterate over its stream to process locations and diagnostics. This API starts at iOS/iPadOS/Mac Catalyst/tvOS 17, macOS 14, visionOS 1, and watchOS 10, not at the framework's original minimum versions. `CLLocationManager` remains the delegate-based alternative.

If needed, the system requests authorization. Use the reported authorization state, not fixed button labels or the mere absence of a prompt, to decide which location-dependent features to enable.

On iOS devices, users can change location service settings at any time in the Settings app, affecting individual apps or the device as a whole. Your app receives events, including authorization changes, by observing asynchronous sequences from CLLocationUpdate and CLMonitor.

## Authorization, availability, and migration

Request the least location access the feature needs and provide the applicable usage-description strings. Observe authorization and diagnostic changes while receiving updates; missing updates can reflect permissions, reduced accuracy, or service conditions, not a stationary user.

Background behavior is platform-specific. Always authorization is unavailable on tvOS and visionOS, and visionOS apps do not receive background location updates. On macOS, When in Use and Always are functionally equivalent; on watchOS, Always access does not cause the system to launch the app. See the [authorization guide](https://developer.apple.com/documentation/corelocation/requesting-authorization-to-use-location-services) and [background lifecycle requirements](https://developer.apple.com/documentation/corelocation/handling-location-updates-in-the-background).

The current reference includes Swift asynchronous streams and Objective-C-oriented APIs such as [`CLLocationUpdater`](https://developer.apple.com/documentation/corelocation/cllocationupdater). Choose the interface and platform availability deliberately; an unfamiliar symbol in the current index is not necessarily new in OS 27.

[`CLGeocoder`](https://developer.apple.com/documentation/corelocation/clgeocoder) has a **26.0 deprecation annotation** directing developers to MapKit. Use [MapKit geocoding requests](MapKit.md) for migration, while retaining availability-appropriate handling for older clients. This is a formal deprecation, not evidence that the class was removed in OS 27. Geocoding also has network and rate-limit failure modes; do not repeatedly geocode every location update.

[`CLPlacemark`](https://developer.apple.com/documentation/corelocation/clplacemark) has a separate **27.0 deprecation annotation**, recommending [GeoToolbox's `PlaceDescriptor`](GeoToolbox.md) or MapKit. Do not assign the geocoder's 26.0 date to the placemark class, or interpret either deprecation as removal.

[`NSLocationDefaultAccuracyReduced`](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationdefaultaccuracyreduced) remains a documented, nondeprecated key. It sets the requested default accuracy; the person can still change precision in Settings.

Location push service extensions require the dedicated entitlement and the person's Always authorization. Their intended location-sharing workflows do not bypass consent or provide unlimited background polling.

## Topics

### Essentials
- [Configuring your app to use location services](https://developer.apple.com/documentation/corelocation/configuring-your-app-to-use-location-services) - Prepare your app to start collecting location data.
- [Supporting live updates in SwiftUI and Mac Catalyst apps](https://developer.apple.com/documentation/corelocation/supporting-live-updates-in-swiftui-and-mac-catalyst-apps) - Enable background events by adding lifecycle event support.
- **CLLocationManager** - The object you use to start and stop the delivery of location-related events to your app.
- **CLBackgroundActivitySession** - An object that manages a visual indicator that keeps your app in use in the background, allowing it to receive updates or events.
- **CLLocationUpdate** - A structure that contains the location information the framework delivers with each update.
- [Adopting live updates in Core Location](https://developer.apple.com/documentation/corelocation/adopting-live-updates-in-core-location) - Simplify location delivery using asynchronous events in Swift.
- [Monitoring location changes with Core Location](https://developer.apple.com/documentation/corelocation/monitoring-location-changes-with-core-location) - Define boundaries and act on user location updates.

### Authorization
- [Requesting authorization to use location services](https://developer.apple.com/documentation/corelocation/requesting-authorization-to-use-location-services) - Obtain authorization to use location services and manage changes to your app's authorization status.
- [Suspending authorization requests](https://developer.apple.com/documentation/corelocation/suspending-authorization-requests) - Defer the system's authorization request dialog until your app is ready.
- **CLAuthorizationStatus** - Constants that indicate the app's authorization to use location services.
- **CLAccuracyAuthorization** - Constants that indicate the level of location accuracy the app has authorization to use.
- **NSLocationAlwaysAndWhenInUseUsageDescription** - A message that tells people why the app is requesting access to their location information at all times.
- **NSLocationWhenInUseUsageDescription** - A message that tells people why the app is requesting access to their location information while the app is running in the foreground.
- **NSLocationUsageDescription** - A message that tells people why the app is requesting access to their location information.
- **NSLocationDefaultAccuracyReduced** - A Boolean value that indicates whether the app requests reduced location accuracy by default.
- **NSLocationAlwaysUsageDescription** - A message that tells people why the app is requesting access to their location at all times. (Deprecated)

### Monitoring
- **CLMonitor** - An object that monitors the conditions you add to it.

### Location updates
- [Getting the current location of a device](https://developer.apple.com/documentation/corelocation/getting-the-current-location-of-a-device) - Start location services and provide information the system needs to optimize power usage for those services.
- [Handling location updates in the background](https://developer.apple.com/documentation/corelocation/handling-location-updates-in-the-background) - Configure your app to receive location updates when it isn't running in the foreground.
- [Creating a location push service extension](https://developer.apple.com/documentation/corelocation/creating-a-location-push-service-extension) - Add and configure an extension to enable your location-sharing app to access a user's location in response to a request from another user.
- **CLLocation** - The latitude, longitude, and course information reported by the system.
- **CLLocationCoordinate2D** - The latitude and longitude associated with a location, specified using the WGS 84 reference frame.
- **CLFloor** - The floor of a building on which the user's device is located.
- **CLVisit** - Information about the user's location during a specific period of time.
- **CLLocationSourceInformation** - Information about the source that provides a location.
- [Monitoring location changes with Core Location](https://developer.apple.com/documentation/corelocation/monitoring-location-changes-with-core-location) - Define boundaries and act on user location updates.
- [**CLServiceSession**](https://developer.apple.com/documentation/corelocation/clservicesession-pt7n) - A retained session that expresses a workflow's authorization requirements and reports diagnostics about whether those requirements are met.

### Region monitoring
- Configure geofences and receive notifications when the user's device crosses the fence's boundaries.
- [Monitoring the user's proximity to geographic regions](https://developer.apple.com/documentation/corelocation/monitoring-the-user-s-proximity-to-geographic-regions) - Use condition monitoring to determine when the user enters or leaves a geographic region.
- **CLRegion** - A base class representing an area that can be monitored.

### iBeacon
- [Ranging for Beacons](https://developer.apple.com/documentation/corelocation/ranging-for-beacons) - Configure a device to act as a beacon and to detect surrounding beacons.
- [Determining the proximity to an iBeacon device](https://developer.apple.com/documentation/corelocation/determining-the-proximity-to-an-ibeacon-device) - Detect beacons and determine the relative distance to them.
- [Turning an iOS device into an iBeacon device](https://developer.apple.com/documentation/corelocation/turning-an-ios-device-into-an-ibeacon-device) - Broadcast iBeacon signals from an iOS device.
- **CLBeacon** - Information about an observed iBeacon device and its relative distance to a person's device.
- **CLCondition** - A [Swift protocol](https://developer.apple.com/documentation/corelocation/clcondition-swift.protocol) for monitor conditions, with a separate [Objective-C base-class interface](https://developer.apple.com/documentation/corelocation/clcondition-c.class).

### Compass headings
- Determine the device's orientation relative to magnetic or true north.
- [Getting heading and course information](https://developer.apple.com/documentation/corelocation/getting-heading-and-course-information) - Use a device's orientation and course information for navigation.
- **CLHeading** - The orientation of the user's device, relative to true or magnetic north.

### Geocoding
- [Converting between coordinates and user-friendly place names](https://developer.apple.com/documentation/corelocation/converting-between-coordinates-and-user-friendly-place-names) - Convert between a latitude and longitude pair and a more user-friendly description of that location.
- [Converting a user's location to a descriptive placemark](https://developer.apple.com/documentation/corelocation/converting-a-user-s-location-to-a-descriptive-placemark) - Transform the user's location that displays on a map into an informative textual description by reverse geocoding.
- **CLGeocoder** - An interface for converting between geographic coordinates and place names. (Deprecated)
- **CLPlacemark** - A user-friendly description of a geographic coordinate, often containing the name of the place, its address, and other relevant information. (Deprecated at 27.0; use GeoToolbox or MapKit.)

### Location push service extension
- **Location Push Service Extension** - An entitlement to enable a location-sharing app to query someone's location in response to a push notification.
- **CLLocationPushServiceExtension** - The interface you adopt in the type that acts as the main entry point for a Location Push Service Extension.
- **CLLocationPushServiceError** - Error codes the location manager returns if starting to monitor for location push notifications fails.
- **CLLocationPushServiceErrorDomain** - The domain for Location Push Service Extension errors.
- [**CLLocationPushServiceError.Code**](https://developer.apple.com/documentation/corelocation/cllocationpushserviceerror-swift.struct/code) - Error codes the location manager returns if starting to monitor for location push notifications fails.

### Errors
- **CLError** - A Core Location error.
- **kCLErrorDomain** - The domain for Core Location errors.
- [**kCLErrorUserInfoAlternateRegionKey**](https://developer.apple.com/documentation/corelocation/kclerroruserinfoalternateregionkey) - A key in the user information dictionary of an error relating to a delayed region-monitoring response.

### Reference
- [Core Location Constants](https://developer.apple.com/documentation/corelocation/core-location-constants) - This document describes the constants found in the Core Location framework.
- [Core Location Functions](https://developer.apple.com/documentation/corelocation/core-location-functions) - The Core Location framework provides functions to help you work with coordinate values.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreLocation)*
