# PermissionKit

Create communication experiences between a child and their parent or guardian.

**Platforms:** iOS 26.0+ | iPadOS 26.0+ | Mac Catalyst 26.0+ | macOS 26.0+ | visionOS 26.0+

## Overview

Use **PermissionKit** in your app to adjust communication rules for a child account on iCloud. PermissionKit provides a way to create consistent asking experiences between a child and their parent or guardian that maintains UI consistency with other communication experiences across the system.

**Important:** Communication experiences using the PermissionKit framework are only available using iMessage.

### Requests are not approvals

Create an appropriate `PermissionQuestion` when an action needs a parent's or guardian's decision. Handle cancelled sending, unavailable communication, `AskError`, declined responses, and pending requests separately. If the child cancels the send flow, the system does **not** deliver a response for that question; absence of a response must not unlock the requested capability.

Observe responses and match them to the relevant question and topic before changing access. Reevaluate current communication limits when they change instead of treating a past approval as permanent or applying it to unrelated contacts.

### Current and compatibility interfaces

**Reviewed September 8, 2026:** `AskCenter`, `PermissionButton`, `SignificantAppUpdateTopic`, and `AskCenter.responses(for:)` are **26.2+** APIs on the framework's supported platforms. The response method registers a topic type and returns an asynchronous sequence. These APIs are not all available at PermissionKit's original 26.0 minimum, and are not new solely because an example uses Xcode 27.

Use [Declared Age Range](DeclaredAgeRange.md) for its supported age-feature and significant-update queries. A communication permission, an age-range response, and acknowledgment of an app update are different results; one does not imply the others.

## Topics

### Essentials
- [Creating a communication experience](https://developer.apple.com/documentation/permissionkit/creating-a-communication-experience) - Request permission and handle communication-response delivery.
- [AskCenter](https://developer.apple.com/documentation/permissionkit/askcenter) - Sends permission questions and observes topic-specific responses.

### Permission buttons
- [PermissionButton](https://developer.apple.com/documentation/permissionkit/permissionbutton) - Current system permission-request presentation, available from 26.2.
- **CommunicationLimitsButton** - The original 26.0 presentation API, retained for compatibility; Apple's framework page places it under deprecated APIs.

### Permission responses
- [AskCenter.responses(for:)](https://developer.apple.com/documentation/permissionkit/askcenter/responses(for:)) - Registers a topic and returns its response sequence.
- **CommunicationLimits** - A type that encapsulates the communication limits for your app.
- **CommunicationHandle** - A piece of identifying information that can be used to communicate with someone.
- **PermissionResponse** - A full permission response that includes the original question and chosen answer.

### Permission questions
- **QuestionTopic** - A protocol that defines a question topic that can be used to interpret what a user is asking for.
- **PermissionQuestion** - A class that captures a permission question posed by a user.
- **CommunicationTopic** - A question topic related to communication.
- [SignificantAppUpdateTopic](https://developer.apple.com/documentation/permissionkit/significantappupdatetopic) - A question about a significant app update.
- **PermissionChoice** - A class that uniquely identifies a specific, statically defined permission choice.

### Error response
- **AskError** - An error that can occur when asking someone to send a communication permission question.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/PermissionKit)*

*Changed-content sources: [framework reference](https://developer.apple.com/documentation/permissionkit.md), [communication lifecycle](https://developer.apple.com/documentation/permissionkit/creating-a-communication-experience.md), and [AskCenter availability](https://developer.apple.com/tutorials/data/documentation/permissionkit/askcenter.json).*
