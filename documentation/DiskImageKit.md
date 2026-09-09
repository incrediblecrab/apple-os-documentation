# DiskImageKit

Manage standalone and layered disk images for virtual-machine storage.

**Platforms:** macOS 27.0+

**Status:** Beta APIs; reviewed September 8, 2026.

## Overview

DiskImageKit creates and opens disk images independently of the guest filesystem stored inside them. Its primary integration is with [Virtualization](Virtualization.md): a `DiskImage` can back a `VZDiskImageStorageDeviceAttachment`.

The framework supports **Apple Sparse Image Format (ASIF)** and **raw** images. ASIF supports standalone images and layers. Raw images can be standalone or the base of a stack, but are not a replacement for ASIF overlay and cache layers. Opening encrypted images is not supported.

## Image and layer model

- A base image provides the underlying disk contents and can serve as a shared read-only foundation.
- An overlay records modifications without rewriting the shared base.
- A cache layer retains blocks read from a lower layer; a stack supports at most one cache layer.
- Layer order matters: the top layer determines the effective disk size and receives writes.

Use [`DiskImage.init(creating:)`](https://developer.apple.com/documentation/diskimagekit/diskimage/init(creating:)) for a new standalone/base image and [`init(opening:)`](https://developer.apple.com/documentation/diskimagekit/diskimage/init(opening:)) for an existing image or layer. `ASIFLayerCreationConfiguration` belongs in a stacking `appending` operation, not `init(creating:)`.

The [`VZDiskImageStorageDeviceAttachment` initializer](https://developer.apple.com/documentation/virtualization/vzdiskimagestoragedeviceattachment/init(diskimage:cachingmode:synchronizationmode:)) accepts the resulting image or stack. Its caching and synchronization arguments default to `.automatic` and `.full`, so `VZDiskImageStorageDeviceAttachment(diskImage:)` is a valid abbreviated call.

## Integrity and failure handling

ASIF images have layer UUIDs; raw images do not. A layer's parent UUID is set when its parent has a layer UUID. For noncache ASIF images, the layer UUID changes when the framework first writes to the image; **cache-layer UUIDs never change**. Appending an existing layer can fail when its recorded parent no longer matches. Preserve related layers together and handle [`IncompatibleStackingError`](https://developer.apple.com/documentation/diskimagekit/incompatiblestackingerror) instead of assuming any overlay can attach to any base.

Changing an image's block count does **not** resize its filesystem or partition map. Truncation cannot target a cache image; it affects the top layer of a stack and requires a positive block count. Shrinking below the guest's stored data can destroy that data. Plan guest-filesystem resizing and backups separately. Also handle invalid sizes, unsupported formats, damaged images, and POSIX errors such as missing files or denied access.

Disk-image management does not grant access to otherwise protected files. A VM app still needs the [Virtualization entitlement](https://developer.apple.com/documentation/virtualization/adding-the-virtualization-entitlement-to-your-project) and appropriate access to its storage locations.

## Topics

- [DiskImage](https://developer.apple.com/documentation/diskimagekit/diskimage)
- [StackedImage](https://developer.apple.com/documentation/diskimagekit/stackedimage)
- [OpenConfiguration](https://developer.apple.com/documentation/diskimagekit/openconfiguration)
- [ASIFCreationConfiguration](https://developer.apple.com/documentation/diskimagekit/asifcreationconfiguration)
- [ASIFLayerCreationConfiguration](https://developer.apple.com/documentation/diskimagekit/asiflayercreationconfiguration)
- [RAWCreationConfiguration](https://developer.apple.com/documentation/diskimagekit/rawcreationconfiguration)

## Sources

- [Apple framework reference](https://developer.apple.com/documentation/diskimagekit)
- [Readable framework documentation and integration examples](https://developer.apple.com/documentation/diskimagekit.md)
- [macOS 27 release notes — Disk Images](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes.md)
