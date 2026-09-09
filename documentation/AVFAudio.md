# AVFAudio

Play, record, and process audio; configure your app's system audio behavior.

**Platforms:** iOS 14.5+ | iPadOS 14.5+ | Mac Catalyst 14.5+ | macOS 11.3+ | tvOS 14.5+ | visionOS 1.0+ | watchOS 9.0+

## Audio-session integration

Treat route changes and interruptions as normal lifecycle events. Follow [Responding to audio route changes](https://developer.apple.com/documentation/avfaudio/responding-to-audio-route-changes) and [Handling audio interruptions](https://developer.apple.com/documentation/avfaudio/handling-audio-interruptions), keeping the UI synchronized with the actual player and session state.

When headphones disconnect, avoid unexpectedly continuing private playback through speakers. Apple's route-change guide notes that `AVPlayer` handles this transition automatically; a custom engine needs equivalent behavior. Recording also requires microphone authorization — choosing a session category is not permission to record.

For OS 27 adoption, distinguish the local audio session from [AVSystemRouting](AVSystemRouting.md) remote-device sessions and [Now Playing](NowPlaying.md) metadata publication. The latter does not replace audio-session setup.

The [macOS 27 Beta 8 notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes#AVFAudio), checked September 8, 2026, mark the AudioDSP crash on device-property changes as **resolved** (163978549). Test connecting and removing audio devices, but do not document that crash as a current platform limitation.

## Topics

### Essentials

- [AVFAudio updates](https://developer.apple.com/documentation/updates/avfaudio) - Learn about important changes to AVFAudio.

### System Audio

- [Handling audio interruptions](https://developer.apple.com/documentation/avfaudio/handling-audio-interruptions) - Observe audio session notifications to ensure that your app responds appropriately to interruptions.
- [Responding to audio route changes](https://developer.apple.com/documentation/avfaudio/responding-to-audio-route-changes) - Observe audio session notifications to ensure that your app responds appropriately to route changes.
- [Adding synthesized speech to calls](https://developer.apple.com/documentation/avfaudio/adding-synthesized-speech-to-calls) - Provide a more accessible experience by adding your app's audio to a call.
- [Capturing stereo audio from built-In microphones](https://developer.apple.com/documentation/avfaudio/capturing-stereo-audio-from-built-in-microphones) - Configure an iOS device's built-in microphones to add stereo recording capabilities to your app.
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

- **AVAudioSessionCapability** - Describes whether a specific capability is supported and if that capability is currently enabled
- **AVAudioSessionPortExtensionBluetoothMicrophone** - An object that describes capabilities of Bluetooth microphone ports.
### Protocols

- **AVAudioSessionSpatialExperience**

### Variables

- **AVAudioSessionSetActiveFlags_NotifyOthersOnDeactivation** - A flag that indicates that when your audio session deactivates, any audio sessions that your audio session interrupted can reactivate themselves. (Deprecated)
- **AVEncoderASPFrequencyKey**
- **AVEncoderContentSourceKey**
- **AVEncoderDynamicRangeControlConfigurationKey**
- **AVSampleRateConverterAlgorithm_Mastering** - Selects the mastering sample-rate conversion algorithm.
- **AVSampleRateConverterAlgorithm_MinimumPhase** - Selects the minimum-phase sample-rate conversion algorithm.
- **AVSampleRateConverterAlgorithm_Normal** - Selects the normal sample-rate conversion algorithm.

### Functions

- **AVMakeBeatRange** - Creates a beat range with the specified start time and length.

### Type Aliases

- **AVAudioConverterInputBlock** - A block to get input data for conversion, as necessary.
- **AVBeatRange**
- **AVMIDIPlayerCompletionHandler** - A callback the system invokes when MIDI playback completes.

### Enumerations

- **AVAudioContentSource**
- **AVAudioDynamicRangeControlConfiguration**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AVFAudio)*
