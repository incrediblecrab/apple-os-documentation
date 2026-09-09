# GeoToolbox

Determine place descriptor information for map coordinates.

**Platforms:** iOS 26.0+ | iPadOS 26.0+ | Mac Catalyst 26.0+ | macOS 26.0+ | tvOS 26.0+ | visionOS 26.0+ | watchOS 26.0+

## Overview

Use GeoToolbox to create PlaceDescriptor structures for use across Maps technologies and third-party mapping systems.

`PlaceDescriptor` packages identifying representations of a place; it is not itself a map renderer, geocoding server, or location-permission request. The receiving mapping service decides how to resolve those representations. Preserve provider-specific identifiers with their provider context and handle an unresolved place without assuming that an identifier works across all services.

Supply at least one `PlaceRepresentation`, ordered with the original or most accurate information first. Supporting service identifiers supplement rather than replace that required representation. `init(item:)` is failable: handle a `nil` descriptor when the system cannot resolve the map item.

GeoToolbox's platform baseline remains 26.0, not 27.0. Obtaining the person's device location still requires the appropriate [Core Location](CoreLocation.md) authorization; constructing a descriptor from an existing address or coordinate does not grant that access. A server lookup uses the mapping service's own authentication.

## Topics

### Getting Rich Information About a Place
- [`PlaceDescriptor`](https://developer.apple.com/documentation/geotoolbox/placedescriptor) - Identifying information a mapping service can use to find richer place details.

### Creating a Place Descriptor
- [`init(item:)`](https://developer.apple.com/documentation/geotoolbox/placedescriptor/init(item:)) - Attempt to create a place descriptor from a map item; returns `nil` if it cannot resolve the item.
- [`init(representations:commonName:supportingRepresentations:)`](https://developer.apple.com/documentation/geotoolbox/placedescriptor/init(representations:commonname:supportingrepresentations:)) - Construct a descriptor from place representations and supporting information.

### Values That Describe Places and Mapping Service Providers
- [`PlaceRepresentation`](https://developer.apple.com/documentation/geotoolbox/placedescriptor/placerepresentation) - Values that represent a physical place.
- [`SupportingPlaceRepresentation`](https://developer.apple.com/documentation/geotoolbox/placedescriptor/supportingplacerepresentation) - Provider-specific supporting representations.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/GeoToolbox)*
