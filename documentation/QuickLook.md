# Quick Look

Create previews of files to use inside your app, or perform simple edits on previews.

**Platforms:** iOS 4.0+ | iPadOS 4.0+ | Mac Catalyst 13.0+ | macOS 10.5+ | visionOS 1.0+

## Overview

Quick Look provides system-managed file previews with basic interaction. Supply items through a preview controller's data source and [check whether an item can be displayed](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller/canpreview(_:)) before presenting it. Common supported formats include:

- iWork and Microsoft Office documents
- Images
- Live Photos
- Text files
- PDFs
- Audio and video files
- USDZ 3D models, with AR or spatial presentation depending on the platform and API

Previews are read-only by default. On supported systems, the [editing delegate callback](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdelegate/previewcontroller(_:editingmodefor:)) can enable supported edits and choose whether to update the original or create a copy. Implement the corresponding save callbacks. This API starts at iOS/iPadOS 13, Mac Catalyst 13.1, and visionOS 1; it doesn't turn Quick Look into a general-purpose editor.

Use lower-level APIs for custom editing, playback, or compositing rather than changing the preview controller's private view hierarchy. In Mac Catalyst, presenting `QLPreviewController` opens a panel while the original window remains visible; embedding the controller produces a thumbnail rather than a live preview.

You can provide previews for your own data types by either rendering a view with your own view controller or by returning a supported preview format, such as PDF or HTML.

**Note:** The list of supported common file types may change between operating system releases.

### Providing Quick Look previews for your data types

To provide Quick Look previews for your own file types, create a Quick Look preview extension with either a view controller or data-based preview. In either case, add your supported content types to the **QLSupportedContentTypes** array in the Info.plist file of the extension.

For a view-based extension, use a `UIViewController` conforming to `QLPreviewingController` and implement `preparePreviewOfFile(at:completionHandler:)` for file URLs. The callback runs on the main thread; move expensive work off that thread and call its completion handler when the preview is ready. Avoid holding the file open for the preview's entire lifetime.

For a data-based extension, subclass `QLPreviewProvider`, conform to `QLPreviewingController`, and return a `QLPreviewReply` from `providePreview(for:completionHandler:)` for the system's `QLFilePreviewRequest`. Set `QLIsDataBasedPreview` to true and configure the extension's supported content types and principal class.

### Availability and hosting

The data-based provider/request/reply types require iOS/iPadOS/Mac Catalyst 15 or visionOS 1. The framework's older minimum isn't the availability of every extension API. `QLPreviewController` itself lists Mac Catalyst 13.1, whereas the framework catalog lists 13.0.

For native macOS UI, use [Quick Look UI](QuickLookUI.md). `PreviewApplication`, `PreviewItem`, `PreviewSession`, and the `EditingMode` alias belong to the visionOS 2+ preview-application workflow; they aren't general iOS 4 APIs. `QLPreviewSceneActivationConfiguration` is a different, iOS/iPadOS/Mac Catalyst 15+ scene configuration.

## Topics

### Previews
- [`QLPreviewController`](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller) - Presents preview items provided by its data source.
- [`QLPreviewItem`](https://developer.apple.com/documentation/quicklook/qlpreviewitem) - Supplies item information to the preview controller.
- [`QLPreviewSceneActivationConfiguration`](https://developer.apple.com/documentation/quicklook/qlpreviewsceneactivationconfiguration) - Configures a prominent, detachable preview scene for a gesture or menu action.

### Previews or thumbnail images for macOS 10.14 or earlier
The [historical generator APIs](https://developer.apple.com/documentation/quicklook/previews-or-thumbnail-images-for-macos-10-14-or-earlier) target older macOS releases. For macOS 10.15+, use [QuickLookThumbnailing](QuickLookThumbnailing.md) for thumbnails and preview extensions for previews instead of adopting generators.

### Preview extensions
- [`QLPreviewingController`](https://developer.apple.com/documentation/quicklook/qlpreviewingcontroller) - Implements view-based file/searchable-item preparation or data-based preview generation.

### Data-based preview extensions
- [`QLPreviewProvider`](https://developer.apple.com/documentation/quicklook/qlpreviewprovider) - The principal class to subclass for a data-based extension.
- [`QLFilePreviewRequest`](https://developer.apple.com/documentation/quicklook/qlfilepreviewrequest) - Describes the content the system wants to preview.
- [`QLPreviewReply`](https://developer.apple.com/documentation/quicklook/qlpreviewreply) - Supplies a supported preview representation.
- [`QLPreviewReplyAttachment`](https://developer.apple.com/documentation/quicklook/qlpreviewreplyattachment) - Supplies linked content for an HTML preview.

### Classes
- [`ARQuickLookPreviewItem`](https://developer.apple.com/documentation/quicklook/arquicklookpreviewitem) - A preview item for AR Quick Look; iOS/iPadOS 13, Mac Catalyst 13.1, and visionOS 1.
- [`PreviewApplication`](https://developer.apple.com/documentation/quicklook/previewapplication) - Opens the visionOS 2+ Quick Look application.

### Structures
- [`PreviewItem`](https://developer.apple.com/documentation/quicklook/previewitem) - A value describing an item for the visionOS preview application.
- [`PreviewSession`](https://developer.apple.com/documentation/quicklook/previewsession) - Provides session events and closing control on visionOS.

### Type Aliases
- [`EditingMode`](https://developer.apple.com/documentation/quicklook/editingmode) - The visionOS 2+ alias for `QLPreviewItemEditingMode`.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/QuickLook)*
