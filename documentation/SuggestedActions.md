# Suggested Actions

Show contextual quick actions alongside messages in a messaging app.

**Platforms:** iOS 27.0+ | iPadOS 27.0+ | macOS 27.0+ | visionOS 27.0+

**Mac Catalyst:** `SuggestedActionsView` and `SuggestedActionsMessage` explicitly list 27.0+. The framework landing page does not enumerate Catalyst.

## Overview

Suggested Actions analyzes message content supplied by your app on device, then offers relevant actions such as creating a calendar event, adding a reminder, or opening a location. It does not send that message content to Apple servers for this analysis.

Add the **`com.apple.developer.suggested-actions` entitlement** to the app target. This framework provides a messaging integration, not a general-purpose API for generating arbitrary app actions.

## Topics

### Message context

- [`SuggestedActionsMessage`](https://developer.apple.com/documentation/suggestedactions/suggestedactionsmessage.md) — Represent a message with `init(id:date:subject:body:sender:recipients:)`.
- [`SuggestedActionsMessage.Participant`](https://developer.apple.com/documentation/suggestedactions/suggestedactionsmessage/participant.md) — Describe a sender or recipient.
- [`previousMessagesLimit`](https://developer.apple.com/documentation/suggestedactions/suggestedactionsmessage/previousmessageslimit.md) — Read the context limit at runtime and bound the preceding conversation accordingly; its value can change between OS releases.

Assign a unique message identifier that remains stable across launches. Cached suggestions are matched using this identifier, so generating a fresh ID for an unchanged message defeats reuse.

### Presentation and preparation

- [`SuggestedActionsView`](https://developer.apple.com/documentation/suggestedactions/suggestedactionsview.md) — A `@MainActor` SwiftUI view placed beside message content.
- [`init(message:previousMessages:)`](https://developer.apple.com/documentation/suggestedactions/suggestedactionsview/init(message:previousmessages:).md) — Supply the message and relevant preceding context.
- [`generate(message:previousMessages:)`](https://developer.apple.com/documentation/suggestedactions/suggestedactionsview/generate(message:previousmessages:).md) — Prepare and cache suggestions before the view is shown.
- [Suggested Actions entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.suggested-actions.md) — Check target configuration requirements.

When no suggestions are available, the view has zero size. Keep the message and existing app actions usable whether or not a suggestion appears; do not reserve a permanent gap or treat no suggestion as a failed message.

## Validation

Check stable identifiers, bounded context, entitlement configuration, no-action messages, delayed results, and unavailable-OS fallback. Test the surrounding message flow with [XCTest](XCTest.md) and [XCUIAutomation](XCUIAutomation.md); do not assert that every message must produce an action.

**Provisioning qualification:** The entitlement reference currently lists iOS/iPadOS 27.0+, while the framework's symbols also list Mac Catalyst, macOS, and visionOS. Confirm signing and provisioning for the selected destination; the platform metadata alone does not verify that configuration.

For making your own app's capabilities available to system experiences, see [App Intents](AppIntents.md) and [App Intents Testing](AppIntentsTesting.md).

*Sources: [Suggested Actions](https://developer.apple.com/documentation/suggestedactions.md), [SuggestedActionsView](https://developer.apple.com/documentation/suggestedactions/suggestedactionsview.md).*
