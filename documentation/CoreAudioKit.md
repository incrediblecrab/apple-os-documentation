# CoreAudioKit

Add user interfaces to audio units.

**Platforms:** iOS 8.0+ | iPadOS 8.0+ | Mac Catalyst 13.0+ | macOS 10.4+ | visionOS 1.0+

## Overview

Core Audio Kit provides views and controllers to use when building Audio Unit user interfaces.

## Topics

### Audio Units
- **AUViewController** - The base class to extend when creating a custom user interface for an audio unit.
- **AUAudioUnitViewConfiguration** - A configuration object that describes how to present the audio unit's user interface.
- **AUGenericView** - A view that provides a generic user interface for a Cocoa audio unit.
- **AUPannerView** - A view that provides a specialized user interface for a Cocoa-based panner audio unit.
- **AUCustomViewPersistentData** - A protocol that defines the methods an Audio Unit host calls to manage view data.

### Bluetooth Devices
- **CABTLEMIDIWindowController** - A window controller that displays nearby Bluetooth-based MIDI peripherals.
- **CABTMIDICentralViewController** - A view controller that displays nearby Bluetooth-based MIDI peripherals.
- **CABTMIDILocalPeripheralViewController** - A view controller that advertises an iOS device as a Bluetooth-based MIDI peripheral.

### Network Devices
- **CANetworkBrowserWindowController** - A window controller that displays available network audio devices.

### Inter-Device Audio
- **CAInterDeviceAudioViewController** - A view controller object that displays iOS devices that support inter-device audio.

### Inter-App Audio
> Inter-App Audio is deprecated in iOS 13 and is unavailable when running iPad apps in macOS.

- **CAInterAppAudioSwitcherView** - A view that provides an audio switcher user interface. *Deprecated*
- **CAInterAppAudioTransportView** - A view that provides an audio transport user interface. *Deprecated*

### Deprecations
- **AUGenericViewInternal**
- **AUGenericViewInternalBase**

### Classes
- **AUAppleCustomViewLoader**
- **AUGenericViewController**

### Structures
- **AUGenericViewDisplayFlags** - Flags that describe the display of a generic view.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreAudioKit)*