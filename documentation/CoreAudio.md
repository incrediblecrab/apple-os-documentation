# Core Audio

Use the Core Audio framework to interact with device's audio hardware.

**Platforms:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 13.1+ | macOS 10.0+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 3.0+

## Overview

The Core Audio framework provides low-level access to audio hardware and allows interaction with the device's audio system.

### Process-tap authorization and sample scope

The [process-tap sample](https://developer.apple.com/documentation/coreaudio/capturing-system-audio-with-core-audio-taps) describes macOS system-audio capture. It requires `NSAudioCaptureUsageDescription`; the system asks for audio-recording permission when recording first starts from an aggregate device containing a tap. Creating a tap description is not permission to capture audio.

The sample's current metadata lists macOS 26 and Xcode 26, while its setup prose still mentions macOS 14.2. Do not use that setup sentence alone as a guarantee that the current sample builds against an older SDK. Check the particular C or Swift API and the sample project separately.

## Topics

### Drivers
- [Creating an Audio Server Driver Plug-in](https://developer.apple.com/documentation/coreaudio/creating-an-audio-server-driver-plug-in) - Build a virtual audio device by creating a custom driver plug-in.
- [Building an Audio Server Plug-in and Driver Extension](https://developer.apple.com/documentation/coreaudio/building-an-audio-server-plug-in-and-driver-extension) - Create a plug-in and driver extension to support an audio device in macOS.
- [Capturing system audio with Core Audio taps](https://developer.apple.com/documentation/coreaudio/capturing-system-audio-with-core-audio-taps) - Use a Core Audio tap to capture outgoing audio from a process or group of processes.

### Reference
- **Core Audio Structures**
- **Core Audio Data Types**
- **Core Audio Functions**
- **Core Audio Constants**
- **Core Audio Enumerations**

### Classes
- **AudioHardwareAggregateDevice**
- **AudioHardwareBox**
- **AudioHardwareClock**
- **AudioHardwareControl**
- **AudioHardwareDevice**
- **AudioHardwareObject**
- **AudioHardwarePlugin**
- **AudioHardwareProcess**
- **AudioHardwareStream**
- **AudioHardwareSystem**
- **AudioHardwareTap**
- **CATapDescription**

### Protocols
- **PropertyListenerDelegate**

### Structures
- **AudioHardwareError**
- **ManagedAudioChannelLayout**

### Variables
- **kAudioDevicePropertyWantsControlsRestored**
- **kAudioDevicePropertyWantsStreamFormatsRestored**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreAudio)*
