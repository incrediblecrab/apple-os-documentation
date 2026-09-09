# CareKit

People can use CareKit apps to manage care plans related to a chronic illness like diabetes, recover from an injury or surgery, or achieve health and wellness goals.

**Platforms:** iOS | iPadOS

## Overview

To learn more about CareKit, see [Research & Care > CareKit](https://www.researchandcare.org/carekit/).

Apple's HIG uses CareKit 2.0 as the context for the component examples below. CareKitUI supplies reusable views, and CareKitStore supplies persistence for entities such as patients, care plans, tasks, and contacts. The CareKit integration layer coordinates store changes with configured view controllers. You can use the UI or store separately; choosing a view doesn't automatically implement data synchronization or keep a remote clinical record current. See the [CareKit project documentation](https://carekit-apple.github.io/CareKit/documentation/carekit).

## Topics

### Data and Privacy

Nothing is more important than protecting people's privacy and safeguarding the extremely sensitive data your CareKit app collects and stores.

- **Provide a coherent privacy policy** - [App Review Guidelines 5.1.1](https://developer.apple.com/app-store/review/guidelines/) requires a privacy-policy link in App Store Connect metadata and easy access within the app. Explain collection, uses, sharing, retention, deletion, and consent withdrawal rather than relying on the framework's presence as a privacy guarantee.

- **Protect data regardless of its source** - Apply appropriate privacy safeguards to both information people enter and information obtained through system capabilities. Obtain the required permission before access; see [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting-user-privacy).

### HealthKit Integration

HealthKit provides a protected health-data store on supported devices, including iPad with iPadOS 17 or later. Check availability and request only the data types the task needs. HealthKit authorization permits reading from or writing to that store; the API's `toShare` parameter means saving data to HealthKit, not permission to disclose it to caregivers. Explain and obtain the appropriate consent for your app's separate care-team sharing flow.

- **Request health access in context** - Ask when a task needs the information, not merely because the app launched. Account for permission changes and follow the authorization API's behavior; see [requestAuthorization(toShare:read:completion:)](https://developer.apple.com/documentation/healthkit/hkhealthstore/requestauthorization(toshare:read:completion:)).

- **Clarify your app's intent by adding descriptive messages** - People expect to see the system-provided permission screen when asked to approve access to health data. Write a few succinct sentences that explain why you need the information and how people can benefit from sharing it with your app. Avoid adding custom screens that replicate the standard permission screen's behavior or content.

- **Distinguish system authorization from app-controlled sharing** - Don't imitate HealthKit's permission screen or present app toggles as if they change system authorization. Help people find the system's health-access controls, while providing understandable controls for your app's own sharing and consent choices.

For related design guidance, see [HealthKit](https://developer.apple.com/design/human-interface-guidelines/healthkit). For developer guidance, see [HealthKit](https://developer.apple.com/documentation/healthkit).

### Motion Data

When relevant and authorized, Core Motion can report activity classifications and supported pedometer measurements. Activity flags aren't mutually exclusive: stationary and automotive can both be true at a stoplight. Check availability separately for measurements such as steps, pace, and floors; don't present unavailable or estimated device data as a certain clinical measurement.

Motion information can also include custom data collected as part of physical therapy. For example, some ResearchKit tasks use device sensors to test flexibility, range of motion, and ambulatory capability.

For developer guidance, see [Core Motion](https://developer.apple.com/documentation/coremotion).

### Photos

Pictures can help communicate treatment progress when a care plan calls for them. Let people choose the photos to share, explain the destination, and obtain the appropriate consent; taking or selecting a photo isn't permission to upload it to a care team.

Use [PhotosPicker](https://developer.apple.com/documentation/photosui/photospicker) or [PHPickerViewController](https://developer.apple.com/documentation/photosui/phpickerviewcontroller) for supported photo-selection workflows. For camera capture, see [UIImagePickerController](https://developer.apple.com/documentation/uikit/uiimagepickercontroller) and request the necessary camera permission.

### ResearchKit Integration

A ResearchKit app lets people participate in medical research studies. Your CareKit app can incorporate relevant surveys, tasks, charts, and consent screens. Those screens help present and record consent; they don't automatically satisfy legal, ethics-review, HealthKit authorization, or caregiver-sharing requirements.

For related design guidance, see [ResearchKit](https://developer.apple.com/design/human-interface-guidelines/researchkit). For developer guidance, see [Research & Care > Developers](https://www.researchandcare.org/developers/).

### CareKit Views

The HIG highlights three groups of CareKitUI views — tasks, charts, and contacts — rather than an exhaustive inventory of the evolving package. Choose appropriate views and configure their data or controller bindings.

Each view category is designed to support specific types of content and interaction. To ensure a consistent experience, use each view type for its intended purpose.

| Category | Purpose |
|----------|---------|
| Tasks | Present tasks, like taking medication or doing physical therapy. Support logging of patient symptoms and other data. |
| Charts | Display graphical data that can help people understand how their treatment is progressing. |
| Contact views | Display contact information. Support communication through phone, message, and email, and link to a map of the contact's location. |

The HIG's card examples use a header and, where appropriate, a vertical stack of content subviews. The header can contain text, a symbol, a disclosure indicator, and a separator; the content appears below it. This isn't a structural requirement for every helper view in CareKitUI.

Use the provided stack and customization interfaces for internal layout. Custom subviews and additional constraints still need testing; the framework doesn't make conflicting constraints impossible.

#### Tasks
A care plan generally presents a set of prescribed actions for people to perform, such as taking medication, eating specific foods, exercising, or reporting symptoms. CareKit UI defines several styles of task views you can use to display prescribed actions. Typically, you customize a task view by providing the information to display, often by specifying data stored in an on-device CareKit Store database. In some cases, you might also supply custom UI elements.

A task can contain the following information. The expectations below describe the HIG's presentation guidance, not Swift property nullability. Example values illustrate UI content, not a prescribed treatment or medication dose.

| Information | HIG design expectation | Description | Example value |
|-------------|----------|-------------|---------------|
| Title | Provide | A word or short phrase that introduces the task. | Daily check-in |
| Schedule | Provide | When the task is intended to be completed. | Once daily |
| Instructions | As needed | Explanations, recommendations, or warnings supplied for the task. | Record notes for your care team. |
| Group ID | No | An identifier you can use to group similar tasks in ways that make sense in your app. | A category identifier like medication or exercise. |

The HIG's CareKit 2.0 examples cover five task styles: simple, instructions, log, checklist, and grid. Each supports a particular use case; consult the chosen package version for its complete view inventory.

- **Use the simple style for a one-step task** - The default simple-style view consists of a header area that contains a title, subtitle, and button. You provide the title and subtitle, and you can provide a custom image to display in the button when the task is complete. If you don't supply an image, CareKit shows that a task is complete by filling in the button and displaying a checkmark. Because the default simple-style view doesn't include a content stack, consider using a different task style if you need to display additional content.

- **Use the instructions style when you need to add informative text** - For example, if a single-step medication task needs to include additional information — such as "Take on an empty stomach" or "Take at bedtime" — you can use an instructions-style task to display it.

- **Use the log style to help people log events** - For example, you could use this task style to display a button people can tap whenever they feel nauseated. The log-style task can automatically display a timestamp every time the patient logs an event.

- **Use the checklist style to display a list of actions or steps in a multistep task** - For example, if people must take a medication three times per day, you could display the three scheduled times in a checklist. Each checklist item can include a text description and a button that people can tap to mark the item as done. By default, a checklist task can also display instructional text below the list.

- **Use the grid style to display a grid of buttons in a multistep task** - Like the checklist style, the grid style also supports a multistep task, but it displays the steps in a more compact arrangement. You can supply a succinct title for each button (if you need to provide additional description for each button, you might want to use the checklist style instead). By default, a grid-style task can also display instructional text below the grid of buttons. Unlike other task styles, the grid style gives you access to its underlying collection view, which means that you can display custom UI elements in the grid layout.

- **Consider using color to reinforce the meaning of task items** - Color can be a good way to help people understand information at a glance. For example, you could use one color for medications and a different color for physical activities. Always avoid using color as the only way to convey information. For guidance, see [Color](https://developer.apple.com/design/human-interface-guidelines/color).

- **Combine accuracy with simplicity when describing a task and its steps** - Use the recognizable medication or task name supplied by the care plan instead of an unfamiliar chemical description. Don't substitute a brand or omit clinically necessary dose, unit, or timing information merely to shorten a label. Remove repetition only when the meaning remains unambiguous.

- **Consider supplementing multistep or complex tasks with videos or images** - Visually demonstrating how to perform a task can help people avoid mistakes.

#### Charts

Chart views can present current and historical care-plan data. Configured CareKit chart controllers can synchronize the displayed data with a store; a standalone chart view doesn't automatically obtain new health measurements.

In CareKit 2.0, CareKit UI provides three chart styles: bar, scatter, and line. For each style, you provide a descriptive title and subtitle, supply axis markers — like days of the week — and specify the data set.

- **Highlight meaningful patterns without overstating them** - For example, a chart can compare recorded medication adherence and reported symptoms. An observed association alone doesn't establish that one caused the other or that a treatment is effective.

- **Label chart elements clearly and succinctly** - Long, detailed labels can make a chart difficult to read and understand. Keep labels short and avoid repeating the same information. For example, a heart rate chart might use the term BPM in an axis label instead of using it in the label of every data point.

- **Use distinct colors** - In general, avoid using different shades of the same color to mean different things. Also ensure that you use colors with sufficient contrast. For related guidance, see [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility).

- **Consider providing a legend to add clarity** - If the colors you use to represent different types of data aren't immediately clear, include a legend that clearly and succinctly describes them.

- **Clearly denote units of time** - People need to know whether time-based data is represented in seconds, minutes, hours, days, weeks, months, or years. If you don't want to include this information in individual data value labels, include it in an axis label or elsewhere on the chart.

- **Consolidate large data sets for greater readability** - A large amount of data can make a chart unreadable by reducing the size of individual data points and presenting too much visible information. Look for ways to group and organize data for clarity and simplicity.

- **Choose a readable, honest chart structure** - If large and small values are difficult to compare, use a suitable scale or separate views and explain any transformation. Don't silently alter values or use misleading axes to exaggerate progress. See [Charting data](https://developer.apple.com/design/human-interface-guidelines/charting-data).

For developer guidance, see [CareKit > Chart Interfaces](https://carekit-apple.github.io/CareKit/documentation/carekit/chart-interfaces). To learn about ResearchKit charts, see the [ResearchKit GitHub project](https://github.com/ResearchKit/ResearchKit).

#### Contact Views

A care plan typically includes a care team and other trusted individuals who can help patients follow the plan. CareKit UI defines a contact view you can use to help patients communicate with the people in their care plan.

In CareKit 2.0, CareKit UI provides two styles of the contact view: simple and detailed.

- **Consider using color to categorize care team members** - Color can help people identify care team members at a glance.

### Best Practices

#### Notifications

Notifications can tell people when it's time to take medication or complete a task, and badging your app icon can show that there's an unread message from a caregiver. Apple Watch can also display a notification from your app; for guidance, see [Notifications](https://developer.apple.com/design/human-interface-guidelines/notifications).

- **Minimize notifications** - Care plans vary from patient to patient. While one individual may have only a few daily tasks to complete, another may have a long list. Use notifications sparingly so people don't feel overwhelmed. When possible, consider coalescing multiple items into a single notification.

- **Consider providing a detail view** - In addition to providing more information, a notification detail view can help people take immediate action without leaving their current context to open your app. For example, you could use a notification detail view to display a list of pending tasks so that people can quickly mark them as complete.

#### Symbols and Branding

CareKit uses a variety of built-in symbols to help people understand what they can do in a care app. For example, CareKit can display the phone, messaging, and envelope symbols in a contact view and the clock symbol in a log-style task view.

Although you can customize the default symbols, most view styles work best with the CareKit-provided symbols. The exception is the highly customizable grid-style task view, which can display your custom UI in a grid layout.

In a grid view, you might want to display custom symbols that are relevant to the unique content and experience in your app. You could use symbols to indicate the grouping of tasks; for example, a pill to represent medication tasks, or a person walking to represent exercise tasks. In this scenario, consider using SF Symbols to illustrate custom items in your app.

Using SF Symbols in your app gives you:

- Designs that coordinate with CareKit's visual design language
- Support for creating custom symbols to represent the unique content in your app

- **Design a relevant care symbol** - If you need to customize a symbol, be sure the design is closely related to your app or the general concept of health and wellness. Avoid creating a purely decorative symbol or using a corporate logo as a custom symbol.

- **Incorporate refined, unobtrusive branding** - People use CareKit apps to help them achieve their health and wellness goals; they don't want to see advertising. To avoid distracting people from their care plan, subtly incorporate your brand through your app's use of color and communication style.

### Platform Considerations

The HIG's care-interface guidance is scoped to iOS and iPadOS; it isn't a complete declaration of library support. The [package manifest at the January 24, 2026 commit](https://github.com/carekit-apple/CareKit/blob/308f7051df6eb861dfab15248a5504e47bae4921/Package.swift) declares iOS 18, macOS 15, and watchOS 11 minimums and includes CareKit, CareKitUI, CareKitStore, and CareKitFHIR products. This is a dated branch snapshot, not a claim about every release or every component's availability. Check the release and modules you adopt rather than applying the HIG's older platform exclusions to the entire project.

### Related Components

- [HealthKit](https://developer.apple.com/design/human-interface-guidelines/healthkit) - How it relates to health data management
- [ResearchKit](https://developer.apple.com/design/human-interface-guidelines/researchkit) - Integration for medical research studies

### Developer Documentation

- [CareKit](https://carekit-apple.github.io/CareKit/documentation/carekit) - Project API and integration documentation
- [Research & Care > Developers](https://www.researchandcare.org/developers/) - Development resources
- [Protecting user privacy — HealthKit](https://developer.apple.com/documentation/healthkit/protecting-user-privacy) - Privacy guidelines
- [CMPedometer](https://developer.apple.com/documentation/coremotion/cmpedometer) - Measurement-specific capability checks
- [CMMotionActivity](https://developer.apple.com/documentation/coremotion/cmmotionactivity) - Activity classification and overlapping flags
- [ResearchKit GitHub project](https://github.com/ResearchKit/ResearchKit) - Open source project

### Videos

- [What's new in CareKit](https://developer.apple.com/videos/play/wwdc2020/10151/) - WWDC 2020
- [Build a research and care app, part 1: Setup onboarding](https://developer.apple.com/videos/play/wwdc2021/10068) - WWDC 2021

## Changelog

These dates describe Apple's HIG article history.

### May 2, 2023
- Consolidated guidance into one page.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/carekit)*
