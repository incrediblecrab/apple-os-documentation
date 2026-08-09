# BrowserEngineCore

Integrate an alternative browser engine into your web browser app.

**Platforms:** iOS 17.4+ | iPadOS 18.0+

## Overview

Use the BrowserEngineCore framework to support low-level functions for your alternative browser engine that renders its UI using BrowserEngineKit. For more information on developing web browser apps, see [Designing your browser architecture](https://developer.apple.com/documentation/browserenginekit/designing_your_browser_architecture).

## Topics

### Kernel Events
- **be_kevent** - Registers for kernel events on the specified queue, and returns events that are pending on the queue, using 32-bit data types.
- **be_kevent64** - Registers for kernel events on the specified queue, and returns events that are pending on the queue, using 64-bit data types.
- **BE_KEVENT_NO_FLAGS** - Indicates that no flags are set in a request to receive kernel events.
- **BE_KEVENT_RETURN_IMMEDIATELY** - Indicates that a request to receive kernel events needs to return without waiting for events.

### JIT Compilation
- **BE_JIT_WRITE_PROTECT_TAG** - A discriminator value the system uses to generate pointer authentication codes for just-in-time compilation.

### Classes
- **BEAudioSession** - An object that represents an audio session.
---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/BrowserEngineCore)*