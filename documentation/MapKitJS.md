# MapKit JS

Embed interactive Apple Maps on your website, annotate points of interest, and perform georelated searches.

**Availability:** A versioned JavaScript library for supported web browsers, independent of the native OS SDK. Review version 6's migration requirements when upgrading a version 5 integration.

## Overview

Use this JavaScript API to embed interactive maps directly into your webpages or apps across different platforms and operating systems, including iOS and Android. Like MapKit for native apps, you can also add annotations and overlays to the map to call out points of interest or user destinations.

MapKit JS also provides interactive views for place details, and Look Around imagery.

MapKit JS requires authorization through a Maps token for initialization and some API calls. To create a Maps token, see Creating a Maps token.

Choose a **MapKit JS** token when provisioning through the developer account. For dynamically signed tokens, the current [token guide](https://developer.apple.com/documentation/mapkitjs/creating-a-maps-token) requires the `mapkit_js` scope and an `origin`. Sharing Maps infrastructure does not make every product-scoped token interchangeable.

Load the libraries your feature needs using the [current loader or core script](https://developer.apple.com/documentation/mapkitjs/loading-the-latest-version-of-mapkit-js). In particular, Look Around needs the `look-around` library; the full `mapkit.js` bundle does not contain that newer feature.

### Browser compatibility

Use the current [browser support reference](https://developer.apple.com/documentation/mapkitjs/browser-support) for the library version you deploy. Native MapKit's OS availability does not establish a JavaScript browser baseline.

## Version 6 migration

The [version 5-to-6 migration guide](https://developer.apple.com/documentation/mapkitjs/migrating-from-version-5-to-version-6), reviewed September 8, 2026, distinguishes breaking changes from retained-but-deprecated interfaces:

- The custom event system is replaced by DOM `EventTarget`. The third `addEventListener` argument is now event-listener options, not a `thisObject`; explicitly bind listener context when needed.
- Optional API properties, return values, and callback/event data use `null` rather than `undefined` for absence. Review strict equality checks and TypeScript nullability.
- Images, including tiles and annotations, require CORS-clean data. Test your asset hosts rather than assuming previously working image URLs remain sufficient.
- Asynchronous services return Promises. Callbacks still work but are deprecated; prefer `AbortController`/`AbortSignal` to numeric request cancellation. An aborted request rejects with `AbortError`, while `RequestError` represents network/HTTP failures.
- `TileOverlay.urlTemplate` remains a deprecated alias of `imageForTile`; old enumeration accessors also remain with warnings. These are not immediate removals.

Use a valid Maps token, handle initialization/load rejection and service failures, and stop obsolete searches when the query changes. Keep the signing key off the website; the browser receives only the intended token. [Apple Maps Server API](AppleMapsServerAPI.md) shares the Maps authorization infrastructure and service quota.

## Topics

### Essentials
- [Displaying place information using the Maps Embed API](https://developer.apple.com/documentation/mapkitjs/displaying-place-information-using-the-maps-embed-api) - Show place information on a map using a URL.
- [Creating a Maps token](https://developer.apple.com/documentation/mapkitjs/creating-a-maps-token) - Generate your token to access MapKit services with proper authorization.
- [Loading the latest version of MapKit JS](https://developer.apple.com/documentation/mapkitjs/loading-the-latest-version-of-mapkit-js) - Link to the most recent autoupdating version of MapKit JS, or a version of your choice.
- **mapkit** - The JavaScript API for embedding Apple Maps on your website.

### Version notes
- [MapKit JS Release Notes](https://developer.apple.com/documentation/mapkitjs/mapkit-js-release-notes) - Learn about updates, bug fixes, and API changes for MapKit JS.
- [Migrating from Version 5 to Version 6](https://developer.apple.com/documentation/mapkitjs/migrating-from-version-5-to-version-6) - Review breaking changes, deprecations, and modern web API conventions.

## See Also

### Related Documentation
- [MapKit](https://developer.apple.com/documentation/mapkit) - Display map or satellite imagery within your app, call out points of interest, and determine placemark information for map coordinates.
- [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi) - Reduce API calls and conserve device power by streamlining your app's georelated searches.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MapKitJS)*
