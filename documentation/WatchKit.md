# WatchKit

Build watchOS apps that use features the app delegate monitors or controls, such as background tasks and extended runtime sessions.

**Platforms:** watchOS 2.0+

## Overview

WatchKit supplies watch-specific application callbacks, background-task handling, extended-runtime sessions, and device information. New single-target apps use `WKApplication` and `WKApplicationDelegate`; older app-plus-extension projects use the legacy extension objects.

You can also use WatchKit to design your app's user interface in a storyboard, connecting UI elements to an interface controller.

Prefer SwiftUI for new interfaces. Storyboard-based WatchKit interfaces remain a distinct legacy workflow, not a requirement for using the framework's lifecycle or device APIs.

For platform guidance, see [watchOS apps](https://developer.apple.com/documentation/watchos-apps).

## Framework boundaries

Use [SwiftUI](SwiftUI.md) for new watch interfaces, [WidgetKit](WidgetKit.md) for complications and Smart Stack widgets, and [RelevanceKit](RelevanceKit.md) for relevance clues. WatchKit still manages watch-specific application callbacks and runtime sessions; changes to the system's app grid are not new WatchKit APIs. Consult [`WKExtendedRuntimeSession`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession) for supported extended-runtime use cases rather than assuming a widget grants unrestricted background execution.

### Lifecycle and runtime availability

`WKApplication`, its delegate, and `WKApplicationMain` begin at watchOS 7. Xcode 14 introduced the single-target project structure, which can deploy to watchOS 7; its introduction isn't an OS 27 requirement. `WKExtension` and `WKExtensionDelegate` begin at watchOS 2 and are deprecated from 9.2, not described as removed.

Extended-runtime sessions require watchOS 6. An app selects one supported session type — self care, mindfulness, physical therapy, or smart alarm — through Background Modes. Some sessions remain frontmost rather than running in the background. Start or schedule a session while the app is active, respect its time limit, and handle invalidation; excessive CPU use can cause cancellation.

## Topics

### App structure
- [Setting up a watchOS project](https://developer.apple.com/documentation/watchos-apps/setting-up-a-watchos-project) - Create a watch app or add a watch target to an iOS project.
- [`WKApplication`](https://developer.apple.com/documentation/watchkit/wkapplication) - Coordinates a single-target watchOS app.
- [`WKApplicationDelegate`](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate) - Handles its application-level events; SwiftUI apps can connect it through `WKApplicationDelegateAdaptor`.
- [`WKExtension`](https://developer.apple.com/documentation/watchkit/wkextension) - The legacy extension-based application object.
- [`WKExtensionDelegate`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate) - Handles legacy extension-level events.
- [`WKApplicationMain(_:_:_:)`](https://developer.apple.com/documentation/watchkit/wkapplicationmain(_:_:_:)) - Creates the application/delegate and enters the event loop.
- [`WKInterfaceDevice`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice) - Provides device information and haptics; obtain the shared instance with `current()` rather than constructing or subclassing it.
- [`WKPrefersNetworkUponForeground`](https://developer.apple.com/documentation/bundleresources/information-property-list/wkprefersnetworkuponforeground) - A watchOS 9+ property-list preference for enabling cellular networking promptly on launch in Low Power Mode. It defaults to `NO`, and doesn't guarantee connectivity.

### Runtime management
- [Background execution](https://developer.apple.com/documentation/watchkit/background-execution) - Manage background sessions and tasks.
- [Life cycles](https://developer.apple.com/documentation/watchkit/life-cycles) - Receive and respond to life-cycle notifications.
- [Using extended runtime sessions](https://developer.apple.com/documentation/watchkit/using-extended-runtime-sessions) - Create an extended runtime session that continues running your app after the user stops interacting with it.
- [`WKExtendedRuntimeSession`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession) - Provides bounded runtime for a supported use case after interaction stops.
- [Interacting with Bluetooth peripherals during background app refresh](https://developer.apple.com/documentation/watchkit/interacting-with-bluetooth-peripherals-during-background-app-refresh) - Keep your complications up-to-date by reading values from a Bluetooth peripheral while your app is running in the background.

### User interface
- [Storyboard support](https://developer.apple.com/documentation/watchkit/storyboard-support) - Connect your code to storyboard elements using interface controllers, interface objects, and event handlers.
- [`NowPlayingView`](https://developer.apple.com/documentation/watchkit/nowplayingview) - A watchOS 7+ SwiftUI audio-control view. The system chooses the current or most recently used source; present it full-screen in a nonscrolling container without additional elements.

### Errors
- [`WatchKitError`](https://developer.apple.com/documentation/watchkit/watchkiterror) - A structure representing a WatchKit error; its current reference doesn't specify an introduction version.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/WatchKit)*
