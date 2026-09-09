# Link Presentation

Fetch, provide, and present rich links in your app.

**Platforms:** iOS 13.0+ | iPadOS 13.0+ | Mac Catalyst 13.0+ | macOS 10.15+ | tvOS 14.0+ | visionOS 1.0+

## Overview

The Link Presentation framework enables you to present content-rich URLs in a consistent way. Retrieve metadata from a URL, present the rich link content inside your app, and provide link metadata to the share sheet experience in iOS.

For the original presentation and sharing workflow, see [WWDC 2019 session 262: Embedding and Sharing Visually Rich Links](https://developer.apple.com/videos/play/wwdc2019/262/).

## Fetching and compatibility

Create an `LPMetadataProvider` for each request, handle failure/cancellation/timeouts, and tolerate missing metadata fields. Sandboxed macOS clients need the outgoing-network [client entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.network.client) for remote URLs.

Cache fetched metadata rather than refetching every time a link is shown. `LPLinkMetadata` supports `NSSecureCoding`; you can also supply known metadata yourself. Pass metadata to `LPLinkView(metadata:)`; the URL initializer creates a placeholder, not a fully fetched preview.

Check individual availability: the catalog lists tvOS 14, but `LPLinkMetadata` and `LPLinkView` declarations list tvOS 13 while `LPMetadataProvider` requires tvOS 18. The metadata/provider references also list watchOS 9, without a watchOS `LPLinkView`.

[`LinkMetadata`](https://developer.apple.com/documentation/linkpresentation/linkmetadata) is a separate Swift value type available on all seven 26.4-generation platforms. It conforms to `Codable`, `Sendable`, and `Transferable`; it isn't an OS 27-only feature or evidence that older `LPLinkMetadata` is removed.

## Topics

### Link metadata
- [`LPMetadataProvider`](https://developer.apple.com/documentation/linkpresentation/lpmetadataprovider) - Fetches optional rich-link metadata and reports errors.
- [`LPLinkMetadata`](https://developer.apple.com/documentation/linkpresentation/lplinkmetadata) - A metadata object that can be fetched, populated locally, or archived.
- [`LinkMetadata`](https://developer.apple.com/documentation/linkpresentation/linkmetadata) - A codable, sendable Swift metadata structure, 26.4+.

### Rich links
- [`LPLinkView`](https://developer.apple.com/documentation/linkpresentation/lplinkview) - Renders the link's available metadata.

### Reference
- [LinkPresentation Errors](https://developer.apple.com/documentation/linkpresentation/errors)
- [LinkPresentation Macros](https://developer.apple.com/documentation/linkpresentation/macros)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/LinkPresentation)*
