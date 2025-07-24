# Quick Look UI

Create previews of files to use inside your macOS app.

**Platforms:** macOS 12.0+

## Overview

When showing files in your app, including the ability to quickly preview a file and its content can be helpful to your users. For example, you may want to allow users to zoom into a photo, play back an audio file, and so on. Use the **Quick Look** framework to show a preview of common file types in your macOS app that allow basic interactions. Quick Look can generate previews for common file types, including:

- iWork and Microsoft Office documents
- Images
- Live Photos
- Text files
- PDFs
- Audio and video files

You can provide previews for your own data types by either rendering a view with your own view controller or by returning a supported preview format such as PDF or HTML.

### Providing Quick Look Previews for your Data Types

To provide Quick Look previews for your own file types, create a Quick Look Preview Extension with either a view controller or data based preview. In either case, add your supported content types to the **QLSupportedContentTypes** array in the Info.plist file of the extension.

To provide a view controller based preview extension, set up an **NSViewController** that conforms to **QLPreviewingController**. Prepare and display the view within the method **preparePreviewOfFile(at:completionHandler:)**.

To provide a data-based preview extension, implement a subclass of **QLPreviewProvider** to provide a **QLPreviewReply** based on the **QLFilePreviewRequest** that the system provides.

## Topics

### Previews
- **QLPreviewPanel** - A class that implements the Quick Look preview panel to display a preview of a list of items.
- **QLPreviewView** - A Quick Look preview of an item that you can embed into your view hierarchy.
- **QLPreviewItem** - A protocol that defines a set of properties you implement to make a preview of your application's content.
- **QLPreviewPanelDataSource** - A protocol that the Quick Look preview panel uses to access the contents of its data source object.
- **QLPreviewPanelDelegate** - A protocol for the delegate of the Quick Look preview panel.
- **QLPreviewItemLoadingBlock** - A type that defines a block used to load a Quick Look preview item.

### Deprecated
Preview Extensions

### Preview Extensions
- **QLPreviewingController** - A protocol for implementing a custom controller to create previews of files.

### Data-based Preview Extensions
- **QLPreviewProvider** - A class that you subclass to provide a data-based Quick Look preview extension.
- **QLFilePreviewRequest** - A Quick Look preview request that indicates the content to preview.
- **QLPreviewReply** - The class you create when providing a data-based Quick Look preview extension.
- **QLPreviewReplyAttachment** - An attachment for a Quick Look preview reply that provides additional content for the system to display a preview.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/QuickLookUI)*