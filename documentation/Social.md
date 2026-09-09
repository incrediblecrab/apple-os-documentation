# Social

Post content to supported social networking services, using standard system interfaces.

**Platforms:** iOS 6.0+ | iPadOS 6.0+ | Mac Catalyst 13.0+ | macOS 10.8+

## Overview

Social provides HTTP request templates and composition interfaces with different platform scopes. `SLComposeViewController` is the iOS/iPadOS/Mac Catalyst service composer; `SLComposeServiceViewController` supports custom sharing extensions on iOS and macOS.

A common way to use this framework is:

1. Create a network session.
2. Get the activity feed for a user.
3. Make a new post.
4. Set properties on a post, add attachments, etc.
5. Publish a post to an activity feed.

An `SLRequest` still needs the target service's URL, parameters, and applicable account authorization. This legacy framework reference does not establish that any particular social network's historical integration remains available.

## Topics

### Composition Interfaces
- [`SLComposeServiceViewController`](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller) - A sharing-extension composer, available from iOS/iPadOS 8.0, Mac Catalyst 13.1, and macOS 10.10.
- [`SLComposeViewController`](https://developer.apple.com/documentation/social/slcomposeviewcontroller) - A service composer on iOS/iPadOS 6.0+ and Mac Catalyst 13.1+. Check service availability before presentation; set initial content before presenting the controller.

### Server Communication
- [`SLRequest`](https://developer.apple.com/documentation/social/slrequest) - Assemble a service-specific HTTP request; available from iOS/iPadOS 6.0, Mac Catalyst 13.1, and macOS 10.8.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Social)*
