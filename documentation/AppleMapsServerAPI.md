# Apple Maps Server API

Reduce API calls and conserve device power by streamlining your app's georelated searches.

**Platforms:** Apple Maps Server API 1.2+

## Overview

Use this web-based service to streamline your app's API by moving georelated searches for places, points of interest, geocoding, directions, possible autocompletions for searches, and estimated time of arrival (ETA) calculations from inside your app to your server.

To try the Maps Server API, generate a temporary token as described in Creating a Maps token. Use these credentials to access the API from your app, or use them on Try Maps Server API.

The Apple Maps Server API is a web-based API similar to the MapKit JS API, and uses the same authorization infrastructure. It requires authorization using a JSON Web Token (JWT) for API calls. You obtain a key for creating the token when you complete the setup in your Apple Developer account.

To start using the API, you first need to generate an identifier and a private key, and authenticate with the service, following the steps below:

1. To create an identifier and private key, follow the steps in Creating a Maps identifier and a private key.
2. To create tokens from your identifier and private key with the Apple Maps Server API, follow the steps in Creating and using tokens with Maps Server API.
3. Use the Token API to Generate a Maps token for API access.

The service provides up to 25,000 service calls per day per team between Apple Maps Server API and MapKit JS. If your app exceeds this quota, the service returns an HTTP 429 error (Too Many Requests) and your app needs to retry later. If your app requires a larger daily quota, submit a quota increase request form.

## Topics

### Essentials
- [Creating and using tokens with Maps Server API](https://developer.apple.com/documentation/applemapsserverapi/creating_and_using_tokens_with_maps_server_api) - Sign JSON Web Tokens to use Maps Server API and debug common signing errors.
- [Creating a Maps identifier and a private key](https://developer.apple.com/documentation/applemapsserverapi/creating_a_maps_identifier_and_a_private_key) - Create a Maps identifier and a private key before generating tokens for MapKit JS.
- [Generate a Maps token](https://developer.apple.com/documentation/applemapsserverapi/generate_a_maps_token) - Returns a JWT maps access token that you use to call the service API.
- [Debugging an Invalid token](https://developer.apple.com/documentation/applemapsserverapi/debugging_an_invalid_token) - Inspect the JavaScript console logs, the token, and events to determine why a token is invalid.
- [Common objects](https://developer.apple.com/documentation/applemapsserverapi/common_objects) - Understand the common JSON objects that API responses contain.
- [Integrating the Apple Maps Server API into Java server applications](https://developer.apple.com/documentation/applemapsserverapi/integrating_the_apple_maps_server_api_into_java_server_applications) - Streamline your app's API by moving georelated searches from inside your app to your server.

### Geocoding
- [Geocode an address](https://developer.apple.com/documentation/applemapsserverapi/geocode_an_address) - Returns the latitude and longitude of the address you specify.
- [Reverse geocode a location](https://developer.apple.com/documentation/applemapsserverapi/reverse_geocode_a_location) - Returns an array of addresses present at the coordinates you provide.

### Searching
- **AddressCategory** - Search categories related to political geographical boundaries.
- **SearchACResultType** - An enumerated string that indicates the result type for the search request.
- **SearchResultType** - An enumerated string that indicates the result type for the search autocomplete request.
- **AlternateIdsResponse** - A list of alternate Place IDs and associated errors.
- **AlternateIdsResponse.AlternateIds** - Contains a list of alternate Place IDs for a given Place ID.
- **PlacesResponse** - A list of Place IDs and errors.
- **PlacesResponse.PlaceLookupError** - An error associated with a lookup call.
- [Search for places that match specific criteria](https://developer.apple.com/documentation/applemapsserverapi/search_for_places_that_match_specific_criteria) - Find places by name or by specific search criteria.
- [Search for places that meet specific criteria to autocomplete a place search](https://developer.apple.com/documentation/applemapsserverapi/search_for_places_that_meet_specific_criteria_to_autocomplete_a_place_search) - Find results that you can use to autocomplete searches.
- [Search for a place using an identifier](https://developer.apple.com/documentation/applemapsserverapi/search_for_a_place_using_an_identifier) - Obtain a Place object for a given Place ID.
- [Search for places using mulitple identifiers](https://developer.apple.com/documentation/applemapsserverapi/search_for_places_using_multiple_identifiers) - Obtain a set of Place objects for a given set of Place IDs.
- [Obtain a list of alternate place identifiers](https://developer.apple.com/documentation/applemapsserverapi/obtain_a_list_of_alternate_place_identifiers) - Get a list of alternate Place IDs given one or more Place IDs.

### Directions
- [Search for directions and estimated travel time between locations](https://developer.apple.com/documentation/applemapsserverapi/search_for_directions_and_estimated_travel_time_between_locations) - Find directions by specific criteria.
- [Determine estimated arrival times and distances to one or more destinations](https://developer.apple.com/documentation/applemapsserverapi/determine_estimated_arrival_times_and_distances_to_one_or_more_destinations) - Returns the estimated time of arrival (ETA) and distance between starting and ending locations.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AppleMapsServerAPI)*