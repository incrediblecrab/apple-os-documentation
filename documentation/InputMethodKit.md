# InputMethodKit

Develop input methods and manage communication with client applications, candidates windows, and input method modes.

**Platforms:** macOS 10.5+

## Overview

The Input Method Kit, introduced in OS X v10.5, provides a streamlined programming interface that lets you develop input methods with far less code than older Mac programming interfaces. It is fully integrated with the Text Services Manager. The Input Method Kit allows 32-bit applications to work with 64-bit applications.

The Input Method Kit provides classes and protocols for managing communication with client applications, candidates windows, and input method modes. Input methods supply text from a conversion engine (written in any language, such as C, C++, Objective-C, Python, and so on), key bindings and optional event handling, and information about your input method in an extended Info.plist file. You also have the option to provide menu items that support input-method-specific commands or preferences settings.

## Topics

### Classes
- **IMKCandidates** - The IMKCandidates class presents candidates to users and notifies the appropriate IMKInputController object when the user selects a candidate. Candidates are alternate characters for a given input sequence. The IMKCandidates class supports using a candidates window in your input method; using IMKCandidates is optional. Not all input methods require them.
- **IMKInputController** - The IMKInputController class provides a base class for custom input controller classes. The IMKServer class, which is allocated in the main function of an input method, creates an input controller object for each input session created by a client application. For every input session there is a corresponding IMKInputController object.
- **IMKServer** - The IMKServer class manages client connections to your input method. When you write the main function for your input method, you create an IMKServer object. You should never need to override this class.

### Protocols
- **IMKMouseHandling** - The IMKMouseHandling protocol defines methods that your input method can implement to handle mouse events.
- **IMKServerInput** - IMKServerInput is an informal protocol that defines methods for receiving text events. This is intentionally not a formal protocol because there are three ways to receive events. An input method chooses one of the following approaches and implements the appropriate methods.
- **IMKStateSetting** - The IMKStateSetting protocol defines methods for setting or accessing values that indicate the state of an input method.

### Reference
- [InputMethodKit Enumerations](https://developer.apple.com/documentation/inputmethodkit/inputmethodkit_enumerations)
- [InputMethodKit Constants](https://developer.apple.com/documentation/inputmethodkit/inputmethodkit_constants)
- [InputMethodKit Data Types](https://developer.apple.com/documentation/inputmethodkit/inputmethodkit_data_types)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/InputMethodKit)*