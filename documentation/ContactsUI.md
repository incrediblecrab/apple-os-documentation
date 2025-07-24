# Contacts UI

Provide an interface that allows people to display information about their contacts.

**Platforms:** iOS 9.0+ | iPadOS 9.0+ | Mac Catalyst 13.0+ | macOS 10.11+ | visionOS 1.0+

## Overview

The Contacts UI framework contains user interface objects that provide access to a person's contacts in your app. Depending on your app's authorization level for using contacts (as indicated by authorizationStatus(for:)), your app may be able to display, edit, select, and create contacts. When the authorization level is CNAuthorizationStatus.limited, you can display a ContactAccessButton to request access to contacts beyond the limited set a person has currently granted your app access to.

## Topics

### Contact viewer
- **CNContactViewController** - A view controller that displays a new, unknown, or existing contact.

### Contact pickers
- **CNContactPickerViewController** - A view controller that displays an interface for picking contacts.
- **CNContactPicker** - A popover-based interface for selecting a contact.

### Contact access
- **ContactAccessButton** - A SwiftUI button that you use to add to the set of contacts someone shares with your app.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ContactsUI)*