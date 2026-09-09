# Buttons

A button initiates an instantaneous action.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

Versatile and highly customizable, buttons give people simple, familiar ways to do tasks in your app. In general, a button combines three attributes to clearly communicate its function:

- **Style.** A visual style based on size, color, and shape.
- **Content.** A symbol (or icon), text label, or both that a button displays to convey its purpose.
- **Role.** A system-defined role that identifies a button's semantic meaning and can affect its appearance.

There are also many button-like components that have distinct appearances and behaviors for specific use cases, like toggles, pop-up buttons, and segmented controls.

## Topics

### Best Practices

When buttons are instantly recognizable and easy to understand, an app tends to feel intuitive and well designed.

- **Make buttons easy to target** - Leave enough space to distinguish and activate each button. The Buttons HIG gives a general hit-region reference of 44x44 pt, or 60x60 pt in visionOS. A hit region isn't the same as the visible button or icon size; also consult [platform-specific control sizing](https://developer.apple.com/design/human-interface-guidelines/accessibility#Mobility) and test the actual input method.
- **Always include a press state for a custom button** - Without a press state, a button can feel unresponsive, making people wonder if it's accepting their input.

### Style

System buttons offer a range of styles that support customization while providing built-in interaction states, accessibility support, and appearance adaptation. Different platforms define different styles that help you communicate hierarchies of actions in your app.

Choose appearance for the button's context rather than assuming every button becomes Liquid Glass after rebuilding. [Materials](https://developer.apple.com/design/human-interface-guidelines/materials) distinguishes functional controls and navigation from content. Over bright, colorful content, prefer the default monochromatic label treatment when a similar accent color would reduce contrast.

- **In general, use a button that has a prominent visual style for the most likely action in a view** - To draw people's attention to a specific button, use a prominent button style so the system can apply an accent color to the button's background. Buttons that use color tend to be the most visually distinctive, helping people quickly identify the actions they're most likely to use. Keep the number of prominent buttons to one or two per view. Presenting too many prominent buttons increases cognitive load, requiring people to spend more time considering options before making a choice.
- **Use style — not size — to visually distinguish the preferred choice among multiple options** - When you use buttons of the same size to offer two or more options, you signal that the options form a coherent set of choices. By contrast, placing two buttons of different sizes near each other can make the interface look confusing and inconsistent. If you want to highlight the preferred or most likely option in a set, use a more prominent button style for that option and a less prominent style for the remaining ones.

### Content

- **Ensure that each button clearly communicates its purpose** - Depending on the platform, a button can contain a symbol (or icon), a text label, or both to help people understand what it does.

Note: In macOS and visionOS, the system displays a tooltip after people hover over a button for a moment. A tooltip displays a brief phrase that explains what a button does; for guidance, see Offering help.

- **Try to associate familiar actions with familiar icons** - For example, people can predict that a button containing the square.and.arrow.up symbol will help them perform share-related activities. If it makes sense to use an icon in your button, consider using an existing or customized symbol. For a list of symbols that represent common actions, see Standard icons.
- **Consider using text when a short label communicates more clearly than an icon** - To use text, write a few words that succinctly describe what the button does. Using title-style capitalization, consider starting the label with a verb to help convey the button's action — for example, a button that lets people add items to their shopping cart might use the label "Add to Cart."

The general Buttons HIG currently uses title-style labels; the [Alerts HIG](https://developer.apple.com/design/human-interface-guidelines/alerts#Buttons) specifies sentence-style labels for alert actions. Follow the relevant presentation's guidance rather than treating either convention as universal.

### Role

A system button can have one of the following roles:

- **Normal.** No specific meaning.
- **Primary.** The button is the default button — the button people are most likely to choose.
- **Cancel.** The button cancels the current action.
- **Destructive.** The button performs an action that can result in data destruction.

A button's role can have additional effects on its appearance. For example, a primary button uses an app's accent color, whereas a destructive button uses the system red color.

These are HIG semantic categories, not a list of SwiftUI enum cases. For example, SwiftUI's [`ButtonRole`](https://developer.apple.com/documentation/swiftui/buttonrole) provides values such as `cancel` and `destructive`, while [`KeyboardShortcut.defaultAction`](https://developer.apple.com/documentation/swiftui/keyboardshortcut/defaultaction) supplies Return-key default activation.

- **Make the expected action easy to activate** - A Return-key default helps people confirm a choice. Completion and dismissal depend on the presentation and API; configure that behavior rather than inferring it from visual prominence.
- **Avoid surprising destructive defaults** - A prominent default can be activated before someone reads it carefully. Prefer safe defaults, while following the [alert-specific guidance](https://developer.apple.com/design/human-interface-guidelines/alerts#Buttons) for confirmations of destructive actions the person deliberately initiated.

### Platform Considerations

**iOS, iPadOS**  
- Represent ongoing work with a configured activity indicator and, when useful, an updated label such as "Checking out…". Update this state as the operation progresses rather than assuming the button detects delays. UIKit's [showsActivityIndicator](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/showsactivityindicator) displays the indicator instead of the image and respects the configured image placement.

**macOS**  
Several specific button types are unique to macOS.

**Push buttons**
- The standard button type in macOS is known as a push button. You can configure a push button to display text, a symbol, an icon, or an image, or a combination of text and image content. Push buttons can act as the default button in a view and you can tint them.
- Use a flexible-height push button only when you need to display tall or variable height content. Flexible-height buttons support the same configurations as regular push buttons — and they use the same corner radius and content padding — so they look consistent with other buttons in your interface. If you need to present a button that contains two lines of text or a tall icon, use a flexible-height button; otherwise, use a standard push button. See [NSButton.BezelStyle.flexiblePush](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/flexiblepush).
- Append an ellipsis when completing the action requires more input, not merely because another view or app opens. For example, Safari's AutoFill Edit actions open a view where people supply changes. See the more precise [menu-label guidance](https://developer.apple.com/design/human-interface-guidelines/menus#Labels).
- Consider supporting spring loading. On systems with a Magic Trackpad, spring loading lets people activate a button by dragging selected items over it and force clicking — that is, pressing harder — without dropping the selected items. After force clicking, people can continue dragging the items, possibly to perform additional actions.

**Square buttons**
- A square button (also known as a gradient button) initiates an action related to a view, like adding or removing rows in a table.
- Square buttons contain symbols or icons — not text — and you can configure them to behave like push buttons, toggles, or pop-up buttons. The buttons appear in close proximity to their associated view — usually within or beneath it — so people know which view the buttons affect.
- Use square buttons in a view, not in the window frame. Square buttons aren't intended for use in toolbars or status bars. If you need a button in a toolbar, use a toolbar item.
- Prefer using a symbol in a square button. SF Symbols provides a wide range of symbols that automatically receive appropriate coloring in their default state and in response to user interaction.
- Avoid using labels to introduce square buttons. Because square buttons are closely connected with a specific view, their purpose is generally clear without the need for descriptive text.
- See [NSButton.BezelStyle.smallSquare](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/smallsquare).

**Help buttons**
- A help button appears within a view and opens app-specific help documentation.
- Help buttons are circular, consistently sized buttons that contain a question mark. For guidance on creating help documentation, see Offering help.
- Use the system-provided help button to display your help documentation. People are familiar with the appearance of the standard help button and know that choosing it opens help content.
- When possible, open the help topic that's related to the current context. For example, the help button in the Rules pane of Mail settings opens the Mail User Guide to a help topic that explains how to change these settings. If no specific help topic applies directly to the current context, open the top level of your app's help documentation when people choose a help button.
- Include no more than one help button per window. Multiple help buttons in the same context make it hard for people to predict the result of clicking one.
- Position help buttons where people expect to find them. Use the following locations for guidance:
  - Dialog with dismissal buttons (like OK and Cancel): Lower corner, opposite to the dismissal buttons and vertically aligned with them
  - Dialog without dismissal buttons: Lower-left or lower-right corner
  - Settings window or pane: Lower-left or lower-right corner
- Use a help button within a view, not in the window frame. For example, avoid placing a help button in a toolbar or status bar.
- Avoid displaying text that introduces a help button. People know what a help button does, so they don't need additional descriptive text.

**Image buttons**
- An image button appears in a view and displays an image, symbol, or icon. You can configure an image button to behave like a push button, toggle, or pop-up button.
- Use an image button in a view, not in the window frame. For example, avoid placing an image button in a toolbar or status bar. If you need to use an image as a button in a toolbar, use a toolbar item. See Toolbars.
- Leave padding between the image and the clickable button boundary, including when that boundary is invisible. The HIG suggests about 10 pixels; don't silently convert that visual guideline into a fixed point inset at every backing scale. In general, omit a system-provided border for this image-button style; see [isBordered](https://developer.apple.com/documentation/appkit/nsbutton/isbordered).
- If you need to include a label, position it below the image button. For related guidance, see Labels.

**visionOS**  
- A visionOS button typically includes a visible background that can help people see it, and the button plays sound to provide feedback when people interact with it.
- There are three standard button shapes in visionOS. Typically, an icon-only button uses a circle shape, a text-only button uses a roundedRectangle or capsule shape, and a button that includes both an icon and text uses the capsule shape.
- visionOS buttons use different visual styles to communicate four different interaction states: Idle, Hover, Selected, and Unavailable.
- Preserve familiar hover feedback. The HIG retains an older note about buttons not supporting custom hover effects, while newer SwiftUI provides [CustomHoverEffect](https://developer.apple.com/documentation/swiftui/customhovereffect) in visionOS 2 or later. Apple's [hover-interaction guidance](https://developer.apple.com/videos/play/wwdc2025/303) describes custom control treatments. Don't interpret the older note as a platform-wide ban on custom hover effects or as permission to access raw gaze data.
- In addition to the four states, a button can also reveal a tooltip when people look at it for a brief time. In general, buttons that contain text don't need to display a tooltip because the button's descriptive label communicates what it does.
- Choose a size supported by the button's shape and content. The current HIG gives this visible-size matrix; hit-region and spacing guidance still applies:

| Shape/content | Mini, 28 pt | Small, 32 pt | Regular, 44 pt | Large, 52 pt | Extra large, 64 pt |
|---------------|-------------|--------------|----------------|--------------|--------------------|
| Circle | Yes | Yes | Yes | Yes | Yes |
| Capsule, text | — | Yes | Yes | Yes | — |
| Capsule, text and icon | — | — | Yes | Yes | — |
| Rounded rectangle | — | Yes | Yes | Yes | — |

- Prefer buttons that have a discernible background shape and fill. It tends to be easier for people to see a button when it's enclosed in a shape that uses a contrasting background fill. The exception is a button in a toolbar, context menu, alert, or ornament where the shape and material of the larger component make the button comfortably visible.
- When a button appears on top of a glass window, use the thin material as the button's background.
- When a button appears floating in space, use the glass material for its background.
- Avoid creating a custom button that uses a white background fill and black text or icons. The system reserves this visual style to convey the toggled state.
- In general, prefer circular or capsule-shape buttons. People's eyes tend to be drawn toward the corners in a shape, making it difficult to keep looking at the shape's center. The more rounded a button's shape, the easier it is for people to look steadily at it. When you need to display a button by itself, prefer a capsule-shape button.
- Provide enough space around a button to make it easy for people to look at it. Aim to place buttons so their centers are always at least 60 pts apart. If your buttons measure 60 pts or larger, add 4 pts of padding around them to keep the hover effect from overlapping. Also, it's usually best to avoid displaying small or mini buttons in a vertical stack or horizontal row.
- Choose the right shape if you need to display text-labeled buttons in a stack or row. Specifically, prefer the rounded-rectangle shape in a vertical stack of buttons and prefer the capsule shape in a horizontal row of buttons.
- Use standard controls to take advantage of the audible feedback sounds people already know. Audible feedback is especially important in visionOS, because the system doesn't play haptics.

**watchOS**  
- Inline watchOS buttons use capsule shapes and material backgrounds that contrast with their content. This isn't a statement that every toolbar button has the same shape.
- Use the toolbar to place buttons in the corners. The system adjusts the time and title around them and applies Liquid Glass to distinguish these functional controls from the content.
- Toolbar buttons automatically inherit the app's tint color. Only change the tint color when you need to convey important information, such as when a button performs a destructive action.
- Prefer buttons that span the width of the screen for primary actions in your app. Full-width buttons look better and are easier for people to tap. If two buttons must share the same horizontal space, use the same height for both, and use images or short text titles for each button's content.
- Use toolbar buttons to provide either navigation to related areas or contextual actions for the view's content. These buttons provide access to additional information or secondary actions for the view's content.
- Use the same height for vertical stacks of one- and two-line text buttons. As much as possible, use identical button heights for visual consistency.

**tvOS**  
- No additional considerations.

### Related

- [Pop-up buttons](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons)
- [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons)
- [Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles)
- [Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)
- [Location button](https://developer.apple.com/design/human-interface-guidelines/privacy#Location-button)

### Developer Documentation

- [Button](https://developer.apple.com/documentation/swiftui/button) - SwiftUI
- [UIButton](https://developer.apple.com/documentation/uikit/uibutton) - UIKit
- [NSButton](https://developer.apple.com/documentation/appkit/nsbutton) - AppKit

## Changelog

These dates describe changes to Apple's HIG article, not edits to this repository.

### December 16, 2025
- Updated guidance for Liquid Glass.

### June 9, 2025
- Updated guidance for button styles and content.

### February 2, 2024
- Noted that visionOS buttons don't support custom hover effects.

### December 5, 2023
- Clarified some terminology and guidance for buttons in visionOS.

### June 21, 2023
- Updated to include guidance for visionOS.

### June 5, 2023
- Updated guidance for using buttons in watchOS.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/buttons)*
