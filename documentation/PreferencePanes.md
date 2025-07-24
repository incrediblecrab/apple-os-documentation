# Preference Panes

Integrate your app's custom preferences into the System Preferences app.

**Platforms:** Mac Catalyst 14.0+ | macOS 10.1+

## Overview

Use the Preference Panes framework to integrate your custom system-level preferences into the System Preferences app. You use this framework to implement a preference pane bundle, which contains the custom interface you want to display to the user. You then install your bundle in the appropriate Library/PreferencePanes directory on the user's system.

System Preferences works with your bundle's custom NSPreferencePane object to manage the presentation of your custom interface to the user. System Preferences loads the view provided by your bundle and delivers lifecycle events to your preference pane object. Use that object to respond to interactions with the controls and views of your interface and to save any settings changes to the user's defaults database.

**Note:** Use preference pane bundles only for settings that must be managed separately from your app. For example, use it to manage settings that are shared between multiple apps in the same suite. Manage app-specific preferences using a custom preferences interface.

## Topics

### Preference Pane Interface

- **NSPreferencePane** - The interface for providing preference panes to System Preferences or other apps.

### Notifications

- **NSPreferencePrefPaneIsAvailable** - Notifies observers that the system preferences app is available to display your preferences.
- **NSPreferencePaneDoUnselect** - Notifies observers that the preference pane may be deselected.
- **NSPreferencePaneCancelUnselect** - Notifies observers that the preference pane should not be deselected.
- **NSPreferencePaneSwitchToPane** - Notifies observers that the user selected a new preference pane.
- **NSPreferencePaneUpdateHelpMenu** - Notifies observers that your help menu content changed.

### Help Menu Keys

- **NSPrefPaneHelpMenuInfoPListKey** - The global help menu items associated with a preference pane.
- **NSPrefPaneHelpMenuTitleKey** - The title of a help menu item in a preference pane.
- **NSPrefPaneHelpMenuAnchorKey** - The help book anchor to display.

### Reference

- [PreferencePanes Constants](https://developer.apple.com/documentation/PreferencePanes/constants)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/PreferencePanes)*