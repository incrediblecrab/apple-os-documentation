# IOBluetooth

Gain user-space access to Bluetooth devices.

**Platforms:** macOS 10.2+

## Overview

IOBluetooth provides C and Objective-C interfaces for user-space access to Bluetooth devices and classic Bluetooth profiles. Its macOS 10.2 framework minimum does not apply to every class: the hands-free classes below require macOS 10.7+.

For sandboxed apps, enable the Boolean [`com.apple.security.device.bluetooth`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.device.bluetooth) entitlement through App Sandbox's Bluetooth hardware option (macOS 10.7+). Current Bluetooth privacy configuration also requires the string [`NSBluetoothAlwaysUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsbluetoothalwaysusagedescription) to explain access to the Bluetooth interface. A paired device and a sandbox entitlement do not replace a person's privacy decision; handle unavailable hardware, denied access, disconnection, and pairing errors.

Prefer IOBluetoothUI's device-selection interface when it meets the app's needs. Direct `IOBluetoothDeviceInquiry` requests are throttled. Wait until inquiry has stopped before requesting remote device names; doing so from an active inquiry or its callbacks can deadlock the process.

## Topics

### Classes
- **IOBluetoothDevice** - An instance of IOBluetoothDevice represents a single remote Bluetooth device.
- **IOBluetoothDeviceInquiry** - Object representing a device inquiry that finds Bluetooth devices in-range of the computer, and (optionally) retrieves name information for them.
- **IOBluetoothDevicePair** - An instance of IOBluetoothDevicePair represents a pairing attempt to a remote Bluetooth device.
- **IOBluetoothDeviceRef** - An object that represents a Bluetooth I/O device.
- **IOBluetoothHandsFree** - Base class for hands-free-profile support; macOS 10.7+.
- **IOBluetoothHandsFreeAudioGateway** - Implements the audio-gateway portion of the Bluetooth audio profile; macOS 10.7+.
- **IOBluetoothHandsFreeDevice** - Provides call-control, call-status, and audio-transfer operations; macOS 10.7+.
- **IOBluetoothHostController** - This class is a representation of a Bluetooth Host Controller Interface that is present on the local computer (either plugged in externally or available internally).
- **IOBluetoothL2CAPChannel** - An instance of IOBluetoothL2CAPChannel represents a single open L2CAP channel.
- **IOBluetoothL2CAPChannelRef**
- **IOBluetoothOBEXSession** - An OBEX Session with a Bluetooth RFCOMM channel as the transport.
- **IOBluetoothObject**
- **IOBluetoothObjectRef**
- **IOBluetoothRFCOMMChannel** - Represents an RFCOMM channel for serial-port-style communication over L2CAP. RFCOMM transport and SDP service discovery are distinct protocols.
- **IOBluetoothRFCOMMChannelRef**
- **IOBluetoothSDPDataElement** - An instance of this class represents a single SDP data element as defined by the Bluetooth SDP spec.
- **IOBluetoothSDPDataElementRef**
- **IOBluetoothSDPServiceAttribute** - IOBluetoothSDPServiceAttribute represents a single SDP service attribute.
- **IOBluetoothSDPServiceRecord** - An instance of this class represents a single SDP service record.
- **IOBluetoothSDPServiceRecordRef**
- **IOBluetoothSDPUUID** - An NSData subclass that represents a UUID as defined in the Bluetooth SDP spec.
- **IOBluetoothSDPUUIDRef**
- **IOBluetoothUserNotification** - Represents a registered notification.
- **IOBluetoothUserNotificationRef**
- **OBEXFileTransferServices** - Implements advanced OBEX operations in addition to simple PUT and GET.
- **OBEXSession** - Object representing an OBEX connection to a remote target.

### Protocols
- **IOBluetoothDeviceAsyncCallbacks**
- **IOBluetoothDeviceInquiryDelegate** - This category on NSObject describes the delegate methods for the IOBluetoothDeviceInquiry object. All methods are optional, but it is highly recommended you implement them all. Do NOT invoke remote name requests on found IOBluetoothDevice objects unless the inquiry object has been stopped. Doing so may deadlock your process.
- **IOBluetoothDevicePairDelegate**
- **IOBluetoothHandsFreeAudioGatewayDelegate** - A set of optional methods for receiving information about status changes for a connected Bluetooth hands-free phone or headset.
- **IOBluetoothHandsFreeDelegate**
- **IOBluetoothHandsFreeDeviceDelegate** - A set of optional methods for receiving status change updates and information about a connected Bluetooth hands-free phone or headset.
- **IOBluetoothL2CAPChannelDelegate**
- **IOBluetoothRFCOMMChannelDelegate**

### Reference
- [Bluetooth.h User-Space](https://developer.apple.com/documentation/iobluetooth/bluetooth-h-user-space) - Bluetooth wireless-technology declarations.
- [IOBluetoothUserLib.h](https://developer.apple.com/documentation/iobluetooth/iobluetoothuserlib-h) - Public interfaces for Apple's implementation of Bluetooth technology.
- [IOBluetoothUtilities.h](https://developer.apple.com/documentation/iobluetooth/iobluetoothutilities-h)
- [OBEX.h](https://developer.apple.com/documentation/iobluetooth/obex-h) - Public OBEX technology interfaces.
- [OBEXBluetooth.h](https://developer.apple.com/documentation/iobluetooth/obexbluetooth-h) - Object Exchange over Bluetooth.
- [OBEXFileTransferServices.h](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices-h)
- [IOBluetooth Structures](https://developer.apple.com/documentation/iobluetooth/iobluetooth-structures)
- [IOBluetooth Enumerations](https://developer.apple.com/documentation/iobluetooth/iobluetooth-enumerations)
- [IOBluetooth Constants](https://developer.apple.com/documentation/iobluetooth/iobluetooth-constants)
- [IOBluetooth Functions](https://developer.apple.com/documentation/iobluetooth/iobluetooth-functions)
- [IOBluetooth Data Types](https://developer.apple.com/documentation/iobluetooth/iobluetooth-data-types)

### Variables
- **kBluetoothConnectionHandleSerialDeviceReserved**

### See Also
- [Bluetooth Device Access Guide](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/Bluetooth/BT_Intro/BT_Intro.html) - Archived architecture and application-development background, not current deployment or privacy requirements.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/IOBluetooth)*
