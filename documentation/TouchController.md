# Touch Controller

Integrate onscreen touch controls into your Metal-based games.

**Platforms:** iOS 26.0+ | iPadOS 26.0+

**Availability scope:** These are the platforms listed for the current `TCTouchController`, `TCControlContents`, and `TCControlImage` APIs. Do not infer Mac Catalyst or visionOS touch-control support from Game Controller's broader availability.

## Overview

Use **Touch Controller** to add custom and interactive touch controls for your games. The framework offers a suite of controls that enable support for a variety of control schemes, like buttons, directional pads, thumbsticks, throttle controls, and touchpads. The Game Controller framework supports each control and surfaces them through a **GCController** instance.

Use [TCTouchController](https://developer.apple.com/documentation/touchcontroller/tctouchcontroller) to manage controls, receive touch input, and render through Metal. The current reference uses [TCControlContents](https://developer.apple.com/documentation/touchcontroller/tccontrolcontents) and [TCControlImage](https://developer.apple.com/documentation/touchcontroller/tccontrolimage) for visual content, including system-provided control imagery.

## Integration checks

Check the controller's documented support property before offering this path. Connect and disconnect it with the game's input lifecycle so its `GCController` represents the active controls. Keep the view size in points distinct from the Metal drawable size in pixels when updating layouts.

Render with the controller's `render(using:)` method and feed it touch begin, move, and end events with consistent indices. Test resizing, multiple touches, cancellation in the surrounding input system, and switching to a physical controller. This is an OS 26-era API, not a new OS 27 introduction.

## Topics

### Essentials
- **TCTouchController** - An object that allows you to create and customize on-screen touch controls for a game that uses Metal.

### Controls
- **TCControl** - A protocol that defines the base properties and methods for all touch controls.
- **TCButton** - A control that represents a single on-screen button.
- **TCDirectionPad** - An object that represents a direction pad.
- [TCSwitch](https://developer.apple.com/documentation/touchcontroller/tcswitch) - A touch switch control.
- **TCThumbstick** - Represents a single on-screen thumbstick.
- **TCThrottle** - Represents a single on-screen throttle - a one axis input.
- **TCTouchpad** - Represents a single on-screen touchpad that reports absolute coordinates or delta movements.

### Control Configuration
- [TCTouchControllerDescriptor](https://developer.apple.com/documentation/touchcontroller/tctouchcontrollerdescriptor) - Configures the controller that owns and renders the controls.
- **TCButtonDescriptor** - A descriptor for configuring a button.
- **TCDirectionPadDescriptor** - A descriptor for configuring a directional pad.
- [TCSwitchDescriptor](https://developer.apple.com/documentation/touchcontroller/tcswitchdescriptor) - Configures a switch.
- **TCThumbstickDescriptor** - A descriptor for configuring a thumbstick.
- **TCThrottleDescriptor** - A descriptor for configuring a throttle.
- **TCTouchpadDescriptor** - A descriptor for configuring a touchpad.

### Visuals
- [TCControlContents](https://developer.apple.com/documentation/touchcontroller/tccontrolcontents) - Visual content associated with a control.
- [TCControlImage](https://developer.apple.com/documentation/touchcontroller/tccontrolimage) - An image used to draw control content.
- [TCControlLayout](https://developer.apple.com/documentation/touchcontroller/tccontrollayout) - Control-layout reference.

### System Content
- [TCControlContents.ButtonShape](https://developer.apple.com/documentation/touchcontroller/tccontrolcontents/buttonshape) - Shape choices for button content.
- [TCControlContents.DpadElementStyle](https://developer.apple.com/documentation/touchcontroller/tccontrolcontents/dpadelementstyle) - Style choices for directional-pad elements.
- [TCControlContents.DpadDirection](https://developer.apple.com/documentation/touchcontroller/tccontrolcontents/dpaddirection) - Direction choices for directional-pad content.

### Collision
- [TCColliderShape](https://developer.apple.com/documentation/touchcontroller/tccollidershape) - The current collider-shape enumeration used by a control's `colliderShape` property.
- [TCTouchController.control(at:)](https://developer.apple.com/documentation/touchcontroller/tctouchcontroller/control(at:)) - Finds the control at a specified point, if one exists.

Keep hit-test shape and visual artwork distinct. Use the current shape property rather than relying on the older standalone collider-class names, which are absent from the current control reference.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/TouchController)*
