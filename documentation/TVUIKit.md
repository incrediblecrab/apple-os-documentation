# TVUIKit

Show common user interface elements from Apple TV in your native app.

**Platforms:** tvOS 12.0+

## Overview

When you build an app for tvOS with **UIKit**, you can use **TVUIKit** to refine the display of your content for a TV environment. Use the **TV Services** framework to provide deeper integration between your app and Apple TV.

For platform planning, see [Get started with tvOS](https://developer.apple.com/tvos/get-started/).

For UIKit-based TV apps, review the [UIKit scene-lifecycle requirement](UIKit.md#required-scene-life-cycle-and-launch-screen). The [tvOS 27 release notes](https://developer.apple.com/documentation/tvos-release-notes/tvos-27-release-notes) and the [iOS & iPadOS 27 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes) carry the same UIKit deprecation: apps built with the latest SDK must adopt the scene-based life cycle or they fail to launch. Apple's [scene-transition guide](https://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle) names tvOS 27 in that requirement. TVUIKit controls do not replace the app life cycle. This framework is separate from the deprecated [TVMLKit](TVMLKit.md) client-server UI model.

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
- [`TVMonogramView`](https://developer.apple.com/documentation/tvuikit/tvmonogramview) - The older monogram lockup view, introduced in tvOS 12 and deprecated in tvOS 27.2.

### Deprecated
For `TVMonogramView`, Apple's deprecation guidance points to [`TVMonogramContentView`](https://developer.apple.com/documentation/tvuikit/tvmonogramcontentview); configure it with the documented Swift [`TVMonogramContentConfiguration`](https://developer.apple.com/documentation/tvuikit/tvmonogramcontentconfiguration-swift.struct). The DocC `renamed` value is `__TVMonogramContentConfiguration`; this metadata spelling should not be presented as a documented public API name. The tvOS 27.2 deprecation is not a removal notice and does not deprecate the entire TVUIKit framework.

---

*Sources: [Apple Developer Documentation](https://developer.apple.com/documentation/tvuikit), [TVMonogramView](https://developer.apple.com/documentation/tvuikit/tvmonogramview), [TVMonogramContentView](https://developer.apple.com/documentation/tvuikit/tvmonogramcontentview), [TVMonogramContentConfiguration](https://developer.apple.com/documentation/tvuikit/tvmonogramcontentconfiguration-swift.struct), [iOS & iPadOS 27 Release Notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes), [tvOS 27 Release Notes](https://developer.apple.com/documentation/tvos-release-notes/tvos-27-release-notes), [Transitioning to the UIKit scene-based life cycle](https://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle)*
