# Siri

Make useful actions and relevant content available through concise, understandable interactions outside your app's main interface.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

People use Siri in different contexts, including hands-free situations and devices without an app screen in view. Design around the task and its outcome rather than assuming a particular visual presentation.

The current HIG describes integration with Apple Intelligence and Siri AI through App Intents. Device, system, language, and feature availability still need to be checked for the experiences you support.

## Topics

### Make actions and content discoverable

- Describe useful actions as app intents and relevant content as app entities. Use terms people already recognize from your app.
- Where a system [app schema](https://developer.apple.com/documentation/appintents/app-schema-domains) matches the action's meaning, use that shared definition rather than inventing a parallel vocabulary.
- Use [App Shortcuts](../components/app-shortcuts.md) for custom actions that fall outside the system's common schemas.
- Prioritize frequent tasks and the contexts where they help: a short hands-free action may need different defaults and feedback than a task performed while reading a screen.
- Keep advertisements and sales pitches out of responses.

### Supply useful context

- Annotate onscreen content with appropriate entities so contextual references can identify what a person is interacting with. See [Providing contextual cues to Apple Intelligence and Siri](https://developer.apple.com/documentation/appintents/providing-contextual-cues-to-apple-intelligence-and-siri).
- Make relevant entities available to Spotlight deliberately. Favorites, recent items, or other personally useful content may be more helpful than indiscriminately exposing an entire collection.
- Donate actions people actually take to help the system surface useful suggestions. Keep donated information accurate when the underlying content changes.
- Treat contextual information as personal data: follow [Privacy](../foundations/privacy.md), minimize what you share, and preserve the person's control.

### Dialogue, confirmation, and results

- Prefer the system's built-in responses when they already communicate the task. Add custom dialogue only when it improves clarity.
- Keep spoken responses short, specific, and useful on their own. Essential information must not depend on a visual snippet being present.
- Use [Snippets](../components/snippets.md) for focused confirmations and results. Review consequential details before acting, and clearly distinguish a proposed action from a completed one.
- Ask a clarifying question when the request is ambiguous. Avoid reading a very long list of choices when a question can narrow it.
- Explain a failure in terms of the actual problem and a useful next step, rather than only saying that something went wrong.
- Use device-neutral wording when possible. A request can originate on one device and affect another.

### Accessibility and editorial care

- Test dialogue without looking at the screen, and test visual results with [VoiceOver](voiceover.md), [larger text](../foundations/typography.md), and increased contrast where supported.
- Keep labels, values, and action states accessible. Optional custom properties may not appear in every response, so do not put essential meaning only in an optional visual element.
- Use inclusive wording and respect parental controls. Remember that a spoken response can be heard by people nearby.
- Refer to Siri by name, without gendered pronouns. Do not impersonate Siri or Apple, and follow Apple's editorial and trademark guidance for localized references.

### Maintaining SiriKit integrations

[Apple's SiriKit documentation](https://developer.apple.com/documentation/sirikit) explicitly retains legacy support through SiriKit, Intents, and IntentsUI for Shortcuts actions, widget configuration, and **most existing Siri interactions**. It recommends App Intents for modern integration.

This is neither a blanket SiriKit deprecation nor a guarantee that every old intent works in every new context. For an existing integration, inspect the specific APIs and migration guidance, preserve necessary legacy behavior, and test the supported devices and invocation paths.

## Related guidance

- [App Shortcuts](../components/app-shortcuts.md)
- [Snippets](../components/snippets.md)
- [Generative AI](generative-ai.md)
- [Writing](../foundations/writing.md)

## Developer documentation

- [App Intents](https://developer.apple.com/documentation/appintents)
- [Apple Intelligence and Siri AI](https://developer.apple.com/documentation/appintents/apple-intelligence-and-siri-ai)
- [Making actions and content discoverable by Apple Intelligence](https://developer.apple.com/documentation/appintents/making-actions-and-content-discoverable-by-apple-intelligence)
- [Displaying static and interactive snippets](https://developer.apple.com/documentation/appintents/displaying-static-and-interactive-snippets)
- [SiriKit](https://developer.apple.com/documentation/sirikit)

## Videos

- [Build intelligent Siri experiences with App Schemas](https://developer.apple.com/videos/play/wwdc2026/240/)
- [Explore advanced App Intents features for Siri and Apple Intelligence](https://developer.apple.com/videos/play/wwdc2026/343/)
- [Discover new capabilities in the App Intents framework](https://developer.apple.com/videos/play/wwdc2026/345/)

## Changelog

### June 8, 2026
- Apple revised the HIG for Siri AI.

### June 5, 2023
- Apple removed Add to Siri guidance and added App Shortcuts references.

### May 2, 2023
- Apple consolidated Siri guidance into one page.

---

*Sources: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/siri) and [SiriKit support guidance](https://developer.apple.com/documentation/sirikit)*
