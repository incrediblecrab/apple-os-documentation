# SMS and Call Reporting

Create app extensions to manage and report unwanted SMS messages and spam calls.

**SDK catalog:** iOS 11.0+ | iPadOS 11.0+ | Mac Catalyst 13.1+ | macOS 10.15+ | visionOS 1.0+. Extension workflows have their own platform, service, and user-enablement requirements.

## Overview

SMS and Call Reporting provides app extensions to manage unwanted communication.

**Message Filter app extension**  
Identifies and filters unwanted SMS and MMS messages.

**Unwanted Communication app extension**  
Lets people report unwanted SMS messages and calls as spam.

**Live Caller ID Lookup app extension**  
Enables up-to-date calling and blocking information.

### Privacy, enablement, and failures

Message filtering applies only to SMS/MMS from unknown senders, not contacts or iMessage. The system invokes the enabled filter and handles any deferral to its associated server; the filter cannot make direct network requests or write message data to a container shared with the containing app.

Spam reporting is a separate user-initiated flow. Only one reporting extension can be enabled at a time, and cancelling its UI does not submit a report. The system deletes that extension's container after termination.

Live Caller ID Lookup uses Apple's relay service, Privacy Pass authentication, and keyword private information retrieval to conceal the client's identity and queried phone number from the provider's server. It is not a raw incoming-number feed to the app. Register the configuration in CloudKit Console's Identity & Trust area and satisfy the documented Apple endpoint-validation requirements. Check the extension's current enabled status rather than treating installation as activation; cached responses can be reused without a new query for every call.

The Live Caller ID manager and related 18-generation APIs are later than the framework's original 11.0 minimum; the manager's metadata lists iOS/iPadOS/Catalyst 18, macOS 15, and visionOS 2.

## Topics

### Message filtering
- [SMS and MMS Message Filtering](https://developer.apple.com/documentation/identitylookup/sms-and-mms-message-filtering) - Filter eligible unknown-sender messages using the system's privacy-preserving extension flow.

### Spam reporting
- [SMS and Call Spam Reporting](https://developer.apple.com/documentation/identitylookup/sms-and-call-spam-reporting) - Create an app extension that lets users report unwanted SMS messages and calls as junk.

### Live Caller ID Lookup
- [Understanding how Live Caller ID Lookup preserves privacy](https://developer.apple.com/documentation/identitylookup/understanding-how-live-caller-id-lookup-preserves-privacy) - Use Live Caller ID Lookup to protect user privacy by hiding the client's IP address, using anonymous authentication, and hiding the incoming phone number.
- [Formatting data for blocking and identity information](https://developer.apple.com/documentation/identitylookup/formatting-data-for-blocking-and-identity-information) - Set up your PIR payload for call blocking and identity information.
- [Setting up the HTTP endpoints for Live Caller ID Lookup](https://developer.apple.com/documentation/identitylookup/setting-up-the-http-endpoints-for-live-caller-id-lookup) - Connect the on-device system to your server.
- [Getting up-to-date calling and blocking information for your app](https://developer.apple.com/documentation/identitylookup/getting-up-to-date-calling-and-blocking-information-for-your-app) - Implement the Live Caller ID Lookup app extension to provide call-blocking and identity services.
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
