# Wallet Passes

Create, distribute, and update passes for the Wallet app.

**Platforms:** iOS 6.0+ | iPadOS 6.0+ | watchOS 2.0+

## Overview

Passes are digital representations of information that might previously be on paper or plastic. They let users take action in the physical world, such as boarding a flight, attending an event, or claiming a coat-check item.

To enable a user to install your pass, you need to:

1. Create the source for a pass.
2. Build a distributable pass from the source.
3. Distribute a pass.

For information on creating and building a pass, see Creating the Source for a Pass and Building a Pass. For information on distributing a pass, see Distributing and updating a pass.

## Topics

### Essentials
- [Creating the Source for a Pass](https://developer.apple.com/documentation/walletpasses/creating-the-source-for-a-pass) - Create the directory structure and add source files and images to define a pass.
- [Building a Pass](https://developer.apple.com/documentation/walletpasses/building-a-pass) - Build a distributable pass.
- [Distributing and updating a pass](https://developer.apple.com/documentation/walletpasses/distributing-and-updating-a-pass) - Distribute a pass to your users or update an existing pass.
- **Pass** - An object that represents a pass.

### Multievent Passes
- **UpcomingPassInformationEntry** - An object that represents the ordered list of all upcoming pass information entries.
- **UpcomingPassInformationEntryType** - An object that represents a upcoming pass information entry for an specific upcoming event.

### Pass Updates
- [Adding a Web Service to Update Passes](https://developer.apple.com/documentation/walletpasses/adding-a-web-service-to-update-passes) - Implement a web server to register, update, and unregister a pass on a device.
- [Register a Pass for Update Notifications](https://developer.apple.com/documentation/walletpasses/register-a-pass-for-update-notifications) - Set up change notifications for a pass on a device.
- [Get the List of Updatable Passes](https://developer.apple.com/documentation/walletpasses/get-the-list-of-updatable-passes) - Send the serial numbers for updated passes to a device.
- [Send an Updated Pass](https://developer.apple.com/documentation/walletpasses/send-an-updated-pass) - Create and sign an updated pass, and send it to the device.
- [Unregister a Pass for Update Notifications](https://developer.apple.com/documentation/walletpasses/unregister-a-pass-for-update-notifications) - Stop sending update notifications for a pass on a device.
- [Log a Message](https://developer.apple.com/documentation/walletpasses/log-a-message) - Record a message on your server.
- **PushToken** - An object that contains the push notification token for a registered pass on a device.
- **SerialNumbers** - An object that contains serial numbers for the updatable passes on a device.
- **LogEntries** - An object that contains an array of messages.

### Personalized Passes
- [Return a Personalized Pass](https://developer.apple.com/documentation/walletpasses/return-a-personalized-pass) - Create and sign a personalized pass, and send it to a device.
- **PersonalizationDictionary** - An object that contains the information you use to personalize a pass.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/WalletPasses)*