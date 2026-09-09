# ExtensionFoundation

Create executable bundles to extend the functionality of other apps.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 16.0+ | macOS 13.0+ | tvOS 17.4+ | visionOS 1.1+ | watchOS 9.0+

## Overview

An app extension is an executable bundle embedded in an app. A host can discover and launch extensions implementing its extension points, but the extension's code runs in a **separate process**, not in the host's address space. The host and extension communicate through an agreed XPC interface.

Use ExtensionFoundation for the entry point, discovery, process management, and non-UI connection configuration. If the extension also provides remote UI, add [ExtensionKit](ExtensionKit.md). UI hosting and service execution are related workflows, not different rules for loading arbitrary code into the host.

## Choosing an extension workflow

Use a system feature's own framework for its extension model — for example [WidgetKit](WidgetKit.md) or [AppMigrationKit](AppMigrationKit.md). Adopt ExtensionFoundation directly when defining extension points for your own host app, discovering implementations, and communicating with them over XPC. Custom UI also needs [ExtensionKit](ExtensionKit.md).

The [current host-app guide](https://developer.apple.com/documentation/extensionfoundation/adding-support-for-app-extensions-to-your-app) describes `AppExtensionPoint.Definition` and an `.appext` file generated from code. Programmatic generation is a **26-generation** workflow enabled by `EX_ENABLE_EXTENSION_POINT_GENERATION = YES`; it is not a requirement to relabel every extension as OS 27-only. Existing hand-authored `.appext` files remain supported.

The host defines supported extension points and each extension binds to one. Keep the process handle while using its XPC connection and release it with `invalidate()` when finished. Discovery only exposes extensions that are available and enabled; separately shipped extensions require the person's approval.

### Per-symbol availability

- `AppExtension` and `AppExtensionConfiguration` declarations begin at iOS/iPadOS/Mac Catalyst/tvOS 16, macOS 13, watchOS 9, and visionOS 1.1. The framework catalog's tvOS 17.4 label differs from those declarations.
- `AppExtensionIdentity` and `AppExtensionProcess` begin at iOS/iPadOS/Mac Catalyst/tvOS/watchOS 26, macOS 13, and visionOS 1.1.
- `AppExtensionPoint`, `Definition`, and `ExtensionPointDefining` list 26 on the platforms above except visionOS, where their declarations retain 1.1.
- `ConnectionHandler` lists iOS/iPadOS/Mac Catalyst/macOS 26 and visionOS 1.1, without tvOS/watchOS declarations.

`Definition` is declared as an `@resultBuilder` structure, even though the guide calls it a property wrapper. Follow the declaration and compiler-supported syntax rather than expecting a `wrappedValue` property.

## Topics

### Essentials
- [Adding support for app extensions to your app](https://developer.apple.com/documentation/extensionfoundation/adding-support-for-app-extensions-to-your-app) - Define extension points and runtime communication.
- [Building an app extension to support a host app](https://developer.apple.com/documentation/extensionfoundation/building-an-app-extension-to-support-a-host-app) - Implement the separate extension process.
- [Discovering app extensions](https://developer.apple.com/documentation/extensionfoundation/discovering-app-extensions-from-your-app) - Find implementations that match the host's extension points.

### App Extensions
- [`AppExtensionIdentity`](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity) - An identity value obtained through discovery, not directly constructed.
- [`AppExtension`](https://developer.apple.com/documentation/extensionfoundation/appextension) - The extension entry-point protocol and configuration.
- [`AppExtensionConfiguration`](https://developer.apple.com/documentation/extensionfoundation/appextensionconfiguration) - A `Sendable` protocol for accepting the host's XPC connection.

### Host Apps
- [`AppExtensionProcess`](https://developer.apple.com/documentation/extensionfoundation/appextensionprocess) - A structure that launches or connects to a running extension process and manages the host's reference to it.

### Protocols
- [`ExtensionPointDefining`](https://developer.apple.com/documentation/extensionfoundation/extensionpointdefining) - Identifies extension-point types.

### Structures
- [`AppExtensionPoint`](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint) - Defines host extension points and extension bindings.
- [`ConnectionHandler`](https://developer.apple.com/documentation/extensionfoundation/connectionhandler) - Configures a closure accepting Foundation XPC connections or XPC sessions.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ExtensionFoundation)*
