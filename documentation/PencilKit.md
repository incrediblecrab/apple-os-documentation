# PencilKit

Capture touch and Apple Pencil input as a drawing, and display that content from your app.

**Platforms:** iOS 13.0+ | iPadOS 13.0+ | Mac Catalyst 13.0+ | macOS 10.15+ | visionOS 1.0+

## Overview

**PencilKit** makes it easy to incorporate hand-drawn content into your iPadOS or macOS apps. PencilKit provides a drawing environment for your iOS app that receives input from Apple Pencil or the user's finger, and turns it into images you display in iPadOS, iOS, or macOS. The environment comes with tools for creating, erasing, and selecting lines.

You capture content in your iPad app using a **PKCanvasView** object that you integrate into your existing view hierarchy. It supports the low-latency capture of touches originating from Apple Pencil or your finger. The canvas object sends final results as a **PKDrawing** object, whose contents you can save with your app's content. You can also convert the drawn content into an image for display in iOS or macOS app.

For information about handling user interactions on Apple Pencil in your UIKit app, see [Apple Pencil interactions](https://developer.apple.com/documentation/uikit/apple_pencil_interactions).

## Topics

### Canvas
- [Drawing with PencilKit](https://developer.apple.com/documentation/pencilkit/drawing_with_pencilkit) - Add expressive, low-latency drawing to your app using PencilKit.
- [Customizing Scribble with Interactions](https://developer.apple.com/documentation/pencilkit/customizing_scribble_with_interactions) - Enable writing on a non-text-input view by adding interactions.
- [Inspecting, Modifying, and Constructing PencilKit Drawings](https://developer.apple.com/documentation/pencilkit/inspecting_modifying_and_constructing_pencilkit_drawings) - Score users' ability to match PencilKit drawings generated from text, by accessing the strokes and points inside PencilKit drawings.
- **PKCanvasView** - A view that captures Apple Pencil input and displays the rendered results in an iOS app.
- **PKDrawing** - A structure representing the drawing information captured by a canvas view.
- **PKStroke** - A structure that represents the paths, boundaries, and other properties of a stroke drawn on a canvas.
- **PKStrokePath** - A structure that captures the components of a stroke and provides methods to find and interpolate points along the stroke's path.
- **PKStrokePoint** - A structure that represents the properties of a specific point along a stroke's path.
- **PKInk** - A structure that represents an ink that specifies its type, color, and width.

### Tools
- [Configuring the PencilKit tool picker](https://developer.apple.com/documentation/pencilkit/configuring_the_pencilkit_tool_picker) - Incorporate a custom PencilKit tool picker with a variety of system and custom tools into a drawing app.
- **PKToolPicker** - A tool palette that displays a selection of drawing tools and colors for tools that a person can choose from.
- **PKInkingTool** - A structure that defines the drawing characteristics (width, color, pen style) to use when drawing lines on a canvas view.
- **PKEraserTool** - A tool for erasing previously drawn content in a canvas view.
- **PKLassoTool** - A tool for selecting stroked lines and shapes in a canvas view.
- **PKTool** - An interface adopted by drawing and writing tools used by a canvas view.

### Backward compatibility
- [Supporting backward compatibility for ink types](https://developer.apple.com/documentation/pencilkit/supporting_backward_compatibility_for_ink_types) - Leverage the latest PencilKit features while providing a good user experience in earlier versions of the OS that don't support those features.
- **PKContentVersion** - Constants that represent versions of PencilKit for backward compatibility.

### Classes
- **PKResponderState** - The state of PencilKit behavior related to a UIResponder. (Beta)

### Enumerations
- **PKToolPickerVisibility** - The visibility state of a tool picker. (Beta)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/PencilKit)*