# Lockups

Lockups combine multiple separate views into a single, interactive unit.

**Platforms:** tvOS

## Overview

Each lockup consists of a content view, a header, and a footer. Headers appear above the main content for a lockup, and footers appear below the main content. All three views expand and contract together as the lockup gets focus.

According to the needs of your app, you can combine four types of lockup: cards, caption buttons, monograms, and posters.

## Topics

### Best Practices

- **Allow adequate space between lockups** - A focused lockup expands in size, so leave enough room between lockups to avoid overlapping or displacing other lockups. For guidance, see Layout.
- **Use consistent lockup sizes within a row or group** - A group of buttons or a row of content images is more visually appealing when the widths and heights of all elements match.

### Cards

A card combines a header, footer, and content view to present ratings and reviews for media items.

For developer guidance, see TVCardView.

### Caption Buttons

A caption button can include a title and a subtitle beneath the button. A caption button can contain either an image or text.

- **Make sure that when people focus on them, caption buttons tilt with the motion that they swipe** - When aligned vertically, caption buttons tilt up and down. When aligned horizontally, caption buttons tilt left and right. When displayed in a grid, caption buttons tilt both vertically and horizontally.

For developer guidance, see TVCaptionButtonView.

### Monograms

Monograms identify people, usually the cast and crew for a media item. Each monogram consists of a circular picture of the person and their name. If an image isn't available, the person's initials appear in place of an image.

- **Prefer images over initials** - An image of a person creates a more intimate connection than text.

For developer guidance, see TVMonogramContentView.

### Posters

Posters consist of an image and an optional title and subtitle, which are hidden until the poster comes into focus. Posters can be any size, but the size needs to be appropriate for their content. For related guidance, see Image views.

For developer guidance, see TVPosterView.

### Platform Considerations

Not supported in iOS, iPadOS, macOS, visionOS, or watchOS.

### Related Components

- [Designing for tvOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos)
- [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)

### Developer Documentation

- [TVLockupView](https://developer.apple.com/documentation/tvuikit/tvlockupview) - TVUIKit
- [TVLockupHeaderFooterView](https://developer.apple.com/documentation/tvuikit/tvlockupheaderfooterview) - TVUIKit

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/lockups)*