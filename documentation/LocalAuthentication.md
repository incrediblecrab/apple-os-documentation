# Local Authentication

Authenticate users biometrically or with a passphrase they already know.

**Framework availability:** iOS 8.0+ | iPadOS 8.0+ | Mac Catalyst 13.1+ | macOS 10.10+ | visionOS 1.0+. The framework catalog lists watchOS 9, while individual `LAContext` declarations date to watchOS 3; check the policy and symbol rather than treating the catalog as a uniform minimum.

## Overview
Many users rely on biometric authentication like Face ID, Touch ID, or Optic ID to enable secure, effortless access to their devices. As a fallback option, and for devices without biometry, a passcode or password serves a similar purpose. Use the LocalAuthentication framework to leverage these mechanisms in your app and extend authentication procedures your app already implements.

Your app receives an authentication result and, when appropriate, error information—not fingerprint images or other biometric templates. Specify an authentication policy and a clear reason for the request; the framework manages the authentication interaction and verification.

### Policy, failure, and context lifetime

Include `NSFaceIDUsageDescription` when using Face ID and provide a meaningful localized reason for authentication. [`canEvaluatePolicy(_:error:)`](https://developer.apple.com/documentation/localauthentication/lacontext/canEvaluatePolicy(_:error:)) checks whether a policy can be evaluated; it does **not** authenticate the person.

Do not cache that eligibility result or call `canEvaluatePolicy` from an `evaluatePolicy` reply block; the latter can deadlock.

Only unlock the protected operation after the evaluation succeeds. Handle unavailable or unenrolled biometry, lockout, cancelled interaction, and evaluation errors. A passcode fallback depends on the chosen policy; a failed biometric-only policy does not silently authorize another method.

Invalidate an [`LAContext`](https://developer.apple.com/documentation/localauthentication/lacontext) when its protected workflow ends or is cancelled. Invalidation cancels pending evaluation with `LAError.Code.appCancel`, and that context cannot evaluate again; create a new context for a later workflow. Do not treat one success as permanent authorization. For secrets, consider keychain access controls so protection applies to retrieval, not just a Boolean flag in the UI.

The right-based APIs begin at iOS/iPadOS/Catalyst 16 and macOS 13, with visionOS 1 support. The SwiftUI `LocalAuthenticationView` below is specifically a macOS 13-or-later view, not a cross-platform replacement for `LAContext`.

## Topics

### Essentials
- [Logging a User into Your App with Face ID or Touch ID](https://developer.apple.com/documentation/localauthentication/logging-a-user-into-your-app-with-face-id-or-touch-id) - Supplement your own authentication scheme with biometric authentication, making it easy for users to access sensitive parts of your app.
- [Accessing Keychain Items with Face ID or Touch ID](https://developer.apple.com/documentation/localauthentication/accessing-keychain-items-with-face-id-or-touch-id) - Protect a keychain item with biometric authentication.
### Authentication and access
- **LARight** - A grouped set of requirements that gate access to a resource or operation.
- **LARight.State** - The possible states for a right during authorization.
- **LAContext** - A mechanism for evaluating authentication policies and access controls.
### Persistence
- **LARightStore** - A container for data protected by a right.
- **LAPersistedRight** - A right that gates access to a key and a secret.
- **LASecret** - Data that's protected by a persisted right.
### Key pairs
- **LAPublicKey** - The public portion of an asymmetric key pair.
- **LAPrivateKey** - The private portion of an asymmetric key pair.
### Requirements
- **LAAuthenticationRequirement** - A set of requirements that protect a right.
- **LABiometryFallbackRequirement** - A set of requirements to fall back on if biometrics aren't present.
### Authentication views
- **LocalAuthenticationView** - A macOS 13-or-later SwiftUI view that displays an authentication interface.
### Errors
- **LAError** - Errors issued by the LocalAuthentication framework.
- **LAError.Code** - Errors issued by the LocalAuthentication framework.
- **LAErrorDomain** - The error domain that the framework uses when issuing errors.
### Reference
- **LocalAuthentication Constants**

### Classes

The domain-state types begin at iOS/iPadOS/Catalyst 18 and macOS 15. `LAEnvironment` also has visionOS 2 and watchOS 11 declarations; these are not part of the original iOS 8 API surface.

- **LADomainState**
- **LADomainStateBiometry**
- **LADomainStateCompanion**
- **LAEnvironment**
### Variables
- **kLAAccessControlOperationCreateItem** - Int32
- **kLAAccessControlOperationCreateKey** - Int32
- **kLAAccessControlOperationUseItem** - Int32
- **kLAAccessControlOperationUseKeyDecrypt** - Int32
- **kLAAccessControlOperationUseKeyKeyExchange** - Int32
- **kLAAccessControlOperationUseKeySign** - Int32
- **kLACompanionTypeMac** - Int32
- **kLACompanionTypeNone** - Int32
- **kLACompanionTypeVision** - Int32
- **kLACompanionTypeWatch** - Int32

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/LocalAuthentication)*

*Changed-content source, reviewed September 8, 2026: [LAContext](https://developer.apple.com/documentation/localauthentication/lacontext.md).*
