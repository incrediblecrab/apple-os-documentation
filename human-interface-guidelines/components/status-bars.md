# Status Bars

A status bar appears along the upper edge of the screen and displays information about the device's current state, like the time, cellular carrier, and battery level.

**Platforms:** iOS | iPadOS

## Overview

A status bar appears along the upper edge of the screen and displays information about the device's current state, like the time, cellular carrier, and battery level.

## Topics

### Best Practices

- **Obscure content under the status bar** - By default, the background of the status bar is transparent, allowing content beneath to show through. This can make it difficult to see the information presented in the status bar. If controls are visible behind the status bar, people may attempt to interact with them and be unable to do so. Be sure to keep the status bar readable and don't imply that content behind it is interactive. There are several common techniques for doing this:
  - Use a top toolbar that automatically displays a status bar background.
  - Display a custom image, like a gradient or solid color, behind the status bar.
  - Place a blurred view behind the status bar. For developer guidance, see [UIBlurEffect](https://developer.apple.com/documentation/uikit/uiblureffect).

- **Consider temporarily hiding the status bar when displaying full-screen media** - A status bar can be distracting when people are paying attention to media. Temporarily hide these elements to provide a more immersive experience. The Photos app, for example, hides the status bar and other interface elements when people browse full-screen photos.

- **Avoid permanently hiding the status bar** - Without a status bar, people have to leave your app to check the time or see if they have a Wi-Fi connection. Let people redisplay a hidden status bar with a simple, discoverable gesture. For example, when browsing full-screen photos in the Photos app, a single tap shows the status bar again.

### Platform Considerations

No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.

### Developer Documentation

- [UIStatusBarStyle](https://developer.apple.com/documentation/uikit/uistatusbarstyle) - UIKit
- [preferredStatusBarStyle](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621416-preferredstatusbarstyle) - UIKit

## Changelog

### Version 1.0
- Initial documentation of status bar guidelines
- Best practices for content obscuring
- Guidelines for full-screen media handling

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/status-bars)*