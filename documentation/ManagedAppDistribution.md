# ManagedAppDistribution

Manage the distribution of apps within an organization.

**Platforms:** iOS 17.2+ | iPadOS 17.2+ | Mac Catalyst 26.4+ | macOS 26.4+ | visionOS 2.4+

## Overview
Managed apps are featured, downloadable apps that an enterprise, educational, or other institution provides to its employees or students. The Managed App Distribution framework allows developers of device management solutions to vend these managed apps. The framework verifies that someone initiated an app installation, provides status and download progress, and can launch the app once it’s downloaded.

> **Important:** The [Managed App Installation UI entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.managed-app-distribution.install-ui) is required. Its key is `com.apple.developer.managed-app-distribution.install-ui`, and its documented value is an **array of strings**, not a Boolean. Enable the capability in Xcode rather than inventing an entitlement value.

The entitlement page lists iOS/iPadOS 17.2, while the framework and library metadata additionally list Mac and visionOS availability above. Check the target's granted capability and provisioning; a framework availability entry does not itself grant installation rights.

The Managed App Distribution framework works with declarative management to provide a list of managed apps that are assigned to a device. Your app can sort or filter the list of managed apps, and request a view from the Managed App Distribution framework to display. See Integrating Declarative Management for more information.

## Topics

### Essentials
- [Fetching and displaying managed apps](https://developer.apple.com/documentation/managedappdistribution/fetching-and-displaying-managed-apps) - Provide a consistent app presentation when displaying managed apps.
- **ManagedApp** - A representation of a managed app.
- **ManagedAppLibrary** - A representation of a library of managed apps.
### App information
- **Platform** - The supported platform for the app.

### Errors
- [ManagedAppDistributionError](https://developer.apple.com/documentation/managedappdistribution/managedappdistributionerror) - Handle failed framework operations instead of treating an app's presence in the catalog as a successful installation.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ManagedAppDistribution)*
