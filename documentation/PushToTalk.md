# Push to Talk

Display the system user interface for your app's Push to Talk services.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 16.0+

## Overview

The Push to Talk framework is a power-efficient, user-friendly, and privacy-focused API. It gives your apps the ability to provide user interface controls that allow your users to transmit audio from anywhere. It supplies an ephemeral Apple Push Notification service token so the system can wake your app in the background to handle incoming audio while a session is ongoing.

**Note:** Push to Talk services aren't available to compatible iPad and iPhone apps running in visionOS.

## Topics

### Essentials

- [Creating a Push to Talk app](https://developer.apple.com/documentation/pushtotalk/creating_a_push_to_talk_app) - Build a walkie-talkie style app with system user interface controls.
- **PTChannelManager** - An object that represents a push-to-talk channel manager.

### Channel management

- **PTChannelManagerDelegate** - A type that represents your life cycle of a channel manager.
- **PTTransmissionMode** - Identifies the type of audio transmission modes.
- **PTServiceStatus** - Identifies the type that indicates the status of the service.
- **PTChannelJoinReason** - Identifies the type that indicates the join reason.
- **PTChannelLeaveReason** - Identifies the type that indicates the leave reason.
- **PTChannelTransmitRequestSource** - Identifies the type that indicates the transmission request source.

### Channel restoration

- **PTChannelDescriptor** - An object that describes a channel.
- **PTChannelRestorationDelegate** - A type that represents the channel restoration behavior.

### Channel participants

- **PTParticipant** - An object that represents a participant.

### Push notification results

- **PTPushResult** - An object that represents a push result.

### Push to Talk errors

- **PTChannelError** - A structure that represents a channel error.
  - **Code** - Error codes for channel operations.
- **PTInstantiationError** - A structure that represents an instantiation error.
  - **Code** - Error codes for instantiation operations.
- **PTChannelErrorDomain** - A string representation of the channel error domain.
- **PTInstantiationErrorDomain** - A string representation of the instantiation error domain.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/PushToTalk)*