# ManagedAppDistribution

Manage the distribution of apps within an organization.

**Platforms:** iOS 17.2+ | iPadOS 17.2+

## Overview
Managed apps are featured, downloadable apps that an enterprise, educational, or other institution provides to its employees or students. The Managed App Distribution framework allows developers of device management solutions to vend these managed apps. The framework verifies that someone initiated an app installation, provides status and download progress, and can launch the app once it’s downloaded.

Important

The Managed App Installation UI entitlement is required to use this framework.

An image of an iPhone showing an app with a banner image along the top of the screen. The middle of the screen contains two app banners, one top of the other. Each app banner contains a title, subtitle, and an install button.

The Managed App Distribution framework works with declarative management to provide a list of managed apps that are assigned to a device. Your app can sort or filter the list of managed apps, and request a view from the Managed App Distribution framework to display. See Integrating Declarative Management for more information.

## Topics

### Essentials
- [Fetching and displaying managed apps](https://developer.apple.com/documentation/managedappdistribution/fetching_and_displaying_managed_apps) - Provide a consistent app presentation when displaying managed apps.
- **ManagedApp** - A representation of a managed app.
- **ManagedAppLibrary** - A representation of a library of managed apps.
### App information
- **Platform** - The supported platform for the app.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ManagedAppDistribution)*
