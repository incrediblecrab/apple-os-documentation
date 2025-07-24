# IOBluetooth

Gain user-space access to Bluetooth devices.

**Platforms:** macOS 10.2+

## Overview

The Bluetooth framework supports user-space access to Bluetooth devices, including both C and Objective-C APIs.

## Topics

### Classes
- **IOBluetoothDevice** - An instance of IOBluetoothDevice represents a single remote Bluetooth device.
- **IOBluetoothDeviceInquiry** - Object representing a device inquiry that finds Bluetooth devices in-range of the computer, and (optionally) retrieves name information for them.
- **IOBluetoothDevicePair** - An instance of IOBluetoothDevicePair represents a pairing attempt to a remote Bluetooth device.
- **IOBluetoothDeviceRef** - An object that represents a Bluetooth I/O device.
- **IOBluetoothHandsFree** - Hands free profile class.
- **IOBluetoothHandsFreeAudioGateway** - An object that sends data to a connected Bluetooth hands-free phone or headset and processes commands from it.
- **IOBluetoothHandsFreeDevice** - An object you use to manage phone calls on a connected Bluetooth hands-free phone or headset.
- **IOBluetoothHostController** - This class is a representation of a Bluetooth Host Controller Interface that is present on the local computer (either plugged in externally or available internally).
- **IOBluetoothL2CAPChannel** - An instance of IOBluetoothL2CAPChannel represents a single open L2CAP channel.
- **IOBluetoothL2CAPChannelRef**
- **IOBluetoothOBEXSession** - An OBEX Session with a Bluetooth RFCOMM channel as the transport.
- **IOBluetoothObject**
- **IOBluetoothObjectRef**
- **IOBluetoothRFCOMMChannel** - An instance of this class represents an RFCOMM channel as defined by the Bluetooth SDP spec.
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
- [Bluetooth.h User-Space](https://developer.apple.com/documentation/iobluetooth/bluetooth_h_user-space)
- [Bluetooth wireless technology](https://developer.apple.com/documentation/iobluetooth/bluetooth_wireless_technology)
- [IOBluetoothUserLib.h](https://developer.apple.com/documentation/iobluetooth/iobluetoothuserlib_h) - Public Interfaces for Apple's implementation of Bluetooth technology.
- [IOBluetoothUtilities.h](https://developer.apple.com/documentation/iobluetooth/iobluetoothutilities_h)
- [OBEX.h](https://developer.apple.com/documentation/iobluetooth/obex_h) - Public OBEX technology interfaces.
- [OBEXBluetooth.h](https://developer.apple.com/documentation/iobluetooth/obexbluetooth_h) - Object Exchange over Bluetooth.
- [OBEXFileTransferServices.h](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices_h)
- [IOBluetooth Structures](https://developer.apple.com/documentation/iobluetooth/iobluetooth_structures)
- [IOBluetooth Enumerations](https://developer.apple.com/documentation/iobluetooth/iobluetooth_enumerations)
- [IOBluetooth Constants](https://developer.apple.com/documentation/iobluetooth/iobluetooth_constants)
- [IOBluetooth Functions](https://developer.apple.com/documentation/iobluetooth/iobluetooth_functions)
- [IOBluetooth Data Types](https://developer.apple.com/documentation/iobluetooth/iobluetooth_data_types)

### Variables
- **kBluetoothConnectionHandleSerialDeviceReserved**

### See Also
- [Bluetooth Device Access Guide](https://developer.apple.com/documentation/iobluetooth/bluetooth_device_access_guide)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/IOBluetooth)*