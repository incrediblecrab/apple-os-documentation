# Speech

Perform speech recognition on live or prerecorded audio, and receive transcriptions, alternative interpretations, and confidence levels of the results.

**Platforms:** iOS 10.0+ | iPadOS 10.0+ | Mac Catalyst 13.1+ | macOS 10.15+ | visionOS 1.0+

## Overview

Use the Speech framework to recognize spoken words in recorded or live audio. The keyboard's dictation support uses speech recognition to translate audio content into text. This framework provides a similar behavior, except that you can use it without the presence of the keyboard. For example, you might use speech recognition to recognize verbal commands or to handle text dictation in other parts of your app.

The SpeechTranscriber class and other module classes provide specific services. The AssetInventory class ensures that the system has the assets necessary to support those classes. The SpeechAnalyzer class manages an analysis session that uses those classes.

For a general understanding of how you use these classes together, see SpeechAnalyzer.

> **iOS 27+, iPadOS 27+, macOS Golden Gate 27+, watchOS 27+, visionOS 27+:** Siri is rebuilt on Apple Foundation Models with extended conversational context and multi-step in-app actions. **[SiriKit is deprecated](SiriKit.md)** — voice-driven app functionality should be exposed through [App Intents](AppIntents.md), not SiriKit intents.

## Topics

### Essentials
- [Bringing advanced speech-to-text capabilities to your app](https://developer.apple.com/documentation/speech/bringing_advanced_speech-to-text_capabilities_to_your_app) - Learn how to incorporate live speech-to-text transcription into your app with SpeechAnalyzer.
- **SpeechAnalyzer** - Analyzes spoken audio content in various ways and manages the analysis session.- **AssetInventory** - Manages the assets that are necessary for transcription or other analyses.
### Modules
- **SpeechTranscriber** - A speech-to-text transcription module that's appropriate for normal conversation and general purposes.- **DictationTranscriber** - A speech-to-text transcription module that's similar to system dictation features and compatible with older devices.- **SpeechDetector** - A module that performs a voice activity detection (VAD) analysis.- **SpeechModule** - Protocol that all analyzer modules conform to.- **LocaleDependentSpeechModule** - If a module conforms to this protocol, then its assets depend on the locale setting.
### Input and output
- **AnalyzerInput** - Time-coded audio data.- **SpeechModuleResult** - Protocol that all module results conform to.
### Custom vocabulary
- **AnalysisContext** - Contextual information that may be shared among analyzers.- **SFSpeechLanguageModel** - A language model built from custom training data.
- **Configuration** - An object describing the location of a custom language model and specialized vocabulary.
- **SFCustomLanguageModelData** - An object that generates and exports custom language model training data.

### Asset and resource management
- **AssetInstallationRequest** - An object that describes, downloads, and installs a selection of assets.- **SpeechModels** - Namespace for methods related to model management.
### Legacy API
- [Speech Recognition in Objective-C](https://developer.apple.com/documentation/speech/speech_recognition_in_objective-c) - Use these classes to perform speech recognition in Objective-C code.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Speech)*
