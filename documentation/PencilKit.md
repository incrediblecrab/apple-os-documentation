# PencilKit

Capture touch and Apple Pencil input as a drawing, and display that content from your app.

**Platforms:** iOS 13.0+ | iPadOS 13.0+ | Mac Catalyst 13.0+ | macOS 10.15+ | visionOS 1.0+

## Overview

PencilKit provides drawing capture, stroke data, and tools for inking, erasure, and selection. `PKCanvasView` receives supported Apple Pencil or touch input; `PKDrawing` stores the result and can produce an image for display or sharing.

The framework's macOS availability doesn't make every UIKit-based view available natively on macOS. `PKCanvasView` and `PKToolPicker` declare iOS/iPadOS 13, Mac Catalyst 13.1, and visionOS 1, without a native macOS declaration. The tool picker's documentation additionally says its palette doesn't display in Mac Catalyst apps. Drawing models and tool values have separate macOS availability.

For hardware-dependent interactions in UIKit, see [Apple Pencil interactions](https://developer.apple.com/documentation/uikit/apple-pencil-interactions) and [Apple Pencil](ApplePencil.md).

## OS 27 drawing APIs

The [June 2026 PencilKit update](https://developer.apple.com/documentation/updates/pencilkit) introduces stroke/path identifiers, programmatic selection, path-based erasure, and handwriting recognition:

- [`PKStroke.id`](https://developer.apple.com/documentation/pencilkit/pkstroke-swift.struct/id) and [`PKStrokePath.id`](https://developer.apple.com/documentation/pencilkit/pkstrokepath-swift.struct/id) expose UUID identity on the five 27-generation platforms in this page's header. Stroke IDs are writable; path IDs are read-only. Reusing a path ID for different control points produces undefined rendering behavior.
- [`PKCanvasView.selection`](https://developer.apple.com/documentation/pencilkit/pkcanvasview/selection) is a set of stroke UUIDs; use [`canvasViewSelectionDidChange(_:)`](https://developer.apple.com/documentation/pencilkit/pkcanvasviewdelegate/canvasviewselectiondidchange(_:)) for selection notifications. The selection property requires iOS/iPadOS/Mac Catalyst/visionOS 27, not macOS; the callback reference retains older availability labels.
- [`PKDrawing.erasePath(_:mask:transform:)`](https://developer.apple.com/documentation/pencilkit/pkdrawing-swift.struct/erasepath(_:mask:transform:)-shn) mutates the drawing along a path; [`erasingPath`](https://developer.apple.com/documentation/pencilkit/pkdrawing-swift.struct/erasingpath(_:mask:transform:)-9dpi9) returns an edited copy. These overloads take an optional `UIBezierPath` mask on iOS/iPadOS/Mac Catalyst/visionOS 27. The [macOS 27 overload](https://developer.apple.com/documentation/pencilkit/pkdrawing-swift.struct/erasepath(_:mask:transform:)-2b2u3) uses `NSBezierPath` instead.
- [`PKStrokeRecognizer`](https://developer.apple.com/documentation/pencilkit/pkstrokerecognizer) is an actor for asynchronous, on-device handwriting recognition and search on iOS/iPadOS/Mac Catalyst/macOS/visionOS 27+. Check `supportedLanguages`; retain `recognitionVersion` with cached results so they can be refreshed when recognition changes.
- The [27 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes) rename `__PKStrokeRenderState` to [`PKStrokeRenderStateReference`](https://developer.apple.com/documentation/pencilkit/pkstrokerenderstatereference), with its initializer replacing `PKStrokeRenderState.asObjCRenderState()`. Update earlier-beta call sites; this is not a reason to raise the framework's existing minimum deployment target.

Keep using `PKContentVersion` and the [ink compatibility guidance](https://developer.apple.com/documentation/pencilkit/supporting-backward-compatibility-for-ink-types) when sharing drawings with older systems. Unsupported inks can make drawing data fail to load; supply a compatible fallback or restrict the available tools rather than assuming all serialized drawings are backward compatible.

### Earlier API generations

`PKDrawing` starts at iOS/iPadOS/Mac Catalyst 13 and macOS 10.15. The Swift `PKStroke`, `PKStrokePath`, `PKStrokePoint`, and `PKInk` structures start at iOS/iPadOS/Mac Catalyst 14 and macOS 11. The inking, eraser, and lasso tool values and `PKTool` start at iOS/iPadOS/Mac Catalyst 13 and macOS 11. These model/tool declarations include visionOS 1.

`PKContentVersion` requires iOS/iPadOS/Mac Catalyst 17, macOS 14, or visionOS 1. `PKResponderState` and `PKToolPickerVisibility` require iOS/iPadOS/Mac Catalyst/visionOS 26, not 27, and have no native macOS declaration.

## Topics

### Canvas
- [Drawing with PencilKit](https://developer.apple.com/documentation/pencilkit/drawing-with-pencilkit) - Add a drawing canvas and tools.
- [Customizing Scribble with Interactions](https://developer.apple.com/documentation/pencilkit/customizing-scribble-with-interactions) - Enable writing on a non-text-input view by adding interactions.
- [Inspecting, Modifying, and Constructing PencilKit Drawings](https://developer.apple.com/documentation/pencilkit/inspecting-modifying-and-constructing-pencilkit-drawings) - Compare user drawings with generated text outlines through stroke and point inspection.
- [`PKCanvasView`](https://developer.apple.com/documentation/pencilkit/pkcanvasview) - Captures input and renders the current drawing.
- [`PKDrawing`](https://developer.apple.com/documentation/pencilkit/pkdrawing-swift.struct) - Stores, serializes, and renders drawing content.
- [`PKStroke`](https://developer.apple.com/documentation/pencilkit/pkstroke-swift.struct) - Describes a stroke's path, boundaries, and related properties.
- [`PKStrokePath`](https://developer.apple.com/documentation/pencilkit/pkstrokepath-swift.struct) - Provides control points and path interpolation.
- [`PKStrokePoint`](https://developer.apple.com/documentation/pencilkit/pkstrokepoint-swift.struct) - Describes a point along a stroke.
- [`PKInk`](https://developer.apple.com/documentation/pencilkit/pkink-swift.struct) - Specifies ink type and color; `PKInkingTool` configures the base drawing width.

### Tools
- [Configuring the PencilKit tool picker](https://developer.apple.com/documentation/pencilkit/configuring-the-pencilkit-tool-picker) - Configure system and custom picker items.
- [`PKToolPicker`](https://developer.apple.com/documentation/pencilkit/pktoolpicker) - Manages the palette and notifies registered observers when the selected tool changes.
- [`PKInkingTool`](https://developer.apple.com/documentation/pencilkit/pkinkingtool-swift.struct) - Sets ink type, color, and base width for subsequent drawing; changing it doesn't restyle existing strokes.
- [`PKEraserTool`](https://developer.apple.com/documentation/pencilkit/pkerasertool-swift.struct) - Erases whole items or portions, depending on the eraser type.
- [`PKLassoTool`](https://developer.apple.com/documentation/pencilkit/pklassotool-swift.struct) - Selects drawn content.
- [`PKTool`](https://developer.apple.com/documentation/pencilkit/pktool-swift.protocol) - The protocol adopted by PencilKit's tools. Don't create your own conforming types; custom picker items use their separate API.

### Backward compatibility
- [Supporting backward compatibility for ink types](https://developer.apple.com/documentation/pencilkit/supporting-backward-compatibility-for-ink-types) - Check required content versions and choose fallback or restricted-ink strategies.
- [`PKContentVersion`](https://developer.apple.com/documentation/pencilkit/pkcontentversion) - Identifies drawing-format capabilities, not the framework's minimum OS version.

### Classes
- [`PKResponderState`](https://developer.apple.com/documentation/pencilkit/pkresponderstate) - Controls a responder's active picker and visibility behavior.

### Enumerations
- [`PKToolPickerVisibility`](https://developer.apple.com/documentation/pencilkit/pktoolpickervisibility) - Specifies picker visibility, including inheritance through the responder chain.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/PencilKit)*
