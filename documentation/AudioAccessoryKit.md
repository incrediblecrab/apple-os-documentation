# AudioAccessoryKit

Report an audio accessory's capabilities and state for system-managed audio features.

**Platforms:** iPhone and iPad only. Framework metadata specifies iOS 26.4+; the fixed-spatial-audio feature described in the 27 release notes is for iOS 27 and iPadOS 27 testing.

**Status:** Reviewed September 8, 2026. Fixed spatial audio is **developer-testing-only**, with EU customer availability planned for a later iOS/iPadOS 27 release—not globally shipping.

## Overview

AudioAccessoryKit lets a third-party accessory manufacturer communicate headphone information to the system. The documented automatic-switching workflow reports placement and connected audio sources so the system can make routing decisions, such as moving audio away from headphones that were removed.

Pair with [AccessorySetupKit](AccessorySetupKit.md) first. Register the resulting accessory with `AccessoryControlDevice`, declaring only the capabilities the hardware implements. Keep configuration current as placement and Bluetooth connections change.

## Platform and regional distinctions

The framework overview permits developer testing in any region and limits customer use to devices located in the EU with an Apple Account whose country or region is in the EU. These restrictions are separate from symbol availability.

The iOS/iPadOS 27 release notes add a narrower status for the new **fixed spatial audio** support: testing on iPhone and iPad now, customer availability in a later 27 release in the EU. An SDK import or an older automatic-switching API does not establish customer eligibility for that new feature.

Apple's top-level symbol metadata does not specify an iPadOS introduction version even though the overview names iPad. Check the particular API and target SDK instead of assigning an unverified minimum version to every iPad feature.

## Configuration and failure handling

[`AccessoryControlDevice`](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice) manages registration, capabilities, and configuration. Its placement values distinguish states such as on-head, in-ear, and off-head. Connected-source information also needs updates when a source connects or disconnects.

Handle registration and configuration errors, loss of the paired accessory, and unsupported capabilities. Do not assume that changing a configuration forces a particular route or guarantees spatial rendering. Accessory state should reflect the hardware, not a guessed state used to influence routing.

This framework is not a replacement for normal app audio-session management. Companion-app pairing and system eligibility remain prerequisites.

## Topics

- [Supporting automatic audio switching](https://developer.apple.com/documentation/audioaccessorykit/supporting-automatic-audio-switching)
- [AccessoryControlDevice](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice)
- [Capabilities](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/capabilities)
- [Placement](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/placement)
- [Configuration](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/configuration-swift.struct)
- [Error](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/error)

## Sources

- [Apple framework reference](https://developer.apple.com/documentation/audioaccessorykit)
- [Framework overview and regional restrictions](https://developer.apple.com/documentation/audioaccessorykit.md)
- [iOS/iPadOS 27 release notes — AudioAccessoryKit](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes.md)
