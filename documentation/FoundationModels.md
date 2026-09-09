# Foundation Models

Build language and image-understanding features with sessions, structured generation, and tools.

**Original on-device APIs:** iOS 26.0+ | iPadOS 26.0+ | Mac Catalyst 26.0+ | macOS 26.0+ | visionOS 26.0+

## Overview

Foundation Models provides a shared Swift session interface for Apple's on-device model, Private Cloud Compute (PCC), and custom language-model providers. Use it for tasks such as summarization, extraction, image understanding, and tool-assisted workflows. Generated structure is not proof of factual accuracy or authorization to perform an action.

The OS 26 on-device APIs remain useful. The OS 27 additions extend the framework rather than retroactively raising all deployment minimums:

| Surface | Documented availability |
|---|---|
| `SystemLanguageModel` | iOS/iPadOS/Mac Catalyst/macOS/visionOS 26.0+ |
| `LanguageModelSession` | The platforms above at 26.0+; watchOS 27.0+ |
| `LanguageModel`, `LanguageModelExecutor`, `LanguageModelCapabilities` | iOS/iPadOS/Mac Catalyst/macOS/visionOS/watchOS 27.0+ |
| `PrivateCloudComputeLanguageModel` | iOS/iPadOS/Mac Catalyst/macOS/visionOS/watchOS 27.0+ |
| `LanguageModelSession.DynamicProfile`, `ImageAttachmentContent`, `LanguageModelError` | iOS/iPadOS/Mac Catalyst/macOS/visionOS/watchOS 27.0+ |

These declarations do not list tvOS. A session or protocol available on watchOS does not imply an on-device `SystemLanguageModel` there. Check each symbol and the chosen model rather than applying one platform list to the whole framework.

## Topics

### Sessions and structured output

- [`SystemLanguageModel`](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel.md) — Access the on-device Apple model and inspect its availability before use.
- [`LanguageModelSession`](https://developer.apple.com/documentation/foundationmodels/languagemodelsession.md) — Maintain session history and generate or stream responses.
- [`Prompt`](https://developer.apple.com/documentation/foundationmodels/prompt.md), [`Instructions`](https://developer.apple.com/documentation/foundationmodels/instructions.md), and [`GenerationOptions`](https://developer.apple.com/documentation/foundationmodels/generationoptions.md) — Separate task input, intended behavior, and generation settings.
- [`Generable`](https://developer.apple.com/documentation/foundationmodels/generable.md) and [guided generation](https://developer.apple.com/documentation/foundationmodels/generating-swift-data-structures-with-guided-generation.md) — Describe structured output with `@Generable` and `@Guide`; validate business constraints after generation.
- [`Tool`](https://developer.apple.com/documentation/foundationmodels/tool.md) — Define named, typed operations callable by a model. Check arguments, authorization, and side effects in the implementation.
- [Transcripts](https://developer.apple.com/documentation/foundationmodels/transcripts.md) — Inspect session entries and attachments for debugging and evaluation.

### Custom providers

[`LanguageModel`](https://developer.apple.com/documentation/foundationmodels/languagemodel.md) describes capabilities and an `executorConfiguration`. Its associated executor bridges the framework to a server API or local inference engine. [`LanguageModelExecutor`](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutor.md) implements `init(configuration:)`, `prewarm(model:transcript:)`, and `respond(to:model:streamingInto:)`; the generation channel carries output deltas back to the session.

Use [`LanguageModelCapabilities`](https://developer.apple.com/documentation/foundationmodels/languagemodelcapabilities.md) to describe supported behavior. A common session interface does not make every model equally capable of image input, guided generation, tools, or reasoning.

Apple's [iOS overview](https://developer.apple.com/ios/whats-new/) names cloud models such as Claude and Gemini as provider examples. That is **not** evidence that Apple ships a package, account, or entitlement for every named provider. Obtain and verify the actual implementation, credentials, terms, and capabilities separately. For local models, see [running a Core AI model in a session](https://developer.apple.com/documentation/foundationmodels/running-a-core-ai-model-in-a-foundation-models-session.md) and [Core AI](CoreAI.md).

### Multimodal input

- [Analyzing images with multimodal prompting](https://developer.apple.com/documentation/foundationmodels/analyzing-images-with-multimodal-prompting.md) — Include text and images in a request, with an appropriate orientation and a clear analysis task.
- [`Attachment`](https://developer.apple.com/documentation/foundationmodels/attachment.md), [`ImageAttachmentContent`](https://developer.apple.com/documentation/foundationmodels/imageattachmentcontent.md), and [`ImageReference`](https://developer.apple.com/documentation/foundationmodels/imagereference.md) — Supply image data and refer to it from tools or a transcript.
- [Vision](Vision.md) provides [`OCRTool`](https://developer.apple.com/documentation/vision/ocrtool.md) and [`BarcodeReaderTool`](https://developer.apple.com/documentation/vision/barcodereadertool.md) for a session's image-analysis toolset.

Supported image inputs include `CGImage`, `CIImage`, `CVPixelBuffer`, and image URLs. Create them through `Attachment` initializers, not by constructing `ImageAttachmentContent` directly. Model support is still required; an attachment type's availability does not promise that any custom provider can consume it.

### Dynamic Profiles

[Dynamic sessions](https://developer.apple.com/documentation/foundationmodels/composing-dynamic-sessions-with-instructions-and-profiles.md) reevaluate instructions and tools as app state changes:

- [`DynamicInstructions`](https://developer.apple.com/documentation/foundationmodels/dynamicinstructions.md) supplies instructions and tools before each model request.
- [`LanguageModelSession.Profile`](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/profile.md) associates those instructions with session-level configuration, including a model.
- [`LanguageModelSession.DynamicProfile`](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofile.md) selects one active profile; changes take effect on the next model request while preserving the session.

Profile transitions can change the model, tools, and data destination. Make those transitions explicit in the app's configuration and test them, especially when moving from on-device to remote processing.

### Private Cloud Compute

[`PrivateCloudComputeLanguageModel`](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel.md) uses Apple's server model for stronger reasoning and a larger context window. [The adoption article](https://developer.apple.com/documentation/foundationmodels/adding-server-side-intelligence-with-private-cloud-compute.md) documents a network requirement, runtime `availability`, daily request limits, `quotaUsage`, and `Error.quotaLimitReached(_:)`.

Access requires eligibility and a managed entitlement. At this cutoff, Apple's [access page](https://developer.apple.com/private-cloud-compute/) limits no-cloud-API-cost access to App Store Small Business Program developers with the entitlement assigned to their account and fewer than two million first-time App Store downloads from any of their apps. Eligible App Store apps can use PCC where Apple Intelligence is available; TestFlight and ad hoc testing are also permitted, with testing installs excluded from that download count. This is **conditional access**, not universally free or unlimited PCC. Consult the access page for continued-eligibility and migration terms.

Apple model access also depends on supported hardware, Apple Intelligence availability, region, and runtime readiness. Check the actual model before presenting the feature. A successful availability check does not eliminate later quota, network, or generation failures.

### Errors and fallback

[`LanguageModelError`](https://developer.apple.com/documentation/foundationmodels/languagemodelerror.md) covers context overflow, rate limits, timeouts, refusal, guardrail violations, unsupported capabilities, unsupported transcript content, unsupported generation guides, and unsupported languages/locales. OS 26 integrations must retain handling appropriate to their older API surface.

For loss of connectivity or unavailable PCC, use an eligible on-device model **only if it supports the task**, or offer a non-AI path. Do not assume all devices have an offline Apple model. Do not silently retry a refused request against another provider or automatically send private content to a server to work around an on-device failure.

## Validation

Use [Evaluations](Evaluations.md) for per-model and per-profile quality, judge calibration, and tool trajectories; use [Swift Testing](Testing.md) for deterministic validation and error handling. Record OS, model configuration, language/region, toolset, dataset, and entitlement state. [Xcode's Foundation Models instrument](Xcode.md#profiling) helps investigate latency and token usage.

Follow the [intelligence integration recipe](../guides/intelligence-integration.md). For exposing app actions to the system, use [App Intents](AppIntents.md); implementing a `LanguageModel` is a different integration.

*Sources: [Foundation Models](https://developer.apple.com/documentation/foundationmodels.md), [`LanguageModel`](https://developer.apple.com/documentation/foundationmodels/languagemodel.md), [iOS developer overview](https://developer.apple.com/ios/whats-new/).*
