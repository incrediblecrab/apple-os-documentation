# Core NFC

Detect NFC tags, read messages that contain NDEF data, and save data to writable tags.

**Platforms:** iOS 11.0+ | iPadOS 11.0+ | Mac Catalyst 13.1+

## Overview

Your app can read tags to give users more information about their physical environment and the real-world objects in it. Using Core NFC, you can read Near Field Communication (NFC) tags of types 1 through 5 that contain data in the NFC Data Exchange Format (NDEF). For example, your app might give users information about products they find in a store or exhibits they visit in a museum.

Your app can also write data to tags, and interact with protocol-specific tags such as ISO 7816, ISO 15693, FeliCa™, and MIFARE® tags.

Core NFC isn't available for use in app extensions, and it requires a device that supports Near Field Communication. To determine if support is available, check the readingAvailable class property before starting a reader session.

## Topics

### Essentials
- [Building an NFC Tag-Reader App](https://developer.apple.com/documentation/corenfc/building_an_nfc_tag-reader_app) - Read NFC tags with NDEF messages in your app.
- [Adding Support for Background Tag Reading](https://developer.apple.com/documentation/corenfc/adding_support_for_background_tag_reading) - Allow users to scan NFC tags without an app using background tag reading.
- **NFCReaderUsageDescription** - A message that tells people why the app is requesting access to the device's NFC hardware.

### Reader Sessions
- **NFCNDEFReaderSession** - A reader session for detecting NFC Data Exchange Format (NDEF) tags.
- **NFCTagReaderSession** - A reader session for detecting ISO7816, ISO15693, FeliCa, and MIFARE tags.
- **NFCVASReaderSession** - A reader session for processing Value Added Service (VAS) tags.
- **NFCReaderSession** - The abstract base class that represents a reader session for detecting NFC tags.
- **NFCReaderSessionProtocol** - A general interface for interacting with a reader session.
- **Near Field Communication Tag Reader Session Formats Entitlement** - The Near Field Communication data formats an app can read.

### Tag Types
- [Creating NFC Tags from Your iPhone](https://developer.apple.com/documentation/corenfc/creating_nfc_tags_from_your_iphone) - Save data to tags, and interact with them using native tag protocols.
- **NFCISO7816Tag** - An interface for interacting with an ISO 7816 tag.
- **NFCISO15693Tag** - An interface for interacting with an ISO 15693 tag.
- **NFCFeliCaTag** - An interface for interacting with a FeliCa™ tag.
- **NFCMiFareTag** - An interface for interacting with a MIFARE® tag.
- **NFCNDEFTag** - An interface for interacting with an NDEF tag.
- **NFCTag** - An object that represents an NFC tag object.
- **NFCTagCommandConfiguration** - A set of parameters you use to define the configuration of an NFC tag command.

### NDEF Messages and Payloads
- **NFCNDEFMessage** - An NFC NDEF message consisting of an array of payload records.
- **NFCNDEFPayload** - A payload record in an NFC NDEF message.

### Card Sessions
- **CardSession** - An ISO 7816 card emulation session.
- **NFCPresentmentIntentAssertion** - An object that signals your app's intention to make exclusive use of the device's contactless features.

### NFC Window Scenes
- **NFCWindowSceneDelegate** - A protocol to notify your app's user interface about NFC-related events.
- **NFCWindowSceneEvent** - An NFC-related event that your app uses to update its user interface.

### Errors
- **Code** - Reader session and tag error codes.
- **NFCReaderError** - An error type that indicates problems with reader sessions or tags.
- **NFCErrorDomain** - The domain for errors associated with Core NFC APIs.
- **NFCTagResponseUnexpectedLengthErrorKey** - A user-information dictionary key that indicates an invalid received response packet length.

### Reference

#### CoreNFC Enumerations

#### Classes
- **NFCISO15693CustomCommandConfiguration**
- **NFCISO15693ReadMultipleBlocksConfiguration**
- **NFCPaymentTagReaderSession** (Beta)

#### Structures
- **NFCFeliCaPollingResponse**
- **NFCFeliCaRequestSpecificationVersionResponse**
- **NFCFeliCaRequsetServiceV2Response**
- **NFCFeliCaStatusFlag**
- **NFCISO15693MultipleBlockSecurityStatus**
- **NFCISO15693SystemInfo**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreNFC)*