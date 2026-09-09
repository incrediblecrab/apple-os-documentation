# MIDIDriverKit

Develop drivers for MIDI devices.

**Platforms:** DriverKit 24.0+

## Overview

Use the MIDIDriverKit framework to implement a MIDI driver extension that communicates with Core MIDI. The framework handles all user-client communication between your driver extension and the Core MIDI server so you don't need to implement a MIDI driver plug-in. You can also leverage other transport-based driver extension frameworks, such as USBDriverKit, in your implementation.

The referenced sample requires Xcode 16 and targets macOS 15 or iPadOS 18 and later. On iPadOS, MIDIDriverKit requires an iPad with an **M-series chip**. The Mac app uses SystemExtensions for activation; on iPadOS, the person enables the driver in Settings > Privacy & Security > Drivers.

The framework's Core MIDI connection does not eliminate every user-client interface: a companion app may use a separate custom user client to configure the driver, as the sample demonstrates.

## Topics

### Essentials
- [Creating a MIDI device driver](https://developer.apple.com/documentation/mididriverkit/creating-a-midi-device-driver) - Implement a configurable virtual MIDI driver as a driver extension that runs in user space in macOS and iPadOS.
- **com.apple.developer.driverkit.family.midi** - A Boolean value that indicates whether to match the driver against devices that support MIDI.

### Classes
- **IOUserMIDIDestination**
- **IOUserMIDIDevice**
- **IOUserMIDIDriver**
- **IOUserMIDIEndpoint**
- **IOUserMIDIEntity**
- **IOUserMIDIObject**
- **IOUserMIDISource**

### Reference
- **MIDIDriverKit Constants**
- **MIDIDriverKit Data Types**

### Namespaces
- **MIDIDriverKit**

### Macros
- **kIOUserMIDIDriverUserClientType**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MIDIDriverKit)*
