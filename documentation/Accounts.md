# Accounts

Help users access and manage their external accounts from within your app, without requiring them to enter login credentials.

**Platforms:** iOS 5.0+ | iPadOS 5.0+ | Mac Catalyst 13.0+ | macOS 10.8+

**Deprecated**: The Accounts framework is deprecated. For new apps, instead of using Accounts, contact the provider of the service you integrate with, to get access to their SDK or documentation about managing accounts with their service.

## Overview

The legacy Accounts model provides access to user accounts in a system-managed database. A stored account contains credentials for a service, and the person can authorize an app to use those credentials rather than reenter them. The historical APIs also support creating and saving accounts. This describes the deprecated framework's model, not a promise that a particular third-party service still integrates with it; use the service provider's current authentication guidance for new work.

## Topics

### Account Management
- **ACAccountStore** - The object you use to request, manage, and store the user's account information.
- **ACAccount** - The information associated with one of the user's accounts.
- **ACAccountCredential** - A credential object that encapsulates the information needed to authenticate a user.

### Account Types
- **ACAccountType** - An object that encapsulates information about all accounts of a particular type.

### Errors
- **ACErrorCode** - Codes for errors that may occur.
- **ACErrorDomain** - The error domain for the Accounts framework.

### Deprecated
- **Deprecated Symbols** - Avoid using deprecated symbols in your apps.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Accounts)*
