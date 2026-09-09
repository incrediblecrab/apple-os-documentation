# Quick Look UI

Create previews of files to use inside your macOS app.

**Platforms:** macOS (core preview views 10.6+; current framework catalog and data-based extensions 12.0+)

## Overview

Use `QLPreviewPanel` for the app's shared preview panel or `QLPreviewView` for an embedded preview. The panel follows the responder chain to find a controller that supplies its data. You can't subclass the panel; customize it through its delegate. Supported formats can vary by OS release, and commonly include:

- iWork and Microsoft Office documents
- Images
- Live Photos
- Text files
- PDFs
- Audio and video files

You can provide previews for your own data types by either rendering a view with your own view controller or by returning a supported preview format such as PDF or HTML.

### Providing Quick Look Previews for your Data Types

To provide Quick Look previews for your own file types, create a Quick Look Preview Extension with either a view controller or data based preview. In either case, add your supported content types to the **QLSupportedContentTypes** array in the Info.plist file of the extension.

For a view-based extension, use an `NSViewController` conforming to `QLPreviewingController` and implement `preparePreviewOfFile(at:completionHandler:)` for file URLs. The system invokes it once on the main thread before presentation. Avoid blocking that thread, call the completion handler when ready, and don't keep a file descriptor open for the entire preview.

For a data-based extension, subclass `QLPreviewProvider`, conform to `QLPreviewingController`, and implement `providePreview(for:completionHandler:)`. Return a `QLPreviewReply` for the system's `QLFilePreviewRequest`. Configure `QLIsDataBasedPreview`, `QLSupportedContentTypes`, and `NSExtensionPrincipalClass` in the extension's property list.

### Availability distinctions

`QLPreviewPanel`, `QLPreviewView`, and the macOS `QLPreviewItem` protocol declare macOS 10.6, earlier than the framework catalog's 12.0 label. The data-based provider/request/reply types require macOS 12. The current `QLPreviewingController` protocol reference lists 12.0 while its file-preparation method lists 10.10; don't treat the aggregate label as the historical introduction of every preview API.

The similarly named iOS-family types are documented under [Quick Look](QuickLook.md). A native AppKit preview view isn't a drop-in UIKit view.

## Topics

### Previews
- [`QLPreviewPanel`](https://developer.apple.com/documentation/quicklookui/qlpreviewpanel) - The app's shared preview panel.
- [`QLPreviewView`](https://developer.apple.com/documentation/quicklookui/qlpreviewview) - An embeddable preview view.
- [`QLPreviewItem`](https://developer.apple.com/documentation/quicklookui/qlpreviewitem) - Supplies the preview URL and optional title; `NSURL` can serve directly as an item.
- [`QLPreviewPanelDataSource`](https://developer.apple.com/documentation/quicklookui/qlpreviewpaneldatasource) - Supplies the panel's items; its current reference lists macOS 12.
- [`QLPreviewPanelDelegate`](https://developer.apple.com/documentation/quicklookui/qlpreviewpaneldelegate) - Customizes panel behavior; its current reference lists macOS 12.
- [`QLPreviewItemLoadingBlock`](https://developer.apple.com/documentation/quicklookui/qlpreviewitemloadingblock) - An error-completion block alias introduced in macOS 10.13 and deprecated in 10.14. Deprecation isn't a claim that the type was removed.

### Preview Extensions
- [`QLPreviewingController`](https://developer.apple.com/documentation/quicklookui/qlpreviewingcontroller) - Provides file/searchable-item preparation or a data-based reply.

### Data-based Preview Extensions
- [`QLPreviewProvider`](https://developer.apple.com/documentation/quicklookui/qlpreviewprovider) - The principal class to subclass for a data-based extension.
- [`QLFilePreviewRequest`](https://developer.apple.com/documentation/quicklookui/qlfilepreviewrequest) - Describes the content to preview.
- [`QLPreviewReply`](https://developer.apple.com/documentation/quicklookui/qlpreviewreply) - Supplies preview data, such as an image, PDF, or HTML.
- [`QLPreviewReplyAttachment`](https://developer.apple.com/documentation/quicklookui/qlpreviewreplyattachment) - Supplies HTML resources referenced through `cid:` identifiers.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/QuickLookUI)*
