# Maps Web Snapshots

Create a static image of a map from a URL.

**Platforms:** Maps Web Snapshots 1.0+ (Beta)

## Overview

Use the Maps Web Snapshots service to generate static map images from a URL. You can use Snapshots any time that an interactive map isn't required, and in any place you typically use an image URL — in web pages, and in places where JavaScript isn't available, such as email clients.

**Note:** If you need an interactive map on the web, see MapKit JS. To generate static map snapshots in iOS, macOS, or tvOS apps, see MKMapSnapshotter.

To learn how to construct a signed and validated snapshot URL, see Generating a URL and Signature to Create a Maps Web Snapshot. You generate the required signature using credentials obtained through your Apple Developer account. See Creating a Maps identifier and a private key to learn how to get these credentials. You can also obtain HTML to show information about a place using Create a Map.

For more information on usage limits for Maps Web Snapshots, see the Apple Developer page, Maps on the Web.

> **Beta Software**
> 
> This documentation contains preliminary information about an API or technology in development. This information is subject to change, and software implemented according to this documentation should be tested with final operating system software.

## Topics

### Essentials
- [Generating a URL and Signature to Create a Maps Web Snapshot](https://developer.apple.com/documentation/snapshots/generating_a_url_and_signature_to_create_a_maps_web_snapshot) - Create a Snapshot URL and generate a signature to validate the request.
- **Annotation** - An object for a Snapshot URL that describes annotation characteristics.
- **Overlay** - A JSON object for a Snapshot URL that describes overlay shape characteristics, including points for the overlay and styles such as width, color, and dash pattern.
- **OverlayStyle** - A JSON object that describes reusable styles for an overlay.
- **Image** - A JSON object for a Snapshot URL that describes the characteristics of custom images to use for map annotations.

### Snapshots
- [Create a Maps Web Snapshot](https://developer.apple.com/documentation/snapshots/create_a_maps_web_snapshot) - Generates a map image with characteristics that you provide in the query parameters.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/snapshots)*