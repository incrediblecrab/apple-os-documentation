# Apple Maps Server API

Reduce API calls and conserve device power by streamlining your app's georelated searches.

**Availability:** Maps web service for authorized developer teams, independent of an OS 27 app deployment target.

## Overview

Use this web-based service to streamline your app's API by moving georelated searches for places, points of interest, geocoding, directions, possible autocompletions for searches, and estimated time of arrival (ETA) calculations from inside your app to your server.

The Apple Maps Server API shares Maps authorization infrastructure with MapKit JS, but product scope matters. The dynamic server flow uses a signed authorization JWT and exchanges it for a Maps access token. Keep the signing key in your backend, not an app or webpage.

To start using the API, you first need to generate an identifier and a private key, and authenticate with the service, following the steps below:

1. To create an identifier and private key, follow the steps in Creating a Maps identifier and a private key.
2. To create tokens from your identifier and private key with the Apple Maps Server API, follow the steps in Creating and using tokens with Maps Server API.
3. Use the Token API to Generate a Maps token for API access.

The service provides up to 25,000 service calls per day per team between Apple Maps Server API and MapKit JS. If your app exceeds this quota, the service returns an HTTP 429 error (Too Many Requests) and your app needs to retry later. If your app requires a larger daily quota, submit a quota increase request form.

## Integration and failure handling

Follow [Creating and using tokens](https://developer.apple.com/documentation/applemapsserverapi/creating-and-using-tokens-with-maps-server-api): sign with `ES256`, provide the required key/team and timestamp claims, and include `server_api` in `scope`. An `origin` is required for browser-oriented scopes such as `mapkit_js`, not universally for a server-only token. Do not reuse App Store Connect or Apple Ads credentials.

Exchange the signed token with `GET https://maps-api.apple.com/v1/token`. Use the returned `accessToken` for service calls and respect its returned `expiresInSeconds`; the example's 1,800 seconds is not a universal lifetime guarantee. The linked portal-token and signing guides differ about static Server API token support, so this reference uses the documented dynamic exchange flow rather than promising that every portal token is interchangeable.

Process pagination and per-place lookup errors, handle no matches and ambiguous results, and back off on `429`. An expired or invalid token needs authorization repair, not an endless search retry. Avoid retaining more customer location information than the feature requires.

This API retrieves geographic information. The separate [Apple Ads Platform API](AppleAdsPlatformAPI.md) manages advertising on Apple Maps; similar product names do not make their endpoints or tokens interchangeable.

## Topics

### Essentials
- [Creating and using tokens with Maps Server API](https://developer.apple.com/documentation/applemapsserverapi/creating-and-using-tokens-with-maps-server-api) - Sign JSON Web Tokens to use Maps Server API and debug common signing errors.
- [Creating a Maps identifier and a private key](https://developer.apple.com/documentation/applemapsserverapi/creating-a-maps-identifier-and-a-private-key) - Create a Maps identifier and a private key before generating tokens for MapKit JS.
- [Generate a Maps token](https://developer.apple.com/documentation/applemapsserverapi/-v1-token) - Returns a JWT maps access token that you use to call the service API.
- [Debugging an Invalid token](https://developer.apple.com/documentation/applemapsserverapi/debugging-an-invalid-token) - Inspect the token and errors to determine why authorization fails.
- [Common objects](https://developer.apple.com/documentation/applemapsserverapi/common-objects) - Understand the common JSON objects that API responses contain.
- [Integrating the Apple Maps Server API into Java server applications](https://developer.apple.com/documentation/applemapsserverapi/integrating-the-apple-maps-server-api-into-java-server-applications) - Move georelated searches from inside your app to your server.

### Geocoding
- [Geocode an address](https://developer.apple.com/documentation/applemapsserverapi/-v1-geocode) - Returns the latitude and longitude of the address you specify.
- [Reverse geocode a location](https://developer.apple.com/documentation/applemapsserverapi/-v1-reversegeocode) - Returns an array of addresses present at the coordinates you provide.

### Searching
- **AddressCategory** - Search categories related to political geographical boundaries.
- [**SearchACResultType**](https://developer.apple.com/documentation/applemapsserverapi/searchacresulttype) - A result-category string enumeration that includes `query` alongside address, physical-feature, and point-of-interest categories.
- [**SearchResultType**](https://developer.apple.com/documentation/applemapsserverapi/searchresulttype) - A result-category string enumeration for address, physical-feature, and point-of-interest categories; its listed values do not include `query`.
- **AlternateIdsResponse** - A list of alternate Place IDs and associated errors.
- **AlternateIdsResponse.AlternateIds** - Contains a list of alternate Place IDs for a given Place ID.
- [**PlacesResponse**](https://developer.apple.com/documentation/applemapsserverapi/placesresponse) - Resolved `Place` objects and per-place lookup errors, not merely a list of input identifiers.
- **PlacesResponse.PlaceLookupError** - An error associated with a lookup call.
- [Search for places](https://developer.apple.com/documentation/applemapsserverapi/-v1-search) - Find places by name or by specific search criteria.
- [Autocomplete a place search](https://developer.apple.com/documentation/applemapsserverapi/-v1-searchautocomplete) - Find results for search completion.
- [Look up a place](https://developer.apple.com/documentation/applemapsserverapi/-v1-place-:id) - Obtain a Place object for a given Place ID.
- [Look up multiple places](https://developer.apple.com/documentation/applemapsserverapi/-v1-place) - Obtain Place objects for a set of Place IDs.
- [Obtain alternate place identifiers](https://developer.apple.com/documentation/applemapsserverapi/-v1-place-alternateids) - Get alternate Place IDs.

### Directions
- [Search for directions](https://developer.apple.com/documentation/applemapsserverapi/-v1-directions) - Find directions by specific criteria.
- [Determine arrival times and distances](https://developer.apple.com/documentation/applemapsserverapi/-v1-etas) - Return ETA and distance between starting and ending locations.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AppleMapsServerAPI)*
