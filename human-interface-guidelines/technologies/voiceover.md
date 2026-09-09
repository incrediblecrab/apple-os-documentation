# VoiceOver

VoiceOver is a screen reader that lets people experience your app's interface without needing to see the screen.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

By supporting VoiceOver, you help people who are blind or have low vision access information in your app and navigate its interface and content when they can't see the display.

VoiceOver is supported in apps and games built for Apple platforms. It's also supported in apps and games developed in Unity using Apple's Unity plug-ins. For related guidance, see Accessibility.

Expose the meaning, value, and state of controls in accessibility information rather than conveying them through material alone. Use logical grouping and reading order, and verify that the same task remains understandable when visual effects change or the screen is not visible.

## Topics

### Best Practices

**Descriptions**

- **Give key interface elements meaningful accessible names** - Standard controls often expose their visible text to VoiceOver automatically. Check those names before overriding them; add or improve an accessibility label when the existing information doesn't explain the element's purpose in your app.
- **Add labels to any custom elements your app defines** - Be sure to keep your descriptions up-to-date as your app's interface and content change.
- **Describe meaningful images** - If you don't describe key images in your app's content, people can't use VoiceOver to fully experience them within your app. Because VoiceOver helps people understand the interface surrounding images too, such as nearby captions, describe only the information the image itself conveys.
- **Make charts and other infographics fully accessible** - Provide a concise description of each infographic that explains what it conveys. If people can interact with the infographic to get more or different information, make these interactions available to people using VoiceOver, too.
- **Exclude purely decorative images from VoiceOver** - It's unnecessary to describe images that are decorative and don't convey useful or actionable information. Excluding these images shows respect for people's time and reduces cognitive load when they use VoiceOver.

**Navigation**

- **Use titles and headings to help people navigate your information hierarchy** - Offer unique titles that succinctly describe each page's content and purpose. Test initial focus and announcements so people know where they have arrived; don't assume that every screen automatically announces its title first.
- **Use accurate section headings that help people build a mental model of each page's information hierarchy** - Headings provide structure and help people understand content organization.
- **Specify how elements are grouped, ordered, or linked** - Proximity, alignment, and other visible contextual cues help sighted people perceive the relationships between elements. Examine your app for places where relationships among elements are visual only, then describe these relationships to VoiceOver.
- **Ensure VoiceOver reads elements in logical order** - Arrange and test the accessibility hierarchy for the active language and locale. In a US English layout, a top-to-bottom, left-to-right order is usually appropriate, but related content may need grouping to remain understandable.
- **Communicate meaningful content and layout changes** - An unexpected change can invalidate a person's mental map of the interface. Verify that important updates remain discoverable, and provide accessibility notifications where needed for custom content rather than announcing every decorative change.
- **Support the VoiceOver rotor when possible** - People can use an interface element called the VoiceOver rotor to navigate a document or webpage by headings, links, and other content types. You can help people navigate content in your app by identifying these elements to the rotor.

### Platform Considerations

**iOS, iPadOS, macOS, tvOS, watchOS**  
No additional considerations for iOS, iPadOS, macOS, tvOS, or watchOS.

**visionOS**  
Be mindful that custom gestures aren't always accessible. With VoiceOver active in visionOS, hand gestures normally navigate and inspect accessible elements; the system withholds hand input from the app to prevent conflicting responses. This is screen-reader navigation with spoken output, not voice-command input. A person can enable Direct Gesture mode to restore app hand input while leaving VoiceOver enabled. Provide accessible alternatives and announcements for meaningful results of custom gestures.

### Related Components

- [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) - Accessibility guidance
- [Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion) - Inclusive design principles

### Developer Documentation

- [Accessibility](https://developer.apple.com/documentation/accessibility) - Framework
- [VoiceOver](https://developer.apple.com/documentation/accessibility/voiceover) - VoiceOver support
- [Supporting VoiceOver in your app](https://developer.apple.com/documentation/uikit/supporting-voiceover-in-your-app) - Implementation guidance
- [Improving accessibility support in your visionOS app](https://developer.apple.com/documentation/visionos/improving-accessibility-support-in-your-app) - visionOS guidance

### Videos

- [Writing Great Accessibility Labels](https://developer.apple.com/videos/play/wwdc2019/254/)
- [Tailor the VoiceOver experience in your data-rich apps](https://developer.apple.com/videos/play/wwdc2021/10121)
- [VoiceOver efficiency with custom rotors](https://developer.apple.com/videos/play/wwdc2020/10116/)

## Changelog

These dates describe Apple's HIG article history.

### March 7, 2025
- New page

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/voiceover)*
