# WatchKit

Build watchOS apps that use features the app delegate monitors or controls, such as background tasks and extended runtime sessions.

**Platforms:** watchOS 2.0+

## Overview

The WatchKit framework provides infrastructure for creating watchOS apps, including an extension delegate that manages background tasks, extended runtime sessions, and Siri intents. The framework also performs other support tasks, such as accessing information about the user's Apple Watch.

You can also use WatchKit to design your app's user interface in a storyboard, connecting UI elements to an interface controller.

**Note:** Building your app with SwiftUI gives you more control over the user interface than designing it in a storyboard. When creating a new watchOS app, strongly consider using SwiftUI. For more information, see Building a watchOS app.

For more information on building watchOS apps, see watchOS apps.

## Topics

### App structure
- [Setting up a watchOS project](https://developer.apple.com/documentation/watchkit/setting-up-a-watchos-project) - Create a new watchOS project or add a watch target to an existing iOS project.
- **WKApplication** - The centralized point of control and coordination for apps with a single watchOS app target.
- **WKApplicationDelegate** - A collection of methods that manages the app-level behavior for a single-target watchOS app.
- **WKExtension** - The centralized point of control and coordination for extension-based apps running in watchOS.
- **WKExtensionDelegate** - A collection of methods that manages the app-level behavior of a WatchKit extension.
- **WKApplicationMain** - Creates the application object and the application delegate, and sets up the app's event cycle.
- **WKInterfaceDevice** - An object that provides information about the user's Apple Watch.
- **WKPrefersNetworkUponForeground** - A Boolean value that indicates whether an app requires network access on launch.

### Runtime management
- [Background execution](https://developer.apple.com/documentation/watchkit/background-execution) - Manage background sessions and tasks.
- [Life cycles](https://developer.apple.com/documentation/watchkit/life-cycles) - Receive and respond to life-cycle notifications.
- [Using extended runtime sessions](https://developer.apple.com/documentation/watchkit/using-extended-runtime-sessions) - Create an extended runtime session that continues running your app after the user stops interacting with it.
- **WKExtendedRuntimeSession** - A session that continues to run your app after the user has stopped interacting.
- [Interacting with Bluetooth peripherals during background app refresh](https://developer.apple.com/documentation/watchkit/interacting-with-bluetooth-peripherals-during-background-app-refresh) - Keep your complications up-to-date by reading values from a Bluetooth peripheral while your app is running in the background.

### User interface
- [Storyboard support](https://developer.apple.com/documentation/watchkit/storyboard-support) - Connect your code to storyboard elements using interface controllers, interface objects, and event handlers.
- **NowPlayingView** - A view that displays the system's Now Playing interface so that the user can control audio.

### Errors
- **WatchKitError** - An error reported by WatchKit.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/WatchKit)*