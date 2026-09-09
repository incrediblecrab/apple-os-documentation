# App License Delivery SDK

Secure the installation of alternative distribution apps on iOS or iPadOS devices by vending licenses from your web server.

## Overview

This Swift SDK enables digital rights management (DRM) for alternative distribution apps. Use this SDK to generate licenses for alternative app marketplaces you build with MarketplaceKit or other apps that you distribute from your website. Alternative app marketplaces use this SDK to generate a license for each app that developers distribute on the marketplace. By licensing each download individually, you provide a secure installation experience similar to the App Store.

Use this SDK's framework to implement a license server on your website back end that's capable of running compiled Swift code. Then, publish endpoints for your license server in a standard location that the device's operating system expects. On an as-needed basis, the system retrieves licenses from your endpoints when a person downloads:

- An alternative app marketplace from your website
- An app that developers distribute on your alternative app marketplace
- An app that you develop and distribute on your website

Download access requires an eligible developer account. See [Distributing your app from your website](https://developer.apple.com/documentation/marketplacekit/distributing-your-app-from-your-website), [Regional distribution](../guides/regional-distribution.md), and [App Store readiness](../guides/app-store-readiness.md) for the applicable program and policy prerequisites.

### Platform, OS, and tools requirements

Apple silicon Macs, Intel Macs, macOS 13.5+, select Linux versions on x86_64, and Xcode 15+ (including the macOS 14 SDK).

These are the SDK's documented server/build requirements, not an assertion that current Xcode versions run on macOS 13.5, or that clients require OS 27. Check the selected toolchain's own host requirements separately.

## Licensing and failure handling

[Prepare the ALD signing/encryption assets](https://developer.apple.com/documentation/applicensedeliverysdk/configuring-the-app-licensing-environment), then follow the [licensing protocol](https://developer.apple.com/documentation/applicensedeliverysdk/licensing-alternative-distribution-apps). The device discovers your configuration at `/.well-known/marketplace-kit` on the registered domain. Serve it over HTTPS with a valid certificate and **without redirects**.

The configuration identifies license creation and renewal endpoints, a license-resolution webpage, and certificate resources. Keep the associated private keys server-side; a request's app identifier alone is not sufficient proof that the account is entitled to a license. If your integration uses account authentication, validate the bearer token the system forwards from your download flow.

Validate and decrypt the request using the documented assets/SDK and handle every requested app deliberately. Report generation failures instead of returning an empty license blob; for deliberate licensing denials, use the protocol's `unlicensedApps` list. Renewal responses use `ineligibleLicenses` for licenses you will not renew. Keep license expiration, renewal, and revocation distinct; revoking a license affects whether an installed app can launch.

## Topics

### Essentials
- [Configuring your app licensing environment](https://developer.apple.com/documentation/applicensedeliverysdk/configuring-the-app-licensing-environment) - Prepare signing assets and the server build.

### App licensing
- [Licensing alternative distribution apps](https://developer.apple.com/documentation/applicensedeliverysdk/licensing-alternative-distribution-apps) - Implement installation licensing.
- [Renewing and revoking app licenses](https://developer.apple.com/documentation/applicensedeliverysdk/renewing-and-revoking-app-licenses) - Manage continued launch authorization.
- **ALDAppKey** - An app identifier paired with the key blob for a specific app variant, which you add to the generated license.
- **ALDLicenseAttribute** - A structure that defines the requested license type for the session.
- **ALDProvider** - An object that creates a session with the alternative app marketplace's signing assets.
- **ALDSession** - A structure that contains the details of a license request and methods to generate license responses.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AppLicenseDeliverySDK)*
