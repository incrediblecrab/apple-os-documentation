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

**Availability:** App Intents' deployment minimums do not guarantee access to every Apple Intelligence or Siri experience. Check the particular API, device, runtime, region, and system-feature availability.

For example, App Intents enables you to express your app's actions, by offering an App Shortcut. People can then ask Siri to take those actions on their behalf, whether they're in your app or elsewhere in the system. Use App Entities to expose content in your app to Spotlight and semantic indexing with Apple Intelligence. People can then ask Siri to retrieve information from your app, like asking Siri to pull up flight information from a travel app to share with a loved one.

You reuse these components with other technologies to offer additional features and experiences that make your app and its functionality even more discoverable and widely available. For example, you reuse modular App Intents code together with WidgetKit to offer:

- Interactive widgets
- Controls
- Live Activities

To learn how to adopt these features, see [Getting started with the App Intents framework](https://developer.apple.com/documentation/appintents/getting-started-with-the-app-intents-framework.md).

For design guidance, see Human Interface Guidelines > App Shortcuts, Human Interface Guidelines > Siri, and Human Interface Guidelines > Action Button.

## OS 27 integration

Apple recommends App Intents for modern Siri and Apple Intelligence integration. [SiriKit](SiriKit.md) continues to provide **legacy support for most existing Siri interactions**, Shortcuts actions, and widget configuration. This is not a blanket framework-deprecation or removal announcement.

The documented [Apple Intelligence and Siri AI workflow](https://developer.apple.com/documentation/appintents/apple-intelligence-and-siri-ai.md) has distinct steps:

1. Model actions, entities, and enumerations with stable identifiers and useful queries.
2. Adopt matching [app schemas](https://developer.apple.com/documentation/appintents/app-schema-domains.md) so the system understands the action or content. A schema alone does not insert every entity into Spotlight.
3. [Index entities in Spotlight](https://developer.apple.com/documentation/appintents/making-app-entities-available-in-spotlight.md) and choose [transferable representations](CoreTransferable.md) where content must move between apps.
4. [Provide onscreen context](https://developer.apple.com/documentation/appintents/providing-contextual-cues-to-apple-intelligence-and-siri.md) through view/entity associations. [`AppEntityUIElement`](https://developer.apple.com/documentation/appintents/appentityuielement.md) and [`AppEntityUIElementsContext`](https://developer.apple.com/documentation/appintents/appentityuielementscontext.md) support custom-view context; UIKit and AppKit also have documented App Intents data-source protocols.
5. Donate appropriate actions and content, and validate the resulting integration.

[App Intents Testing](AppIntentsTesting.md) verifies registered intent execution, queries, Spotlight results, and view annotations out-of-process from an XCTest UI testing bundle on supported OS 27 destinations. Keep lower-OS and unavailable-system-feature paths working.

For audio search and playback, see [Media Intents](MediaIntents.md). For a staged migration from custom SiriKit intents, follow the [migration recipe](../guides/app-intents-migration.md).

## Topics

### Essentials
- [App Intents updates](https://developer.apple.com/documentation/updates/appintents.md) - Learn about important changes in App Intents.
- [Getting started with the App Intents framework](https://developer.apple.com/documentation/appintents/getting-started-with-the-app-intents-framework.md) - Make your app's actions and content available to the rest of the system.
- [Creating your first app intent](https://developer.apple.com/documentation/appintents/creating-your-first-app-intent.md) - Create your first app intent that makes your app available in system experiences like Spotlight or the Shortcuts app.
- [Adopting App Intents to support system experiences](https://developer.apple.com/documentation/appintents/adopting-app-intents-to-support-system-experiences.md) - Create app intents and entities to incorporate system experiences such as Spotlight, visual intelligence, and Shortcuts.
- [Accelerating app interactions with App Intents](https://developer.apple.com/documentation/appintents/acceleratingappinteractionswithappintents.md) - Enable people to use your app's features quickly through Siri, Spotlight, and Shortcuts.

### Siri and Apple Intelligence
- [Apple Intelligence and Siri AI](https://developer.apple.com/documentation/appintents/apple-intelligence-and-siri-ai.md) - Combine schemas, indexing, transferable content, view associations, and donations.
- [Providing contextual cues to Apple Intelligence and Siri](https://developer.apple.com/documentation/appintents/providing-contextual-cues-to-apple-intelligence-and-siri.md) - Associate onscreen content with the relevant app entities.
- [App schema domains](https://developer.apple.com/documentation/appintents/app-schema-domains.md) - Match your actions, entities, and enumerations to system-defined schemas.
- [Making actions and content discoverable by Apple Intelligence](https://developer.apple.com/documentation/appintents/making-actions-and-content-discoverable-by-apple-intelligence.md) - Adopt appropriate domain schemas so Siri can understand your app's capabilities.

The older `AssistantIntent`, `AssistantEntity`, and `AssistantEnum` macros appear in [Deprecated symbols](https://developer.apple.com/documentation/appintents/deprecated-symbols.md). Use the current app-schema documentation when updating those integrations.

### Visual Intelligence
- [Visual Intelligence](https://developer.apple.com/documentation/appintents/visual-intelligence.md) - Match images to your app's content and return results to Visual Intelligence.
- [`IntentValueQuery`](https://developer.apple.com/documentation/appintents/intentvaluequery.md) - A query that provides entity values to the system; for example, for visual intelligence search.

### Interactive Snippets
- [Displaying static and interactive snippets](https://developer.apple.com/documentation/appintents/displaying-static-and-interactive-snippets.md) - Enable people to view the outcome of an app intent and immediately perform follow-up actions.
- [`SnippetIntent`](https://developer.apple.com/documentation/appintents/snippetintent.md) - An app intent that presents an interactive snippet onscreen.

### Other system experiences
- [Making app entities available in Spotlight](https://developer.apple.com/documentation/appintents/making-app-entities-available-in-spotlight.md) - Allow people to find your app's content in Spotlight by donating app entities to its semantic index.
- [Focus](https://developer.apple.com/documentation/appintents/focus) - Adjust your app's behavior and filter incoming notifications when the current Focus changes.
- [Hardware interactions](https://developer.apple.com/documentation/appintents/hardware-interactions.md) - Run App Shortcuts with the Action button on supported iPhone models, or start workouts and dive sessions with the Action button on supported Apple Watch models.
- [Developing a WidgetKit strategy](https://developer.apple.com/documentation/widgetkit/developing-a-widgetkit-strategy.md) - Explore features, tasks, related frameworks, and constraints as you make a plan to implement widgets, controls, watch complications, and Live Activities.

### SiriKit migration
- [Soup Chef with App Intents: Migrating custom intents](https://developer.apple.com/documentation/sirikit/soup-chef-with-app-intents-migrating-custom-intents.md) - Integrate App Intents while preserving custom-intent shortcuts and donations.

### Actions
- [App intents](https://developer.apple.com/documentation/appintents/app-intents.md) - Define custom actions, their parameters, results, and runtime behavior.
- [Donations and discovery](https://developer.apple.com/documentation/appintents/donations-and-discovery.md) - Donate your app's intents and entities to help the system identify trends and predict future behaviors.
- [App Shortcuts](https://developer.apple.com/documentation/appintents/app-shortcuts.md) - Integrate your app's intents and entities with the Shortcuts app, Siri, Spotlight, and supported hardware interactions.

### Parameters, custom data types, and queries
- [Adding parameters to an app intent](https://developer.apple.com/documentation/appintents/adding-parameters-to-an-app-intent.md) - Enable people to configure app intents with their custom input values.
- [Defining app entities for your custom data types](https://developer.apple.com/documentation/appintents/defining-app-entities-for-your-custom-data-types.md) - Describe your app's data types so intents can use them as parameters.
- [`IntentParameter`](https://developer.apple.com/documentation/appintents/intentparameter.md) - Declare an intent's input argument with a property wrapper and configure its input behavior.
- [App entities](https://developer.apple.com/documentation/appintents/app-entities.md) - Make core types or concepts discoverable to the system by declaring them as app entities.
- [Entity queries](https://developer.apple.com/documentation/appintents/entity-queries.md) - Help the system find the entities your app defines and use them to resolve parameters.
- [Resolvers](https://developer.apple.com/documentation/appintents/resolvers) - Resolve the parameters of your app intents, and extend the standard resolution types to include your app's custom types.

### Utility types
- [Common data types](https://developer.apple.com/documentation/appintents/common-data-types.md) - Use framework-defined parameter and result types, including currencies, files, and contacts.

### Errors
- [`AppIntentError`](https://developer.apple.com/documentation/appintents/appintenterror.md) - Structured failure information that intent-handling code can throw.

### Protocols
- [`AppIntentSceneDelegate`](https://developer.apple.com/documentation/appintents/appintentscenedelegate.md) - Implement this protocol on your UIScene delegate to handle AppIntent invocations targeting a specific scene.
- [`AppShortcutsContent`](https://developer.apple.com/documentation/appintents/appshortcutscontent.md)
- [`CustomURLRepresentationParameterConvertible`](https://developer.apple.com/documentation/appintents/customurlrepresentationparameterconvertible.md) - Represent a custom value in an intent or entity URL.
- [`ShowsSnippetIntent`](https://developer.apple.com/documentation/appintents/showssnippetintent.md) - The result of an action that presents a snippet generated by a SnippetIntent-conforming type.
- [`TargetContentProvidingIntent`](https://developer.apple.com/documentation/appintents/targetcontentprovidingintent.md)
- [`UISceneAppIntent`](https://developer.apple.com/documentation/appintents/uisceneappintent.md)
- [`UndoableIntent`](https://developer.apple.com/documentation/appintents/undoableintent.md) - Register undoable actions from an app intent.

### Structures
- [`ConfirmationConditions`](https://developer.apple.com/documentation/appintents/confirmationconditions.md) - Conditions for a confirmation request.
- [`EntityPropertyModifiers`](https://developer.apple.com/documentation/appintents/entitypropertymodifiers.md)
- [`EntityURLRepresentation`](https://developer.apple.com/documentation/appintents/entityurlrepresentation.md) - The URL representation of an app entity.
- [`EnumURLRepresentation`](https://developer.apple.com/documentation/appintents/enumurlrepresentation.md) - The URL representation of an app enum.
- [`FileEntityIdentifier`](https://developer.apple.com/documentation/appintents/fileentityidentifier.md) - An identifier for an app entity that refers to a document or other file.
- [`IntentChoiceOption`](https://developer.apple.com/documentation/appintents/intentchoiceoption.md) - A structure representing an entry in a list of options for a person to choose from before an app intent resumes its action.
- [`IntentModes`](https://developer.apple.com/documentation/appintents/intentmodes.md) - A set of options that describe an app intent's behavior.
- [`IntentURLRepresentation`](https://developer.apple.com/documentation/appintents/intenturlrepresentation.md) - The URL representation of an app intent.

### Macros
- [`UnionValue()`](https://developer.apple.com/documentation/appintents/unionvalue().md)

### Enumerations
- [`AppShortcutPhraseToken`](https://developer.apple.com/documentation/appintents/appshortcutphrasetoken.md) - Dynamic values you can include in the spoken phrases that run your shortcut.
- [`VideoCategory`](https://developer.apple.com/documentation/appintents/videocategory.md)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AppIntents)*
