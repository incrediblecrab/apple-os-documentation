# MatterSupport

Coordinate and control compatible smart home accessories.

**Platforms:** iOS 16.1+ | iPadOS 16.1+ | Mac Catalyst 14.0+ | macOS 14.0+ | visionOS 1.0+

## Overview

Matter is a smart home connectivity standard that gives your app the ability to control devices from a wide variety of manufacturers and across platforms. Adopt this framework in your app to add compatible devices to your ecosystem, then use Matter to commission and control them.

**Important:** Calls to this framework return errors to Mac apps built with Mac Catalyst.

## Topics

### Adding a device
- [Adding Matter support to your ecosystem](https://developer.apple.com/documentation/mattersupport/adding_matter_support_to_your_ecosystem) - Allow people to add Matter accessories to your platform.
- **MatterAddDeviceRequest** - A request that adds and sets up a device into an ecosystem.
- **MatterAddDeviceExtensionRequestHandler** - The object that handles configuration and commissioning of a device into an ecosystem.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MatterSupport)*