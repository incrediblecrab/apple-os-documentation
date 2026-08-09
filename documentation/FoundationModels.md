# Foundation Models

Perform tasks with the on-device model that specializes in language understanding, structured output, and tool calling.

**Platforms:** iOS 26.0+ | iPadOS 26.0+ | Mac Catalyst 26.0+ | macOS 26.0+ | visionOS 26.0+

## Overview

The Foundation Models framework provides access to Apple's on-device large language model that powers Apple Intelligence to help you perform intelligent tasks specific to your use case. The text-based on-device model identifies patterns that allow for generating new text that's appropriate for the request you make, and it can make decisions to call code you write to perform specialized tasks.

An illustration that represents a foundation model.

Generate text content based on requests you make. The on-device model excels at a diverse range of text generation tasks, like summarization, entity extraction, text understanding, refinement, dialog for games, generating creative content, and more.

Generate entire Swift data structures with guided generation. With the @Generable macro, you can define custom data structures and the framework provides strong guarantees that the model generates instances of your type.

To expand what the on-device foundation model can do, use Tool to create custom tools that the model can call to assist with handling your request. For example, the model can call a tool that searches a local or online database for information, or calls a service in your app.

To use the on-device language model, people need to turn on Apple Intelligence on their device. For a list of supported devices, see Apple Intelligence.

For more information about acceptable usage of the Foundation Models framework, see Acceptable use requirements for the Foundation Models framework.

## What's New in OS 27

> **iOS 27+, iPadOS 27+, macOS Golden Gate 27+, visionOS 27+:** Foundation Models generalizes beyond Apple's on-device model.

**The `LanguageModel` protocol**

The framework now exposes a generalized `LanguageModel` protocol. Your app can target Apple's on-device model or any conformant provider, including cloud models — Google Gemini is available as an optional cloud model for certain Siri features, alongside other providers such as Claude. Write against the protocol rather than a concrete model type so provider choice stays a configuration decision.

**Siri**

Siri itself is rebuilt on Apple Foundation Models in OS 27, with extended conversational context, cross-app awareness, and multi-step in-app actions. Apps that expose good App Intents schemas become actionable through that assistant. See [App Intents](AppIntents.md).

**Validating model-backed features**

Model output is non-deterministic, so unit tests alone are insufficient. The new [Evaluations](Evaluations.md) framework is designed for validating AI feature behavior.

> **Note:** Multimodal prompt support and Dynamic Profiles were reported among the OS 27 additions but could not be confirmed against a published Apple documentation page. Verify against the [Foundation Models documentation](https://developer.apple.com/documentation/foundationmodels) before depending on them.

## Topics

### Essentials
- [Generating content and performing tasks with Foundation Models](https://developer.apple.com/documentation/foundationmodels/generating_content_and_performing_tasks_with_foundation_models) - Enhance the experience in your app by prompting an on-device large language model.
- [Improving safety from generative model output](https://developer.apple.com/documentation/foundationmodels/improving_safety_from_generative_model_output) - Create generative experiences that appropriately handle sensitive inputs and respect people.
- [Adding intelligent app features with generative models](https://developer.apple.com/documentation/foundationmodels/adding_intelligent_app_features_with_generative_models) - Build robust apps with guided generation and tool calling by adopting the Foundation Models framework.
- **class SystemLanguageModel** - An on-device large language model capable of text-generation tasks.
- **struct UseCase** - A type that represents the use case for prompting.

### Prompting
- **class LanguageModelSession** - An object that represents a session that interacts with a large language model.
- **struct Instructions** - Instructions define the model's intended behavior on prompts.
- **struct Prompt** - A prompt from a person to the model.
- **struct Transcript** - A transcript that documents interactions with a language model. Transcripts contain an ordered list of entries, representing inputs to and outputs from the model.
- **struct GenerationOptions** - Options that control how the model generates its response to a prompt.

### Guided generation
- [Generating Swift data structures with guided generation](https://developer.apple.com/documentation/foundationmodels/generating_swift_data_structures_with_guided_generation) - Create robust apps by describing output you want programmatically.
- **protocol Generable** - A type that the model uses when responding to prompts.

### Tool calling
- [Expanding generation with tool calling](https://developer.apple.com/documentation/foundationmodels/expanding_generation_with_tool_calling) - Build tools that enable the model to perform tasks that are specific to your use case.
- [Generate dynamic game content with guided generation and tools](https://developer.apple.com/documentation/foundationmodels/generate_dynamic_game_content_with_guided_generation_and_tools) - Make gameplay more lively with AI generated dialog and encounters personalized to the player.
- **protocol Tool** - A tool that a model can call to gather information at runtime or perform side effects.

### Feedback
- **struct LanguageModelFeedbackAttachment** - Feedback appropriate for attaching to Feedback Assistant.

**Note:** To use the Foundation Models framework, people need to turn on Apple Intelligence on their device. For a list of supported devices, see Apple Intelligence documentation.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/FoundationModels)*
