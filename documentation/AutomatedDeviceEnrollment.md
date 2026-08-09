# Automated Device Enrollment

Allow users of third-party MDM apps to add macOS and iOS devices to their organization.

**Platforms:** iOS 16.1+ | iPadOS 16.1+ | Mac Catalyst 16.1+

## Overview

This framework provides a user interface for device administrators to add macOS, iOS, and iPadOS devices to their Apple School Manager, Apple Business Manager, and Apple Business Essentials organizations. The provided SwiftUI view allows a user with device enrollment privileges to sign in with their Managed Apple ID and add devices to their organization.

This feature requires Bluetooth access to discover and pair with nearby devices, and camera access to scan visual pairing PIN codes. To use this feature, you must have the Automated Device Enrollment entitlement. To obtain permission for this entitlement, see Automated Device Enrollment Entitlement Request.

## Topics

### Essentials
- **automatedDeviceEnrollmentAddition(isPresented:)** - Presents a modal view that enables users to add devices to their organization.
- **com.apple.developer.automated-device-enrollment.add-devices** - A Boolean value that indicates whether an app may add a device to Automated Device Enrollment.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AutomatedDeviceEnrollment)*