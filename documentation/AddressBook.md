# Address Book

Access the centralized database for storing users' contacts.

**Platforms:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 14.0+ | macOS 10.2+

## Overview

The Address Book is a centralized database containing contacts and their personal information. Users enter personal information about themselves and their friends only once, instead of entering it repeatedly whenever the information is used. Apps that support the AddressBook framework share this contact information with other apps, including Apple's Mail and Messages.

**Important:** Do not use the AddressBook framework in macOS 10.11 and later. Use the APIs defined in the Contacts framework instead.

## Topics

### Essentials
- **ABAddressBook** - The main object you use to access the Address Book database.

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
- **Deprecated symbols** - Review unsupported symbols and their replacements.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AddressBook)*