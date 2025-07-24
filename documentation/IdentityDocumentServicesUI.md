# IdentityDocumentServicesUI

Provide an interface so people can present mobile documents.

**Platforms:** iOS 26.0+ (Beta) | iPadOS 26.0+ (Beta) | macOS 26.0+ (Beta)

## Overview

The IdentityDocumentServicesUI framework contains user-interface objects that support the features in IdentityDocumentServices. This includes types for implementing authorization UI for an IdentityDocumentProvider app. It also includes a controller to enable browsers to implement the Digital Credentials API.

## Topics

### Building identity document provider authorization UI
- **IdentityDocumentProvider** - An app extension that provides an identity document.
- **IdentityDocumentRequestScene** - A scene that indicates support for a specific document request type.
- **ISO18013MobileDocumentRequestScene**
- **ISO18013MobileDocumentRequestContext** - An object that contains details about the ISO 18013 mobile document request.
- **IdentityDocumentRequestSceneBuilder** - A result builder that combines one or more IdentityDocumentRequestScenes into a single scene.

### Implementing the web presentment flow into your browser
- [Implementing as an identity document provider](https://developer.apple.com/documentation/identitydocumentservicesui/implementing_as_an_identity_document_provider) - Add your app as an option for mobile document web presentment.
- **IdentityDocumentWebPresentmentController** - A controller that performs identity document requests originating from the web.
- **IdentityDocumentWebPresentmentControllerDelegate** - Defines a delegate that the system uses in conjunction with a web presentment controller.
- **IdentityDocumentPresentmentControllerPresentationContextProviding** - An interface the controller uses to receive a presentation context.
- **IdentityDocumentPresentationAnchor** - The presentation anchor the system uses to present your app UI.
- **IdentityDocumentPresentmentControlling** - A closed protocol that indicates this object is a controller that the system uses for identity document presentment.

---

> **Beta Software:** This documentation contains preliminary information about an API or technology in development. This information is subject to change, and software implemented according to this documentation should be tested with final operating system software.

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/IdentityDocumentServicesUI)*