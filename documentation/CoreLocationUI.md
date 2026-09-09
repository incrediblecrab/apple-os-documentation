# CoreLocationUI

Streamline access to users' location data through a standard, secure UI.

**Platforms:** iOS 15.0+ | iPadOS 15.0+ | Mac Catalyst 15.0+ | watchOS 10.0+

## Overview

CoreLocationUI supplies system location buttons for requesting temporary authorization. It doesn't replace [CoreLocation](CoreLocation.md), which your app uses to obtain the location after authorization.

Use `LocationButton` in SwiftUI or `CLLocationButton` in UIKit. The first interaction asks the person to approve this authorization mechanism. If approved, it grants temporary `authorizedWhenInUse` access, like Allow Once, which expires when the app is no longer in use. Subsequent taps can obtain another temporary grant without repeating that confirmation.

The button doesn't return coordinates. Its action runs on every tap, including when authorization already exists; handle location requests and their results separately.

The framework catalog lists watchOS 10, while the SwiftUI `LocationButton` declaration lists watchOS 8. The UIKit button has no watchOS declaration. Preserve that per-symbol distinction rather than treating the framework header as a uniform button minimum.

**Note**  
The location button ignores user input on Mac apps built with Mac Catalyst, and on compatible iPad and iPhone apps running in visionOS.

## Topics

### Location authorization
- [Sharing Your Location to Find a Park](https://developer.apple.com/documentation/corelocationui/sharing-your-location-to-find-a-park) - Ask for location access using a customizable location button.
- [`LocationButton`](https://developer.apple.com/documentation/corelocationui/locationbutton) - The SwiftUI temporary-authorization button.
- [`CLLocationButton`](https://developer.apple.com/documentation/corelocationui/cllocationbutton) - The UIKit temporary-authorization button.

### Button customization
- [`CLLocationButtonIcon`](https://developer.apple.com/documentation/corelocationui/cllocationbuttonicon) - UIKit location-arrow icon styles.
- [`CLLocationButtonLabel`](https://developer.apple.com/documentation/corelocationui/cllocationbuttonlabel) - UIKit button label choices.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreLocationUI)*
