# Siri

Siri makes it easy for people to accomplish everyday tasks quickly, using voice, touch, or automation.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

When you use SiriKit to define the tasks and actions that your app supports, people can use Siri to perform them even when your app isn't running. If you're an accessory maker, you can also help people use Siri to control your accessories by integrating them with HomeKit or AirPlay. Here are some of the ways people can use Siri to interact with your app or accessory:

- Ask Siri to perform a system-defined task that your app supports, like send a message, play a song, or start a workout
- Run a shortcut, which is a way to accelerate actions your app defines through onscreen interactions or by voice
- Use the Shortcuts app to adjust what a shortcut does, including combining several actions to perform one multistep shortcut
- Tap a suggestion to perform a shortcut with your app (Siri can suggest shortcuts that people might want to perform, based on their current context and the information you provide)
- Use Siri to control an accessory that integrates with your app

Siri works with your products on iPhone, iPad, Mac, Apple Watch, HomePod, and AirPods, so people can use it almost everywhere.

## Topics

### Best Practices

**Integrating Your App with Siri**

- **Identify key tasks in your app that people might want to perform on a regular basis** - Focus on actions that people use frequently and would benefit from voice activation.
- **Drive engagement by telling the system about your app's key tasks and by supporting suggestions** - When you provide information about your actions to the system, Siri can suggest shortcuts when people are likely to be interested in them.
- **Design functional conversational flows that feel natural** - For actions that people can perform through voice interaction, create flows that mirror natural conversation patterns.
- **Consider various usage contexts** - Explore the different ways people might perform your app's tasks, such as in hands-free situations, and the devices they might be using.

**Voice Experience Design**

- **Complete requests without leaving Siri whenever possible** - If a request must be finished in your app, take people directly to the expected destination without showing intermediary screens.
- **When a request has financial impact, default to the safest and least expensive option** - Never deceive people or misrepresent information. For purchases with multiple pricing levels, don't default to the most expensive.
- **Provide alternative results if media playback requests are ambiguous** - When you display alternative results within the Siri UI, people can easily choose different content if your first offering isn't what they want.
- **Design streamlined workflows for Apple Watch** - Use intelligent defaults instead of asking for input whenever possible.

**Custom Vocabulary and Examples**

- **Create example requests** - When people tap the Help button in the Siri interface, they view a guide that can include example phrases you supply.
- **Define custom vocabulary that people use with your app** - Help Siri learn specific terms people might use in requests, like account names, contact names, and workout names.
- **Consider defining alternative app names** - If people might refer to your app in different ways, provide alternative names to help Siri understand what people mean.

### System Intents

SiriKit defines a large number of system intents that represent common tasks people do, such as playing music, sending messages to friends, and managing notes. For system intents, Siri defines the conversational flow, while your app provides the data to complete the interaction.

**Available Domains:**
- **VoIP Calling** - Initiate calls
- **Workouts** - Start, pause, resume, end, and cancel workouts  
- **Lists and Notes** - Create notes, search for notes, create reminders
- **Media** - Search for and play media content, like or dislike items, add items to library or playlist
- **Messaging** - Send messages, search for messages, read received messages
- **Payments** - Send payments, request payments
- **Car Commands** - Activate hazard lights, lock/unlock doors, check fuel or power level

### Custom Intents

If your app lets people perform an everyday task that doesn't fit into any of the SiriKit domains, you can create a custom intent to represent it. Custom intents give people a quick way to initiate frequently performed actions by speaking a simple phrase or accepting a suggestion from Siri.

**Custom Intent Categories:**
- **Generic** - Do, Run, Go
- **Information** - View, Open
- **Order** - Order, Book, Buy
- **Start** - Start
- **Navigate** - Navigate
- **Share** - Share, Post, Send
- **Create** - Create, Add
- **Search** - Search, Find, Filter
- **Download** - Download, Get
- **Other** - Set, Request, Toggle, Check in

**Design Guidelines:**
- **Design custom intents that accelerate common, useful tasks** - Take advantage of the familiarity people have with your app
- **Ensure your intent works well in every scenario** - Make it easy for people to run your intent as a shortcut, regardless of how they initiate it
- **Design intents for tasks that aren't overly complex** - People benefit most from intents that reduce the number of actions required to complete a task
- **Design your intents to be long-lived** - Avoid offering intents that are date-specific or associated with temporary data
- **Support background operation** - The best intents support shortcuts that run quickly without bringing your app to the front

### Shortcuts and Suggestions

When you support shortcuts, people have various ways to discover and interact with the custom and system intents your app provides:

- Siri can suggest shortcuts for actions people have performed at least once
- Your app can supply shortcuts for actions people haven't done yet but might want to do
- People can use the Shortcuts app to view all their shortcuts and combine actions from different apps
- People can automate shortcuts by defining conditions that run them

**Shortcut Best Practices:**
- **Make app actions widely available** - Donate information about actions to help the system offer them to people in various ways
- **Make a donation every time people perform the action** - This helps the system accurately predict when to offer shortcuts
- **Only donate actions that people actually perform** - Don't donate when people browse menus or perform unrelated actions
- **Remove donations for actions that require corresponding data** - If required information no longer exists, delete the donation

### Platform Considerations

**iOS, iPadOS**  
In iPadOS and iOS, an app's keyboard shortcuts appear in the shortcut interface that displays when people hold the Command key on a connected keyboard.

**macOS**  
The Shortcuts app is available in macOS 12 and later.

**tvOS**  
tvOS apps can use gyroscope data from the Siri Remote to enhance Siri interactions.

**visionOS**  
When people connect a physical keyboard while using your visionOS app or game, the system displays a virtual keyboard overlay.

**watchOS**  
The Shortcuts app is available in watchOS 7 and later. All watchOS apps participating in a nearby interaction experience must be in the foreground.

### Related Components

- [App Shortcuts](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts) - App shortcuts guidance
- [Design for intelligence](https://developer.apple.com/design/human-interface-guidelines/designing-for-intelligence) - Intelligence design principles

### Developer Documentation

- [SiriKit](https://developer.apple.com/documentation/sirikit) - Framework
- [System intents](https://developer.apple.com/documentation/sirikit/system_intents) - Available system intents
- [Creating an Intents UI Extension](https://developer.apple.com/documentation/sirikit/creating_an_intents_ui_extension) - Custom UI guidance

### Videos

- [Design interactive snippets](https://developer.apple.com/videos/play/wwdc2023/10229/)
- [Explore Machine Learning in Apple Frameworks](https://developer.apple.com/videos/play/wwdc2023/10166/)

## Changelog

### June 5, 2023
- Removed Add to Siri guidance
- Added references to the new App Shortcuts page

### May 2, 2023
- Consolidated guidance into one page

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/siri)*