# Designing for tvOS

People enjoy the vibrant content, immersive experiences, and streamlined interactions that tvOS delivers in media and games, as well as in fitness, education, and home utility apps.

**Platforms:** tvOS

## Overview

As you begin designing your app or game for tvOS, start by understanding the following fundamental device characteristics and patterns that distinguish the tvOS experience. Using these characteristics and patterns to inform your design decisions can help you provide an app or game that tvOS users appreciate.

**Display.** A TV typically has a very large, high-resolution display.

**Ergonomics.** Although people generally remain many feet away from their stationary TV — often 8 feet or more — they sometimes continue to interact with content as they move around the room.

**Inputs.** People can use a remote, a game controller, their voice, and apps running on their other devices to interact with Apple TV.

**App interactions.** People can get deeply immersed in a single experience — often lasting hours — but they also appreciate using a picture-in-picture view to simultaneously follow an alternative app or video.

**System features.** Apple TV users expect their apps and games to integrate well with the following system experiences.

- Integrating with the TV app
- SharePlay
- Top Shelf
- TV provider accounts

Start with [Design principles](design-principles.md). Judge the experience from across the room, using a remote rather than a touch simulation.

## Topics

### Best Practices

Great tvOS experiences integrate the platform and device capabilities that people value most. To help your experience feel at home in tvOS, prioritize the following ways to incorporate these features and capabilities.

- **Support intuitive remote interactions** - Support powerful, delightful interactions through the fluid, familiar gestures people make with the Siri Remote.

- **Embrace the focus system** - Embrace the tvOS focus system, letting it gently highlight and expand onscreen items as people move among them, helping them know what to do and where they are at all times.

- **Create a cinematic experience** - Deliver beautiful, edge-to-edge artwork, subtle and fluid animations, and engaging audio, wrapping people in a rich, cinematic experience that's clear, legible, and captivating from across the room.

- **Enhance multiuser support** - Enhance multiuser support by making sign-in easy and infrequent, handling shared sign-in, and automatically switching profiles when people change the current viewer.

### Focus-driven interaction

- Make every actionable element reachable with directional navigation. Use the system's [focus effects](../inputs/focus-and-selection.md), and distinguish moving focus from activating an item.
- Keep focus movement predictable across rows, menus, and overlays. When a temporary view closes, return people to an understandable place in the task.
- Combine related artwork and descriptive text into a single [lockup](../components/lockups.md) when they represent one selectable item, rather than adding unnecessary focus stops.
- Preserve expected [remote](../inputs/remotes.md) selection and back behavior. Minimize text entry, and use system entry and sign-in experiences where appropriate.
- Check controls over bright, dark, and moving video. A focus treatment that works on a static solid background may not remain distinct over media or [materials](../foundations/materials.md).

### Accessibility and validation

- Use readable type and generous spacing for the viewing distance. Support [Dynamic Type](../foundations/typography.md) where available, and test enlarged text and long labels without clipping. Do not simply reuse a phone's layout at television scale.
- Test focus order, labels, playback controls, and dismissal using [VoiceOver](../technologies/voiceover.md). Include supported remote, controller, and keyboard input paths.
- Localize [right-to-left layouts](../foundations/right-to-left.md) while preserving the intended direction of media timelines and playback controls.
- Honor [Reduce Motion](../foundations/motion.md) and supported display preferences. Focus and selection must remain obvious without relying only on parallax, translucency, or color.

### Resources

- [Design principles](design-principles.md)
- [Apple Design Resources](https://developer.apple.com/design/resources/)

### Developer Documentation

- [tvOS Pathway](https://developer.apple.com/tvos/get-started/)

### Videos

- [Build SwiftUI apps for tvOS](https://developer.apple.com/videos/play/wwdc2020/10042)

## Changelog

### September 14, 2022
- Refined best practices for multiuser support.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos)*
