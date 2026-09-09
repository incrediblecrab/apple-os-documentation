# TVUIKit

Show common user interface elements from Apple TV in your native app.

**Platforms:** tvOS 12.0+

## Overview

When you build an app for tvOS with **UIKit**, you can use **TVUIKit** to refine the display of your content for a TV environment. Use the **TV Services** framework to provide deeper integration between your app and Apple TV.

For platform planning, see [Planning your tvOS app](https://developer.apple.com/tvos/planning/).

When rebuilding a UIKit-based TV app with the 27 SDK, apply the [UIKit scene-lifecycle requirement](UIKit.md#required-scene-life-cycle-and-launch-screen) on tvOS as well. TVUIKit controls do not replace the app life cycle. This framework is separate from the deprecated [TVMLKit](TVMLKit.md) client-server UI model.

## Topics

### Collections of Content
These full-screen collection types require tvOS 13+, later than the framework's tvOS 12 baseline.

- [Creating immersive experiences using a full-screen layout](https://developer.apple.com/documentation/tvuikit/creating-immersive-experiences-using-a-full-screen-layout) - Build a browsable full-screen collection layout.
- **TVCollectionViewFullScreenLayout** - A collection view layout that organizes items into a browsable, full-screen display format.
- **TVCollectionViewDelegateFullScreenLayout** - Methods that send notifications of events during cell transitions.
- **TVCollectionViewFullScreenCell** - A full-screen cell to use in full-screen display format.
- **TVCollectionViewFullScreenLayoutAttributes** - Attributes to manage the appearance of the collection view's layout.

### Content Views
- [`TVMediaItemContentView`](https://developer.apple.com/documentation/tvuikit/tvmediaitemcontentview) - A media-content view, tvOS 15+.
- [`TVMonogramContentView`](https://developer.apple.com/documentation/tvuikit/tvmonogramcontentview) - A circular image or localized initials view, tvOS 15+.

### Numeric Input
- **TVDigitEntryViewController** - A view controller that enables the user to enter digits, like a passcode, in your app.

### Lockup Views
- **TVLockupView** - A focusable view that presents main content, like a movie poster, and an optional header and footer.
- **TVLockupViewComponent** - The protocol for responding to lockup view state changes.
- **TVLockupHeaderFooterView** - A view that contains header and footer information.
- **TVCardView** - A view that responds to focus interaction with a motion effect it applies to all of its subviews.
- **TVPosterView** - An optimized view for displaying an image, a header, and a footer.
- **TVCaptionButtonView** - A button-like view that responds to user interactions.
- [`TVMonogramView`](https://developer.apple.com/documentation/tvuikit/tvmonogramview) - The older monogram lockup view, introduced in tvOS 12 and deprecated in tvOS 27.

### Deprecated
For `TVMonogramView`, move to [`TVMonogramContentConfiguration`](https://developer.apple.com/documentation/tvuikit/tvmonogramcontentconfiguration-swift.struct) and `TVMonogramContentView`. Deprecation of that view doesn't deprecate the entire TVUIKit framework.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/TVUIKit)*
