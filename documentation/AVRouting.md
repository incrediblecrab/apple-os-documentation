# AVRouting

Display custom destinations to stream media in the system route picker.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 16.0+ | macOS 13.0+ | tvOS 26.0+ (Beta)

## Overview

Use the AVRouting framework to add third-party devices and protocols to AVRoutePickerView. This enables a user to stream AV content through a third-party protocol using the same system menu as AirPlay.

When the user taps the view, the system presents a popover that lists the available media receivers. If your app's bundle includes an extension with the Media Device Discovery Extension entitlement, the system runs the extension and adds its associated third-party protocol to the picker, if the device resides nearby.

### Add a custom route to the system device-picker view

To indicate your app's intent to search for a nearby third-party media receiver, set a custom routing controller (AVCustomRoutingController) on the view.

```swift
struct DevicePickerView: UIViewRepresentable {
    func makeUIView(context: Context) -> UIView {
        let routePickerView = AVRoutePickerView()
        routePickerView.delegate = context.coordinator
        routePickerView.customRoutingController = RouteManager.shared.customRoutingController
```

Next, let the view know which particular device your app intends to add. Each device requires a unique device discovery extension, which distinguishes itself through a uniform type identifier in its Info.plist file. Add a custom routing action (AVCustomRoutingActionItem) with type set to the identifier and pass the item to the controller's customActionItems.

```swift
func routePickerViewWillBeginPresentingRoutes(_ routePickerView: AVRoutePickerView) {
    if let type = UTType("com.example.apple-DataAccessDemo.menu") {
        let customRow1 = AVCustomRoutingActionItem()
        customRow1.type = type
        RouteManager.shared.customRoutingController?.customActionItems = [customRow1]
    }
}
```

If the extension finds the device at runtime, it passes the device to the system for display in the picker. See [Discovering a third-party media-streaming device](https://developer.apple.com/documentation/avrouting/discovering_a_third-party_media-streaming_device) for a complete sample code project that routes media through a custom protocol.

## Topics

### Media Routing
- **AVCustomRoutingController** - An object that manages the connection from a device to a destination.
- **AVCustomRoutingControllerDelegate** - A protocol for delegates of a custom routing controller.
- **AVCustomRoutingEvent** - An object that represents an event that occurs on a route.
- **AVCustomRoutingActionItem** - An object that represents a custom action item to display in a device route picker.

### Playback Arbitration
- **AVRoutingPlaybackArbiter** - An object that manages playback routing preferences. (Beta)
- **AVRoutingPlaybackParticipant** - A protocol for objects that participate in playback routing arbitration. (Beta)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AVRouting)*