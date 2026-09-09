# ExtensionKit

Present remote app-extension UI and manage enabled extensions.

**Platforms:** iOS 16.1+ | iPadOS 16.1+ | Mac Catalyst 16.0+ | macOS 13.0+ | tvOS 16.0+ | visionOS 1.0+ | watchOS 10.0+

## Overview

ExtensionKit works with [ExtensionFoundation](ExtensionFoundation.md) to present UI supplied by an extension running in a separate process. The extension defines its scenes; the host presents opaque remote content rather than executing the extension's code in its own address space. System features such as widgets retain their feature-specific extension workflows.

For a custom host, follow [Including extension-based UI in your interface](https://developer.apple.com/documentation/extensionkit/including-extension-based-ui-in-your-interface): the extension supplies an `AppExtensionScene`, and the host presents its remote UI through `EXHostViewController`. The [extension browser](https://developer.apple.com/documentation/extensionkit/displaying-the-app-extensions-available-to-your-app) lets people enable and disable matching extensions. Keep this distinct from [UIKit app scenes](UIKit.md#required-scene-life-cycle-and-launch-screen) and from system-specific widget or migration extensions.

The host's extension point must permit UI. Configure the host controller with an extension identity and scene identifier; each controller displays one extension scene at a time. Host-bundled extensions are enabled by default, while extensions shipped in separate apps are disabled until the person enables them.

### Hosting and scene availability

`EXHostViewController` requires iOS/iPadOS/Mac Catalyst 26 or macOS 13. The extension browser requires iOS/iPadOS/Mac Catalyst 18 or macOS 13. Neither controller declares support for tvOS, watchOS, or visionOS, even though the framework contains types for those platforms.

The scene protocol, primitive scene, result builder, and scene configuration declare iOS/iPadOS/Mac Catalyst/tvOS 16, macOS 13, visionOS 1, and watchOS 9. Those iOS/watchOS values differ from the aggregate framework header. Do not assign the header's minimum to every scene or host-controller API.

## Topics

### UI App Extensions
- [`AppExtensionScene`](https://developer.apple.com/documentation/extensionkit/appextensionscene) - A main-actor protocol providing a named extension scene.
- [`AppExtensionSceneConfiguration`](https://developer.apple.com/documentation/extensionkit/appextensionsceneconfiguration) - A structure conforming to `AppExtensionConfiguration` for extensions with UI.
- [`AppExtensionSceneBuilder`](https://developer.apple.com/documentation/extensionkit/appextensionscenebuilder) - A result-builder structure that combines extension scenes.
- [`PrimitiveAppExtensionScene`](https://developer.apple.com/documentation/extensionkit/primitiveappextensionscene) - Supplies a scene identifier, content, and optional scene-specific connection handling.

### Host Apps
- [`EXHostViewController`](https://developer.apple.com/documentation/extensionkit/exhostviewcontroller) - Hosts remote content for the configured identity and scene.
- [`EXAppExtensionBrowserViewController`](https://developer.apple.com/documentation/extensionkit/exappextensionbrowserviewcontroller) - Presents system-managed extension approval and enable/disable controls.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ExtensionKit)*
