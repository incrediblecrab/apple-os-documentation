# PHASE

Create dynamic audio experiences in your game or app that react to events and cues in the environment.

**Platforms:** iOS 15.0+ | iPadOS 15.0+ | Mac Catalyst 15.0+ | macOS 12.0+ | tvOS 15.0+ | visionOS 1.0+

## Overview

Use **PHASE** (Physical Audio Spatialization Engine) to provide complex, dynamic audio experiences in your games and apps. With PHASE, you can control sound layers and adjust audio parameters in real time. As you develop your app, dynamic integration with your app's visual scene enables audio to react to logic and visual changes automatically. The framework supports various audio hardware, which enables your app to provide a consistent spatial audio experience across platforms and output devices like headphones and speakers.

**Note:** If the audio in your game or app doesn't incorporate environmental events or cues, you can use AVFoundation or Core Audio.

### Integrate Audio with Visual Simulation

Apps and games that model a detailed environment involve substantial revision during development. When you provide PHASE with a basic understanding of your app's scene, audio plays in accordance with the scene's characteristics. As you modify the scene, such as by adding a game level, the audio follows along by accommodating the level's visual shape and properties. PHASE couples sound with visuals and minimizes your app's audio maintenance by:

- Accepting scene geometry and reducing the volume of obstructed, sound-emitting scene objects. For example, PHASE lowers the volume of an incoming fireball when the player takes cover behind a wall.
- Offering complex sound events that play in reaction to your app's runtime state.
- Adding sound effects that emanate from a shape. When you provide the shape of a scene object to PHASE, the sound's volume scales based on the player's distance and orientation relative to the shape.
- Adding reverberation and timed audio reflection to create environmental effects and simulate indoor scenes.

## Topics

### Essentials
- [Playing sound from a location in a 3D scene](https://developer.apple.com/documentation/phase/playing_sound_from_a_location_in_a_3d_scene) - Position sound from a specific direction and automatically raise or lower volume based on the environment.
- [Personalizing spatial audio in your app](https://developer.apple.com/documentation/phase/personalizing_spatial_audio_in_your_app) - Enhance the realism of spatial audio output by tracking a person's head movement and accounting for their personal spatial audio profile.
- [PHASE updates](https://developer.apple.com/documentation/phase/phase_updates) - Learn about important changes to PHASE.

### Setup
- **PHASEEngine** - An object that manages audio assets, controls playback, and configures environmental effects.
- **UpdateMode** - Modes that determine when the framework consumes API calls and updates internal state.
- **RenderingMode** - Modes that determine whether the system renders audio in process or out of process. (Beta)
- **PHASEAssetRegistry** - A central repository of audio assets.
- **PHASENormalizationMode** - Options that determine whether the framework adjusts a sound asset's loudness for the user's output device.
- **PHASESpatializationMode** - The manner in which PHASE outputs spatial audio.
- **PHASEReverbPreset** - The manner in which PHASE diffuses resonating sound.
- **PHASEMedium** - A property or quality of the environment that affects how sound travels.

### Soundscape Creation
- **PHASESource** - An object that plays audio from a 3D location and orientation in a scene.
- **PHASEListener** - A central point of reference that defines the location within the scene that's most audible to the user.
- **PHASEOccluder** - An object with a shape and position that blocks audio from reaching the listener.
- **PHASEObject** - An object in the scene.
- **PHASEShape** - A collection of points that connect to form a 3D volume.
- **Element** - An object that describes the characteristics of a physical surface.
- **PHASEMaterial** - Surface characteristics that determine the acoustic properties of an object.
- **PHASEMaterialPreset** - A collection of physical surfaces that each add a unique acoustic quality to your app's audio.
- **PHASEMixerParameters** - An object that specifies a mixer for sound events and orients them in 3D space.

### Audio Selection and Playback
- **PHASESoundAsset** - A sound resource stored in the asset registry.
- **PHASESoundEvent** - An object that determines which audio to play.
- **RenderingState** - The playback status of audio.
- **PHASESoundEventNodeDefinition** - A base class for sound event nodes that connect to form a node hierarchy.
- **PHASESoundEventNodeAsset** - A template object for sounds that can play in reaction to environmental state.
- **PHASEAsset** - A base class that adds a name to framework assets.

### Sound Event Nodes
Objects that connect to form a hierarchical tree of audio actions.

### Audio Layering and Effects
- **PHASEChannelMixerDefinition** - An audio-layering object that routes sound directly to the device's output.
- **PHASEAmbientMixerDefinition** - An audio-layering object that outputs sound in a particular direction in 3D space.
- **PHASEMixerDefinition** - An object to initialize a mixer with a given configuration.
- **PHASEMixer** - An object that combines multiple audio signals into a single signal.
- **PHASEDefinition** - A base class that adds a name to framework definitions.

### Spatial Mixing
Define environmental characteristics that determine how sound plays in your app's 3D soundscape.

### Dynamic Sound Control
- **PHASEEnvelope** - A collection of segments that connect to graph a complex curve over a linear input.
- **PHASEEnvelopeSegment** - A curved portion of an envelope.
- **PHASECurveType** - Options that apply a mathematical function to an input value.
- **PHASENumericPair** - An ordered pair that defines a bounding box for an envelope.

### Playback Parameterization
Change the characteristics of in-flight audio by adjusting its properties at runtime.

### Sound Grouping and Management
- **PHASEGroup** - A container that shares audio parameters with a collection of sounds.
- **PHASEGroupPreset** - A collection of settings for groups.
- **PHASEGroupPresetSetting** - Settings for group presets.
- **PHASEDucker** - An object that manages competing sounds.

### Errors
- **PHASE Errors** - Errors that the PHASE framework reports.

### Classes
- **PHASEPullStreamNode**
- **PHASEPullStreamNodeDefinition**
- **PHASEStreamNode**

### Structures
- **PHASEAutomaticHeadTrackingFlags**

### Type Aliases
- **PHASEPullStreamRenderHandler**

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/PHASE)*