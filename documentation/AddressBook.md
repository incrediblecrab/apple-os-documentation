# Address Book

Access the centralized database for storing users' contacts.

**Platforms:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 14.0+ | macOS 10.2+

## Overview

The Address Book is a centralized database containing contacts and their personal information. Users enter personal information about themselves and their friends only once, instead of entering it repeatedly whenever the information is used. Apps that support the AddressBook framework share this contact information with other apps, including Apple's Mail and Messages.

**Migration recommendation:** Apple says not to use AddressBook for macOS 10.11-and-later development; use [Contacts](Contacts.md) instead. That framework-level recommendation is not an OS 27 removal notice. The reviewed macOS [`ABAddressBook`](https://developer.apple.com/documentation/addressbook/abaddressbook-swift.class) declaration does not carry a dated deprecation annotation; do not turn the recommendation into an invented universal SDK deprecation date.

Keep this reference for legacy integration work, consult individual symbols for platform-specific status, and use modern Contacts authorization rather than assuming database access is automatically granted. [Address Book UI](AddressBookUI.md) has separately documented iOS deprecations.

## Topics

### Essentials
- [`ABAddressBook`](https://developer.apple.com/documentation/addressbook/abaddressbook-swift.class) - The legacy macOS address-book object.

### Data Types
- **ABPerson** - An object that encapsulates all information about a person in the Address Book database.
- **ABGroup** - An object that represents a group of records in the Address Book database.
- **ABMultiValue** - An immutable representation of a property that might have multiple values.
- **ABMutableMultiValue** - A mutable representation of a property that might have multiple values.
- **ABImageClient** - Methods for responding to a request to load images associated with a contact.
- **ABRecord** - An abstract class that defines the common properties for all Address Book records.

### Pickers
- **ABPeoplePickerView** - An object you use to customize the behavior of people-picker views in an app's user interface.
- **ABPersonView** - An object that provides a view for displaying and editing contacts.

### Search Elements
- **ABSearchElement** - An object you use to specify a search query for records in the Address Book database.
- **ABSearchElementRef** - A reference to an ABSearchElement object.

### Action Plug-In
- **ABActionDelegate** - Implement an Address Book action plug-in to support the display of rollover menus on top of custom items.

### C Interfaces
- **C Types** - Identify the C types that correspond to Address Book objects.
- **AddressBook Functions** - Find the C functions and function-like macros you use to manipulate Address Book data.
- **Address Book Constants** - Get the constants you use to specify Address Book information.
- **AddressBook Enumerations** - Get the enumerations you use to specify Address Book information.
- **AddressBook Data Types** - Get the data types you use to specify Address Book information.

### Deprecated symbols
- [Deprecated symbols](https://developer.apple.com/documentation/addressbook/deprecated-symbols) - Check individual legacy symbols and their replacements.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AddressBook)*
