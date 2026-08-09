# Bundle Resources

Resources located in an app, framework, or plugin bundle.

**Platforms:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 2.0+ | macOS 10.0+ | tvOS 9.0+ | visionOS 1.0+ | watchOS 2.0+

## Overview

A bundle is a directory with a standardized hierarchical structure that holds executable code and the resources used by that code. The bundle contains resources for you to access at runtime, such as images, audio files, user interface files, and property lists.

> **iOS 27+, iPadOS 27+, macOS Golden Gate 27+, tvOS 27+, watchOS 27+, visionOS 27+:** The **`UIDesignRequiresCompatibility`** Info.plist key is **ignored by the OS 27 SDK**. It remains effective only for apps still linked against the OS 26 SDK, which keep the legacy appearance even when running on OS 27. Once you rebuild with Xcode 27, Liquid Glass applies with no supported override.

## Topics

### Property Lists
- [Entitlements](https://developer.apple.com/documentation/bundleresources/entitlements) - Key-value pairs that grant an executable permission to use a service or technology.
- [Information Property List](https://developer.apple.com/documentation/bundleresources/information_property_list) - A resource containing key-value pairs that identify and configure a bundle.
- [Privacy manifest files](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files) - Describe the data your app or third-party SDK collects and the required reasons APIs it uses.

### Structure
- [Placing content in a bundle](https://developer.apple.com/documentation/bundleresources/placing_content_in_a_bundle) - Place bundle content in the correct location based on its type.

### Universal links service
- **applinks** - The root object for a universal links service definition.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/BundleResources)*
