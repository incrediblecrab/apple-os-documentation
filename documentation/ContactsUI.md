# Contacts UI

Provide an interface that allows people to display information about their contacts.

**Platforms:** iOS 9.0+ | iPadOS 9.0+ | Mac Catalyst 13.0+ | macOS 10.11+ | visionOS 1.0+

## Overview

The Contacts UI framework contains user interface objects that provide access to a person's contacts in your app. Depending on your app's authorization level for using contacts (as indicated by authorizationStatus(for:)), your app may be able to display, edit, select, and create contacts. When the authorization level is CNAuthorizationStatus.limited, you can display a ContactAccessButton to request access to contacts beyond the limited set a person has currently granted your app access to.

[`ContactAccessButton`](https://developer.apple.com/documentation/contactsui/contactaccessbutton) requires iOS/iPadOS/Mac Catalyst 18+, unlike the framework's older contact pickers. It expands limited access through an explicit user action; under denied authorization it offers an access prompt, and under full authorization it doesn't appear.

On iOS/iPadOS 18+, [`contactAccessPicker(isPresented:completionHandler:)`](https://developer.apple.com/documentation/swiftui/view/contactaccesspicker(ispresented:completionhandler:)) presents access management without your own search field. Use it under **limited** authorization; otherwise its completion result is empty. The callback contains newly granted contact identifiers, not identifiers for contacts whose access was removed. The method doesn't list Mac Catalyst support.

By contrast, `CNContactPickerViewController` can return the person's selected contacts or properties without requesting address-book authorization. This selection interface isn't interchangeable with the limited-access management controls.

## Topics

### Contact viewer
- [`CNContactViewController`](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller) - Displays a new, unknown, or existing contact.

### Contact pickers
- [`CNContactPickerViewController`](https://developer.apple.com/documentation/contactsui/cncontactpickerviewcontroller) - A selection controller; iOS/iPadOS 9+, Mac Catalyst 13.1+, and visionOS 1+.
- [`CNContactPicker`](https://developer.apple.com/documentation/contactsui/cncontactpicker) - The macOS 10.11+ popover-based contact picker.

### Contact access
- [`ContactAccessButton`](https://developer.apple.com/documentation/contactsui/contactaccessbutton) - A SwiftUI button for requesting additional shared contacts.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/ContactsUI)*
