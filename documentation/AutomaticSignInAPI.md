# Automatic Sign-In API

Manage sign-in tokens that facilitate single sign-on across the devices of your media streaming service customers from your web server.

**Platforms:** Automatic Sign-In API 1.0+

## Overview

This API works in conjunction with Video Subscriber Account to manage sign-in tokens from your web server that implement the VSUserAccountManager Automatic Sign-In feature.

**Note**: For more on Automatic Sign-In for Apple devices, see Signing people in to their media accounts automatically.

### Authenticate your API calls and test using the sandbox

The Automatic Sign-In API shares authentication and testing steps with the App Store Server API. Before issuing calls to this service, perform the setup in Authorize your API calls. To test your web server during development, see Test using the sandbox environment.

## Topics

### Token updates
- **Update Sign-In Token** - Updates a specific sign-in token to a new value.
- **UpdateAutoSignInTokenRequest** - The request body that contains the old sign-in token and the new sign-in token.

### Token deletion
- **Delete Sign-In Token** - Deletes a specific sign-in token.
- **DeleteAutoSignInTokenRequest** - The request body that contains the sign-in token to be deleted.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AutomaticSignInAPI)*