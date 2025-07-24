# Account & Organizational Data Sharing

Provide people with the ability to authorize your apps and websites that access information about them on Apple REST services, like Roster API.

**Platforms:** AccountOrganizationalDataSharing 1.0+

## Overview

With OAuth 2.0, Account & Organizational Data Sharing gives your users a safe way to authorize your apps and websites to access information about them on Apple services, for example Roster API.

## Topics

### Generating Tokens
- [Creating a client secret](https://developer.apple.com/documentation/accountorganizationaldatasharing/creating_a_client_secret) - Generate a signed token to identify your client application.
- [Fetch Apple's public key for verifying token signature](https://developer.apple.com/documentation/accountorganizationaldatasharing/fetch_apple_s_public_key_for_verifying_token_signature) - Retrieve the public key associated with the cryptographic identity Apple uses to sign the token.
- [Generate and validate tokens](https://developer.apple.com/documentation/accountorganizationaldatasharing/generate_and_validate_tokens) - Validate an authorization grant code delivered to your app to obtain tokens, or validate an existing refresh token.

### Using and Revoking Tokens
- [Request an authorization](https://developer.apple.com/documentation/accountorganizationaldatasharing/request_an_authorization) - Request a user authorization to Account & Organizational Data Sharing apps and web services.
- [Revoke tokens](https://developer.apple.com/documentation/accountorganizationaldatasharing/revoke_tokens) - Invalidate the tokens and associated user authorizations for someone when they are no longer associated with your app.

### Common Objects
- **JWKSet** - A set of JSON web keys.
- **TokenResponse** - The response token object returned on a successful request.
- **ErrorResponse** - The error object returned after an unsuccessful request.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AccountOrganizationalDataSharing)*