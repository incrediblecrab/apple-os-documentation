# Digit Entry Views

A digit entry view fills the entire screen and prompts people to enter a series of digits, like a PIN, using a digit-specific keyboard.

**Platforms:** tvOS

## Overview

You can add an optional title and prompt above the line of digits.

## Topics

### Best Practices

- **Use secure digit fields** - Secure digit fields display asterisks instead of the entered digit onscreen. Always use a secure digit field when your app asks for sensitive data.

- **Clearly state the purpose of the digit entry view** - Use a title and prompt that explains why someone needs to enter digits.

### Platform Considerations

Not supported in iOS, iPadOS, macOS, visionOS, or watchOS.

### Related Components

- [Virtual keyboards](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards) - Onscreen keyboards for text and digit input

### Developer Documentation

- [TVDigitEntryViewController](https://developer.apple.com/documentation/tvuikit/tvdigitentryviewcontroller) - TVUIKit

---

*Design baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Reviewed 2026-08-09.*

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/digit-entry-views)*