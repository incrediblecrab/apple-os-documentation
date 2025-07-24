# CryptoTokenKit

Access security tokens and the cryptographic assets they store.

**Platforms:** iOS 13.0+ | iPadOS 13.0+ | Mac Catalyst 13.0+ | macOS 10.10+ | tvOS 13.0+ | visionOS 1.0+ | watchOS 8.0+

## Overview

You use the CryptoTokenKit framework to easily access cryptographic tokens. Tokens are physical devices built in to the system, located on attached hardware (like a smart card), or accessible through a network connection. Tokens store cryptographic objects like keys and certificates. They also may perform operations—for example, encryption or digital signature verification—using these objects. You use the framework to work with a token's assets as if they were part of your system, even though they remain secured by the token.

You can also use the framework to enable a token for two-factor authentication in macOS. Authentication services manage associations between users and identities stored on a token, granting users access when the appropriate token is present and unlocked. You supply a token driver in the form of an app extension that bridges the gap between authentication services and the underlying token hardware.

Starting in macOS 10.15.4, the CryptoTokenKit framework includes support for always-available tokens, referred to as persistent tokens. Persistent token support provides access to tokens from Hardware Security Modules (HSMs). The app hosting the token extension allows the system to address and use available tokens, address and use identities available by accessing tokens, and to access additional configuration information about tokens. Persistent tokens aren't suitable for validating a user login because they're available on a per-user basis, and therefore aren't accessible until after the user logs in.

**Note:** When you want to manage the associations between users and tokens on a given computer, use the sc_auth command line utility. See the sc_auth(8) man page for details.

## Topics

### Smart Cards
- [Using Cryptographic Assets Stored on a Smart Card](https://developer.apple.com/documentation/cryptotokenkit/using_cryptographic_assets_stored_on_a_smart_card) - Access certificates, keys, and identities stored on a smart card as if they were part of the keychain.
- **TKSmartCardSlotManager** - An interface to all available smart card reader slots.
- **TKSmartCardSlot** - A single smart card reader slot in the system.
- **TKSmartCard** - A representation of a smart card.

### Smart Card App Extensions
- [Authenticating Users with a Cryptographic Token](https://developer.apple.com/documentation/cryptotokenkit/authenticating_users_with_a_cryptographic_token) - Grant access to user accounts and the keychain by creating a smart card app extension.
- [Configuring Smart Card Authentication](https://developer.apple.com/documentation/cryptotokenkit/configuring_smart_card_authentication) - Set preferences for smart card authentication operations, including those on managed devices.
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
- **Code** - Error codes from CryptoTokenKit.

### Classes
- **TKSmartCardSlotNFCSession** - NFC session that's related to NFC smart card slot which was created. (Beta)
- **TKSmartCardTokenRegistrationManager** - Provides a centralized management system for registering and unregistering smartcards using their token IDs. (Beta)

### Type Aliases
- **TKTokenObjectID** - (Deprecated)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CryptoTokenKit)*