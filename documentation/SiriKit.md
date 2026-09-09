# SiriKit

Empower users to interact with their devices through voice, intelligent suggestions, and personalized workflows.

**Platforms:** iOS 10.0+ | iPadOS 10.0+ | Mac Catalyst 13.0+ | macOS 12.0+ | tvOS 14.0+ | visionOS 1.0+ | watchOS 3.2+

## Overview

The **Intents** and **IntentsUI** frameworks support legacy Siri interactions, Shortcuts actions, and widget configuration. Donating completed actions or user activities helps the system predict relevant shortcuts; see [Donating Shortcuts](https://developer.apple.com/documentation/sirikit/donating-shortcuts.md) for the appropriate timing and donation types.

A collection of devices, including a MacBook Air, an iPhone, an Apple Watch, and a HomePod mini. The devices display user interactions that SiriKit enables. On the MacBook Air, the Shortcuts app is open with a collection of shortcuts in the All Shortcuts section. The iPhone displays a Siri Suggestion with the Maps icon. The Apple Watch displays the Siri animation and the words "What can I help you with?"

Use the standard intents that the system provides to empower actions users already ask Siri to do, such as playing music or sending a text message. You can also offer your app's unique capabilities throughout the system by designing custom intents. For more details about defining custom intents, see Adding User Interactivity with Siri Shortcuts and the Shortcuts App.

You can process intents directly in your app, or in an Intents app extension. For guidance on setting up an app extension and sharing information between your app and extension, see Structuring Your Code to Support App Extensions.

To display branding or other customized content in Siri and Maps after you fulfill a user request, create a custom view controller in an **IntentsUI** app extension. See Creating an Intents UI Extension for more details.

**Important:** With a person's permission, an installed health research app that uses SensorKit entitlements may collect Face Metrics data while your SiriKit app is in use. On iOS and iPadOS 17.0+, set the Boolean [`SRResearchDataGeneration`](https://developer.apple.com/documentation/bundleresources/information-property-list/srresearchdatageneration.md) information property list key to `NO` to opt out of contributing SensorKit data. Its default is `YES`.

## Legacy support and modern adoption

The [current SiriKit documentation](https://developer.apple.com/documentation/sirikit.md) says SiriKit, Intents, and IntentsUI continue to support Shortcuts actions, widget configuration, and **most existing Siri interactions** as legacy integrations. It recommends [App Intents](AppIntents.md) for modern support and integration with Apple Intelligence and Siri AI.

That statement is not a formal, blanket deprecation of these frameworks, and it does not say every existing SiriKit intent stops working with the newer Siri. Individual symbols or domains can have their own deprecations; check those separately. Do not invent a framework removal date or discard working legacy paths solely because of OS 27.

For custom intents, share the underlying action code, migrate intent definitions and entity queries, preserve existing shortcut identity, and validate both old and new entry points. See the [App Intents migration recipe](../guides/app-intents-migration.md) and [App Intents Testing](AppIntentsTesting.md). SiriKit Cloud Media is a distinct integration; consult [its reference](SiriKitCloudMedia.md) rather than assuming every domain has an identical migration.

The Siri Watch Face articles below describe legacy interfaces, not watchOS 27 UI availability. For current Smart Stack content, use [WidgetKit](WidgetKit.md) and App Intents, as described in [Apple Watch support](https://developer.apple.com/documentation/sirikit/watch-and-widget-support.md).

## Topics

### Frameworks
Reference the APIs that compose SiriKit.
- [Intents](https://developer.apple.com/documentation/intents.md) - Empower people to customize interactions for your app on their device.
- [IntentsUI](https://developer.apple.com/documentation/intentsui.md) - Customize content in the interface for Siri and Maps.

### Sample code
Browse sample code that walks through specific Intents and IntentsUI workflows.
These are legacy workflow examples, not an OS 27 domain-support matrix; check the individual APIs and their deprecations before adopting one.
- [Adding Shortcuts for Wind Down](https://developer.apple.com/documentation/sirikit/adding-shortcuts-for-wind-down.md) - Reveal your app's shortcuts inside the Health app.
- [Booking Rides with SiriKit](https://developer.apple.com/documentation/sirikit/booking-rides-with-sirikit.md) - Add Intents extensions to your app to handle requests to book rides using Siri and Maps.
- [Handling Payment Requests with SiriKit](https://developer.apple.com/documentation/sirikit/handling-payment-requests-with-sirikit.md) - Add an Intent Extension to your app to handle money transfer requests with Siri.
- [Handling Workout Requests with SiriKit](https://developer.apple.com/documentation/sirikit/handling-workout-requests-with-sirikit.md) - Add an Intent Extension to your app that handles requests to control workouts with Siri.
- [Integrating Your App with Siri Event Suggestions](https://developer.apple.com/documentation/sirikit/integrating-your-app-with-siri-event-suggestions.md) - Donate reservations and provide quick access to event details throughout the system.
- [Managing Audio with SiriKit](https://developer.apple.com/documentation/sirikit/managing-audio-with-sirikit.md) - Control audio playback and handle requests to add media using SiriKit Media Intents.
- [Providing Hands-Free App Control with Intents](https://developer.apple.com/documentation/sirikit/providing-hands-free-app-control-with-intents.md) - Resolve, confirm, and handle intents without an extension.
- [Soup Chef: Accelerating App Interactions with Shortcuts](https://developer.apple.com/documentation/sirikit/soup-chef-accelerating-app-interactions-with-shortcuts.md) - Make it easy for people to use Siri with your app by providing shortcuts to your app's actions.
- [Soup Chef with App Intents: Migrating custom intents](https://developer.apple.com/documentation/sirikit/soup-chef-with-app-intents-migrating-custom-intents.md) - Integrate App Intents to provide your app's actions to Siri and Shortcuts.

### Articles
Browse articles that cover high-level Intents and IntentsUI tasks.
- [Adding User Interactivity with Siri Shortcuts and the Shortcuts App](https://developer.apple.com/documentation/sirikit/adding-user-interactivity-with-siri-shortcuts-and-the-shortcuts-app.md) - Add custom intents and parameters to help users interact more quickly and effectively with Siri and the Shortcuts app.
- [Defining Relevant Shortcuts for the Siri Watch Face](https://developer.apple.com/documentation/sirikit/defining-relevant-shortcuts-for-the-siri-watch-face.md) - Inform Siri when your app's shortcuts may be useful to the user in the legacy watch-face workflow.
- [Deleting Donated Shortcuts](https://developer.apple.com/documentation/sirikit/deleting-donated-shortcuts.md) - Remove your donations from Siri.
- [Dispatching intents to handlers](https://developer.apple.com/documentation/sirikit/dispatching-intents-to-handlers.md) - Provide SiriKit with an intent handler capable of handling a specific intent.
- [Improving Siri Media Interactions and App Selection](https://developer.apple.com/documentation/sirikit/improving-siri-media-interactions-and-app-selection.md) - Fine-tune voice controls and improve Siri Suggestions by sharing app capabilities, customized names, and listening habits with the system.
- [Improving interactions between Siri and your messaging app](https://developer.apple.com/documentation/sirikit/improving-interactions-between-siri-and-your-messaging-app.md) - Donate app-specific content, use Siri's contact suggestions, and adopt the latest platform features to create a more consistent messaging experience.
- [Registering Custom Vocabulary with SiriKit](https://developer.apple.com/documentation/sirikit/registering-custom-vocabulary-with-sirikit.md) - Register your app's custom terminology, and provide sample phrases for how to use your app with Siri.
- [Confirming the Details of an Intent](https://developer.apple.com/documentation/sirikit/confirming-the-details-of-an-intent.md) - Perform final validation of the intent parameters and verify that your services are ready to fulfill the intent.
- [Handling an Intent](https://developer.apple.com/documentation/sirikit/handling-an-intent.md) - Fulfill the intent and provide feedback to SiriKit about what you did.
- [Resolving the Parameters of an Intent](https://developer.apple.com/documentation/sirikit/resolving-the-parameters-of-an-intent.md) - Validate the parameters of an intent and make sure that you have the information you need to continue.
- [Generating a List of Ride Options](https://developer.apple.com/documentation/sirikit/generating-a-list-of-ride-options.md) - Generate ride options for Maps to display to the user.
- [Handling the Ride-Booking Intents](https://developer.apple.com/documentation/sirikit/handling-the-ride-booking-intents.md) - Support the different intent-handling sequences for booking rides with Shortcuts or Maps.
- [Displaying Shortcut Information in a Siri Watch Face Card](https://developer.apple.com/documentation/sirikit/displaying-shortcut-information-in-a-siri-watch-face-card.md) - Customize a legacy Siri Watch Face card with a default template.
- [Donating Reservations](https://developer.apple.com/documentation/sirikit/donating-reservations.md) - Inform Siri of reservations made from your app.
- [Specifying Synonyms for Your App Name](https://developer.apple.com/documentation/sirikit/specifying-synonyms-for-your-app-name.md) - Provide alternative names for your app that are more familiar or easier for users to speak.
- [Intent Phrases](https://developer.apple.com/documentation/sirikit/intent-phrases.md) - The keys that you include in your global vocabulary file to show how users engage your app from Siri.
- [Localizing Your Vocabulary for Chinese Dialects](https://developer.apple.com/documentation/sirikit/localizing-your-vocabulary-for-chinese-dialects.md) - Apply emphasis markers to your pronunciation tips to assist Siri with Chinese dialects.
- [Parameter Vocabularies](https://developer.apple.com/documentation/sirikit/parameter-vocabularies.md) - The keys you include in your global vocabulary file to describe app-specific terms.
- [Offering Actions in the Shortcuts App](https://developer.apple.com/documentation/sirikit/offering-actions-in-the-shortcuts-app.md) - Suggest shortcuts users may want to add to Siri or combine with other actions in their own shortcuts.
- [Creating an Intents App Extension](https://developer.apple.com/documentation/sirikit/creating-an-intents-app-extension.md) - Add and configure an Intents app extension in your Xcode project.
- [Requesting Authorization to Use Siri](https://developer.apple.com/documentation/sirikit/requesting-authorization-to-use-siri.md) - Request permission from the user for Siri and Maps to communicate with your app or Intents app extension.
- [Structuring Your Code to Support App Extensions](https://developer.apple.com/documentation/sirikit/structuring-your-code-to-support-app-extensions.md) - Move your back-end services to a private framework so your app and app extensions can use them.
- [Providing Live Status Updates](https://developer.apple.com/documentation/sirikit/providing-live-status-updates.md) - Provide regular updates to Maps about the status of a booked ride.
- [Donating Shortcuts](https://developer.apple.com/documentation/sirikit/donating-shortcuts.md) - Tell Siri about shortcuts to actions that the user performed in your app.
- [Configuring the View Controller for Your Custom Interface](https://developer.apple.com/documentation/sirikit/configuring-the-view-controller-for-your-custom-interface.md) - Configure your view controller to replace or augment the default interface in Siri or Maps.
- [Configuring Your Intents UI App Extension Target](https://developer.apple.com/documentation/sirikit/configuring-your-intents-ui-app-extension-target.md) - Configure your Xcode project to include an Intents UI app extension that you use to customize the Siri and Maps interfaces.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SiriKit)*
