# Snippets

Present a compact confirmation or result for an app action without requiring people to open the full app.

**Platforms:** iOS | iPadOS | macOS

## Overview

A snippet is an App Intents view that can appear during an interaction with Siri, Spotlight, or Shortcuts. Design it around one task, such as reviewing an order or seeing the result of a lookup, rather than reproducing an app screen.

The HIG describes two types. An intent that presents a snippet always provides a result; confirmation is an optional step before that result.

## Topics

### Confirmation and result

| Type | Purpose | System-provided actions |
|------|---------|-------------------------|
| Confirmation | Review the proposed action and any choices that affect it before proceeding. | Cancel and a primary action whose label you can customize. |
| Result | Explain the outcome or show requested information without requiring another action. | Done dismisses the snippet. |

- Use a confirmation when people need to check consequential details before an action runs. Make the object, recipient, amount, or other relevant consequence clear.
- Label the primary action with a meaningful verb, such as **Order**, rather than **OK**. Do not duplicate the system's confirmation buttons inside the custom view.
- Describe the actual result, including a failure or incomplete outcome. Do not make a confirmation preview look like a completed transaction.
- Keep follow-up actions focused. For a detailed result, link to the relevant content in your app instead of expanding the snippet into a full workflow.
- Keep presentation separate from performing the action. The system may run a `SnippetIntent` repeatedly to refresh its view; rebuilding that view must not repeat a purchase, deletion, or other side effect.

### Layout and dialogue

- Keep the custom view within the HIG's **400-point maximum height**. Design for larger text before deciding how much content will fit.
- Use consistent margins, a clear hierarchy, and readable contrast against the system background in light and dark appearances.
- The system can display the intent's dialogue above the custom view. Make the visual content understandable on its own rather than depending on that text.
- Keep meaningful spoken dialogue for hands-free use even when omitting duplicated dialogue text from the visual presentation.

### Accessibility and review

- Test both confirmation and result views with [VoiceOver](../technologies/voiceover.md). Give controls meaningful labels and expose relevant values and states in a logical reading order.
- Support [Dynamic Type](../foundations/typography.md) without truncating essential consequences or hiding the primary action. Move extra detail into the app when it cannot fit.
- Do not distinguish pending, successful, and failed results only by color, animation, or material. Include concise text, and honor [Reduce Motion](../foundations/motion.md).
- Verify the cancellation path as carefully as the success path. A person who cancels a confirmation should not discover that the proposed action already happened.

### Platform considerations

The current HIG supports snippets in iOS, iPadOS, and macOS, not tvOS, visionOS, or watchOS. This is the availability of this presentation pattern, not the availability of the App Intents framework as a whole. Check individual APIs for deployment requirements.

The developer guide also specifies that intents invoked from a Control Center control cannot display snippets. Design an appropriate result path for the entrypoint rather than assuming every App Intents invocation can present one.

## Related guidance

- [App Shortcuts](app-shortcuts.md)
- [Siri](../technologies/siri.md)
- [Accessibility](../foundations/accessibility.md)
- [Feedback](../patterns/feedback.md)
- [App Intents reference](../../documentation/AppIntents.md)

## Developer documentation

- [App Intents](https://developer.apple.com/documentation/appintents)
- [Displaying static and interactive snippets](https://developer.apple.com/documentation/appintents/displaying-static-and-interactive-snippets)
- [ConfirmationActionName](https://developer.apple.com/documentation/appintents/confirmationactionname)

---

*Source: [Apple Human Interface Guidelines — Snippets](https://developer.apple.com/design/human-interface-guidelines/snippets)*
