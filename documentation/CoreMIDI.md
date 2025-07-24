# Core MIDI

Communicate with MIDI devices such as hardware keyboards and synthesizers.

**Platforms:** iOS 4.2+ | iPadOS 4.2+ | Mac Catalyst 13.0+ | macOS 10.0+ | tvOS 15.0+ | visionOS 1.0+ | watchOS 8.0+

## Overview

The Core MIDI framework provides APIs to communicate with MIDI (Musical Instrument Digital Interface) devices, including hardware keyboards and synthesizers. Connect from an iOS device using the dock connector or a network. For more information about using the dock connector, see the MFi Program.

## Topics

### Services
- [MIDI Services](https://developer.apple.com/documentation/coremidi/midi_services) - Communicate with hardware using Universal MIDI Packets.
- [MIDI System Setup](https://developer.apple.com/documentation/coremidi/midi_system_setup) - Configure the global MIDI system.
- [MIDI Bluetooth](https://developer.apple.com/documentation/coremidi/midi_bluetooth) - Connect to Bluetooth Low Energy MIDI peripherals.
- [MIDI Messages](https://developer.apple.com/documentation/coremidi/midi_messages) - Create and configure messages.
- [MIDI Thru Connection](https://developer.apple.com/documentation/coremidi/midi_thru_connection) - Create play-through connections between sources and destinations.
- [MIDI Networking](https://developer.apple.com/documentation/coremidi/midi_networking) - Create and manage devices connected over a local network.
- [MIDI Drivers](https://developer.apple.com/documentation/coremidi/midi_drivers) - Create driver plug-ins.
- [MIDI Capability Inquiry](https://developer.apple.com/documentation/coremidi/midi_capability_inquiry) - Provide support for bidirectional discovery and configuration of devices.

### Reference
- [Core MIDI Structures](https://developer.apple.com/documentation/coremidi/core_midi_structures)
- [Core MIDI Enumerations](https://developer.apple.com/documentation/coremidi/core_midi_enumerations)
- [Core MIDI Constants](https://developer.apple.com/documentation/coremidi/core_midi_constants)
- [Core MIDI Functions](https://developer.apple.com/documentation/coremidi/core_midi_functions)
- [Core MIDI Data Types](https://developer.apple.com/documentation/coremidi/core_midi_data_types)
- [Core MIDI Macros](https://developer.apple.com/documentation/coremidi/core_midi_macros)

### Articles
- [Deprecated Symbols](https://developer.apple.com/documentation/coremidi/deprecated_symbols) - Review unsupported symbols and their replacements.

### Classes
- **kMIDIObjectType_ExternalMask** - A bit mask indicating that a device is external.
- **MIDI2DeviceInfo**
- **MIDICIDevice**
- **MIDICIDeviceManager**
- **MIDICIDiscoveredNode** - A discovered MIDI-CI node that represents a MIDI source and destination that respond to capability inquiries.
- **MIDIUMPCIProfile** (Deprecated)
- **MIDIUMPEndpoint**
- **MIDIUMPEndpointManager**
- **MIDIUMPFunctionBlock**
- **MIDIUMPMutableEndpoint**
- **MIDIUMPMutableFunctionBlock**

### Variables
- **kMIDINoteAttributeManufacturerSpecific** (Deprecated)
- **kMIDINoteAttributeNone** (Deprecated)
- **kMIDINoteAttributePitch** (Deprecated)
- **kMIDINoteAttributeProfileSpecific** (Deprecated)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreMIDI)*