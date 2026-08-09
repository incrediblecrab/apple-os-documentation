# Social

Post content to supported social networking services, using standard system interfaces.

**Platforms:** iOS 6.0+ | iPadOS 6.0+ | Mac Catalyst 13.0+ | macOS 10.8+

## Overview

On iOS and macOS, this framework provides a template for creating HTTP requests. On iOS only, the Social framework provides a generalized interface for posting requests on behalf of the user.

A common way to use this framework is:

1. Create a network session.
2. Get the activity feed for a user.
3. Make a new post.
4. Set properties on a post, add attachments, etc.
5. Publish a post to an activity feed.

## Topics

### Composition Interfaces
- **SLComposeServiceViewController** - A view controller that you present from your share app extension, allowing the user to compose social media posts.
- **SLComposeViewController** - A view controller that allows the user to compose social media posts.

### Server Communication
- **SLRequest** - An object that you use to assemble an HTTP request for communicating with a social media service.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Social)*