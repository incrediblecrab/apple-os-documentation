# Authentication Services

Make it easy for users to log into apps and services.

**Platforms:** iOS 12.0+ | iPadOS 12.0+ | Mac Catalyst 13.1+ | macOS 10.15+ | tvOS 13.0+ | visionOS 1.0+ | watchOS 6.0+. Individual authorization and credential APIs have later minimums.

## Overview

Use the Authentication Services framework to improve the experience of users when they enter credentials to establish their identity.

- Give users the ability to sign into your services with their Apple Account.
- Enable users to look up their stored passwords from within the sign-in flow of an app.
- Provide a passwordless registration and authentication workflow for apps and websites using iCloud Keychain or a physical security key.
- Perform automatic security upgrades from weak to strong passwords, or upgrade to using Sign in with Apple.
- Share data between an app and a web browser using technologies like OAuth to leverage existing web-based logins in the app.
- Create a single sign-on (SSO) experience in an enterprise app.

Simple and straightforward sign-up and sign-in flows reduce the burden on the user to remember passwords, which may improve security.

### Authorization and credential lifetime

Handle authorization cancellation and errors separately from successful credential delivery. Presenting a sheet or receiving an account identifier is not enough to establish a verified server session. For Sign in with Apple, follow [identity-token verification](https://developer.apple.com/documentation/signinwithapple/verifying-a-user), including signature, issuer, audience, nonce, and expiry checks.

Check [`getCredentialState(forUserID:completion:)`](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidprovider/getCredentialState(forUserID:completion:)) when restoring a Sign in with Apple session. A revoked or missing credential must not preserve authenticated access. Account deletion does not necessarily produce a credential-revoked notification, so do not rely on that notification alone.

Capabilities and configuration are provider-specific: Sign in with Apple, associated-domain passkey flows, credential-provider extensions, and enterprise SSO have different requirements. Guard each API's availability and do not treat the framework's historical minimum as availability for every newer credential feature.

The Sign in with Apple entitlement, `com.apple.developer.applesignin`, is an array of strings configured by its Xcode capability. The Boolean `com.apple.developer.authentication-services.autofill-credential-provider` entitlement belongs on both an AutoFill extension and its host app, and still requires the person's enablement. The fast-passkey-creation sample requires a matching `webcredentials` associated domain and an `apple-app-site-association` entry for the app.

## Topics

### Authorization requests
- **ASAuthorizationController** - Manages provider-created requests; its iOS/iPadOS declaration starts at 13, not the framework's original 12 minimum.
- **AuthorizationController** - A SwiftUI environment value for authorization requests, introduced in iOS/iPadOS/Catalyst/tvOS 16.4, macOS 13.3, watchOS 9.4, and visionOS 1.
- **ASAuthorizationResult** - A successful authorization result in that same 16.4/macOS 13.3-generation SwiftUI API.

### Sign In with Apple
- [Implementing User Authentication with Sign in with Apple](https://developer.apple.com/documentation/authenticationservices/implementing-user-authentication-with-sign-in-with-apple) - Provide a way for users of your app to set up an account and start using your services.
- [Simplifying User Authentication in a tvOS App](https://developer.apple.com/documentation/authenticationservices/simplifying-user-authentication-in-a-tvos-app) - Build a fluid sign-in experience for your tvOS apps using AuthenticationServices.
- **SignInWithAppleButton** - A SwiftUI view that creates the Sign in with Apple button for display.
- **Sign in with Apple Entitlement** - An entitlement that lets your app use Sign in with Apple.
- **ASAuthorizationAppleIDProvider** - A mechanism for generating requests to authenticate users based on their Apple ID.
- **ASAuthorizationAppleIDCredential** - A credential that results from a successful Apple ID authentication.

### Passwords
- [Password AutoFill](https://developer.apple.com/documentation/security/password-autofill) - Streamline your app's login and onboarding procedures.
- **ASAuthorizationPasswordProvider** - A mechanism for generating requests to perform keychain credential sharing.
- **ASPasswordCredential** - A password credential.

### Passkeys
- [Public-Private Key Authentication](https://developer.apple.com/documentation/authenticationservices/public-private-key-authentication) - Register and authenticate users with passkeys and security keys, without using passwords.
- [Passkey use in web browsers](https://developer.apple.com/documentation/authenticationservices/passkey-use-in-web-browsers) - Register and authenticate website users by using passkeys.
- [Performing fast account creation with passkeys](https://developer.apple.com/documentation/authenticationservices/performing-fast-account-creation-with-passkeys) - Allow people to quickly create an account with passkeys and associated domains.
- [Connecting to a service with passkeys](https://developer.apple.com/documentation/authenticationservices/connecting-to-a-service-with-passkeys) - Allow users to sign in to a service without typing a password.

### Web authentication sessions
- [Authenticating a User Through a Web Service](https://developer.apple.com/documentation/authenticationservices/authenticating-a-user-through-a-web-service) - Use a web authentication session to authenticate a user in your app.
- [Securing Logins with iCloud Keychain Verification Codes](https://developer.apple.com/documentation/authenticationservices/securing-logins-with-icloud-keychain-verification-codes) - Use time-based codes generated on-device for a secure authentication experience.
- **ASWebAuthenticationSession** - A session for web-service authentication; tvOS support begins at 16 and watchOS support at 6.2, later than the framework's initial releases on those platforms.
- **WebAuthenticationSession** - A SwiftUI environment value that views use to authenticate someone using a web service.
- [Supporting Single Sign-On in a Web Browser App](https://developer.apple.com/documentation/authenticationservices/supporting-single-sign-on-in-a-web-browser-app) - Extend your web browser app to handle web authentication requests from other apps.
- **ASWebAuthenticationSessionWebBrowserSessionManager** - A session manager that mediates sharing data between an app and a web browser.
- **ASWebAuthenticationSessionWebBrowserSupportCapabilities** - A collection of keys that a browser app uses to declare its ability to handle authentication requests from other apps.

### AutoFill credentials
- [Providing one-time passcodes to AutoFill](https://developer.apple.com/documentation/authenticationservices/providing-one-time-passcodes-to-autofill) - Help people efficiently perform multifactor authentication.
- **AutoFill Credential Provider Entitlement** - A Boolean value that indicates whether the app may, with user permission, provide user names and passwords for AutoFill in Safari and other apps.
- **ASCredentialProviderViewController** - A view controller that a credential manager app uses to extend AutoFill.

### Credential migration

These managers begin at iOS/iPadOS/Catalyst/macOS/visionOS 26.0; they are not part of the original framework release.

- **ASCredentialExportManager** - A class to manage exporting credentials.
- **ASCredentialImportManager** - A class to manage importing credentials.

### Single sign-on (SSO)
- [Enterprise single sign-on (SSO)](https://developer.apple.com/documentation/authenticationservices/enterprise-single-sign-on-sso)
- [Platform single sign-on (SSO)](https://developer.apple.com/documentation/authenticationservices/platform-single-sign-on-sso) - Integrate an identity provider with macOS through a Platform SSO extension.

### Apple TV authentication
- **ASAuthorizationController.customAuthorizationMethods** - An array of custom authorization methods for the user to choose.
- **authorizationController(_:didCompleteWithCustomMethod:)** - Informs the delegate when authorization completes, and specifies the custom method the user selected.
- **ASAuthorizationCustomMethod** - The custom authorization method.

### Automatic security upgrades
- [Upgrading Account Security With an Account Authentication Modification Extension](https://developer.apple.com/documentation/authenticationservices/upgrading-account-security-with-an-account-authentication-modification-extension) - Handle user-initiated upgrades, verify authorization with the service, and cancel on refusal or failure; some flows require additional UI or multifactor authentication.
- **ASAccountAuthenticationModificationController** - An object that performs a request to modify an account's authentication properties.
- **ASAccountAuthenticationModificationViewController** - A view controller that can upgrade user passwords to strong passwords, or convert accounts to use Sign in with Apple.
- **ASAccountAuthenticationModificationExtensionContext** - An object that you interact with to change an account's password or to upgrade to Sign in with Apple.

### Updating credential managers
- [ASCredentialDataManager](https://developer.apple.com/documentation/authenticationservices/ascredentialdatamanager) - The 26.2-or-later replacement for submitting credentials and events to enabled credential managers. For privacy, a successful call confirms well-formed parameters, not that the manager performed the update.
- **ASCredentialUpdater** - Introduced in 26.0 and deprecated in 26.2 in favor of `ASCredentialDataManager`; retained as a legacy reference.

### Reference
- **AuthenticationServices Enumerations**
- **AuthenticationServices Data Types**

### Classes
- **ASAuthorizationAccountCreationPlatformPublicKeyCredential**
- **ASAuthorizationAccountCreationPlatformPublicKeyCredentialRequest**
- **ASAuthorizationAccountCreationProvider**
- **ASAuthorizationProviderExtensionUserLoginConfiguration**
- **ASOneTimeCodeCredentialIdentity**

### Protocols
- **ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialAssertionRequest**
- **ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialProvider** - Creates browser registration and assertion requests for security-key credentials; iOS 17.4/macOS 14.4-generation API.
- **ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialRegistrationRequest**

### Structures

Large-blob types originate in iOS 17/macOS 14; PRF and passkey extension input/output types are from iOS 18/macOS 15 and visionOS 2. Individual members may be later—for example, PRF properties on security-key request types are 26.4-generation additions. Check extension support and optional output instead of assuming every passkey flow supplies it.

- **ASAuthorizationProviderExtensionEncryptionAlgorithm**
- **ASAuthorizationProviderExtensionSigningAlgorithm**
- **ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput**
- **ASAuthorizationPublicKeyCredentialLargeBlobAssertionOutput**
- **ASAuthorizationPublicKeyCredentialLargeBlobRegistrationInput**
- **ASAuthorizationPublicKeyCredentialLargeBlobRegistrationOutput**
- **ASAuthorizationPublicKeyCredentialPRFAssertionInput** - Supplies PRF salt inputs for an assertion, including optional per-credential inputs.
- **ASAuthorizationPublicKeyCredentialPRFAssertionOutput** - Contains a first `SymmetricKey` and an optional second key when PRF output is available. Use derived keys for the operation, then discard them rather than storing or exporting them.
- **ASAuthorizationPublicKeyCredentialPRFRegistrationInput**
- **ASAuthorizationPublicKeyCredentialPRFRegistrationOutput**
- **ASEmailIdentifier**
- **ASImportableCredentialScope** - The scope for where a credential should be usable.
- **ASImportableEditableField** - A field that someone can edit within a credential.
- **ASPasskeyAssertionCredentialExtensionInput**
- **ASPasskeyAssertionCredentialExtensionOutput**
- **ASPasskeyRegistrationCredentialExtensionInput**
- **ASPasskeyRegistrationCredentialExtensionOutput**
- **ASPhoneNumberIdentifier**
- **ASPublicKeyCredentialClientData**

### Variables
- **ASCredentialExchangeActivity** - The activity type used in user activity objects sent to importing apps.
- **ASCredentialImportToken** - The key for the token in the user info dictionary of the user activity sent to importing apps.

### Enumerations
- **ASContactIdentifier**
- **ASContactIdentifierRequest**
- **ASPasskeyCredentialExtensionInput**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AuthenticationServices)*

*Authorization handling reviewed September 8, 2026: [Sign in with Apple sample](https://developer.apple.com/documentation/authenticationservices/implementing-user-authentication-with-sign-in-with-apple.md), [token verification](https://developer.apple.com/documentation/signinwithapple/verifying-a-user.md), and [account-change handling](https://developer.apple.com/documentation/signinwithapple/processing-changes-for-sign-in-with-apple-accounts.md).*
