# SharePlay

SharePlay lets people do activities together from anywhere, such as watching a movie, playing a game, or sketching on a whiteboard.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS

## Overview

With SharePlay, people take part in your app's activities together from their own devices, even when they aren't in the same room. An activity is a shareable experience your app defines. The system keeps each activity in sync on every participant's device and works alongside FaceTime or Messages, so people can talk while they share.

An activity can start from a control in your app, from a FaceTime call, or from a shared link. The system asks each participant to open your app on their own device and invites anyone who doesn't have it to download it from the App Store.

> **Note:** When an activity involves content people buy or subscribe to, each participant needs their own copy or subscription. The system prompts anyone without access to download or subscribe.

## Topics

### Best Practices

- **Use SharePlay for real-time experiences** - SharePlay is built for activities people do together at the same moment. To also support collaboration on each person's own schedule, let people share or save the activity after the session ends. For example, people can view and edit a Freeform board together over SharePlay, then share a link to keep collaborating afterward. For developer guidance, see [Adding shared content collaboration to your app](https://developer.apple.com/documentation/sharedwithyou/adding-shared-content-collaboration-to-your-app).

- **Fit the experience to what people are doing together** - For many activities, like watching or browsing, everyone sharing one view works best. Other activities are better when each person's view reflects their role, like a game that gives every player their own perspective.

- **Design activities that work across Apple platforms** - People may share with others who use different devices, settings, and ways of communicating. Make the experience adapt to those differences so everyone can take part.

- **Make it easy to start a shared activity** - Give people a clear, recognizable way to begin, such as a button that includes the SharePlay symbol. People can also start from system features like the share sheet, and in visionOS from the Share button next to the window bar. For developer guidance, see [Presenting SharePlay activities from your app's UI](https://developer.apple.com/documentation/groupactivities/promoting-shareplay-activities-from-your-apps-ui).

- **Let people join an activity without friction** - Take people who join straight to the shared content, without views unrelated to the activity. If they must sign in, download content, or subscribe first, guide them in a view that goes away as soon as they finish. For purchases and subscriptions, consider offering nonsubscribers provisional access or supporting Family Sharing. Move nonessential steps to a natural later moment; for example, a game can let people join a match right away and set up a profile once they're connected.

- **Describe activities clearly and concisely** - A clear description in the invitation tells people what they're about to join. For a movie, that might be the title, a short summary, and a poster image. Keep the description short enough to avoid truncation.

- **Keep people oriented as an activity changes** - When one person's action changes the activity for everyone, help people see why. For media, the system can coordinate playback, so pausing a movie for one person pauses it for all. For other changes, show who's doing what with in-app cues; in Freeform, for example, each participant's initials appear next to their contribution.

- **Use the term SharePlay correctly** - You can use SharePlay as a noun, as in "Join SharePlay," or as a verb for an action in your interface, like a SharePlay Movie button. Don't pair SharePlay with an adjective (in a visionOS app, for example, don't add words like virtual or spatial), and don't change the term itself, as in SharePlayed, SharePlays, or SharePlaying.

### Platform Considerations

No additional considerations for tvOS. SharePlay isn't supported in watchOS.

**iOS, iPadOS, macOS**

- **Support Picture in Picture for shared video** - Let people keep watching together while they do other things on their device. On iPhone and iPad, a shared video can keep playing in a Picture in Picture window; on Mac, it can keep playing in a window people bring forward when they want to watch.

**visionOS**

In visionOS, SharePlay adds a sense of presence to shared activities, whether people are collaborating in the same room, playing a game with friends far away, or catching up over FaceTime. People can share standard windows through screen mirroring with the Share button by default; adopt SharePlay to share volumetric windows and immersive content.

#### Designing shared activities

When people join a shared activity, the system creates a shared context so everyone experiences your content in the same relative location. People can talk about, point to, and interact with the content as if it were in the room with them. Keeping your app's windows and volumes aligned across devices assures people that they're looking at the same thing, and your app needs to position 3D objects, play sounds, and handle interactions in ways that reinforce the feeling of being together. For developer guidance, see [Synchronizing data during a SharePlay activity](https://developer.apple.com/documentation/groupactivities/synchronizing-data-during-a-shareplay-activity).

- **Prefer starting your experience from a window** - People can find and share an activity that starts in a window by tapping the Share button next to the window bar. An activity that begins in an immersive space needs custom UI to start it. For developer guidance, see [Implementing SharePlay for immersive spaces in visionOS](https://developer.apple.com/documentation/visionos/implementing-shareplay-for-immersive-spaces-in-visionos).

- **Resolve conflicts naturally** - More than one person may try to act on the same thing at once. If only one person can use a tool or object at a time, don't show UI that lets someone else take control; let people speak or gesture to the group when they want a turn. A simple rule, such as the last change wins, keeps the environment collaborative and predictable.

- **Reserve unique views for moments that call for them** - In general, keep views and immersion levels in sync so people feel connected, though a personalized view sometimes improves the experience. When someone enters an immersive view of their own, show a contact photo in place of their spatial Persona so others know they've stepped away, and let everyone keep talking over FaceTime Audio.

- **Let people opt in to immersion changes when they're mid-task** - When one person changes their level of immersion, your app can bring everyone along, but first check whether the change would interrupt what someone is doing; if it would, let that person choose when to join. For example, when someone watching a movie in the Apple TV app switches to an immersive environment, a participant busy in another window sees a prompt to join when ready, while everyone else transitions right away. For guidance, see [Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences).

- **Let participants adjust the experience for comfort and accessibility** - Settings like volume and subtitles help people stay comfortable. Keep these adjustments specific to each participant so one person's changes don't affect anyone else.

- **Make it easy to leave and rejoin** - People sometimes step away for another task or to engage with their surroundings. Give someone who exits a clear control to rejoin quickly. If your app offers a windowed version of the activity, people can keep multitasking while staying connected to the activity and FaceTime Audio.

#### Personas

How someone appears in a shared activity depends on their device and location. A remote participant on Apple Vision Pro can appear as a spatial Persona, which can make eye contact, gesture, move around, and interact with your content as if in the same room; without a Persona set up, they appear as a contact photo. Participants on iPhone, iPad, Mac, or Apple TV appear in a 2D window showing their video. People wearing Apple Vision Pro in the same room see shared content in the same physical location and see each other through passthrough.

- **Support people who aren't represented by a spatial Persona** - Some participants join from other devices, and someone on Apple Vision Pro might turn off their Persona or join over windowed FaceTime. Make sure your activity works for all of them, and if it relies on facial expressions or gestures, offer alternatives in your UI.

For developer guidance, see [Adding spatial Persona support to an activity](https://developer.apple.com/documentation/groupactivities/adding-spatial-persona-support-to-an-activity) and [Configure your visionOS app for sharing with people nearby](https://developer.apple.com/documentation/groupactivities/configure-your-app-for-sharing-with-people-nearby).

#### Spatial templates

A spatial template arranges participants around your content to suit what they're doing together. Each person gets a seat that sets where they appear and which way they face. Set [spatialTemplatePreference](https://developer.apple.com/documentation/groupactivities/systemcoordinator/configuration-swift.struct/spatialtemplatepreference) to the template that best fits your activity, or create a custom template if no system template does.

- **Side-by-side template** - Places participants next to each other along a curve, all facing the shared content. Good for watching content together; because participants don't face one another, it keeps attention on the content and invites less nonverbal interaction.

- **Surround template** - Arranges participants in a circle around the shared content. Good for tabletop games and other centralized experiences, especially when the content is 3D or differs per participant, because each person sees it from a different angle. Participants face each other, which encourages both verbal and nonverbal interaction.

- **Conversational template** - Groups participants around a center point but places your content along the edge of the circle. Not everyone has the same view of the content, so interacting with it may be awkward for some. Consider it when the experience is more about being together while your app does something in the background, like playing music.

- **Divide a complex activity into stages** - Give each stage its own template, such as one for choosing teams and another for play. Because you can transition between templates, a mix of system and custom templates is better than one complex custom template.

- **Let people initiate template transitions** - Unexpected role or seat changes are disorienting, so tie template changes to a person's explicit action, such as choosing a team in a game.

- **Keep template transitions smooth** - Avoid frequent transitions and transitions that require a lot of movement. When you move someone to a new seat or role, fade out and back in, and give visual cues that help them reorient.

#### Custom templates

When no system template suits your activity, a custom template lets you define your own seat arrangement. Seats apply only to people using a spatial Persona in visionOS; people on other platforms can take part in the same activity without a seat. For developer guidance, see [Building a guessing game for visionOS](https://developer.apple.com/documentation/groupactivities/building-a-guessing-game-for-visionos).

- **Account for people who are physically together** - People sharing a room with Apple Vision Pro see each other through passthrough, not as spatial Personas. A template can move a remote participant's Persona into a seat but can't move someone who is physically present, so if your activity depends on positions, guide people with visual cues like position markers. For developer guidance, see [Configure your visionOS app for sharing with people nearby](https://developer.apple.com/documentation/groupactivities/configure-your-app-for-sharing-with-people-nearby).

- **Orient seats for your content** - Seats face the center of your content by default, and you can set each seat's direction. For developer guidance, see [SpatialTemplateSeatElement](https://developer.apple.com/documentation/groupactivities/spatialtemplateseatelement).

- **Support the maximum number of seats** - Apple Vision Pro supports up to five spatial Personas in an activity, so include five seats when your activity allows it. Define every seat up front and keep a seat in place after someone leaves, because adding and removing seats as people come and go is disorienting. If your activity has a participant limit, such as a two-player game, consider spectator seats where others can watch and talk.

- **Place seats at least a meter apart** - This gives people room to interact comfortably. People can still share gestures like a handshake or a high five, but a spatial Persona that gets too close to another is replaced with a contact photo, which breaks the sense of presence.

- **Define the order in which people take seats** - Seats fill in the order people join, so order them to keep the arrangement balanced when only some are occupied; filling seats strictly left to right, for example, can look lopsided with only a few people.

- **Keep roles independent of seats** - Don't tie roles such as player, spectator, or team member to seat assignments, because a role has to work for everyone in the activity, including people without a seat. Let people take any open seat so they can join without delay, and reserve a specific seat only for a role that needs one, like a game host at the head of a table. For developer guidance, see [isSpatial](https://developer.apple.com/documentation/groupactivities/systemcoordinator/participantstate/isspatial) and [isNearbyWithLocalParticipant](https://developer.apple.com/documentation/groupactivities/participant/isnearbywithlocalparticipant).

### Related Technologies

- [Auto-renewable subscriptions](https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase#Auto-renewable-subscriptions) - Subscription guidance

### Developer Documentation

- [Group Activities](https://developer.apple.com/documentation/groupactivities) - Group Activities framework

### Videos

- [Share visionOS experiences with nearby people](https://developer.apple.com/videos/play/wwdc2025/318)
- [Design spatial SharePlay experiences](https://developer.apple.com/videos/play/wwdc2023/10075)
- [Add SharePlay to your app](https://developer.apple.com/videos/play/wwdc2023/10239)

## Changelog

### September 9, 2026
- Reorganized best practices, expanded visionOS guidance, and added a section on custom templates.

### December 5, 2023
- Added artwork for visionOS.

### June 21, 2023
- Updated to include guidance for visionOS.

### December 19, 2022
- Clarified guidance for helping nonsubscribers join a group activity.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/shareplay)*
