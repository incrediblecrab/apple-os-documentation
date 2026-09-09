# SafetyKit

Detect and respond to car crash events in your app.

**SDK platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 16.1+ | macOS 13.0+ | watchOS 10.1+. Runtime support requires an availability check.

## Overview

SafetyKit delivers severe vehicular Crash Detection events to an authorized app on supported hardware. Apple's introductory examples include iPhone 14 and 14 Pro, Apple Watch Series 8, Apple Watch SE (2nd generation), and Apple Watch Ultra; this is not a current exhaustive device list. Emergency SOS can call the local emergency service, such as 911, when enabled. Third-party assistance, such as contacting a roadside assistance provider, is a separate response and does not replace that emergency workflow.

SafetyKit supports three crash scenarios. In each scenario, Apple is the first party, and your app is the third party.

The first scenario has first-party Emergency SOS turned off and third-party sharing turned on. When the device detects a crash, a critical alert occurs and the third party receives the crash information.

In the second scenario, first-party Emergency SOS and third-party sharing are turned on. When the device detects a crash, the first-party Emergency SOS runs automatically. After the first party completes its procedures, a critical alert occurs and the third party receives the crash information.

In the third scenario, first-party Emergency SOS is turned on and there's no third-party sharing. When the device detects a crash, the first-party Emergency SOS runs automatically.

> **Important:** Crash Detection requires the Boolean [`com.apple.developer.severe-vehicular-crash-event`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.severe-vehicular-crash-event) entitlement. Its reference links to Apple's access-request process.

To support Crash Detection, use SACrashDetectionManager to determine whether it's available and if so, ask permission to allow your app to receive crash events. Then set delegate to the object that receives the events. Only one app on the device can receive Crash Detection events.

If your app receives a Crash Detection event, use SAEmergencyResponseManager to provide assistance.

### Availability, denied access, and revocation

Use [`SACrashDetectionManager.isAvailable`](https://developer.apple.com/documentation/safetykit/sacrashdetectionmanager/isavailable) and its current `authorizationStatus`, not the SDK platform list or the historical hardware examples above, to decide whether the feature can be offered.

The severe-vehicular-crash entitlement does not grant the person's authorization. Only one app can receive these events; handle refusal and later authorization changes without continuing to claim active monitoring. Install the delegate promptly at app launch, including when the system launches the app to deliver an event.

Keep request and response failures visible to the app's state management. Do not present third-party assistance as a replacement for Emergency SOS or assume an event notification guarantees that an assistance call completed.

## Topics

### Detecting a crash
- **SACrashDetectionManager** - Provides registration and management of Crash Detection events.
- **SAAuthorizationStatus** - An enumeration that represents the current Crash Detection event authorization state.
- **SACrashDetectionEvent** - Describes the information about a vehicular crash.
- **SACrashDetectionDelegate** - The protocol that an object adopts to receive Crash Detection events and changes to the authorization status.

### Responding to a crash
- **SAEmergencyResponseManager** - Provides actions in response to a Crash Detection event.
- **SAEmergencyResponseDelegate** - The interface for receiving updates about a requested emergency response action.
- **SACrashDetectionEvent.Response** - An enumeration that defines possible emergency responses to a Crash Detection event.

### Handling errors
- **SAErrorDomain** - The domain for error objects that SafetyKit produces.
- **SAError.Code** - Codes for identifying errors in SafetyKit.
- **SAError** - An error reported by SafetyKit.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SafetyKit)*

*Changed-content sources, reviewed September 8, 2026: [SACrashDetectionManager](https://developer.apple.com/documentation/safetykit/sacrashdetectionmanager.md) and [SACrashDetectionDelegate](https://developer.apple.com/documentation/safetykit/sacrashdetectiondelegate.md).*
