# Collaboration

Find and access identities, that is, users and groups. Display the Identity Picker, which lets users create and select identities.

**Platforms:** macOS 10.5+

## Overview

The Collaboration framework allows developers to monitor identities and their attributes. Identities reside in an identity authority, which can be either local to a user's system, or on a network directory. The Collaboration framework also manages a sheet, known as the identity picker, to allow applications to select identities.

The Collaboration framework works closely with the Core Services Identity APIs to form the Identity Services technology. If you need the ability to create and manipulate identities read Core Services Identity Reference.

## Topics

### Classes
- **CBGroupIdentity** - An object of the CBGroupIdentity class represents a group identity and is used for viewing the attributes of group identities from an identity authority. The principal attributes of a CBGroupIdentity object are a POSIX group identifier (GID) and a list of members.
- **CBIdentity** - Access an identity's attributes and represent the identity in an access control list (ACL). Use the Core Services Identity APIs when you need to edit attributes.
- **CBIdentityAuthority** - An identity authority is a database that stores information about identities. The CBIdentityAuthority class defines one or more identity authorities. You can search this database for identities in conjunction with the CBIdentity class factory methods.
- **CBIdentityPicker** - Present an application-modal picker or document sheet and return selected user/group identities for use in ACLs. A record that is not yet a user or group identity can require additional information to become a sharing account.
- **CBUserIdentity** - Represent a user identity, inspect its POSIX UID and certificate, or authenticate a supplied password with `authenticate(withPassword:)`. The authentication method is not a stored-password getter.

## See Also

### Related Documentation
- **Core Services Identity Reference**
- **Identity Services Programming Guide**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Collaboration)*
