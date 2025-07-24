# App License Delivery SDK

Secure the installation of alternative distribution apps on iOS or iPadOS devices by vending licenses from your web server.

## Overview

This Swift SDK enables digital rights management (DRM) for alternative distribution apps. Use this SDK to generate licenses for alternative app marketplaces you build with MarketplaceKit or other apps that you distribute from your website. Alternative app marketplaces use this SDK to generate a license for each app that developers distribute on the marketplace. By licensing each download individually, you provide a secure installation experience similar to the App Store.

Use this SDK's framework to implement a license server on your website back end that's capable of running compiled Swift code. Then, publish endpoints for your license server in a standard location that the device's operating system expects. On an as-needed basis, the system retrieves licenses from your endpoints when a person downloads:

- An alternative app marketplace from your website
- An app that developers distribute on your alternative app marketplace
- An app that you develop and distribute on your website

You can download this SDK from Downloads if your developer account qualifies to distribute apps from your website. For more information, see Distributing your app from your website.

### Platform, OS, and tools requirements

Apple silicon Macs, Intel Macs, macOS 13.5+, select Linux versions on x86_64, and Xcode 15+ (including the macOS 14 SDK).

## Topics

### Essentials
- [Configuring your app licensing environment](https://developer.apple.com/documentation/AppLicenseDeliverySDK/configuring_your_app_licensing_environment) - Create your account-level signing assets and build the SDK for your target platform.

### App licensing
- [Licensing alternative distribution apps](https://developer.apple.com/documentation/AppLicenseDeliverySDK/licensing_alternative_distribution_apps) - Build a license server that supports the installation of your apps and the apps available in your marketplace.
- [Renewing and revoking app licenses](https://developer.apple.com/documentation/AppLicenseDeliverySDK/renewing_and_revoking_app_licenses) - Determine whether an app for which you issue a license launches.
- **ALDAppKey** - A structure that identifies an app and a key that's required to decrypt the app's license request.
- **ALDLicenseAttribute** - A structure that defines the requested license type for the session.
- **ALDProvider** - An object that creates a session with the alternative app marketplace's signing assets.
- **ALDSession** - A structure that contains the details of a license request and methods to generate license responses.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AppLicenseDeliverySDK)*