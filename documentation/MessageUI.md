# Message UI

Create a user interface for composing email and text messages, so users can edit and send messages without leaving your app.

**Platforms:** iOS 3.0+ | iPadOS 3.0+ | Mac Catalyst 13.0+ | visionOS 1.0+

## Overview

The Message UI framework provides specialized view controllers for presenting standard composition interfaces for email and SMS (Short Messaging Service) text messages. Use these interfaces to add message delivery capabilities, without requiring the user to leave your app.

To display a composition interface, present the corresponding view controller modally from your app. Once presented, the user has the option to customize the contents before sending or canceling the message. Your custom delegate object then handles the dismissal of the view controller based on the user's action. For information on how to present and dismiss view controllers, see View Controller Programming Guide for iOS.

**Important:** The view controllers in this framework provide methods for determining if you can send a given message type on the current iOS device. If you can't send a message, don't display the corresponding view controller.

## Topics

### Email composition interface
- **MFMailComposeViewController** - A standard view controller, whose interface lets the user manage, edit, and send email messages.

### Message composition interface
- **MFMessageComposeViewController** - A standard view controller whose interface lets the user compose and send SMS or MMS messages.

### Enumerations
- **MFMailComposeControllerDeferredAction**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MessageUI)*