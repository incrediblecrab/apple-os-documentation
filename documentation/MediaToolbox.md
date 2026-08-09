# Media Toolbox

Enable support for media format readers; tap and process audio from an audio mix.

**Platforms:** iOS 6.0+ | iPadOS 6.0+ | Mac Catalyst 6.0+ | macOS 10.9+ | tvOS 9.0+ | visionOS 1.0+

## Overview

Call the **MTRegisterProfessionalVideoWorkflowFormatReaders()** function to enable the use of custom MediaExtension format readers.

Use an **MTAudioProcessingTap** to tap audio from an **AVPlayer**.

## Topics

### Professional video workflows
- **MTRegisterProfessionalVideoWorkflowFormatReaders()** - Enables the use of media format readers that support professional video workflows.

### Audio Taps
- **MTAudioProcessingTapCreate()** - Creates a new audio processing tap.
- **MTAudioProcessingTapGetSourceAudio()** - Retrieves source audio for an audio processing tap.
- **MTAudioProcessingTapGetStorage()** - Retrieves a custom storage pointer for an audio processing tap.
- **MTAudioProcessingTapGetTypeID()** - Retrieves the type identifier for this audio processing tap.
- **MTAudioProcessingTapFlags** - Flags that indicate where to tap the audio.
- **MTAudioProcessingTap** - An audio processing tap object.

### Utility
- **MTCopyLocalizedNameForMediaType()** - Returns a localized name for the specified media type.
- **MTCopyLocalizedNameForMediaSubType()** - Returns a localized name for the specified media type and subtype.

### Enumerations
- **Anonymous Enumerations**

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/MediaToolbox)*