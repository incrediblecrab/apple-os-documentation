# Designing for watchOS

When people glance at their Apple Watch, they know they can access essential information and perform simple, timely tasks whether they're stationary or in motion.

**Platforms:** watchOS

## Overview

As you begin designing your app for Apple Watch, start by understanding the following fundamental device characteristics and patterns that distinguish the watchOS experience. Using these characteristics and patterns to inform your design decisions can help you provide an app that Apple Watch users appreciate.

**Display.** The small Apple Watch display fits on the wrist while delivering an easy-to-read, high-resolution experience.

**Ergonomics.** People typically view the display from within about a foot as they raise their wrist and use their other hand to interact. On models that support [Always On](../technologies/always-on.md), useful information can remain visible when the wrist is lowered.

**Inputs.** Use the [Digital Crown](../inputs/digital-crown.md) for vertical navigation and data inspection, alongside familiar tap, swipe, and drag gestures. On a supported device, the [Action button](../inputs/action-button.md) can initiate a key action; Apple Watch Ultra supports activity-related actions such as workouts and dives. Shortcuts can accelerate routine tasks. Device data such as location, heart measurements, elevation, and motion can inform useful features, but check capability and authorization rather than assuming every watch exposes every sensor or health measurement.

**App interactions.** People glance at the Always On display many times throughout the day, performing concise app interactions that can last for less than a minute each. People frequently use a watchOS app's related experiences — like complications, notifications, and Siri interactions — more than they use the app itself.

**System features.** watchOS provides several features that help people interact with the system and their apps in familiar, consistent ways.

- [Complications](../components/complications.md)
- [Notifications](../components/notifications.md)
- [Always On](../technologies/always-on.md)
- [Watch faces](../components/watch-faces.md)

Start with [Design principles](design-principles.md). Prioritize what someone can understand in a brief glance and accomplish with a small number of actions.

## Topics

### Best Practices

Great Apple Watch experiences are streamlined and specialized, and integrate the platform and device capabilities that people value most. To help your experience feel at home in watchOS, prioritize the following ways to incorporate these features and capabilities.

- **Support quick interactions** - Support quick, glanceable, single-screen interactions that deliver critical information succinctly and help people perform targeted actions with a simple gesture or two.

- **Minimize navigation depth** - Minimize the depth of hierarchy in your app's navigation, and use the Digital Crown to provide vertical navigation for scrolling or switching between screens.

- **Personalize the experience** - Personalize the experience by proactively anticipating people's needs and using on-device data to provide actionable content that's relevant in the moment or very soon.

- **Use complications** - Use complications to provide relevant, potentially dynamic data and graphics right on the watch face where people can view them on every wrist raise and tap them to dive straight into your app.

- **Deliver timely notifications** - Use notifications to deliver timely, high-value information and let people perform important actions without opening your app.

- **Use visual hierarchy** - Use background content such as color to convey useful supporting information, and use materials to illustrate hierarchy and a sense of place.

- **Design for independence** - Design your app to function independently, complementing your notifications and complications by providing additional details and functionality.

### Glanceable tasks

- Lead with one timely fact or action. Move secondary detail behind a deliberate interaction rather than compressing an entire phone dashboard onto the watch.
- Keep [complications](../components/complications.md), [widgets](../components/widgets.md), and the app consistent about the value and state they show. When an entrypoint opens the app, navigate to the relevant content rather than an unrelated starting screen.
- Provide visible feedback when the [Digital Crown](../inputs/digital-crown.md) changes a selection or value. Keep navigation shallow and use familiar scrolling behavior.
- Design the [Always On](../technologies/always-on.md) state separately: keep useful information legible at reduced luminance, consider privacy, and make stale data distinguishable from a current reading.
- Minimize typing. Use appropriate system input and concise choices rather than requiring a custom miniature keyboard.

### Accessibility and validation

- Test [Dynamic Type](../foundations/typography.md) on the smallest supported display, with long localized text. Allow information to reflow instead of making it too small to read.
- Complete the task with [VoiceOver](../technologies/voiceover.md), including Crown-driven changes, actionable notifications, and errors.
- Check [right-to-left layouts](../foundations/right-to-left.md), truncation, and the ordering of values and units.
- Test normal and dimmed presentation, sufficient contrast, and [Reduce Motion](../foundations/motion.md). Pair important haptics and color changes with understandable visual and accessible feedback.
- Preserve standard [material backgrounds](../foundations/materials.md) for modal views, and test the display and accessibility preferences available on each supported device.

### Resources

- [Design principles](design-principles.md)
- [Apple Design Resources](https://developer.apple.com/design/resources/)

### Developer Documentation

- [watchOS Pathway](https://developer.apple.com/watchos/get-started/)

### Videos

- [What's new in watchOS 26](https://developer.apple.com/videos/play/wwdc2025/334)

## Changelog

These dates describe changes to Apple's HIG article, not edits to this repository.

### June 5, 2023
- Enhanced guidance for providing a glanceable, focused app experience, and emphasized the importance of the Digital Crown in navigation.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos)*
