# Watch Connectivity

Implement two-way communication between an iOS app and its paired watchOS app.

**Platforms:** iOS 9.0+ | iPadOS 9.0+ | Mac Catalyst 13.0+ | visionOS 1.0+ | watchOS 2.0+

## Overview

Use this framework to transfer data between your iOS app and the WatchKit extension of a paired watchOS app. You can pass small amounts of data or entire files. You also use this framework to trigger an update to your watchOS app's complication.

After initiating a transfer from your app, the system assumes responsibility for the transmission of any data. Most transfers happen in the background when the receiving app is inactive. When the app wakes up, it is notified of any data that arrived while it was inactive. Live communication is also possible when both apps are active.

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