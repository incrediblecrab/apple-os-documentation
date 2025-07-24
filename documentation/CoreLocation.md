# Core Location

Obtain the geographic location and orientation of a device.

**Platforms:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 13.0+ | macOS 10.6+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 2.0+

## Overview

Core Location provides services that determine a device's geographic location, altitude, and orientation, or its position relative to a nearby iBeacon device. The framework gathers data using all available components on the device, including the Wi-Fi, GPS, Bluetooth, magnetometer, barometer, and cellular hardware.

You use instances of the CLLocationManager class to configure, start, and stop the Core Location services. A location manager object supports the following location-related activities:

**Standard and significant location updates**  
Track large or small changes in the user's current location with a configurable degree of accuracy.

**Region monitoring**  
Monitor distinct regions of interest and generate location events when the user enters or leaves those regions.

**Beacon ranging**  
Detect and locate nearby beacons.

**Compass headings**  
Report heading changes from the onboard compass.

To use location services, call liveUpdates(_:) to obtain an update stream, then asynchronously iterate over that stream to receive and process location updates, and receive diagnostic properties to understand if and why location updates don't arrive.

If needed, the system prompts the user to grant or deny the request. An initial prompt is shown in the example below:

A screenshot of an iPhone showing a prompt asking the user if they allow the "Park Finder" app to have access to their location. The options are "OK" and "Not now".

On iOS devices, users can change location service settings at any time in the Settings app, affecting individual apps or the device as a whole. Your app receives events, including authorization changes, by observing asynchronous sequences from CLLocationUpdate and CLMonitor.

## Topics

### Essentials
- [Configuring your app to use location services](https://developer.apple.com/documentation/corelocation/configuring_your_app_to_use_location_services) - Prepare your app to start collecting location data.
- [Supporting live updates in SwiftUI and Mac Catalyst apps](https://developer.apple.com/documentation/corelocation/supporting_live_updates_in_swiftui_and_mac_catalyst_apps) - Enable background events by adding lifecycle event support.
- **CLLocationManager** - The object you use to start and stop the delivery of location-related events to your app.
- **CLBackgroundActivitySession** - An object that manages a visual indicator that keeps your app in use in the background, allowing it to receive updates or events.
- **CLLocationUpdate** - A structure that contains the location information the framework delivers with each update.
- [Adopting live updates in Core Location](https://developer.apple.com/documentation/corelocation/adopting_live_updates_in_core_location) - Simplify location delivery using asynchronous events in Swift.
- [Monitoring location changes with Core Location](https://developer.apple.com/documentation/corelocation/monitoring_location_changes_with_core_location) - Define boundaries and act on user location updates.

### Authorization
- [Requesting authorization to use location services](https://developer.apple.com/documentation/corelocation/requesting_authorization_to_use_location_services) - Obtain authorization to use location services and manage changes to your app's authorization status.
- [Suspending authorization requests](https://developer.apple.com/documentation/corelocation/suspending_authorization_requests) - Defer the system's authorization request dialog until your app is ready.
- **CLAuthorizationStatus** - Constants that indicate the app's authorization to use location services.
- **CLAccuracyAuthorization** - Constants that indicate the level of location accuracy the app has authorization to use.
- **NSLocationAlwaysAndWhenInUseUsageDescription** - A message that tells people why the app is requesting access to their location information at all times.
- **NSLocationWhenInUseUsageDescription** - A message that tells people why the app is requesting access to their location information while the app is running in the foreground.
- **NSLocationUsageDescription** - A message that tells people why the app is requesting access to their location information.
- **NSLocationDefaultAccuracyReduced** - A Boolean value that indicates whether the app requests reduced location accuracy by default. (Deprecated)
- **NSLocationAlwaysUsageDescription** - A message that tells people why the app is requesting access to their location at all times. (Deprecated)

### Monitoring
- **CLMonitor** - An object that monitors the conditions you add to it.

### Location updates
- [Getting the current location of a device](https://developer.apple.com/documentation/corelocation/getting_the_current_location_of_a_device) - Start location services and provide information the system needs to optimize power usage for those services.
- [Handling location updates in the background](https://developer.apple.com/documentation/corelocation/handling_location_updates_in_the_background) - Configure your app to receive location updates when it isn't running in the foreground.
- [Creating a location push service extension](https://developer.apple.com/documentation/corelocation/creating_a_location_push_service_extension) - Add and configure an extension to enable your location-sharing app to access a user's location in response to a request from another user.
- **CLLocation** - The latitude, longitude, and course information reported by the system.
- **CLLocationCoordinate2D** - The latitude and longitude associated with a location, specified using the WGS 84 reference frame.
- **CLFloor** - The floor of a building on which the user's device is located.
- **CLVisit** - Information about the user's location during a specific period of time.
- **CLLocationSourceInformation** - Information about the source that provides a location.
- [Monitoring location changes with Core Location](https://developer.apple.com/documentation/corelocation/monitoring_location_changes_with_core_location) - Define boundaries and act on user location updates.
- **CLServiceSession**

### Region monitoring
- Configure geofences and receive notifications when the user's device crosses the fence's boundaries.
- [Monitoring the user's proximity to geographic regions](https://developer.apple.com/documentation/corelocation/monitoring_the_user_s_proximity_to_geographic_regions) - Use condition monitoring to determine when the user enters or leaves a geographic region.
- **CLRegion** - A base class representing an area that can be monitored.

### iBeacon
- [Ranging for Beacons](https://developer.apple.com/documentation/corelocation/ranging_for_beacons) - Configure a device to act as a beacon and to detect surrounding beacons.
- [Determining the proximity to an iBeacon device](https://developer.apple.com/documentation/corelocation/determining_the_proximity_to_an_ibeacon_device) - Detect beacons and determine the relative distance to them.
- [Turning an iOS device into an iBeacon device](https://developer.apple.com/documentation/corelocation/turning_an_ios_device_into_an_ibeacon_device) - Broadcast iBeacon signals from an iOS device.
- **CLBeacon** - Information about an observed iBeacon device and its relative distance to a person's device.
- **CLCondition** - The abstract base class for all other monitor conditions.

### Compass headings
- Determine the device's orientation relative to magnetic or true north.
- [Getting heading and course information](https://developer.apple.com/documentation/corelocation/getting_heading_and_course_information) - Use a device's orientation and course information for navigation.
- **CLHeading** - The orientation of the user's device, relative to true or magnetic north.

### Geocoding
- [Converting between coordinates and user-friendly place names](https://developer.apple.com/documentation/corelocation/converting_between_coordinates_and_user-friendly_place_names) - Convert between a latitude and longitude pair and a more user-friendly description of that location.
- [Converting a user's location to a descriptive placemark](https://developer.apple.com/documentation/corelocation/converting_a_user_s_location_to_a_descriptive_placemark) - Transform the user's location that displays on a map into an informative textual description by reverse geocoding.
- **CLGeocoder** - An interface for converting between geographic coordinates and place names. (Deprecated)
- **CLPlacemark** - A user-friendly description of a geographic coordinate, often containing the name of the place, its address, and other relevant information.

### Location push service extension
- **Location Push Service Extension** - An entitlement to enable a location-sharing app to query someone's location in response to a push notification.
- **CLLocationPushServiceExtension** - The interface you adopt in the type that acts as the main entry point for a Location Push Service Extension.
- **CLLocationPushServiceError** - Error codes the location manager returns if starting to monitor for location push notifications fails.
- **CLLocationPushServiceErrorDomain** - The domain for Location Push Service Extension errors.
- **Code** - Error codes the location manager returns if starting to monitor for location push notifications fails.

### Errors
- **CLError** - A Core Location error.
- **kCLErrorDomain** - The domain for Core Location errors.
- **kCLErrorUserInfoAlternateRegionKey** - A key in the user information dictionary of an error relating to a delayed region-monitoring response. (Deprecated)

### Reference
- [Core Location Constants](https://developer.apple.com/documentation/corelocation/core_location_constants) - This document describes the constants found in the Core Location framework.
- [Core Location Functions](https://developer.apple.com/documentation/corelocation/core_location_functions) - The Core Location framework provides functions to help you work with coordinate values.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreLocation)*