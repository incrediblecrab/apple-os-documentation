# Audio Toolbox

Record or play audio, convert formats, parse audio streams, and configure your audio session.

**Platforms:** iOS 2.0+ | iPadOS 2.0+ | Mac Catalyst 13.1+ | macOS 10.0+ | tvOS 9.0+ | visionOS 1.0+

## Overview

The AudioToolbox framework provides interfaces for recording, playback, and stream parsing. In iOS, the framework provides additional interfaces for managing audio sessions.

## Topics

### Essentials
- [Porting your audio code to Apple silicon](https://developer.apple.com/documentation/audiotoolbox/porting_your_audio_code_to_apple_silicon) - Eliminate issues in your audio-specific code when running on Apple silicon Mac computers.

### Audio Units
- [Generating spatial audio from a multichannel audio stream](https://developer.apple.com/documentation/audiotoolbox/generating_spatial_audio_from_a_multichannel_audio_stream) - Convert 8-channel audio to 2-channel spatial audio by using a spatial mixer audio unit.
- [Audio Unit v3 Plug-Ins](https://developer.apple.com/documentation/audiotoolbox/audio_unit_v3_plug-ins) - Deliver custom audio effects, instruments, and other audio behaviors using an Audio Unit v3 app extension.
- [Audio Components](https://developer.apple.com/documentation/audiotoolbox/audio_components) - Find, load, and configure audio components, such as Audio Units and audio codecs.
- [Audio Unit v2 (C) API](https://developer.apple.com/documentation/audiotoolbox/audio_unit_v2_c_api) - Configure an Audio Unit and prepare it to render audio.
- [Audio Unit Properties](https://developer.apple.com/documentation/audiotoolbox/audio_unit_properties) - Obtain information about the built-in mixers, equalizers, filters, effects, and other Audio Unit app extensions.
- [Audio Unit Voice I/O](https://developer.apple.com/documentation/audiotoolbox/audio_unit_voice_i_o) - Configure system voice processing and respond to speech events.

### Playback and Recording
- [Audio Queue Services](https://developer.apple.com/documentation/audiotoolbox/audio_queue_services) - Connect to audio hardware and manage the recording or playback process.
- [Audio Services](https://developer.apple.com/documentation/audiotoolbox/audio_services) - Play short sounds or trigger a vibration effect on iOS devices with the appropriate hardware.
- [Music Player](https://developer.apple.com/documentation/audiotoolbox/music_player) - Create and play a sequence of tracks, and manage aspects of playback in response to standard events.
- [Anchoring sound to a window or volume](https://developer.apple.com/documentation/audiotoolbox/anchoring_sound_to_a_window_or_volume) - Provide unique app experiences by attaching sounds to windows and volumes in 3D space.

### Audio Files and Formats
- [Audio Format Services](https://developer.apple.com/documentation/audiotoolbox/audio_format_services) - Access information about audio formats and codecs.
- [Audio File Services](https://developer.apple.com/documentation/audiotoolbox/audio_file_services) - Read or write a variety of audio data to or from disk or a memory buffer.
- [Extended Audio File Services](https://developer.apple.com/documentation/audiotoolbox/extended_audio_file_services) - Read and write compressed files and linear PCM audio files using a simplified interface.
- [Audio File Stream Services](https://developer.apple.com/documentation/audiotoolbox/audio_file_stream_services) - Parse streamed audio files as the data arrives on the user's computer.
- [Audio File Components](https://developer.apple.com/documentation/audiotoolbox/audio_file_components) - Get information about audio file formats, and about files containing audio data.
- [Core Audio File Format](https://developer.apple.com/documentation/audiotoolbox/core_audio_file_format) - Parse the structure of Core Audio files.

### Utilities
- [Analyzing audio performance with Instruments](https://developer.apple.com/documentation/audiotoolbox/analyzing_audio_performance_with_instruments) - Ensure a smooth and immersive audio experience in your apps using Audio System Trace.
- [Audio Converter Services](https://developer.apple.com/documentation/audiotoolbox/audio_converter_services) - Convert between linear PCM audio formats, and between linear PCM and compressed formats.
- [Audio Session Support](https://developer.apple.com/documentation/audiotoolbox/audio_session_support) - Describe the properties that you associate with audio sessions and audio routes.
- [Audio Toolbox Debugging](https://developer.apple.com/documentation/audiotoolbox/audio_toolbox_debugging) - Obtain the internal state of Core Audio objects during the development and debugging of your code.
- [Workgroup Management](https://developer.apple.com/documentation/audiotoolbox/workgroup_management) - Coordinate the activity of custom real-time audio threads with those of the system and other processes.
- [Audio Codec](https://developer.apple.com/documentation/audiotoolbox/audio_codec) - Translate audio data from one format to another.
- [Clock Utilities](https://developer.apple.com/documentation/audiotoolbox/clock_utilities) - Manage time-related information associated with audio playback.

### Deprecated
- [Deprecated Symbols](https://developer.apple.com/documentation/audiotoolbox/deprecated_symbols) - Review unsupported symbols and their replacements.

### Reference
- **AudioToolbox Structures**
- **AudioToolbox Enumerations**
- **AudioToolbox Constants**
- **AudioToolbox Functions**
- **AudioToolbox Data Types**

### Macros
- **Macros**

### Protocols
- **SpatialAudioExperience** - Configure an audio stream for spatial computing. *Beta*

### Structures
- **AutomaticSpatialAudio** - A spatial audio experience determined by the system. *Beta*
- **BypassedSpatialAudio** - An experience in which the system does not apply spatial processing to the audio stream. *Beta*
- **FixedSpatialAudio** - A spatial experience that does not take user motion into account. *Beta*
- **HeadTrackedSpatialAudio** - A spatial experience that takes user motion into account. *Beta*

### Variables
- **kAUAudioMixParameter_RemixAmount** *Beta*
- **kAUAudioMixParameter_Style** *Beta*
- **kAUAudioMixProperty_EnableSpatialization** *Beta*
- **kAUAudioMixProperty_SpatialAudioMixMetadata** *Beta*
- **kAudioCodecContentSource_AV_Spatial_Live**
- **kAudioCodecContentSource_AV_Spatial_Offline**
- **kAudioCodecContentSource_AV_Traditional_Live**
- **kAudioCodecContentSource_AV_Traditional_Offline**
- **kAudioCodecContentSource_AppleAV_Spatial_Live**
- **kAudioCodecContentSource_AppleAV_Spatial_Offline**
- **kAudioCodecContentSource_AppleAV_Traditional_Live**
- **kAudioCodecContentSource_AppleAV_Traditional_Offline**
- **kAudioCodecContentSource_AppleCapture_Spatial**
- **kAudioCodecContentSource_AppleCapture_Spatial_Enhanced**
- **kAudioCodecContentSource_AppleCapture_Traditional**
- **kAudioCodecContentSource_AppleMusic_Spatial**
- **kAudioCodecContentSource_AppleMusic_Traditional**
- **kAudioCodecContentSource_ApplePassthrough**
- **kAudioCodecContentSource_Capture_Spatial**
- **kAudioCodecContentSource_Capture_Spatial_Enhanced**
- **kAudioCodecContentSource_Capture_Traditional**
- **kAudioCodecContentSource_Music_Spatial**
- **kAudioCodecContentSource_Music_Traditional**
- **kAudioCodecContentSource_Passthrough**
- **kAudioCodecContentSource_Reserved**
- **kAudioCodecContentSource_Unspecified**
- **kAudioCodecDynamicRangeControlConfiguration_Capture**
- **kAudioCodecDynamicRangeControlConfiguration_Movie**
- **kAudioCodecDynamicRangeControlConfiguration_Music**
- **kAudioCodecDynamicRangeControlConfiguration_None**
- **kAudioCodecDynamicRangeControlConfiguration_Speech**
- **kAudioCodecPropertyASPFrequency**
- **kAudioCodecPropertyContentSource**
- **kAudioCodecPropertyDynamicRangeControlConfiguration**
- **kAudioConverterPropertyChannelMixMap**
- **kAudioConverterPropertyPerformDownmix**
- **kAudioUnitErr_MultipleVoiceProcessors**
- **kAudioUnitSubType_AUAudioMix** *Beta*

### Functions
- **AudioConverterFillComplexBufferRealtimeSafe** *Beta*
- **AudioConverterFillComplexBufferWithPacketDependencies** *Beta*
- **AudioFileWritePacketsWithDependencies** *Beta*
- **AudioServicesPlayAlertSound** - Play an alert sound with the provided spatial audio experience. *Beta*
- **AudioServicesPlaySystemSound** - Play a system sound with the provided spatial audio experience. *Beta*

### Type Aliases
- **AudioConverterComplexInputDataProcRealtimeSafe**

### Enumerations
- **AUAudioMixRenderingStyle**
- **SpatialAudioExperiences** *Beta*

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AudioToolbox)*