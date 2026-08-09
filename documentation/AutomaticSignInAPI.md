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

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AutomaticSignInAPI)*