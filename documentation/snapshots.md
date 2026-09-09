# Maps Web Snapshots

Create a static image of a map from a URL.

**Service reference:** Maps Web Snapshots 1.0 — a service catalog version, not an Apple OS minimum.

## Overview

Use the Maps Web Snapshots service to generate static map images from a URL. You can use Snapshots any time that an interactive map isn't required, and in any place you typically use an image URL — in web pages, and in places where JavaScript isn't available, such as email clients.

For interactive web maps, use [MapKit JS](MapKitJS.md). For native map snapshots, see [`MKMapSnapshotter`](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter).

The service requires authentication. The [endpoint's query-parameter reference](https://developer.apple.com/documentation/snapshots/get-a-map-snapshot) documents two alternatives:

- A `token` created for **Web Snapshots** through your developer account's Maps services. See [Creating a Maps token](https://developer.apple.com/documentation/mapkitjs/creating-a-maps-token).
- The per-request signing recipe using `teamId`, `keyId`, and a final `signature` parameter. See [Creating a Maps identifier and a private key](https://developer.apple.com/documentation/applemapsserverapi/creating-a-maps-identifier-and-a-private-key) and the signing guide below.

**Source distinction:** The signing guide and the endpoint's short discussion say every request needs a signature, but the endpoint's detailed parameter definitions explicitly make `token` an alternative to `teamId`/`keyId`/`signature`. Do not combine those authentication forms or treat the signing recipe as the entire current authentication interface.

For per-request signing, URL-encode the query values and sign the exact request path and query string using ES256, then Base64 URL-encode the signature. Preserve parameter order and append `signature` last; changing or reordering signed parameters requires a new signature.

Keep private signing keys on a trusted server, never in client code or source control. Follow token restrictions and revocation guidance for the token workflow. Consult [Maps on the Web](https://developer.apple.com/maps/web/) for current usage limits rather than confusing a per-request image limit with an account's daily quota.

This is a static map-image service, not a `WKWebView` screenshot API or a Safari 27-only capability. Provide a [meaningful text alternative](https://www.w3.org/WAI/tutorials/images/informative/) when the map conveys information.

## Topics

### Essentials
- [Generating a URL and Signature to Create a Maps Web Snapshot](https://developer.apple.com/documentation/snapshots/generating-a-url-and-signature-to-create-a-maps-web-snapshot) - Create a snapshot URL and generate its signature.
- [`Annotation`](https://developer.apple.com/documentation/snapshots/annotation) - Annotation characteristics supplied as part of the request.
- [`Overlay`](https://developer.apple.com/documentation/snapshots/overlay) - Shape points and styling such as line width, color, and dash pattern.
- [`OverlayStyle`](https://developer.apple.com/documentation/snapshots/overlaystyle) - Styles reused across overlays in one request. These describe a rendered image, not live objects that update an already-downloaded snapshot.
- [`Image`](https://developer.apple.com/documentation/snapshots/image) - Custom annotation images in JPEG, PNG, or GIF format. A request supports up to **10 unique images**, which can be reused by annotations; an image that fails to load can fall back to the default balloon marker.

### Snapshots
- [Create a Maps Web Snapshot](https://developer.apple.com/documentation/snapshots/get-a-map-snapshot) - The `GET https://snapshot.apple-mapkit.com/api/v1/snapshot` endpoint. Query parameters select map dimensions, language, color scheme, annotations, and overlays.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/snapshots)*
