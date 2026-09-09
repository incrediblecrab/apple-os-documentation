# InputMethodKit

Develop input methods and manage communication with client applications, candidates windows, and input method modes.

**Platforms:** macOS 10.5+

## Overview

Input Method Kit was introduced in OS X 10.5 and integrates input methods with the Text Services Manager. The original reference's discussion of 32-bit/64-bit interoperability is historical: [macOS Catalina 10.15 and later don't run 32-bit apps](https://support.apple.com/en-us/103076). Use the current [AppKit text APIs](AppKit.md#controls-input-and-observation) alongside these input-method-specific interfaces.

InputMethodKit manages client connections, candidate windows, and input modes. Your input method supplies the conversion engine, key bindings or event handling, and `Info.plist` metadata. It can also supply menu commands and preferences. The framework doesn't provide your language-conversion logic.

## Topics

### Classes
- [`IMKCandidates`](https://developer.apple.com/documentation/inputmethodkit/imkcandidates) - Optional candidate-window support. The input controller supplies alternate text and handles candidate selections.
- [`IMKInputController`](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller) - An input-session controller created by the server for each client session. Its default mouse/state methods forward to implemented delegate methods.
- [`IMKServer`](https://developer.apple.com/documentation/inputmethodkit/imkserver) - Owns client connections; normally created by the input method rather than subclassed.

### Protocols and input callbacks
- [`IMKMouseHandling`](https://developer.apple.com/documentation/inputmethodkit/imkmousehandling) - Mouse-event handling methods.
- [`IMKServerInput`](https://developer.apple.com/documentation/inputmethodkit/imkserverinput) - An informal set of `NSObject` callbacks, not a standalone formal protocol to adopt. Choose key-binding dispatch (`inputText(_:client:)` and `didCommand(by:client:)`), unpacked text/key/modifier input (`inputText(_:key:modifiers:client:)`), or direct events (`handle(_:client:)`).
- [`IMKStateSetting`](https://developer.apple.com/documentation/inputmethodkit/imkstatesetting) - Input-method activation, modes, preferences, and state access.

### Reference
- [InputMethodKit Enumerations](https://developer.apple.com/documentation/inputmethodkit/inputmethodkit-enumerations)
- [InputMethodKit Constants](https://developer.apple.com/documentation/inputmethodkit/inputmethodkit-constants)
- [InputMethodKit Data Types](https://developer.apple.com/documentation/inputmethodkit/inputmethodkit-data_types)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/InputMethodKit)*
