# WidgetKit

Extend the reach of your app by creating widgets, watch complications, Live Activities, and controls.

**Platforms:** iOS 14.0+ | iPadOS 14.0+ | Mac Catalyst 14.0+ | macOS 11.0+ | visionOS 26.0+ Beta | watchOS 9.0+

## Overview
Using WidgetKit, you can make your app’s content available in contexts outside the app and extend its reach by building an ecosystem of glanceable, up-to-date experiences.

A conceptual image that shows a small widget on iPhone, a rectangular widget on Apple Watch, and a small widget on the Mac desktop.

The ecosystem that WidgetKit enables consists of:

Widgets
Widgets elevate a small amount of timely, personally relevant information from your app, display it where people can see it at a glance, and offer specific app functionality without launching the app. On iPhone and iPad, people put widgets in Today View, on the Home Screen, and on the Lock Screen. On Mac, people put native Mac app widgets on the desktop and in Notification Center. Additionally, people place iPhone widgets in locations like a Mac desktop and Notification Center, or in CarPlay. On Apple Watch, widgets appear in the Smart Stack, and on Apple Vision Pro, widgets become three-dimensional objects that people pin to horizontal and vertical surfaces.

Smart Stacks
On iPhone and iPad, people stack widgets on their Home Screen and create Smart Stacks that use Smart Rotate to show the most contextually relevant widget. On Apple Watch, the system intelligently displays widgets that are most relevant to someone’s personal context. Additionally, a person configures a widget to always appear in the Smart Stack or pins it to a fixed position.

Watch complications
People place watch complications on the Apple Watch face to view timely, relevant information when they lift their wrist. Additionally, the Smart Stack on Apple Watch offers space for up to three complications.

Live Activities
Live Activities display up-to-date content from your app such as event and task information on the Lock Screen or in the Dynamic Island. Live Activities use ActivityKit for updates and optionally the Apple Push Notification service (APNs) to send ActivityKit push notifications. For more information, refer to ActivityKit.

Controls
Controls act as a button or toggle that allows people to perform actions you describe with the App Intents framework in Control Center, on the Lock Screen, and from the Action button. A button control might initiate an action from your app, or open your app to a specific view, and a toggle might turn a light on and off or open and close a garage door. Controls appear in Control Center or as menu bar items and in Control Center on Apple Watch.

Develop glanceable features iteratively
WidgetKit enables features across iPad, iPhone, the Mac, Apple Watch, and Apple Vision Pro, but only in a way that best fits a person’s device and personal needs. For example, WidgetKit powers widgets on all platforms in various sizes. It also powers Live Activities and controls, features that aren’t available on Apple Vision Pro.

Even though not every feature that WidgetKit powers is available on every platform or device, widgets, Live Activities, controls, and watch complications share technology and design similarities. This makes it easy to develop features in tandem and to expand usage across contexts.

Use an iterative approach and start with support for one feature or select sizes of widgets — for example, start with a small widget as described in Creating a widget extension, but plan and design additional sizes and features across platforms from the beginning. Then allow people to view your content in as many contexts as possible. For more information, refer to Developing a WidgetKit strategy.

Understand interactivity and personalization
The WidgetKit ecosystem enables people to view your app content in new contexts and offers specific interactions with your app when and where they need it:

People tap a widget, watch complication, or Live Activity to launch the corresponding app or the app’s scene with matching information or functionality. For example, tapping an Emoji Ranger widget or watch complication launches the scene in the app that matches the displayed hero. For more information, refer to Linking to specific app scenes from your widget or Live Activity.

People use buttons and toggles in widgets, controls, and Live Activities to interact with your app without launching it. For example, the large widget of the Emoji Rangers: Supporting Live Activities, interactivity, and animations sample code project includes a button that people tap to give the healing capability of their hero a temporary boost.

In addition to offering relevant information and specific interactivity at a glance, people use widgets, watch complications, Live Activities, and controls to personalize their devices:

People configure widgets and watch complications to display details specific to their needs. For example, a widget of the Emoji Rangers: Supporting Live Activities, interactivity, and animations sample code project allows people to configure the hero that appears on the widget.

People arrange widgets and watch complications in the way that works best for them. When they stack widgets and enable Smart Rotate on iPhone or iPad, WidgetKit automatically rotates the most relevant widget to the top, making sure people see the most important details at the right time. On Apple Watch, the Smart Stack displays widgets based on contextual relevance, and people pin a favorite widget to a fixed position in the Smart Stack.

Update content with timelines and push notifications
Widgets and watch complications use a special mechanism to update their content: You create a timeline of data updates and hand it to WidgetKit. WidgetKit then makes sure the widget or complication updates its content in an energy-efficient way. For more information on timelines, refer to Keeping a widget up to date. Additionally, widgets can receive updates by using the Apple Push Notification service (APNs) and remote push notifications.

Live Activities don’t use timelines to update their content. Instead, they use ActivityKit and ActivityKit push notifications you send with APNs. For more information, refer to ActivityKit.

Controls don’t use timelines to update their content. Instead, your controls update their content when someone uses them, the app reloads them, or the system receives a remote push notification from APNs.

Create a focused, glanceable design
Widgets, watch complications, Live Activities, and controls are small and require a focused, glanceable design. For design guidance, refer to Human Interface Guidelines > Widgets, Human Interface Guidelines > Complications, Human Interface Guidelines > Live Activities, and Human Interface Guidelines > Controls.

## Topics

### Essentials
- [Developing a WidgetKit strategy](https://developer.apple.com/documentation/widgetkit/developing_a_widgetkit_strategy) - Explore features, tasks, related frameworks, and constraints as you make a plan to implement widgets, controls, watch complications, and Live Activities.
- [WidgetKit updates](https://developer.apple.com/documentation/widgetkit/widgetkit_updates) - Learn about important changes in WidgetKit.

### Widget creation
- [Creating a widget extension](https://developer.apple.com/documentation/widgetkit/creating_a_widget_extension) - Display your app's content in a convenient, informative widget on various devices.
- [Supporting additional widget sizes](https://developer.apple.com/documentation/widgetkit/supporting_additional_widget_sizes) - Offer widgets in additional contexts by adding support for various widget sizes.
- [Creating accessory widgets and watch complications](https://developer.apple.com/documentation/widgetkit/creating_accessory_widgets_and_watch_complications) - Support accessory widgets that appear on the Lock Screen and as complications on Apple Watch.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](https://developer.apple.com/documentation/widgetkit/emoji_rangers_supporting_live_activities_interactivity_and_animations) - Offer Live Activities, controls, animate data updates, and add interactivity to widgets.
- **Widget** - The configuration and content of a widget to display on the Home screen or in Notification Center.
- **WidgetBundle** - A container used to expose multiple widgets from a single widget extension.
- **StaticConfiguration** - An object describing the content of a widget that has no user-configurable options.
- **WidgetFamily** - Values that define the widget's size and shape.

### Presentation
- [Preparing widgets for additional platforms, contexts, and appearances](https://developer.apple.com/documentation/widgetkit/preparing_widgets_for_additional_platforms_contexts_and_appearances) - Create widgets that support additional platforms and adapt to their context.
- [Displaying the right widget background](https://developer.apple.com/documentation/widgetkit/displaying_the_right_widget_background) - Group your widget's background views and mark them as removable to ensure your widget appears correctly for each context and platform.
- [Optimizing your widget for accented rendering mode and Liquid Glass](https://developer.apple.com/documentation/widgetkit/optimizing_your_widget_for_accented_rendering_mode_and_liquid_glass) - Make your widget feel at home on Apple platforms and Liquid Glass by using accented rendering mode.
- [Adding StandBy and CarPlay support to your widget](https://developer.apple.com/documentation/widgetkit/adding_standby_and_carplay_support_to_your_widget) - Ensure that your small system family widget works well in StandBy and CarPlay.
- [Creating views for widgets, Live Activities, and watch complications](https://developer.apple.com/documentation/widgetkit/creating_views_for_widgets_live_activities_and_watch_complications) - Implement glanceable views with WidgetKit and SwiftUI.
- [SwiftUI views for widgets](https://developer.apple.com/documentation/widgetkit/swiftui_views_for_widgets) - Present your app's content in widgets with SwiftUI views.
- [Introducing SwiftUI](https://developer.apple.com/documentation/swiftui) - SwiftUI is a modern way to declare user interfaces for any Apple platform. Create beautiful, dynamic apps faster than ever before.
- **WidgetRenderingMode** - Constants that indicate the rendering mode for a widget.
- **WidgetAccentedRenderingMode** - Constants that indicate the rendering mode for an Image in when displayed in a widget in accented mode.
- **AccessoryWidgetBackground** - An adaptive background view that provides a standard appearance based on the widget's environment.
- **WidgetLocation** - Values that indicate different widget locations.

### visionOS widgets
- [Updating your widgets for visionOS](https://developer.apple.com/documentation/widgetkit/updating_your_widgets_for_visionos) - Choose widget styles specific to visionOS, support recessed and elevated appearances, and add proximity awareness to your widget.
- **widgetTexture** - Specifies the widget texture for this widget.
- **WidgetTexture** - Values that define the texture of the widget's coating layer.
- **supportedMountingStyles** - Specifies the mounting style for this widget.
- **WidgetMountingStyle** - Values that define the widget's supported mounting style.
- **LevelOfDetail** - The level of detail the view is recommended to have.

### Interactivity
- [Adding interactivity to widgets and Live Activities](https://developer.apple.com/documentation/widgetkit/adding_interactivity_to_widgets_and_live_activities) - Include buttons or toggles in a widget or Live Activity to offer app functionality without launching the app.
- [Animating data updates in widgets and Live Activities](https://developer.apple.com/documentation/widgetkit/animating_data_updates_in_widgets_and_live_activities) - Use SwiftUI animations to indicate data updates in your widgets and Live Activities.
- [Linking to specific app scenes from your widget or Live Activity](https://developer.apple.com/documentation/widgetkit/linking_to_specific_app_scenes_from_your_widget_or_live_activity) - Add deep links to your widgets and Live Activities that enable people to open a specific scene in your app.

### Configurable widgets
- [Making a configurable widget](https://developer.apple.com/documentation/widgetkit/making_a_configurable_widget) - Give people the option to customize their widgets by adding a custom app intent to your project.
- [Migrating widgets from SiriKit Intents to App Intents](https://developer.apple.com/documentation/widgetkit/migrating_widgets_from_sirikit_intents_to_app_intents) - Configure your widgets for backward compatibility.
- **AppIntentConfiguration** - An object describing the content of a widget that uses a custom intent to provide user-configurable options.
- **WidgetInfo** - A structure that contains information about user-configured widgets.
- **AppIntentRecommendation** - An object that describes a recommended intent configuration for a user-customizable widget.
- **IntentConfiguration** - An object describing the content of a widget that uses a custom intent definition to provide user-configurable options.
- **IntentRecommendation** - An object that describes a recommended intent configuration for a user-customizable widget.

### Timeline management
- [Keeping a widget up to date](https://developer.apple.com/documentation/widgetkit/keeping_a_widget_up_to_date) - Plan your widget's timeline to show timely, relevant information using dynamic views, and update the timeline when things change.
- **TimelineProvider** - A type that advises WidgetKit when to update a widget's display.
- **AppIntentTimelineProvider** - A type that advises WidgetKit when to update a user-configurable widget's display.
- **IntentTimelineProvider** - A type that advises WidgetKit when to update a user-configurable widget's display.
- **TimelineProviderContext** - An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
- **TimelineEntry** - A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget's content.
- **Timeline** - An object that specifies a date for WidgetKit to update a widget's view.
- **WidgetCenter** - An object that contains a list of user-configured widgets and is used for reloading widget timelines.

### Push notification updates
- [Updating widgets with WidgetKit push notifications](https://developer.apple.com/documentation/widgetkit/updating_widgets_with_widgetkit_push_notifications) - Use WidgetKit to receive push tokens and reload your widgets with remote push notifications.
- **WidgetPushHandler** - A type that can receive push information about widget refreshes and relevance refreshes.
- **WidgetPushInfo** - A structure that contains information about the push token for updating widgets and widget relevances.

### watchOS widgets
- **AccessoryWidgetGroup** - A view type that has a label at the top and three content views masked with a circle or rounded square.
- **AccessoryWidgetGroupStyle** - The style for an AccessoryWidgetGroup view.
- [Migrating ClockKit complications to WidgetKit](https://developer.apple.com/documentation/widgetkit/migrating_clockkit_complications_to_widgetkit) - Leverage WidgetKit's API to create watchOS complications using SwiftUI.

### Accessibility
- [Adding accessible descriptions to widgets and Live Activities](https://developer.apple.com/documentation/widgetkit/adding_accessible_descriptions_to_widgets_and_live_activities) - Describe the interface elements of your widgets and Live Activities to help people understand what they represent.

### Location services in widgets
- [Accessing location information in widgets](https://developer.apple.com/documentation/widgetkit/accessing_location_information_in_widgets) - Incorporate location information into your widget presentation to make it more relevant and contextual.

### Networking
- [Making network requests in a widget extension](https://developer.apple.com/documentation/widgetkit/making_network_requests_in_a_widget_extension) - Update your widget with new information you fetch with a network request.

### Smart Stacks
- [Increasing the visibility of widgets in Smart Stacks](https://developer.apple.com/documentation/widgetkit/increasing_the_visibility_of_widgets_in_smart_stacks) - Provide contextual information and donate intents to the system to make sure your widget appears prominently in Smart Stacks.
- **TimelineEntryRelevance** - An object that describes the relative importance of a timeline entry compared to other entries in the current and past timelines.
- **RelevanceConfiguration** - A type that describes the content of a widget that uses relevance clues.
- **RelevanceEntriesProvider** - A type that provides the content for a widget that uses relevance clues to display information in the Smart Stack.
- **RelevanceEntry** - A type that specifies the information to render a widget at a specific relevance configuration.
- **WidgetRelevance** - A type collecting the relevances for a widget kind.
- **WidgetRelevanceAttribute** - A type describing when a specific widget could be relevant.
- **WidgetRelevanceGroup** - A type for configuring widget behavior in the watchOS Smart Stack.

### Widget preview and debugging
- [Previewing widgets and Live Activities in Xcode](https://developer.apple.com/documentation/widgetkit/previewing_widgets_and_live_activities_in_xcode) - Use Xcode previews to iteratively develop, fine-tune, and troubleshoot widgets and Live Activities.
- [Debugging widgets](https://developer.apple.com/documentation/widgetkit/debugging_widgets) - Set environment variables in Xcode to control your widget's configuration in the debugger.
- **WidgetPreviewContext** - A specification for the context of a widget preview.
- [Preview macros](https://developer.apple.com/documentation/widgetkit/preview_macros) - Use Swift macros to create widget previews in Xcode.

### Live Activities
- **ActivityConfiguration** - An object that describes the content of a Live Activity.
- **DynamicIsland** - The layout and configuration for a Live Activity that appears in the Dynamic Island.
- **NSUserActivityTypeLiveActivity** - A string that the system passes to the app on launch from a Live Activity that doesn't provide a URL.
- **ActivityPreviewViewKind** - Values that represent Live Activity presentations for use in Xcode previews.
- **ActivityFamily** - A family that defines the Live Activity's size.

### Controls
- [Creating controls to perform actions across the system](https://developer.apple.com/documentation/widgetkit/creating_controls_to_perform_actions_across_the_system) - Perform your app's actions from Control Center, the Lock Screen, and the Action button.
- [Adding refinements and configuration to controls](https://developer.apple.com/documentation/widgetkit/adding_refinements_and_configuration_to_controls) - Customize the way controls display across the system and offer people the ability to configure them.
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
- [Updating controls locally and remotely](https://developer.apple.com/documentation/widgetkit/updating_controls_locally_and_remotely) - Update and reload controls from your app or using push notifications.
- **ControlPushHandler** - A type that can receive push information about user-configured controls.
- **ControlPushInfo** - A structure that contains information about the push token of a user-configured control.
---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/WidgetKit)*
