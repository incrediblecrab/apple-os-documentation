# CallKit

Display the system-calling UI for your app's VoIP services, and coordinate your calling services with other apps and the system.

**Platforms:** iOS 10.0+ | iPadOS 10.0+ | Mac Catalyst 13.0+ | macOS 13.0+ | visionOS 1.0+ | watchOS 9.0+

## Overview

Use CallKit to integrate your calling services with other call-related apps in the system. CallKit provides the calling interface, and you handle the back-end communication with your VoIP service. See [Making and receiving VoIP calls](https://developer.apple.com/documentation/callkit/making-and-receiving-voip-calls) for more information.

CallKit integrates calls with the platform's system calling interface. Reporting an incoming call does not guarantee that it will be presented or connected: system filtering, Do Not Disturb, and service failures can affect the outcome.

In addition to handling calls, you can use a Call Directory app extension to provide caller ID information and a list of blocked numbers associated with your service. See [Identifying and blocking calls](https://developer.apple.com/documentation/callkit/identifying-and-blocking-calls) for more information. Directory entries are supplied when the extension loads, not fetched from your server individually for each incoming call.

### Manage user privacy

With a person's permission, an installed health research app that uses SensorKit entitlements may collect Speech Metrics data while your CallKit app is in use. On iOS/iPadOS 17+, you can set [`SRResearchDataGeneration`](https://developer.apple.com/documentation/bundleresources/information-property-list/srresearchdatageneration) to `NO` to prevent your app's use from contributing this data; its default is `YES`.

> **Important**
> 
> When a person makes a call in your app that uses CallKit, your app provides the contact information of the recipient to the system. The system may use that information to indicate communication with that person as a suggestion in the Journal app, or in other apps that use the Journaling Suggestions framework.

### Become the default calling app

In iOS and iPadOS 18.2 and later, a person may select an app — other than the Phone app or FaceTime — to place calls by default. To make your CallKit or LiveCommunicationKit app support the default calling app setting, see [Preparing your app to be the default calling app](https://developer.apple.com/documentation/callkit/preparing-your-app-to-be-the-default-calling-app).

The app needs the `com.apple.developer.calling-app` entitlement, the `voip` background mode, and integration with CallKit or LiveCommunicationKit. Handle `tel:` requests, and use a `telephony:` fallback only following the person's explicit action. Default calling is distinct from default cellular dialing; see [LiveCommunicationKit](LiveCommunicationKit.md).

## Topics

### Essentials
Call-related actions route through your provider and its delegate, which you use to communicate with your service.
- **CXProvider** - An object that represents a telephony provider.
- **CXProviderDelegate** - A collection of methods that a telephony provider object calls.
- **CXProviderConfiguration** - An encapsulation of the configuration of a provider object.

### Making and receiving VoIP calls
Initiate outgoing calls with VoIP and configure your app to receive incoming calls.
- [VoIP calling with CallKit](https://developer.apple.com/documentation/callkit/voip-calling-with-callkit) - Use the CallKit framework to integrate native VoIP calling.
- [Preparing your app to be the default calling app](https://developer.apple.com/documentation/callkit/preparing-your-app-to-be-the-default-calling-app) - Configure your CallKit or LiveCommunicationKit app so people can set it as the default calling app on their device.
- [CallKit updates](https://developer.apple.com/documentation/updates/callkit) - Learn about important changes to CallKit.

### Incoming calls
Report an incoming call through the provider's `reportNewIncomingCall(with:update:completion:)` using a call UUID and `CXCallUpdate`. Follow the applicable [PushKit](PushKit.md) callback's reporting requirements and handle reporting errors. An answer action is a later system request, not the initial incoming-call report.
- [Responding to VoIP Notifications from PushKit](https://developer.apple.com/documentation/pushkit/responding-to-voip-notifications-from-pushkit) - Receive incoming Voice-over-IP (VoIP) push notifications and use them to display the system call interface to the user.
- **CXCallUpdate** - An encapsulation of new and changed information about a call.
- **CXAnswerCallAction** - An encapsulation of the act of answering an incoming call.

### Outgoing calls
Request outgoing calls with a call controller, then handle the accepted action through the provider delegate. Fulfill or fail the action according to the service result, and wait for system audio-session activation before starting call audio.
- [Sending End-to-End Encrypted VoIP Calls](https://developer.apple.com/documentation/callkit/sending-end-to-end-encrypted-voip-calls) - Initiate VoIP calls when your server can't determine whether an outgoing notification is a request for a VoIP call due to metadata encryption.
- **CXCallController** - A programmatic interface for interacting with and observing calls.
- **CXTransaction** - An object that contains zero or more action objects for a call controller to perform.
- **CXStartCallAction** - An encapsulation of the act of initiating an outgoing call.

### Call-related actions
Respond to reported actions.
- **CXAction** - An abstract class that declares a programmatic interface for objects that represent a telephony action.
- **CXCallAction** - A programmatic interface for objects that represent a telephony action associated with a call object.
- **CXEndCallAction** - An encapsulation of the act of ending a call.
- **CXPlayDTMFCallAction** - An encapsulation of the act of playing a dual tone multifrequency (DTMF) sequence.
- **CXSetGroupCallAction** - An encapsulation of the act of grouping or ungrouping calls.
- **CXSetHeldCallAction** - An encapsulation of the act of placing a call on hold or removing a call from hold.
- **CXSetMutedCallAction** - An encapsulation of the act of muting or unmuting a call.
- [**CXSetTranslatingCallAction**](https://developer.apple.com/documentation/callkit/cxsettranslatingcallaction) - A call-translation action available on iOS, iPadOS, and Mac Catalyst 26.0+, not every platform or version in the framework header.

### Call information
Get information about calls, and receive notifications when the status of a call changes.
- **CXCall** - A telephony call.
- **CXCallObserver** - A programmatic interface for an object that manages a list of active calls and observes call changes.
- **CXCallObserverDelegate** - A collection of methods the system calls when a call changes state.
- **CXHandle** - A way to reach a call recipient, such as a phone number or email address.

### Caller ID
Use a Call Directory app extension to block calls and provide caller ID information.
- [Identifying and blocking calls](https://developer.apple.com/documentation/callkit/identifying-and-blocking-calls) - Create a Call Directory app extension to identify and block incoming callers by their phone number.
- **CXCallDirectoryProvider** - The principal object for a Call Directory app extension for a host app.
- **CXCallDirectoryExtensionContext** - A programmatic interface for adding identification and blocking entries to a Call Directory app extension.
- **CXCallDirectoryExtensionContextDelegate** - A collection of methods a Call Directory extension context object calls when a request fails.
- **CXCallDirectoryManager** - The programmatic interface to an object that manages a Call Directory app extension.

### Reference
- [CallKit Enumerations](https://developer.apple.com/documentation/callkit/callkit-enumerations)
- [CallKit Constants](https://developer.apple.com/documentation/callkit/callkit-constants)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CallKit)*
