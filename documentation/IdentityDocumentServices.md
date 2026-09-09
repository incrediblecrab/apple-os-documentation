# IdentityDocumentServices

Share mobile documents using the Digital Credentials API.

**Platforms:** iOS 26.0+ | iPadOS 26.0+ | macOS 26.0+

Provider-registration documentation specifies iOS/iPadOS 26. The browser/raw-request validation APIs also declare macOS 26; the framework-level platform list does not make every provider operation a Mac API.

## Overview

Identity Document Services enables on-device document presentation and browser support for the Digital Credentials API. Once the person authorizes the provider, they can select the app during a document request and separately authorize disclosure in UI built with IdentityDocumentServicesUI.

This framework also enables web browsers to implement the presentment flow for the Digital Credentials API. With web browser support, a person can present identity documents locally on their device or remotely on another device using the same iCloud account. Identity documents can include documents such as a driver's license or identity card.

### Entitlement, registration, and consent

A provider needs [`com.apple.developer.identity-document-services.document-provider.mobile-document-types`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.identity-document-services.document-provider.mobile-document-types), an **array of strings** listing the mobile document types it supplies. Only register types allowed by that entitlement; use the appropriate standardized document type and namespaces.

Registration can fail when the person declines provider authorization. Inspect the registration store's current `status`, support later settings changes, and remove registrations for documents that are no longer available. An `invalidationDate` also affects whether a document remains eligible for presentation.

Provider authorization does **not** authorize every disclosure. Show the requesting origin and requested information, and call the response function only after explicit approval. Handle cancellation without releasing a document.

### Validate before disclosing

The provider guide distinguishes a system-parsed request for the authorization UI from the raw request released after interaction. Compare their consistency, validate the raw request's signatures and trusted certificate relationship, then build and encrypt the response using the documented ISO flow. The system's preliminary checks do not replace the provider's validation.

Do not log identity-document contents or broaden the disclosed fields after approval. Treat validation errors and revoked/unavailable documents as failures rather than returning an empty success response.

For the website side, the documented `navigator.credentials.get` request needs an explicit user interaction. After decrypting a response, validate issuer and device authentication before using its fields; possession of an encrypted response alone does not establish a trusted identity.

## Topics

### Essentials
- [Requesting a mobile document on the web](https://developer.apple.com/documentation/identitydocumentservices/requesting-a-mobile-document-on-the-web) - Build the ISO mdoc request, initiate a user-mediated browser flow, and validate the response on the server.
- [Implementing as an identity document provider](https://developer.apple.com/documentation/identitydocumentservices/implenting-as-an-identity-document-provider) - Register documents, obtain authorization, and validate presentation requests. Apple's published URL uses `implenting`.

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
- [IdentityDocumentPresentmentError](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentpresentmenterror) - A documented error from identity-document presentation.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/IdentityDocumentServices)*

*Changed-content source, reviewed September 8, 2026: [provider integration and authorization](https://developer.apple.com/documentation/identitydocumentservices/implenting-as-an-identity-document-provider.md).*
