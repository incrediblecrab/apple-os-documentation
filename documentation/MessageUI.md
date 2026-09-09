# Message UI

Create a user interface for composing email and text messages, so users can edit and send messages without leaving your app.

**Platforms:** iOS 3.0+ | iPadOS 3.0+ | Mac Catalyst 13.0+ | visionOS 1.0+

## Overview

The Message UI framework provides specialized view controllers for presenting standard composition interfaces for email and SMS (Short Messaging Service) text messages. Use these interfaces to add message delivery capabilities, without requiring the user to leave your app.

Configure recipients, subject where supported, body, and attachments before presenting the composer modally. The person can then edit, send, or cancel. Assign a delegate and explicitly dismiss the controller when it reports completion; don't modify the controller's private view hierarchy.

**Important:** Check [`canSendMail()`](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/cansendmail()) or [`canSendText()`](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/cansendtext()) before presenting the corresponding interface. Check attachment and subject capabilities separately for messages. Framework availability doesn't mean the device or account can send that message type.

Composition completion isn't proof of delivery. Mail queues an approved message in its outbox, and the Mail or Messages app handles actual sending. MessageUI doesn't provide silent, app-controlled delivery.

## Topics

### Email composition interface
- [`MFMailComposeViewController`](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller) - A user-approved email composer; iOS/iPadOS 3+, Mac Catalyst 13.1+, and visionOS 1+.

### Message composition interface
- [`MFMessageComposeViewController`](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller) - An SMS/MMS composer; iOS/iPadOS 4+, Mac Catalyst 13.1+, and visionOS 1+, subject to capability checks.

### Enumerations
- [`MFMailComposeControllerDeferredAction`](https://developer.apple.com/documentation/messageui/mfmailcomposecontrollerdeferredaction) - An enumeration declaration in the reference. The page doesn't document cases or a composition workflow for it; use the documented composer interfaces above.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MessageUI)*
