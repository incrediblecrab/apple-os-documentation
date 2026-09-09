# App Shortcuts

An App Shortcut gives people access to your app's key functions or content throughout the system.

**Platforms:** iOS | iPadOS | visionOS | watchOS

## Overview

People can initiate App Shortcuts using features like Siri, Spotlight, and the Shortcuts app; using hardware features like the Action button on iPhone or Apple Watch; or by squeezing Apple Pencil.

Because App Shortcuts are part of your app, they are available immediately when installation finishes. For example, a journaling app could offer an App Shortcut for making a new journal entry that's available before a person opens the app for the first time. Once someone starts using your app, its App Shortcuts can reflect their choices, like those from FaceTime for calling recent contacts.

App Shortcuts use App Intents to define actions within your app to make available to the system. Each App Shortcut includes one or more actions that represent a set of steps people might want to perform to accomplish a task. For example, a home security app might combine the two common actions of turning off the lights and locking exterior doors when a person goes to sleep at night into a single App Shortcut. Each app can include up to 10 App Shortcuts.

Note: When you use App Intents to make your app's actions available to the system, in addition to the App Shortcuts that your app provides, people can also make their own custom shortcuts by combining actions in the Shortcuts app. Custom shortcuts give people flexibility to configure the behavior of actions, and enable workflows that perform tasks across multiple apps. For additional guidance, see the Shortcuts User Guide.

## Topics

### Best Practices

Use [App Intents](https://developer.apple.com/documentation/appintents) to describe your app's actions and relevant data. When an action needs a compact confirmation or visual result, follow the [Snippets](snippets.md) guidance, including its platform and accessibility considerations.

- **Offer App Shortcuts for your app's most common and important tasks** - Straightforward tasks that people can complete without leaving their current context work best, but you can also open your app if it helps people complete multistep tasks more easily.
- **Add flexibility by letting people choose from a set of options** - An App Shortcut can include a single optional value, or parameter, if it makes sense. For example, a meditation app could offer an App Shortcut that lets someone begin a specific type of meditation: "Start [morning, daily, sleep] meditation." Include predictable and familiar values as options, because people won't have the list in front of them for reference. For developer guidance, see Adding parameters to an app intent.
- **Ask for clarification in response to a request that's missing optional information** - For example, someone might say "Start meditation" without specifying the type (morning, daily, or sleep); you could follow up by suggesting the one they used most recently, or one based on the current time of day. If one option is most likely, consider presenting it as the default, and provide a short list of alternatives to choose from if a person doesn't want the default choice.
- **Keep voice interactions simple** - If your phrase feels too complicated when you say it aloud, it's probably too difficult to remember or say correctly. For example, "Start [sleep] meditation with nature sounds" appears to have two possible parameters: the meditation type, and the accompanying sound. If additional information is absolutely required, ask for it in a subsequent step. For additional guidance on writing dialogue text for voice interactions, see Siri.
- **Make App Shortcuts discoverable in your app** - People are most likely to remember and use App Shortcuts for tasks they do often, once they know the shortcut is available. Consider showing occasional tips in your app when people perform common actions to let them know an App Shortcut exists. For developer guidance, see SiriTipUIView.

### Responding to App Shortcuts

As a person engages with an App Shortcut, your app can respond in a variety of ways, including with dialogue that Siri speaks aloud and custom visuals like snippets and Live Activities.

Snippets can display information or let people interact with an action's result, such as reviewing the weather or confirming an order. For developer guidance, see [Displaying static and interactive snippets](https://developer.apple.com/documentation/appintents/displaying-static-and-interactive-snippets).

Live Activities offer continuous access to information that's likely to remain relevant and change over a period of time, and are great for timers and countdowns that appear until an event is complete. For developer guidance, see LiveActivityIntent.

- **Provide enough detail for interaction on audio-only devices** - People can receive responses on audio-only devices such as AirPods and HomePod too, and may not always be able to see content onscreen. Include all critical information in the full dialogue text of your App Shortcuts. For developer guidance, see init(full:supporting:systemImageName:).

### Editorial Guidelines

- **Provide brief, memorable activation phrases and natural variants** - Because an App Shortcut phrase (or a variant you define) is what people say to run an App Shortcut with Siri, it's important to keep it brief to make it easier to remember. You have to include your app name, but you can be creative with it. For example, Keynote accepts both "Create a Keynote" and "Add a new presentation in Keynote" as App Shortcut phrases for creating a new document. For developer guidance, see AppShortcutPhrase.
- **When referring to App Shortcuts or the Shortcuts app, always use title case and make sure that Shortcuts is plural** - For example, MyApp integrates with Shortcuts to provide a quick way to get things done with just a tap or by asking Siri, and offers App Shortcuts you can place on the Action button.
- **When referring to individual shortcuts (not App Shortcuts or the Shortcuts app), use lowercase** - For example, Run a shortcut by asking Siri or tapping a suggestion on the Lock Screen.

### Platform Considerations

**iOS, iPadOS**  
- App Shortcuts can appear in the Top Hit area of Spotlight when people search for your app, or in the Shortcuts area below. Each App Shortcut includes a symbol from SF Symbols that you choose to represent its functionality, or a preview image of an item that the shortcut links to directly.
- Order shortcuts based on importance. The order you choose determines how App Shortcuts initially appear in both Spotlight and the Shortcuts app, so it's helpful to include the most generally useful ones first. Once people start using your App Shortcuts, the system updates to prioritize the ones they use most frequently.

**macOS**  
- The HIG's platform section says App Shortcuts aren't supported in macOS, while the [AppShortcutsProvider declaration](https://developer.apple.com/documentation/appintents/appshortcutsprovider) lists macOS availability. These sources don't provide a consistent platform summary, so don't use the HIG sentence as an API availability table. App Intents actions can participate in custom shortcuts on Mac; check the documentation for the particular system experience you support.

**visionOS, watchOS**  
- No additional considerations.

**tvOS**  
- Not supported.

### Related

- [Siri](https://developer.apple.com/design/human-interface-guidelines/siri)
- [Siri Style Guide](https://developer.apple.com/siri/style-guide/)
- [Shortcuts User Guide](https://support.apple.com/guide/shortcuts/welcome/ios)

### Developer Documentation

- [App Intents](https://developer.apple.com/documentation/AppIntents) - AppIntents
- [SiriKit](https://developer.apple.com/documentation/SiriKit) - SiriKit
- [Getting started with the App Intents framework](https://developer.apple.com/documentation/appintents/getting-started-with-the-app-intents-framework) - App Intents
- [App entities](https://developer.apple.com/documentation/appintents/app-entities) - App Intents

### Videos

- [Design interactive snippets](https://developer.apple.com/videos/play/wwdc2025/281)
- [Get to know App Intents](https://developer.apple.com/videos/play/wwdc2025/244)
- [Spotlight your app with App Shortcuts](https://developer.apple.com/videos/play/wwdc2023/10102/)

## Changelog

### January 17, 2025
- Updated and streamlined guidance.

### June 5, 2023
- New page.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts)*
