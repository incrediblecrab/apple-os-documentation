# PermissionKit

Create communication experiences between a child and their parent or guardian.

**Platforms:** iOS 26.0+ (Beta) | iPadOS 26.0+ (Beta) | Mac Catalyst 26.0+ (Beta) | macOS 26.0+ (Beta) | visionOS 26.0+ (Beta)

## Overview

Use **PermissionKit** in your app to adjust communication rules for a child account on iCloud. PermissionKit provides a way to create consistent asking experiences between a child and their parent or guardian that maintains UI consistency with other communication experiences across the system.

**Important:** Communication experiences using the PermissionKit framework are only available using iMessage.

## Topics

### Essentials
- [Creating a communication experience](https://developer.apple.com/documentation/permissionkit/creating_a_communication_experience) - Request permission from a parent or guardian to modify a child's communication rules.

### Permission buttons
- **CommunicationLimitsButton** - A button that presents a system UI to a parent or guardian to ask for an exception to a child's communication limits.

### Permission responses
- **CommunicationLimits** - A type that encapsulates the communication limits for your app.
- **CommunicationHandle** - A piece of identifying information that can be used to communicate with someone.
- **PermissionResponse** - A full permission response that includes the original question and chosen answer.

### Permission questions
- **QuestionTopic** - A protocol that defines a question topic that can be used to interpret what a user is asking for.
- **PermissionQuestion** - A class that captures a permission question posed by a user.
- **CommunicationTopic** - A question topic related to communication.
- **PermissionChoice** - A class that uniquely identifies a specific, statically defined permission choice.

### Error response
- **AskError** - An error that can occur when asking someone to send a communication permission question.

---

**Beta Software**

This documentation contains preliminary information about an API or technology in development. This information is subject to change, and software implemented according to this documentation should be tested with final operating system software.

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/PermissionKit)*