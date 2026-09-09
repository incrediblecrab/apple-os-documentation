# Watch Connectivity

Implement two-way communication between an iOS app and its paired watchOS app.

**Platforms:** iOS 9.0+ | iPadOS 9.0+ | Mac Catalyst 13.0+ | visionOS 1.0+ | watchOS 2.0+

These are SDK listings, not pairing support on every listed device. `WCSession.isSupported()` returns true on Apple Watch and iPhones that support Apple Watch pairing; Apple's discussion specifies false for other devices.

## Overview

Use this framework to transfer data between your iOS app and the WatchKit extension of a paired watchOS app. You can pass small amounts of data or entire files. You also use this framework to trigger an update to your watchOS app's complication.

Configure a delegate and activate the session before transferring data. Immediate message APIs also require a reachable counterpart; activation alone does not guarantee reachability. Background transfers are queued and opportunistic, not instant or guaranteed to finish at a particular time. Handle transfer errors and changes in pairing or app installation.

Complication-specific transfers require an active session and must be tested on paired devices; `transferCurrentComplicationUserInfo(_:)` is not supported in Simulator.

## Topics

### Essentials
- **WCSession** - The object that initiates communication between a WatchKit extension and its companion iOS app.
- **WCSessionDelegate** - A delegate protocol that defines methods for receiving messages sent by a WCSession object.

### Data Objects
- **WCSessionFile** - Information about a file currently being transferred between an iOS app and WatchKit extension.
- **WCSessionFileTransfer** - Information about in-progress file transfers.
- **WCSessionUserInfoTransfer** - Information about in-progress data transfers.

### Sample Code
- [Transferring data with Watch Connectivity](https://developer.apple.com/documentation/watchconnectivity/transferring-data-with-watch-connectivity) - Transfer data between a watchOS app and its companion iOS app.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/WatchConnectivity)*
