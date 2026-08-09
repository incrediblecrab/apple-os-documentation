# Core Audio

Use the Core Audio framework to interact with device's audio hardware.

**Platforms:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 13.1+ | macOS 10.0+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 3.0+

## Overview

The Core Audio framework provides low-level access to audio hardware and allows interaction with the device's audio system.

## Topics

### Drivers
- [Creating an Audio Server Driver Plug-in](https://developer.apple.com/documentation/coreaudio/creating_an_audio_server_driver_plug-in) - Build a virtual audio device by creating a custom driver plug-in.
- [Building an Audio Server Plug-in and Driver Extension](https://developer.apple.com/documentation/coreaudio/building_an_audio_server_plug-in_and_driver_extension) - Create a plug-in and driver extension to support an audio device in macOS.
- [Capturing system audio with Core Audio taps](https://developer.apple.com/documentation/coreaudio/capturing_system_audio_with_core_audio_taps) - Use a Core Audio tap to capture outgoing audio from a process or group of processes.

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

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreAudio)*