# Shared with You

Surface relevant shared links and provide system attribution and collaboration interactions.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 16.0+ | macOS 13.0+ | tvOS 16.0+ | visionOS 1.0+. Check individual UI and collaboration APIs for platform support. This framework predates OS 27.

## Overview

Shared with You lets an app display content that the system surfaces from sharing conversations. Build a shelf around the supplied highlights and use system attribution views to let people return to the associated conversation.

The system decides which links to expose and how to rank them. The framework is not permission to read a person's Messages database, and a highlight does not grant access to otherwise private content on your server.

## Prerequisites

1. Support universal links through a two-way app/website association and the Associated Domains capability.
2. Handle the incoming browsing `NSUserActivity` and resolve its URL to content your app understands.
3. Add the Shared with You capability in Xcode.
4. Retain an [`SWHighlightCenter`](https://developer.apple.com/documentation/sharedwithyou/swhighlightcenter), set its delegate, and update the shelf when the system changes its highlights.

See [Making your app content shareable](https://developer.apple.com/documentation/sharedwithyou/making-your-app-content-shareable) for the complete integration.

## Topics

- [`SWHighlightCenter`](https://developer.apple.com/documentation/sharedwithyou/swhighlightcenter) — Obtain the priority-ordered `highlights` list and its localized collection title.
- [`SWHighlightCenterDelegate`](https://developer.apple.com/documentation/sharedwithyou/swhighlightcenterdelegate) — Respond when the list or ranking changes.
- [`SWHighlight`](https://developer.apple.com/documentation/sharedwithyou/swhighlight) — Identify the shared URL represented by an item.
- [`SWAttributionView`](https://developer.apple.com/documentation/sharedwithyou/swattributionview) — Display system attribution and supported contextual interactions.
- [Shared content interactions](https://developer.apple.com/documentation/sharedwithyou/shared-content-interactions) — Connect content presentation to sharing interactions.
- [Adding shared content collaboration](https://developer.apple.com/documentation/sharedwithyou/adding-shared-content-collaboration-to-your-app) and [Adding custom collaboration](https://developer.apple.com/documentation/sharedwithyou/adding-custom-collaboration-to-your-app) — Integrate collaboration rather than treating a shared link as a collaboration session.
- [Shared with You Core](https://developer.apple.com/documentation/sharedwithyoucore) — Related infrastructure for custom collaboration with Messages, Mail, and FaceTime.

## Authorization, privacy, and failure handling

Use the app's normal authentication and content-access checks when resolving a highlighted URL. Validate the URL's supported domain and route; never bypass document permissions because it appeared in a shelf.

An empty highlight list can be a normal system result. Do not interpret it as proof that the person has never shared content. Reconcile the entire current list after delegate updates so removed or reordered highlights do not leave stale attribution behind.

Handle lookup failures using [`SWHighlightCenterErrorCode`](https://developer.apple.com/documentation/sharedwithyou/swhighlightcentererrorcode). If the underlying content is unavailable or the network fails, offer an appropriate unavailable/retry state without manufacturing an attribution. Check the highlight center's system collaboration support before relying on full Messages collaboration features.

## Sources

- [Shared with You](https://developer.apple.com/documentation/sharedwithyou)
- [Making your app content shareable](https://developer.apple.com/documentation/sharedwithyou/making-your-app-content-shareable)
- [SWHighlightCenter](https://developer.apple.com/documentation/sharedwithyou/swhighlightcenter)
