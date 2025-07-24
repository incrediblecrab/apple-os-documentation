# VoiceOver

VoiceOver is a screen reader that lets people experience your app's interface without needing to see the screen.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

By supporting VoiceOver, you help people who are blind or have low vision access information in your app and navigate its interface and content when they can't see the display.

VoiceOver is supported in apps and games built for Apple platforms. It's also supported in apps and games developed in Unity using Apple's Unity plug-ins. For related guidance, see Accessibility.

## Topics

### Best Practices

**Descriptions**

- **Provide alternative labels for all key interface elements** - VoiceOver uses alternative labels (which aren't visible onscreen) to audibly describe your app's interface. System-provided controls have generic labels by default, but you should provide more descriptive labels that convey your app's functionality.
- **Add labels to any custom elements your app defines** - Be sure to keep your descriptions up-to-date as your app's interface and content change.
- **Describe meaningful images** - If you don't describe key images in your app's content, people can't use VoiceOver to fully experience them within your app. Because VoiceOver helps people understand the interface surrounding images too, such as nearby captions, describe only the information the image itself conveys.
- **Make charts and other infographics fully accessible** - Provide a concise description of each infographic that explains what it conveys. If people can interact with the infographic to get more or different information, make these interactions available to people using VoiceOver, too.
- **Exclude purely decorative images from VoiceOver** - It's unnecessary to describe images that are decorative and don't convey useful or actionable information. Excluding these images shows respect for people's time and reduces cognitive load when they use VoiceOver.

**Navigation**

- **Use titles and headings to help people navigate your information hierarchy** - The title is the first information someone receives from an assistive technology when arriving on a page or screen in your app. Offer unique titles that succinctly describe each page's content and purpose.
- **Use accurate section headings that help people build a mental model of each page's information hierarchy** - Headings provide structure and help people understand content organization.
- **Specify how elements are grouped, ordered, or linked** - Proximity, alignment, and other visible contextual cues help sighted people perceive the relationships between elements. Examine your app for places where relationships among elements are visual only, then describe these relationships to VoiceOver.
- **Ensure VoiceOver reads elements in logical order** - VoiceOver reads elements in the same order people read content in their active language and locale. For example, in US English, this is top-to-bottom, left-to-right.
- **Inform VoiceOver when visible content or layout changes occur** - People may find an unexpected content or layout change confusing because it means their mental map of the content is no longer accurate. It's crucial to report visible changes so VoiceOver and other assistive technologies can help people update their understanding of the content.
- **Support the VoiceOver rotor when possible** - People can use an interface element called the VoiceOver rotor to navigate a document or webpage by headings, links, and other content types. You can help people navigate content in your app by identifying these elements to the rotor.

### Platform Considerations

**iOS, iPadOS, macOS, tvOS, watchOS**  
No additional considerations for iOS, iPadOS, macOS, tvOS, or watchOS.

**visionOS**  
Be mindful that custom gestures aren't always accessible. When VoiceOver is turned on in visionOS, apps and games that define custom gestures don't receive hand input by default. This ensures people can explore the interface using their voice, without an app responding to hand input at the same time. A person can opt out of this behavior by enabling Direct Gesture mode, which disables standard VoiceOver gestures and lets apps process hand input directly.

### Related Components

- [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) - Accessibility guidance
- [Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion) - Inclusive design principles

### Developer Documentation

- [Accessibility](https://developer.apple.com/documentation/accessibility) - Framework
- [VoiceOver](https://developer.apple.com/documentation/accessibility/voiceover) - VoiceOver support
- [Supporting VoiceOver in your app](https://developer.apple.com/documentation/accessibility/supporting_voiceover_in_your_app) - Implementation guidance
- [Improving accessibility support in your visionOS app](https://developer.apple.com/documentation/visionos/improving_accessibility_support_in_your_visionos_app) - visionOS guidance

### Videos

- [Writing Great Accessibility Labels](https://developer.apple.com/videos/play/wwdc2019/254/)
- [Tailor the VoiceOver experience in your data-rich apps](https://developer.apple.com/videos/play/wwdc2021/10122/)
- [VoiceOver efficiency with custom rotors](https://developer.apple.com/videos/play/wwdc2020/10116/)

## Changelog

### March 7, 2025
- New page

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/voiceover)*