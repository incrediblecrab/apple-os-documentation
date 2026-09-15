# Security

Secure the data your app manages, and control access to your app.

**Framework catalog:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 13.0+ | macOS 10.0+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 2.0+. These historical catalog values are not the minimums of every listed function; for example, `SecIdentityCreate` has a Catalyst 13.1 declaration.

## Overview

Use the Security framework to protect information, establish trust, and control access to software. Broadly, security services support these goals:

- Establish a user's identity (authentication) and then selectively grant access to resources (authorization).
- Secure data, both on disk and in motion across a network connection.
- Ensure the validity of code to be executed for a particular purpose.

Prefer system cryptographic implementations over designing your own. Use [CryptoKit](CryptoKit.md) for its supported cryptographic operations, and Security for facilities such as keychain storage, certificate trust, and code-signing checks.

**Note:** Use the highest-level networking API that meets your needs. Prefer Foundation's URL Loading System for HTTP and URL resources, and [Network](Network.md) when direct transport access is required. The Secure Transport entry below is a legacy reference, not the recommended starting point for a new networking implementation.

### OS 27: stricter TLS for selected system processes

**Reviewed September 8, 2026:** The 27 release notes tighten network security for system processes involved in **MDM, Declarative Device Management (DDM), Automated Device Enrollment, configuration-profile installation, app installation, and software updates**. This is not a statement that every app network call has acquired the same new policy.

Servers used by those workflows must support **TLS 1.2 or later** and ATS-compliant cipher suites and certificates. Apple's deployment guidance recommends TLS 1.3; TLS 1.2 configurations need ECDHE, AES-GCM with a SHA-256-or-stronger pseudorandom function, and the Extended Master Secret extension. Certificates must pass the applicable trust checks, including hostname and validity checks, appropriate trust anchors, minimum RSA 2048-bit or ECC 256-bit signing keys, and SHA-256-or-stronger signatures. The stricter checks also reject certificate signature algorithms not offered by the client.

Apple explicitly excludes SCEP-server connections used while installing a profile or resolving a DDM asset, and content-caching-server connections, from this change. Consult [Prepare your network environment for stricter security requirements](https://support.apple.com/en-us/126655) for the exact scope, certificate-anchor nuances, and diagnostics.

For the specific default-server-trust warning, that article says remediation is unnecessary if the certificate is in the auto-enrollment profile's anchor certificates. This is not a blanket exception to the other cipher, signature, or key-size requirements.

Audit representative enrollment, installation, and update workflows on 26.4-or-later test devices, then verify behavior on 27. A blocked early connection can hide later failures. Fix the affected server configuration rather than adding broad exceptions to an unrelated app.

### App networking remains API-specific

[App Transport Security](https://developer.apple.com/documentation/security/preventing-insecure-network-connections) applies to the standard URL Loading System. Apple explicitly distinguishes lower-level Network and CFNetwork calls, where the app is responsible for connection security.

[`NSRequiresNIAPTLSPackageVersion`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsrequiresniaptlspackageversion) is a **string-valued, opt-in** ATS configuration introduced in the 26.4 generation, not a switch that OS 27 silently enables for every app. Its documented values are `none`, `FCP_v2.1`, and `recommended`. Place it inside `NSAppTransportSecurity` if the app needs that additional compliance mode.

## Topics

### Essentials
- **Security updates** - Learn about important changes to Security.

### Authorization and authentication
- **Password AutoFill** - Streamline your app's login and onboarding procedures.
- **Shared Web Credentials** - Share credentials between iOS apps and their website counterparts.
- **Authorization Services** - Access restricted areas of the operating system, and control access to particular features of your macOS app.
- **Authorization Plug-ins** - Extend the authorization services API by creating plug-ins that can participate in authorization decisions.
- **Sessions** - Manage login, authorization, and security sessions in macOS.
- **One-time codes** - Streamline entry of authentication and recovery codes.

### Secure data
- **Keychain services** - Securely store small chunks of data on behalf of the user.
- [Preventing Insecure Network Connections](https://developer.apple.com/documentation/security/preventing-insecure-network-connections) - Understand ATS scope, certificate requirements, and server remediation.

### Secure code
- **Code Signing Services** - Examine and validate signed code running on the system.
- [Notarizing macOS software before distribution](https://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution) - Give users even more confidence in your macOS software by submitting it to Apple for notarization.
- [Preparing your app to work with pointer authentication](https://developer.apple.com/documentation/security/preparing-your-app-to-work-with-pointer-authentication) - Test your app against the arm64e architecture to ensure that it works seamlessly with enhanced security features.
- **App Sandbox** - Restrict access to system resources and user data in macOS apps to contain damage if an app becomes compromised.
- **Hardened Runtime** - Manage security protections and resource access for your macOS apps.
- [Disabling and Enabling System Integrity Protection](https://developer.apple.com/documentation/security/disabling-and-enabling-system-integrity-protection) - Disable system protections only temporarily during development to test drivers, kernel extensions, and other low-level code.
- [Using the latest code signature format](https://developer.apple.com/documentation/xcode/using-the-latest-code-signature-format) - Update legacy app code signatures so your app runs on current OS releases.
- [Updating Mac Software](https://developer.apple.com/documentation/security/updating-mac-software) - Implement Mac software updates without causing code-signing crashes.
- [TN3125: Inside Code Signing: Provisioning Profiles](https://developer.apple.com/documentation/technotes/tn3125-inside-code-signing-provisioning-profiles) - Learn how provisioning profiles enable third-party code to run on Apple platforms.

### Launch environment constraints
- [Applying launch environment and library constraints](https://developer.apple.com/documentation/security/applying-launch-environment-and-library-constraints) - Limit the libraries your process loads, and the situations where it runs.
- [Defining launch environment and library constraints](https://developer.apple.com/documentation/security/defining-launch-environment-and-library-constraints) - Restrict your app's components to their expected contexts.
- [Constraining a tool's launch environment](https://developer.apple.com/documentation/security/constraining-a-tool's-launch-environment) - Improve the security of your macOS app by limiting the ways its components can run.

### Cryptography
- [Complying with Encryption Export Regulations](https://developer.apple.com/documentation/security/complying-with-encryption-export-regulations) - Declare the use of encryption in your app to streamline the app submission process.
- **Certificate, Key, and Trust Services** - Establish trust using certificates and cryptographic keys.
- **Cryptographic Message Syntax Services** - Cryptographically sign and encrypt S/MIME messages.
- **Randomization Services** - Generate cryptographically secure random numbers.
- **Security Transforms** - A legacy Mac transform interface. Its `SecTransformExecute` API was deprecated in macOS 12 with the message that SecTransform is no longer supported; prefer supported modern cryptographic APIs.
- **ASN.1** - Encode and decode Distinguished Encoding Rules (DER) and Basic Encoding Rules (BER) data streams.

### Result codes
- **Security Framework Result Codes** - Evaluate result codes common to many Security framework functions.

### Legacy interfaces
- **Common Security Services Manager** - A set of open source modules underpinning the legacy implementation of the Security framework.
- **Secure Transport** - Secure network communication using standardized transport layer security mechanisms.
- **Secure Download** - Implement Apple's Secure Download System in macOS.
- **Security legacy reference** - Learn about legacy APIs.

### Reference
- **Security Structures**
- **Security Constants**
- **Security Functions**
- **Security Data Types**

### Variables
- **TLS_ECDHE_PSK_WITH_CHACHA20_POLY1305_SHA256: SSLCipherSuite**
- **errSecMissingQualifiedCertStatement: OSStatus**
- **kSecPolicyAppleEAPClient: CFString**
- **kSecPolicyAppleEAPServer: CFString**
- **kSecPolicyAppleIPSecClient: CFString**
- **kSecPolicyAppleIPSecServer: CFString**
- **kSecPolicyAppleSSLClient: CFString**
- **kSecPolicyAppleSSLServer: CFString**
- **kSecTrustQCStatements: CFString**
- **kSecTrustQWACValidation: CFString**

### Functions

`SecIdentityCreate` dates to iOS/iPadOS/tvOS 11.2, Catalyst 13.1, macOS 10.12, watchOS 4.2, and visionOS 1. The two metadata-copy functions are later: iOS/iPadOS/Catalyst/tvOS 18.5, macOS 15.5, watchOS 11.5, and visionOS 2.5.

- **SecIdentityCreate(CFAllocator?, SecCertificate, SecKey) -> SecIdentity?**
- **sec_protocol_metadata_copy_negotiated_protocol(sec_protocol_metadata_t) -> UnsafePointer<CChar>?**
- **sec_protocol_metadata_copy_server_name(sec_protocol_metadata_t) -> UnsafePointer<CChar>?**

### Type Aliases
- **CE_DataType**
- **CE_ExtendedKeyUsage**
- **CE_GeneralNameType**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Security)*

*Changed-content sources: [iOS/iPadOS 27 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes.md), [macOS 27 release notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes.md), [deployment audit guidance](https://support.apple.com/en-us/126655), and [ATS documentation](https://developer.apple.com/documentation/security/preventing-insecure-network-connections.md).*
