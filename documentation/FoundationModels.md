# Foundation Models

Perform tasks with the on-device model that specializes in language understanding, structured output, and tool calling.

**Platforms:** iOS 26.0+ (Beta) | iPadOS 26.0+ (Beta) | Mac Catalyst 26.0+ (Beta) | macOS 26.0+ (Beta) | visionOS 26.0+ (Beta)

## Overview

The Foundation Models framework provides access to Apple's on-device large language model that powers Apple Intelligence to help you perform intelligent tasks specific to your use case. The text-based on-device model identifies patterns that allow for generating new text that's appropriate for the request you make, and it can make decisions to call code you write to perform specialized tasks.

An illustration that represents a foundation model.

Generate text content based on requests you make. The on-device model excels at a diverse range of text generation tasks, like summarization, entity extraction, text understanding, refinement, dialog for games, generating creative content, and more.

Generate entire Swift data structures with guided generation. With the @Generable macro, you can define custom data structures and the framework provides strong guarantees that the model generates instances of your type.

To expand what the on-device foundation model can do, use Tool to create custom tools that the model can call to assist with handling your request. For example, the model can call a tool that searches a local or online database for information, or calls a service in your app.

To use the on-device language model, people need to turn on Apple Intelligence on their device. For a list of supported devices, see Apple Intelligence.

For more information about acceptable usage of the Foundation Models framework, see Acceptable use requirements for the Foundation Models framework.

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

**Beta Software**

This documentation contains preliminary information about an API or technology in development. This information is subject to change, and software implemented according to this documentation should be tested with final operating system software.

Learn more about using Apple's beta software

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/FoundationModels)*