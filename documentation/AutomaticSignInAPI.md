# Automatic Sign-In API

Manage sign-in tokens that facilitate single sign-on across the devices of your media streaming service customers from your web server.

**Service version:** Automatic Sign-In API 1.0+. This is a server API, not an OS or compiler deployment baseline.

## Overview

Automatic Sign-In works with Video Subscriber Account in a media-streaming app. After the person opts in, the app supplies a sign-in token that the system stores with their Apple Account and makes available to the app on their other devices. This web API updates or deletes that token; it does not replace the app's initial authentication or opt-in flow.

Use [Signing people in to media apps automatically](https://developer.apple.com/documentation/videosubscriberaccount/signing-people-in-to-media-apps-automatically) for the client integration. Server-side changes support cases such as an opt-out or password change requiring sign-out across devices.

### Authenticate your API calls and test using the sandbox

Follow [Authorizing API calls using bearer tokens](https://developer.apple.com/documentation/videosubscriberaccount/authorizing-api-calls-using-bearer-tokens). The service uses an App Store Connect In-App Purchase key and an ES256-signed JWT identifying the issuer and app bundle ID, with audience `appstoreconnect-v1`. Its documented authorization-token lifetime is at most **60 minutes**. Keep the signing key separate from the media customer's sign-in token.

Use the endpoint's sandbox URL and a development or Ad Hoc build signed into a Sandbox Apple Account to create test data. The current Automatic Sign-In references use `api.storekit-sandbox.itunes.apple.com`; do not substitute another service's domain migration or treat sandbox data as production.

Both operations return HTTP `204` on success, `401` for invalid JWT authorization, and `404` when the sign-in token is not found. Inspect these results before reporting that a token changed, and reconcile an uncertain outcome before repeating a change.

## Topics

### Token updates
- [Update this token for all associated users](https://developer.apple.com/documentation/automaticsigninapi/update-this-token-for-all-associated-users) - Replace a specified sign-in token.
- [`UpdateAutoSignInTokenRequest`](https://developer.apple.com/documentation/automaticsigninapi/updateautosignintokenrequest) - The old and replacement sign-in tokens.

### Token deletion
- [Delete this token for all associated users](https://developer.apple.com/documentation/automaticsigninapi/delete-this-token-for-all-associated-users) - Delete a specified sign-in token.
- [`DeleteAutoSignInTokenRequest`](https://developer.apple.com/documentation/automaticsigninapi/deleteautosignintokenrequest) - The sign-in token to delete.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AutomaticSignInAPI)*
