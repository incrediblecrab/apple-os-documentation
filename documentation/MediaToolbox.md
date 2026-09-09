# Media Toolbox

Enable support for media format readers; tap and process audio from an audio mix.

**Platforms:** iOS 6.0+ | iPadOS 6.0+ | Mac Catalyst 13.1+ (audio-tap functions) | macOS 10.9+ | tvOS 9.0+ | visionOS 1.0+

**Availability qualification:** The framework and some type references inherit a Mac Catalyst “6.0” annotation. The concrete audio-tap creation, access, and utility functions instead list Catalyst 13.1; use those callable declarations for deployment checks, not a nonexistent Catalyst 6 release.

## Overview

In a macOS app, call **MTRegisterProfessionalVideoWorkflowFormatReaders()** to opt in to professional-workflow format readers. This function is macOS-only and predates [MediaExtension](MediaExtension.md), which has its own macOS 15.0+ availability. The Media Toolbox platform list does not make format-reader registration an iOS API.

Use an **MTAudioProcessingTap** to tap audio from an **AVPlayer**.

## Topics

### Professional video workflows
- [`MTRegisterProfessionalVideoWorkflowFormatReaders()`](https://developer.apple.com/documentation/mediatoolbox/mtregisterprofessionalvideoworkflowformatreaders()) - Enables professional-workflow format readers on macOS; the function's reference starts at macOS 10.10.

### Audio Taps
- [`MTAudioProcessingTapCreate(_:_:_:_:)`](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapcreate(_:_:_:_:)) - Creates a new audio processing tap.
- [`MTAudioProcessingTapGetSourceAudio(_:_:_:_:_:_:)`](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapgetsourceaudio(_:_:_:_:_:_:)) - Retrieves source audio for an audio processing tap.
- [`MTAudioProcessingTapGetStorage(_:)`](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapgetstorage(_:)) - Retrieves a custom storage pointer for an audio processing tap.
- **MTAudioProcessingTapGetTypeID()** - Retrieves the type identifier for this audio processing tap.
- **MTAudioProcessingTapFlags** - Flags that indicate where to tap the audio.
- **MTAudioProcessingTap** - An audio processing tap object.

### Utility
- [`MTCopyLocalizedNameForMediaType(_:)`](https://developer.apple.com/documentation/mediatoolbox/mtcopylocalizednameformediatype(_:)) - Returns a localized name for the specified media type.
- [`MTCopyLocalizedNameForMediaSubType(_:_:)`](https://developer.apple.com/documentation/mediatoolbox/mtcopylocalizednameformediasubtype(_:_:)) - Returns a localized name for the specified media type and subtype.

### Enumerations
- **Anonymous Enumerations**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MediaToolbox)*
