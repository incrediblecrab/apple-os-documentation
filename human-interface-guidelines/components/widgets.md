# Widgets

A widget elevates and displays a small amount of timely, relevant information from your app or game so people can see it at a glance in additional contexts.

**Platforms:** iOS | iPadOS | macOS | visionOS | watchOS

## Overview

Widgets offer focused information and, in supported contexts, simple actions without opening the app. They aren't miniature replacements for the app's complete interface.

Placement depends on the platform and widget family. iPhone and iPad offer Home Screen, Today View, and Lock Screen contexts; Mac offers the desktop and Notification Center. Apple Watch presents widgets in its Smart Stack. visionOS 26 adds spatially placed widgets, and CarPlay with iOS 26 supports small system widgets.

People choose widgets through the system's platform-specific gallery and editing interface. Configuration, such as selecting a Weather location, isn't necessarily performed in the gallery itself. Supported iPhone widgets can also appear on Mac through Continuity. On Apple Watch, people can add, remove, rearrange, and pin Smart Stack widgets; don't apply the iPhone stack limit to Watch.

On iPhone and iPad, people can stack same-size Home Screen widgets. Apple's [iPhone instructions](https://support.apple.com/en-us/118610) specify up to 10 widgets per stack. Smart Rotate and Widget Suggestions are optional: suggestions can appear when relevant, and people can add one to keep it in the stack. These Home Screen stacks aren't Lock Screen accessory widgets. See also the [iPad widget guide](https://support.apple.com/guide/ipad/add-edit-and-remove-widgets-ipadb0de8630/ipados).

Widgets range from compact accessory families to large system families. A symbol's SDK availability alone doesn't establish every place its family can appear.

System-family contexts include:

| Widget family | iPhone | iPad | Mac | visionOS |
| --- | --- | --- | --- | --- |
| System small | Home Screen, Today View, StandBy; also CarPlay | Home Screen, Today View, Lock Screen | Desktop, Notification Center | Spatial placement |
| System medium | Home Screen, Today View | Home Screen, Today View | Desktop, Notification Center | Spatial placement |
| System large | Home Screen, Today View | Home Screen, Today View | Desktop, Notification Center | Spatial placement |
| System extra large | Not a regular iPhone placement | Home Screen, Today View | Desktop, Notification Center | Compatible iPhone/iPad widgets map to portrait; native apps use the portrait family |
| System extra large portrait | Home Screen and Today View, iOS 27 beta | Today View, iPadOS 27 beta | Desktop, macOS 27 beta | Native portrait family from visionOS 26 |

The portrait row follows the current [`systemExtraLargePortrait`](https://developer.apple.com/documentation/widgetkit/widgetfamily/systemextralargeportrait) declaration and its documented contexts, including the 27 beta additions. The [`systemExtraLarge`](https://developer.apple.com/documentation/widgetkit/widgetfamily/systemextralarge) documentation distinguishes native visionOS widgets from compatible iPhone/iPad widgets; don't assume one extra-large orientation rule applies to both.

Accessory-family contexts include:

| Widget family | iPhone | iPad | Apple Watch |
| --- | --- | --- | --- |
| Accessory circular | Lock Screen | Lock Screen | Complications and Smart Stack |
| Accessory corner | — | — | Complications |
| Accessory rectangular | Lock Screen | Lock Screen | Complications and Smart Stack |
| Accessory inline | Lock Screen | Lock Screen | Complications |

## Topics

### Best Practices

- **Look for a simple idea that's clearly related to your app's main purpose** - The first step in the design process is to choose a single idea for your widget. Throughout the process, use that idea to help you include only the most relevant content and functionality in the widget. For example, people who use the Weather app are often most interested in the current high and low temperatures and weather conditions, so the widget for Weather prioritizes this information.

- **In each size, display only the information that's directly related to the widget's main purpose** - In larger widgets, you can display more data — or more detailed visualizations of the data — but you don't want to lose sight of the widget's primary purpose. For example, all Calendar widgets display a person's upcoming events. In each size, the widget remains centered on events while expanding the range of information as the size increases.

- **Offer your widget in multiple sizes when doing so adds value** - In general, avoid simply expanding a smaller widget's content to fill a larger area. It's more important to create one widget in the size that works best for the content you want to display than it is to provide the widget in all sizes.

- **Aim to create a widget that gives people quick access to the content they want** - People appreciate widgets that display meaningful content and offer useful actions and deep links to key areas of your app. When a widget merely behaves like an app icon, it offers little additional value and people may be less likely to keep it on their screens.

- **Prefer timely information** - Choose content that remains useful between updates. Avoid implying a fixed refresh interval: system-rendered dates and timers can change without requesting a new timeline.

- **Look for opportunities to surprise and delight** - For example, you might design a unique visual treatment for your calendar widget to display on meaningful occasions, like birthdays or holidays.

- **Let people know when authentication adds value** - If your widget provides additional functionality when someone is signed in to your app, make sure people know that. For example, an app that shows upcoming reservations might include a message like "Sign in to view reservations" when people are signed out.

### Updating Widget Content

A widget extension isn't continuously running, even while its widget is visible. Use timelines, appropriate reload requests, and supported WidgetKit push updates rather than continuous polling. The system budgets updates; push notifications supplement timelines and don't guarantee immediate delivery.

- **Match updates to the information** - Plan predictable changes in a timeline and request reloads when appropriate. Show an update time when freshness matters, rather than presenting old information as current. See [Keeping a widget up to date](https://developer.apple.com/documentation/widgetkit/keeping-a-widget-up-to-date).

- **Use system functionality to refresh dates and times in your widget** - Widget update frequency is limited, and you can preserve some of your update opportunities by letting the system refresh date and time information.

- **Provide useful Smart Stack relevance information** - Describe when your content is relevant so the system can consider surfacing it. Relevance is a signal, not a guarantee of placement, and must respect people's settings. See [RelevanceKit](https://developer.apple.com/documentation/relevancekit).

- **Show content quickly** - When you determine the update frequency that fits with the data you display, you don't need to hide stale data behind placeholder content.

- **Use brief transitions for meaningful changes** - Supported widget animations have a maximum duration of two seconds. Widgets and Live Activities don't animate in reduced-luminance Always On presentations. Respect Reduce Motion and check the target OS behavior; older systems have different animation support. See [Animating data updates](https://developer.apple.com/documentation/widgetkit/animating-data-updates-in-widgets-and-live-activities).

- **Consider a Live Activity for a bounded ongoing event** - On supported platforms, a Live Activity can keep an event's changing status visible. Its SwiftUI presentation can share code with widgets, but [ActivityKit](https://developer.apple.com/documentation/activitykit) manages a different lifecycle and update mechanism. Neither feature is an unrestricted real-time stream.

### Configuring Widgets

In some cases, people need to edit a widget to ensure it displays the information that's most useful for them. For example, people choose a stock symbol for a Stocks widget. In contrast, some widgets — like the Podcasts widget — automatically display recent content, so people don't need to customize them.

- **Keep configuration focused** - Offer a small set of useful choices with sensible defaults. With App Intents configuration, the system builds editing UI from your `WidgetConfigurationIntent` parameters; your app still supplies the intent, available choices, and timeline provider. Older deployment targets can use the appropriate SiriKit-based configuration rather than assuming SiriKit is universally deprecated. See [Making a configurable widget](https://developer.apple.com/documentation/widgetkit/making-a-configurable-widget).

### Adding Interactivity to Widgets

Where the family and presentation context support interactivity, App Intent-backed buttons and toggles can perform a focused action without launching the app. Use links for navigation instead of making an action button merely open the app. Check the actual supported families and contexts in [Adding interactivity to widgets and Live Activities](https://developer.apple.com/documentation/widgetkit/adding-interactivity-to-widgets-and-live-activities); don't infer identical support for every complication, Smart Stack widget, or vehicle.

- **Offer simple, relevant functionality in a widget, reserving complex functionality for your app** - Useful widgets offer an easy way to complete a task or action that's directly related to its content.

- **Deep link to the relevant destination when launching is supported** - Open the matching content rather than an unrelated landing screen. Use one `widgetURL(_:)` per widget view hierarchy; supported families can add `Link` targets. Multiple `widgetURL` modifiers have undefined behavior. CarPlay has additional restrictions described below. See [Linking to specific app scenes](https://developer.apple.com/documentation/widgetkit/linking-to-specific-app-scenes-from-your-widget-or-live-activity).

- **Keep interaction targets clear and limited** - Avoid dense app-like controls. Give each supported target enough space, an understandable label, and useful feedback. Confirm consequential actions where appropriate, not every routine Watch interaction. An inline accessory widget has a single tap target.

### Interface Design

Widgets use vivid colors, rich images, and clear, crisp text that's easy to read at a glance. A unique, beautiful widget not only provides useful information, it can encourage people to feature it on their devices.

- **Help people recognize your widget by including design elements linked to your brand's identity** - Design elements like brand colors, typeface, and stylized glyphs can make a widget instantly recognizable. Take care to keep brand-related design elements from crowding out useful information or making your widget look out of place in its context.

App-name labels vary by context and appearance. Test the widget in its actual placement instead of relying on a universal caption rule.

- **Consider carefully before displaying a logo, wordmark, or app icon in your widget** - When you include brand-related design elements like colors and fonts, people seldom need your logo or app icon to help them recognize your widget. Also, the widget gallery displays your app name and icon when it lists the various types and sizes of widgets you offer. In some widgets — for example, those that display content from multiple sources — it may make sense to include a small logo in the top-right corner to subtly identify the app that provides the widget.

- **Aim for a comfortable density of information** - When content appears sparse, the widget can seem unnecessary; when content is too dense, the widget isn't glanceable. If you have lots of information to include, avoid letting your widget become a collage of items that are difficult to parse. Seek ways to curate the content so that people can grasp the essential parts instantly and view relevant details at a longer look. You might also consider creating a larger widget and looking for places where you can replace text with graphics without losing clarity.

- **Use color judiciously** - Beautiful colors draw the eye, but they're best when they don't prevent people from absorbing a widget's information at a glance. Use color to enhance a widget's appearance without competing with its content. In your asset catalog, you can also specify the colors you want the system to use as it generates your widget's editing-mode user interface.

- **Avoid mirroring your widget's appearance within your app** - If your app displays an element that looks like your widget but doesn't behave like it, people can be confused when the element responds differently when they interact with it. Also, people may be less likely to try other ways to interact with such an element in your app because they expect it to behave like a widget.

### Scaling Content and Using Margins and Padding

Widgets scale to adapt to the screen sizes of different devices and onscreen areas. Ensure that your widget looks great on every device by supplying content at appropriate sizes.

- **Use flexible layouts and test each context** - System sizing and scaling don't guarantee that a dense design remains readable. Use the specifications as design references, not fixed production geometry. Inspect the family and available size, and test localization, larger text, and supported appearances.

- **Coordinate shapes with their container** - [`ContainerRelativeShape`](https://developer.apple.com/documentation/swiftui/containerrelativeshape) derives an inset of the current container shape; without one, it becomes a rectangle. Use it where appropriate instead of hardcoding a radius for every widget context.

The HIG specifies the Large through AX5 Dynamic Type range for widgets on iOS, iPadOS, and visionOS. Use scalable system or custom fonts and verify that important text and actions remain accessible throughout that range.

- **Start with system content margins** - WidgetKit applies context-dependent margins; read [`widgetContentMargins`](https://developer.apple.com/documentation/swiftui/environmentvalues/widgetcontentmargins) when adapting a layout. The HIG's typical 16-point margin and tighter 11-point examples are design guidance, not universal constants. Don't automatically add another 16 points on top of system margins.

### Displaying Text in Widgets

- **Consider using the system font, text styles, and SF Symbols** - Using the system font helps your widget look at home on its platform and supports coordinated weights, styles, and sizes. Use SF Symbols where suitable to align and scale symbols with text. If you need a custom font, use it sparingly and verify glanceability; a distinctive headline can work alongside smaller labels in the platform's system font. For guidance, see Typography and SF Symbols.

- **Avoid using very small font sizes** - In general, display text using fonts at 11 points or larger. Text in a font that's smaller than 11 points can be too hard for many people to read.

- **Preserve semantic text and accessible meaning** - Prefer text views so content can scale and remain available to assistive technologies. Rasterized text needs an appropriate accessible alternative; an image can have an accessibility label, so rasterization doesn't inherently make VoiceOver speech impossible. Don't rely on OCR to recover essential content.

### Supporting Different Appearances and Modes

For every appearance, a unique, beautiful widget not only provides useful information, it can encourage people to feature it on their devices. Depending on the context in which they appear, widgets can look different. For example:

- Color varies from vivid colors to tinted, monochrome colors.
- Images vary from rich, full-color images, to monochrome images, to symbols and glyphs only.

For example, a small system widget appears as follows:

- On the Home Screen of iPhone and iPad, widgets can use full-color light/dark appearances or an accented treatment for supported clear and tinted styles.
- On the Lock Screen of iPad, the widget takes on a vibrant appearance.
- In StandBy, small widgets are enlarged and ordinarily use full color with the background removed. Low-light Night mode applies a red treatment; don't assume all StandBy presentations use the same rendering mode.
- In Notification Center in macOS, widgets can use full-color light/dark appearances; account for the actual system presentation rather than assuming one permanent style.
- On the desktop on Mac, the appearance can depend on context and the person's widget-style settings. Don't assume interacting with another app always forces every widget into a monochrome presentation.
- In CarPlay, a small widget uses full color with its removable background omitted.
- In visionOS, widgets normally use full color; a tinted customization uses accented rendering.

Similarly, a rectangular accessory widget appears as follows:
- On the Lock Screen of iPhone and iPad, it takes on a vibrant appearance.
- On Apple Watch, the widget can appear as a watch complication in both full-color and tinted appearances, and it can also appear in the Smart Stack.

The system chooses a rendering mode according to the family and context. Read [`widgetRenderingMode`](https://developer.apple.com/documentation/widgetkit/widgetrenderingmode) and design for its actual result; a family doesn't support every appearance in every placement.

| Mode | Meaning for the design |
| --- | --- |
| Full color | Preserve meaningful color and imagery while supporting the applicable light/dark appearance. |
| Accented | The system styles primary and accent groups, rather than simply preserving every nonaccented view's original color. |
| Vibrant | Content participates in a reduced-color, material-based treatment; establish hierarchy and contrast without relying on hue. |

Current WidgetKit guidance explicitly includes accented and clear treatments on Mac. The HIG's platform rendering table conflicts with that guidance, so its “not supported” Mac accented entry isn't a reliable current SDK restriction. See [Preparing widgets for additional contexts and appearances](https://developer.apple.com/documentation/widgetkit/preparing-widgets-for-additional-contexts-and-appearances).

- **Support Dark Mode** - Ideally, a widget looks great in both the light and dark appearances. In general, avoid displaying dark text on a light background for the dark appearance, or light text on a dark background for the light appearance. When you use the semantic system colors for text and backgrounds, the colors dynamically adapt to the current appearance. You can also support different appearances by putting color variants in your asset catalog. For guidance, see Dark Mode; for developer guidance, see Asset management and Supporting Dark Mode in your interface.

- **Support StandBy and Night mode** - StandBy displays two small system widgets side by side. Favor larger, glanceable content. Group the background with `containerBackground(for: .widget)` so the system can remove it where appropriate, rather than painting an unwanted foreground-colored box. Verify contrast when Night mode applies a red treatment.

- **Prepare assets for vibrant rendering** - In contexts that use vibrancy, pixel opacity influences the material effect, and transparent areas reveal the background. Prefer opaque grayscale values for hierarchy instead of assuming translucent white behaves identically. Test meaningful images, numbers, and labels against varied backgrounds; a darker gray can lose contrast even when it looks satisfactory on a single wallpaper.

To make sure images look great in the vibrant rendering mode:
- Confirm that image content has sufficient contrast in grayscale.
- Use opaque grayscale values, rather than opacities of white, to achieve the best vibrant material effect.

- **Test the Mac's actual rendering modes** - Prepare for full color, vibrancy, and supported accented treatments according to context and settings. Receding content still needs sufficient contrast. Test iPhone widgets displayed on Mac as well as native Mac widgets; don't assume every switch to another app triggers the same appearance.

#### Accented Widgets

In iOS 18 and later and iPadOS 18 and later, people can select a tint color on the Home Screen. The system applies the selected tint color to widgets and app icons on the Home Screen and in the Today View, similar to how the system applies a tint color to complications on the watch face.

Accented rendering separates content into primary and accent groups. `widgetAccentable(_:)` selects the accent group; the system still styles both groups. A nonaccented view isn't automatically exempt from tinting. Clear and tinted user appearances use the existing accented rendering mode, not a fourth mode. See [Optimizing for accented rendering and Liquid Glass](https://developer.apple.com/documentation/widgetkit/optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass).

- **Use full-color images selectively** - [`Image.widgetAccentedRenderingMode(_:)`](https://developer.apple.com/documentation/swiftui/image/widgetaccentedrenderingmode(_:)) controls an image's accented treatment. Full-color artwork can help recognition, but shouldn't overwhelm surrounding information; keeping it smaller than the whole widget is design guidance, not a universal API size limit. The full-color image treatment is ignored in watchOS. Test grouping carefully because an accentable parent can conflict with the image modifier.

- **Convey meaning without relying on specific colors to represent information** - Someone may choose a color that changes the purpose of the information you're showing. In watchOS, the system may invert colors depending on the watch face a person chooses.

### Previews and Placeholders

- **Design a realistic preview to display in the widget gallery** - Highlighting your widget's capabilities — and clearly representing the experiences each widget type or size can provide — helps people make an informed decision. You can display real data in your widget preview, but if the data takes too long to generate or load, display realistic simulated data instead.

- **Provide a recognizable placeholder when requested** - Use stable layout and redacted shapes to communicate the widget's structure before personalized content is available. Don't assume every refresh must replace useful cached content with a loading placeholder.

- **Write a succinct description of your widget** - The widget gallery displays descriptions that help people understand what each widget does. It generally works well to begin a description with an action verb — for example, "See the current weather conditions and forecast for a location" or "Keep track of your upcoming events and meetings." Avoid including unnecessary phrases that reference the widget itself, like "This widget shows…," "Use this widget to…," or "Add this widget." Use approachable language and sentence-style capitalization.

- **Group your widget's sizes together, and provide a single description** - If your widget is available in multiple sizes, group the sizes together so people don't think each size is a different widget. Provide a single description of your widget — regardless of how many sizes you offer — to avoid repetition and to help people understand how each size provides a slightly different perspective on the same content and functionality.

### Platform Considerations

#### iOS and iPadOS

Widgets on the Lock Screen are functionally similar to watch complications and follow design principles for Complications in addition to design principles for widgets. Provide useful information in your Lock Screen widget, and don't treat it only as an additional way for people to launch into your app. Additionally, the vibrant rendering mode that widgets on the Lock Screen use is similar to the accented rendering mode for watch complications because they both communicate information without relying on color only. In many cases, a design for complications also works well for widgets on the Lock Screen (and vice versa), so consider creating them in tandem.

The Lock Screen supports inline, circular, and rectangular accessory families. Don't assume iPhone and iPad use the same arrangement in every orientation; iPad also has a small system-family Lock Screen context.

Support Always-On display on iPhone. Devices with Always-On display render widgets on the Lock Screen with reduced luminance. Use levels of gray that provide enough contrast in Always-On display, and make sure your content is legible.

See [Creating accessory widgets and watch complications](https://developer.apple.com/documentation/widgetkit/creating-accessory-widgets-and-watch-complications).

#### CarPlay

Prepare the small system family with a removable background, generous readable text, and driving-appropriate information. Supporting widgets doesn't itself require a CarPlay app entitlement, but opening an app in CarPlay requires a supported CarPlay integration.

In touchscreen vehicles, supported buttons and toggles can perform actions; a widget can open the corresponding CarPlay app when that integration exists. Without a touchscreen, widget controls and widget-to-app launching are inactive. Never design an interaction that requires handling the connected iPhone while driving.

Mark an unsuitable context with `disfavoredLocations` rather than assuming this hides the widget completely. Apple's June 2026 CarPlay guide says people can still choose such a widget, but its interaction is disabled. See [Adding StandBy and CarPlay support](https://developer.apple.com/documentation/widgetkit/adding-standby-and-carplay-support-to-your-widget) and the [CarPlay Developer Guide](https://developer.apple.com/download/files/CarPlay-Developer-Guide.pdf).

#### macOS

Test desktop and Notification Center placements, widget-style preferences, and available background treatments. Native Mac widgets use macOS font metrics; iPhone widgets shown on Mac use iOS metrics. Don't assume the same nominal font choice produces identical spacing. Keep content legible when a background recedes or is removed.

#### visionOS

Spatial widgets can be mounted on horizontal or vertical surfaces and remain placed between uses. Preserve a clear visual hierarchy at different sizes, viewing distances, and lighting conditions.

- **Adapt to distance.** Read the `levelOfDetail` environment value: `.default` is the normal nearby presentation, while `.simplified` calls for fewer, larger elements farther away. The HIG recommends removing interaction controls in the simplified presentation. Don't substitute an invented fixed distance threshold.
- **Allow comfortable scaling.** People can scale widgets from 75% to 125%. The reference dimensions below use 100%; they aren't device-pixel measurements.
- **Choose supported mounting styles deliberately.** Elevated widgets work on horizontal or vertical surfaces; recessed widgets require a vertical surface. The API supports both styles by default, although the HIG describes elevated as the default presentation. Use the configuration modifier `supportedMountingStyles(_:)` to restrict the set; a recessed-only configuration can't be placed horizontally. Different support sets need separate configurations.
- **Test frame variations.** People can change the system frame width. Layouts can't query the selected frame width, so don't depend on one particular border measurement.
- **Use the appropriate texture.** Native visionOS widgets use glass by default and can select paper with the configuration modifier `widgetTexture(_:)`. Paper responds to ambient lighting; glass treats the foreground separately from the background. Neither choice removes the need to test contrast. If a design depends on blend modes interacting with the container background, the developer guide directs it to paper rather than glass.

See [Updating your widgets for visionOS](https://developer.apple.com/documentation/widgetkit/updating-your-widgets-for-visionos).

#### watchOS

Design for brief glances and the Smart Stack's limited space. Its default background is a dark material, not a guaranteed pure-black fill. Use a custom background only when it adds meaning, and don't depend on red/green alone to communicate a value or trend. See [Displaying the right widget background](https://developer.apple.com/documentation/widgetkit/displaying-the-right-widget-background).

People can add, remove, reorder, and pin widgets using the [Smart Stack interface](https://support.apple.com/guide/watch/see-widgets-in-the-smart-stack-apdecf142fb9/watchos). Keep VoiceOver labels, focus order, and Crown-based browsing useful; a widget shouldn't require a dense set of precise targets.

#### tvOS

The HIG doesn't define a tvOS WidgetKit widget presentation. This isn't a claim about every similarly named interface or API.

### Specifications

These are selected published HIG design-reference entries, not an exhaustive current device catalogue or fixed production constraints. They don't provide dimensions for every newer device or the 27 beta portrait-family contexts. Use adaptive layout and the actual widget context; preserve the distinction between iPad design canvas and displayed device sizes.

#### iOS widget dimensions

| Screen size (portrait, pt) | Small (pt) | Medium (pt) | Large (pt) | Circular (pt) | Rectangular (pt) | Inline (pt) |
| --- | --- | --- | --- | --- | --- | --- |
| 430×932 | 170x170 | 364x170 | 364x382 | 76x76 | 172x76 | 257x26 |
| 428x926 | 170x170 | 364x170 | 364x382 | 76x76 | 172x76 | 257x26 |
| 414x896 | 169x169 | 360x169 | 360x379 | 76x76 | 160x72 | 248x26 |
| 414x736 | 159x159 | 348x157 | 348x357 | 76x76 | 170x76 | 248x26 |
| 393x852 | 158x158 | 338x158 | 338x354 | 72x72 | 160x72 | 234x26 |
| 390x844 | 158x158 | 338x158 | 338x354 | 72x72 | 160x72 | 234x26 |
| 375x812 | 155x155 | 329x155 | 329x345 | 72x72 | 157x72 | 225x26 |
| 375x667 | 148x148 | 321x148 | 321x324 | 68x68 | 153x68 | 225x26 |
| 360x780 | 155x155 | 329x155 | 329x345 | 72x72 | 157x72 | 225x26 |
| 320x568 | 141x141 | 292x141 | 292x311 | N/A | N/A | N/A |

#### iPadOS widget dimensions

| Screen size (portrait, pt) | Target | Small (pt) | Medium (pt) | Large (pt) | Extra large (pt) |
| --- | --- | --- | --- | --- | --- |
| 768x1024 | Canvas | 141x141 | 305.5x141 | 305.5x305.5 | 634.5x305.5 |
| | Device | 120x120 | 260x120 | 260x260 | 540x260 |
| 744x1133 | Canvas | 141x141 | 305.5x141 | 305.5x305.5 | 634.5x305.5 |
| | Device | 120x120 | 260x120 | 260x260 | 540x260 |
| 810x1080 | Canvas | 146x146 | 320.5x146 | 320.5x320.5 | 669x320.5 |
| | Device | 124x124 | 272x124 | 272x272 | 568x272 |
| 820x1180 | Canvas | 155x155 | 342x155 | 342x342 | 715.5x342 |
| | Device | 136x136 | 300x136 | 300x300 | 628x300 |
| 834x1112 | Canvas | 150x150 | 327.5x150 | 327.5x327.5 | 682x327.5 |
| | Device | 132x132 | 288x132 | 288x288 | 600x288 |
| 834x1194 | Canvas | 155x155 | 342x155 | 342x342 | 715.5x342 |
| | Device | 136x136 | 300x136 | 300x300 | 628x300 |
| 954x1373 * | Canvas | 162x162 | 350x162 | 350x350 | 726x350 |
| | Device | 162x162 | 350x162 | 350x350 | 726x350 |
| 970x1389 * | Canvas | 162x162 | 350x162 | 350x350 | 726x350 |
| | Device | 162x162 | 350x162 | 350x350 | 726x350 |
| 1024x1366 | Canvas | 170x170 | 378.5x170 | 378.5x378.5 | 795x378.5 |
| | Device | 160x160 | 356x160 | 356x356 | 748x356 |
| 1192x1590 * | Canvas | 188x188 | 412x188 | 412x412 | 860x412 |
| | Device | 188x188 | 412x188 | 412x412 | 860x412 |

* When Display Zoom is set to More Space.

#### watchOS widget dimensions

| Apple Watch size | Size of a widget in the Smart Stack (pt) |
| --- | --- |
| 40mm | 152x69.5 |
| 41mm | 165x72.5 |
| 44mm | 173x76.5 |
| 45mm | 184x80.5 |
| 49mm | 191x81.5 |

#### visionOS reference dimensions

Selected native-family references at 100% scale:

| Widget family | Layout size (pt) | Nominal spatial size (mm) |
| --- | --- | --- |
| Small | 158×158 | 268×268 |
| Medium | 338×158 | 574×268 |
| Large | 338×354 | 574×600 |
| Extra large portrait | 338×450 | 574×763 |

The HIG also publishes landscape extra-large reference geometry. Follow the SDK's native-versus-compatible family mapping above rather than treating that reference row as a promise that every app can offer both orientations.

### Related Components

- [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) - Layout guidance

### Developer Documentation

- [WidgetKit](https://developer.apple.com/documentation/widgetkit)
- [Developing a WidgetKit strategy](https://developer.apple.com/documentation/widgetkit/developing-a-widgetkit-strategy) - WidgetKit
- [Updating widgets with WidgetKit push notifications](https://developer.apple.com/documentation/widgetkit/updating-widgets-with-widgetkit-push-notifications) - Budgeted updates that supplement timelines

### Videos

- [What's new in widgets](https://developer.apple.com/videos/play/wwdc2025/278)
- [Bring widgets to life](https://developer.apple.com/videos/play/wwdc2023/10028/)
- [Design widgets for visionOS](https://developer.apple.com/videos/play/wwdc2025/255)

## Changelog

### December 16, 2025
- Updated the HIG's platform guidance, including visionOS and CarPlay widgets.

### January 17, 2025
- Corrected watchOS widget dimensions.

### June 10, 2024
- Updated to include guidance for accented widgets in iOS 18 and iPadOS 18.

### June 5, 2023
- Updated guidance to include widgets in watchOS, widgets on the iPad Lock Screen, and updates for iOS 17, iPadOS 17, and macOS 14.

### November 3, 2022
- Added guidance for widgets on the iPhone Lock Screen and updated design comprehensives for iPhone 14, iPhone 14 Pro, and iPhone 14 Pro Max.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/widgets)*
