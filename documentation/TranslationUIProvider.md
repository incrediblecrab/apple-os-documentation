# TranslationUIProvider

Provide UI for translations of text people select.

**Platforms:** iOS 18.4+ | iPadOS 18.4+ | Mac Catalyst 18.4+

## Overview

The **TranslationUIProvider** framework enables your app to provide custom translation UI for text that users select across the system. Use this framework to create app extensions that integrate with system translation workflows.

On iOS and iPadOS 18.4 and later, people can choose a default translation app. This integration requires the `com.apple.developer.translation-app` entitlement and a translation UI extension. If the extension needs networking, set `com.apple.developer.translation-ui-provider.network-access` to `true` in the app's `Info.plist`; framework availability alone does not configure these requirements.

## Topics

### Essentials
- [Preparing your app to be the default translation app](https://developer.apple.com/documentation/translationuiprovider/preparing-your-app-to-be-the-default-translation-app.md) - Configure your app so people can set it as the default translation app on their device.

### Extension context and protocols
- **TranslationUIProviderContext** - An object that encapsulates the XPC communication between the host process and the third-party extension implementation.
- **TranslationUIProviderExtension** - A protocol that translation apps implement to provide a text-selection view.
- **TranslationUIProviderExtensionScene** - The protocol this extension's scene need to implement.

### Configuration and Text Selection
- **TranslationProviderUIExtensionConfiguration** - The type for a translation UI provider extension's configuration object.
- **TranslationUIProviderSelectedTextScene** - The specific app extension scene that this extension provides.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/TranslationUIProvider)*
