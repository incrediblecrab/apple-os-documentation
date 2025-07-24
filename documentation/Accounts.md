# Accounts

Help users access and manage their external accounts from within your app, without requiring them to enter login credentials.

**Platforms:** iOS 5.0+ | iPadOS 5.0+ | Mac Catalyst 13.0+ | macOS 10.8+

**Deprecated**: The Accounts framework is deprecated. For new apps, instead of using Accounts, contact the provider of the service you integrate with, to get access to their SDK or documentation about managing accounts with their service.

## Overview

The Accounts framework provides access to user accounts stored in the Accounts database, which is managed by the system. An account stores the login credentials of a particular service, such as LinkedIn, and you use those credentials to authenticate with the service. When you integrate the Accounts framework into your app, you don't need to store account logins yourself. Instead, the user grants your app access to use their account login credentials, bypassing the need to type their username and password. If no account for a particular service exists in the user's Accounts database, you can let them create and save an account from within your app.

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