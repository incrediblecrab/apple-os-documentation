# Messages

Create app extensions that allow users to send text, stickers, media files, and interactive messages.

**Platforms:** iOS 10.0+ | iPadOS 10.0+ | Mac Catalyst 14.0+

## Overview

You can use the Messages framework to create sticker packs and iMessage apps. You can create sticker packs and iMessage apps as either standalone apps or as app extensions within a containing iOS app. For more information on creating and working with app extensions, see App extensions.

iMessage apps and stickers help people interact and communicate in the context of a Messages conversation. For design guidance, see Human Interface Guidelines > iMessage apps and stickers.

### iMessage apps

iMessage apps leverage the full framework to interact with the Messages app.

**Note:** To avoid a crash, an iMessage app linked on or after iOS 10 must include usage description keys for the device features it needs to access in its Info.plist file. Specifically, it must include **NSCameraUsageDescription** to access the device's camera, and it must include **NSMicrophoneUsageDescription** to access the device's microphones.

Use iMessage apps to:

- Present a custom user interface inside the Messages app; see **MSMessagesAppViewController**.
- Create a custom or dynamic sticker browser; see **MSStickerBrowserViewController**.
- Insert text, stickers, or media files into the Messages app's input field; see **MSConversation**.
- Create interactive messages that carry app-specific data; see **MSMessage**.
- Update interactive messages (for example, to create games or collaborative apps); see **MSSession**.

For more information on submitting iMessage Apps to the App Store, see Preparing Your iMessage App for Submission.

In iOS 17, Messages allows you to interactively resize iMessage apps with a vertical pan gesture. Messages handles any conflicts between resize gestures and your custom gestures. If your app uses manual touch handling such as `touchesBegan(_:with:)`, `touchesMoved(_:with:)`, and `touchesEnded(_:with:)`, you can do either of the following:

- Change your manual touch handling code to use a gesture recognizer instead.
- Use your **UIView** to override `gestureRecognizerShouldBegin(_:)` and return NO when your iMessage app doesn't own the gesture.

### Become the default messaging app

In iOS and iPadOS 18.2 and later, a person may select an app other than the Messages app to send instant messages. If you wish to make your app the default messages app, see Preparing your app to be the default messaging app.

## Topics

### Default messaging app
- [Preparing your app to be the default messaging app](https://developer.apple.com/documentation/messages/preparing_your_app_to_be_the_default_messaging_app) - Configure your messaging app so people can set it as the default on their device.

### Custom sticker packs
- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](https://developer.apple.com/documentation/messages/adding_sticker_packs_and_imessage_apps_to_the_system_stickers_app_messages_camera_and_facetime) - Enable your Sticker pack or iMessage app in the media context.
- [Adding your sticker packs to Messages](https://developer.apple.com/documentation/messages/adding_your_sticker_packs_to_messages) - Drag and drop your sticker pack into the Stickers asset catalog to let people access your stickers from Messages.
- **MSStickerBrowserViewController** - A view controller that provides dynamic content to the standard sticker browser.
- **MSStickerBrowserView** - A browser view that displays a dynamically generated list of stickers.
- **MSStickerView** - A view for displaying a sticker.
- **MSStickerSize** - The size of the stickers in the browser view.

### Custom iMessage app interface
- [IceCreamBuilder: Building an iMessage Extension](https://developer.apple.com/documentation/messages/icecreambuilder_building_an_imessage_extension) - Allow users to collaborate on the design of ice cream sundae stickers.
- [Creating a Sticker App with a Custom Layout](https://developer.apple.com/documentation/messages/creating_a_sticker_app_with_a_custom_layout) - Expand on the Messages sticker app template to create an app with a customized user interface.
- **MSMessagesAppViewController** - The principal view controller for iMessage apps.
- **MSMessagesAppTranscriptPresentation** - A protocol that provides support for displaying live messages in the transcript of the Messages app.
- **MSMessagesAppPresentationStyle** - Presentation styles that describe your iMessage app's appearance.

### Message content
- **MSConversation** - An object that represents a conversation in the Messages app.
- **MSSticker** - A sticker that can be sent as a new message or attached to an existing balloon in the Messages app's transcript.

### Interactive messages
- **MSMessage** - A custom message object.
- **MSSession** - A session object used to create and update messages.
- **MSMessageLayout** - An abstract base class that defines the appearance of MSMessage objects in the conversation transcript.
- **MSMessageTemplateLayout** - A template-based layout for custom messages.
- **MSMessageLiveLayout** - A layout that provides a custom, interactive view inside the transcript.

### Critical messages
- [Sending SMS messages from an app](https://developer.apple.com/documentation/messages/sending_sms_messages_from_an_app) - Send critical messages from inside your app using the Critical Messaging API.
- **MSCriticalSMSMessenger** - The user interface for the Critical Messaging API.
- **MSRecipient** - A structure that describes the recipient of a critical message.
- **MSCriticalMessage** - A simple struct to encapsulate the message string.
- **MSCriticalMessagingAuthorizationStatus** - Values that describe the authorization status for the Critical Messaging API.

### Errors
- **MSStickersErrorDomain** - The error domain for stickers.
- **MSMessagesErrorDomain** - The error domain for iMessage apps.
- **MSMessageErrorCode** - The error codes that the Messages framework generates.
- **MSCriticalMessagingError** - Values that describe errors the Critical Messaging API returns.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Messages)*