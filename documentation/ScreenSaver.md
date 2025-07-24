# Screen Saver

Animate screen savers, and interact with the screen saver infrastructure.

**Platforms:** macOS 10.0+

## Overview

The Screen Saver framework defines the interface for custom modules to interact with the Screen Effects user interface feature. Write screen savers in Objective-C, and implement your module's user interface using Cocoa. Use the available functions to produce random values and centering rectangles.

To create a screen saver, create a bundle directory with the .saver suffix and install it in one of the Library/Screen Savers directories on the system. In your bundle's executable, include a ScreenSaverView subclass. That view defines the interface you use to generate your screen saver content. If your screen saver stores any preference information, use the ScreenSaverDefaults class instead of the standard UserDefaults class.

Because screen savers are plug-ins for the screen saver engine, the screen saver binary must support the same hardware architecture of the running engine. As with any application, the screen saver engine uses the native architecture of the host computer. For full compatibility, make sure your screen saver supports both the x86_64 and arm64 architectures.

### How the system runs your screen saver

When macOS starts your screen saver, the system:

- Fades the screen to black.
- Instantiates your ScreenSaverView subclass and calls its init(frame:isPreview:) method.
- Creates a window and installs your ScreenSaverView subclass in it.
- Activates the window and sets its order.
- Calls your view's draw(_:) method so you can draw your initial state.
- Fades in the screen to reveal your window in the front.
- Calls your view's startAnimation() method, which you use to set up any animation-related state information.
- Calls your view's animateOneFrame() method repeatedly.

When the user takes some action, the system calls your view's stopAnimation() method to stop your screen saver. Use that method to clean up any state information you establish in your startAnimation() method.

**Note:** The stopAnimation() or startAnimation() methods don't immediately start or stop the animations. The system can still call your animateOneFrame() method after calling stopAnimation().

## Topics

### Interface
- **ScreenSaverView** - An abstract class that defines the interface for subclassers to interact with the screen saver infrastructure.
- **ScreenSaverDefaults** - A class that defines a set of methods for saving and restoring user defaults for screen savers.

### Utilities
- **SSRandomIntBetween(Int32, Int32) -> Int32** - Returns a random integer value.
- **SSRandomFloatBetween(CGFloat, CGFloat) -> CGFloat** - Returns a random float value.
- **SSRandomPointForSizeWithinRect(NSSize, NSRect) -> NSPoint** - Returns a random point.
- **SSCenteredRectInRect(NSRect, NSRect) -> NSRect** - Returns a rectangle.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ScreenSaver)*