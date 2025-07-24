# Settings

People expect apps and games to just work, but they also appreciate having ways to customize the experience to fit their needs.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

On all Apple platforms, the system-provided Settings app lets people adjust things like the overall appearance of the system, network connections, account details, accessibility requirements, and language and region settings. On some platforms, the system-provided Settings app can also include settings for specific apps and games, often letting people adjust whether the app or game can access location information, use device features like microphone or camera, and integrate with system features like notifications, Siri, or Search.

When necessary, you can provide a custom settings area within your app or game to offer general settings that affect your overall experience, like interface style or game-saving behavior. If you need to offer settings that affect only a specific task, you can provide these options within the task itself, so people don't have to leave the experience to customize it.

## Topics

### Best Practices

- **Provide optimal default settings** - Aim to provide default settings that give the best experience to the largest number of people. For example, you can automatically maximize performance for the device your game is running on instead of asking players to make this choice after your game launches (for developer guidance, see [Improving your game's graphics performance and settings](https://developer.apple.com/documentation/metal/improving_your_game_s_graphics_performance_and_settings)). When you choose appropriate default settings, people may not have to make any adjustments before they can start enjoying your app or game.

- **Minimize the number of settings** - Although people appreciate having control over an app or game, too many settings can make the experience feel less approachable, while also making it hard to find a particular setting.

- **Make settings accessible in expected ways** - For example, when a physical keyboard is connected, people often use the standard Command-Comma (,) keyboard shortcut to open an app's settings, whereas in a game, players often use the Esc (Escape) key.

- **Avoid asking for information you can detect automatically** - For example, a game can automatically detect a connected controller or accessory instead of asking the player to identify it; an app can detect whether people are currently using Dark Mode.

- **Respect systemwide settings** - People expect to use the system-provided Settings app to manage global options like accessibility accommodations, scrolling behavior, and authentication methods, and they expect all apps and games to adhere to their choices. Including custom versions of global options in your settings area is likely to confuse people because it implies that systemwide settings may not apply to your app or game and that changing your custom version of a global setting may affect other apps and games, too.

### General Settings

- **Include infrequently changed options** - Put general, infrequently changed settings in your custom settings area. People must suspend what they're doing to open an app's or game's settings area, so you want to include options that people don't need to change all the time. For example, an app might list options for adjusting window configuration; a game might let players specify game-saving behavior or keyboard mappings; both apps and games might offer options related to people's accounts.

### Task-Specific Options

- **Make options available in context** - When possible, prefer letting people modify task-specific options without going to your settings area. For example, if people can adjust things like showing or hiding parts of the current view, reordering a collection of items, or filtering a list, make these options available in the screens they affect, where they're discoverable and convenient. Putting this type of option in a separate settings area disconnects it from its context, requiring people to suspend their task to make adjustments, and often hiding the results until people resume the task.

> **Note:** In games, players tend to adjust their approach to a specific task as part of the gameplay, not as a settings option to change.

### System Settings

- **Add only rarely changed options** - Add only the most rarely changed options to the system-provided Settings app. If it makes sense to add your app's or game's settings to the system-provided Settings app, consider providing a button that opens it directly from your interface.

### Platform Considerations

**iOS, iPadOS, tvOS, visionOS**  
No additional considerations for these platforms.

**macOS**  
When people choose the Settings item in your app's or game's App menu, your custom settings window opens. Typically, a custom settings window contains a toolbar that includes buttons for switching between views — called panes — that each contain a group of related settings.

- **Include a settings item in the App menu** - Avoid adding settings buttons to a window's toolbar, because doing so decreases the space available for essential commands that people use frequently. If you provide document-level options, add this item to your app's File menu.

- **Dim minimize and maximize buttons** - It's quick to open a custom settings window using the standard Command–Comma (,) keyboard command, so there's no need to keep the window in the Dock, and because a settings window accommodates the size of the current pane, people don't need to expand the window to see more.

- **Use a stable, noncustomizable toolbar** - In your settings window, use a noncustomizable toolbar that remains visible and always indicates the active toolbar button. A settings window's toolbar identifies the areas people can customize and helps people navigate among those areas. People rely on a stable settings interface to help them find what they need.

- **Update window title based on current pane** - Update the window's title to reflect the currently visible pane. If your settings window doesn't have multiple panes, use the title App Name Settings.

- **Restore the last viewed pane** - People often adjust related settings more than once, so it can be convenient when a settings window opens to the last pane people used.

**watchOS**  
In watchOS, apps and games don't add custom settings to the system-provided Settings app. As an alternative, consider making a small number of essential options available at the bottom of the main view or letting people use a More menu to reconfigure objects.

### Related Components

- [Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding) - Introducing people to your app's features and settings

### Developer Documentation

- [Settings](https://developer.apple.com/documentation/swiftui/settings) - SwiftUI
- [UserDefaults](https://developer.apple.com/documentation/foundation/userdefaults) - Foundation
- [Preference Panes](https://developer.apple.com/documentation/preferencepanes) - macOS

## Changelog

### June 10, 2024
- Reorganized some guidance into new topics and added game-specific examples

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/settings)*