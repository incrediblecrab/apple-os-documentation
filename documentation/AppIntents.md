# App Intents

Make your app's content and actions discoverable with system experiences like Spotlight, widgets, and the Shortcuts app.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 16.0+ | macOS 13.0+ | tvOS 16.0+ | visionOS 1.0+ | watchOS 9.0+

## Overview

The App Intents framework provides functionality to deeply integrate your app's actions and content with system experiences across platforms, including Siri, Spotlight, widgets, controls and more. With Apple Intelligence and enhancements to App Intents, Siri will suggest your app's actions to help people discover your app's features and gains the ability to take actions in and across apps.

By adopting the App Intents framework, you allow people to personalize their devices by instantly using your app's functionality with:

- Interactions with Siri, including those that use the personal context awareness and action capabilities of Apple Intelligence.
- Spotlight suggestions and search.
- Actions and automations in the Shortcuts app.
- Hardware interactions that initiate app actions, like the Action button and squeeze gestures on Apple Pencil.
- Focus to allow people to reduce distractions.

**Note:** Siri's personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.

For example, App Intents enables you to express your app's actions, by offering an App Shortcut. People can then ask Siri to take those actions on their behalf, whether they're in your app or elsewhere in the system. Use App Entities to expose content in your app to Spotlight and semantic indexing with Apple Intelligence. People can then ask Siri to retrieve information from your app, like asking Siri to pull up flight information from a travel app to share with a loved one.

You reuse these components with other technologies to offer additional features and experiences that make your app and its functionality even more discoverable and widely available. For example, you reuse modular App Intents code together with WidgetKit to offer:

- Interactive widgets
- Controls
- Live Activities

To learn more about features that the App Intents framework enables and how you can best adopt the framework, see Making actions and content discoverable and widely available.

For design guidance, see Human Interface Guidelines > App Shortcuts, Human Interface Guidelines > Siri, and Human Interface Guidelines > Action Button.

## Topics

### Essentials
- [App Intents updates](https://developer.apple.com/documentation/appintents/app_intents_updates) - Learn about important changes in App Intents.
- [Making actions and content discoverable and widely available](https://developer.apple.com/documentation/appintents/making_actions_and_content_discoverable_and_widely_available) - Adopt App Intents to make your app discoverable with Spotlight, controls, widgets, and the Action button.
- [Creating your first app intent](https://developer.apple.com/documentation/appintents/creating_your_first_app_intent) - Create your first app intent that makes your app available in system experiences like Spotlight or the Shortcuts app.
- [Adopting App Intents to support system experiences](https://developer.apple.com/documentation/appintents/adopting_app_intents_to_support_system_experiences) - Create app intents and entities to incorporate system experiences such as Spotlight, visual intelligence, and Shortcuts.
- [Accelerating app interactions with App Intents](https://developer.apple.com/documentation/appintents/accelerating_app_interactions_with_app_intents) - Enable people to use your app's features quickly through Siri, Spotlight, and Shortcuts.

### Siri and Apple Intelligence
- [Integrating actions with Siri and Apple Intelligence](https://developer.apple.com/documentation/appintents/integrating_actions_with_siri_and_apple_intelligence) - Create app intents, entities, and enumerations that conform to assistant schemas to tap into the enhanced action capabilities of Siri and Apple Intelligence.
- [Making onscreen content available to Siri and Apple Intelligence](https://developer.apple.com/documentation/appintents/making_onscreen_content_available_to_siri_and_apple_intelligence) - Enable Siri and Apple Intelligence to respond to a person's questions and action requests for your app's onscreen content.
- [App intent domains](https://developer.apple.com/documentation/appintents/app_intent_domains) - Make your app's actions and content available to Siri and Apple Intelligence with assistant schemas.
- [Making your app's functionality available to Siri](https://developer.apple.com/documentation/appintents/making_your_app_s_functionality_available_to_siri) - Add assistant schemas to your app so Siri can complete requests, and integrate your app with Apple Intelligence, Spotlight, and other system experiences.

### Visual Intelligence
- [Integrating your app with visual intelligence](https://developer.apple.com/documentation/appintents/integrating_your_app_with_visual_intelligence) - Enable people to find app content that matches their surroundings or objects onscreen with visual intelligence.
- [Visual Intelligence](https://developer.apple.com/documentation/appintents/visual_intelligence) - Include your app's content in search results that visual intelligence provides. (Beta)
- **IntentValueQuery** - A query that provides entity values to the system; for example, for visual intelligence search.

### Interactive Snippets
- [Displaying static and interactive snippets](https://developer.apple.com/documentation/appintents/displaying_static_and_interactive_snippets) - Enable people to view the outcome of an app intent and immediately perform follow-up actions.
- **SnippetIntent** - An app intent that presents an interactive snippet onscreen.

### Other system experiences
- [Making app entities available in Spotlight](https://developer.apple.com/documentation/appintents/making_app_entities_available_in_spotlight) - Allow people to find your app's content in Spotlight by donating app entities to its semantic index.
- [Focus](https://developer.apple.com/documentation/appintents/focus) - Adjust your app's behavior and filter incoming notifications when the current Focus changes.
- [Action button on iPhone and Apple Watch](https://developer.apple.com/documentation/appintents/action_button_on_iphone_and_apple_watch) - Enable people to run your App Shortcuts with the Action button on iPhone or to start your app's workout or dive sessions using the Action button on Apple Watch.
- [Developing a WidgetKit strategy](https://developer.apple.com/documentation/widgetkit/developing_a_widgetkit_strategy) - Explore features, tasks, related frameworks, and constraints as you make a plan to implement widgets, controls, watch complications, and Live Activities.

### SiriKit migration
- [Soup Chef with App Intents: Migrating custom intents](https://developer.apple.com/documentation/appintents/soup_chef_with_app_intents_migrating_custom_intents) - Integrating App Intents to provide your appʼs actions to Siri and Shortcuts.

### Actions
- [App intents](https://developer.apple.com/documentation/appintents/app_intents) - Define the custom actions your app exposes to the system, and incorporate support for existing SiriKit intents.
- [Intent discovery](https://developer.apple.com/documentation/appintents/intent_discovery) - Donate your app's intents to the system to help it identify trends and predict future behaviors.
- [App Shortcuts](https://developer.apple.com/documentation/appintents/app_shortcuts) - Integrate your app's intents and entities with the Shortcuts app, Siri, Spotlight, and the Action button on supported iPhone and Apple Watch models.

### Parameters, custom data types, and queries
- [Adding parameters to an app intent](https://developer.apple.com/documentation/appintents/adding_parameters_to_an_app_intent) - Enable people to configure app intents with their custom input values.
- [Integrating custom data types into your intents](https://developer.apple.com/documentation/appintents/integrating_custom_data_types_into_your_intents) - Provide the system with information about the types your app uses to model its data so that your intents can use those types as parameters.
- [Parameter resolution](https://developer.apple.com/documentation/appintents/parameter_resolution) - Define the required parameters for your app intents and specify how to resolve those parameters at runtime.
- [App entities](https://developer.apple.com/documentation/appintents/app_entities) - Make core types or concepts discoverable to the system by declaring them as app entities.
- [Entity queries](https://developer.apple.com/documentation/appintents/entity_queries) - Help the system find the entities your app defines and use them to resolve parameters.
- [Resolvers](https://developer.apple.com/documentation/appintents/resolvers) - Resolve the parameters of your app intents, and extend the standard resolution types to include your app's custom types.

### Utility types
- [Common types](https://developer.apple.com/documentation/appintents/common_types) - Specify common types that your app supports, including currencies, files, and contacts.

### Errors
- **AppIntentError** - Errors that your intent-handling code can return to indicate problems while interpreting or executing an app intent.

### Protocols
- **AppIntentSceneDelegate** - Implement this protocol on your UIScene delegate to handle AppIntent invocations targeting a specific scene (Beta)
- **AppShortcutsContent**
- **CustomURLRepresentationParameterConvertible**
- **ShowsSnippetIntent** - The result of performing an action that present a snippet generated by a SnippetIntent-conforming type.
- **TargetContentProvidingIntent** (Beta)
- **UISceneAppIntent** (Beta)
- **UndoableIntent**

### Structures
- **ConfirmationConditions** - Conditions for a confirmation request.
- **EntityPropertyModifiers**
- **EntityURLRepresentation** - The URL representation of an app entity.
- **EnumURLRepresentation** - The URL representation of an app enum.
- **FileEntityIdentifier** - An identifier for an app entity that refers to a document or other file.
- **IntentChoiceOption** - A structure representing an entry in a list of options for a person to choose from before an app intent resumes its action.
- **IntentModes** - A set of options that describe an app intent's behavior.
- **IntentURLRepresentation** - The URL representation of an app intent.

### Macros
- **UnionValue()**

### Enumerations
- **AppShortcutPhraseToken** - Dynamic values you can include in the spoken phrases that run your shortcut.
- **VideoCategory**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AppIntents)*