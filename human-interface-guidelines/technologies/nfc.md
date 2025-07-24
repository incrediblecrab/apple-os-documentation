# NFC

Near-field communication (NFC) allows devices within a few centimeters of each other to exchange information wirelessly.

**Platforms:** iOS | iPadOS

## Overview

iOS apps running on supported devices can use NFC scanning to read data from electronic tags attached to real-world objects. For example, a person can scan a toy to connect it with a video game, a shopper can scan an in-store sign to access coupons, or a retail employee can scan products to track inventory.

## Topics

### In-App Tag Reading

An app can support single- or multiple-object scanning when the app is active, and display a scanning sheet whenever people are about to scan something.

- **Don't encourage people to make contact with physical objects** - To scan a tag, an iOS device must simply be within close proximity of the tag. It doesn't need to actually touch the tag. Use terms like "scan" and "hold near" instead of "tap" and "touch" when asking people to scan objects.

- **Use approachable terminology** - Near-field communication may be unfamiliar to some people. To make it approachable, avoid referring to technical, developer-oriented terms like NFC, Core NFC, Near-field communication, and tag. Instead, use friendly, conversational terms that most people will understand.

- **Provide succinct instructional text for the scanning sheet** - Provide a complete sentence, in sentence case, with ending punctuation. Identify the object to scan, and revise the text appropriately for subsequent scans. Keep the text short to avoid truncation.

#### Recommended Language

**Use:**
- "Scan the [object name]."
- "Hold your iPhone near the [object name] to learn more about it."

**Don't use:**
- "Scan the NFC tag."
- "To use NFC scanning, tap your phone to the [object]."

#### Instructional Text Examples

**First scan:** "Hold your iPhone near the [object name] to learn more about it."

**Subsequent scans:** "Now hold your iPhone near another [object name]."

### Background Tag Reading

Background tag reading lets people scan tags quickly any time, without needing to first open your app and initiate scanning. On devices that support background tag reading, the system automatically looks for nearby compatible tags whenever the screen is illuminated.

- **Support both background and in-app tag reading** - Your app must still provide an in-app way to scan tags, for people with devices that don't support background tag reading.

Note that background reading isn't available when an NFC scanning sheet is visible, Wallet or Apple Pay are in use, cameras are in use, the device is in Airplane Mode, and the device is locked after a restart.

### Developer Documentation

- [Core NFC](https://developer.apple.com/documentation/corenfc) - Core NFC

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/nfc)*