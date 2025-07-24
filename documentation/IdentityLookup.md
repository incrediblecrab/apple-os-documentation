# SMS and Call Reporting

Create app extensions to manage and report unwanted SMS messages and spam calls.

**Platforms:** iOS 11.0+ | iPadOS 11.0+ | Mac Catalyst 13.1+ | macOS 10.15+ | visionOS 1.0+

## Overview

SMS and Call Reporting provides app extensions to manage unwanted communication.

**Message Filter app extension**  
Identifies and filters unwanted SMS and MMS messages.

**Unwanted Communication app extension**  
Lets people report unwanted SMS messages and calls as spam.

**Live Caller ID Lookup app extension**  
Enables up-to-date calling and blocking information.

## Topics

### Message filtering
- [SMS and MMS Message Filtering](https://developer.apple.com/documentation/identitylookup/sms_and_mms_message_filtering) - Create an app extension that identifies and filters unwanted SMS and MMS messages while preserving user privacy.

### Spam reporting
- [SMS and Call Spam Reporting](https://developer.apple.com/documentation/identitylookup/sms_and_call_spam_reporting) - Create an app extension that lets users report unwanted SMS messages and calls as junk.

### Live Caller ID Lookup
- [Understanding how Live Caller ID Lookup preserves privacy](https://developer.apple.com/documentation/identitylookup/understanding_how_live_caller_id_lookup_preserves_privacy) - Use Live Caller ID Lookup to protect user privacy by hiding the client's IP address, using anonymous authentication, and hiding the incoming phone number.
- [Formatting data for blocking and identity information](https://developer.apple.com/documentation/identitylookup/formatting_data_for_blocking_and_identity_information) - Set up your PIR payload for call blocking and identity information.
- [Setting up the HTTP endpoints for Live Caller ID Lookup](https://developer.apple.com/documentation/identitylookup/setting_up_the_http_endpoints_for_live_caller_id_lookup) - Connect the on-device system to your server.
- [Getting up-to-date calling and blocking information for your app](https://developer.apple.com/documentation/identitylookup/getting_up-to-date_calling_and_blocking_information_for_your_app) - Implement the Live Caller ID Lookup app extension to provide call-blocking and identity services.
- **LiveCallerIDLookupProtocol** - Information the system uses to query the app extension for context.
- **LiveCallerIDLookupExtensionConfiguration** - An object that allows the system to query the app extension.
- **LiveCallerIDLookupExtensionContext** - The information the system uses for configuration.
- **CallLookupExtensionStatus** - Returns a value with the current state of the app extension.
- **LiveCallerIDLookupManager** - The entry point that provides access to a collection of functions that help manage the state of the Live Caller ID Lookup app extension.

### Macros
- **Macros**

### Type Aliases
- **BlockingInfoCoreDataPropertiesSet**
- **IdentityInfoCoreDataPropertiesSet**
- **LiveLookupDBExtensionCoreDataPropertiesSet**
- **LiveLookupStoreCoreDataFrameworkManagedObject**
- **LiveLookupStoreFoundationFrameworkSet**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/IdentityLookup)*