# LiveCommunicationKit

Coordinate VoIP and cellular conversations with the system, and support eligible default-calling or default-dialer integrations.

**Platforms:** iOS 17.4+ | iPadOS 17.4+ | Mac Catalyst 17.4+ | visionOS 1.1+ | watchOS 10.4+

## Overview

LiveCommunicationKit allows you to offer VoIP conversation functionalities in your app, and to integrate your communication services with other communication apps in the system. With LiveCommunicationKit, your app can:

- Initiate and receive VoIP conversations
- Forward cellular network conversations to the system

Default calling and default dialing are separate capabilities, not automatic consequences of importing the framework. A calling app supplies VoIP services; a dialer presents an interface for initiating cellular conversations. The [`TelephonyConversationManager`](https://developer.apple.com/documentation/livecommunicationkit/telephonyconversationmanager) API starts at iOS/iPadOS/Mac Catalyst 26.0 and requires the Default Dialer App entitlement. Follow the [dialer guide](https://developer.apple.com/documentation/livecommunicationkit/preparing-your-app-to-be-the-default-dialer-app) for eligibility and user-selection requirements, and the [regional distribution guide](../guides/regional-distribution.md) for distribution considerations.

The [VoIP integration guide](https://developer.apple.com/documentation/livecommunicationkit/initiating-voip-conversations-with-livecommunicationkit) describes optional fallback to the system when your VoIP service cannot complete a conversation. Handle errors instead of assuming that a conversation action establishes a connection.

### Manage user privacy

With a person's permission, an installed health research app that uses SensorKit entitlements may collect Speech Metrics data while your LiveCommunicationKit app is in use. To prevent this, set the SRResearchDataGeneration information property list key to NO.

**Important**: When someone starts a conversation in your app that uses LiveCommunicationKit, your app provides the contact information of the recipient to the system. The system may use that information to indicate communication with that person as a suggestion in the Journal app, or in other apps that use the Journaling Suggestions framework.

## Topics

### Essentials
- [Initiating VoIP conversations with LiveCommunicationKit](https://developer.apple.com/documentation/livecommunicationkit/initiating-voip-conversations-with-livecommunicationkit) - Let people initiate and receive VoIP conversations, and configure your app so it can be the default calling app on a person's device.
- [Preparing your app to be the default dialer app](https://developer.apple.com/documentation/livecommunicationkit/preparing-your-app-to-be-the-default-dialer-app) - Let people configure their device to set your app as the default dialer app.
- [LiveCommunicationKit updates](https://developer.apple.com/documentation/updates/livecommunicationkit) - Framework changes, including June 2025's cellular-conversation and translation additions; not an OS 27 introduction list.

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
- **SetTranslatingAction** - An action that starts or stops translation.
- **StartConversationAction** - An action that starts an outgoing conversation and causes the devices of a remote participant to ring.
- **UnmergeConversationAction** - An action that separates two previously merged conversations.

### Participant information
- **Handle** - A way to reach a participant, such as a phone number or email address.

### Conversation history
- **ConversationHistoryManager** - An interface for managing and providing conversation history.

Cellular history access requires both the Default Dialer App entitlement and the person's selection of your app as the default dialer. The documented history starts when the app became the default, not before.

### Cellular network conversations
- [`TelephonyConversationManager`](https://developer.apple.com/documentation/livecommunicationkit/telephonyconversationmanager) - Initiates cellular-network conversation requests and lets the system route them to the appropriate calling app.
- [`CellularService`](https://developer.apple.com/documentation/livecommunicationkit/cellularservice) - A cellular service account used when starting or joining a conversation.
- [`StartCellularConversationAction`](https://developer.apple.com/documentation/livecommunicationkit/startcellularconversationaction) - A request to start a cellular conversation using the default calling app.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/LiveCommunicationKit)*
