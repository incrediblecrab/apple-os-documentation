# Core Audio Types

Use specialized data types to interact with audio streams, complex buffers, and audiovisual timestamps.

**Platforms:** iOS 13.0+ | iPadOS 13.0+ | Mac Catalyst 13.0+ | macOS 10.15+ | tvOS 13.0+ | visionOS 1.0+ | watchOS 6.0+

## Overview

The Core Audio Types framework declares common data types and constants that other Core Audio interfaces use. This framework also includes several convenience functions.

If you're unfamiliar with the specialized terminology regarding the manipulation of audio data, refer to Core Audio Glossary.

## Topics

### Buffers
- **AudioBuffer** - A structure that holds a buffer of audio data.
- **AudioBufferList** - A structure that stores a variable-length array of audio buffers.

### Channels
- **AudioChannelDescription** - A structure that describes a channel of audio data.
- **AudioChannelLayout** - A structure that specifies a channel layout in a file or in hardware.

### Codecs
- **AudioClassDescription** - A structure that describes an audio codec.

### Audio Time
- **AudioTimeStamp** - A structure that represents a timestamp value.
- **AudioTimeStampFlags** - A structure that represents flags for a timestamp.

### SMPTE Time
- **SMPTETime** - A structure that defines an SMPTE time value.
- **SMPTETimeFlags** - A structure that defines SMPTE time flags.
- **SMPTETimeType** - Constants that define SMPTE time types.

### Values
- **AudioValueRange** - A structure that represents a continuous range of values.
- **AudioValueTranslation** - A structure that stores buffers to use in translation operations.

### Streams
- **AudioStreamBasicDescription** - A format specification for an audio stream.
- **AudioStreamPacketDescription** - A value that describes a packet in a buffer of audio data.
- **AudioFormatFlags** - A type definition for audio format flags.
- [Audio Format Flags](https://developer.apple.com/documentation/coreaudiotypes/audio_format_flags) - Commonly used combinations of data format flags for an audio stream description.
- **AudioFormatID** - A type definition for audio format identifiers.
- [Audio Format Identifiers](https://developer.apple.com/documentation/coreaudiotypes/audio_format_identifiers) - Identifiers for supported audio formats.
- **kAudioStreamAnyRate** - A value that indicates that an audio stream can use any sample rate.
- **MPEG4ObjectID** - Constants that define the type of MPEG-4 audio data.

### Common Types
- **AVAudioInteger** - An integer type for audio operations.
- **AVAudioUInteger** - An unsigned integer type for audio operations.
- **AudioSessionID** - A unique identifier of an audio session.
- **kAudioUnitSampleFractionBits** - The number of fractional bits in fixed-point samples.
- **COREAUDIOTYPES_VERSION** - A value that represents the Core Audio Types version.
- **AudioSampleType** - The canonical audio data sample type for input and output. *Deprecated*
- **AudioUnitSampleType** - The canonical audio data sample type for audio processing. *Deprecated*
- **AudioFormatListItem**

### Errors
- **kAudio_ParamError** - An error in the parameter list of the function.
- **kAudio_MemFullError** - An error that indicates that the heap zone is full.
- **kAudio_FileNotFoundError** - An error that indicates the file wasn't found.
- **kAudio_UnimplementedError** - An error that indicates the app called an unimplemented system function.

### Reference
- **CoreAudioTypes Enumerations**

### Structures
- **AudioStreamPacketDependencyDescription**

### Variables
- **kAudioChannelLayoutTag_Ogg_3_0**
- **kAudioChannelLayoutTag_Ogg_4_0**
- **kAudioChannelLayoutTag_Ogg_5_0**
- **kAudioChannelLayoutTag_Ogg_5_1**
- **kAudioChannelLayoutTag_Ogg_6_1**
- **kAudioChannelLayoutTag_Ogg_7_1**
- **kAudioFormatAPAC**
- **kAudio_BadFilePathError**
- **kAudio_FilePermissionError**
- **kAudio_NoError**
- **kAudio_TooManyFilesOpenError**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/CoreAudioTypes)*