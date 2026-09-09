# Camera Control

The Camera Control provides direct access to your app's camera experience.

**Platforms:** iOS

## Overview

On iPhone 16 and iPhone 16 Pro models, the Camera Control quickly opens your app's camera experience to capture moments as they happen. When a person lightly presses the Camera Control, the system displays an overlay that extends from the device bezel.

The overlay allows people to quickly adjust controls. A person can view the available controls by lightly double-pressing the Camera Control. After selecting a control, they can slide their finger on the Camera Control to adjust a value to capture their content as they want.

## Topics

### Anatomy

The Camera Control offers two types of controls for adjusting values or changing between options:

**Slider** - A slider provides a range of values to choose from, such as how much contrast to apply to the content.

**Picker** - A picker offers discrete options, such as turning a grid on and off in the viewfinder.

In addition to custom controls that you create, the system provides a set of standard controls that you can optionally include in the overlay to allow someone to adjust their camera's zoom and exposure:

- Zoom factor control
- Exposure bias control

### Best Practices

- **Use SF Symbols** - Use SF Symbols to represent control functionality. The system doesn't support custom symbols; instead, pick a symbol from SF Symbols that clearly denotes a control's behavior. iOS offers thousands of symbols you can use to represent the controls your app shows in the overlay. Symbols for controls don't represent their current state. To view available symbols, see the Camera & Photos section in the SF Symbols app.

- **Keep names short** - Keep names of controls short. Control labels adhere to Dynamic Type sizes, and longer names may obfuscate the camera's viewfinder.

- **Give values context** - Include appropriate units, symbols, or a localized description so people understand the parameter being adjusted. See [localizedValueFormat](https://developer.apple.com/documentation/avfoundation/avcaptureslider/localizedvalueformat).

- **Make useful increments easy to reach** - Choose prominent values that correspond to common settings or meaningful steps, rather than arbitrary stops. See [prominentValues](https://developer.apple.com/documentation/avfoundation/avcaptureslider/prominentvalues-199dz).

- **Make space for overlay** - Make space for the overlay in the viewfinder. The overlay and control labels occupy the screen area adjacent to the Camera Control in both portrait and landscape orientations. To avoid overlapping the interface elements of your camera capture experience, place your UI outside of the overlay areas. Maximize the height and width of the viewfinder and allow the overlay to appear and disappear over it.

- **Minimize viewfinder distractions** - Minimize distractions in the viewfinder. When capturing a photo or video, people appreciate a large preview image with as few visual distractions as possible. Avoid duplicating controls, like sliders and toggles, in your UI and the overlay when the system displays the overlay.

- **Enable controls based on mode** - Disable controls that don't apply to the current camera mode. Apple's HIG says controls can't be added or removed at runtime, but the [addControl(_:) reference](https://developer.apple.com/documentation/avfoundation/avcapturesession/addcontrol(_:)) explicitly permits adding controls while the session is running. Follow the capture-session API requirements, including checking `canAddControl(_:)`, rather than treating the HIG statement as an API restriction.

- **Consider control arrangement** - Consider how to arrange your controls. Order commonly used controls toward the middle to allow quick access, and include lesser used controls on either side. When a person lightly presses the Camera Control to open the overlay again, the system remembers the last control they used in your app.

- **Support the system's camera entrypoints** - Where appropriate, provide a locked camera capture extension so people can choose your capture experience for Camera Control. See [Camera experiences on a locked device](https://developer.apple.com/design/human-interface-guidelines/controls#Camera-experiences-on-a-locked-device).

### Platform Considerations

Not supported in iPadOS, macOS, watchOS, tvOS, or visionOS.

### Related

- [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols)
- [Controls](https://developer.apple.com/design/human-interface-guidelines/controls)

### Developer Documentation

- [Enhancing your app experience with the Camera Control — AVFoundation](https://developer.apple.com/documentation/avfoundation/enhancing-your-app-experience-with-the-camera-control)
- [AVCaptureControl — AVFoundation](https://developer.apple.com/documentation/avfoundation/avcapturecontrol)
- [LockedCameraCapture](https://developer.apple.com/documentation/lockedcameracapture)

## Changelog

### September 9, 2024
- New page.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/camera-control)*
