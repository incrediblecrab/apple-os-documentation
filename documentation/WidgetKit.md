# WidgetKit

Extend the reach of your app by creating widgets, watch complications, Live Activities, and controls.

**Platforms:** iOS 14.0+ | iPadOS 14.0+ | Mac Catalyst 14.0+ | macOS 11.0+ | visionOS 26.0+ | watchOS 9.0+

## Overview
WidgetKit uses SwiftUI to present focused app content outside the main app. Choose the appropriate experience rather than treating every surface as the same kind of widget:

- **Widgets:** Show selected information on supported Home Screens, Lock Screens, desktops, Notification Center, and other system surfaces. iPhone widgets can also appear in supported Mac and CarPlay contexts. On visionOS 26, spatial widgets can attach to horizontal or vertical surfaces.
- **Smart Stacks:** The system considers context and relevance when promoting widgets; people can configure or pin them. Donating relevance information doesn't guarantee prominence or a particular display time.
- **Watch complications:** Present glanceable content on the watch face. The watch Smart Stack also reserves space for up to three complications.
- **Live Activities:** Use WidgetKit for presentation and [ActivityKit](ActivityKit.md) for the activity lifecycle and updates. The Dynamic Island is only one supported presentation, not a requirement on every device.
- **Controls:** App Intents-backed buttons and toggles expose actions in supported Control Centers, Lock Screens, Action buttons, and Mac menu bars. A control can also open the app to an appropriate view.

Framework availability doesn't establish availability of every experience. For example, controls begin with iOS/iPadOS/Mac Catalyst 18 and expand to macOS/watchOS 26. `AppIntentConfiguration` begins with iOS/iPadOS/Mac Catalyst 17, macOS 14, watchOS 10, and visionOS 26. Apple Vision Pro supports spatial widgets, not the Live Activities and controls described here.

Start with a focused size or feature, but design for additional contexts. People can configure a widget's content, open a matching app scene, or use supported intent-backed buttons and toggles without opening the app. [Developing a WidgetKit strategy](https://developer.apple.com/documentation/widgetkit/developing-a-widgetkit-strategy) explains which experiences can share views and which need separate lifecycle logic.

Most widgets and complications update through timelines: arrays of dated entries plus a reload policy. Entry dates and reload dates are not exact delivery guarantees. On watchOS 26, `RelevanceConfiguration` and `RelevanceEntriesProvider` offer a relevance-driven alternative to a timeline provider.

Live Activities instead use ActivityKit updates or ActivityKit push notifications. Controls update through interactions, app reload requests, or their own push mechanism. WidgetKit push notifications supplement widget updates as described below; these mechanisms aren't interchangeable.

Keep the design glanceable and test the actual supported surfaces, sizes, rendering modes, and accessibility settings.

## API and OS 27 migration checks

[`WidgetFamily.systemExtraLargePortrait`](https://developer.apple.com/documentation/widgetkit/widgetfamily/systemextralargeportrait) has iOS/iPadOS/Mac Catalyst/macOS 27 beta availability and visionOS 26 nonbeta availability. Its Discussion lists possible placements on the iPhone Home Screen, Today View on iOS/iPadOS, the Mac desktop, and visionOS. The availability list is not a placement table: don't infer support on every surface of each declared platform. Consult this case's Discussion alongside the widget HIG.

[`WidgetPushHandler`](https://developer.apple.com/documentation/widgetkit/widgetpushhandler), introduced on iOS/iPadOS/Mac Catalyst/macOS/visionOS/watchOS 26, receives widget push-token and configuration changes through [`pushTokenDidChange(_:widgets:)`](https://developer.apple.com/documentation/widgetkit/widgetpushhandler/pushtokendidchange(_:widgets:)). Attach it with [`pushHandler(_:)`](https://developer.apple.com/documentation/swiftui/widgetconfiguration/pushhandler(_:)) on the widget configuration. [WidgetKit push notifications](https://developer.apple.com/documentation/widgetkit/updating-widgets-with-widgetkit-push-notifications) request timeline reloads; they are budgeted and delivered opportunistically, not a replacement for timelines or a real-time delivery guarantee. Widget tokens are obtained with WidgetKit, not ordinary UserNotifications registration, and widget updates do not use broadcast channels.

The [iOS & iPadOS 27 beta 8 notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes) classify the failure to render timelines/images for `WidgetConfigurationIntent` types containing `@UnionValue` as **resolved** (177493357). Retest existing affected configurations; do not document union-valued intents as permanently unsupported.

Keep [ActivityKit](ActivityKit.md) updates, control updates, and widget timelines separate. Use [RelevanceKit](RelevanceKit.md) for watchOS relevance clues rather than assuming it changes Smart Stack ordering on every platform. For appearance, select appropriate [`WidgetAccentedRenderingMode`](https://developer.apple.com/documentation/widgetkit/widgetaccentedrenderingmode) behavior and test accented/full-color contexts and accessibility settings. The [widget HIG](https://developer.apple.com/design/human-interface-guidelines/widgets) is the design reference, not a fixed glass-rendering recipe.

## Topics

### Essentials
- [Developing a WidgetKit strategy](https://developer.apple.com/documentation/widgetkit/developing-a-widgetkit-strategy) - Explore features, tasks, related frameworks, and constraints as you make a plan to implement widgets, controls, watch complications, and Live Activities.
- [WidgetKit updates](https://developer.apple.com/documentation/updates/widgetkit) - Learn about important changes in WidgetKit.

### Widget creation
- [Creating a widget extension](https://developer.apple.com/documentation/widgetkit/creating-a-widget-extension) - Display your app's content in a convenient, informative widget on various devices.
- [Supporting additional widget sizes](https://developer.apple.com/documentation/widgetkit/supporting-additional-widget-sizes) - Offer widgets in additional contexts by adding support for various widget sizes.
- [Creating accessory widgets and watch complications](https://developer.apple.com/documentation/widgetkit/creating-accessory-widgets-and-watch-complications) - Support accessory widgets that appear on the Lock Screen and as complications on Apple Watch.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](https://developer.apple.com/documentation/widgetkit/emoji-rangers-supporting-live-activities-interactivity-and-animations) - Offer Live Activities, controls, animate data updates, and add interactivity to widgets.
- **Widget** - The configuration and content of a widget to display on the Home screen or in Notification Center.
- **WidgetBundle** - A container used to expose multiple widgets from a single widget extension.
- **StaticConfiguration** - An object describing the content of a widget that has no user-configurable options.
- **WidgetFamily** - Values that define the widget's size and shape.

### Presentation
- [Preparing widgets for additional platforms, contexts, and appearances](https://developer.apple.com/documentation/widgetkit/preparing-widgets-for-additional-contexts-and-appearances) - Create widgets that support additional platforms and adapt to their context.
- [Displaying the right widget background](https://developer.apple.com/documentation/widgetkit/displaying-the-right-widget-background) - Group your widget's background views and mark them as removable to ensure your widget appears correctly for each context and platform.
- [Optimizing your widget for accented rendering mode and Liquid Glass](https://developer.apple.com/documentation/widgetkit/optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass) - Make your widget feel at home on Apple platforms and Liquid Glass by using accented rendering mode.
- [Adding StandBy and CarPlay support to your widget](https://developer.apple.com/documentation/widgetkit/adding-standby-and-carplay-support-to-your-widget) - Ensure that your small system family widget works well in StandBy and CarPlay.
- [Creating views for widgets, Live Activities, and watch complications](https://developer.apple.com/documentation/widgetkit/creating-views-for-widgets-live-activities-and-watch-complications) - Implement glanceable views with WidgetKit and SwiftUI.
- [SwiftUI views for widgets](https://developer.apple.com/documentation/widgetkit/swiftui-views) - Present your app's content in widgets with SwiftUI views.
- [SwiftUI](https://developer.apple.com/documentation/swiftui) - Declare the views used by widget presentations.
- **WidgetRenderingMode** - Constants that indicate the rendering mode for a widget.
- **WidgetAccentedRenderingMode** - How an image is rendered within an accented widget.
- **AccessoryWidgetBackground** - An adaptive background view that provides a standard appearance based on the widget's environment.
- **WidgetLocation** - Values that indicate different widget locations.

### visionOS widgets
- [Updating your widgets for visionOS](https://developer.apple.com/documentation/widgetkit/updating-your-widgets-for-visionos) - Choose widget styles specific to visionOS, support recessed and elevated appearances, and add proximity awareness to your widget.
- [`widgetTexture(_:)`](https://developer.apple.com/documentation/swiftui/widgetconfiguration/widgettexture(_:)) - Specifies the widget texture.
- **WidgetTexture** - Values that define the texture of the widget's coating layer.
- [`supportedMountingStyles(_:)`](https://developer.apple.com/documentation/swiftui/widgetconfiguration/supportedmountingstyles(_:)) - Specifies supported mounting styles.
- **WidgetMountingStyle** - Values that define the widget's supported mounting style.
- **LevelOfDetail** - The level of detail the view is recommended to have.

### Interactivity
- [Adding interactivity to widgets and Live Activities](https://developer.apple.com/documentation/widgetkit/adding-interactivity-to-widgets-and-live-activities) - Include buttons or toggles in a widget or Live Activity to offer app functionality without launching the app.
- [Animating data updates in widgets and Live Activities](https://developer.apple.com/documentation/widgetkit/animating-data-updates-in-widgets-and-live-activities) - Use SwiftUI animations to indicate data updates in your widgets and Live Activities.
- [Linking to specific app scenes from your widget or Live Activity](https://developer.apple.com/documentation/widgetkit/linking-to-specific-app-scenes-from-your-widget-or-live-activity) - Add deep links to your widgets and Live Activities that enable people to open a specific scene in your app.

### Configurable widgets
- [Making a configurable widget](https://developer.apple.com/documentation/widgetkit/making-a-configurable-widget) - Give people the option to customize their widgets by adding a custom app intent to your project.
- [Migrating widgets from SiriKit Intents to App Intents](https://developer.apple.com/documentation/widgetkit/migrating-from-sirikit-intents-to-app-intents) - Configure your widgets for backward compatibility.
- **AppIntentConfiguration** - An object describing the content of a widget that uses a custom intent to provide user-configurable options.
- **WidgetInfo** - A structure that contains information about user-configured widgets.
- **AppIntentRecommendation** - An object that describes a recommended intent configuration for a user-customizable widget.
- **IntentConfiguration** - An object describing the content of a widget that uses a custom intent definition to provide user-configurable options.
- **IntentRecommendation** - An object that describes a recommended intent configuration for a user-customizable widget.

### Timeline management
- [Keeping a widget up to date](https://developer.apple.com/documentation/widgetkit/keeping-a-widget-up-to-date) - Plan your widget's timeline to show timely, relevant information using dynamic views, and update the timeline when things change.
- **TimelineProvider** - A type that advises WidgetKit when to update a widget's display.
- **AppIntentTimelineProvider** - A type that advises WidgetKit when to update a user-configurable widget's display.
- **IntentTimelineProvider** - A type that advises WidgetKit when to update a user-configurable widget's display.
- **TimelineProviderContext** - An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
- **TimelineEntry** - A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget's content.
- [`Timeline`](https://developer.apple.com/documentation/widgetkit/timeline) - An array of dated entries and a policy for requesting the next timeline; updates can occur later than the requested dates.
- **WidgetCenter** - An object that contains a list of user-configured widgets and is used for reloading widget timelines.

### Push notification updates
- [Updating widgets with WidgetKit push notifications](https://developer.apple.com/documentation/widgetkit/updating-widgets-with-widgetkit-push-notifications) - Use WidgetKit to receive push tokens and reload your widgets with remote push notifications.
- **WidgetPushHandler** - A type that can receive push information about widget refreshes and relevance refreshes.
- **WidgetPushInfo** - A structure that contains information about the push token for updating widgets and widget relevances.

### watchOS widgets
- **AccessoryWidgetGroup** - A view type that has a label at the top and three content views masked with a circle or rounded square.
- **AccessoryWidgetGroupStyle** - The style for an AccessoryWidgetGroup view.
- [Migrating ClockKit complications to WidgetKit](https://developer.apple.com/documentation/widgetkit/converting-a-clockkit-app) - Leverage WidgetKit's API to create watchOS complications using SwiftUI.

### Accessibility
- [Adding accessible descriptions to widgets and Live Activities](https://developer.apple.com/documentation/activitykit/adding-accessible-descriptions-to-widgets-and-live-activities) - Describe the interface elements of your widgets and Live Activities to help people understand what they represent.

### Location services in widgets
- [Accessing location information in widgets](https://developer.apple.com/documentation/widgetkit/accessing-location-information-in-widgets) - Incorporate location information into your widget presentation to make it more relevant and contextual.

### Networking
- [Making network requests in a widget extension](https://developer.apple.com/documentation/widgetkit/making-network-requests-in-a-widget-extension) - Update your widget with new information you fetch with a network request.

### Smart Stacks
- [Increasing the visibility of widgets in Smart Stacks](https://developer.apple.com/documentation/widgetkit/widget-suggestions-in-smart-stacks) - Supply the platform-appropriate relevance signals; the system and user settings determine presentation.
- **TimelineEntryRelevance** - An object that describes the relative importance of a timeline entry compared to other entries in the current and past timelines.
- **RelevanceConfiguration** - A type that describes the content of a widget that uses relevance clues.
- **RelevanceEntriesProvider** - A type that provides the content for a widget that uses relevance clues to display information in the Smart Stack.
- **RelevanceEntry** - A type that specifies the information to render a widget at a specific relevance configuration.
- **WidgetRelevance** - A type collecting the relevances for a widget kind.
- **WidgetRelevanceAttribute** - A type describing when a specific widget could be relevant.
- **WidgetRelevanceGroup** - A type for configuring widget behavior in the watchOS Smart Stack.

### Widget preview and debugging
- [Previewing widgets and Live Activities in Xcode](https://developer.apple.com/documentation/widgetkit/previewing-widgets-and-live-activities-in-xcode) - Use Xcode previews to iteratively develop, fine-tune, and troubleshoot widgets and Live Activities.
- [Debugging widgets](https://developer.apple.com/documentation/widgetkit/debugging-widgets) - Set environment variables in Xcode to control your widget's configuration in the debugger.
- **WidgetPreviewContext** - A specification for the context of a widget preview.
- [Preview macros](https://developer.apple.com/documentation/widgetkit/preview-macros) - Use Swift macros to create widget previews in Xcode.

### Live Activities
- **ActivityConfiguration** - An object that describes the content of a Live Activity.
- **DynamicIsland** - The layout and configuration for a Live Activity that appears in the Dynamic Island.
- **NSUserActivityTypeLiveActivity** - A string that the system passes to the app on launch from a Live Activity that doesn't provide a URL.
- **ActivityPreviewViewKind** - Values that represent Live Activity presentations for use in Xcode previews.
- **ActivityFamily** - A family that defines the Live Activity's size.

### Controls
- [Creating controls to perform actions across the system](https://developer.apple.com/documentation/widgetkit/creating-controls-to-perform-actions-across-the-system) - Perform your app's actions from Control Center, the Lock Screen, and the Action button.
- [Adding refinements and configuration to controls](https://developer.apple.com/documentation/widgetkit/adding-refinements-and-configuration-to-controls) - Customize the way controls display across the system and offer people the ability to configure them.
- **ControlWidgetToggle** - A control template representing a toggle.
- **ControlCenter** - An object that contains a list of user-configured controls and is used for reloading controls.
- **ControlWidgetButton** - A control template representing a button.

### Control values and previews
- **ControlValueProvider** - A type that provides a value to a control widget template.
- **AppIntentControlValueProvider** - A type that uses a custom intent to provide a value to a control template.

### Control configuration
- **StaticControlConfiguration** - The description of a control widget that has no user-configurable options.
- **AppIntentControlConfiguration** - The description of a control widget that uses a custom intent to provide user-configurable options.
- **ControlInfo** - A structure that contains information about user-configured controls.

### Control updates
- [Updating controls locally and remotely](https://developer.apple.com/documentation/widgetkit/updating-controls-locally-and-remotely) - Update and reload controls from your app or using push notifications.
- **ControlPushHandler** - A type that can receive push information about user-configured controls.
- **ControlPushInfo** - A structure that contains information about the push token of a user-configured control.
---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/WidgetKit)*
