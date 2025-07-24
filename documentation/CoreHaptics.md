# Core Haptics

Compose and play haptic patterns to customize your iOS app's haptic feedback.

**Platforms:** iOS 13.0+ | iPadOS 13.0+ | Mac Catalyst 13.0+ | tvOS 14.0+ | visionOS 1.0+

## Overview

Core Haptics lets you add customized haptic and audio feedback to your app. Use haptics to engage users physically, with tactile and audio feedback that gets attention and reinforces actions. Some system-provided interface elements—like pickers, switches, and sliders—automatically provide haptic feedback as users interact with them. With Core Haptics, you extend this functionality by composing and combining haptics beyond the default patterns.

Your app can play custom haptic patterns crafted from basic building blocks called haptic events (CHHapticEvent). Events can be transient, like the feedback you get from toggling a switch, or continuous, like the vibration or sound from a ringtone. You can use transient and continuous patterns independently, or build your pattern from precise combinations of the two. Another type of haptic event allows you to play customized audio content as part of your pattern.

## Topics

### Essentials
- [Preparing your app to play haptics](https://developer.apple.com/documentation/corehaptics/preparing_your_app_to_play_haptics) - Set up your app to play haptics.
- [Playing a single-tap haptic pattern](https://developer.apple.com/documentation/corehaptics/playing_a_single-tap_haptic_pattern) - Create and play a transient haptic pattern from a dictionary literal inline.
- **class CHHapticEngine** - An object that represents the connection to the haptic server.
- **class CHHapticPattern** - An object representing a haptic waveform.
- **protocol CHHapticPatternPlayer** - A protocol that defines a standard pattern player capable of playing haptic patterns with fixed parameters.
- **protocol CHHapticAdvancedPatternPlayer** - A protocol that defines an advanced pattern player capable of looping, seeking, pausing, and resuming haptic playback.

### Programmatic haptics
You can synthesize haptics by configuring parameters like haptic intensity and sharpness. Event parameters define the initial state, while dynamic parameters change the pattern during playback.

- [Delivering Rich App Experiences with Haptics](https://developer.apple.com/documentation/corehaptics/delivering_rich_app_experiences_with_haptics) - Enhance your app's experience by incorporating haptic and sound feedback into key interactive moments.
- [Playing Collision-Based Haptic Patterns](https://developer.apple.com/documentation/corehaptics/playing_collision-based_haptic_patterns) - Play a custom haptic pattern whose strength depends on an object's collision speed.
- [Updating Continuous and Transient Haptic Parameters in Real Time](https://developer.apple.com/documentation/corehaptics/updating_continuous_and_transient_haptic_parameters_in_real_time) - Generate continuous and transient haptic patterns in response to user touch.
- **class CHHapticEvent** - An object that describes a single haptic or audio event.
- **class CHHapticEventParameter** - A static parameter value that represents a single property of the haptic pattern.
- **class CHHapticDynamicParameter** - A value that you send to a haptic pattern player to alter a property value during playback.
- **class CHHapticParameterCurve** - A curve that you send to a haptic pattern player to alter a property value gradually during playback.

### File-based haptics
Apple Haptic and Audio Pattern (AHAP) files are a JSON-like representation of synced haptics and audio that you can load and play from disk.

- [Playing a Custom Haptic Pattern from a File](https://developer.apple.com/documentation/corehaptics/playing_a_custom_haptic_pattern_from_a_file) - Sample predesigned Apple Haptic Audio Pattern files, and learn how to play your own.
- [Representing haptic patterns in AHAP files](https://developer.apple.com/documentation/corehaptics/representing_haptic_patterns_in_ahap_files) - Understand the Apple Haptic and Audio Pattern (AHAP) file format.

### Game controller haptics
- [Playing Haptics on Game Controllers](https://developer.apple.com/documentation/corehaptics/playing_haptics_on_game_controllers) - Add haptic feedback to supported game controllers by using Core Haptics.

### Haptic errors
- **let CoreHapticsErrorDomain: String** - A string representation of the haptic error domain.
- **struct CHHapticError** - A structure that represents a framework error.
- **enum Code** - Error codes for framework operations.

### Variables
- **let CHHapticAudioResourceKeyLoopEnabled: String** - A key for a Boolean value that indicates whether to loop audio playback.
- **let CHHapticAudioResourceKeyUseVolumeEnvelope: String** - A key for a Boolean value that indicates whether audio file playback fades in and out using an envelope.

### Type Aliases
- **typealias CHHapticAudioResourceKey** - A type alias for a key that identifies the playback behavior of an audio resource.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreHaptics)*