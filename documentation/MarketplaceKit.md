# MarketplaceKit

Create an alternative app marketplace, distribute your app on an alternative app marketplace, or distribute your app from your website.

**Platforms:** iOS 17.4+ | iPadOS 18.0+

## Overview

An alternative app marketplace is an app from which someone can install apps from other developers, as an alternative to the App Store. MarketplaceKit enables alternative app marketplaces to install the apps they distribute to peoples' devices. The framework also supports features that compose a quality browsing and installation experience, such as Spotlight Search and App Thinning. With the framework, you can manage existing app installations, convey download progress, update app licensing, and customize app search behavior.

In addition to alternative app marketplaces, this framework also serves:

- Web browsers, specifically by requesting app installation on a webpage.
- Apps that install from an alternative app marketplace or webpage, by determining the installation source at runtime. This allows an app to branch its functionality depending on the installation source.

**Important:** To request the marketplace entitlement, see Getting started as an alternative app marketplace in the European Union. To apply to distribute your app from your website, see Getting started with Web Distribution in the EU.

## Topics

### Essentials
- [Creating an alternative app marketplace](https://developer.apple.com/documentation/marketplacekit/creating_an_alternative_app_marketplace) - Enable the distribution of other third-party apps from within your marketplace app.
- [Distributing your app from your website](https://developer.apple.com/documentation/marketplacekit/distributing_your_app_from_your_website) - Configure your app and website to enable people to install your app on their devices from your website.
- [Distributing your app on an alternative app marketplace](https://developer.apple.com/documentation/marketplacekit/distributing_your_app_on_an_alternative_app_marketplace) - Design your app for alternative distribution from an alternative app marketplace.

### Web services
- [Processing alternative app marketplace notifications](https://developer.apple.com/documentation/marketplacekit/processing_alternative_app_marketplace_notifications) - Manage the addition and removal of apps available on your alternative marketplace.
- [Ingesting an alternative distribution package](https://developer.apple.com/documentation/marketplacekit/ingesting_an_alternative_distribution_package) - Process an available app version from App Store Connect and store it for download from your server.
- [Installing your app from your website](https://developer.apple.com/documentation/marketplacekit/installing_your_app_from_your_website) - Manage the installation of an app that you develop and distribute through your website.
- [Installing apps from an alternative marketplace](https://developer.apple.com/documentation/marketplacekit/installing_apps_from_an_alternative_marketplace) - Manage the installation of apps that developers distribute from your marketplace app.
- [Supplying an install verification token](https://developer.apple.com/documentation/marketplacekit/supplying_an_install_verification_token) - Support the installation of alternative distribution apps by creating signed JSON web tokens.

### Authorization
- [Reauthenticating a person to manage apps](https://developer.apple.com/documentation/marketplacekit/reauthenticating_a_person_to_manage_apps) - Renew your app's authorization when an app needs updating or when a device restores from backup.
- **com.apple.developer.marketplace.app-installation** - The entitlement that enables an app to vend other apps as an alternative app marketplace.
- **com.apple.developer.browser.app-installation** - The entitlement that enables a browser to install alternative-distribution apps from a website.
- [App License Delivery SDK](https://developer.apple.com/documentation/marketplacekit/app_license_delivery_sdk) - Secure the installation of alternative distribution apps on iOS or iPadOS devices by vending licenses from your web server.

### Browser support
- [Enabling alternative distribution app installation in a browser](https://developer.apple.com/documentation/marketplacekit/enabling_alternative_distribution_app_installation_in_a_browser) - Add support for browser apps to install alternative distribution apps from websites.

### App management
- **AppLibrary** - An object that manages search characteristics, licensing, and the installation of apps.
- **AppVersion** - Information that describes an app, including its identifier and version number.
- **AutomaticUpdate** - Information that describes an app that's available for update, including a download URL.
- **InstallRequirements** - An app's installation criteria for a device.
- **AppleItemID** - An identifier that represents an app.
- **AppleVersionID** - An identifier that represents a single app version.
- **MarketplaceKitURIScheme** - A URI scheme that defines an alternative distribution app installation link.

### Background services
- **MarketplaceExtension** - An extension that facilitates authentication, installation, and launching a marketplace with deep links.
- **MarketplaceExtensionConfiguration** - The type for a marketplace extension's configuration object.

### App distribution UI
- **ActionButton** - A user-interface element that enables a person to install, update, or launch apps by tapping the element.
- **InstallMetadata** - Information about a specific app to install or update and the person who initiates it.
- **InstallConfiguration** - Information that describes a requested app installation or app update.
- **InstallConfirmationResult** - Options that indicate whether the installation of an app proceeds when a person interacts with an app installation button.
- **BatchInstallConfiguration** - Information that describes multiple app installations or app updates.
- **BatchInstallConfirmationResult** - Options that indicate whether the installation of multiple apps proceeds when a person interacts with an app installation button.
- **MarketplaceDisplayOption** - The kinds of deep links that the operating system makes into your marketplace.
- **MarketplaceSceneDelegate** - A delegate that handles deep link requests into your marketplace app.

### Installation sources
- **AppDistributor** - Options that describe the marketplace from which the app installs.

### Errors
- **MarketplaceKitError** - Errors that can occur in the marketplace workflow.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MarketplaceKit)*