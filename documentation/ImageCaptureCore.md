# ImageCaptureCore

Browse for media devices and control them programmatically from your app.

**Platforms:** iOS 13.0+ | iPadOS 13.0+ | Mac Catalyst 13.0+ | macOS 10.6+ | visionOS 1.0+

## Overview

Using ImageCaptureCore, your app can:

- Discover connected cameras and scanners
- View and modify the folders, files, and metadata on a connected camera
- Take photos directly on a connected camera using tethered capture
- Perform overview scans and scans on a connected scanner

### Configuring tethered capture and photo import

To import pictures and tether from a macOS app, you first need to enable the Hardened Runtime capability in Xcode, and then add the Photos Library Entitlement.

Before you can tether from an iOS app, you need to tell the user why the app is requesting access to an external camera. Add the NSCameraUsageDescription key to your Info.plist file with a description of your intended use.

> **Important:** In macOS 14 and later, use the com.apple.security.device.usb entitlement key to allow your sandboxed app to interact with USB devices.

## Topics

### Essentials
- **ICDeviceBrowser** - An object for finding digital cameras and scanners.
- **Photos Library Entitlement** - A Boolean value that indicates whether the app has read-write access to the user's Photos library.
- **NSCameraUsageDescription** - A message that tells people why the app is requesting access to the device's camera.

### Cameras  
- **ICCameraDevice** - An object that represents a camera.
- **ICCameraDeviceDelegate** - Methods for detecting cameras, getting metadata and thumbnails, handling access and capability changes, and performing other actions on connected cameras.
- **ICCameraItem** - An abstract class that represents a camera item.
- **ICCameraFile** - An object that represents a file on a camera.
- **ICCameraFolder** - An object that represents a folder on a camera.

### Scanners
- **ICScannerDevice** - An object that represents a scanner.
- **ICScannerDeviceDelegate** - Methods for determining availability, selecting a functional unit, and performing scans on connected scanners.
- **Scanner Configuration** - Examine a scanner's functional units and features.

### Errors
- **ICReturn** - An error returned from ImageCaptureCore.
- **ICLegacyReturn** - A legacy error returned from ImageCaptureCore.
- **ICReturnConnectionError** - A connection error returned from ImageCaptureCore.
- **ICReturnDownloadError** - A download error returned from ImageCaptureCore.
- **ICReturnMetadataError** - A metadata error returned from ImageCaptureCore.
- **ICReturnObjectError** - An object error returned from ImageCaptureCore.
- **ICReturnPTPDeviceError** - A PTP device error returned from ImageCaptureCore.
- **ICReturnThumbnailError** - A thumbnail error returned from ImageCaptureCore.

### Legacy Symbols
- **ICRunLoopMode** - (Deprecated)

### Articles
- **ImageCaptureCore Constants**
- **ImageCaptureCore Data Types**
- **ImageCaptureCore Enumerations**
- **ImageCaptureCore Macros**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ImageCaptureCore)*