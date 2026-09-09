# Design principles

Use these principles to decide what belongs in an experience, how it behaves, and how people recover when something goes wrong.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

Good design starts with people's goals, not a visual treatment. Apple's principles are a way to evaluate tradeoffs: a simpler screen isn't necessarily better if it hides an essential action, and an expressive animation isn't helpful if it delays a task.

## Topics

### Purpose and agency

- Identify the task your product makes easier, and give its essential content and actions priority.
- Let people explore without forcing an unnecessary setup sequence or trapping them in a mode.
- Make cancellation, navigation back, and recovery predictable. Offer [undo](../patterns/undo-and-redo.md) where an action can be reversed; use [confirmation](../components/alerts.md) when the consequences justify an interruption.

### Responsibility and familiarity

- Explain why you need information before requesting it, collect only what serves the task, and protect it throughout its use. See [Privacy](../foundations/privacy.md).
- Use familiar controls, terms, and platform conventions. A consistent action should have a consistent name and behavior.
- Show understandable [feedback](../patterns/feedback.md) for progress, success, and failure instead of making people infer what happened.

### Flexibility and simplicity

- Treat [accessibility](../foundations/accessibility.md) and [inclusion](../foundations/inclusion.md) as design inputs, not final checks.
- Preserve the current task when windows resize, text grows, the reading direction changes, or someone switches input methods.
- Establish hierarchy with layout, concise language, and recognizable actions. Removing useful labels or navigation is not the same as simplifying.
- Adapt intentionally to each platform rather than stretching one layout across every device.

### Craft and delight

- Prototype the entire interaction, including empty states, errors, interruptions, and recovery.
- Test on the devices and in the environments people will use. Refine wording, input behavior, animation, and performance together.
- Express your app's character in ways that support its purpose. Decorative motion must not obscure feedback or override Reduce Motion.
- Continue improving the experience after release as platform conventions and people's needs change.

## Getting started on each platform

Choose an entrypoint, then use the principles above to review a complete task from start to finish.

- [iOS](iOS.md): reachable controls and focused tasks on a handheld screen.
- [iPadOS](iPadOS.md): resizable windows and transitions between touch, Pencil, pointer, and keyboard.
- [macOS](macOS.md): sustained work, document windows, menus, and keyboard commands.
- [tvOS](tvOS.md): predictable focus and information readable from across a room.
- [watchOS](watchOS.md): glanceable information and brief, targeted interactions.
- [visionOS](visionOS.md): comfortable spatial placement and deliberate levels of immersion.

## Related guidance

- [Layout](../foundations/layout.md)
- [Writing](../foundations/writing.md)
- [Materials](../foundations/materials.md)
- [Interface fundamentals](../../liquid-glass/interface-fundamentals.md)

---

*Source: [Apple Human Interface Guidelines — Design principles](https://developer.apple.com/design/human-interface-guidelines/design-principles)*
