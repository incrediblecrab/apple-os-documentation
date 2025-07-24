# Touch Controller

Integrate onscreen touch controls into your Metal-based games.

**Platforms:** iOS 26.0+ Beta | iPadOS 26.0+ Beta | Mac Catalyst 26.0+ Beta | visionOS 26.0+ Beta

## Overview

Use **Touch Controller** to add custom and interactive touch controls for your games. The framework offers a suite of controls that enable support for a variety of control schemes, like buttons, directional pads, thumbsticks, throttle controls, and touchpads. The Game Controller framework supports each control and surfaces them through a **GCController** instance.

Use the **TCTouchController** class as the central point to manage and render your touch controls. To configure the appearance of your controls, use **TCControlVisuals** and **TCSpriteRenderer**. Use **TCControlSystemVisualsProvider** to create a consistent look and feel with system-provided assets.

## Topics

### Essentials
- **TCTouchController** - An object that allows you to create and customize on-screen touch controls for a game that uses Metal.

### Controls
- **TCControl** - A protocol that defines the base properties and methods for all touch controls.
- **TCButton** - A control that represents a single on-screen button.
- **TCDirectionPad** - An object that represents a direction pad.
- **TCThumbstick** - Represents a single on-screen thumbstick.
- **TCThrottle** - Represents a single on-screen throttle - a one axis input.
- **TCTouchpad** - Represents a single on-screen touchpad that reports absolute coordinates or delta movements.

### Control Configuration
- **TCButtonDescriptor** - A descriptor for configuring a button.
- **TCDirectionPadDescriptor** - A descriptor for configuring a directional pad.
- **TCThumbstickDescriptor** - A descriptor for configuring a thumbstick.
- **TCThrottleDescriptor** - A descriptor for configuring a throttle.
- **TCTouchpadDescriptor** - A descriptor for configuring a touchpad.

### Visuals
- **TCControlVisuals** - Represents the visual elements of a touch control.
- **TCSpriteRenderer** - A renderer for drawing sprites using Metal.

### System Visuals
- **TCControlSystemVisualsProvider** - Provides system-defined visuals for touch controls.
- **TCButtonVisualShape** - Defines the visual shape of a button.
- **TCDirectionPadVisualStyle** - Defines the visual style of a direction pad.
- **TCDirectionPadVisualDirection** - Defines the direction of a direction pad visual.

### Collision
- **TCCollider** - A protocol defining the collider properties for a control.
- **TCColliderType** - Defines the type of collider.
- **TCRectCollider** - A rectangular collider.
- **TCCircleCollider** - A circular collider.
- **TCRegionCollider** - A collider that covers a specific region of the touch controller.
- **TCRegionColliderRegion** - Defines the region of the touch controller that the TCRegionCollider represents.

---

**Beta Software**

This documentation contains preliminary information about an API or technology in development. This information is subject to change, and software implemented according to this documentation should be tested with final operating system software.

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/TouchController)*