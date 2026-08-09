# Address Book UI

Access users' contacts and display them in a graphical interface.

**Platforms:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 14.0+

## Overview

The AddressBookUI framework provides controllers that facilitate displaying, editing, selecting, and creating records in the Address Book database.

**Important:** Do not use the AddressBookUI framework in iOS 9 and later. Use the APIs defined in the Contacts UI framework instead.

## Topics

### People Picker
- **ABPeoplePickerNavigationController** - The ABPeoplePickerNavigationController class (whose instances are known as people-picker navigation controllers) implements a view controller that manages a set of views that allow the user to select a contact or one of its contact-information items from an address book. *(Deprecated)*

### Detail Display
- **ABNewPersonViewController** - A view controller presenting an interface to create a contact. *(Deprecated)*
- **ABPersonViewController** - The ABPersonViewController class (whose instances are known as person view controllers) implements the view used to display a person record (ABPersonRef). *(Deprecated)*
- **ABUnknownPersonViewController** - The ABUnknownPersonViewController class (whose instances are known as unknown-person view controllers) implements a view controller used to create a person record from a set of person properties. *(Deprecated)*
- **ABCreateStringWithAddressDictionary([AnyHashable : Any], Bool) -> String** - Returns a formatted address from an address property. *(Deprecated)*

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AddressBookUI)*