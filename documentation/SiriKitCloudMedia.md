# SiriKit Cloud Media

Stream music directly to HomePod speakers from your media service.

**Platforms:** SiriKit Cloud Media 1.0.2+

## Overview

When the user asks an authorized HomePod speaker to play some media, the media device can contact your SiriKitCloudMedia service directly, rather than send requests through an intermediary iOS device.

Download the SiriKit Cloud Media OpenAPI Specification. For details about applying for the SiriKit Media Intents on HomePod program, see the HomePod section of Siri for Developers.

### Configure the User's HomePod

Authorize HomePod speakers to contact your media service by adopting **Media Setup** in your iOS app and vending tokens from an OAuth service. After the user enables your service for devices in their home, they can manage access in the Home app.

Provide a HomePod speaker with details about sending requests to your service by implementing the configuration endpoint. Include paths and required headers for the endpoints you support. See Configure Your Service Endpoints for more information.

**Note:** During a single session, some requests may come from a different HomePod speaker or an Apple TV within the user's home. Respond to these requests the same as you do when a single device sends all of them. Use the **Session** object to maintain continuity.

### Respond to a Siri Intent with a Media Playback Queue

Implement the Process a Play Media Intent endpoint to receive the user's request, resolve the media they want to play, and handle the intent. Respond with a **UserActivity**, which the client uses to request a Queue of media Content from the Get a Media Queue endpoint.

Manage how frequently the user can skip content in a queue, and what playback controls are available with each piece of content, with the **PlayMediaControl** you include in each queue. Monitor user interactions and playback progress with periodic updates on the Report Playback Progress and Activity endpoint. You may optionally respond to Report Playback Progress and Activity requests with a queue segment to replace or modify the current playback queue.

### Adapt to the User's Tastes

Empower the user to customize their library and playlists with the Process an Add Media Intent endpoint. They might ask Siri to add a certain artist's latest album to their library, or to add the currently playing song to their Karaoke Practice playlist.

You can also tune algorithmic playlists by incorporating the preferences users share as Process an Update Media Affinity Intent intents. For example, if the user says "I like rock-and-roll," you might include more songs from that genre the next time they ask to play some music. Or if they say "I don't like this song," you might exclude the currently playing song from future recommendations.

## Topics

### Device Configuration
- [Configure Your Service Endpoints](https://developer.apple.com/documentation/sirikitcloudmedia/configure_your_service_endpoints) - Provide configuration details for your media server's endpoints to a HomePod speaker or an Apple TV.
- **ExtensionConfigTag** - A unique identifier for a specific media service configuration.
- **ExtensionConfig** - Instructions for accessing your media service's endpoints.
- **PlayMediaControlActivity** - Options for reporting playback progress.

### Media Play Queues
- [Process a Play Media Intent](https://developer.apple.com/documentation/sirikitcloudmedia/process_a_play_media_intent) - Interpret the user's request to play a media item, and provide instructions to access a corresponding playback queue.
- [Get a Media Queue](https://developer.apple.com/documentation/sirikitcloudmedia/get_a_media_queue) - Provide a playback queue from a successfully processed play media intent.

### Content Protection
- [Retrieve an Asset's Content Protection Key](https://developer.apple.com/documentation/sirikitcloudmedia/retrieve_an_asset_s_content_protection_key) - Provide the content key for a specific protected asset.
- **ContentProtectionKeyRequest** - A request for an item's content protection key.
- **ContentProtectionKeyResponse** - A response to a request for an item's content protection key.
- **ContentProtectionKeySystem** - The content protection key systems that SiriKit Cloud Media supports.

### Playback Events
- **QueueActivityReportEvent** - An event that occurs during content playback.
- [Report Playback Progress and Activity](https://developer.apple.com/documentation/sirikitcloudmedia/report_playback_progress_and_activity) - Monitor progress through the playback queue.
- **UpdateActivityRequest** - A report of the client's current playback state and recent user interaction, and an opportunity for your service to modify the client's playback queue.
- **UpdateActivityResponse** - Updates to the client's queue and user activity in response to a report of playback progress.
- [Process an Update Media Affinity Intent](https://developer.apple.com/documentation/sirikitcloudmedia/process_an_update_media_affinity_intent) - Record the user's preference for a specific media item or a broader category of media.

### Playback Failure
- [Recover from Content Playback Failure](https://developer.apple.com/documentation/sirikitcloudmedia/recover_from_content_playback_failure) - Provide a recovery queue that allows the client to resume playback after an error.
- **ContentFailure** - An object that describes why the client can't play a specific piece of content.
- **ContentPlaybackFailureRequest** - A request the client sends to recover from failed content playback.
- **ContentPlaybackFailureResponse** - A response that allows the client to recover from failed content playback.

### Library and Playlists
- [Process an Add Media Intent](https://developer.apple.com/documentation/sirikitcloudmedia/process_an_add_media_intent) - Add media items to the user's library or to a playlist.

### Media Items
- **MediaItem** - A particular piece of media that an intent references, such as a song, podcast episode, or playlist.
- **MediaReference** - A way of identifying the current media item rather than with metadata.
- **MediaSearch** - A description of the media items the user wants to play, add to a playlist, or express a preference for.
- **MediaItemType** - Types of media items or media searches.

### Requests
- **Invocation** - Properties that clients include in requests to all intent endpoints.
- **Session** - Information the client provides about a sequence of requests and responses to process an intent.
- **Constraints** - Client-originated limitations on how to process a request, such as including explicit content and how much content the client device can receive in a response.
- **PlayerContext** - Information about the current playback content.
- **InvocationResponse** - Properties to include in responses from all intent endpoints.

### Intents
Common objects for processing intents.
- **Intent** - A user request for your service to fulfill.
- **IntentResponse** - Your service's response to an intent.
- **UserActivity** - The context for playing a media queue.
- **IntentResolutionResult** - An object that matches a parameter of an intent, or information about why your service can't determine a value for the parameter.
- **BooleanResolutionResult** - A Boolean value that matches an intent parameter, or information about why your service can't determine the value.

### Exceptions
- **ProtocolExceptionInvocationResponse** - A response object that indicates when the service fails to process the client's request.
- **ProtocolException** - An exception response from a media service.
- **ProtocolExceptionReason** - Categories of exceptions a service can encounter.

### Errors
- **UnderlyingError** - An object that describes a system framework error.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SiriKitCloudMedia)*