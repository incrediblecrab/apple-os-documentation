# PaperKit

Add drawings, shapes, and a consistent markup experience to your app.

**Platforms:** iOS 26.0+ | iPadOS 26.0+ | Mac Catalyst 26.0+ | macOS 26.0+ | visionOS 26.0+

## Overview

PaperKit combines [PencilKit](PencilKit.md) ink with shapes, text boxes, and images in one markup model. Use `PaperMarkupViewController` for the canvas and `PaperMarkup` for saving, loading, and rendering its content. Your app must implement persistence; merely showing the controller doesn't save the model to disk.

Insertion UI is platform-specific: `MarkupEditViewController` on iOS/iPadOS/visionOS, and `MarkupToolbarViewController` on macOS. Both insertion controllers also declare Mac Catalyst 26 support in the structured reference, although the overview's platform prose omits it.

## OS 27 markup model

On iOS/iPadOS/Mac Catalyst/macOS/visionOS 27+, [`Markup`](https://developer.apple.com/documentation/paperkit/markup) describes individual elements, including [`LinkMarkup`](https://developer.apple.com/documentation/paperkit/linkmarkup) for tappable URL links. **Do not implement your own `Markup` conformance**; the protocol is reserved for PaperKit's types. [`MarkupAdornment`](https://developer.apple.com/documentation/paperkit/markupadornment) adds image overlays that can track zoom or retain a fixed size in the base coordinate system. Gate these additions separately from the 26-generation canvas and persistence APIs.

## Topics

### Essentials
- [Integrating PaperKit into your app](https://developer.apple.com/documentation/paperkit/getting-started-with-paperkit) - Set up the canvas, insertion tools, and persistence.

### View controllers
- [PaperMarkupViewController](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller) - Hosts an editable markup canvas.
- [MarkupEditViewController](https://developer.apple.com/documentation/paperkit/markupeditviewcontroller) - Supplies insertion controls on iOS, iPadOS, and visionOS.
- [MarkupToolbarViewController](https://developer.apple.com/documentation/paperkit/markuptoolbarviewcontroller) - Supplies the macOS markup toolbar.

### Configuration
- [FeatureSet](https://developer.apple.com/documentation/paperkit/featureset) - Selects available markup capabilities.
- [ShapeConfiguration](https://developer.apple.com/documentation/paperkit/shapeconfiguration) - Configures a shape's appearance.
- [RenderingOptions](https://developer.apple.com/documentation/paperkit/renderingoptions) - Configures model rendering.

### Data model
- [PaperMarkup](https://developer.apple.com/documentation/paperkit/papermarkup) - Stores canvas content and supports serialized data representations.

### Error handling
- [`MarkupError`](https://developer.apple.com/documentation/paperkit/markuperror) - Encoding and decoding errors for the markup data model.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/PaperKit)*
