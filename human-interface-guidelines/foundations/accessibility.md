# Accessibility

Accessible user interfaces empower everyone to have a great experience with your app or game.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

When you design for accessibility, you reach a larger audience and create a more inclusive experience. An accessible interface allows people to experience your app or game regardless of their capabilities or how they use their devices. Accessibility makes information and interactions available to everyone. An accessible interface is:

**Intuitive.** Your interface uses familiar and consistent interactions that make tasks straightforward to perform.

**Perceivable.** Your interface doesn't rely on any single method to convey information. People can access and interact with your content, whether they use sight, hearing, speech, or touch.

**Adaptable.** Your interface adapts to how people want to use their device, whether by supporting system accessibility features or letting people personalize settings.

Audit representative tasks throughout design and development. Accessibility Inspector helps reveal issues and the information exposed to assistive technologies; verify the actual interactions as well. For describing supported features on the App Store, follow the evaluation criteria for [Accessibility Nutrition Labels](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels).

## Topics

### Vision

Test custom text, controls, and [materials](materials.md) with the display and accessibility preferences available on the target platform, including Reduce Transparency, Increase Contrast, and Reduce Motion where offered. Preserve understandable state and grouping when effects change; system adaptation does not replace testing your own colors, layout, and accessibility information.

The people who use your interface may be blind, color blind, or have low vision or light sensitivity. They may also be in situations where lighting conditions and screen brightness affect their ability to interact with your interface.

**Support larger text sizes.** Let people enlarge text and meaningful icons without losing content or functionality. Aim for at least 200% of the default text size; watchOS uses its largest Dynamic Type size, which exceeds 140% of the default. These are final sizes, not increases of another 200% or 140%. Adopt Dynamic Type where the system offers it, or provide equivalent text-size controls. See [Supporting Dynamic Type](https://developer.apple.com/design/human-interface-guidelines/typography#Supporting-Dynamic-Type) and Apple's [Larger Text evaluation criteria](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/larger-text-evaluation-criteria).

**Use recommended defaults for custom type sizes.** Each platform has different default and minimum sizes for system-defined type styles to promote readability. If you're using custom type styles, follow the recommended defaults.

| Platform | Default size | Minimum size |
|----------|--------------|--------------|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

Bear in mind that font weight can also impact how easy text is to read. If you're using a custom font with a thin weight, aim for larger than the recommended sizes to increase legibility. For more guidance, see [Typography](https://developer.apple.com/design/human-interface-guidelines/typography).

**Evaluate contrast using the correct criteria.** Test foreground text against its actual background, including light, dark, and increased-contrast appearances. For WCAG 2.2 Level AA text-contrast claims, use [Success Criterion 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html):

| Text category | Minimum contrast ratio |
|---------------|------------------------|
| Normal text, including bold text below the large-text threshold | 4.5:1 |
| Large-scale text: at least 18 CSS pt, or at least 14 CSS pt when bold | 3:1 |

The HIG's simplified table lists 3:1 for all bold text, but that is not WCAG's large-text definition. WCAG's point thresholds use CSS `pt`; don't equate them automatically with native layout points or treat every bold label as large. The criterion defines exceptions for inactive, decorative or incidental text, and logotypes. Alternate perceptual metrics are not interchangeable with WCAG contrast ratios.

Use Accessibility Inspector and Apple's [Sufficient Contrast evaluation criteria](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/sufficient-contrast-evaluation-criteria) for native-app evaluation. Those criteria allow a verified Increase Contrast appearance or suitable custom color schemes when the default is insufficient. Test the actual result; merely supporting a setting or using a semantic color doesn't certify every composition.

**Prefer system-defined colors.** These colors have their own accessible variants that automatically adapt when people adjust their color preferences, such as enabling Increase Contrast or toggling between the light and dark appearances. For guidance, see [Color](https://developer.apple.com/design/human-interface-guidelines/color).

**Convey information with more than color alone.** Some people have trouble differentiating between certain colors and shades. For example, people who are color blind may have particular difficulty with pairings such as red-green and blue-orange. Offer visual indicators, like distinct shapes or icons, in addition to color to help people perceive differences in function and changes in state. Consider allowing people to customize color schemes such as chart colors or game characters so they can personalize your interface in a way that's comfortable for them.

**Describe your app's interface and content for VoiceOver.** VoiceOver is a screen reader that lets people experience your app's interface without needing to see the screen. For more guidance, see [VoiceOver](https://developer.apple.com/design/human-interface-guidelines/voiceover).

### Hearing

The people who use your interface may be deaf or hard of hearing. They may also be in noisy or public environments.

**Provide appropriate alternatives for audio and video.** Don't communicate dialogue or essential information through sound alone. Provide text alternatives for audio, and descriptions of important visual information where appropriate. Let people customize the presentation of captions and subtitles:

- **Captions** give people the textual equivalent of audible information in video or audio-only content. Captions are great for scenarios like game cutscenes and video clips where text synchronizes live with the media.

- **Subtitles** allow people to read live onscreen dialogue in their preferred language. Subtitles are great for TV shows and movies.

- **Audio descriptions** are interspersed between natural pauses in the main audio of a video and supply spoken narration of important information that's presented only visually.

- **Transcripts** provide a complete textual description of a video, covering both audible and visual information. Transcripts are great for longer-form media like podcasts and audiobooks where people may want to review content as a whole or highlight the transcript as media is playing.

For developer guidance, see [Selecting Subtitles and Alternative Audio Tracks](https://developer.apple.com/documentation/avfoundation/selecting-subtitles-and-alternative-audio-tracks).

**Pair audio cues with other feedback.** Where haptics are supported, they can complement a success sound, error, or game event. [Music Haptics](https://developer.apple.com/documentation/mediaaccessibility/music-haptics) supplies tactile feedback for known music tracks; check whether it is active and whether the track has haptic support. It isn't a promise of haptics for every recording or device. See also [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/playing-haptics).

[Audio graphs](https://developer.apple.com/documentation/accessibility/audio-graphs) serve a different purpose: VoiceOver turns chart data into an audible representation for people who are blind or have low vision. They aren't a haptic chart API and don't replace nonaudio alternatives for people who can't hear the output.

**Augment audio cues with visual cues.** This is especially important for games and spatial apps where important content might be taking place off screen. When using audio to guide people towards a specific action, also add in visual indicators that point to where you want people to interact.

### Mobility

Ensure your interface offers a comfortable experience for people with limited dexterity or mobility.

**Offer sufficiently sized controls.** Controls that are too small are hard for many people to interact with and select. Strive to meet the recommended minimum control size for each platform to ensure controls and menus are comfortable for all when tapping and clicking.

| Platform | Default control size | Minimum control size |
|----------|---------------------|---------------------|
| iOS, iPadOS | 44x44 pt | 28x28 pt |
| macOS | 28x28 pt | 20x20 pt |
| tvOS | 66x66 pt | 56x56 pt |
| visionOS | 60x60 pt | 28x28 pt |
| watchOS | 44x44 pt | 28x28 pt |

**Consider spacing between controls as important as size.** Include enough padding between elements to reduce the chance that someone taps the wrong control. In general, it works well to add about 12 points of padding around elements that include a bezel. For elements without a bezel, about 24 points of padding works well around the element's visible edges.

**Support simple gestures for common interactions.** For many people, with or without disabilities, complex gestures can be challenging. For interactions people do frequently in your app or game, use the simplest gesture possible — avoid custom multifinger and multihand gestures — so repetitive actions are both comfortable and easy to remember.

**Offer alternatives to gestures.** Make sure your UI's core functionality is accessible through more than one type of physical interaction. Gestures can be less comfortable for people who have limited dexterity, so offer onscreen ways to achieve the same outcome. For example, if you use a swipe gesture to dismiss a view, also make a button available so people can tap or use an assistive device.

**Support spoken interaction.** Provide recognizable control labels so people can navigate, activate actions, and edit text using [Voice Control](https://developer.apple.com/documentation/accessibility/voice-control).

**Integrate with Siri and Shortcuts to let people perform tasks using voice alone.** When your app supports Siri and Shortcuts, people can automate the important and repetitive tasks they perform regularly. They can initiate these tasks from Siri, the Action button on their iPhone or Apple Watch, and shortcuts on their Home Screen or in Control Center. For guidance, see [Siri](https://developer.apple.com/design/human-interface-guidelines/siri).

**Support mobility-related assistive technologies.** Features like VoiceOver, AssistiveTouch, Full Keyboard Access, Pointer Control, and Switch Control offer alternative ways for people with low mobility to interact with their devices. Conduct testing and verify that your app or game supports these technologies, and that your interface elements are appropriately labeled to ensure a great experience. For more information, see [Performing accessibility testing for your app](https://developer.apple.com/documentation/accessibility/performing-accessibility-testing-for-your-app).

### Speech

Apple's accessibility features help people with speech disabilities and people who prefer text-based interactions to communicate effectively using their devices.

**Test keyboard-only navigation.** Preserve system shortcuts and verify that Full Keyboard Access can reach and operate the interface in a useful order. See [Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards) and [Support Full Keyboard Access in your iOS app](https://developer.apple.com/videos/play/wwdc2021/10120).

**Support Switch Control.** Check that people can navigate and perform actions with their chosen switches or other supported inputs, rather than requiring precise touch gestures. See [Switch Control](https://developer.apple.com/documentation/accessibility/switch-control).

### Cognitive

When you minimize complexity in your app or game, all people benefit.

**Keep actions simple and intuitive.** Ensure that people can navigate your interface using easy-to-remember and consistent interactions. Prefer system gestures and behaviors people are already familiar with over creating custom gestures people must learn and retain.

**Minimize use of time-boxed interface elements.** Views and controls that auto-dismiss on a timer can be problematic for people who need longer to process information, and for people who use assistive technologies that require more time to traverse the interface. Prefer dismissing views with an explicit action.

**Consider offering difficulty accommodations in games.** Everyone has their own way of playing and enjoying games. To support a variety of cognitive abilities, consider adding the ability to customize the difficulty level of your game, such as offering options for people to reduce the criteria for successfully completing a level, adjust reaction time, or enable control assistance.

**Keep playback under the person's control.** Provide discoverable start and stop controls, and respect preferences that limit autoplay or animated content. See [Animated images](https://developer.apple.com/documentation/accessibility/animated-images) and [isVideoAutoplayEnabled](https://developer.apple.com/documentation/uikit/uiaccessibility/isvideoautoplayenabled).

**Honor flashing-light accommodations.** If your app plays video, support the system's Dim Flashing Lights behavior where available. Check the relevant APIs rather than assuming a custom player handles it automatically. See [Flashing lights](https://developer.apple.com/documentation/mediaaccessibility/flashing-lights).

**Be cautious with fast-moving and blinking animations.** When you use these effects in excess, it can be distracting, cause dizziness, and in some cases even result in epileptic episodes. People who are prone to these effects can turn on the Reduce Motion accessibility setting. When this setting is active, ensure your app or game responds by reducing automatic and repetitive animations, including zooming, scaling, and peripheral motion. Other best practices for reducing motion include:

- Tightening animation springs to reduce bounce effects
- Tracking animations directly with people's gestures
- Avoiding animating depth changes in z-axis layers
- Replacing transitions in x-, y-, and z-axes with fades to avoid motion
- Avoiding animating into and out of blurs

**Optimize your app's UI for Assistive Access.** Assistive Access is an accessibility feature in iOS and iPadOS that allows people with cognitive disabilities to use a streamlined version of your app. Assistive Access sets a default layout and control presentation for apps that reduces cognitive load.

To optimize your app for this mode, use the following guidelines when Assistive Access is turned on:

- Identify the core functionality of your app and consider removing noncritical workflows and UI elements.
- Break up multistep workflows so people can focus on a single interaction per screen.
- Always ask for confirmation twice whenever people perform an action that's difficult to recover from, such as deleting a file.

For developer guidance, see [Assistive Access](https://developer.apple.com/documentation/accessibility/assistive-access).

### Platform Considerations

**visionOS**

visionOS offers a variety of accessibility features people can use to interact with their surroundings in ways that are comfortable and work best for them, including head and hand Pointer Control, and a Zoom feature.

**Prioritize comfort.** The immersive nature of visionOS means that interfaces, animations, and interactions have a greater chance of causing motion sickness, and visual and ergonomic discomfort for people. To ensure the most comfortable experience, consider these tips:

- Keep interface elements within a person's field of view. Prefer horizontal layouts to vertical ones that might cause neck strain, and avoid demanding the viewer's attention in different locations in quick succession.
- Reduce the speed and intensity of animated objects, particularly in someone's peripheral vision.
- Be gentle with camera and video motion, and avoid situations where someone may feel like the world around them is moving without their control.
- Avoid anchoring content to the wearer's head, which may make them feel stuck and confined, and also prevent them from using assistive technologies like Pointer Control.
- Minimize the need for large and repetitive gestures, as these can become tiresome and may be difficult depending on a person's surroundings.

For additional guidance, see [Create accessible spatial experiences](https://developer.apple.com/videos/play/wwdc2023/10034) and [Design considerations for vision and motion](https://developer.apple.com/videos/play/wwdc2023/10078).

### Resources

**Related**
- [Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion)
- [Typography](https://developer.apple.com/design/human-interface-guidelines/typography)
- [VoiceOver](https://developer.apple.com/design/human-interface-guidelines/voiceover)

**Developer documentation**
- [Building accessible apps](https://developer.apple.com/accessibility/)
- [Accessibility framework](https://developer.apple.com/documentation/accessibility)
- [Overview of Accessibility Nutrition Labels](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels)

**Videos**
- [Principles of inclusive app design](https://developer.apple.com/videos/play/wwdc2025/316)
- [Evaluate your app for Accessibility Nutrition Labels](https://developer.apple.com/videos/play/wwdc2025/224)
- [Refine accessibility for custom controls](https://developer.apple.com/videos/play/wwdc2026/220)

## Changelog

These dates describe changes to Apple's HIG article, not edits to this repository.

### June 9, 2025
- Added guidance and links for Assistive Access, Switch Control, and Accessibility Nutrition Labels.

### March 7, 2025
- Expanded and refined all guidance. Moved Dynamic Type guidance to the Typography page, and moved VoiceOver guidance to a new VoiceOver page.

### June 10, 2024
- Added a link to Apple's Unity plug-ins for supporting Dynamic Type.

### December 5, 2023
- Updated visionOS Zoom lens artwork.

### June 21, 2023
- Updated to include guidance for visionOS.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/accessibility)*
