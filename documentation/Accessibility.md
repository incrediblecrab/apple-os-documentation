# Accessibility

Make your apps accessible to everyone who uses Apple devices.

**Platforms:** iOS 14.0+ | iPadOS 14.0+ | Mac Catalyst 14.0+ | macOS 11.0+ | tvOS 14.0+ | visionOS 1.0+ | watchOS 7.0+

## Overview

Accessibility features help people with different needs interact with their devices. Design accessible workflows from the beginning and test them with the settings and assistive technologies people use; adopting one API doesn't establish that an entire app is accessible.

For many, accessibility is a necessity. For others, it's a practicality. For example, closed captions can be necessary for someone who is deaf or hard of hearing, but also useful for someone watching a video in a noisy environment. Learn more about how to support different types of accessibility needs in your app using Apple's wide range of accessibility APIs.

### Accessibility Domains

**Vision**  
A person may be blind or color blind, or have a vision challenge that makes focusing difficult.

**Speech**  
A person may have a speech disability or prefer to connect without using their voice.

**Mobility**  
A person with reduced mobility may have difficulty holding a device or tapping the interface.

**Cognitive**  
A person may have difficulty remembering a sequence of steps, or they may find an overly complex user interface difficult to process and manage.

**Hearing**  
A person may be deaf, have partial hearing loss, or have difficulty hearing sounds within a certain range.

### Featured Sample Apps

Explore how sample apps leverage accessible design principles and accessibility APIs to create a great user experience for everyone.

- [Destination Video](https://developer.apple.com/documentation/visionos/destination-video)
- [Happy Beam](https://developer.apple.com/documentation/visionos/happybeam)

### Assistive Technologies

People can personalize their devices by choosing the accessibility features and assistive technologies that give them the best user experience. Make sure your app provides a great experience for people who use assistive technologies by testing your app with them.

**VoiceOver**  
A screen reader that describes interface content. Its interaction methods vary by platform; it isn't limited to touch gestures.

**Voice Control**  
An interface for navigating a device using voice commands to tap, swipe, type, and more.

**Switch Control**  
An interface for navigating a device with a variety of adaptive switch hardware, wireless game controllers, or sounds such as a click or a pop.

**Assistive Access**  
A mode that tailors the iOS and iPadOS experience for people with cognitive disabilities.

### Accessibility Nutrition Labels

You can add Accessibility Nutrition Labels to your App Store product page to indicate which accessibility features your app supports on each platform. For example, a person who is blind or has low vision might seek apps that support VoiceOver or Larger Text.

Evaluate each device separately: claiming support for a feature requires that people can complete all common app tasks with it, including fundamental flows such as onboarding, login, purchases, and settings. Labels aren't a certification that adopting one accessibility API makes the app accessible.

For eligibility, feature definitions, and submission instructions, see [Overview of Accessibility Nutrition Labels](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels) in App Store Connect Help.

### API and migration checks

- [`AccessibilityNotification`](https://developer.apple.com/documentation/accessibility/accessibilitynotification) provides typed announcements and layout/screen-change notifications from iOS 17, macOS 14, and aligned releases. Choose announcement priority deliberately rather than flooding the speech queue.
- [`AccessibilitySettings`](https://developer.apple.com/documentation/accessibility/accessibilitysettings) exposes system preferences and supported settings destinations. Individual members have different minimum versions; the type's availability does not make every destination available on every OS.
- [`AXBrailleTranslator`](https://developer.apple.com/documentation/accessibility/axbrailletranslator) adds table-based print/Braille translation on the 26-generation platforms. It is not an OS 27-only feature.
- On supported OS 27 platforms, SwiftUI's [`TabsPickerStyle`](https://developer.apple.com/documentation/swiftui/tabspickerstyle) and AppKit's segmented-control/toolbar-group roles distinguish navigation tabs from value-selection controls for VoiceOver. See [SwiftUI](SwiftUI.md#layout-input-and-toolbars) and [AppKit](AppKit.md#controls-input-and-observation).
- For web content, Safari 27 adds `ariaNotify()` announcements; retain a live-region fallback on older engines. See the [Safari migration guide](../guides/safari27-migration.md).

Follow the [accessibility HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility) and [material guidance](https://developer.apple.com/design/human-interface-guidelines/materials): test Reduce Transparency, Increase Contrast, motion preferences, large text, and assistive input. Do not convey state through translucency or color alone. Use [Accessibility Inspector](https://developer.apple.com/documentation/accessibility/accessibility-inspector) and the [XCUIAutomation](XCUIAutomation.md) tooling alongside manual assistive-technology testing.

## Topics

### Essentials
- [Accessibility updates](https://developer.apple.com/documentation/updates/accessibility) - Learn about important changes to Accessibility.
- [Accessibility HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility) - Design guidance for accessible interfaces.
- [Performing accessibility testing for your app](https://developer.apple.com/documentation/accessibility/performing-accessibility-testing-for-your-app) - Test your app with accessibility settings and assistive technologies to discover and address accessibility issues.

### Sample Code
- [Enhancing the accessibility of your SwiftUI app](https://developer.apple.com/documentation/accessibility/enhancing-the-accessibility-of-your-swiftui-app) - Support advancements in SwiftUI accessibility to make your app accessible to everyone.
- [Creating Accessible Views](https://developer.apple.com/documentation/swiftui/creating-accessible-views) - Make your app accessible to everyone by applying accessibility modifiers to your SwiftUI views.
- [Delivering an exceptional accessibility experience](https://developer.apple.com/documentation/accessibility/delivering_an_exceptional_accessibility_experience) - Make improvements to your app's interaction model to support assistive technologies such as VoiceOver.
- [Integrating accessibility into your app](https://developer.apple.com/documentation/accessibility/integrating-accessibility-into-your-app) - Make your app more accessible to users with disabilities by adding accessibility features.
- [Accessibility design for Mac Catalyst](https://developer.apple.com/documentation/accessibility/accessibility_design_for_mac_catalyst) - Improve navigation in your app by using keyboard shortcuts and accessibility containers.

### Domains
- [Vision](https://developer.apple.com/documentation/accessibility/vision) - A person may be blind or color blind, or have a vision challenge that makes focusing difficult.
- [Speech](https://developer.apple.com/documentation/accessibility/speech) - A person may have a speech disability or prefer to connect without using their voice.
- [Mobility](https://developer.apple.com/documentation/accessibility/mobility) - A person with reduced mobility may have difficulty holding a device or tapping the interface.
- [Cognitive](https://developer.apple.com/documentation/accessibility/cognitive) - A person may have difficulty remembering a sequence of steps, or they may find an overly complex user interface difficult to process and manage.
- [Hearing](https://developer.apple.com/documentation/accessibility/hearing) - A person may be deaf, have partial hearing loss, or have difficulty hearing sounds within a certain range.

### Developer Tools
- [Accessibility Inspector](https://developer.apple.com/documentation/accessibility/accessibility-inspector) - Reveal how your app represents itself to people using accessibility features.

### Assistive Technologies
- [Assistive technologies](https://developer.apple.com/documentation/accessibility/assistive-technologies) - Evaluate interactions with the technologies people use.

### Accessibility Framework
- [Accessibility API](https://developer.apple.com/documentation/accessibility/accessibility-api) - Browse API in the Accessibility framework.

### Platforms
- [Accessibility fundamentals](https://developer.apple.com/documentation/swiftui/accessibility-fundamentals) - Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Accessibility for UIKit](https://developer.apple.com/documentation/uikit/accessibility-for-uikit) - Make your UIKit apps accessible to everyone who uses iOS and tvOS.
- [Accessibility for AppKit](https://developer.apple.com/documentation/appkit/accessibility-for-appkit) - Make your AppKit apps accessible to everyone who uses macOS.
- [Accessibility for visionOS](https://developer.apple.com/documentation/accessibility/accessibility-for-visionos) - Make your apps accessible to everyone who uses visionOS.

### WWDC Challenges
- [WWDC22 Challenge: Learn Switch Control through gaming](https://developer.apple.com/documentation/accessibility/wwdc22_challenge_learn_switch_control_through_gaming) - Play a card-matching game using Switch Control.
- [WWDC21 Challenge: Large Text Challenge](https://developer.apple.com/documentation/accessibility/wwdc21_challenge_large_text_challenge) - Design for large text sizes by modifying the user interface.
- [WWDC21 Challenge: Speech Synthesizer Simulator](https://developer.apple.com/documentation/accessibility/wwdc21_challenge_speech_synthesizer_simulator) - Simulate a conversation using speech synthesis.
- [WWDC21 Challenge: VoiceOver Maze](https://developer.apple.com/documentation/accessibility/wwdc21_challenge_voiceover_maze) - Navigate to the end of a dark maze using VoiceOver as your guide.

### Related Videos
- [Create accessible spatial experiences](https://developer.apple.com/videos/play/wwdc2023/10034)
- [Build accessible apps with SwiftUI and UIKit](https://developer.apple.com/videos/play/wwdc2023/10036)
- [Meet Assistive Access](https://developer.apple.com/videos/play/wwdc2023/10032)
- [Design considerations for vision and motion](https://developer.apple.com/videos/play/wwdc2023/10078)
- [Perform accessibility audits for your app](https://developer.apple.com/videos/play/wwdc2023/10035)
- [Extend Speech Synthesis with personal and custom voices](https://developer.apple.com/videos/play/wwdc2023/10033)

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Accessibility)*
