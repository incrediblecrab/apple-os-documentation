# Game Controller

Support hardware game controllers in your game.

**Platforms:** iOS 7.0+ | iPadOS 7.0+ | Mac Catalyst 13.1+ | macOS 10.9+ | tvOS 9.0+ | visionOS 1.0+

## Overview

Use Game Controller to support users interacting with your app using a physical or virtual game controller. Game controllers include third-party products, such as the DualShock 4, DualSense, and Xbox, as well as the mouse, keyboard, Siri Remote, and racing wheels.

To support game controllers, add the Game Controller capability (the GCSupportsControllerUserInteraction property) to your project, and Xcode adds the Game Controller framework automatically. Then, choose the types of controllers your app supports (the GCSupportedGameControllers property) under the Game Controllers capability on the Signing & Capabilities pane.

For controllers other than the racing wheel, follow these steps to process the game controller input in your app:

- To get a physical game controller object, register for specific notifications when users connect and disconnect game controllers. Alternatively, you can display a virtual controller for the user to interact with.

- Then get a profile object from the physical or virtual controller to access its input elements, such as buttons, triggers, thumbsticks, and directional pads. Profiles encapsulate the hardware details and layout of the input elements on the controller from your app.

- To process the input, either get the values directly from the elements or register callbacks for when the user changes their values. Apps running in visionOS receive input events only when the person is looking at the app's window.

For controllers that support haptics, you can provide feedback to the user by creating an engine that manipulates the controller's actuators.

Users may remap game controller elements in Settings and Preferences, so be sure to display the correct input element in your interface. If the hasRemappedElements property is true, the user remapped elements and you can get the mapping between the actual and alias elements using the mappedElementAlias(forPhysicalInputName:) and mappedPhysicalInputNames(forElementAlias:) methods.

To support racing wheel devices in your macOS app, see Racing wheel device support.

## OS 27 controller testing

The [iOS and iPadOS](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes#Game-Controller) and [macOS](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes#Game-Controller) Beta 8 notes checked September 8, 2026 add support for the **PlayStation Access controller** on those three platforms, including device-local custom input profiles (168071382). Do not extend that announcement to tvOS or visionOS without separate support evidence.

The macOS notes mark lightbar changes persisting after focus loss (163514369) and incorrect `supportsHIDDevice:` results shortly after connection (176985783) as **resolved**. Keep focus changes, device connection, and profile remapping in the regression suite rather than describing these defects as ongoing limitations.

For spatial controllers and styli, follow [Apple's discovery and tracking guide](https://developer.apple.com/documentation/gamecontroller/discovering-and-tracking-spatial-game-controllers-and-styli):

- Use connection notifications for initial discovery; an immediate list query can be empty while discovery is still completing.
- Obtain input through Game Controller and spatial tracking through ARKit or RealityKit. Accessory transforms require the documented `NSAccessoryTrackingUsageDescription` and tracking authorization.
- Use the accessory's supported locations and inputs rather than assuming every controller has the same buttons, haptics, or tracking points.

The [visionOS 27 Bluetooth notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-27-release-notes#Bluetooth) still list initial spatial-accessory tracking failure after pairing as a **known issue** (181827411), with an accessory or Bluetooth off/on cycle as the workaround. This is separate from the resolved macOS controller issues.

## Topics

### Essentials
- [Game Controller updates](https://developer.apple.com/documentation/updates/gamecontroller) - Learn about important changes to Game Controller.
- **GCSupportsControllerUserInteraction** - A Boolean value indicating whether the app supports a game controller.
- **GCSupportedGameControllers** - The types of game controller profiles that the app supports or requires.
- **GCSupportsMultipleMicroGamepads** - A Boolean value indicating whether the physical Apple TV Remote and the Apple TV Remote app operate as separate game controllers.
- [Handling input events](https://developer.apple.com/documentation/gamecontroller/handling-input-events) - Receive controller input using either polling or callbacks.

### View Controller
- **GCEventViewController** - A view controller that delivers input either from the responder chain to views, or from game controllers to profiles.

### Game Controllers
- [Supporting Game Controllers](https://developer.apple.com/documentation/gamecontroller/supporting-game-controllers) - Support a physical controller or add a virtual controller to enhance how people interact with your game through haptics, lighting, and motion sensing.
- [Letting players use their second-generation Siri Remote as a game controller](https://developer.apple.com/documentation/gamecontroller/letting-players-use-their-second-generation-siri-remote-as-a-game-controller) - Support the second-generation Siri Remote as a game controller in your Apple TV game.
- [Discovering and tracking spatial game controllers and styli](https://developer.apple.com/documentation/gamecontroller/discovering-and-tracking-spatial-game-controllers-and-styli) - Receive controller and stylus input to interact with content in your augmented reality app.
- **GCDevice** - A protocol that defines a common interface for game input devices.
- **GCController** - A representation of a real game controller, a virtual controller, or a snapshot of a controller.
- **GCRacingWheel** - An object that represents a physical racing wheel controller connected to a device.
- **GCKeyboard** - An object that represents a physical keyboard connected to a device.
- **GCMouse** - An object that represents a physical mouse connected to a device.
- **GCStylus** - An object that represents a physical stylus connected to the device.
### Game Controller Profiles
- [Input](https://developer.apple.com/documentation/gamecontroller/input) - Receive controller input in the way that best integrates with the flow of your game or game engine.
- **GCMotion** - A controller profile that supports orientation and motion.
- **GCDeviceBattery** - The charge level and state of a device's battery.
- **GCDeviceHaptics** - The locations of haptic actuators on a game controller.
- **GCDeviceLight** - The colored light on a device.

### Touch Controller
- [Adding virtual controls to games that support game controllers in iOS](https://developer.apple.com/documentation/gamecontroller/adding-virtual-controls-to-games-that-support-game-controllers-in-ios) - Use `GCVirtualController` for players without physical controllers. This is separate from the newer Touch Controller framework.
- **GCVirtualController** - A software emulation of a real controller that you configure specifically for your game.

### Button Elements and Names
- **GCTouchedStateInput** - The common properties for an element that has touch state input.
- **GCPressedStateInput** - The common properties for an element that has press state input, such as input from a button.

### Racing Wheels
- [Racing wheel device support](https://developer.apple.com/documentation/gamecontroller/racing-wheel-device-support) - Add support for racing wheel devices in macOS.
- [Understanding game controller backward compatibility](https://developer.apple.com/documentation/gamecontroller/understanding-game-controller-backward-compatibility) - Learn how macOS brings support for the latest game controllers to software that predates the introduction of the Game Controller framework.
- **kIOHIDGCSyntheticDeviceKey** - A key that specifies whether the device is a game controller synthetic HID device.

### Aliases for Backward Compatibility
- **GCDeviceElement** - An alias for a symbol name for backward compatibility with a previous SDK version.
- **GCDeviceAxisInput** - An alias for a symbol name for backward compatibility with a previous SDK version.
- **GCDeviceButtonInput** - An alias for a symbol name for backward compatibility with a previous SDK version.
- **GCDeviceTouchpad** - An alias for a symbol name for backward compatibility with a previous SDK version.
- **GCDeviceDirectionPad** - An alias for a symbol name for backward compatibility with a previous SDK version.

### Deprecated Symbols
- [Deprecated symbols](https://developer.apple.com/documentation/gamecontroller/deprecated-symbols)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/GameController)*
