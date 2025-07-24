# TVUIKit

Show common user interface elements from Apple TV in your native app.

**Platforms:** tvOS 12.0+

## Overview

When you build an app for tvOS with **UIKit**, you can use **TVUIKit** to refine the display of your content for a TV environment. Use the **TV Services** framework to provide deeper integration between your app and Apple TV.

For more information about combining Apple technologies to build a great Apple TV experience, see [Planning your tvOS app](https://developer.apple.com/documentation/tvos/planning_your_tvos_app).

## Topics

### Collections of Content
- [Creating immersive experiences using a full-screen layout](https://developer.apple.com/documentation/tvuikit/creating_immersive_experiences_using_a_full-screen_layout) - Display content with a collection view that maximizes the tvOS experience.
- **TVCollectionViewFullScreenLayout** - A collection view layout that organizes items into a browsable, full-screen display format.
- **TVCollectionViewDelegateFullScreenLayout** - Methods that send notifications of events during cell transitions.
- **TVCollectionViewFullScreenCell** - A full-screen cell to use in full-screen display format.
- **TVCollectionViewFullScreenLayoutAttributes** - Attributes to manage the appearance of the collection view's layout.

### Content Views
- **TVMediaItemContentView** - A view that represents media content, such as movies and TV shows.
- **TVMonogramContentView** - A view that contains a circular image of a person or the person's initials.

### Numeric Input
- **TVDigitEntryViewController** - A view controller that enables the user to enter digits, like a passcode, in your app.

### Lockup Views
- **TVLockupView** - A focusable view that presents main content, like a movie poster, and an optional header and footer.
- **TVLockupViewComponent** - The protocol for responding to lockup view state changes.
- **TVLockupHeaderFooterView** - A view that contains header and footer information.
- **TVCardView** - A view that responds to focus interaction with a motion effect it applies to all of its subviews.
- **TVPosterView** - An optimized view for displaying an image, a header, and a footer.
- **TVCaptionButtonView** - A button-like view that responds to user interactions.
- **TVMonogramView** - A specialized lockup view that contains a circular image of a person or the person's initials, along with a footer view.

### Deprecated
See archived documentation for deprecated classes and methods.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/TVUIKit)*