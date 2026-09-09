# Ratings and Reviews

People often view the ratings and reviews for an app or game before they download it.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

Delivering a great overall experience is the best way to encourage positive ratings and reviews, but it's also crucial to choose the right time to ask people for feedback. Although every app is different, some possible ways to do this involve looking at how many times or how frequently people launch your app, the number of features someone explores, or the number of tasks they complete.

People can also rate and review your app directly in the App Store.

> **Separate creator-content policy:** [App Review Guideline 1.2.1(a)](https://developer.apple.com/app-store/review/guidelines/#creator-content) requires creator apps to let people identify content above the app's age rating and restrict underage access using verified or declared age. This provision is scoped to creator apps, not a general condition for requesting an App Store review. See also [program guidance](../../os27-intro/Program.md).

## Topics

### Best Practices

- **Ask for a rating only after people have demonstrated engagement with your app or game** - For example, you might prompt people when they complete a game level or a significant task. Avoid asking for a rating on first launch or during onboarding, because people haven't had enough time to gain a clear understanding of your app's value or form an opinion. People may even be more likely to leave negative feedback if they feel an app is asking for a rating before they get a chance to use it.

- **Avoid interrupting people while they're performing a task or playing a game** - Asking for feedback can disrupt the user experience and feel like a burden. Look for natural breaks or stopping points in your app or game where a rating request is less likely to be bothersome.

- **Avoid pestering people** - Repeated rating requests can be irritating, and may even negatively influence people's opinion of your app. Consider allowing at least a week or two between requests, prompting again after people demonstrate additional engagement with your experience.

- **Prefer the system-provided prompt** - In SwiftUI, use StoreKit's [RequestReviewAction](https://developer.apple.com/documentation/storekit/requestreviewaction) where available. StoreKit decides whether a request actually displays, and people can opt out of these prompts. If a person hasn't rated or reviewed the app on that device, the limit is three presentations within 365 days. If they have, StoreKit requires a new app version and more than 365 days since their previous review.

- **Don't make a button depend on the prompt appearing** - A request isn't guaranteed to show an alert. For an explicit “Write a review” action, use a persistent App Store product-page link with `action=write-review`. Development builds display the test prompt, but this review-request API has no effect in TestFlight builds.

- **Consider a rating reset carefully** - A new version can start a fresh aggregate rating, but fewer ratings may discourage downloads. Resetting doesn't remove written reviews. App Store Connect applies the reset to the selected platform version across all countries and regions when that version releases; the previous rating can't then be restored. See [Reset an app overview rating](https://developer.apple.com/help/app-store-connect/monitor-ratings-and-reviews/reset-an-app-overview-rating).

### Platform Considerations

No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.

### Related Resources

- [Ratings, reviews, and responses](https://developer.apple.com/app-store/ratings-and-reviews/)

### Developer Documentation

- [RequestReviewAction](https://developer.apple.com/documentation/storekit/requestreviewaction) - StoreKit's SwiftUI review action
- [SKStoreReviewController](https://developer.apple.com/documentation/storekit/skstorereviewcontroller) - Legacy controller; deprecated in iOS/iPadOS/Mac Catalyst 18, macOS 15, and visionOS 2

## Changelog

These dates describe changes to Apple's HIG article, not edits to this repository.

### September 12, 2023
- Added artwork

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews)*
