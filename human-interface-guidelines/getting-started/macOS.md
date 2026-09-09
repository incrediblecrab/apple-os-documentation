# Designing for macOS

People rely on the power, spaciousness, and flexibility of a Mac as they perform in-depth productivity tasks, view media or content, and play games, often using several apps at once.

**Platforms:** macOS

## Overview

As you begin designing your app or game for macOS, start by understanding the fundamental device characteristics and patterns that distinguish the macOS experience. Using these characteristics and patterns to inform your design decisions can help you provide an app or game that Mac users appreciate.

**Display.** A Mac typically has a large, high-resolution display, and people can extend their workspace by connecting additional displays, including their iPad.

**Ergonomics.** People generally use a Mac while they're stationary, often placing the device on a desk or table. In the typical use case, the viewing distance can range from about 1 to 3 feet.

**Inputs.** Support combinations of [keyboards](../inputs/keyboards.md), [pointing devices](../inputs/pointing-devices.md), [game controls](../inputs/game-controls.md), and [Siri](../technologies/siri.md), rather than assuming a single input method.

**App interactions.** Interactions can last anywhere from a few minutes of performing some quick tasks to several hours of deep concentration. People frequently have multiple apps open at the same time, and they expect smooth transitions between active and inactive states as they switch from one app to another.

**System features.** macOS provides several features that help people interact with the system and their apps in familiar, consistent ways.

- [The menu bar](../components/the-menu-bar.md)
- [File management](../patterns/file-management.md)
- [Going full screen](../patterns/going-full-screen.md)
- [Dock menus](../components/dock-menus.md)

Start with [Design principles](design-principles.md). Design for sustained work across windows and input methods, not just a larger version of a phone screen.

## Topics

### Best Practices

Great Mac experiences integrate the platform and device capabilities that people value most. To help your design feel at home in macOS, prioritize the following ways to incorporate these features and capabilities.

- **Leverage large displays** - Leverage large displays to present more content in fewer nested levels and with less need for modality, while maintaining a comfortable information density that doesn't make people strain to view the content they want.

- **Support window management** - Let people resize, hide, show, and move your windows to fit their work style and device configuration, and support full-screen mode to offer a distraction-free context.

- **Use the menu bar** - Use the menu bar to give people easy access to all the commands they need to do things in your app.

- **Enable precise interactions** - Help people take advantage of high-precision input modes to perform pixel-perfect selections and edits.

- **Support keyboard shortcuts** - Handle keyboard shortcuts to help people accelerate actions and use keyboard-only work styles.

- **Support personalization** - Support personalization, letting people customize toolbars, configure windows to display the views they use most, and choose the colors and fonts they want to see in the interface.

### Windows, menus, and precision

- Make [windows](../components/windows.md) useful at different sizes and on multiple displays. Preserve unsaved work and task context when people resize, hide, or return to a window.
- Give documents and windows understandable titles. Keep document operations, selection, and [undo](../patterns/undo-and-redo.md) scoped to the appropriate task.
- Put important commands in [the menu bar](../components/the-menu-bar.md), with conventional [keyboard shortcuts](../inputs/keyboards.md). Context menus and toolbar icons should not be the only routes to essential commands.
- Support precise [pointer interactions](../inputs/pointing-devices.md) without requiring tiny targets. Offer keyboard alternatives to drag-only operations.
- Separate navigation and tools from the content being edited. Use [materials](../foundations/materials.md) for hierarchy rather than covering document content with glass effects.

### Accessibility and validation

- Complete editing and navigation with the keyboard and [VoiceOver](../technologies/voiceover.md), including changes between windows, toolbars, and inspectors.
- Make text enlargable and layouts flexible. Follow [Typography](../foundations/typography.md) and the HIG's [larger-text guidance](../foundations/accessibility.md); do not assume a fixed desktop font size is sufficient or that every platform exposes the same Dynamic Type settings.
- Test [right-to-left layouts](../foundations/right-to-left.md), long menu labels, and localized shortcut conventions.
- Verify light, dark, and increased-contrast appearances. Respect Reduce Transparency and [Reduce Motion](../foundations/motion.md), keeping selection and status clear even when visual effects change.

### Resources

- [Design principles](design-principles.md)
- [Apple Design Resources](https://developer.apple.com/design/resources/)

### Developer Documentation

- [macOS Pathway](https://developer.apple.com/macos/get-started/)

### Videos

- [Meet Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219)
- [Get to know the new design system](https://developer.apple.com/videos/play/wwdc2025/356)
- [Build an AppKit app with the new design](https://developer.apple.com/videos/play/wwdc2025/310)

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos)*
