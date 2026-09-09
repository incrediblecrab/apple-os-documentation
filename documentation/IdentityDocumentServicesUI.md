# IdentityDocumentServicesUI

Provide an interface so people can present mobile documents.

**Platforms:** iOS 26.0+ | iPadOS 26.0+ | macOS 26.0+

## Overview

IdentityDocumentServicesUI has two roles: a document-provider extension presents authorization UI, and a browser uses a web-presentment controller for Digital Credentials API requests. [IdentityDocumentServices](IdentityDocumentServices.md) manages document registration and request/response data.

Provider and request-scene declarations list iOS/iPadOS 26. The browser controller additionally lists macOS 26. Their Catalyst metadata entries supply no introduction version, so don't derive a Catalyst deployment minimum from them.

A provider must declare its mobile document types in the [Mobile Document Provider entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.identity-document-services.document-provider.mobile-document-types), register eligible documents, and obtain the person's authorization. Only send a document after explicit approval in the authorization UI. The provider guide also requires comparing the parsed and raw requests, validating signatures and trust, and constructing an encrypted response; presenting system UI doesn't replace those checks.

## Topics

### Building identity document provider authorization UI
- [Implementing as an identity document provider](https://developer.apple.com/documentation/identitydocumentservices/implenting-as-an-identity-document-provider) - Configure registration, authorization UI, and response validation.
- [`IdentityDocumentProvider`](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentprovider) - An `AppExtension` protocol for the provider's authorization interface.
- [`IdentityDocumentRequestScene`](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentrequestscene) - An `AppExtensionScene` protocol with framework-provided request-specific implementations.
- [`ISO18013MobileDocumentRequestScene`](https://developer.apple.com/documentation/identitydocumentservicesui/iso18013mobiledocumentrequestscene) - A concrete scene whose SwiftUI content conforms to `View` and `Sendable`.
- [`ISO18013MobileDocumentRequestContext`](https://developer.apple.com/documentation/identitydocumentservicesui/iso18013mobiledocumentrequestcontext) - Supplies the parsed request, requesting website origin, response operation, and cancellation.
- [`IdentityDocumentRequestSceneBuilder`](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentrequestscenebuilder) - Combines request scenes.

### Implementing the web presentment flow into your browser
- [`IdentityDocumentWebPresentmentController`](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentwebpresentmentcontroller) - A main-actor controller for identity document requests originating from the web.
- [`IdentityDocumentWebPresentmentControllerDelegate`](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentwebpresentmentcontrollerdelegate) - Its class-bound delegate protocol.
- [`IdentityDocumentPresentmentControllerPresentationContextProviding`](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentpresentmentcontrollerpresentationcontextproviding) - Provides the presentation context.
- [`IdentityDocumentPresentationAnchor`](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentpresentationanchor) - The presentation anchor type used by the controller.
- [`IdentityDocumentPresentmentControlling`](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentpresentmentcontrolling) - A closed protocol adopted by the framework's presentment controller.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/IdentityDocumentServicesUI)*
