# Core NFC

Detect NFC tags, read messages that contain NDEF data, and save data to writable tags.

**SDK platforms:** iOS 11.0+ | iPadOS 11.0+ | Mac Catalyst 13.1+. A declaration on a platform does not establish the presence of usable NFC hardware.

## Overview

Your app can read tags to give users more information about their physical environment and the real-world objects in it. Using Core NFC, you can read Near Field Communication (NFC) tags of types 1 through 5 that contain data in the NFC Data Exchange Format (NDEF). For example, your app might give users information about products they find in a store or exhibits they visit in a museum.

Your app can also write data to tags, and interact with protocol-specific tags such as ISO 7816, ISO 15693, FeliCa™, and MIFARE® tags.

Core NFC isn't available for use in app extensions, and it requires a device that supports Near Field Communication. To determine if support is available, check the readingAvailable class property before starting a reader session.

Configure the string `NFCReaderUsageDescription` and the string-array [`com.apple.developer.nfc.readersession.formats`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.nfc.readersession.formats) entitlement through the NFC Tag Reading capability. Missing purpose text terminates an app that attempts to read a tag. Handle cancellation and reader invalidation; an invalidated session cannot be reused.

Background tag reading is a system feature on supported iPhones, not continuous app execution. The system displays a notification for a suitable NDEF URI; tapping it and, when necessary, unlocking the phone delivers the data. App links need the documented Associated Domains configuration. Custom URL schemes are not supported by this background-reading path.

### Distinct payment and emulation features

`CardSession` and `NFCPresentmentIntentAssertion` start at 17.4. Host card emulation is a separately entitled, eligibility-gated workflow documented for the European Economic Area (EEA), not an unrestricted extension of basic NDEF reading. Check `NFCReaderSession.readingAvailable`, `CardSession.isSupported`, and `CardSession.isEligible` before creating a card session.

HCE requires the Boolean [`com.apple.developer.nfc.hce`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.nfc.hce) and string-array [`com.apple.developer.nfc.hce.iso7816.select-identifier-prefixes`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.nfc.hce.iso7816.select-identifier-prefixes) entitlements. Missing required privileges can cause initialization to raise a fatal error. An optional default-contactless-app entitlement does not itself make the app the person's selected default.

Presentment intent is foreground-only and expires on backgrounding, deinitialization, or after 15 seconds; a 15-second cooldown follows expiry. Card emulation has a separate maximum duration of 60 seconds after `startEmulation()`. Handle reader loss, expiry, and session invalidation instead of assuming continued exclusive access.

`NFCPaymentTagReaderSession` is a different, 26.0-generation **reader** API. Its documented customer conditions require an EU-registered account and a device physically in the EU; check that session type's `readingAvailable`. Follow its separate development-testing, supported-AID, and format requirements. Neither HCE nor payment-tag hardware testing is replaced by a Simulator or a platform header.

## Topics

### Essentials
- [Building an NFC Tag-Reader App](https://developer.apple.com/documentation/corenfc/building-an-nfc-tag-reader-app) - Read NFC tags with NDEF messages in your app.
- [Adding Support for Background Tag Reading](https://developer.apple.com/documentation/corenfc/adding-support-for-background-tag-reading) - Handle tags read by the system and delivered after user interaction.
- **NFCReaderUsageDescription** - A message that tells people why the app is requesting access to the device's NFC hardware.

### Reader Sessions
- **NFCNDEFReaderSession** - A reader session for detecting NFC Data Exchange Format (NDEF) tags.
- **NFCTagReaderSession** - A reader session for detecting ISO7816, ISO15693, FeliCa, and MIFARE tags.
- [NFCPaymentTagReaderSession](https://developer.apple.com/documentation/corenfc/nfcpaymenttagreadersession) - The region-limited payment-tag reader introduced in 26.
- **NFCVASReaderSession** - A reader session for processing Value Added Service (VAS) tags.
- **NFCReaderSession** - The abstract base class that represents a reader session for detecting NFC tags.
- **NFCReaderSessionProtocol** - A general interface for interacting with a reader session.
- **Near Field Communication Tag Reader Session Formats Entitlement** - The Near Field Communication data formats an app can read.

### Tag Types
- [Creating NFC Tags from Your iPhone](https://developer.apple.com/documentation/corenfc/creating-nfc-tags-from-your-iphone) - Save data to tags, and interact with them using native tag protocols.
- **NFCISO7816Tag** - An interface for interacting with an ISO 7816 tag.
- **NFCISO15693Tag** - An interface for interacting with an ISO 15693 tag.
- **NFCFeliCaTag** - An interface for interacting with a FeliCa™ tag.
- **NFCMiFareTag** - An interface for interacting with a MIFARE® tag.
- **NFCNDEFTag** - An interface for interacting with an NDEF tag.
- **NFCTag** - A Swift enum that wraps the detected protocol-specific tag.
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
- **NFCReaderError.Code** - Reader session and tag error codes.
- **NFCReaderError** - An error type that indicates problems with reader sessions or tags.
- **NFCErrorDomain** - The domain for errors associated with Core NFC APIs.
- **NFCTagResponseUnexpectedLengthErrorKey** - A user-information dictionary key that indicates an invalid received response packet length.

### Reference

#### CoreNFC Enumerations

#### Classes
- **NFCISO15693CustomCommandConfiguration**
- **NFCISO15693ReadMultipleBlocksConfiguration**
#### Structures
- **NFCFeliCaPollingResponse**
- **NFCFeliCaRequestSpecificationVersionResponse**
- **NFCFeliCaRequsetServiceV2Response**
- **NFCFeliCaStatusFlag**
- **NFCISO15693MultipleBlockSecurityStatus**
- **NFCISO15693SystemInfo**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreNFC)*
