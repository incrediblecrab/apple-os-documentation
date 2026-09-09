# Bundle Resources

Resources located in an app, framework, or plugin bundle.

**Platforms:** iOS | iPadOS | Mac Catalyst | macOS | tvOS | visionOS | watchOS

This is a resource-format and configuration-key reference, not a uniform runtime API minimum. Check each resource or key's availability; the catalog's “Mac Catalyst 2.0” label is not a usable Catalyst deployment target.

## Overview

A bundle is a directory with a standardized hierarchical structure that typically packages executable code and resources. Resources can include images, audio files, user interface files, and property lists; their correct locations depend on the bundle type and platform.

## UI design compatibility

[`UIDesignRequiresCompatibility`](https://developer.apple.com/documentation/bundleresources/information-property-list/uidesignrequirescompatibility) is a temporary UI compatibility switch introduced in the 26 generation. `YES` requests the earlier design; `NO` (or omission for apps linked against the latest SDKs) uses the running OS's UI design.

Apple explicitly says the system **ignores this key when you build for iOS 27+, iPadOS 27+, Mac Catalyst 27+, macOS 27+, or tvOS 27+**. Do not extend that list to watchOS or visionOS, or replace it with a blanket claim about every Xcode 27 build. Xcode 27 can build apps with older deployment targets, including OS 26; the SDK, build target, and running OS are distinct. Test each supported combination rather than promising an appearance based only on the SDK number.

For the separate scene-manifest and launch-screen requirements in 27 SDK builds, see [UIKit migration](UIKit.md#os-27-migration). Use [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass) as the design migration reference.

## Topics

### Property Lists
- [Entitlements](https://developer.apple.com/documentation/bundleresources/entitlements) - Key-value pairs that grant an executable permission to use a service or technology.
- [Information Property List](https://developer.apple.com/documentation/bundleresources/information-property-list) - A resource containing key-value pairs that identify and configure a bundle.
- [Privacy manifest files](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files) - Describe the data your app or third-party SDK collects and the required reasons APIs it uses.

### Structure
- [Placing content in a bundle](https://developer.apple.com/documentation/bundleresources/placing-content-in-a-bundle) - Place bundle content in the correct location based on its type.

### Universal links service
- [`applinks`](https://developer.apple.com/documentation/bundleresources/applinks) - The root object for a universal links service definition.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/BundleResources)*
