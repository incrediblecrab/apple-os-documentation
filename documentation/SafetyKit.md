# SafetyKit

Detect and respond to car crash events in your app.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 16.1+ | macOS 13.0+ | watchOS 10.1+

## Overview

SafetyKit provides Crash Detection, a feature that sends a crash event to an authorized app if a person is in a severe vehicular crash as detected by their iPhone 14, iPhone 14 Pro, Apple Watch Series 8, Apple Watch SE (2nd generation), or Apple Watch Ultra. These devices provide a feature called Emergency SOS - Call After Severe Crash. If enabled, Emergency SOS dials a municipal emergency service such as 911 in the event of a vehicular crash. After Emergency SOS places its call, Crash Detection can assist someone by initiating a call to a contact designated by the app, such as a roadside assistance provider.

SafetyKit supports three crash scenarios. In each scenario, Apple is the first party, and your app is the third party.

The first scenario has first-party Emergency SOS turned off and third-party sharing turned on. When the device detects a crash, a critical alert occurs and the third party receives the crash information.

In the second scenario, first-party Emergency SOS and third-party sharing are turned on. When the device detects a crash, the first-party Emergency SOS runs automatically. After the first party completes its procedures, a critical alert occurs and the third party receives the crash information.

In the third scenario, first-party Emergency SOS is turned on and there's no third-party sharing. When the device detects a crash, the first-party Emergency SOS runs automatically.

> **Important:** Crash Detection requires the com.apple.developer.severe-vehicular-crash-event entitlement. To apply for this entitlement, see Request Access to the Vehicular Crash Event Entitlement.

To support Crash Detection, use SACrashDetectionManager to determine whether it's available and if so, ask permission to allow your app to receive crash events. Then set delegate to the object that receives the events. Only one app on the device can receive Crash Detection events.

If your app receives a Crash Detection event, use SAEmergencyResponseManager to provide assistance.

## Topics

### Detecting a crash
- **SACrashDetectionManager** - Provides registration and management of Crash Detection events.
- **SAAuthorizationStatus** - An enumeration that represents the current Crash Detection event authorization state.
- **SACrashDetectionEvent** - Describes the information about a vehicular crash.
- **SACrashDetectionDelegate** - The protocol that an object adopts to receive Crash Detection events and changes to the authorization status.

### Responding to a crash
- **SAEmergencyResponseManager** - Provides actions in response to a Crash Detection event.
- **SAEmergencyResponseDelegate** - The interface for receiving updates about a requested emergency response action.
- **Response** - An enumeration that defines possible emergency responses to a Crash Detection event.

### Handling errors
- **SAErrorDomain** - The domain for error objects that SafetyKit produces.
- **Code** - Codes for identifying errors in SafetyKit.
- **SAError** - An error reported by SafetyKit.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SafetyKit)*