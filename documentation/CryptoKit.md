# Apple CryptoKit

Perform cryptographic operations securely and efficiently.

**Platforms:** iOS 13.0+ | iPadOS 13.0+ | Mac Catalyst 15.0+ | macOS 10.15+ | tvOS 15.0+ | visionOS 1.0+ | watchOS 8.0+

## Overview

Use Apple CryptoKit to perform common cryptographic operations:

- Compute and compare cryptographically secure digests.

- Use public-key cryptography to create and evaluate digital signatures, and to perform key exchange. In addition to working with keys stored in memory, you can also use private keys stored in and managed by the Secure Enclave.

- Generate symmetric keys, and use them in operations like message authentication and encryption.

Prefer CryptoKit over lower-level interfaces. CryptoKit frees your app from managing raw pointers, and automatically handles tasks that make your app more secure, like overwriting sensitive data during memory deallocation.

## Topics

### Essentials
- [Complying with Encryption Export Regulations](https://developer.apple.com/documentation/cryptokit/complying_with_encryption_export_regulations) - Declare the use of encryption in your app to streamline the app submission process.
- [Performing Common Cryptographic Operations](https://developer.apple.com/documentation/cryptokit/performing_common_cryptographic_operations) - Use CryptoKit to carry out operations like hashing, key generation, and encryption.
- [Storing CryptoKit Keys in the Keychain](https://developer.apple.com/documentation/cryptokit/storing_cryptokit_keys_in_the_keychain) - Convert between strongly typed cryptographic keys and native keychain types.
- [Using the quantum-secure APIs](https://developer.apple.com/documentation/cryptokit/using_the_quantum-secure_apis) - Enhance your app's privacy and security by using quantum-secure workflows.

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
- **MLKEM768** - The Module-Lattice key encapsulation mechanism (KEM). (Beta)
- **MLKEM1024** - The Module-Lattice key encapsulation mechanism (KEM). (Beta)
- **XWingMLKEM768X25519** - The X-Wing (ML-KEM768 with X25519) Key Encapsulation Mechanism, defined in https://datatracker.ietf.org/doc/html/draft-connolly-cfrg-xwing-kem-06 (Beta)

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
- **SHA3_256Digest** - The output of a Secure Hashing Algorithm 3 (SHA-2) hash with a 256-bit digest.
- **SHA3_384** - An implementation of Secure Hashing Algorithm 3 (SHA-3) hashing with a 384-bit digest.
- **SHA3_384Digest** - The output of a Secure Hashing Algorithm 3 (SHA-2) hash with a 384-bit digest.
- **SHA3_512** - An implementation of Secure Hashing Algorithm 3 (SHA-3) hashing with a 512-bit digest.
- **SHA3_512Digest** - The output of a Secure Hashing Algorithm 3 (SHA-2) hash with a 512-bit digest.

### Type Aliases
- **CryptoKitMetaError**
- **SHA2_256** - An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 256-bit digest.
- **SHA2_384** - An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 384-bit digest.
- **SHA2_512** - An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 512-bit digest.

### Enumerations
- **MLDSA65** - The MLDSA65 Digital Signature Algorithm (Beta)
- **MLDSA87** - The MLDSA87 Digital Signature Algorithm (Beta)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CryptoKit)*