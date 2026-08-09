# Designing for iOS

People depend on their iPhone to help them stay connected, play games, view media, accomplish tasks, and track personal data in any location and while on the go.

**Platforms:** iOS

## Overview

As you begin designing your app or game for iOS, start by understanding the following fundamental device characteristics and patterns that distinguish the iOS experience. Using these characteristics and patterns to inform your design decisions can help you provide an app or game that iPhone users appreciate.

**Display.** iPhone has a medium-size, high-resolution display.

**Ergonomics.** People generally hold their iPhone in one or both hands as they interact with it, switching between landscape and portrait orientations as needed. While people are interacting with the device, their viewing distance tends to be no more than a foot or two.

**Inputs.** Multi-Touch gestures, virtual keyboards, and voice control let people perform actions and accomplish meaningful tasks while they're on the go. In addition, people often want apps to use their personal data and input from the device's gyroscope and accelerometer, and they may also want to participate in spatial interactions.

**App interactions.** Sometimes, people spend just a minute or two checking on event or social media updates, tracking data, or sending messages. At other times, people can spend an hour or more browsing the web, playing games, or enjoying media. People typically have multiple apps open at the same time, and they appreciate switching frequently among them.

**System features.** iOS provides several features that help people interact with the system and their apps in familiar, consistent ways.

- Widgets
- Home Screen quick actions
- Spotlight
- Shortcuts
- Activity views

> **iOS 27+:** Liquid Glass is refined — stronger content diffusion, a darkened edge ring, and brighter specular highlights — and a continuous **transparency slider** in Settings > Appearance replaces the OS 26 Clear/Tinted toggle. App icons gain sharper layer separation. `UIDesignRequiresCompatibility` is ignored by the iOS 27 SDK, so rebuilding opts you fully in. iOS 27 drops no iPhones.

## Topics

### Best Practices

Great iPhone experiences integrate the platform and device capabilities that people value most. To help your design feel at home in iOS, prioritize the following ways to incorporate these features and capabilities.

- **Prioritize content** - Help people concentrate on primary tasks and content by limiting the number of onscreen controls while making secondary details and actions discoverable with minimal interaction.

- **Adapt to user preferences** - Adapt seamlessly to appearance changes — like device orientation, Dark Mode, and Dynamic Type — letting people choose the configurations that work best for them.

- **Support natural interactions** - Support interactions that accommodate the way people usually hold their device. For example, it tends to be easier and more comfortable for people to reach a control when it's located in the middle or bottom area of the display, so it's especially important let people swipe to navigate back or initiate actions in a list row.

- **Integrate platform capabilities** - With people's permission, integrate information available through platform capabilities in ways that enhance the experience without asking people to enter data. For example, you might accept payments, provide security through biometric authentication, or offer features that use the device's location.

### Resources

- [Apple Design Resources](https://developer.apple.com/design/resources/)

### Developer Documentation

- [iOS Pathway](https://developer.apple.com/pathways/ios/)

### Videos

- [Meet Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/10001/)
- [Get to know the new design system](https://developer.apple.com/videos/play/wwdc2025/10002/)

---

*Design baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Reviewed 2026-08-09.*

*Source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios)*
