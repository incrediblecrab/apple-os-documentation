# Authentication Services

Make it easy for users to log into apps and services.

**Platforms:** iOS 12.0+ | iPadOS 12.0+ | Mac Catalyst 13.0+ | macOS 10.15+ | tvOS 13.0+ | visionOS 1.0+ | watchOS 6.0+

## Overview

Use the Authentication Services framework to improve the experience of users when they enter credentials to establish their identity.

- Give users the ability to sign into your services with their Apple ID.
- Enable users to look up their stored passwords from within the sign-in flow of an app.
- Provide a passwordless registration and authentication workflow for apps and websites using iCloud Keychain or a physical security key.
- Perform automatic security upgrades from weak to strong passwords, or upgrade to using Sign in with Apple.
- Share data between an app and a web browser using technologies like OAuth to leverage existing web-based logins in the app.
- Create a single sign-on (SSO) experience in an enterprise app.

Simple and straightforward sign-up and sign-in flows reduce the burden on the user to remember passwords, which may improve security.

## Topics

### Authorization requests
- **ASAuthorizationController** - A controller that manages authorization requests that a provider creates.
- **AuthorizationController** - A SwiftUI environment value that views use to perform authorization requests.
- **ASAuthorizationResult** - Describes the outcome of a successful authorization request.

### Sign In with Apple
- [Implementing User Authentication with Sign in with Apple](https://developer.apple.com/documentation/authenticationservices/implementing_user_authentication_with_sign_in_with_apple) - Provide a way for users of your app to set up an account and start using your services.
- [Simplifying User Authentication in a tvOS App](https://developer.apple.com/documentation/authenticationservices/simplifying_user_authentication_in_a_tvos_app) - Build a fluid sign-in experience for your tvOS apps using AuthenticationServices.
- **SignInWithAppleButton** - A SwiftUI view that creates the Sign in with Apple button for display.
- **Sign in with Apple Entitlement** - An entitlement that lets your app use Sign in with Apple.
- **ASAuthorizationAppleIDProvider** - A mechanism for generating requests to authenticate users based on their Apple ID.
- **ASAuthorizationAppleIDCredential** - A credential that results from a successful Apple ID authentication.

### Passwords
- [Password AutoFill](https://developer.apple.com/documentation/authenticationservices/password_autofill) - Streamline your app's login and onboarding procedures.
- **ASAuthorizationPasswordProvider** - A mechanism for generating requests to perform keychain credential sharing.
- **ASPasswordCredential** - A password credential.

### Passkeys
- [Public-Private Key Authentication](https://developer.apple.com/documentation/authenticationservices/public-private_key_authentication) - Register and authenticate users with passkeys and security keys, without using passwords.
- [Passkey use in web browsers](https://developer.apple.com/documentation/authenticationservices/passkey_use_in_web_browsers) - Register and authenticate website users by using passkeys.
- [Performing fast account creation with passkeys](https://developer.apple.com/documentation/authenticationservices/performing_fast_account_creation_with_passkeys) - Allow people to quickly create an account with passkeys and associated domains.
- [Connecting to a service with passkeys](https://developer.apple.com/documentation/authenticationservices/connecting_to_a_service_with_passkeys) - Allow users to sign in to a service without typing a password.

### Web authentication sessions
- [Authenticating a User Through a Web Service](https://developer.apple.com/documentation/authenticationservices/authenticating_a_user_through_a_web_service) - Use a web authentication session to authenticate a user in your app.
- [Securing Logins with iCloud Keychain Verification Codes](https://developer.apple.com/documentation/authenticationservices/securing_logins_with_icloud_keychain_verification_codes) - Use time-based codes generated on-device for a secure authentication experience.
- **ASWebAuthenticationSession** - A session that an app uses to authenticate a user through a web service.
- **WebAuthenticationSession** - A SwiftUI environment value that views use to authenticate someone using a web service.
- [Supporting Single Sign-On in a Web Browser App](https://developer.apple.com/documentation/authenticationservices/supporting_single_sign-on_in_a_web_browser_app) - Extend your web browser app to handle web authentication requests from other apps.
- **ASWebAuthenticationSessionWebBrowserSessionManager** - A session manager that mediates sharing data between an app and a web browser.
- **ASWebAuthenticationSessionWebBrowserSupportCapabilities** - A collection of keys that a browser app uses to declare its ability to handle authentication requests from other apps.

### AutoFill credentials
- [Providing one-time passcodes to AutoFill](https://developer.apple.com/documentation/authenticationservices/providing_one-time_passcodes_to_autofill) - Help people efficiently perform multifactor authentication.
- **AutoFill Credential Provider Entitlement** - A Boolean value that indicates whether the app may, with user permission, provide user names and passwords for AutoFill in Safari and other apps.
- **ASCredentialProviderViewController** - A view controller that a credential manager app uses to extend AutoFill.

### Credential migration
- **ASCredentialExportManager** - A class to manage exporting credentials. *Beta*
- **ASCredentialImportManager** - A class to manage importing credentials. *Beta*

### Single sign-on (SSO)
- [Enterprise single sign-on (SSO)](https://developer.apple.com/documentation/authenticationservices/enterprise_single_sign-on_sso)
- [Platform single sign-on (SSO)](https://developer.apple.com/documentation/authenticationservices/platform_single_sign-on_sso) - Use credentials from macOS login to perform single sign-on with an identity provider.

### Apple TV authentication
- **customAuthorizationMethods** - An array of custom authorization methods for the user to choose.
- **authorizationController(ASAuthorizationController, didCompleteWithCustomMethod:)** - Informs the delegate when authorization completes, and specifies the custom method the user selected.
- **ASAuthorizationCustomMethod** - The custom authorization method.

### Automatic security upgrades
- [Upgrading Account Security With an Account Authentication Modification Extension](https://developer.apple.com/documentation/authenticationservices/upgrading_account_security_with_an_account_authentication_modification_extension) - Automatically and transparently convert accounts to Sign in with Apple or to use strong passwords for improved security.
- **ASAccountAuthenticationModificationController** - An object that performs a request to modify an account's authentication properties.
- **ASAccountAuthenticationModificationViewController** - A view controller that can upgrade user passwords to strong passwords, or convert accounts to use Sign in with Apple.
- **ASAccountAuthenticationModificationExtensionContext** - An object that you interact with to change an account's password or to upgrade to Sign in with Apple.

### Updating credential managers
- **ASCredentialUpdater** - A class to pass credential update events to credential managers enabled on the system. *Beta*

### Reference
- **AuthenticationServices Enumerations**
- **AuthenticationServices Data Types**

### Classes
- **ASAuthorizationAccountCreationPlatformPublicKeyCredential** *Beta*
- **ASAuthorizationAccountCreationPlatformPublicKeyCredentialRequest** *Beta*
- **ASAuthorizationAccountCreationProvider** *Beta*
- **ASAuthorizationProviderExtensionUserLoginConfiguration**
- **ASOneTimeCodeCredentialIdentity**

### Protocols
- **ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialAssertionRequest**
- **ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialProvider** - A protocol for creating passkey requests.
- **ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialRegistrationRequest**

### Structures
- **ASAuthorizationProviderExtensionEncryptionAlgorithm**
- **ASAuthorizationProviderExtensionSigningAlgorithm**
- **ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput**
- **ASAuthorizationPublicKeyCredentialLargeBlobAssertionOutput**
- **ASAuthorizationPublicKeyCredentialLargeBlobRegistrationInput**
- **ASAuthorizationPublicKeyCredentialLargeBlobRegistrationOutput**
- **ASAuthorizationPublicKeyCredentialPRFAssertionInput** - This type represents the inputs for the WebAuthentication PRF extension, when used during assertion requests. The PRF extension lets you create general purpose SymmetricKeys from passkeys, which could useful for tasks such as encryption of user data. The same input values used with the same passkey will always produce the same SymmetricKey.
- **ASAuthorizationPublicKeyCredentialPRFAssertionOutput** - The outputs of the WebAuthentication PRF extension, when requested during an assertion. This object represents one or two SymmetricKeys which are available anywhere the passkey can be used. These are general purpose keys which can be used for application-specific needs, such as encryption of user data. These keys should not be stored or exported. They should only ever be derived as the result of an assertion operation, and then discarded when finished.
- **ASAuthorizationPublicKeyCredentialPRFRegistrationInput**
- **ASAuthorizationPublicKeyCredentialPRFRegistrationOutput**
- **ASEmailIdentifier** *Beta*
- **ASImportableCredentialScope** - The scope for where a credential should be usable. *Beta*
- **ASImportableEditableField** - A field that someone can edit within a credential. *Beta*
- **ASPasskeyAssertionCredentialExtensionInput**
- **ASPasskeyAssertionCredentialExtensionOutput**
- **ASPasskeyRegistrationCredentialExtensionInput**
- **ASPasskeyRegistrationCredentialExtensionOutput**
- **ASPhoneNumberIdentifier** *Beta*
- **ASPublicKeyCredentialClientData**

### Variables
- **ASCredentialExchangeActivity** - The activity type used in user activity objects sent to importing apps. *Beta*
- **ASCredentialImportToken** - The key for the token in the user info dictionary of the user activity sent to importing apps. *Beta*

### Enumerations
- **ASContactIdentifier** *Beta*
- **ASContactIdentifierRequest** *Beta*
- **ASPasskeyCredentialExtensionInput**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AuthenticationServices)*