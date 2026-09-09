# Wallet Passes

Create, distribute, and update passes for the Wallet app.

**Availability:** Pass packages and update services for supported Wallet clients. Individual pass styles, semantic tags, and client features have their own availability; this is not an OS 27-only format.

## Overview

Passes are digital representations of information that might previously be on paper or plastic. They let users take action in the physical world, such as boarding a flight, attending an event, or claiming a coat-check item.

To enable a user to install your pass, you need to:

1. Create the source for a pass.
2. Build a distributable pass from the source.
3. Distribute a pass.

Start with [Creating the Source for a Pass](https://developer.apple.com/documentation/walletpasses/creating-the-source-for-a-pass), [Building a Pass](https://developer.apple.com/documentation/walletpasses/building-a-pass), and [Distributing and updating a pass](https://developer.apple.com/documentation/walletpasses/distributing-and-updating-a-pass).

## Current authoring and update guidance

[Pass Designer](https://developer.apple.com/documentation/walletpasses/creating-a-pass-with-pass-designer) is a macOS authoring app. Its current guide requires **macOS 27 or later** and describes saving a `.pkpasstemplate` bundle that still needs building and signing. This is the tool's host requirement, not an Xcode requirement or a new minimum for all Wallet clients.

Follow the [pass metadata](https://developer.apple.com/documentation/walletpasses/defining-the-metadata-of-your-wallet-pass) and pass-specific authoring guides instead of deriving keys or feature limits from the Wallet app's own interface. General semantic metadata predates OS 27; newer layouts and integrations have separate requirements.

The [semantic boarding-pass guide](https://developer.apple.com/documentation/walletpasses/creating-an-airline-boarding-pass-using-semantic-tags) describes the iOS/watchOS 26 experience for **airline** passes: use `semanticBoardingPass` in `preferredStyleSchemes`, the `boardingPass` dictionary with `PKTransitTypeAir`, and the required semantic tags. Keep valid legacy pass fields for fallback; adding semantic tags does not make every transit pass eligible for this layout.

For [poster event passes](https://developer.apple.com/documentation/walletpasses/creating-an-event-pass-using-semantic-tags), follow the style's required tags and fallback rules. That guide warns that poster event tickets are incompatible with tickets requiring a QR code or barcode for entry. Do not apply the poster layout blindly to an existing barcode-entry ticket.

### Signing and distribution

The distributable `.pkpass` is not an unsigned JSON file or a saved designer template. The [building workflow](https://developer.apple.com/documentation/walletpasses/building-a-pass) requires a manifest of source-file **SHA-1** hashes, a **PKCS #7 detached signature** made with the pass type's signing certificate, and the resulting ZIP-based `.pkpass` package. Do not substitute a different manifest hash algorithm merely because another service uses it.

Check that `passTypeIdentifier` and `teamIdentifier` match the signing certificate and account. The pair `passTypeIdentifier` and `serialNumber` identifies a pass; distributing another version with that pair replaces the existing pass rather than creating a distinct ticket.

### Update service and failure handling

For ongoing changes, implement the [update web service](https://developer.apple.com/documentation/walletpasses/adding-a-web-service-to-update-passes), including device registration, authentication, fetching updated passes, and unregistration. Provide `webServiceURL` and `authenticationToken` in the pass. Use HTTPS in production.

Authenticate registration, unregistration, and pass retrieval with `Authorization: ApplePass {authenticationToken}`. The update-list operation instead uses the opaque device library identifier as its shared secret; it is not a public enumeration endpoint.

An empty-JSON push notification prompts the device to list and retrieve updates; it is not the replacement pass itself. Pass-update push notifications use the **production** APNs environment. Keep the pass type identifier, serial number, and authentication token stable across updates.

Respect the endpoint-specific responses:
- Registration returns `201` for a new registration, `200` when already registered, or `401` when unauthorized.
- Listing updated passes returns `200` with `SerialNumbers`, or `204` when none match. Its `lastUpdated` value is a developer-defined tag used with `passesUpdatedSince`, not necessarily a Unix timestamp.
- Pass retrieval returns the signed pass as `application/vnd.apple.pkpass`; unregistration removes the relevant device-pass relationship, not every registration for that pass.

Test malformed or incorrectly signed packages, expired signing credentials, failed update requests, and removal of registrations. Do not expose a personalized pass or its update credentials in logs or unauthenticated administrative endpoints.

## Topics

### Essentials
- [Creating a pass with Pass Designer](https://developer.apple.com/documentation/walletpasses/creating-a-pass-with-pass-designer) - Author and customize supported pass styles.
- [Creating the Source for a Pass](https://developer.apple.com/documentation/walletpasses/creating-the-source-for-a-pass) - Create the directory structure and add source files and images to define a pass.
- [Building a Pass](https://developer.apple.com/documentation/walletpasses/building-a-pass) - Build a distributable pass.
- [Defining the metadata of your Wallet Pass](https://developer.apple.com/documentation/walletpasses/defining-the-metadata-of-your-wallet-pass) - Configure documented pass metadata.
- [Distributing and updating a pass](https://developer.apple.com/documentation/walletpasses/distributing-and-updating-a-pass) - Distribute a pass to your users or update an existing pass.
- [`Pass`](https://developer.apple.com/documentation/walletpasses/pass) - The pass's top-level content and metadata object.

### Multievent Passes
- [`UpcomingPassInformationEntry`](https://developer.apple.com/documentation/walletpasses/upcomingpassinformationentry) - One upcoming entry, with its own identifier, name, type, dates, and content. The ordered list is `Pass.upcomingPassInformation`.
- [`UpcomingPassInformationEntryType`](https://developer.apple.com/documentation/walletpasses/upcomingpassinformationentrytype) - Supporting image-related object types for upcoming entries, not the entry list or its `type` string.

### Pass Updates
- [Adding a Web Service to Update Passes](https://developer.apple.com/documentation/walletpasses/adding-a-web-service-to-update-passes) - Implement a web server to register, update, and unregister a pass on a device.
- [Register a Pass for Update Notifications](https://developer.apple.com/documentation/walletpasses/register-a-pass-for-update-notifications) - Set up change notifications for a pass on a device.
- [Get the List of Updatable Passes](https://developer.apple.com/documentation/walletpasses/get-the-list-of-updatable-passes) - Send the serial numbers for updated passes to a device.
- [Send an Updated Pass](https://developer.apple.com/documentation/walletpasses/send-an-updated-pass) - Create and sign an updated pass, and send it to the device.
- [Unregister a Pass for Update Notifications](https://developer.apple.com/documentation/walletpasses/unregister-a-pass-for-update-notifications) - Stop sending update notifications for a pass on a device.
- [Log a Message](https://developer.apple.com/documentation/walletpasses/log-a-message) - Record a message on your server.
- [`PushToken`](https://developer.apple.com/documentation/walletpasses/pushtoken) - An object that contains the push notification token for a registered pass on a device.
- [`SerialNumbers`](https://developer.apple.com/documentation/walletpasses/serialnumbers) - Updated pass serial numbers and a developer-defined update tag.
- [`LogEntries`](https://developer.apple.com/documentation/walletpasses/logentries) - An object that contains an array of messages.

### Personalized Passes
- [Return a Personalized Pass](https://developer.apple.com/documentation/walletpasses/return-a-personalized-pass) - Sign and return the request's personalization token. The documented `200` response is `application/octet-stream`, not a replacement `.pkpass` package.
- [`PersonalizationDictionary`](https://developer.apple.com/documentation/walletpasses/personalizationdictionary) - The required `personalizationToken` and user-entered `requiredPersonalizationInfo` for this exchange.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/WalletPasses)*
