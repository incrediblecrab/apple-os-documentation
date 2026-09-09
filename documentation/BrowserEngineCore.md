# BrowserEngineCore

Integrate an alternative browser engine into your web browser app.

**Platforms:** iOS 17.4+ | iPadOS 18.0+

## Overview

Use the BrowserEngineCore framework to support low-level functions for your alternative browser engine that renders its UI using BrowserEngineKit. For more information on developing web browser apps, see [Designing your browser architecture](https://developer.apple.com/documentation/browserenginekit/designing-your-browser-architecture).

This framework is not a web-content rendering API or a way to opt arbitrary apps into Safari 27 features. Follow [BrowserEngineKit's regional and entitlement requirements](BrowserEngineKit.md#regional-and-embedding-requirements) and check [BrowserKit](BrowserKit.md) eligibility. Keep the multi-process engine architecture separate from ordinary [WKWebView embedding](WebKit.md#native-embedding-apis).

## Topics

### Kernel Events

The event functions require **iOS/iPadOS 18.4+**, later than the framework's introduction. Their names distinguish the event-record layouts, not support for running a 32-bit browser process.

- [`be_kevent(_:_:_:_:_:_:)`](https://developer.apple.com/documentation/browserenginecore/be_kevent(_:_:_:_:_:_:)) - Registers and retrieves events using `kevent` records.
- [`be_kevent64(_:_:_:_:_:_:)`](https://developer.apple.com/documentation/browserenginecore/be_kevent64(_:_:_:_:_:_:)) - Uses `kevent64_s` records instead. Both functions take six arguments, ending in flags, rather than a timeout argument.
- [`BE_KEVENT_NO_FLAGS`](https://developer.apple.com/documentation/browserenginecore/be_kevent_no_flags) - Requests the default behavior.
- [`BE_KEVENT_RETURN_IMMEDIATELY`](https://developer.apple.com/documentation/browserenginecore/be_kevent_return_immediately) - Polls without waiting for events.

Check error records as well as the return value: an error can appear as an `EV_ERROR` event. The functions return `-1` with `errno` when they cannot record an error in the output array.

### JIT Compilation
- [`BE_JIT_WRITE_PROTECT_TAG`](https://developer.apple.com/documentation/browserenginecore/be_jit_write_protect_tag) - A pointer-authentication discriminator for JIT write protection, not permission to execute arbitrary writable memory. Follow [Protecting code compiled just in time](https://developer.apple.com/documentation/browserenginekit/protecting-code-compiled-just-in-time).

### Classes
- [`BEAudioSession`](https://developer.apple.com/documentation/browserenginecore/beaudiosession-7bb2q) - An **iOS/iPadOS 26+** wrapper that gives a browser extension scoped access to audio output while the main browser retains control of the audio-session configuration.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/BrowserEngineCore)*
