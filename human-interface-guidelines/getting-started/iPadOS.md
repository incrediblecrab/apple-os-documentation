# Designing for iPadOS

People value the power, mobility, and flexibility of iPad as they enjoy media, play games, perform detailed productivity tasks, and bring their creations to life.

**Platforms:** iPadOS

## Overview

As you begin designing your app or game for iPad, start by understanding the following fundamental device characteristics and patterns that distinguish the iPadOS experience. Using these characteristics and patterns to inform your design decisions can help you provide an app or game that iPad users appreciate.

**Display.** iPad has a large, high-resolution display.

**Ergonomics.** People often hold their iPad while using it, but they might also set it on a surface or place it on a stand. Positioning the device in different ways can change the viewing distance, although people are typically within about 3 feet of the device as they interact with it.

**Inputs.** People can interact with iPad using Multi-Touch gestures and virtual keyboards, an attached keyboard or pointing device, Apple Pencil, or voice, and they often combine multiple input modes.

**App interactions.** Sometimes, people perform a few quick actions on their iPad. At other times, they spend hours immersed in games, media, content creation, or productivity tasks. People frequently have multiple apps open at the same time, and they appreciate viewing more than one app onscreen at once and taking advantage of inter-app capabilities like drag and drop.

**System features.** iPadOS provides several features that help people interact with the system and their apps in familiar, consistent ways.

- Multitasking
- Widgets
- Drag and drop

Start with [Design principles](design-principles.md). An iPad experience needs to work as a resizable workspace as well as a handheld, touch-first interface.

## Topics

### Best Practices

Great iPad experiences integrate the platform and device capabilities that people value most. To help your experience feel at home in iPadOS, prioritize the following ways to incorporate these features and capabilities.

- **Leverage the large display** - Take advantage of the large display to elevate the content people care about, minimizing modal interfaces and full-screen transitions, and positioning onscreen controls where they're easy to reach, but not in the way.

- **Consider viewing distance and input modes** - Use viewing distance and input mode to help you determine the size and density of the onscreen content you display.

- **Support multiple input methods** - Let people use Multi-Touch gestures, a physical keyboard or trackpad, or Apple Pencil, and consider supporting unique interactions that combine multiple input modes.

- **Adapt to changes seamlessly** - Adapt seamlessly to appearance changes — like device orientation, multitasking modes, Dark Mode, and Dynamic Type — and transition effortlessly to running in macOS, letting people choose the configurations that work best for them.

### Windowing and input

- Adapt to the space the window actually has, not a hard-coded device model or a fixed catalog of multitasking sizes. Reflow [split views](../components/split-views.md) and sidebars without losing the current selection or edit.
- Keep important content and controls clear of system window controls and safe areas. Test compact and expanded [windows](../components/windows.md), rotation, and supported external-display configurations.
- Keep touch actions usable while adding [pointer](../inputs/pointing-devices.md) precision and hover feedback. Hover must not be the only way to discover a necessary action.
- Provide discoverable [keyboard commands](../inputs/keyboards.md), meaningful focus order, and standard editing commands. Verify that commands act on the intended window.
- Treat [Apple Pencil](../inputs/apple-pencil-and-scribble.md) as a precise input option, not a prerequisite. Preserve touch and accessible alternatives, and support [drag and drop](../patterns/drag-and-drop.md) where it helps move content between tasks.

### Accessibility and validation

- Resize while using [Dynamic Type](../foundations/typography.md), long localized labels, and the onscreen keyboard. Allow the layout to change rather than shrinking text to fit.
- Check [right-to-left layouts](../foundations/right-to-left.md) and navigation order in both sidebar and compact presentations.
- Complete a task with [VoiceOver](../technologies/voiceover.md) and with keyboard-only navigation, including changing panes and dismissing a modal.
- Validate contrast and selection over [materials](../foundations/materials.md). Test Reduce Transparency and [Reduce Motion](../foundations/motion.md) without losing context during layout transitions.

### Resources

- [Design principles](design-principles.md)
- [Multitasking](../patterns/multitasking.md)
- [Apple Design Resources](https://developer.apple.com/design/resources/)

### Developer Documentation

- [iPadOS Pathway](https://developer.apple.com/ipados/get-started/)

### Videos

- [Elevate the design of your iPad app](https://developer.apple.com/videos/play/wwdc2025/208)
- [Meet Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219)
- [Get to know the new design system](https://developer.apple.com/videos/play/wwdc2025/356)

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados)*
