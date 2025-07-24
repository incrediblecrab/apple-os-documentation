# Group Activities

Create app-specific activities your users can share and experience together.

**Platforms:** iOS 15.0+ | iPadOS 15.0+ | Mac Catalyst 15.0+ | macOS 12.0+ | tvOS 15.0+ | visionOS 1.0+

## Overview

With the Group Activities framework, you can provide your app's content in SharePlay experiences, which create a sense of connection and immediacy for your users. For example, a video-streaming app might offer the ability to attend movie-watching parties in which participants watch simultaneously from their personal devices. The app handles the playback on each device, but the Group Activities framework synchronizes that playback and facilitates communication between the devices.

This framework leverages the FaceTime infrastructure to synchronize your app's activities and to invite other participants to join those activities. When your app's UI contains shareable activities, adopt the GroupActivity protocol in the objects you use to represent those activities. When a group activity begins, use the GroupSession object to synchronize your app's behavior with other participating devices.

**Note:** The Group Activities framework uses end-to-end encryption on all session data that the GroupSession object synchronizes between devices. Apple doesn't have the keys to decrypt this data. Your use of the Group Activities framework doesn't provide Apple with visibility into the content your app shares, or information related to playback of media content in your app, such as where in the content a user starts, pauses, or skips a session. Apple servers facilitating Group Activities sessions don't know the identity of your app. Occasionally, Apple may ask a small number of users to help troubleshoot issues, such as by capturing a sysdiagnose or installing a debugging profile, which may incidentally result in Apple collecting some information related to content shared in your app.

## Topics

### Essentials
- **com.apple.developer.group-session** - A Boolean value that indicates whether the app may implement shared group experiences.

### Activity Definition
- [Defining your app's SharePlay activities](https://developer.apple.com/documentation/groupactivities/defining_your_app_s_shareplay_activities) - Configure your app's SharePlay support and define the activities that people can perform from your app.
- [Supporting Coordinated Media Playback](https://developer.apple.com/documentation/groupactivities/supporting_coordinated_media_playback) - Create synchronized media experiences that enable users to watch and listen across devices.
- **GroupActivity** - A type that can advertise your app's activities to other participants.
- **GroupActivityMetadata** - Text and image content that describes an activity to potential participants.
- **GroupActivityActivationResult** - The result of preparing to start a custom activity.
- **GroupActivityTransferRepresentation** - A type that lets you start a group activity from a known context.

### Interface Presentation
- [Presenting SharePlay activities from your app's UI](https://developer.apple.com/documentation/groupactivities/presenting_shareplay_activities_from_your_app_s_ui) - Make it easy for people to start activities from your app's UI, from the system share sheet, or using AirPlay over AirDrop.
- **GroupActivitySharingController** (macOS) - A macOS view controller that displays the system interface for starting an activity, and optionally starts a FaceTime call for that activity.
- **GroupActivitySharingController** (iOS) - An iOS view controller that displays the system interface for starting an activity, and optionally starts a FaceTime call for that activity.

### Session Management
- [Joining and managing a shared activity](https://developer.apple.com/documentation/groupactivities/joining_and_managing_a_shared_activity) - Configure the session when a SharePlay activity starts, and handle events that occur during the lifetime of the activity.
- [Drawing content in a group session](https://developer.apple.com/documentation/groupactivities/drawing_content_in_a_group_session) - Invite your friends to draw on a shared canvas while on a FaceTime call.
- **GroupSession** - A session for an in-progress activity that synchronizes content among participant devices.
- **CustomMessageIdentifiable** - A type that assigns a custom ID string to messages you send to other devices.
- **Participant** - An active participant in a group session.

### Spatial Activities
- [Configure your visionOS app for sharing with people nearby](https://developer.apple.com/documentation/groupactivities/configure_your_visionos_app_for_sharing_with_people_nearby) - Create shared experiences for people wearing Vision Pro in the same room and those on FaceTime.
- [Adding spatial Persona support to an activity](https://developer.apple.com/documentation/groupactivities/adding_spatial_persona_support_to_an_activity) - Update your SharePlay activities to support spatial Personas and the shared context when running in visionOS.
- **SystemCoordinator** - A type you use to coordinate your interface's behavior when an active SharePlay session supports spatial placement of content.
- **ParticipantState** - A structure that tells you whether a participant supports a shared simulation space for the current activity.
- **groupActivityAssociation(_ kind: GroupActivityAssociationKind?) -> some View** - Specifies how a view should be associated with the current SharePlay group activity. (Beta)
- **GroupActivityAssociationInteraction** - An interaction configures a view's association with the current SharePlay group activity. (Beta)
- **GroupActivityAssociationKind** - An association a user-interface element can have with a SharePlay group activity. (Beta)

### Custom Spatial Templates
- [Building a guessing game for visionOS](https://developer.apple.com/documentation/groupactivities/building_a_guessing_game_for_visionos) - Create a team-based guessing game for visionOS using Group Activities.
- **SpatialTemplate** - An interface you use to create custom arrangements of spatial Personas in a scene.
- **SpatialTemplatePreference** - A structure that specifies the preferred arrangement of participant spatial Personas in a shared simulation space.
- **SpatialTemplateSeatElement** - A spatial template element that represents a seat for a participant in the activity.
- **SpatialTemplateElement** - An interface that defines an element in your spatial template.
- **SpatialTemplateElementPosition** - A type that defines the position of an element in a spatial template.
- **SpatialTemplateElementDirection** - The initial direction a participant faces when an activity starts.
- **SpatialTemplateRole** - An interface for defining roles that you assign to the participants of a group activity.

### File and Data Transfer
- [Synchronizing data during a SharePlay activity](https://developer.apple.com/documentation/groupactivities/synchronizing_data_during_a_shareplay_activity) - Send custom messages and data between devices to synchronize content for your activity, and incorporate messages your app receives from other participants.
- **GroupSessionMessenger** - An object that transfers app-specific data between the devices joined in a group session.
- **GroupSessionJournal** - An object that manages file and data transfers between participants joined in a group session.

### System Status
- **GroupStateObserver** - An object that contains information about the system's ability to start SharePlay experiences.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/GroupActivities)*