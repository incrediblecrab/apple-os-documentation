# LiveCommunicationKit

Initiate and handle VoIP conversations, coordinate them with other communication apps and the system, and get ready to be a default calling or dialer app.

**Platforms:** iOS 17.4+ | iPadOS 17.4+ | Mac Catalyst 17.4+ | visionOS 1.1+ | watchOS 10.4+

## Overview

LiveCommunicationKit allows you to offer VoIP conversation functionalities in your app, and to integrate your communication services with other communication apps in the system. With LiveCommunicationKit, your app can:

- Initiate and receive VoIP conversations
- Forward cellular network conversations to the system

Using LiveCommunicationKit in your app allows people to configure their device to use your app as the default dialer or calling app.

### Manage user privacy

With a person's permission, an installed health research app that uses SensorKit entitlements may collect Speech Metrics data while your LiveCommunicationKit app is in use. To prevent this, set the SRResearchDataGeneration information property list key to NO.

**Important**: When someone starts a conversation in your app that uses LiveCommunicationKit, your app provides the contact information of the recipient to the system. The system may use that information to indicate communication with that person as a suggestion in the Journal app, or in other apps that use the Journaling Suggestions framework.

## Topics

### Essentials
- [Initiating VoIP conversations with LiveCommunicationKit](https://developer.apple.com/documentation/livecommunicationkit/initiating_voip_conversations_with_livecommunicationkit) - Let people initiate and receive VoIP conversations, and configure your app so it can be the default calling app on a person's device.
- [Preparing your app to be the default dialer app](https://developer.apple.com/documentation/livecommunicationkit/preparing_your_app_to_be_the_default_dialer_app) - Let people configure their device to set your app as the default dialer app.
- [LiveCommunicationKit updates](https://developer.apple.com/documentation/livecommunicationkit/livecommunicationkit_updates) - Learn about important changes to LiveCommunicationKit.

### VoIP conversation management
- **ConversationManager** - An interface for managing and observing VoIP conversations.
- **ConversationManagerDelegate** - Methods for managing conversations and receiving VoIP conversation updates.
- **Conversation** - A type that describes a video or audio conversation.

### VoIP conversation actions
- **ConversationAction** - A type that represents a VoIP action for a conversation.
- **EndConversationAction** - An action that removes the local participant from a conversation and stops all audio and video streams.
- **JoinConversationAction** - An action for joining an incoming conversation.
- **MergeConversationAction** - An action that merges two separate conversations into one conversation.
- **MuteConversationAction** - An action that mutes or unmutes a conversation.
- **PauseConversationAction** - An action that stops or restarts all audio and video streams for a conversation.
- **PlayToneAction** - An action that plays sequence of tones to indicate that a participant of a conversation interacted with the keypad.
- **SetTranslatingAction** - An action that starts or stops translation. Beta
- **StartConversationAction** - An action that starts an outgoing conversation and causes the devices of a remote participant to ring.
- **UnmergeConversationAction** - An action that separates two previosuly merged conversations.

### Participant information
- **Handle** - A way to reach a participant, such as a phone number or email address.

### Conversation history
- **ConversationHistoryManager** - An interface for managing and providing conversation history.

### Classes
- **TelephonyConversationManager**

### Structures
- **CellularService** - Struct representing an account which can be used to dial a call
- **StartCellularConversationAction** - Struct representing a request to dial a conversation using the default calling application

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/LiveCommunicationKit)*