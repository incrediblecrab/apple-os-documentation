# TipKit

Display tips that help people discover features in your app.

**Platforms:** iOS 17.0+ | iPadOS 17.0+ | Mac Catalyst 17.0+ | macOS 14.0+ | tvOS 16.0+ | visionOS 1.0+ | watchOS 10.0+

## Overview

Use **TipKit** to show contextual tips that highlight new, interesting, or unused features people haven't discovered on their own yet.

Define your tip content, and the conditions under which they appear, with the **Tip** protocol. Then draw attention to new features using the **TipView**.

As you design tips for your app, ensure you don't overwhelm your users. Use tips sparingly to highlight nonobvious features people haven't discovered on their own. Similarly, avoid displaying tips each time someone uses your app. Tips can become distracting when they appear unnecessarily. Don't use tips to guide people through your app, or for advertising and promotion purposes.

For design guidance on tips, see Human Interface Guidelines > Offering help.

### Related Sessions

- **WWDC24 Session 10070:** Customize feature discovery with TipKit
- **WWDC23 Session 10229:** Make features discoverable with TipKit

### Example Usage

```swift
import SwiftUI
import TipKit

// Define your tip's content.
struct FavoriteLandmarkTip: Tip {
    var title: Text {
        Text("Save as a Favorite")
    }

    var message: Text? {
        Text("Your favorite landmarks always appear at the top of the list.")
    }

    var image: Image? {
        Image(systemName: "star")
    }
}

@main
struct LandmarkTips: App {
    // Create an instance of your tip.
    var favoriteLandmarkTip = FavoriteLandmarkTip()

    var body: some Scene {
        WindowGroup {
            VStack {
                // Place the tip view near the feature you want to highlight.
                TipView(favoriteLandmarkTip, arrowEdge: .bottom)

                Image(systemName: "star")
                    .imageScale(.large)
                Spacer()
            }
            .task {
                // Configure and load your tips at app launch.
                do {
                    try Tips.configure()
                } 
                catch {
                    // Handle TipKit errors
                    print("Error initializing TipKit \(error.localizedDescription)")
                }
            }
        }
    }
}
```

## Topics

### Essentials
- [Highlighting app features with TipKit](https://developer.apple.com/documentation/tipkit/highlighting_app_features_with_tipkit) - Bring attention to new features in your app by using tips.

### Content
- **Tip** - A type that sets a tip's content, as well as the conditions for when it displays.
- **TipGroup** - A collection of tips that can be presented one at a time using a specific order or based on the first tip eligible for display.

### Configuration
- **Tips.configure([Tips.ConfigurationOption])** - Loads and configures the persistent state of all tips in your app.
- **Tips.cloudKitContainer(Tips.ConfigurationOption.CloudKitContainer?)** - Sets the CloudKit container used for syncing tips.
- **Tips.datastoreLocation(Tips.ConfigurationOption.DatastoreLocation)** - Specify a custom location for your tips datastore.
- **Tips.displayFrequency(Tips.ConfigurationOption.DisplayFrequency)** - Customizes how often new tips are presented in your app after another tip has been displayed.

### Views
- **TipView** - A user interface element that represents an inline tip.
- **popoverTip(_:arrowEdge:action:)** - Presents a popover tip on the modified view.

### UIKit Views
- **TipUIView** - A user interface element that represents a tip in UIKit applications.
- **TipUIPopoverViewController** - A view controller that displays a popover tip in UIKit applications.
- **TipUICollectionViewCell** - A collection view cell that embeds a tip.
- **TipUICollectionReusableView** - A UICollectionReusableView subclass that represents a tip.

### AppKit Views
- **TipNSView** - A user interface element that represents a tip in AppKit applications.
- **TipNSPopover** - A subclass of NSPopover that displays a popover tip in AppKit applications.

### Display Rules
- **Rule** - A condition to meet before displaying a tip.
- **Parameter** - A type that monitors the state of its wrapped value to reevaluate any dependent tip rules when the value changes.
- **Event** - A repeatable user-defined action.

### View Style
- **tipViewStyle(_:)** - Sets the given style for TipView within the view hierarchy.
- **TipViewStyle** - A type that applies custom appearance to all tips within a view hierarchy.
- **TipViewStyleConfiguration** - The container type that holds a tip's configuration.
- **MiniTipViewStyle** - The default style for a TipView.

### Testing
- **Tips.showAllTipsForTesting()** - Show all tips regardless of their display rule eligibility or display frequency status for UI testing of tips.
- **Tips.showTipsForTesting([any Tip.Type])** - Show specified tips regardless of their display rule eligibility or display frequency status for UI testing of certain tips.
- **Tips.hideAllTipsForTesting()** - Hide all tips regardless of their display rule eligibility for UI testing without tips.
- **Tips.hideTipsForTesting([any Tip.Type])** - Hide specified tips regardless of their display rule eligibility for UI testing without certain tips.
- **Tips.resetDatastore()** - Resets the tips' datastore to the initial state for re-testing tip display rules and eligibility.

### Common Types
- **AnyTip** - A type-erased tip value.
- **TipKitError** - A localized tip kit error.
- **TipOption** - A type that represents the various customizations that you can make to a tip's behavior.

### Enumerations
- **Tips** - TipKit namespace.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/TipKit)*