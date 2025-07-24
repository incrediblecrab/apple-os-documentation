# SiriKit

Empower users to interact with their devices through voice, intelligent suggestions, and personalized workflows.

**Platforms:** iOS 10.0+ | iPadOS 10.0+ | Mac Catalyst 13.0+ | macOS 12.0+ | tvOS 14.0+ | visionOS 1.0+ | watchOS 3.2+

## Overview

The **Intents** and **IntentsUI** frameworks drive interactions that start with "Hey Siri…", Shortcuts actions, and widget configuration. The system also incorporates intents and user activities your app donates into contextual suggestions in Maps, Calendar, Watch complications, widgets, and search results.

A collection of devices, including a MacBook Air, an iPhone, an Apple Watch, and a HomePod mini. The devices display user interactions that SiriKit enables. On the MacBook Air, the Shortcuts app is open with a collection of shortcuts in the All Shortcuts section. The iPhone displays a Siri Suggestion with the Maps icon. The Apple Watch displays the Siri animation and the words "What can I help you with?"

Use the standard intents that the system provides to empower actions users already ask Siri to do, such as playing music or sending a text message. You can also offer your app's unique capabilities throughout the system by designing custom intents. For more details about defining custom intents, see Adding User Interactivity with Siri Shortcuts and the Shortcuts App.

You can process intents directly in your app, or in an Intents app extension. For guidance on setting up an app extension and sharing information between your app and extension, see Structuring Your Code to Support App Extensions.

To display branding or other customized content in Siri and Maps after you fulfill a user request, create a custom view controller in an **IntentsUI** app extension. See Creating an Intents UI Extension for more details.

**Important:** With a person's permission, an installed health research app that uses SensorKit entitlements may collect Face Metrics data while your SiriKit app is in use. To prevent SensorKit from collecting Face Metrics data while your app is in use, you can set the **SRResearchDataGeneration** information property list key to NO.

## Topics

### Frameworks
Reference the API that compose SiriKit
- **Intents** - Empower people to customize interactions for your app on their device.
- **IntentsUI** - Customize content in the interface for Siri and Maps.

### Sample code
Browse sample code that walks through specific Intents and IntentsUI workflows.
- [Adding Shortcuts for Wind Down](https://developer.apple.com/documentation/sirikit/adding_shortcuts_for_wind_down) - Reveal your app's shortcuts inside the Health app.
- [Booking Rides with SiriKit](https://developer.apple.com/documentation/sirikit/booking_rides_with_sirikit) - Add Intents extensions to your app to handle requests to book rides using Siri and Maps.
- [Handling Payment Requests with SiriKit](https://developer.apple.com/documentation/sirikit/handling_payment_requests_with_sirikit) - Add an Intent Extension to your app to handle money transfer requests with Siri.
- [Handling Workout Requests with SiriKit](https://developer.apple.com/documentation/sirikit/handling_workout_requests_with_sirikit) - Add an Intent Extension to your app that handles requests to control workouts with Siri.
- [Integrating Your App with Siri Event Suggestions](https://developer.apple.com/documentation/sirikit/integrating_your_app_with_siri_event_suggestions) - Donate reservations and provide quick access to event details throughout the system.
- [Managing Audio with SiriKit](https://developer.apple.com/documentation/sirikit/managing_audio_with_sirikit) - Control audio playback and handle requests to add media using SiriKit Media Intents.
- [Providing Hands-Free App Control with Intents](https://developer.apple.com/documentation/sirikit/providing_hands-free_app_control_with_intents) - Resolve, confirm, and handle intents without an extension.
- [Soup Chef: Accelerating App Interactions with Shortcuts](https://developer.apple.com/documentation/sirikit/soup_chef_accelerating_app_interactions_with_shortcuts) - Make it easy for people to use Siri with your app by providing shortcuts to your app's actions.
- [Soup Chef with App Intents: Migrating custom intents](https://developer.apple.com/documentation/sirikit/soup_chef_with_app_intents_migrating_custom_intents) - Integrating App Intents to provide your appʼs actions to Siri and Shortcuts.

### Articles
Browse articles that cover high-level Intents and IntentsUI tasks.
- [Adding User Interactivity with Siri Shortcuts and the Shortcuts App](https://developer.apple.com/documentation/sirikit/adding_user_interactivity_with_siri_shortcuts_and_the_shortcuts_app) - Add custom intents and parameters to help users interact more quickly and effectively with Siri and the Shortcuts app.
- [Defining Relevant Shortcuts for the Siri Watch Face](https://developer.apple.com/documentation/sirikit/defining_relevant_shortcuts_for_the_siri_watch_face) - Inform Siri when your app's shortcuts may be useful to the user.
- [Deleting Donated Shortcuts](https://developer.apple.com/documentation/sirikit/deleting_donated_shortcuts) - Remove your donations from Siri.
- [Dispatching intents to handlers](https://developer.apple.com/documentation/sirikit/dispatching_intents_to_handlers) - Provide SiriKit with an intent handler capable of handling a specific intent.
- [Improving Siri Media Interactions and App Selection](https://developer.apple.com/documentation/sirikit/improving_siri_media_interactions_and_app_selection) - Fine-tune voice controls and improve Siri Suggestions by sharing app capabilities, customized names, and listening habits with the system.
- [Improving interactions between Siri and your messaging app](https://developer.apple.com/documentation/sirikit/improving_interactions_between_siri_and_your_messaging_app) - Donate app-specific content, use Siri's contact suggestions, and adopt the latest platform features to create a more consistent messaging experience.
- [Registering Custom Vocabulary with SiriKit](https://developer.apple.com/documentation/sirikit/registering_custom_vocabulary_with_sirikit) - Register your app's custom terminology, and provide sample phrases for how to use your app with Siri.
- [Confirming the Details of an Intent](https://developer.apple.com/documentation/sirikit/confirming_the_details_of_an_intent) - Perform final validation of the intent parameters and verify that your services are ready to fulfill the intent.
- [Handling an Intent](https://developer.apple.com/documentation/sirikit/handling_an_intent) - Fulfill the intent and provide feedback to SiriKit about what you did.
- [Resolving the Parameters of an Intent](https://developer.apple.com/documentation/sirikit/resolving_the_parameters_of_an_intent) - Validate the parameters of an intent and make sure that you have the information you need to continue.
- [Generating a List of Ride Options](https://developer.apple.com/documentation/sirikit/generating_a_list_of_ride_options) - Generate ride options for Maps to display to the user.
- [Handling the Ride-Booking Intents](https://developer.apple.com/documentation/sirikit/handling_the_ride-booking_intents) - Support the different intent-handling sequences for booking rides with Shortcuts or Maps.
- [Displaying Shortcut Information in a Siri Watch Face Card](https://developer.apple.com/documentation/sirikit/displaying_shortcut_information_in_a_siri_watch_face_card) - Display and customize watch-specific shortcut information with a default card template.
- [Donating Reservations](https://developer.apple.com/documentation/sirikit/donating_reservations) - Inform Siri of reservations made from your app.
- [Defining Relevant Shortcuts for the Siri Watch Face](https://developer.apple.com/documentation/sirikit/defining_relevant_shortcuts_for_the_siri_watch_face) - Inform Siri when your app's shortcuts may be useful to the user.
- [Specifying Synonyms for Your App Name](https://developer.apple.com/documentation/sirikit/specifying_synonyms_for_your_app_name) - Provide alternative names for your app that are more familiar or easier for users to speak.
- [Intent Phrases](https://developer.apple.com/documentation/sirikit/intent_phrases) - The keys that you include in your global vocabulary file to show how users engage your app from Siri.
- [Localizing Your Vocabulary for Chinese Dialects](https://developer.apple.com/documentation/sirikit/localizing_your_vocabulary_for_chinese_dialects) - Apply emphasis markers to your pronunciation tips to assist Siri with Chinese dialects.
- [Parameter Vocabularies](https://developer.apple.com/documentation/sirikit/parameter_vocabularies) - The keys you include in your global vocabulary file to describe app-specific terms.
- [Offering Actions in the Shortcuts App](https://developer.apple.com/documentation/sirikit/offering_actions_in_the_shortcuts_app) - Suggest shortcuts users may want to add to Siri or combine with other actions in their own shortcuts.
- [Creating an Intents App Extension](https://developer.apple.com/documentation/sirikit/creating_an_intents_app_extension) - Add and configure an Intents app extension in your Xcode project.
- [Requesting Authorization to Use Siri](https://developer.apple.com/documentation/sirikit/requesting_authorization_to_use_siri) - Request permission from the user for Siri and Maps to communicate with your app or Intents app extension.
- [Structuring Your Code to Support App Extensions](https://developer.apple.com/documentation/sirikit/structuring_your_code_to_support_app_extensions) - Move your back-end services to a private framework so your app and app extensions can use them.
- [Providing Live Status Updates](https://developer.apple.com/documentation/sirikit/providing_live_status_updates) - Provide regular updates to Maps about the status of a booked ride.
- [Donating Shortcuts](https://developer.apple.com/documentation/sirikit/donating_shortcuts) - Tell Siri about shortcuts to actions that the user performed in your app.
- [Configuring the View Controller for Your Custom Interface](https://developer.apple.com/documentation/sirikit/configuring_the_view_controller_for_your_custom_interface) - Configure your view controller to replace or augment the default interface in Siri or Maps.
- [Configuring Your Intents UI App Extension Target](https://developer.apple.com/documentation/sirikit/configuring_your_intents_ui_app_extension_target) - Configure your Xcode project to include an Intents UI app extension that you use to customize the Siri and Maps interfaces.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SiriKit)*