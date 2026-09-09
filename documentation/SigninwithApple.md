# Sign in with Apple

Provide users the ability to sign in to your apps and websites using their Apple Account.

**Platforms:** Sign in with Apple JS 1.0+ | Sign in with Apple REST API 1.0+

## Overview

Sign in with Apple lets people authenticate with their Apple Account instead of creating another password for your service. It can reduce credential setup, but your app may still need account-specific onboarding and authorization.

Sign in with Apple at Work & School also supports managed Apple Accounts in Apple School Manager (ASM) or Apple Business Manager (ABM).

**Note:** Administrators can configure Access Management controls for Sign in with Apple at Work & School within Apple Business Manager and Apple School Manager.

To support Sign in with Apple for iOS, macOS, tvOS, and watchOS apps, see Implementing User Authentication with Sign in with Apple. For website support, see **Sign in with Apple JS**, and use the **Sign in with Apple REST API** to communicate with Apple servers.

### Verification, denial, and revoked consent

Validate the identity token on the server before establishing an authenticated session. Apple's [verification guide](https://developer.apple.com/documentation/signinwithapple/verifying-a-user) covers the signature, nonce, issuer, audience, and expiration. A cancelled or failed authorization must not create a signed-in session.

For native apps, check credential state when restoring access and handle revoked or missing credentials. For server integrations, verify the signed server-to-server notification before acting on events such as `consent-revoked`, `account-deleted`, `email-enabled`, and `email-disabled`. An email-forwarding change is not the same event as revocation of sign-in consent.

Apple notes that permanent account deletion invalidates tokens but does **not** send `credentialRevokedNotification` to native apps. Use the documented credential-state checks and server notifications rather than treating the absence of a notification as continuing authorization.

## Topics

### On-device support
- [Implementing User Authentication with Sign in with Apple](https://developer.apple.com/documentation/authenticationservices/implementing-user-authentication-with-sign-in-with-apple) - Configure native authorization and credential-state handling.
- [Displaying Sign in with Apple buttons in your app](https://developer.apple.com/documentation/signinwithapple/displaying-sign-in-with-apple-buttons-in-your-app) - Configure native Sign in with Apple buttons.

### Web support
- **Sign in with Apple JS** - Provide a web sign-in flow using an Apple Account.
- **Sign in with Apple REST API** - Communicate between your app servers and Apple's authentication servers.
- [Displaying Sign in with Apple buttons on the web](https://developer.apple.com/documentation/signinwithapple/displaying-sign-in-with-apple-buttons-on-the-web) - Configure the appearance of Sign in with Apple buttons with CSS styles.
- [Configuring your environment for Sign in with Apple](https://developer.apple.com/documentation/signinwithapple/configuring-your-environment-for-sign-in-with-apple) - Authenticate users with your web service by associating an existing app with a Services ID and private key.
- [Processing changes for Sign in with Apple accounts](https://developer.apple.com/documentation/signinwithapple/processing-changes-for-sign-in-with-apple-accounts) - Validate and act on account-change notifications.

### Transfers across teams
- [Transferring your apps and users to another team](https://developer.apple.com/documentation/signinwithapple/transferring-your-apps-and-users-to-another-team) - Migrate Sign in with Apple users to another team.
- [Bringing new apps and users into your team](https://developer.apple.com/documentation/signinwithapple/bringing-new-apps-and-users-into-your-team) - Receive Sign in with Apple users and associated apps from another team.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SigninwithApple)*

*Changed-content sources, reviewed September 8, 2026: [token verification](https://developer.apple.com/documentation/signinwithapple/verifying-a-user.md) and [account-change semantics](https://developer.apple.com/documentation/signinwithapple/processing-changes-for-sign-in-with-apple-accounts.md).*
