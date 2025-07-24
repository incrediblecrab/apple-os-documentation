# TranslationUIProvider

Provide UI for translations of text people select.

**Platforms:** iOS 18.4+ | iPadOS 18.4+

## Overview

The **TranslationUIProvider** framework enables your app to provide custom translation UI for text that users select across the system. Use this framework to create app extensions that integrate with system translation workflows.

## Topics

### Essentials
- [Preparing your app to be the default translation app](https://developer.apple.com/documentation/translationuiprovider/preparing_your_app_to_be_the_default_translation_app) - Configure your app so people can set it as the default translation app on their device.
- [Creating translation app extensions](https://developer.apple.com/documentation/translationuiprovider/creating_translation_app_extensions) - Build app extensions that provide translation services.

### Core Protocols
- **TranslationUIProviderContext** - An object that encapsulates the XPC communication between the host process and the third-party extension implementation.
- **TranslationUIProviderExtension** - A protocol that translation apps implement to provide a text-selection view.
- **TranslationUIProviderExtensionScene** - The protocol this extension's scene need to implement.

### Configuration and Text Selection
- **TranslationProviderUIExtensionConfiguration** - The type for a translation UI provider extension's configuration object.
- **TranslationUIProviderSelectedTextScene** - The specific app extension scene that this extension provides.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/TranslationUIProvider)*