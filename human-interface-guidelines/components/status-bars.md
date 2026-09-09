# Status Bars

A status bar appears along the upper edge of the screen and displays information about the device's current state, like the time, cellular carrier, and battery level.

**Platforms:** iOS | iPadOS

## Overview

A status bar appears along the upper edge of the screen and displays information about the device's current state, like the time, cellular carrier, and battery level.

## Topics

### Best Practices

- **Keep the status bar readable over underlying content** - Its transparent background can let content compete with status information or make obscured controls look interactive. Prefer the system's scroll edge treatment to provide separation rather than assuming a top toolbar supplies an opaque background. See [ScrollEdgeEffectStyle](https://developer.apple.com/documentation/swiftui/scrolledgeeffectstyle) and [UIScrollEdgeEffect](https://developer.apple.com/documentation/uikit/uiscrolledgeeffect).

- **Consider temporarily hiding the status bar when displaying full-screen media** - A status bar can be distracting when people are paying attention to media. Temporarily hide these elements to provide a more immersive experience. The Photos app, for example, hides the status bar and other interface elements when people browse full-screen photos.

- **Avoid permanently hiding the status bar** - Without a status bar, people have to leave your app to check the time or see if they have a Wi-Fi connection. Let people redisplay a hidden status bar with a simple, discoverable gesture. For example, when browsing full-screen photos in the Photos app, a single tap shows the status bar again.

### Platform Considerations

No additional considerations for iOS or iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.

### Developer Documentation

- [UIStatusBarStyle](https://developer.apple.com/documentation/uikit/uistatusbarstyle) - UIKit
- [preferredStatusBarStyle](https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredstatusbarstyle) - UIKit

## Documentation Coverage

This repository page covers status-bar readability and full-screen media behavior. Apple does not publish an article change log on the linked HIG page.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/status-bars)*
