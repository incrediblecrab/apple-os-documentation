# CryptoTokenKit

Access security tokens and the cryptographic assets they store.

**Framework catalog:** iOS 13.0+ | iPadOS 13.0+ | macOS 10.10+ | tvOS 13.0+ | visionOS 1.0+ | watchOS 8.0+. Smart-card classes use Mac Catalyst 13.1, not the catalog's 13.0 label; some individual slot APIs also have earlier iOS/tvOS/watchOS annotations.

## Overview

You use the CryptoTokenKit framework to easily access cryptographic tokens. Tokens are physical devices built in to the system, located on attached hardware (like a smart card), or accessible through a network connection. Tokens store cryptographic objects like keys and certificates. They also may perform operations—for example, encryption or digital signature verification—using these objects. You use the framework to work with a token's assets as if they were part of your system, even though they remain secured by the token.

You can also use the framework to enable a token for two-factor authentication in macOS. Authentication services manage associations between users and identities stored on a token, granting users access when the appropriate token is present and unlocked. You supply a token driver in the form of an app extension that bridges the gap between authentication services and the underlying token hardware.

Starting in macOS 10.15.4, the CryptoTokenKit framework includes support for always-available tokens, referred to as persistent tokens. Persistent token support provides access to tokens from Hardware Security Modules (HSMs). The app hosting the token extension allows the system to address and use available tokens, address and use identities available by accessing tokens, and to access additional configuration information about tokens. Persistent tokens aren't suitable for validating a user login because they're available on a per-user basis, and therefore aren't accessible until after the user logs in.

**Note:** When you want to manage the associations between users and tokens on a given computer, use the sc_auth command line utility. See the sc_auth(8) man page for details.

### Access and token lifetime

`TKSmartCardSlotManager` requires the Boolean [`com.apple.security.smartcard`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.smartcard) entitlement with value `true`; without it, the default slot manager is `nil`. This privilege is not successful PIN authentication or a guarantee that a slot or token is present.

Observe token insertion and removal with `TKTokenWatcher`. A persistent keychain reference is not permanent access: after removal, token-item operations can return `errSecItemNotFound`. Handle cancellation, authentication failure, missing objects, and missing tokens. NFC session operations also fail after their slot disappears through cancellation, timeout, or session termination.

## Topics

### Smart Cards
- [Using Cryptographic Assets Stored on a Smart Card](https://developer.apple.com/documentation/cryptotokenkit/using-cryptographic-assets-stored-on-a-smart-card) - Access certificates, keys, and identities stored on a smart card as if they were part of the keychain.
- **TKSmartCardSlotManager** - An interface to all available smart card reader slots.
- **TKSmartCardSlot** - A single smart card reader slot in the system.
- **TKSmartCard** - A representation of a smart card.

### Smart Card App Extensions
- [Authenticating Users with a Cryptographic Token](https://developer.apple.com/documentation/cryptotokenkit/authenticating-users-with-a-cryptographic-token) - Implement a macOS token extension for supported authentication operations.
- [Configuring Smart Card Authentication](https://developer.apple.com/documentation/cryptotokenkit/configuring-smart-card-authentication) - Configure the macOS authentication preferences and their managed/system/default precedence.
- **TKSmartCardTokenDriver** - The driver that acts as an entry point for smart card app extensions.
- **TKSmartCardToken** - A representation of a smart card based cryptographic token.
- **TKSmartCardTokenSession** - A token session that is based on a smart card token.

### Tokens
- **TKTokenWatcher** - An object that tracks the tokens available in the system.
- **TKTokenDriver** - A base class for building token drivers.
- **TKToken** - A representation of a hardware-based cryptographic token.
- **TKTokenSession** - A token session that manages the authentication state of a token.

### Errors
- **TKError** - An error specific to the CryptoTokenKit framework.
- **TKErrorDomain** - The domain for all CryptoTokenKit framework errors.
- **TKError.Code** - Error codes from CryptoTokenKit.

### Classes
- **TKSmartCardSlotNFCSession** - An NFC session tied to a smart-card slot; its SDK declarations begin at iOS/iPadOS/Catalyst/visionOS 26.
- **TKSmartCardTokenRegistrationManager** - Registers and unregisters smart cards using token IDs; its SDK declarations begin at iOS/iPadOS/Catalyst/visionOS 26.

### Type Aliases
- [TKTokenObjectID](https://developer.apple.com/documentation/cryptotokenkit/tktokenobjectid-8mo7f) - The legacy `AnyObject` alias, introduced in macOS 10.12 and deprecated in 10.15.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CryptoTokenKit)*
