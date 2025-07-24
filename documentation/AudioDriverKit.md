# AudioDriverKit

Develop drivers for audio devices.

**Platforms:** DriverKit 21.0+

## Overview

The AudioDriverKit framework supports the development of DriverKit-based audio extensions that communicate with the CoreAudio HAL. AudioDriverKit handles all of the necessary user client communication between the CoreAudio HAL and the driver extension, which eliminates the need to implement an audio server plug-in. You can also integrate with transport-based driver extension frameworks like PCIDriverKit.

Develop your driver by subclassing IOUserAudioDriver. On macOS, use the System Extensions framework to install and upgrade your driver. On iPadOS, the system automatically discovers and upgrades drivers along with their host apps.

> **Note:** AudioDriverKit is available on macOS for Intel and Apple Silicon devices, and on iPadOS for devices with an M-series processor.

## Topics

### Essentials
- **IOUserAudioObject** - The base class for most classes in the framework.
- **IOUserAudioDriver** - A DriverKit provider object that manages communications with an audio device.
- **DriverKit Audio Family** - A Boolean value that indicates whether the device supports audio functionality.
- [Creating an audio device driver](https://developer.apple.com/documentation/audiodriverkit/creating_an_audio_device_driver) - Implement a configurable audio input source as a driver extension that runs in user space in macOS and iPadOS.

### Working with Audio Devices
- **IOUserAudioClockDevice** - An audio clock device object, used to synchronize and perform I/O.
- **IOUserAudioDevice** - An audio clock device object that handles the configurations for running I/O.

### Containing Audio Objects
- **IOUserAudioBox** - A container for other audio objects, typically audio devices and audio clock devices.

### Working with Audio Streams
- **IOUserAudioStream** - An audio object that performs I/O for an audio device.

### Using Audio Controls
- **IOUserAudioControl** - The base class for audio control objects.
- **IOUserAudioBooleanControl** - A control object that supports setting a Boolean value.
- **IOUserAudioStereoPanControl** - A control object that supports panning between stereo channels.
- **IOUserAudioSliderControl** - A control object that supports setting a 32-bit integer value.
- **IOUserAudioSelectorControl** - A control object that supports selecting from a set of values.
- **IOUserAudioLevelControl** - A control object that supports setting an audio level, with either scalar or decibel values.

### Supporting Types
- **IOUserAudioReservedConfigChangeAction** - Identifiers for object state changes that require a configuration change.

### Namespaces
- **AudioDriverKit**

### Macros
- **DebugMsg**
- **FailIf**
- **FailIfError**
- **FailIfNULL**
- **kIOUserAudioDriverUserClientType**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AudioDriverKit)*