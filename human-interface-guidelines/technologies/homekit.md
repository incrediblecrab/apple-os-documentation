# HomeKit

HomeKit lets people securely control connected accessories in their homes using Siri or the Home app on iPhone, iPad, Apple Watch, and Mac.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

In iOS, the Home app also lets people manage and configure accessories.

Your iOS, tvOS, or watchOS app can integrate with HomeKit (and by extension the Home app) to provide a custom or accessory-specific experience. For example, you can:

- Help people set up, name, and organize their accessories
- Allow fine-grained accessory configuration and control
- Provide access to custom accessory features
- Show people how to create powerful, hands-free automations
- Provide support

For developer guidance, see HomeKit. If you're an MFi licensee, visit the MFi portal for guidance on naming and messaging for accessory packaging.

## Topics

### Terminology and Layout

HomeKit models the home as a hierarchy of objects and defines a vocabulary of terms that refer to them. The Home app uses the HomeKit object model and terminology to give people intuitive control of accessories by voice, app, and automation.

It's crucial for your app to use the terminology and object model that HomeKit defines, so that you can reinforce people's understanding and make home automation feel approachable.

In the HomeKit model, the home object is the root of a hierarchy that contains all other objects, such as rooms, accessories, and zones. When there's more than one home, each home is the root of a different hierarchy.

- **Acknowledge the hierarchical model that HomeKit uses** - Even if your app doesn't organize accessories by rooms and zones in its UI, it's useful to reference the HomeKit model when helping people set up or control their accessories. People need to know where accessories are located so they can use Siri and HomePod to control them by speaking commands like "Siri, turn on the lights upstairs," or "It's dark in here."
- **Make it easy for people to find an accessory's related HomeKit details** - If your app's organization is based on accessories, don't hide other HomeKit information, such as an accessory's zone or room, in a hard-to-discover settings screen. Instead, consider making the related HomeKit information easily available in an accessory detail view.
- **Recognize that people can have more than one home** - Even if your app doesn't support the concept of multiple homes per user, consider providing the relevant home information in an accessory detail view.
- **Don't present duplicate home settings** - If your app has a different perspective on the organization of a home, don't confuse people by asking them to set up all or parts of their homes again or by showing a duplicate settings view. Always defer to the settings people made in the Home app and find an intuitive way to present these details in your UI.

### Object Model Terms

**Homes**  
HomeKit uses the term home to represent a physical home, office, or other location of relevance to people. One person might have multiple homes.

**Rooms**  
A room represents a physical room in a home. Rooms don't have attributes like size or location; they're simply names that have meaning to people, such as Bedroom or Office.

**Accessories, services, and characteristics**  
The term accessory represents a physical, connected home accessory, like a ceiling fan, lamp, lock, or camera. HomeKit uses category to represent a type of accessory, such as thermostat, fan, or light.

A controllable feature of an accessory, such as the switch on a connected light, is known as a service. Some accessories offer multiple services.

A characteristic is a controllable attribute of a service. For example, in a ceiling fan, the fan service might have a speed characteristic and the light service might have a brightness characteristic.

A service group represents a group of accessory services that someone might want to control as a unit.

**Actions and scenes**  
The term action refers to the changing of a service's characteristic, such as adjusting the speed of a fan or the brightness of a light.

A scene is a group of actions that control one or more services in one or more accessories. For example, people might create a Movie Time scene that lowers the shades and dims the lights in the living room, or a Good Morning scene that turns on the lights, raises the shades, and starts the coffee maker in the kitchen.

**Automations**  
Automations cause accessories to react to certain situations, such as when a person's location changes, a particular time of day occurs, another accessory turns on or off, or a sensor detects something.

**Zones**  
A zone represents an area in the home that contains multiple rooms, such as upstairs or downstairs. Setting up a zone is optional, but doing so lets people control multiple accessories at one time.

### Setup

- **Use the system-provided setup flow to give people a familiar experience** - The HomeKit setup flow works more quickly than traditional setup flows because it lets people name accessories, join networks, pair with HomeKit, assign room and service categories, and designate favorites in just a few steps.
- **Provide context to explain why you need access to people's Home data** - Create a purpose string with a phrase that describes why you're asking for permission to access data, such as "Lets you control this accessory with the Apple Home app and Siri across your Apple devices."
- **Don't require people to create an account or supply personal information** - Instead, defer to HomeKit for any information you might need. If your app provides additional services that require an account, such as cloud services, make account setup optional and wait until after initial HomeKit setup to offer it.
- **Honor people's setup choices** - When people choose to use HomeKit to set up your accessory, don't force them to set up other platforms during the HomeKit setup flow.
- **Carefully consider how and when to provide a custom accessory setup experience** - Always begin by presenting the system-provided setup flow. Then, after the accessory's basic functionality is available, offer a custom post-setup experience that highlights the unique features of your accessory.

### Help People Choose Useful Names

- **Suggest service names that suit your accessory** - If your app detects when someone creates a suboptimal name for Siri voice controls, recommend alternatives that you know will work well for most people. Never suggest company names or model numbers for use as service names.
- **Check that the names people provide follow HomeKit naming rules** - If people enter a name that breaks one or more rules, briefly explain the problem and suggest some alternative names that work.

HomeKit naming rules:
- Use only alphanumeric, space, and apostrophe characters
- Start and end with an alphabetic or numeric character
- Don't include emojis

- **Help people avoid creating names that include location information** - Although it's natural for someone to use "kitchen light" to name a light in the kitchen, including the room name in the service name can lead to unpredictable results when controlling the accessory by voice.

### Siri Interactions

HomeKit supports powerful, hands-free control using voice commands. You can help people use Siri to interact with accessories, services, and zones in their home quickly and efficiently.

- **Present example voice commands to demonstrate using Siri to control accessories during setup** - As soon as people complete the setup of a new accessory, consider using the service name they chose in a few example Siri phrases and encourage people to try them out.
- **After setup, consider teaching people about more complex Siri commands** - People might not be aware of the broad range of natural language phrases they can use with Siri and HomePod to control their accessories.
- **Recommend that people create zones and service groups, if they make sense for your accessory** - If people might benefit from using context-specific voice commands to control your accessory, suggest these types of interactions and help people set them up.
- **Offer shortcuts only for accessory-specific functionality that HomeKit doesn't support** - HomeKit lets people use ordinary (or natural) language to control accessories without requiring any additional configuration, so you avoid confusing people by offering shortcuts that duplicate HomeKit functionality.
- **If your app supports both HomeKit and shortcuts, help people understand the difference between these types of voice control** - People can get confused if they're presented with multiple methods of voice control.

### Custom Functionality

- **Be clear about what people can do in your app and when they might want to use the Home app** - For example, if your app supports only lights, consider encouraging people to create a "Movie Time" scene that not only dims the lights, but also closes the shades, and turns on the TV to a specific input.
- **Defer to HomeKit if your database differs from the HomeKit database** - Give people a seamless experience by automatically reflecting changes made in the Home app or in other third-party HomeKit apps.
- **Ask permission to update the HomeKit database when people make changes in your app** - You don't want to surprise people by changing something in the Home app, so it's essential to get permission or an indication of intent before you write to the database.

### Cameras

Your app can display still images or streaming video from a connected HomeKit IP camera.

- **Don't block camera images** - It's fine to supplement the camera's content with useful features, such as an alert calling attention to potentially interesting activity. However, avoid covering portions of the camera's images with other content.
- **Show a microphone button only if the camera supports bidirectional audio** - A nonfunctioning microphone button takes up valuable display space in your app and risks confusing people.

### Using HomeKit Icons

Use the HomeKit icon in setup or instructional communications related to HomeKit technology.

In addition, you can use the Apple Home app icon when referencing the Apple Home app or in a button that opens the Apple Home app product page in the App Store.

- **Use only Apple-provided icons** - Don't create your own HomeKit or Home app icon design or attempt to mimic the Apple-provided designs.
- **Position the HomeKit icon consistently with other technology icons** - When other technology icons are contained within shapes, treat the HomeKit icon in the same manner.
- **Use the HomeKit icon noninteractively** - Don't use the icon and the name HomeKit in custom interactive elements or buttons. You can use the Apple Home app icon to open the app's product page in the App Store.
- **Don't use the HomeKit icon within text or as a replacement for the word HomeKit** - See Referring to HomeKit to learn how to properly reference HomeKit in text.
- **Pair the icon with the name HomeKit correctly** - You can show the name below or beside the icon if other technologies are referenced in this way. Use the same font that's used on the rest of your layout.

### Referring to HomeKit

- **Emphasize your app over HomeKit** - Make references to HomeKit or Apple Home less prominent than your app name or main identity.
- **Adhere to Apple's trademark guidelines** - Apple trademarks can't appear in your app name or images. In text, use Apple product names exactly as shown on the Apple Trademark List.
- **Use correct capitalization when using the term HomeKit** - HomeKit is one word, with an uppercase H and uppercase K, followed by lowercase letters. Apple Home is two words, with an uppercase A and uppercase H, followed by lowercase letters.
- **Don't use the name HomeKit as a descriptor** - Instead use terms like works with, use, supports, or compatible.
- **Don't suggest that HomeKit is performing an action or function** - For example, say "Back door is unlocked with HomeKit," not "HomeKit unlocked the back door."
- **Use the app name Apple Home whenever referring specifically to the app** - On the first mention of the app in body copy, use the complete name Apple Home. Subsequent mentions can refer to the Home app.

### Platform Considerations

No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.

### Related Components

- [Guidelines for Using Apple Trademarks and Copyrights](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html)

### Developer Documentation

- [HomeKit](https://developer.apple.com/documentation/homekit) - HomeKit
- [performAccessorySetup(using:completionHandler:)](https://developer.apple.com/documentation/homekit/hmaccessorysetupmanager/performaccessorysetup(using:completionhandler:)) - HomeKit

## Changelog

### May 2, 2023
- Consolidated guidance into one page.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/homekit)*