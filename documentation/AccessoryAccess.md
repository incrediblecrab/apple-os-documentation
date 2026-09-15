# Accessory Access

Discover connected USB accessories and coordinate access to them on Mac.

**Platforms:** macOS 27.0+

**Status:** OS 27 APIs; reviewed September 8, 2026.

## Overview

AccessoryAccess connects an app's interest in particular USB devices with the access needed to use them through [IOUSBHost](IOUSBHost.md). Register matching criteria and a listener with the shared `AAUSBAccessoryManager`; the manager supplies an `AAUSBAccessory` when a matching accessory connects.

This is separate from [AccessorySetupKit](AccessorySetupKit.md), which provides an accessory-setup experience on its supported platforms. Do not substitute one framework's availability or authorization model for the other.

## Configuration and lifecycle

Enable the Boolean [`com.apple.developer.accessory-access.usb`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.accessory-access.usb) entitlement in the app's Xcode configuration. Without it, API calls return `internalError` with “Unable to communicate with service.” The manager presents UI on the app's behalf, so the caller must be an application with a UI that appears in the Dock, not a headless service.

Obtain the manager through its shared property instead of constructing one directly. Register an [`AAUSBAccessoryListener`](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorylistener) with [`AAUSBAccessoryMatchingCriteria`](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymatchingcriteria). Notifications arrive on the manager's internal serial queue while the listener remains registered. Move UI updates to the appropriate UI execution context.

An accessory can be opened exclusively for transfers. Discovery is not a guarantee of access: another client may already be using it, it may disconnect, or its state may change before the operation completes.

## Failure handling and release notes

Handle [`AAError.Code`](https://developer.apple.com/documentation/accessoryaccess/aaerror/code), including an already-registered listener, inaccessible accessory, and invalid accessory state. Errors may also originate in lower-level frameworks. Unregister listeners and stop using disconnected accessories rather than retaining stale access indefinitely.

The macOS 27 release notes mark the earlier App Sandbox and macOS-VM support issues as **resolved**. They are not current blanket prohibitions; still test the app's actual sandbox, entitlement, and virtualized-device configuration.

## Topics

- [AAUSBAccessoryManager](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymanager)
- [AAUSBAccessory](https://developer.apple.com/documentation/accessoryaccess/aausbaccessory)
- [AAUSBAccessoryMatchingCriteria](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymatchingcriteria)
- [AAUSBAccessoryListener](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorylistener)
- [AAError](https://developer.apple.com/documentation/accessoryaccess/aaerror)

## Sources

- [Apple framework reference](https://developer.apple.com/documentation/accessoryaccess)
- [Manager requirements](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymanager.md)
- [macOS 27 release notes — Accessory Access](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes.md)
