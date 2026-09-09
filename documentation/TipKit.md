# TipKit

Display tips that help people discover features in your app.

**Platforms:** iOS 17.0+ | iPadOS 17.0+ | Mac Catalyst 17.0+ | macOS 14.0+ | tvOS 17.0+ | visionOS 1.0+ | watchOS 10.0+

## Overview

Use **TipKit** to show contextual tips that highlight new, interesting, or unused features people haven't discovered on their own yet.

Define your tip content, and the conditions under which they appear, with the **Tip** protocol. Then draw attention to new features using the **TipView**.

As you design tips for your app, ensure you don't overwhelm your users. Use tips sparingly to highlight nonobvious features people haven't discovered on their own. Similarly, avoid displaying tips each time someone uses your app. Tips can become distracting when they appear unnecessarily. Don't use tips to guide people through your app, or for advertising and promotion purposes.

For design guidance, see [Offering help](https://developer.apple.com/design/human-interface-guidelines/offering-help). Tips are contextual feature discovery, not a substitute for a multistep tutorial.

Call `Tips.configure(_:)` during app initialization, before tips display or parameter values update. Display frequency governs **new** tips; an already displayed tip can appear again while eligible. Use rules and invalidation to manage relevance rather than treating a frequency setting as a universal suppression interval.

### API availability

The framework catalog lists tvOS 16, but `Tip`, `TipView`, `Tips.configure`, and the reviewed rule/configuration APIs require tvOS 17. `TipGroup` and CloudKit synchronization require iOS/iPadOS/Mac Catalyst/tvOS 18, macOS 15, visionOS 2, or watchOS 11.

The UIKit view types below declare iOS/iPadOS/Mac Catalyst 17 and visionOS 1; the AppKit view types declare macOS 14. The shared `popoverTip` reference has conflicting iPadOS/watchOS availability metadata, so don't infer an older-platform popover minimum from that aggregate reference. An optional, type-erased tip can also select the newer 26-generation overload. Check the exact overload rather than treating every `popoverTip` call as interchangeable. The example uses `TipView`, whose minimum is unambiguous.

### Related Sessions

- [WWDC24 Session 10070: Customize feature discovery with TipKit](https://developer.apple.com/videos/play/wwdc2024/10070/)
- [WWDC23 Session 10229: Make features discoverable with TipKit](https://developer.apple.com/videos/play/wwdc2023/10229/)

### Example Usage

This display-only example shows a tip beside an illustrative feature icon; it doesn't implement a favorites list.

```swift
import SwiftUI
import TipKit

struct FavoriteLandmarkTip: Tip {
    var title: Text {
        Text("Save as a Favorite")
    }

    var message: Text? {
        Text("Keep favorite landmarks easy to revisit.")
    }

    var image: Image? {
        Image(systemName: "star")
    }
}

@main
struct LandmarkTips: App {
    private let favoriteLandmarkTip = FavoriteLandmarkTip()

    init() {
        do {
            try Tips.configure()
        } catch {
            print("Error initializing TipKit \(error.localizedDescription)")
        }
    }

    var body: some Scene {
        WindowGroup {
            VStack {
                TipView(favoriteLandmarkTip, arrowEdge: .bottom)

                Image(systemName: "star")
                    .imageScale(.large)
                Spacer()
            }
        }
    }
}
```

## Topics

### Essentials
- [Highlighting app features with TipKit](https://developer.apple.com/documentation/tipkit/highlightingappfeatureswithtipkit) - Apple's iOS 18+/Xcode 16+ sample; its requirements don't raise the framework's older baseline.

### Content
- [`Tip`](https://developer.apple.com/documentation/tipkit/tip) - Defines content and eligibility; a title is required.
- [`TipGroup`](https://developer.apple.com/documentation/tipkit/tipgroup) - Presents one eligible tip at a time using ordered or first-available priority; first-available is the default.

### Configuration
The option factories belong to `Tips.ConfigurationOption`, not directly to `Tips`; pass their results to `Tips.configure(_:)`.

- [`Tips.configure(_:)`](https://developer.apple.com/documentation/tipkit/tips/configure(_:)) - A throwing setup method taking an options array, which defaults to empty.
- [`Tips.ConfigurationOption.cloudKitContainer(_:)`](https://developer.apple.com/documentation/tipkit/tips/configurationoption/cloudkitcontainer(_:)) - Selects tip-state synchronization; syncing is off by default and `nil` disables it. Configure iCloud/CloudKit and remote-notification Background Modes capabilities. A separate tips container helps avoid record collisions.
- [`Tips.ConfigurationOption.datastoreLocation(_:)`](https://developer.apple.com/documentation/tipkit/tips/configurationoption/datastorelocation(_:)) - Chooses the persistent store's location; tvOS has a caches/UserDefaults-based default, unlike the usual Application Support location.
- [`Tips.ConfigurationOption.displayFrequency(_:)`](https://developer.apple.com/documentation/tipkit/tips/configurationoption/displayfrequency(_:)) - Controls the interval before new tips can appear; individual tips can opt out.

### Views
- [`TipView`](https://developer.apple.com/documentation/tipkit/tipview) - Displays an inline tip near its related feature.
- [`popoverTip(_:arrowEdge:action:)`](https://developer.apple.com/documentation/swiftui/view/popovertip(_:arrowedge:action:)) - Presents an eligible tip from an existing SwiftUI view; check the specific overload's SDK availability.
- [`popoverTip(_:isPresented:attachmentAnchor:arrowEdge:action:)`](https://developer.apple.com/documentation/swiftui/view/popovertip(_:ispresented:attachmentanchor:arrowedge:action:)) - The 26-generation presentation-control overload. Its binding can temporarily hide or show a currently eligible tip; it doesn't bypass eligibility rules.

### UIKit Views
- [`TipUIView`](https://developer.apple.com/documentation/tipkit/tipuiview) - Embeds a tip in a UIKit hierarchy.
- [`TipUIPopoverViewController`](https://developer.apple.com/documentation/tipkit/tipuipopoverviewcontroller) - Presents a UIKit popover tip.
- [`TipUICollectionViewCell`](https://developer.apple.com/documentation/tipkit/tipuicollectionviewcell) - Embeds a tip in a collection-view cell.
- [`TipUICollectionReusableView`](https://developer.apple.com/documentation/tipkit/tipuicollectionreusableview) - Supplies a reusable tip view for a collection view.

### AppKit Views
- [`TipNSView`](https://developer.apple.com/documentation/tipkit/tipnsview) - Displays a tip in an AppKit hierarchy.
- [`TipNSPopover`](https://developer.apple.com/documentation/tipkit/tipnspopover) - Presents a native AppKit tip popover.

Observe the tip's `shouldDisplayUpdates` or `statusUpdates` to add and remove native AppKit presentations; creating the object isn't the complete eligibility lifecycle.

### Display Rules
- [`Rule`](https://developer.apple.com/documentation/tipkit/tips/rule) - An eligibility condition, commonly constructed with `#Rule`.
- [`Parameter`](https://developer.apple.com/documentation/tipkit/tips/parameter) - State tracked through the `@Parameter` macro, persistent by default.
- [`Event`](https://developer.apple.com/documentation/tipkit/tips/event) - A user-defined action whose donations inform event-based rules.

### View Style
- [`tipViewStyle(_:)`](https://developer.apple.com/documentation/swiftui/view/tipviewstyle(_:)) - Sets the style for descendant tip views.
- [`TipViewStyle`](https://developer.apple.com/documentation/tipkit/tipviewstyle) - Defines a custom tip-view appearance.
- [`TipViewStyleConfiguration`](https://developer.apple.com/documentation/tipkit/tipviewstyleconfiguration) - Supplies the content for a tip style.
- [`MiniTipViewStyle`](https://developer.apple.com/documentation/tipkit/minitipviewstyle) - The default `TipView` style.

### Testing
- [`Tips.showAllTipsForTesting()`](https://developer.apple.com/documentation/tipkit/tips/showalltipsfortesting()) - Overrides eligibility and frequency for display testing.
- [`Tips.showTipsForTesting(_:)`](https://developer.apple.com/documentation/tipkit/tips/showtipsfortesting(_:)) - Applies that override to selected tip types.
- [`Tips.hideAllTipsForTesting()`](https://developer.apple.com/documentation/tipkit/tips/hidealltipsfortesting()) - Suppresses tips for tests.
- [`Tips.hideTipsForTesting(_:)`](https://developer.apple.com/documentation/tipkit/tips/hidetipsfortesting(_:)) - Suppresses selected tip types.
- [`Tips.resetDatastore()`](https://developer.apple.com/documentation/tipkit/tips/resetdatastore()) - A throwing reset that removes tip, event, and parameter records. Call it **before** `Tips.configure`; dismissed tips become eligible again.

Keep these overrides out of production behavior. Their precedence is: show selected, hide selected, show all, then hide all. The show overrides restore invalidated tips to an available state for repeat testing.

### Common Types
- [`AnyTip`](https://developer.apple.com/documentation/tipkit/anytip) - A type-erased tip value.
- [`TipKitError`](https://developer.apple.com/documentation/tipkit/tipkiterror) - A localized TipKit error.
- [`TipOption`](https://developer.apple.com/documentation/tipkit/tipoption) - The protocol for tip-specific behavior options, also exposed as `Tip.Option`.

### Enumerations
- [`Tips`](https://developer.apple.com/documentation/tipkit/tips) - The namespace for setup, rules, events, and testing helpers.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/TipKit)*
