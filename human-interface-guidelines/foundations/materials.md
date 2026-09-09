# Materials

A material is a visual effect that creates a sense of depth, layering, and hierarchy between foreground and background elements.

**Platforms:** iOS | iPadOS | macOS | tvOS | visionOS | watchOS

## Overview

Materials communicate hierarchy while preserving context from the background. Choose them by the role of a surface, not by a fixed color or blur level.

Liquid Glass is for the functional layer of controls and navigation. Standard materials help organize the content beneath that layer. The same visual vocabulary does not imply identical rendering or API availability on every platform.

## Topics

### Liquid Glass

Use Liquid Glass to distinguish navigation and important controls from the content they affect. Let system bars handle scrolling content and foreground legibility instead of recreating the treatment with a static image.

**Do not use glass as a general content background.** Repeated glass cards compete with navigation and weaken the separation between content and controls. An embedded slider or toggle can briefly adopt glass during interaction; that exception is not a reason to apply glass to its entire surrounding content area.

**Use Liquid Glass effects sparingly.** Prefer standard controls and navigation, which adopt the system treatment. Reserve custom glass effects for important functional elements; repeating glass backgrounds throughout a content grid weakens hierarchy. See [Applying Liquid Glass to custom views](https://developer.apple.com/documentation/swiftui/applying-liquid-glass-to-custom-views).

#### Choosing regular or clear

| Liquid Glass variant | Use | Legibility considerations |
|----------------------|-----|---------------------------|
| `regular` | The usual choice for controls, navigation, and text-heavy elements such as sidebars and popovers. | Adjusts the background's blur and luminosity to help foreground content remain readable. Scroll edge effects provide additional separation over scrolling content. |
| `clear` | Controls floating over visually rich photos or video, when preserving the media's visibility matters. | Highly translucent; choose it only when the foreground remains legible against the actual media. |

For clear glass over bright content, the HIG suggests considering a **35%-opaque dark dimming layer** behind the component. This is design guidance, not a guarantee of sufficient contrast. Check the resulting text and symbols over representative content. Do not add another dimming layer when the background is already sufficiently dark or standard AVKit playback controls supply their own.

The `regular` and `clear` variants belong to Liquid Glass. They are not interchangeable with the thicknesses of standard `Material`, and a system appearance preference is not an instruction to replace all materials with one variant.

#### Appearance and accessibility

- Test the Liquid Glass appearances the target system actually offers, alongside Reduce Transparency and Increase Contrast where available. The material can change with these preferences; do not assume a fixed amount of translucency or a particular Settings control.
- Use semantic foreground colors and validate text, icons, focus, and selected states against bright, dark, and moving backgrounds.
- Keep state understandable through labels, shapes, or other noncolor cues, and expose it to [VoiceOver](../technologies/voiceover.md).
- Check larger text and Reduce Motion as well as contrast. Custom animations and layouts need their own testing even when the material adapts automatically.

For SDK adoption and the compatibility key, see [Adopting Liquid Glass](../../liquid-glass/adopting-liquid-glass.md).

### Standard materials

Use standard materials and effects — such as blur, vibrancy, and blending modes — to convey a sense of structure in the content beneath Liquid Glass.

**Choose materials and effects based on semantic meaning and recommended usage.** Avoid selecting a material or effect based on the apparent color it imparts to your interface, because system settings can change its appearance and behavior. Instead, match the material or vibrancy style to your specific use case.

**Prefer semantic, system-defined foreground colors on materials.** Their vibrant variants adapt to context and appearance preferences. Still check the resulting contrast, especially for secondary text and fine symbols. See [Color](color.md).

**Consider contrast and visual separation when choosing a material to combine with blur and vibrancy effects.** For example, consider that:

- Thicker materials, which are more opaque, can provide better contrast for text and other elements with fine features.
- Thinner materials, which are more translucent, can help people retain their context by providing a visible reminder of the content that's in the background.

For developer guidance, see [Material](https://developer.apple.com/documentation/swiftui/material).

### Platform Considerations

#### iOS and iPadOS

Use standard ultra-thin, thin, regular, or thick materials to organize the content layer beneath Liquid Glass.

iOS and iPadOS define vibrant colors for labels, fills, and separators that are specifically designed to work with each material.

Label and fill roles provide different emphasis levels. Choose a role appropriate to the information's importance, and check contrast against the selected material. In particular, avoid quaternary labels over thin and ultra-thin materials.

- `UIVibrancyEffectStyle.label` (default, highest label contrast)
- `UIVibrancyEffectStyle.secondaryLabel`
- `UIVibrancyEffectStyle.tertiaryLabel`
- `UIVibrancyEffectStyle.quaternaryLabel` (lowest label contrast)

You can use the following vibrancy values for fills on all materials.

- `UIVibrancyEffectStyle.fill` (default)
- `UIVibrancyEffectStyle.secondaryFill`
- `UIVibrancyEffectStyle.tertiaryFill`

The system also provides the `UIVibrancyEffectStyle.separator` role for separators.

#### macOS

Choose standard materials by their semantic purpose, rather than attempting to match a particular shade. macOS also supplies vibrant versions of system colors. See [NSVisualEffectView.Material](https://developer.apple.com/documentation/appkit/nsvisualeffectview/material-swift.enum).

**Choose when to allow vibrancy in custom views and controls.** Depending on configuration and system settings, system views and controls use vibrancy to make foreground content stand out against any background. Test your interface in a variety of contexts to discover when vibrancy enhances the appearance and improves communication.

**Choose the appropriate source of background content.** Behind-window blending uses content outside the window; within-window blending uses content in the window. See [NSVisualEffectView.BlendingMode](https://developer.apple.com/documentation/appkit/nsvisualeffectview/blendingmode-swift.enum).

#### tvOS

Liquid Glass appears in navigation and system experiences. Some elements, including buttons and image views, take on the treatment when focused. Preserve recognizable [focus and selection](../inputs/focus-and-selection.md) over moving video and artwork, and test from the expected viewing distance.

Standard materials continue to organize the content layer. Their thickness controls how much underlying content remains visible.

For example, consider using standard materials in the following ways:

| Material | Recommended for |
|----------|----------------|
| ultraThin | Full-screen views that require a light color scheme |
| thin | Overlay views that partially obscure onscreen content and require a light color scheme |
| regular | Overlay views that partially obscure onscreen content |
| thick | Overlay views that partially obscure onscreen content and require a dark color scheme |

#### visionOS

In visionOS, windows generally use an unmodifiable system-defined material called glass that helps people stay grounded by letting light, the current Environment, virtual content, and objects in people's surroundings show through. Glass is an adaptive material that limits the range of background color information so a window can continue to provide contrast for app content while becoming brighter or darker depending on people's physical surroundings and other virtual content.

> **Note:** visionOS doesn't have a distinct Dark Mode setting. Instead, glass automatically adapts to the luminance of the objects and colors behind it.

**Prefer translucency to opaque window backgrounds.** Preserve awareness of the surroundings without compromising the legibility of essential content. visionOS window glass is a platform-specific material; do not treat it as a requirement to apply Liquid Glass to every spatial surface.

**If necessary, choose materials that help you create visual separations or indicate interactivity in your app.** If you need to create a custom component, you may need to specify a system material for it. Use the following examples for guidance.

- The thin material brings attention to interactive elements like buttons and selected items.
- The regular material can help you visually separate sections of your app, like a sidebar or a grouped table view.
- The thick material lets you create a dark element that remains visually distinct when it's on top of an area that uses a regular background.

To ensure foreground content remains legible when it displays on top of a material, visionOS applies vibrancy to text, symbols, and fills. Vibrancy enhances the sense of depth by pulling light and color forward from both virtual and physical surroundings.

visionOS defines three vibrancy values that help you communicate a hierarchy of text, symbols, and fills.

- Use UIVibrancyEffectStyle.label for standard text.
- Use UIVibrancyEffectStyle.secondaryLabel for descriptive text like footnotes and subtitles.
- Use UIVibrancyEffectStyle.tertiaryLabel for inactive elements, and only when text doesn't need high legibility.

#### watchOS

**Use materials to provide context in a full-screen modal view.** Because full-screen modal views are common in watchOS, the contrast provided by material layers can help orient people in your app and distinguish controls and system elements from other content. Avoid removing or replacing material backgrounds for modal sheets when they're provided by default.

### Related Components

- [Color](https://developer.apple.com/design/human-interface-guidelines/color)
- [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
- [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode)

### Developer Documentation

- [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass)
- [glassEffect(_:in:)](https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:)) - SwiftUI
- [Glass.regular](https://developer.apple.com/documentation/swiftui/glass/regular) - SwiftUI
- [Glass.clear](https://developer.apple.com/documentation/swiftui/glass/clear) - SwiftUI
- [Material](https://developer.apple.com/documentation/swiftui/material) - SwiftUI
- [UIVisualEffectView](https://developer.apple.com/documentation/uikit/uivisualeffectview) - UIKit
- [NSVisualEffectView](https://developer.apple.com/documentation/appkit/nsvisualeffectview) - AppKit

### Videos

- [Meet Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219)
- [Get to know the new design system](https://developer.apple.com/videos/play/wwdc2025/356)

## Changelog

### September 9, 2025
- Apple updated its Liquid Glass guidance.

### June 9, 2025
- Added guidance for Liquid Glass.

### August 6, 2024
- Added platform-specific art.

### December 5, 2023
- Updated descriptions of the various material types, and clarified terms related to vibrancy and material thickness.

### June 21, 2023
- Updated to include guidance for visionOS.

### June 5, 2023
- Added guidance on using materials to provide context and orientation in watchOS apps.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/materials)*
