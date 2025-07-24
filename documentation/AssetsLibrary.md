# Assets Library

Access the assets in a user's media library.

**Platforms:** iOS 4.0+ | iPadOS 4.0+ | Mac Catalyst 14.0+

## Overview

Use the Assets Library framework to access the pictures and videos managed by the Photos application.

> **Important:** The Assets Library framework is deprecated as of iOS 9.0. Instead, use the PhotoKit framework, which in iOS 8.0 and later provides more features and better performance for working with a user's photo library.

## Topics

### Classes
- **ALAsset** - An ALAsset object represents a photo or a video managed by the Photo application. *Deprecated*
- **ALAssetRepresentation** - An ALAssetRepresentation object encapsulates one of the representations of a given ALAsset object. *Deprecated*
- **ALAssetsFilter** - ALAssetsFilter encapsulates filtering criteria to be used when retrieving assets from a group. *Deprecated*
- **ALAssetsGroup** - An ALAssetsGroup object represents an ordered set of the assets managed by the Photos application. The order of the elements is the same as the user sees in the Photos application. An asset can belong to multiple assets groups. *Deprecated*
- **ALAssetsLibrary** - An instance of ALAssetsLibrary provides access to the videos and photos that are under the control of the Photos application. *Deprecated*

### Reference
- **AssetsLibrary Enumerations**
- **AssetsLibrary Constants**
- **AssetsLibrary Data Types**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AssetsLibrary)*