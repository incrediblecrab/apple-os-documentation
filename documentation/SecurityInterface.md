# Security Interface

Provide user interface elements for security features such as authorization, access to digital certificates, and access to items in keychains.

**Platforms:** macOS 10.3+

## Overview

**Note:** This document was previously titled Security Objective-C API. The documentation for the SFAuthorization class is now in a separate document, Security Foundation.

The Security Interface framework is a set of Objective-C classes that provide user interface elements for programs that implement security features such as authorization, access to digital certificates, and access to items in keychains.

## Topics

### Classes
- **SFAuthorizationPluginView** - Allows authorization plug-in developers to create a custom view their plug-in can display.
- **SFAuthorizationView** - The class responsible for displaying a lock icon that can be used to indicate that a user interface has restricted access.
- **SFCertificatePanel** - A panel or sheet that displays one or more certificates.
- **SFCertificateTrustPanel** - A panel or sheet that lets the user edit the trust settings in any of the certificates in a certificate chain.
- **SFCertificateView** - A view that displays the contents of a certificate, with options to display certificate details, display trust settings, and allow users to edit a certificate's trust settings.
- **SFChooseIdentityPanel** - A panel or sheet containing a list of identities that a user can choose from.
- **SFChooseIdentityTableCellView**
- **SFKeychainSavePanel** - A panel or sheet that allows the user to create a keychain.
- **SFKeychainSettingsPanel** - A panel or sheet that allows users to change their keychain settings.

### Reference
- **SFAuthorizationViewState** - Defines the current state of the authorization view.
- **SFButtonType** - These constants define the button types used by authorization plug-ins.
- **SFViewType** - These constants define the view type requested by the authorization plug-in.
- **SecurityInterface Constants** - Constants in the SecurityInterface framework.
- **SecurityInterface Data Types** - Data types found in the Security Interface framework.
- **SecurityInterface Enumerations**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SecurityInterface)*