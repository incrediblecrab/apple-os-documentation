# IdentityDocumentServices

Share mobile documents using the Digital Credentials API.

**Platforms:** iOS 26.0+ | iPadOS 26.0+ | macOS 26.0+

## Overview

Identity Document Services enables the presentment of identity documents on device and web browser support for the Digital Credentials API. Once authorized, a person can select your app during a identity documents request, where they can authorize the presentment of identification through a UI you create with IdentityDocumentServicesUI.

This framework also enables web browsers to implement the presentment flow for the Digital Credentials API. With web browser support, a person can present identity documents locally on their device or remotely on another device using the same iCloud account. Identity documents can include documents such as a driver's license or identity card.

## Topics

### Essentials
- [Requesting a mobile document on the web](https://developer.apple.com/documentation/identitydocumentservices/requesting_a_mobile_document_on_the_web) - Send a request for mobile document information for apps installed on a device.
- [Implementing as an identity document provider](https://developer.apple.com/documentation/identitydocumentservices/implementing_as_an_identity_document_provider) - Add your app as an option for mobile document web presentment.

### Registering as an identity document provider
- **IdentityDocumentProviderRegistrationStore** - A store that notifies the system which documents an app has available for presentment.
- **IdentityDocumentRegistration** - A protocol that defines an identity document registration.
- **MobileDocumentRegistration** - A type you use to register mobile documents.

### Implementing the web presentment flow into your browser
- **IdentityDocumentWebPresentmentRawRequestValidator** - A type that contains functions for validating the incoming web presentment raw request.
- **IdentityDocumentWebPresentmentRequest** - A closed protocol that indicates that the system uses this object to perform an identity document web presentment
- **ISO18013MobileDocumentRequest** - A type that represents an incoming ISO 18013-5 mobile document request.
- **IdentityDocumentWebPresentmentResponse** - A closed protocol that indicates that the system uses this object to represent a web presentment response.
- **ISO18013MobileDocumentResponse** - A type representing the document response from a web presentment request.
- **IdentityDocumentWebPresentmentRawRequest** - A struct that defines the type that represents a raw web presentment request.

### Errors
- **IdentityDocumentWebPresentmentError** - An error type thrown from the identity document web presentment controller.

### Deprecated

### Structures
- **IdentityDocumentPresentmentError** - An error type that is thrown from the identity document web presentment controller.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/IdentityDocumentServices)*