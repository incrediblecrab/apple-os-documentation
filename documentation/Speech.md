# Speech

Perform speech recognition on live or prerecorded audio, and receive transcriptions, alternative interpretations, and confidence levels of the results.

**Platforms:** iOS 10.0+ | iPadOS 10.0+ | Mac Catalyst 13.1+ | macOS 10.15+ | visionOS 1.0+

## Overview

Use the Speech framework to recognize spoken words in recorded or live audio. The keyboard's dictation support uses speech recognition to translate audio content into text. This framework provides a similar behavior, except that you can use it without the presence of the keyboard. For example, you might use speech recognition to recognize verbal commands or to handle text dictation in other parts of your app.

SpeechTranscriber and other modules provide specific services. AssetInventory manages the assets they need. The SpeechAnalyzer actor manages their analysis session.

[`SpeechAnalyzer`](https://developer.apple.com/documentation/speech/speechanalyzer.md) and [`SpeechTranscriber`](https://developer.apple.com/documentation/speech/speechtranscriber.md) declare iOS, iPadOS, Mac Catalyst, macOS, tvOS, and visionOS 26.0+ availability. These newer APIs do not share the legacy framework's minimum versions. Check `SpeechTranscriber.isAvailable` and `supportedLocales`; Apple recommends disabling the feature or considering `DictationTranscriber` when its models are unsupported.

For a general understanding of how you use these classes together, see SpeechAnalyzer.

Speech recognition and system action integration are separate tasks. Use [App Intents](AppIntents.md) for modern Siri-accessible actions; [SiriKit](SiriKit.md) retains legacy support for most existing Siri interactions. Do not infer a Speech API's availability or a SiriKit removal date from changes to the assistant.

Check each transcription module's hardware, language, authorization, and asset requirements. Keep an appropriate fallback when permission is denied, model assets are unavailable, or an offline transcription path isn't supported.

## Topics

### Essentials
- [Bringing advanced speech-to-text capabilities to your app](https://developer.apple.com/documentation/speech/bringing-advanced-speech-to-text-capabilities-to-your-app.md) - Learn how to incorporate live speech-to-text transcription into your app with SpeechAnalyzer.
- **SpeechAnalyzer** - Analyzes spoken audio content in various ways and manages the analysis session.
- **AssetInventory** - Manages the assets that are necessary for transcription or other analyses.

### Modules
- **SpeechTranscriber** - A speech-to-text transcription module that's appropriate for normal conversation and general purposes.
- **DictationTranscriber** - A speech-to-text transcription module that's similar to system dictation features and compatible with older devices.
- **SpeechDetector** - A module that performs a voice activity detection (VAD) analysis.
- **SpeechModule** - Protocol that all analyzer modules conform to.
- **LocaleDependentSpeechModule** - If a module conforms to this protocol, then its assets depend on the locale setting.

### Input and output
- **AnalyzerInput** - Time-coded audio data.
- **SpeechModuleResult** - Protocol that all module results conform to.

### Custom vocabulary
- **AnalysisContext** - Contextual information that may be shared among analyzers.
- **SFSpeechLanguageModel** - A language model built from custom training data.
- **SFSpeechLanguageModel.Configuration** - An object describing the location of a custom language model and specialized vocabulary.
- **SFCustomLanguageModelData** - An object that generates and exports custom language model training data.

### Asset and resource management
- **AssetInstallationRequest** - An object that describes, downloads, and installs a selection of assets.
- **SpeechModels** - Namespace for methods related to model management.

### Legacy API
- [Speech Recognition in Objective-C](https://developer.apple.com/documentation/speech/speech-recognition-in-objc.md) - Use these classes to perform speech recognition in Objective-C code.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Speech)*
