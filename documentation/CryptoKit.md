# Apple CryptoKit

Perform cryptographic operations securely and efficiently.

**Framework catalog:** iOS 13.0+ | iPadOS 13.0+ | Mac Catalyst 15.0+ | macOS 10.15+ | tvOS 15.0+ | visionOS 1.0+ | watchOS 8.0+. This catalog is not the earliest availability of every symbol: for example, `SHA256` has Catalyst 13.0, tvOS 13.0, and watchOS 6.0 declaration annotations.

## Overview

Use Apple CryptoKit to perform common cryptographic operations:

- Compute and compare cryptographically secure digests.

- Use public-key cryptography to create and evaluate digital signatures, and to perform key exchange. In addition to working with keys stored in memory, you can also use private keys stored in and managed by the Secure Enclave.

- Generate symmetric keys, and use them in operations like message authentication and encryption.

Prefer CryptoKit over lower-level interfaces. CryptoKit frees your app from managing raw pointers, and automatically handles tasks that make your app more secure, like overwriting sensitive data during memory deallocation.

## Topics

### Essentials
- [Complying with Encryption Export Regulations](https://developer.apple.com/documentation/security/complying-with-encryption-export-regulations) - Declare the use of encryption in your app to streamline the app submission process.
- [Performing Common Cryptographic Operations](https://developer.apple.com/documentation/cryptokit/performing-common-cryptographic-operations) - Use CryptoKit to carry out operations like hashing, key generation, and encryption.
- [Storing CryptoKit Keys in the Keychain](https://developer.apple.com/documentation/cryptokit/storing-cryptokit-keys-in-the-keychain) - Convert between strongly typed cryptographic keys and native keychain types.
- [Enhancing your app's privacy and security with quantum-secure workflows](https://developer.apple.com/documentation/cryptokit/enhancing-your-app-s-privacy-and-security-with-quantum-secure-workflows) - Compare the documented hybrid encryption, key-encapsulation, and signature workflows.

### Cryptographically Secure Hashes
- **HashFunction** - A type that performs cryptographically secure hashing.
- **SHA512** - An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 512-bit digest.
- **SHA384** - An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 384-bit digest.
- **SHA256** - An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 256-bit digest.

### Message Authentication Codes
- **HMAC** - A hash-based message authentication algorithm.
- **SymmetricKey** - A symmetric cryptographic key.
- **SymmetricKeySize** - The sizes that a symmetric cryptographic key can take.

### Ciphers
- **AES** - A container for Advanced Encryption Standard (AES) ciphers.
- **ChaChaPoly** - An implementation of the ChaCha20-Poly1305 cipher.

### Public Key Cryptography
- **Curve25519** - An elliptic curve that enables X25519 key agreement and Ed25519 signatures.
- **P521** - An elliptic curve that enables NIST P-521 signatures and key agreement.
- **P384** - An elliptic curve that enables NIST P-384 signatures and key agreement.
- **P256** - An elliptic curve that enables NIST P-256 signatures and key agreement.
- **SharedSecret** - A key agreement result from which you can derive a symmetric cryptographic key.
- **SecureEnclave** - A representation of a device's hardware-based key manager.
- **HPKE** - A container for hybrid public key encryption (HPKE) operations.

### Key Derivation Functions
- **HKDF** - A standards-based implementation of an HMAC-based Key Derivation Function (HKDF).

### Key Encapsulation Mechanisms (KEM)
- **KEM** - A key encapsulation mechanism.
- **MLKEM768** - A Module-Lattice key encapsulation mechanism.
- **MLKEM1024** - A Module-Lattice key encapsulation mechanism.
- [XWingMLKEM768X25519](https://developer.apple.com/documentation/cryptokit/xwingmlkem768x25519) - A hybrid key encapsulation mechanism combining ML-KEM768 and X25519.

### KEM Keys
- **KEMPrivateKey** - The private key for a key encapsulation mechanism.
- **KEMPublicKey** - The public key for a key encapsulation mechanism.

### Errors
- **CryptoKitError** - General cryptography errors used by CryptoKit.
- **CryptoKitASN1Error** - Errors from decoding ASN.1 content.

### Legacy Algorithms
- **Insecure** - A container for older, cryptographically insecure algorithms.

### Protocols
- **DiffieHellmanKeyAgreement** - A Diffie-Hellman Key Agreement Key
- **HPKEDiffieHellmanPrivateKey** - A type that represents the private key in a Diffie-Hellman key exchange.
- **HPKEDiffieHellmanPrivateKeyGeneration** - A type that represents the generation of private keys in a Diffie-Hellman key exchange.
- **HPKEDiffieHellmanPublicKey** - A type that represents the public key in a Diffie-Hellman key exchange.
- **HPKEKEMPrivateKey** - A type that represents the private key in HPKE.
- **HPKEKEMPrivateKeyGeneration** - A type that represents the generation of private keys in HPKE
- **HPKEKEMPublicKey** - A type that represents the public key in HPKE
- **HPKEPublicKeySerialization** - A type that HPKE uses to encode the public key.

### Structures
- **CorecryptoCurveType**
- **SHA3_256** - An implementation of Secure Hashing Algorithm 3 (SHA-3) hashing with a 256-bit digest.
- **SHA3_256Digest** - The 256-bit output of SHA3-256.
- **SHA3_384** - An implementation of Secure Hashing Algorithm 3 (SHA-3) hashing with a 384-bit digest.
- **SHA3_384Digest** - The 384-bit output of SHA3-384.
- **SHA3_512** - An implementation of Secure Hashing Algorithm 3 (SHA-3) hashing with a 512-bit digest.
- **SHA3_512Digest** - The 512-bit output of SHA3-512.

### Type Aliases
- **CryptoKitMetaError**
- **SHA2_256** - An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 256-bit digest.
- **SHA2_384** - An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 384-bit digest.
- **SHA2_512** - An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 512-bit digest.

### Enumerations
- **MLDSA65** - A Module-Lattice digital signature algorithm.
- **MLDSA87** - A Module-Lattice digital signature algorithm.

### Availability and key handling

Check each symbol's minimum version rather than applying this framework's historical minimum to every algorithm. For example, `XWingMLKEM768X25519` and the SHA-3 digest types are 26.0-generation APIs, not new 27-only additions.

Keep private keys and shared secrets out of logs, use the documented serialization and keychain interfaces, and handle key-generation, decoding, and authentication failures. An authentication failure must not be treated as successfully decrypted data.

The keychain sample distinguishes NIST keys that map to `SecKey` from key types stored as generic-password data. A Secure Enclave key's exported representation is a device-bound encrypted block, not an export of its raw private key.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CryptoKit)*
