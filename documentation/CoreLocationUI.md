# CoreLocationUI

Streamline access to users' location data through a standard, secure UI.

**Platforms:** iOS 15.0+ | iPadOS 15.0+ | Mac Catalyst 15.0+ | watchOS 10.0+

## Overview

The CoreLocationUI framework contains a standardized UI that interacts securely with Core Location to request authorization to access location data.

CoreLocationUI provides LocationButton for SwiftUI apps and CLLocationButton for UIKit apps. Add these buttons to your UI when you want someone to grant one-time authorization for your app to fetch their location. The button's style is consistent with the standard Core Location design language, giving users a sense of familiarity and trust when they interact with it.

**Note**  
The location button ignores user input on Mac apps built with Mac Catalyst, and on compatible iPad and iPhone apps running in visionOS.

## Topics

### Location authorization
- [Sharing Your Location to Find a Park](https://developer.apple.com/documentation/corelocationui/sharing_your_location_to_find_a_park) - Ask for location access using a customizable location button.
- **LocationButton** - A SwiftUI button that grants one-time location authorization.
- **CLLocationButton** - A button that grants one-time location authorization.

### Button customization
- **CLLocationButtonIcon** - Constants that specify styles for the location arrow icon on the button.
- **CLLocationButtonLabel** - Constants that specify the text of the button label.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreLocationUI)*