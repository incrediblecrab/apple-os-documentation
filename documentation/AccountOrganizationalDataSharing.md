# Account & Organizational Data Sharing

Provide people with the ability to authorize your apps and websites that access information about them on Apple REST services, like Roster API.

**Service API version:** AccountOrganizationalDataSharing 1.0. This is a REST service version, not an Apple OS deployment minimum.

## Overview

Account & Organizational Data Sharing uses OAuth 2.0 to authorize apps and websites to access information on designated Apple services, such as Roster API.

## Topics

### Generating Tokens
- [Creating a client secret](https://developer.apple.com/documentation/accountorganizationaldatasharing/creating-a-client-secret) - Generate a signed token to identify your client application.
- [Fetch Apple's public key for verifying token signature](https://developer.apple.com/documentation/accountorganizationaldatasharing/fetch-apple's-public-key-for-verifying-token-signature) - Retrieve the public key associated with the cryptographic identity Apple uses to sign the token.
- [Generate and validate tokens](https://developer.apple.com/documentation/accountorganizationaldatasharing/generate-and-validate-tokens) - Validate an authorization grant code delivered to your app to obtain tokens, or validate an existing refresh token.

### Using and Revoking Tokens
- [Request an authorization](https://developer.apple.com/documentation/accountorganizationaldatasharing/request-an-authorization) - Request a user authorization to Account & Organizational Data Sharing apps and web services.
- [Token revocation](https://developer.apple.com/documentation/accountorganizationaldatasharing/revoke-tokens) - Invalidate a user's tokens and associated authorization using a valid access or refresh token. Handle errors separately from successful or already-invalidated responses.

### Common Objects
- **JWKSet** - A set of JSON web keys.
- **TokenResponse** - The response token object returned on a successful request.
- **ErrorResponse** - The error object returned after an unsuccessful request.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AccountOrganizationalDataSharing)*
