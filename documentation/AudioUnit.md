# Audio Unit

Add sophisticated audio manipulation and processing capabilities to your app.

**Platforms:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 13.0+ | macOS 10.0+ | tvOS 9.0+ | visionOS 1.0+

> **Deprecated:** Use the Audio Unit types in Audio Toolbox instead.

## Overview

The Audio Unit framework provides interfaces for hosting either version 2 or version 3 audio units and implementing version 3 audio processing plug-ins known as Audio Unit extensions. Developers implementing version 3 audio units should subclass the AUAudioUnit class.

Version 3 Audio Unit extensions can be used on iOS, tvOS, and macOS by host apps and distributed via the App Store.

## Topics

### Variables
- **AUDIO_UNIT_VERSION**

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AudioUnit)*