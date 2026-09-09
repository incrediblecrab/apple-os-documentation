# ManagedSettingsUI

Define and configure the appearance of shielding views.

**Platforms:** iOS 15.0+ | iPadOS 15.0+ | Mac Catalyst 15.0+

## Overview

ManagedSettingsUI customizes the appearance of shields over restricted apps and websites. [ManagedSettings](ManagedSettings.md) handles restrictions, enforcement, and shield actions; changing the shield's appearance doesn't change authorization or access rules.

Subclass `ShieldConfigurationDataSource` in the shield configuration extension and return a configuration promptly. The extension's sandbox prevents network requests and moving sensitive content outside its address space. The system falls back to its appearance if a callback isn't overridden or takes too long, and supplies default values for configuration properties left `nil`.

On iOS/iPadOS/Mac Catalyst 26.4+, [`secondaryButtonSubmenuItems`](https://developer.apple.com/documentation/managedsettingsui/shieldconfiguration/secondarybuttonsubmenuitems) supports up to three strings for secondary-button menu actions. Handle the corresponding `ShieldAction` submenu cases in ManagedSettings. A `nil` or empty array retains the normal secondary-button action; the system adds the menu's Cancel action. This is a 26.4 feature, not an OS 27-only API.

## Topics

### Shield Configuration
- [`ShieldConfigurationDataSource`](https://developer.apple.com/documentation/managedsettingsui/shieldconfigurationdatasource) - The base class for the extension's appearance provider.
- [`ShieldConfiguration`](https://developer.apple.com/documentation/managedsettingsui/shieldconfiguration) - A structure specifying shield text, imagery, colors, and buttons.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ManagedSettingsUI)*
