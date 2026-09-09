# SecureElementCredential

Allow access to credentials inside the Secure Element on device.

**API availability:** `CredentialSession` and the base entitlement have iOS/iPadOS 18.1+ SDK declarations. Actual use depends on eligible hardware, region, and platform access; an SDK declaration alone is not a supported-device guarantee.

## Overview

The SecureElementCredential framework allows your app to manage and use Secure Element credentials with contactless transaction capabilities. See [NFC & SE Platform for secure contactless transactions](https://developer.apple.com/support/nfc-se-platform) for requirements, regional availability, and requesting platform access.

That program documents deployed support on eligible iPhone XS-or-later devices, with OS minimums varying by territory and use case. Card-emulation testing needs NFC reader hardware, not Simulator. For example, Government ID support has separate iOS 26.4 and EU/eligible-US-market conditions; the 18.1 SDK floor is not a universal rollout date.

Using this framework depends on having registered an applet bundle with the Apple Business Register (ABR). The applet contains the cryptographic code required to complete a transaction. You use this framework to provision your applet and its credentials, which downloads a bundle from the ABR and installs it into the Secure Element. Provisioning returns an instance of CredentialSession.Credential, which you use with your calls to the framework.

The CredentialSession class serves as the entry point to the framework. This class provides three major functions:

**Management**  
Allows your app to create, read, update, and delete credentials in the Secure Element.

**Wired actions**  
Allows your app to exchange data, given a credential, with an applet that corresponds to the credential.

**Card emulation**  
Allows the credential to communicate with a contactless reader.

The framework also provides SwiftUI and UIKit extensions that perform wired actions and card emulation while providing an appropriate user interface.

SecureElementCredential supports transactions for in-store payments, car keys, closed-loop transit, corporate badges, student IDs, home keys, hotel keys, merchant loyalty and rewards cards, and event tickets.

**Warning:** In any file that imports a symbol from this framework's SwiftUI extension, don't also import UIKit. Similarly, if you use this framework's UIKit extensions, don't also import SwiftUI in the same file. Importing SwiftUI and UIKit in the same file results in ambiguity during compilation.

### Eligibility, authorization, and failure handling

Check [`CredentialSession.isEligible`](https://developer.apple.com/documentation/secureelementcredential/credentialsession/iseligible) before starting a session. The Boolean `com.apple.developer.secure-element-credential` entitlement is separate from authorization for a particular transaction and from the additional default-contactless-app entitlement.

Start a session, confirm the intended credential is available, and use the documented transaction UI for user authentication. Handle cancellation, ineligible devices, unavailable credentials, provisioning errors, and invalid session states without treating a partially completed interaction as a successful transaction.

A presentment assertion is temporary. Relinquish it before transaction methods that acquire their own internal assertion, handle contention and timeout events, and invalidate sessions that are no longer needed. Owner-level credential maintenance is distinct from ordinary transaction authorization.

Only one credential session can be active per app. Backgrounding invalidates it after a short delay; in wired mode, 15 seconds without a `transceive(_:)` call also invalidates it.

### Published timing differences

The [integration guide](https://developer.apple.com/documentation/secureelementcredential/accessing-and-using-secure-element-credentials) describes a 15-second assertion and two acquisitions per 80 seconds. The current [`PresentmentIntentAssertion` reference](https://developer.apple.com/documentation/secureelementcredential/credentialsession/presentmentintentassertion) instead describes a 60-second window and a 15-second wait after relinquishing. The platform support article describes a 15-second lifetime and wait after expiry. These sources do not establish a single version-independent timer. Handle `presentmentIntentAssertionTimeout`, release, and acquisition errors rather than scheduling work on an assumed guaranteed duration.

## Topics

### Essentials
- [Accessing and using secure element credentials](https://developer.apple.com/documentation/secureelementcredential/accessing-and-using-secure-element-credentials) - Eligibility checks, session states, authentication, and temporary presentment assertions.

### Entitlements
- **com.apple.developer.secure-element-credential** - A Boolean value that indicates whether your app can use the SecureElementCredential framework.
- **com.apple.developer.secure-element-credential.default-contactless-app** - A Boolean value that indicates whether your app that uses the SecureElementCredential framework can become the default contactless app.

### Credentials
- **CredentialSession** - A class for performing actions on a credential stored in the Secure Element.

### Transactions
- **CredentialTransaction** - A transaction object for performing wired and contactless operations in SwiftUI views.

### UIKit scene delegate
- **CredentialSessionWindowSceneDelegate** - Notifies a UIKit scene of credential-session events. Its reference has an iOS/iPadOS 17.4 annotation, which does not lower the 18.1 requirement of `CredentialSession`.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SecureElementCredential)*

*Changed-content sources, reviewed September 8, 2026: [session integration](https://developer.apple.com/documentation/secureelementcredential/accessing-and-using-secure-element-credentials.md) and [CredentialSession availability](https://developer.apple.com/tutorials/data/documentation/secureelementcredential/credentialsession.json).*
