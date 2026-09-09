# AVRouting

Display custom destinations to stream media in the system route picker.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 16.0+ | macOS 13.0+ | tvOS 26.0+

## Overview

Use the AVRouting framework to add third-party devices and protocols to AVRoutePickerView. This enables a user to stream AV content through a third-party protocol using the same system menu as AirPlay.

When the user taps the view, the system presents a popover that lists the available media receivers. If your app's bundle includes an extension with the Media Device Discovery Extension entitlement, the system runs the extension and adds its associated third-party protocol to the picker, if the device resides nearby.

### Add a custom route to the system device-picker view

To indicate your app's intent to search for a nearby third-party media receiver, set a custom routing controller (AVCustomRoutingController) on the view.

The following UIKit configuration is an excerpt, not a complete `UIViewRepresentable`. Its `context.coordinator` and app-defined `RouteManager` come from the [complete discovery sample](https://developer.apple.com/documentation/devicediscoveryextension/discovering-a-third-party-media-streaming-device).

```swift
let routePickerView = AVRoutePickerView()
routePickerView.delegate = context.coordinator
routePickerView.customRoutingController = RouteManager.shared.customRoutingController
```

Next, identify the discovery extension through its uniform type identifier in `Info.plist`. Add a custom routing action (`AVCustomRoutingActionItem`) with `type` set to that identifier and pass the item to the controller's `customActionItems`. This delegate-method excerpt uses the same sample's routing manager; the example identifier must match the extension's actual configuration.

```swift
func routePickerViewWillBeginPresentingRoutes(_ routePickerView: AVRoutePickerView) {
    if let type = UTType("com.example.apple-DataAccessDemo.menu") {
        let customRow1 = AVCustomRoutingActionItem()
        customRow1.type = type
        RouteManager.shared.customRoutingController?.customActionItems = [customRow1]
    }
}
```

If the extension finds the device at runtime, it passes the device to the system for display in the picker. See [Discovering a third-party media-streaming device](https://developer.apple.com/documentation/devicediscoveryextension/discovering-a-third-party-media-streaming-device) for a complete sample code project that routes media through a custom protocol.

### Relationship to OS 27 system routing

The custom-route APIs above retain their earlier deployment requirements. For the OS 27 provider-extension architecture, use [AVSystemRouting](AVSystemRouting.md) in the media app and [Media Device](MediaDevice.md) in the protocol provider. Do not interchange the older discovery-extension setup with the new media-device-extension entitlement.

The new workflow targets iOS and iPadOS 27. Its framework references annotate Mac Catalyst 27, but Apple's routing guide explicitly excludes Catalyst; see the discrepancy documented on the new reference pages before relying on that annotation. A remote speaker or TV is a receiver, not evidence of another SDK platform. Handle selection, activation, playback startup, and disconnection separately.

## Topics

### Media Routing

- **AVCustomRoutingController** - An object that manages the connection from a device to a destination.
- **AVCustomRoutingControllerDelegate** - A protocol for delegates of a custom routing controller.
- **AVCustomRoutingEvent** - An object that represents an event that occurs on a route.
- **AVCustomRoutingActionItem** - An object that represents a custom action item to display in a device route picker.

### Playback Arbitration

- **AVRoutingPlaybackArbiter** - An object that manages playback routing preferences.
- **AVRoutingPlaybackParticipant** - A protocol for objects that participate in playback routing arbitration.
---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AVRouting)*
