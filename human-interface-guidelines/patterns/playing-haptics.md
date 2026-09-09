# Playing haptics

Playing haptics can engage people's sense of touch and bring their familiarity with the physical world into your app or game.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

Depending on the platform and the device people are using, the system can play haptics in addition to visual and auditory feedback. For example, components like switches, sliders, and pickers provide feedback on supported iPhone models. Apple Watch offers predefined haptics that can be accompanied by sound. On a Mac with a Force Touch trackpad, an app can provide feedback for actions such as aligning dragged content or changing a pressure-sensitive control.

In addition to built-in haptic capabilities, some external input devices can also play haptics. For example:

- In an iPadOS, macOS, tvOS, or visionOS app or game, supported game controllers can provide haptic feedback. See [Playing Haptics on Game Controllers](https://developer.apple.com/documentation/corehaptics/playing-haptics-on-game-controllers).

- Apple Pencil Pro and compatible haptic trackpads can provide feedback with supported iPad models. Check [Apple Pencil compatibility](https://www.apple.com/apple-pencil/) and the actual accessory's capabilities.

SDK availability doesn't establish that the device or connected accessory has a haptic actuator. Check the intended output device's capabilities, respect feedback preferences, and keep the experience usable without tactile output.

## Best practices
Use system-provided haptic patterns according to their documented meanings. People recognize standard haptics because the system plays them consistently on interactions with standard controls. If the documented use case for a pattern doesn’t make sense in your app or game, avoid using the pattern to mean something else. Instead, use a generic pattern or create your own, where supported. For guidance, see Custom haptics.

Use haptics consistently throughout your app or game. It’s important to build a clear, causal relationship between each haptic and the action that causes it so people learn to associate certain haptic patterns with certain experiences. If a haptic doesn’t reinforce a cause-and-effect relationship, it can be confusing and seem gratuitous. For example, if your game plays a specific haptic pattern when a character fails to finish a mission, people associate that pattern with a negative outcome. If you use the same haptic pattern for a positive outcome like a level completion, people will be confused.

Prefer using haptics to complement other feedback in your app or game. When visual, auditory, and tactile feedback are in harmony — as they generally are in the physical world — the user experience is more coherent and can seem more natural. For example, you generally want to match the intensity and sharpness of a haptic with the intensity and sharpness of the animation it accompanies. You can also synchronize sound with haptics; for developer guidance, see Delivering Rich App Experiences with Haptics.

Avoid overusing haptics. Sometimes a haptic can feel just right when it happens occasionally, but become tiresome when it plays frequently. Doing user testing can help you discover a balance that most people appreciate. Often, the best haptic experience is one that people may not be conscious of, but miss when it’s turned off.

In most apps, prefer playing short haptics that complement discrete events. Although long-running haptics that accompany a gameplay flow can enhance the experience, long-running haptics in an app can dilute the meaning of the feedback and distract people from their task. On Apple Pencil Pro, for example, continuous or long-lasting haptics don’t tend to clarify the writing or drawing experience and can even make holding the pencil less pleasant.

Make haptics optional. Let people turn off or mute haptics, and make sure people can still enjoy your app or game without them.

Be aware that playing haptics might impact other user experiences. By design, haptics produce enough physical force for people to feel the vibration. Ensure that haptic vibrations don't disrupt experiences involving device features like the camera, gyroscope, or microphone.

## Custom haptics

Games often use custom haptics to enhance gameplay. Although it’s less common, nongame apps might also use custom haptics to provide a richer, more delightful experience.

You can design custom haptic patterns that vary dynamically, based on user input or context. For example, the impact players feel when a game character jumps from a tree can be stronger than when the character jumps in place, and substantial experiences — like a collision or a hit — can feel very different from subtle experiences like the approach of footsteps or a looming danger.

There are two basic building blocks you can use to generate custom haptic patterns.

Transient events are brief and compact, often feeling like taps or impulses; a short pulse confirming a button action is a typical design example.

Continuous events feel like sustained vibrations, such as the experience of the lasers effect in a message.

For supported custom haptics, intensity controls perceived strength and sharpness communicates a softer, rounder or crisper, more mechanical character. These are design parameters, not a promise of identical physical sensations on every output device.

By combining transient and continuous events, varying sharpness and intensity, and including optional audio content, you can create a wide range of different haptic experiences. For developer guidance, see Core Haptics.

## Platform considerations

### iOS

On supported iPhone models, you can add haptics to your experience in the following ways:

Use standard UI components — like toggles, sliders, and pickers — that play Apple-designed system haptics by default.

When it makes sense, use a feedback generator to play one of several predefined haptic patterns in the categories of notification, impact, and selection (for developer guidance, see UIFeedbackGenerator).

#### Notification

Notification haptics provide feedback about the outcome of a task or action, such as depositing a check or unlocking a vehicle.

- **Success**: Indicates that a task or action has completed.
- **Warning**: Indicates that a task or action has produced a warning of some kind.
- **Error**: Indicates that an error has occurred.

#### Impact

Impact haptics provide a physical metaphor you can use to complement a visual experience. For example, people might feel a tap when a view snaps into place or a thud when two heavy objects collide.

- **Light**: Indicates a collision between small or lightweight UI objects.
- **Medium**: Indicates a collision between medium-sized or medium-weight UI objects.
- **Heavy**: Indicates a collision between large or heavyweight UI objects.
- **Rigid**: Indicates a collision between hard or inflexible UI objects.
- **Soft**: Indicates a collision between soft or flexible UI objects.

#### Selection

Selection haptics provide feedback while the values of a UI element are changing.

- **Selection**: Indicates that a UI element's values are changing.

### macOS

With a supported Force Touch trackpad, including a compatible built-in trackpad, your app can provide the following patterns in response to the person's actions. Don't assume every product named Magic Trackpad has this capability.

| Haptic feedback pattern | Description |
|--------------------------|-------------|
| **Alignment** | Indicates the alignment of a dragged item. For example, this pattern could be used in a drawing app when the people drag a shape into alignment with another shape. Other scenarios where this type of feedback could be used might include scaling an object to fit within specific dimensions, positioning an object at a preferred location, or reaching the beginning/end or minimum/maximum of something like a scrubber in a video app. |
| **Level change** | Indicates movement between discrete levels of pressure. For example, as people press a fast-forward button on a video player, playback could increase or decrease and haptic feedback could be provided as different levels of pressure are reached. |
| **Generic** | Intended for providing general feedback when the other patterns don't apply. |

Use [NSHapticFeedbackPerformer](https://developer.apple.com/documentation/appkit/nshapticfeedbackperformer) for user-initiated feedback. Its default performer accounts for the current input device, accessibility settings, and preferences; don't use these patterns for unrelated background events.

### watchOS
Apple Watch Series 4 and later supports Digital Crown haptics. The crown sequencer enables linear feedback by default, but apps and user preferences can affect whether it plays. Table scrolling can coordinate feedback with new rows. See [isHapticFeedbackEnabled](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/ishapticfeedbackenabled).

The HIG describes these standard patterns. This isn't an exhaustive list of every [WKHapticType](https://developer.apple.com/documentation/watchkit/wkhaptictype), which also includes navigation-specific patterns:

- **Notification**: Signals an event needing attention. This is the system notification pattern, not a guarantee that every delivered notification produces tactile feedback.
- **Up**: An important value increased or crossed an upper threshold.
- **Down**: An important value decreased or crossed a lower threshold.
- **Success**: An action completed successfully.
- **Failure**: An action failed.
- **Retry**: A failed action can be attempted again.
- **Start**: An explicitly started activity began.
- **Stop**: A previously started activity ended.
- **Click**: Marks discrete progress or intervals; avoid rapid, overlapping clicks that lose their meaning.

## Resources

### Related

- [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback)
- [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures)

### Developer documentation

- [Core Haptics](https://developer.apple.com/documentation/corehaptics)
- [UIFeedbackGenerator](https://developer.apple.com/documentation/uikit/uifeedbackgenerator) - Choose an appropriate concrete generator subclass
- [Playing haptic feedback in your app](https://developer.apple.com/documentation/applepencil/playing-haptic-feedback-in-your-app) - SwiftUI, UIKit, and Apple Pencil feedback
- [CHHapticEngine.capabilitiesForHardware()](https://developer.apple.com/documentation/corehaptics/chhapticengine/capabilitiesforhardware()) - Device-engine capability checks

### Videos

- [Practice audio haptic design](https://developer.apple.com/videos/play/wwdc2021/10278)
- [Introducing Core Haptics](https://developer.apple.com/videos/play/wwdc2019/520)

## Changelog

These dates describe Apple's HIG article history.

### May 7, 2024
- Added guidance for playing haptics on Apple Pencil Pro.

### June 21, 2023
- Updated to include guidance for visionOS.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/playing-haptics)*
