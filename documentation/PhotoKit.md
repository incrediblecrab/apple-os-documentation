# PhotoKit

Work with image and video assets that the Photos app manages, including those from iCloud Photos and Live Photos.

**Platforms:** iOS 8.0+ | iPadOS 8.0+ | Mac Catalyst 13.1+ | macOS 10.11+ | tvOS 10.0+ | visionOS 1.0+ | watchOS 10.0+

## Overview

PhotoKit is the combination of the Photos and PhotosUI frameworks, which together enable you to access image and video assets that the Photos app manages. You might use PhotoKit to edit or display a person's photos, or to manage collections of assets such as albums, Moments, and Shared Albums. The framework provides access to photos on the person's device and in iCloud.

## OS 27 asset metadata

The September 8, 2026 review of the [iOS and iPadOS](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes#PhotoKit), [macOS](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes#PhotoKit), and [visionOS](https://developer.apple.com/documentation/visionos-release-notes/visionos-27-release-notes#PhotoKit) Beta 8 notes identifies two developer-facing changes:

- Use the new optional [PHAssetResource.filename](https://developer.apple.com/documentation/photos/phassetresource/filename) on its supported OS 27 platforms. It replaces the misleadingly non-null `originalFilename` contract (175412725). A missing filename is valid; do not force-unwrap it or require every resource to supply a display name.
- The `PHAsset.addedDate` issue that could return `nil` despite a non-null declaration is listed as **resolved** (175050631), not a current blanket limitation.

These API changes do not imply unrestricted library access. Retain the Photos picker and authorization guidance below, and request only the access the feature needs. Consumer Photos editing features are not a specification for PhotoKit transformations, export limits, or watermark metadata.

## Topics

### Frameworks
Reference the API that compose PhotoKit.

- [Photos](https://developer.apple.com/documentation/photos) - Work with image and video assets that the Photos app manages, including those from iCloud Photos and Live Photos.
- [PhotosUI](https://developer.apple.com/documentation/photosui) - Present a person's photo library using a picker interface, display Live Photos, or extend the Photos app with custom functionality.

### Sample code
Browse sample code that walk through specific Photos and PhotosUI workflows.

- [Browsing and Modifying Photo Albums](https://developer.apple.com/documentation/photokit/browsing-and-modifying-photo-albums) - Help users organize their photos into albums and browse photo collections in a grid-based layout using PhotoKit.
- [Selecting Photos and Videos in iOS](https://developer.apple.com/documentation/photokit/selecting-photos-and-videos-in-ios) - Improve the user experience of finding and selecting assets by using the Photos picker.
- [Bringing Photos picker to your SwiftUI app](https://developer.apple.com/documentation/photokit/bringing-photos-picker-to-your-swiftui-app) - Select media assets by using a Photos picker view that SwiftUI provides.
- [Implementing an inline Photos picker](https://developer.apple.com/documentation/photokit/implementing-an-inline-photos-picker) - Embed a system-provided, half-height Photos picker into your app's view.
- [Creating a Slideshow Project Extension for Photos](https://developer.apple.com/documentation/photokit/creating-a-slideshow-project-extension-for-photos) - Augment the macOS Photos app with extensions that support project creation.

### Articles
Browse articles that cover high-level Photos and PhotosUI tasks.

- [Delivering an Enhanced Privacy Experience in Your Photos App](https://developer.apple.com/documentation/photokit/delivering-an-enhanced-privacy-experience-in-your-photos-app) - Adopt the latest privacy enhancements to deliver advanced user-privacy controls.
- [Fetching Objects and Requesting Changes](https://developer.apple.com/documentation/photokit/fetching-objects-and-requesting-changes) - Get assets, asset collections, and collection lists matching a specified query.
- [Loading and Caching Assets and Thumbnails](https://developer.apple.com/documentation/photokit/loading-and-caching-assets-and-thumbnails) - Request image, video, or Live Photos content, and cache for quick reuse.
- [Displaying Live Photos](https://developer.apple.com/documentation/photokit/displaying-live-photos) - Provide the same interactive playback of Live Photos as in the iOS Photos app.
- [Creating Photo Editing Extensions](https://developer.apple.com/documentation/photokit/creating-photo-editing-extensions) - Provide custom functionality in the Photos app by bundling an app extension.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/PhotoKit)*
