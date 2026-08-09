# Rating Indicators

A rating indicator uses a series of horizontally arranged graphical symbols — by default, stars — to communicate a ranking level.

**Platforms:** macOS

## Overview

A rating indicator doesn't display partial symbols; it rounds the value to display complete symbols only. Within a rating indicator, symbols are always the same distance apart and don't expand or shrink to fit the component's width.

## Topics

### Best Practices

- **Make it easy to change rankings** - When presenting a list of ranked items, let people adjust the rank of individual items inline without navigating to a separate editing screen.
- **If you replace the star with a custom symbol, make sure that its purpose is clear** - The star is a very recognizable ranking symbol, and people may not associate other symbols with a rating scale.

### Platform Considerations

No additional considerations for macOS.

Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.

### Related Components

- [Ratings and reviews](https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews) - Related pattern for app ratings

### Developer Documentation

- [NSLevelIndicator.Style.rating](https://developer.apple.com/documentation/appkit/nslevelindicator/style/rating) - AppKit

## Changelog

### September 23, 2022
- New page.

---

*Design baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Reviewed 2026-08-09.*

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/rating-indicators)*