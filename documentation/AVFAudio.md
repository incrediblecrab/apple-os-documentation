# AVFAudio

Play, record, and process audio; configure your app's system audio behavior.

**Platforms:** iOS 14.5+ | iPadOS 14.5+ | Mac Catalyst 14.5+ | macOS 11.3+ | tvOS 14.5+ | visionOS 1.0+ | watchOS 9.0+

## Topics

### Essentials
- [AVFAudio updates](https://developer.apple.com/documentation/avfaudio/avfaudio_updates) - Learn about important changes to AVFAudio.

### System Audio
- [Handling audio interruptions](https://developer.apple.com/documentation/avfaudio/handling_audio_interruptions) - Observe audio session notifications to ensure that your app responds appropriately to interruptions.
- [Responding to audio route changes](https://developer.apple.com/documentation/avfaudio/responding_to_audio_route_changes) - Observe audio session notifications to ensure that your app responds appropriately to route changes.
- [Adding synthesized speech to calls](https://developer.apple.com/documentation/avfaudio/adding_synthesized_speech_to_calls) - Provide a more accessible experience by adding your app's audio to a call.
- [Capturing stereo audio from built-In microphones](https://developer.apple.com/documentation/avfaudio/capturing_stereo_audio_from_built-in_microphones) - Configure an iOS device's built-in microphones to add stereo recording capabilities to your app.
- **AVAudioSession** - An object that communicates to the system how you intend to use audio in your app.
- **AVAudioApplication** - An object that manages one or more audio sessions that belong to an app.
- **AVAudioRoutingArbiter** - An object for configuring macOS apps to participate in AirPods Automatic Switching.

### Basic Playback and Recording
- **AVAudioPlayer** - An object that plays audio data from a file or buffer.
- **AVAudioRecorder** - An object that records audio data to a file.
- **AVMIDIPlayer** - An object that plays MIDI data through a system sound module.

### Advanced Audio Processing
- **Audio Engine** - Perform advanced real-time and offline audio processing, implement 3D spatialization, and work with MIDI and samplers.

### Speech Synthesis
- **Speech synthesis** - Configure voices to speak strings of text.

### Macros
- **Macros**

### Classes
- **AVAudioSessionCapability** - Describes whether a specific capability is supported and if that capability is currently enabled (Beta)
- **AVAudioSessionPortExtensionBluetoothMicrophone** - An object that describes capabilities of Bluetooth microphone ports. (Beta)

### Protocols
- **AVAudioSessionSpatialExperience**

### Variables
- **AVAudioSessionSetActiveFlags_NotifyOthersOnDeactivation** - A flag that indicates that when your audio session deactivates, any audio sessions that your audio session interrupted can reactivate themselves. (Deprecated)
- **AVEncoderASPFrequencyKey** (Beta)
- **AVEncoderContentSourceKey** (Beta)
- **AVEncoderDynamicRangeControlConfigurationKey** (Beta)
- **AVSampleRateConverterAlgorithm_Mastering** - The mastering encoder bit rate strategy.
- **AVSampleRateConverterAlgorithm_MinimumPhase** - The minimum phase encoder bit rate strategy.
- **AVSampleRateConverterAlgorithm_Normal** - The usual encoder bit rate strategy.

### Functions
- **AVMakeBeatRange** - Creates a beat range with the specified start time and length.

### Type Aliases
- **AVAudioConverterInputBlock** - A block to get input data for conversion, as necessary.
- **AVBeatRange**
- **AVMIDIPlayerCompletionHandler** - A callback the system invokes when MIDI playback completes.

### Enumerations
- **AVAudioContentSource** (Beta)
- **AVAudioDynamicRangeControlConfiguration**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AVFAudio)*