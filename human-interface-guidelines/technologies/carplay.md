# CarPlay

CarPlay lets people get directions, make calls, send and receive messages, listen to music, and more from their car's built-in display, all while staying focused on the road.

**Platforms:** iOS

## Overview

People download CarPlay apps from the App Store and install them on iPhone like any other app. When people connect their iPhone with their vehicle, app icons for installed CarPlay apps appear on the CarPlay Home screen.

Driver-facing CarPlay experiences need to support quick tasks with minimal interaction. The guidance below focuses on that driving context. Some capabilities have a different safety boundary: Apple's WWDC26 guidance describes video apps for supported vehicles only while parked, as well as voice-based conversational apps. Follow the requirements for your app category rather than assuming every CarPlay capability is usable while driving.

Use the system-defined templates appropriate to your app category. Your app supplies their content, while CarPlay manages standard controls, layout adaptation, and vehicle input. This doesn't make all custom content automatic: a navigation app, for example, draws the map beneath a `CPMapTemplate` control overlay. Test your content and artwork across supported display and input configurations.

See the [CarPlay Developer Guide](https://developer.apple.com/download/files/CarPlay-Developer-Guide.pdf) for app-category rules and templates. CarPlay apps require approval for the category-specific entitlement; adding templates alone doesn't establish eligibility.

## Topics

### iPhone Interactions

- **Eliminate app interactions on iPhone while driving** - Interactions need to occur using the car's built-in controls and display. If your app requires setup on iPhone, make sure people perform it while parked, before the vehicle is in motion.
- **Never lock people out of CarPlay because the connected iPhone requires input** - Your app needs to function when iPhone is inaccessible — for example, when people put it in a bag or in the trunk while driving. If people must resolve a problem on the connected iPhone, let them do so after the vehicle stops.
- **Make sure your app works without requiring people to unlock iPhone** - Most people use CarPlay while their iPhone is locked, so ensure that the features you provide in your CarPlay app work as expected in this scenario.

### Audio

- **Let people choose when to start playback** - In general, avoid beginning playback automatically unless your app's purpose is to play a single source of audio, or your app is resuming previously interrupted audio. Don't activate a playback audio session until audio is ready, because an interrupting session can stop another source such as the vehicle's radio. Navigation prompts require appropriate mixing rather than treating all audio sessions alike.
- **Start playback as soon as audio has sufficiently loaded** - Buffering and network conditions can delay a selection. Use the template's loading behavior while processing it: for a `CPListItem` selection handler, CarPlay displays progress until your app calls the supplied completion closure. This is an app-managed completion signal, not automatic detection that a stream is playable.
- **Display the Now Playing screen when audio is ready to play** - Don't delay playback until descriptive information completes loading. If necessary, continue loading such information in the background, and show it when it's available.
- **Resume audio playback after an interruption only when it's appropriate** - For example, your app can resume audio after a temporary interruption like a phone call. Permanent interruptions, such as a music playlist initiated by Siri, are nonresumable. When a resumable interruption occurs, your app needs to resume playback when the interruption ends if audio was actively playing when the interruption started.
- **When necessary, automatically adjust audio levels, but don't change the overall volume** - Although your app can adjust relative, independent volume levels to achieve a great mix of audio, people need to control the final output volume.

### Layout

CarPlay supports portrait and landscape displays with varying resolutions, pixel densities, and aspect ratios. The system scales app icons and standard interface components to keep their physical appearance reasonably consistent. The HIG lists these examples, not an exhaustive set of supported displays:

| Dimensions (pixels) | Aspect ratio |
|-------------------|--------------|
| 800x480           | 5:3          |
| 960x540           | 16:9         |
| 1280x720          | 16:9         |
| 1920x720          | 8:3          |

- **Provide useful, high-value information in a clean layout that's easy to scan from the driver's seat** - Don't clutter the screen with nonessential details and unnecessary visual embellishments.
- **Maintain an overall consistent appearance throughout your app** - In general, ensure that elements with similar functions look similar.
- **Ensure that primary content stands out and feels actionable** - Large items tend to appear more important than smaller ones and are easier for people to tap. In general, place the most important content and controls in the upper half of the screen.

### Color

- **Prefer a limited color palette that coordinates with your app logo** - Subtle use of color is a great way to communicate your brand.
- **Avoid using the same color for interactive and noninteractive elements** - If interactive and noninteractive elements have the same color, it's hard for people to know where to tap.
- **Test your app's color scheme under a variety of lighting conditions in a parked car** - Lighting varies significantly based on time of day, weather, window tinting, and more. Colors you see on your computer at design time won't always look the same when your app is used in the real world. Consider how color brightness might affect the experience of driving at night, and how low-contrast colors can wash out in direct sunlight.
- **Ensure your app looks great in both dark and light environments** - CarPlay supports both light and dark appearances, and may automatically adjust the current appearance based on lighting conditions.
- **Choose colors that help you communicate effectively with everyone** - Different people see and interpret colors differently. For guidance on using colors in ways that people appreciate, see Inclusive color.

### Icons and Images

- **Supply high-resolution images with scale factors of @2x and @3x for all CarPlay artwork** - The system automatically shows the correct images and scales them appropriately, based on the resolution and size of the car's display.
- **Mirror your iPhone app icon** - A well-designed app icon works well in CarPlay and on iPhone, without the need for a second design.
- **Don't use black for your icon's background** - Lighten a black background or add a border so the icon doesn't blend into the display background.

Create your CarPlay app icon in the following sizes:

| @2x (pixels) | @3x (pixels) |
|-------------|-------------|
| 120x120     | 180x180     |

### Error Handling

- **Report errors in CarPlay, not on the connected iPhone** - If you must notify people of a problem, do so clearly in CarPlay. Never direct people to pick up their iPhone to read or resolve an error.

### Platform Considerations

**iOS**  
No additional considerations for iOS. Not supported in iPadOS, macOS, tvOS, visionOS, or watchOS.

### Developer Documentation

- [CarPlay Developer Guide](https://developer.apple.com/download/files/CarPlay-Developer-Guide.pdf)
- [CarPlay framework](https://developer.apple.com/documentation/carplay)
- [CPMapTemplate](https://developer.apple.com/documentation/carplay/cpmaptemplate) - Template overlay and app-drawn map responsibilities
- [CPListItem.handler](https://developer.apple.com/documentation/carplay/cplistitem/handler) - Selection completion and progress behavior

### Videos

- [Rev up your CarPlay app](https://developer.apple.com/videos/play/wwdc2026/212/)

## Changelog

These dates describe Apple's HIG article history.

### May 2, 2023
- Consolidated guidance into one page.

---

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/carplay)*
