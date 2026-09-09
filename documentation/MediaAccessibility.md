# Media Accessibility

Make your app's media more accessible by supporting people's systemwide preferences for video and audio content.

**Platforms:** iOS 7.0+ | iPadOS 7.0+ | Mac Catalyst 13.1+ | macOS 10.9+ | tvOS 9.0+ | visionOS 1.0+

These minimums describe legacy caption-preference APIs, not every feature in the framework.

## Overview

People can specify a variety of preferences about media content such as videos, songs, and images in Accessibility system settings. For example, people can customize the appearance of captions that appear when they watch videos. The Media Accessibility framework provides information about these accessibility settings for media content so you can adapt your app's UI to people's preferences.

## Availability and source differences

The framework landing page currently annotates iOS, iPadOS, and tvOS 17, plus Mac Catalyst 13. That is not the introduction date of the older caption functionality. Concrete references for [`MACaptionAppearanceGetDisplayType(_:)`](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancegetdisplaytype(_:)) and [`MACaptionAppearanceCopySelectedLanguages(_:)`](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancecopyselectedlanguages(_:)) list iOS/iPadOS 7 and Mac Catalyst 13.1.

The tvOS sources also disagree: those concrete web references currently list tvOS 17. Apple's installed tvOS 26.5 SDK instead declares these functions in `MACaptionAppearance.h` with `CF_AVAILABLE(10_9, 7_0)`, without a later tvOS restriction. Syntax-only checks of those declarations accept a tvOS 9.0 deployment target. The header above therefore preserves the legacy caption baseline; this SDK check is not a tvOS 9 runtime test.

### Newer feature minimums

- [`MADimFlashingLightsEnabled()`](https://developer.apple.com/documentation/mediaaccessibility/madimflashinglightsenabled()) reads the preference from iOS/iPadOS/Mac Catalyst/tvOS 16.4, macOS 13.3, and visionOS 1.
- [`MAFlashingLightsProcessor`](https://developer.apple.com/documentation/mediaaccessibility/maflashinglightsprocessor), for custom video processing, requires iOS/iPadOS/Mac Catalyst/tvOS 17, macOS 14, or visionOS 1.
- [`MAMusicHapticsManager`](https://developer.apple.com/documentation/mediaaccessibility/mamusichapticsmanager) is annotated from iOS/iPadOS/Mac Catalyst/tvOS 18, macOS 15, and visionOS 2. API presence does not guarantee haptic playback on a device: check feature activation and availability of a haptic track for the song.

## Topics

### Features
- [Captions](https://developer.apple.com/documentation/mediaaccessibility/captions) - Coordinate the presentation of closed-captioned data for your app's media files.
- [Flashing lights](https://developer.apple.com/documentation/mediaaccessibility/flashing-lights) - Detect, mitigate, and inform people about flashing lights in media content.
- [Music Haptics](https://developer.apple.com/documentation/mediaaccessibility/music-haptics) - Play haptic tracks along with known music tracks.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MediaAccessibility)*
