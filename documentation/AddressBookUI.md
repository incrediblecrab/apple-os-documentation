# Address Book UI

Access users' contacts and display them in a graphical interface.

**Platforms:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 14.0+

## Overview

The AddressBookUI framework provides controllers that facilitate displaying, editing, selecting, and creating records in the Address Book database.

**Important:** Apple directs iOS 9-and-later apps to [Contacts UI](https://developer.apple.com/documentation/contactsui) instead. This is supported by actual symbol deprecations: [`ABPeoplePickerNavigationController`](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller) is deprecated at iOS/iPadOS 9.0 and at Mac Catalyst 13.1, with `CNContactPickerViewController` as its replacement.

These deprecations predate OS 27 and do not establish a new removal date. When migrating, use [Contacts](Contacts.md) for authorized data access and Contacts UI for selection/editing. Handle cancellation and restricted or limited access rather than assuming that presenting a legacy picker grants access to the entire contact store.

## Topics

### People Picker
- **ABPeoplePickerNavigationController** - The ABPeoplePickerNavigationController class (whose instances are known as people-picker navigation controllers) implements a view controller that manages a set of views that allow the user to select a contact or one of its contact-information items from an address book. *(Deprecated)*

### Detail Display
- **ABNewPersonViewController** - A view controller presenting an interface to create a contact. *(Deprecated)*
- **ABPersonViewController** - The ABPersonViewController class (whose instances are known as person view controllers) implements the view used to display a person record (ABPersonRef). *(Deprecated)*
- **ABUnknownPersonViewController** - The ABUnknownPersonViewController class (whose instances are known as unknown-person view controllers) implements a view controller used to create a person record from a set of person properties. *(Deprecated)*
- **ABCreateStringWithAddressDictionary([AnyHashable : Any], Bool) -> String** - Returns a formatted address from an address property. *(Deprecated)*

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AddressBookUI)*
