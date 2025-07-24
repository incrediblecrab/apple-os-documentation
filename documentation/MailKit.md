# MailKit

Secure, customize, and act on email messages that users send and receive.

**Platforms:** macOS 12.0+

## Overview
MailKit lets your app include an app extension that customizes several features of Mail. A Mail app extension provides one or more of the following enhancements:

A content blocker defines rules to prevent loading content when users view messages.

An action handler performs actions such as flagging, setting colors, or archiving when Mail downloads messages.

A compose session handler validates recipient email addresses, displays a view controller on Mail’s compose windows, confirms if messages are suitable for delivery, and adds custom headers.

A message security handler secures messages using encryption and digital signatures.

The entry point for your extension is an object that conforms to MEExtension. When MailKit invokes your extension, this objects determines the handlers that provide each capability in the list above.

## Topics

### Essentials
- **MEExtension** - A type that provides objects for manipulating email messages, such as performing actions on messages or blocking content when users view messages.
- [Build Mail App Extensions](https://developer.apple.com/documentation/mailkit/build_mail_app_extensions) - Create app extensions that block content, perform message and composing actions, and help message security.
### Content Blockers
- **MEContentBlocker** - An object that provides a set of rules to block content when displaying a message.
### Message Actions
- **MEMessageActionHandler** - An object that performs actions on messages as the system downloads them.
### Compose Window Enhancements
- **MEComposeSessionHandler** - An object that participates in the composition of mail messages, and annotates recipient tokens.
### Message Encryption, Decryption, and Digital Signatures
- **MEMessageSecurityHandler** - An object that digitally signs or encrypts messages the user sends and receives.
### Message Properties
- **MEMessage** - An object that contains information about a mail message, such as the subject, addressees, date sent, and the message contents.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MailKit)*
