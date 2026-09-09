# Apple Pencil

Enhance your iPad app's user experience by supporting drawing, handwriting, and other features of Apple Pencil.

## Overview

Apple Pencil is an input accessory for iPad that people rely on for tasks like drawing, sketching, painting, jotting notes, marking up documents, and more. In addition to drawing and handwriting, Apple Pencil can also serve as a pointer and UI interaction tool.

Choose the Pencil features that fit your iPad app and adopt them through [PencilKit](PencilKit.md), [SwiftUI](SwiftUI.md), and [UIKit](UIKit.md). Apple Pencil is a technology collection, not a separate framework to import. Hardware capabilities depend on both the Pencil model and compatible iPad.

### Drawing

Use PencilKit for a drawing canvas and tools, or UIKit touch data for your own renderer. Available touch information includes position, azimuth, altitude, roll, and force, but not every Pencil model provides every measurement. For example, [`rollAngle`](https://developer.apple.com/documentation/uikit/uitouch/rollangle) returns `0` for a model without barrel-roll support. Force can initially be estimated; process expected updates when your renderer needs them.

### Handwriting

Scribble converts handwriting into typed text in supported editable text views. It is enabled by default for supported languages, but people can change the setting and apps can customize or suppress it. [`UIScribbleInteraction`](https://developer.apple.com/documentation/uikit/uiscribbleinteraction) works with editable `UITextInput` views; indirect Scribble interactions extend text entry to other custom views.

### Double tap and squeeze

Supported Pencil models can report double taps; squeeze is an Apple Pencil Pro feature. Read and respect the person's preferred action when using SwiftUI or UIKit interaction APIs, rather than assuming every gesture means “switch tool.”

### Haptics

Apple Pencil Pro can provide haptic feedback, for example when an object snaps to a guide. Request feedback through SwiftUI sensory-feedback APIs or UIKit feedback generators. The system decides whether to play it based on hardware, settings, and app state; a request isn't a playback guarantee.

### Hover

When a person holds a supported model of Apple Pencil close above the screen without touching it, the pencil can provide information about the distance of the tip from the screen. You can use this hover distance to create more expressive drawing and input experiences with Apple Pencil. You get this information using hover gestures in UIKit.

### Pointers

On compatible hardware, Pencil hover can provide pointer-style feedback over a view. Use SwiftUI hover events or UIKit pointer interactions for appropriate visual affordances.

For the hardware combinations and feature differences, see Apple's [Apple Pencil comparison](https://www.apple.com/apple-pencil/). An API's availability alone doesn't establish hardware support.

## Topics

### Essentials
- [Apple Pencil updates](https://developer.apple.com/documentation/updates/applepencil) - Learn about important changes to Apple Pencil.

### Drawing
- [Drawing with PencilKit](https://developer.apple.com/documentation/pencilkit/drawing-with-pencilkit) - Add drawing with PencilKit.
- [Inspecting, Modifying, and Constructing PencilKit Drawings](https://developer.apple.com/documentation/pencilkit/inspecting-modifying-and-constructing-pencilkit-drawings) - A sample comparing user drawings with text-derived drawings through stroke and point data.
- [Getting high-fidelity input with coalesced touches](https://developer.apple.com/documentation/uikit/getting-high-fidelity-input-with-coalesced-touches) - Process additional touch samples.
- [Implementing coalesced touch support in an app](https://developer.apple.com/documentation/uikit/implementing-coalesced-touch-support-in-an-app) - A coalesced-touch example.

### Handwriting
- [Customizing Scribble with Interactions](https://developer.apple.com/documentation/pencilkit/customizing-scribble-with-interactions) - Enable writing on a non-text-input view by adding interactions.
- [Handwriting recognition](https://developer.apple.com/documentation/uikit/handwriting-recognition) - Text-input and indirect Scribble interfaces.

### Double tap and squeeze
- [Apple Pencil interactions](https://developer.apple.com/documentation/uikit/apple-pencil-interactions) - UIKit gesture-interaction APIs.
- [Handling squeezes from Apple Pencil](https://developer.apple.com/documentation/applepencil/handling-squeezes-from-apple-pencil) - Handle Apple Pencil Pro squeezes.
- [Handling double taps from Apple Pencil](https://developer.apple.com/documentation/applepencil/handling-double-taps-from-apple-pencil) - Handle double taps on supported models.

### Haptics
- [Playing haptic feedback in your app](https://developer.apple.com/documentation/applepencil/playing-haptic-feedback-in-your-app) - Choose and request feedback for meaningful interactions.

### Hover
- [Adopting hover support for Apple Pencil](https://developer.apple.com/documentation/uikit/adopting-hover-support-for-apple-pencil) - A hover-preview sample with specific hardware requirements.

### Pointers
- [Input events](https://developer.apple.com/documentation/swiftui/input-events) - SwiftUI input and hover-event APIs.
- [Pointer interactions](https://developer.apple.com/documentation/uikit/pointer-interactions) - UIKit pointer feedback for custom views.
- [Integrating pointer interactions into your iPad app](https://developer.apple.com/documentation/uikit/integrating-pointer-interactions-into-your-ipad-app) - Add pointer affordances to iPad views.

### Design
- [Apple Pencil and Scribble](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble) - Drawing, handwriting, and interaction design.
- [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/playing-haptics) - Feedback design guidance.

### Related videos
- [Introducing PencilKit](https://developer.apple.com/videos/play/wwdc2019/221/)
- [What's new in PencilKit](https://developer.apple.com/videos/play/wwdc2020/10107/)
- [Meet Scribble for iPad](https://developer.apple.com/videos/play/wwdc2020/10106/)
- [Inspect, modify, and construct PencilKit drawings](https://developer.apple.com/videos/play/wwdc2020/10148/)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ApplePencil)*
