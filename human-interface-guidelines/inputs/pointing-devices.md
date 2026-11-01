# Pointing Devices

People can use a pointing device like a trackpad or mouse to navigate the interface and initiate actions.

**Platforms:** iOS | iPadOS | macOS | visionOS

## Overview

People appreciate the precision and flexibility that pointing devices offer. On a Mac, people typically expect to combine a pointing device with a keyboard as they navigate apps and the system. On iPad and Apple Vision Pro, a pointing device gives people an additional way to interact with apps and content, without replacing touch, eyes, or gestures.

Test pointer targeting as windows resize and on supported external displays. Keep touch and keyboard alternatives usable, and do not hide an essential action behind hover alone. See [Designing for iPadOS](../getting-started/iPadOS.md).

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

**iPadOS 26 and later**

Apple introduced a more precise pointer and a Liquid Glass highlight treatment in iPadOS 26. The pointer tracks input directly rather than magnetizing or rubber-banding to controls. Test existing pointer effects against that behavior. Apple's [Elevate the design of your iPad app](https://developer.apple.com/videos/play/wwdc2025/208) session describes the change in its Pointer chapter.

- **Allow multiple selection in custom views when necessary** - In iPadOS 15 and later, people can click and drag the pointer over multiple items to select them. As people use the pointer in this way, it expands into a visible rectangle that selects the items it encompasses. Standard nonlist collection views support this interaction by default; if you want to support multiple selection in custom views, you need to implement it yourself.
- **Distinguish between pointer and finger input only if it provides value** - For example, a scrubber can give people an additional way to target a location in a video when they're using the pointer. In this scenario, people can drag the playhead using either the pointer or touch, but they can use the pointer to click a precise seek destination.

**Pointer Shape and Content Effects**  
iPadOS integrates the appearance and behavior of both the pointer and the element it moves over, bringing focus to the item the pointer is targeting. You can support the system-provided pointer effects or modify them to suit your experience.

By default, the pointer's shape is an arrow, but it can display a system-defined or custom shape when people move it over specific elements or regions. For example, the pointer automatically uses the familiar I-beam shape when people move it over a text-entry area.

With a content effect, the UI element or region beneath the pointer can also change its appearance when people hold the pointer over it. iPadOS defines three content effects that bring focus to different types of interactive elements in your app: highlight, lift, and hover.

- **Highlight effect** - Places a Liquid Glass shape between the pointer and the control it's over, focusing the control without distracting from the task. By default, iPadOS applies the highlight effect to bar buttons, tab bars, segmented controls, and edit menus.
- **Lift effect** - Combines a subtle parallax with the appearance of elevation to make an element seem like it's floating above the screen: the system scales the element up, adds a shadow beneath it and a soft specular highlight on top. By default, iPadOS applies the lift effect to standalone Liquid Glass controls, app icons, and buttons in Control Center.
- **Hover effect** - A generic effect that lets you apply custom scale, tint, or shadow values to an element as the pointer moves over it. The hover effect combines your custom values to bring focus to an item, but it doesn't transform the default pointer shape.

Before iPadOS 26, the pointer was circular by default and morphed into the highlight behind the control it was over. Apple's WWDC25 session above describes the iPadOS 26 pointer's new shape and the Liquid Glass highlight that replaces the morphing effect.

**Pointer Accessories**  
Pointer accessories are visual indicators that help people understand how they can use the pointer to interact with the current UI element. For example, a pointer approaching a resizable element might display small arrows to indicate that the element allows resizing along a certain axis.

- **Use clear, simple images to create custom accessories** - A pointer accessory is small, so it's essential to create an image that communicates the pointer interaction without using too many details.
- **Consider using the accessory transition to signal a change in an element's state or behavior** - In addition to animating the appearance and disappearance of pointer accessories, the system also animates the transitions among accessory shapes and positions that can accompany content effects.

**Pointer Magnetism**  
Before iPadOS 26, the pointer magnetized to nearby targets. In iPadOS 26 it no longer magnetizes or rubber-bands to any target and always tracks input directly, as the WWDC25 session above describes. The current HIG article no longer covers magnetism.

**Standard Pointers and Effects**  
- **When possible, support the system-provided content effects** - People quickly become accustomed to the content effects they see throughout the system and generally expect their experience to apply to every app they use. Use highlight for a group of controls in a Liquid Glass container, lift for a standalone Liquid Glass control or a small element with an opaque background, and hover for large elements, customizing scale, tint, and shadow as needed.
- **Prefer the system-provided pointer appearances for standard buttons and text-entry areas** - You can help people feel more comfortable with your app when the pointer behaves in ways they expect.
- **Add padding around interactive elements to create comfortable hit regions** - You might need to experiment to determine the right size for an element's hit region. In general, it works well to add about 12 points of padding around elements that include a bezel; for elements without a bezel, it works well to add about 24 points of padding around the element's visible edges.
- **Create contiguous hit regions for custom bar buttons** - If there's space between the hit regions of adjacent buttons in a bar, the highlight shape briefly disappears as the pointer moves between them, which causes distracting motion.

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

**Touch Support for Hidden Controls on Mac**  
Some Mac apps show certain controls only when the pointer moves over them. On a Mac with a touch display, those controls need another way to appear. See also [Gestures](gestures.md).

- **Decide which hidden controls need touch support** - Add it for essential controls only. Tooltips and other static information don't need it, and neither do features people can already reach with touch, such as carousel navigation buttons when people can swipe to scroll. Don't keep hidden controls permanently visible just to accommodate touch.
- **Reveal a hidden control when someone taps its general location** - Reveal only the controls relevant to the content in use, and hide a control again when the person is done with it or after a few seconds without use. Sidebars and the close button in a tabbed window follow the rules below.
- **Retain the current selection when revealing a hidden control** - Tapping to reveal a control, and then tapping the control, shouldn't change the selection the control might act on.
- **Make essential hidden controls available in a context menu** - A short context menu with the most-needed controls gives a dependable route; with touch, people open it by touching and holding. See [Context menus](https://developer.apple.com/design/human-interface-guidelines/context-menus).
- **In a sidebar, reveal hidden controls when someone taps the section header or row** - The tap does what a click does, such as collapsing a section or selecting a row, and reveals the controls for that item only. Keep them visible until touch moves outside the sidebar or the person uses a pointing device again. A tap on a hidden control's area reveals the control without activating it; a second tap activates it.
- **In a tabbed window, reveal the selected tab's close button when someone taps anywhere in the window** - Keep it visible until the person returns to a pointing device. If they close the selected tab with touch, show the close button on the newly selected tab.

**iOS**

No additional considerations for iOS.

Not supported in tvOS or watchOS.

### Related Components

- [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures) - Gesture input
- [Focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection) - Focus system

### Developer Documentation

- [UIPointerAccessory](https://developer.apple.com/documentation/uikit/uipointeraccessory) - UIKit
- [UIPointerShape.roundedRect(_:radius:)](https://developer.apple.com/documentation/uikit/uipointershape-swift.enum/roundedrect(_:radius:)) - UIKit
- [UIBandSelectionInteraction](https://developer.apple.com/documentation/uikit/uibandselectioninteraction) - UIKit
- [Pointer interactions](https://developer.apple.com/documentation/uikit/pointer-interactions) - UIKit
- [Input events](https://developer.apple.com/documentation/swiftui/input-events) - SwiftUI
- [Mouse, Keyboard, and Trackpad](https://developer.apple.com/documentation/appkit/mouse-keyboard-and-trackpad) - AppKit

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)*
