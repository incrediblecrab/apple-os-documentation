# Automated Device Enrollment

Allow users of third-party MDM apps to add macOS and iOS devices to their organization.

**UI API declarations:** iOS 16.0+ | iPadOS 16.0+

The framework catalog separately lists iOS/iPadOS and Mac Catalyst 16.1. The SwiftUI modifier and entitlement references declare iOS/iPadOS 16.0 and do not list Catalyst. These differing catalog and symbol annotations are not confirmation of a usable Catalyst enrollment UI.

## Overview

This framework provides an administration interface for adding macOS, iOS, and iPadOS devices to an organization. The device being added is distinct from the device hosting the interface. The SwiftUI modifier's current documentation describes Apple School Manager and Apple Business organizations: a user signs in with a Managed Apple Account that has device-enrollment privileges.

This feature requires Bluetooth access to discover and pair with nearby devices, and camera access to scan visual pairing PIN codes. To use this feature, you must have the Automated Device Enrollment entitlement. To obtain permission for this entitlement, see [Automated Device Enrollment Entitlement Request](https://developer.apple.com/contact/request/automated-device-enrollment/).

### Permissions and enrollment-network failures

An entitlement does not replace the administrator's enrollment privileges or the person's Bluetooth and camera permissions. Handle denied access, cancelled pairing, and failed sign-in without treating a displayed enrollment sheet as successful device assignment.

**27 beta, reviewed September 8, 2026:** System processes involved in Automated Device Enrollment now require servers to support TLS 1.2 or later with ATS-compliant cipher suites and certificates. This is part of the targeted management, installation, and update hardening—not a new blanket requirement on all app network calls.

Audit the complete enrollment path, including vendor-hosted services and redirects. Apple's [network preparation guidance](https://support.apple.com/en-us/126655) explains logging, stricter TLS 1.2 requirements, and the SCEP/content-caching exceptions. For iPhone and iPad ADE testing, it describes installing the diagnostic profile with Apple Configurator before Setup Assistant reaches the Device Management pane.

## Topics

### Essentials
- [automatedDeviceEnrollmentAddition(isPresented:)](https://developer.apple.com/documentation/swiftui/view/automateddeviceenrollmentaddition(ispresented:)) - Presents the modal device-enrollment interface.
- [com.apple.developer.automated-device-enrollment.add-devices](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.automated-device-enrollment.add-devices) - A Boolean entitlement allowing the app to add a device to Automated Device Enrollment.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AutomatedDeviceEnrollment)*

*27-beta source: [Prepare your network environment for stricter security requirements](https://support.apple.com/en-us/126655).*
