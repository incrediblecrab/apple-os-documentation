# SharePlay

SharePlay helps multiple people share activities — like viewing a movie, listening to music, playing a game, or sketching ideas on a whiteboard — while they're in a FaceTime call or Messages conversation.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS

## Overview

The system synchronizes app playback on all participating devices to support seamless media and content sharing that lets everyone enjoy the experience simultaneously. In visionOS, SharePlay helps people enjoy these experiences while they're together in the same virtual space.

When someone shares content during a FaceTime call, the system asks each participant to launch the app to begin the experience. If people don't have the app installed, the SharePlay alert encourages them to download it from the App Store.

## Topics

### Best Practices

- **Let people know that you support SharePlay** - People often expect media playback experiences to be shareable, so indicate this capability in your interface. For example, you can use the shareplay SF Symbol to identify the content or experiences in your app that support SharePlay.

- **Consider ways to help nonsubscriber participants quickly join a group activity** - If part of your app requires a subscription, you might offer temporary or provisional access to nonsubscribers or let an existing subscriber send a one-time pass to a friend.

- **Support Picture in Picture (PiP) when possible** - On iPhone and iPad, people can open a shared video in a PiP window. On a Mac, a shared video opens in a background window that people can move into the foreground when they want to watch.

- **Use the term SharePlay correctly** - You can use SharePlay as a noun and also as a verb when describing a direct action in your interface. Avoid using an adjective with SharePlay or changing the term in any way.

### Sharing Activities

An activity is an app-defined type of shareable experience. For example, an app that lets people view videos might define a separate activity for viewing each type of content.

- **Briefly describe each activity** - When people receive an invitation to participate in an activity, your description helps them understand the experience they're about to share. Write a simple, meaningful description that's short enough to avoid truncation.

- **Make it easy to start sharing an activity** - If there's no session available when people start a shareable activity, you can present UI that lets them start a group activity.

- **Help people prepare to join a session before displaying the activity** - If people must log in, download content, or make a payment before they can participate, display views that help them perform these tasks before showing the activity UI.

- **When possible, defer app tasks that might delay a shared activity** - For example, if your app needs to know a participant's profile, consider asking for this information at a convenient time, like when playback pauses or finishes.

### Platform Considerations

**visionOS**  
People expect most visionOS apps to support SharePlay. While wearing Apple Vision Pro, people choose the Spatial option in FaceTime to share content and activities with others.

In a shared activity, FaceTime can show representations of other participants — called spatial Personas — within each wearer's space, making everyone feel like they're sharing the same experience in the same place.

#### Spatial Persona Templates

- **Side-by-side template** - Places participants next to each other along a curved line segment, all facing the shared content. Good for watching media together.

- **Surround template** - Arranges participants all the way around the shared content in the center. Works especially well when the content is 3D.

- **Conversational template** - Groups participants around a center point, but places your content along the circle. Consider using this if your experience is more about people being together while your app performs a task in the background.

#### visionOS Best Practices

- **Be prepared to launch directly into your shared activity** - When one person shares your activity with others on a FaceTime call, the system minimizes friction by automatically launching your app for everyone.

- **Help people enter a shared activity together, but don't force them** - When one participant changes their level of immersion, offer others the choice to join the updated experience.

- **Smoothly update a shared activity when new participants join** - Integrate new participants without disrupting the experience for everyone else.

#### Maintaining a Shared Context

- **Make sure everyone views the same state of your app** - Avoid letting different participants view different states, as this can diminish people's sense of being together in a shared space.

- **Use Spatial Audio to enrich your shared activity** - Playing Spatial Audio can help you strengthen the realism of the shared experience.

- **Let people discover natural, social solutions to conflicts** - When conflicts can arise during your shared activity, consider implementing simple rules and letting people use these to define acceptable behavior.

- **Help people keep their private and shared content separate** - Make it easy for people to distinguish shared from unshared windows and let them drag content they want to share from a private window to a shared one.

#### Adjusting a Shared Context

- **Let people personalize their experience without changing the experience for others** - People might need to adjust various settings, like volume or subtitles, to make views and interactions accessible.

- **Consider when to give each participant a unique view of the shared content** - Some content looks best when people view it from a specific perspective.

- **Make it easy for people to exit and rejoin a shared activity** - Present a control that lets people quickly rejoin the shared activity when they need to perform unrelated tasks.

### Related Technologies

- [Auto-renewable subscriptions](https://developer.apple.com/design/human-interface-guidelines/auto-renewable-subscriptions) - Subscription guidance

### Developer Documentation

- [Group Activities](https://developer.apple.com/documentation/groupactivities) - Group Activities framework

## Changelog

### December 5, 2023
- Added artwork for visionOS.

### June 21, 2023
- Updated to include guidance for visionOS.

### December 19, 2022
- Clarified guidance for helping nonsubscribers join a group activity.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/shareplay)*