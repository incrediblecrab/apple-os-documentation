# Preference Panes

Integrate your app's custom preferences into the System Preferences app.

**Reference platform metadata:** Mac Catalyst 14.0+ | macOS 10.1+

## Overview

This is a legacy reference for System Preferences plug-in bundles, not the default way to add settings to a modern app. For app-specific settings on macOS, use a [SwiftUI `Settings` scene](https://developer.apple.com/documentation/swiftui/settings) (macOS 11+) or an AppKit settings interface. `Settings` is macOS-only; the framework's Catalyst metadata doesn't make that alternative available in Catalyst. Do not infer current System Settings extension-hosting behavior solely from historical API minima.

In the documented System Preferences model, package an `NSPreferencePane` subclass and its interface resources in a `.prefPane` bundle in an appropriate `Library/PreferencePanes` directory.

The host loads the pane's main view and delivers selection/deselection lifecycle callbacks. The pane initializes controls from stored preferences, handles interactions, and persists changes; loading the pane doesn't save settings automatically.

**Note:** Use preference pane bundles only for settings that must be managed separately from your app. For example, use it to manage settings that are shared between multiple apps in the same suite. Manage app-specific preferences using a custom preferences interface.

## Topics

### Preference Pane Interface

- [`NSPreferencePane`](https://developer.apple.com/documentation/preferencepanes/nspreferencepane) - The preference-hosted pane interface.

### Notifications

- [`NSPreferencePrefPaneIsAvailable`](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nspreferenceprefpaneisavailable) - The preferences host is available.
- [`NSPreferencePaneDoUnselect`](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nspreferencepanedounselect) - A deferred deselection is approved.
- [`NSPreferencePaneCancelUnselect`](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nspreferencepanecancelunselect) - A deferred deselection is refused.
- [`NSPreferencePaneSwitchToPane`](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nspreferencepaneswitchtopane) - A different preference pane was selected.
- [`NSPreferencePaneUpdateHelpMenu`](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nspreferencepaneupdatehelpmenu) - Help content changed; the notification object contains an array of help-item dictionaries.

### Help Menu Keys

- [`NSPrefPaneHelpMenuInfoPListKey`](https://developer.apple.com/documentation/preferencepanes/nsprefpanehelpmenuinfoplistkey) - The global help-item property-list key.
- [`NSPrefPaneHelpMenuTitleKey`](https://developer.apple.com/documentation/preferencepanes/nsprefpanehelpmenutitlekey) - A help item's title key.
- [`NSPrefPaneHelpMenuAnchorKey`](https://developer.apple.com/documentation/preferencepanes/nsprefpanehelpmenuanchorkey) - A help-book anchor key.

### Reference

- [PreferencePanes Constants](https://developer.apple.com/documentation/preferencepanes/preferencepanes-constants)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/PreferencePanes)*
