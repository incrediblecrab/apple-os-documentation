# Pointing Devices

People can use a pointing device like a trackpad or mouse to navigate the interface and initiate actions.

**Platforms:** iOS | iPadOS | macOS | visionOS

## Overview

People appreciate the precision and flexibility that pointing devices offer. On a Mac, people typically expect to combine a pointing device with a keyboard as they navigate apps and the system. On iPad and Apple Vision Pro, a pointing device gives people an additional way to interact with apps and content, without replacing touch, eyes, or gestures.

## Topics

### Best Practices

- **Be consistent when responding to mouse and trackpad gestures** - People expect most gestures to work the same throughout the system, regardless of the app or game they're using. On a Mac, for example, people rely on the "Swipe between pages" gesture to behave the same way whether they're browsing individual document pages, webpages, or images.
- **Avoid redefining systemwide trackpad gestures** - Even in a game that uses app-specific gestures in a custom way, people expect systemwide gestures to be available; for example, people expect to make familiar gestures to reveal the Dock or Mission Control in macOS. Remember that Mac users can customize the gestures for performing systemwide actions.
- **Provide a consistent experience in your app, whether people are using gestures, eyes, a pointing device, or a keyboard** - People expect to move fluidly between multiple types of input, and they don't want to learn different interactions for each mode or for each app they use.
- **Let people use the pointer to reveal and hide controls that automatically minimize or fade out** - In iPadOS, for example, people can reveal the minimized Safari toolbar by holding the pointer over it (the toolbar minimizes again when the pointer moves away). People can also move the pointer to reveal or hide playback controls while they watch a full-screen video.
- **Provide a consistent experience when people press and hold a modifier key while interacting with objects in your app** - For example, if people can duplicate an object by pressing and holding the Option key while they drag that object, ensure the result is the same whether they drag using touch or the pointer.

### Platform Considerations

**iPadOS**  
iPadOS builds on the traditional pointer experience, automatically adapting the pointer to the current context and providing rich visual feedback at a level of precision that enhances productivity and simplifies common tasks on a touchscreen device. The iPadOS pointing system gives people an additional way to interact with apps and content — it doesn't replace touch.

- **Allow multiple selection in custom views when necessary** - In iPadOS 15 and later, people can click and drag the pointer over multiple items to select them. As people use the pointer in this way, it expands into a visible rectangle that selects the items it encompasses. Standard nonlist collection views support this interaction by default; if you want to support multiple selection in custom views, you need to implement it yourself.
- **Distinguish between pointer and finger input only if it provides value** - For example, a scrubber can give people an additional way to target a location in a video when they're using the pointer. In this scenario, people can drag the playhead using either the pointer or touch, but they can use the pointer to click a precise seek destination.

**Pointer Shape and Content Effects**  
iPadOS integrates the appearance and behavior of both the pointer and the element it moves over, bringing focus to the item the pointer is targeting. You can support the system-provided pointer effects or modify them to suit your experience.

By default, the pointer's shape is a circle, but it can display a system-defined or custom shape when people move it over specific elements or regions. For example, the pointer automatically uses the familiar I-beam shape when people move it over a text-entry area.

With a content effect, the UI element or region beneath the pointer can also change its appearance when people hold the pointer over it. Depending on the type of content effect, the pointer can retain its current shape or transform into a shape that integrates with the element's new appearance.

iPadOS defines three content effects that bring focus to different types of interactive elements in your app: highlight, lift, and hover.

- **Highlight effect** - Transforms the pointer into a translucent, rounded rectangle that acts as a background for a control and includes a gentle parallax. By default, iPadOS applies the highlight effect to bar buttons, tab bars, segmented controls, and edit menus.
- **Lift effect** - Combines a subtle parallax with the appearance of elevation to make an element seem like it's floating above the screen. By default, iPadOS applies the lift effect to app icons and to buttons in Control Center.
- **Hover effect** - A generic effect that lets you apply custom scale, tint, or shadow values to an element as the pointer moves over it. The hover effect combines your custom values to bring focus to an item, but it doesn't transform the default pointer shape.

**Pointer Accessories**  
Pointer accessories are visual indicators that help people understand how they can use the pointer to interact with the current UI element. For example, a pointer approaching a resizable element might display small arrows to indicate that the element allows resizing along a certain axis.

- **Use clear, simple images to create custom accessories** - A pointer accessory is small, so it's essential to create an image that communicates the pointer interaction without using too many details.
- **Consider using the accessory transition to signal a change in an element's state or behavior** - In addition to animating the appearance and disappearance of pointer accessories, the system also animates the transitions among accessory shapes and positions that can accompany content effects.

**Pointer Magnetism**  
iPadOS helps people use the pointer to target an element by making the element appear to attract the pointer. People can experience this magnetic effect when they move the pointer close to an element and when they flick the pointer toward an element.

**Standard Pointers and Effects**  
- **When possible, support the system-provided content effects** - People quickly become accustomed to the content effects they see throughout the system and generally expect their experience to apply to every app they use.
- **Prefer the system-provided pointer appearances for standard buttons and text-entry areas** - You can help people feel more comfortable with your app when the pointer behaves in ways they expect.
- **Add padding around interactive elements to create comfortable hit regions** - You might need to experiment to determine the right size for an element's hit region. In general, it works well to add about 12 points of padding around elements that include a bezel; for elements without a bezel, it works well to add about 24 points of padding around the element's visible edges.

**macOS**  
macOS supports a wide range of standard mouse and trackpad interactions that people can customize. For example, when a click or gesture isn't a primary way to interact with content, people can often turn it on or off based on their current workflow.

Common mouse and trackpad gestures include:
- **Primary click** - Select or activate an item
- **Secondary click** - Reveal contextual menus
- **Scrolling** - Move content within a view
- **Smart zoom** - Zoom in or out on content
- **Swipe between pages** - Navigate between pages
- **Force click** - Display Quick Look or lookup windows
- **Pinch to zoom** - Zoom in or out
- **Rotate** - Rotate content

**iOS, visionOS**  
No additional considerations for iOS.

Not supported in tvOS or watchOS.

### Related Components

- [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures) - Gesture input
- [Focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection) - Focus system

### Developer Documentation

- [UIPointerAccessory](https://developer.apple.com/documentation/uikit/uipointeraccessory) - UIKit
- [UIPointerShape.roundedRect(_:radius:)](https://developer.apple.com/documentation/uikit/uipointershape/3539043-roundedrect) - UIKit
- [UIBandSelectionInteraction](https://developer.apple.com/documentation/uikit/uibandselectioninteraction) - UIKit

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)*