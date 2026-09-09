# PDFKit

Display and manipulate PDF documents in your apps.

**Platforms:** iOS 11.0+ | iPadOS 11.0+ | Mac Catalyst 13.1+ | macOS 10.4+ | visionOS 1.0+

## Overview

Use `PDFDocument` as the document model and `PDFView` for embedded display, navigation, selection, and zooming. Annotations represent PDF content such as links, form fields, and notes; page overlay views are a separate UI customization mechanism.

The framework catalog labels Mac Catalyst as 11.0, but the concrete `PDFView`, `PDFDocument`, and annotation declarations specify 13.1. The header follows those usable declarations. `PDFThumbnailView` starts at macOS 10.5, and page overlays require newer systems as noted below.

## Topics

### Views
- [`PDFView`](https://developer.apple.com/documentation/pdfkit/pdfview) - An embeddable PDF viewer with navigation, selection, zoom, and page-history support.
- [`PDFThumbnailView`](https://developer.apple.com/documentation/pdfkit/pdfthumbnailview) - Displays thumbnails representing document pages.

### Content Model
- [`PDFDocument`](https://developer.apple.com/documentation/pdfkit/pdfdocument) - Loads PDF data or a file URL and manages pages, searches, and document output.
- [`PDFPage`](https://developer.apple.com/documentation/pdfkit/pdfpage) - Renders an individual page and provides access to its annotations, text, and selections.
- [`PDFOutline`](https://developer.apple.com/documentation/pdfkit/pdfoutline) - Represents an optional navigation hierarchy; its root is a container rather than a visible outline item.
- [`PDFSelection`](https://developer.apple.com/documentation/pdfkit/pdfselection) - Identifies contiguous or noncontiguous document text.

### Annotations
- [Adding Widgets to a PDF Document](https://developer.apple.com/documentation/pdfkit/adding-widgets-to-a-pdf-document) - Add text, button, and choice form fields, not WidgetKit widgets.
- [Adding Custom Graphics to a PDF](https://developer.apple.com/documentation/pdfkit/adding-custom-graphics-to-a-pdf) - Create custom annotation and page graphics.
- [Custom Graphics](https://developer.apple.com/documentation/pdfkit/custom-graphics) - Demonstrates adding a watermark to a PDF page.
- [PDF Widgets](https://developer.apple.com/documentation/pdfkit/pdf-widgets) - Demonstrates interactive PDF form elements.
- [`PDFAnnotation`](https://developer.apple.com/documentation/pdfkit/pdfannotation) - A page-positioned annotation that may support interaction.

### Protocols
- [`PDFPageOverlayViewProvider`](https://developer.apple.com/documentation/pdfkit/pdfpageoverlayviewprovider) - Supplies page overlay views and receives their display-lifecycle callbacks; iOS/iPadOS/Mac Catalyst 16+, macOS 13+, and visionOS 1+.

### Reference
- [PDFKit Enumerations](https://developer.apple.com/documentation/pdfkit/enumerations)
- [PDFKit Constants](https://developer.apple.com/documentation/pdfkit/constants)
- [PDFKit Data Types](https://developer.apple.com/documentation/pdfkit/data-types)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/PDFKit)*
