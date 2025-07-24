# Keyboards

A physical keyboard can be an essential input device for entering text, playing games, controlling apps, and more.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS

## Overview

People can connect a physical keyboard to any device except Apple Watch. Mac users tend to use a physical keyboard all the time and iPad users often do. Many games work well with a physical keyboard, and people can prefer using one instead of a virtual keyboard when entering a lot of text.

Keyboard users often appreciate using keyboard shortcuts to speed up their interactions with apps and games. A keyboard shortcut is a combination of a primary key and one or more modifier keys (Control, Option, Shift, and Command) that map to a specific command. A keyboard shortcut in a game — called a key binding — often consists of a single key.

Apple defines standard keyboard shortcuts to work consistently across the system and most apps, helping people transfer their knowledge to new experiences. Some apps define custom keyboard shortcuts for the app-specific commands people use most; most games define custom key bindings that make it quick and efficient to use the keyboard to control the game.

## Topics

### Best Practices

- **Support Full Keyboard Access when possible** - Available in iOS, iPadOS, macOS, and visionOS, Full Keyboard Access lets people navigate and activate windows, menus, controls, and system features using only the keyboard. To test Full Keyboard Access in your app or game, turn it on in the Accessibility area of the system-supplied Settings app.
- **Respect standard keyboard shortcuts** - While using most apps, people generally expect to rely on the standard keyboard shortcuts that work in other apps and throughout the system. If your app offers a unique action that people perform frequently, prefer creating a custom shortcut for it instead of repurposing a standard one that people associate with a different action. While playing a game, people may expect to use certain standard keyboard shortcuts — such as Command–Q to quit the game — but they also expect to be able to modify each game's key bindings to fit their personal play style.

Important: Although iPadOS supports keyboard navigation in text fields, text views, and sidebars, and provides APIs you can use to support it in collection views and other custom views, avoid supporting keyboard navigation for controls, such as buttons, segmented controls, and switches. Instead, let people use Full Keyboard Access to activate controls, navigate to all onscreen components, and perform gesture-based interactions like drag and drop.

### Standard Keyboard Shortcuts

In general, don't repurpose standard keyboard shortcuts for custom actions. People can get confused when the shortcuts they know work differently in your app or game. Only consider redefining a standard shortcut if its action doesn't make sense in your experience. For example, if your app doesn't support text editing, it doesn't need a text-styling command like Italic, so you might repurpose Command–I for an action that has more relevance, like Get Info.

People expect each of the following standard keyboard shortcuts to perform the action listed:

**Common Shortcuts**
- **Command-Space** - Show or hide the Spotlight search field
- **Command-Tab** - Move forward to the next most recently used app
- **Command-A** - Select every item in a document or window
- **Command-C** - Copy the selection to the Clipboard
- **Command-V** - Paste the Clipboard contents at the insertion point
- **Command-X** - Remove the selection and store on the Clipboard
- **Command-Z** - Undo the previous operation
- **Command-S** - Save a new document or save a version of a document
- **Command-O** - Display a dialog for choosing a document to open
- **Command-P** - Display the Print dialog
- **Command-Q** - Quit the app
- **Command-W** - Close the active window
- **Command-N** - Open a new document
- **Command-F** - Open a Find window
- **Command-G** - Find the next occurrence of the selection
- **Esc** - Cancel the current action or process

**Text Formatting**
- **Command-B** - Boldface the selected text or toggle boldfaced text
- **Command-I** - Italicize the selected text or toggle italic text
- **Command-U** - Underline the selected text or turn underlining on/off

**System Functions**
- **Control-F1** - Toggle full keyboard access on or off
- **Command-M** - Minimize the active window to the Dock
- **Command-H** - Hide the windows of the currently running app
- **Shift-Command-3** - Capture the screen to a file
- **Shift-Command-4** - Capture a selection to a file

### Custom Keyboard Shortcuts

Define custom keyboard shortcuts for only the most frequently used app-specific commands. People appreciate using keyboard shortcuts for actions they perform frequently, but defining too many new shortcuts can make your app seem difficult to learn.

- **Use modifier keys in ways that people expect** - For example, pressing Command while dragging moves items as a group, and pressing Shift while drag-resizing constrains resizing to the item's aspect ratio.
- **Prefer the Command key as the main modifier key in a custom keyboard shortcut** - Use the Shift key as a secondary modifier that complements a related shortcut.
- **Use the Option modifier sparingly for less-common commands or power features** - Avoid using the Control key as a modifier. The system uses Control in many systemwide features and shortcuts.
- **List modifier keys in the correct order** - If you use more than one modifier key in a custom shortcut, always list them in this order: Control, Option, Shift, Command.
- **Avoid adding Shift to a shortcut that uses the upper character of a two-character key** - People already understand that they must hold the Shift key to type the upper character of a two-character key.
- **Let the system localize and mirror your keyboard shortcuts as needed** - The system automatically localizes a shortcut's primary and modifier keys to support the currently connected keyboard.
- **Avoid creating a new shortcut by adding a modifier to an existing shortcut for an unrelated command** - For example, because people are accustomed to using Command-Z for undoing an action, it would be confusing to use Shift-Command-Z as the shortcut for a command that's unrelated to undo and redo.

### Platform Considerations

**iPadOS, visionOS**  
In iPadOS and visionOS, an app's keyboard shortcuts appear in the shortcut interface that displays when people hold the Command key on a connected keyboard. Similar in organization to an app's menu bar menus on a Mac, the shortcut interface on iPad and Apple Vision Pro displays app commands in familiar system-defined menu categories such as File, Edit, and View.

- **Write descriptive shortcut titles** - Because the shortcut interface displays a flat list of all items in each category, submenu titles aren't available to provide context for their child items. Make sure each shortcut title is descriptive enough to convey its action without the additional context a submenu title might provide.
- **Consider customizing keyboard effects in your iPadOS app or game** - For example, you can customize visual effects that help people focus on individual items as they navigate your interface.
- **Recognize that people see an overlay when they use a physical keyboard with your visionOS app or game** - When people connect a physical keyboard while using your visionOS app or game, the system displays a virtual keyboard overlay that provides typing completion and other controls.

No additional considerations for iOS, macOS, or tvOS.

Not supported in watchOS.

### Related Components

- [Virtual keyboards](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards) - On-screen keyboards
- [Entering data](https://developer.apple.com/design/human-interface-guidelines/entering-data) - Data entry guidance
- [Pointing devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices) - Mouse and trackpad input
- [Game controls](https://developer.apple.com/design/human-interface-guidelines/game-controls) - Game-specific keyboard guidance
- [Focus-based navigation](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection) - Keyboard navigation
- [Right to left](https://developer.apple.com/design/human-interface-guidelines/right-to-left) - Localization guidance

### Developer Documentation

- [KeyboardShortcut](https://developer.apple.com/documentation/swiftui/keyboardshortcut) - SwiftUI
- [Input events](https://developer.apple.com/documentation/swiftui/input-events) - SwiftUI
- [Handling key presses made on a physical keyboard](https://developer.apple.com/documentation/uikit/keyboards_and_input/handling_key_presses_made_on_a_physical_keyboard) - UIKit
- [Mouse, Keyboard, and Trackpad](https://developer.apple.com/documentation/appkit/mouse_keyboard_and_trackpad) - AppKit
- [Support Full Keyboard Access in your iOS app](https://developer.apple.com/documentation/uikit/focus-based_navigation/supporting_full_keyboard_access_in_your_ios_app) - UIKit
- [isFullKeyboardAccessEnabled](https://developer.apple.com/documentation/uikit/uiaccessibility/1615143-isfullkeyboardaccessenabled) - UIKit
- [discoverabilityTitle](https://developer.apple.com/documentation/uikit/uikeycommand/1621097-discoverabilitytitle) - UIKit

## Changelog

### June 9, 2025
- Moved game-specific key bindings guidance to the Game controls page.

### June 10, 2024
- Added game-specific guidance and made organizational updates.

### June 21, 2023
- Updated to include guidance for visionOS.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/keyboards)*