# Add an evaluated, fallback-safe intelligence feature

Build one text-and-optional-image feature that can use an appropriate model without making the rest of the app depend on model availability.

## Prerequisites and availability

- Define the task, allowed inputs, acceptable output, latency budget, and non-AI fallback before choosing a model.
- Use [Foundation Models](../documentation/FoundationModels.md) as the canonical session/API reference. Original on-device APIs start at iOS/iPadOS/Mac Catalyst/macOS/visionOS 26.0.
- `LanguageModel`, custom executors, image `Attachment`, Dynamic Profiles, and `PrivateCloudComputeLanguageModel` are documented for iOS/iPadOS/Mac Catalyst/macOS/visionOS/watchOS **27.0+**. This does not establish an on-device Apple model on watchOS or support on tvOS.
- [Evaluations](../documentation/Evaluations.md) requires Xcode 27 and iOS/iPadOS/Mac Catalyst/macOS/visionOS/watchOS 27.0+; it does **not** list tvOS.
- Record model, runtime, hardware, language/region, asset readiness, and credential/entitlement status—not secret values. Compilation alone cannot verify access.

## 1. Choose the narrowest suitable API

Use [Translation](../documentation/Translation.md), [Speech](../documentation/Speech.md), [Vision](../documentation/Vision.md), [Media Intelligence](../documentation/MediaIntelligence.md), or [Music Understanding](../documentation/MusicUnderstanding.md) when a documented domain API directly solves the task.

For your own neural model, [Core AI](../documentation/CoreAI.md) provides `AIModelAsset`, `AIModel`, `InferenceFunction`, and `NDArray`, plus specialization and caching. Install Xcode's Metal Toolchain for `.aimodel` builds. Keep [Core ML](../documentation/CoreML.md) for supported non-neural models such as decision trees; Core AI is not a blanket replacement.

For a language-model workflow, begin with a session and a representative task dataset. Evaluate before adding a remote model merely because it has a larger context window.

## 2. Implement model availability as a state, not a one-time assumption

Inspect `SystemLanguageModel.default.availability` before offering the on-device feature. Its documented unavailable reasons include `deviceNotEligible`, `appleIntelligenceNotEnabled`, and `modelNotReady`. Keep a general unavailable branch for future reasons and offer the non-AI path.

Create a `LanguageModelSession` only with an appropriate model. An initially available model can still fail during generation; keep the feature's error state independent of the app's ordinary editing or browsing state.

For PCC, create a `PrivateCloudComputeLanguageModel()` instance and inspect its `availability` and `quotaUsage`. Access requires an approved managed entitlement and continued eligibility. Apple's [access page](https://developer.apple.com/private-cloud-compute/) documents no cloud API cost only for qualifying Small Business Program developers whose apps meet the first-time-download condition. PCC is neither universally free nor unlimited, and requires a network connection.

## 3. Keep the provider boundary explicit

If using a custom provider, implement or obtain an actual [`LanguageModel`](https://developer.apple.com/documentation/foundationmodels/languagemodel.md) conformance. Inspect its `capabilities` and `executorConfiguration`.

Its [`LanguageModelExecutor`](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutor.md) translates a `LanguageModelExecutorGenerationRequest` in `respond(to:model:streamingInto:)` and streams output through `LanguageModelExecutorGenerationChannel`. Validate supported options, credential errors, timeouts, and cancellation at this boundary.

Apple's mention of Claude or Gemini does not establish a bundled provider package or an account for your app. Verify the package, service terms, credentials, and supported capabilities separately. Do not silently send content to a remote provider when a local request fails.

## 4. Bound the prompt, output, and tools

- Separate `Instructions` from task input and validate content size.
- Describe structured output with `@Generable` and `@Guide`, then validate factual and business constraints. A generated Swift value is not automatically correct.
- For image input, use `Attachment` with the correct image orientation and meaningful labels. Check that the chosen model supports the input; use `ImageReference` when an image is passed to a custom tool.
- If OCR or barcode extraction is needed, consider Vision's documented model tools. Their platform lists differ, and both `OCRTool` and `BarcodeReaderTool` are unavailable in Simulator; validate them on supported physical devices. See [Vision](../documentation/Vision.md#os-27-model-tools).
- Expose the smallest useful `Tool` set. Validate arguments, authenticate access, and confirm side effects in application code. Model output must not directly authorize a purchase, message, or data change.

If the toolset or model changes with task state, use `DynamicInstructions`, `LanguageModelSession.Profile`, and `LanguageModelSession.DynamicProfile`. Exactly one profile is active; changes apply on the next model request. Test that a transition does not retain unintended tools or change the processing destination without the app's intended configuration.

## 5. Provide explicit failure and offline paths

| Condition | Safe behavior |
|---|---|
| Unsupported device, disabled intelligence, unready model, or denied access | Explain the unavailable feature and retain ordinary app functionality |
| PCC network failure or quota exhaustion | Use a suitable, available on-device model or non-AI path; do not assume every device has that model |
| Rate limit or timeout | Bound retries and retain cancellation; do not loop indefinitely |
| Context overflow | Reduce or reset context deliberately without losing required task constraints |
| Unsupported language, capability, or transcript content | Offer a supported input/task or the manual path |
| Refusal or guardrail violation | Respect the result; do not switch providers to bypass it |
| Tool or asset failure | Report the action as failed; avoid duplicated side effects and recover or reload safely |

Use OS 27 [`LanguageModelError`](https://developer.apple.com/documentation/foundationmodels/languagemodelerror.md) for generation failures such as context overflow, unsupported input, rate limits, and refusal. Model availability, tool execution, and model-asset failures also need their own checks; PCC separately documents `Error.quotaLimitReached(_:)`. Preserve error handling appropriate to any OS 26 code path.

## 6. Validate before and after changing the model

1. Version the prompts, dataset, toolset, model configuration, and expected outcomes.
2. Implement an `Evaluation`: load `ModelSample` values through `ArrayLoader`, `JSONLoader`, or a custom `Loader`; implement `subject(from:)`; score with `Metric` and `Evaluator`; summarize with `MetricsAggregator`. Assert the loaded sample count: `JSONLoader` logs and skips malformed entries.
3. Capture `session.transcript.structuredTranscript` in `ModelSubject` when checking tool calls. Use `ToolCallEvaluator`, `TrajectoryExpectation`, and `ArgumentMatcher` to test selection, arguments, and order with side-effect-free test doubles.
4. For subjective criteria, configure `ModelJudgeEvaluator`, `ModelJudgePrompt`, and `ScoreDimension`, and calibrate scores against human-reviewed examples.
5. Run with `@Test(.evaluates(...))` and inspect `EvaluationContext.current.result`. Review per-sample failures, including `SubjectInferenceError` and `EvaluatorErrors` columns when present, not only aggregate averages. The runner can continue after individual failures. Check metric presence before threshold comparisons: `aggregateValue(_:)` returns `-1` for a missing aggregate, not a measured result.
6. Test denied access, unavailable assets, offline operation, unsupported locales, cancellation, and provider changes. In Xcode's Run scheme options, use **Simulated Apple Foundation Models Availability** to test approaching/exhausted PCC quota as documented by Apple.
7. Keep [Swift Testing](../documentation/Testing.md) or [XCTest](../documentation/XCTest.md) coverage for deterministic logic. Use [Xcode profiling](../documentation/Xcode.md#profiling) to compare latency, token usage, and resource costs on representative devices.

An unavailable evaluation environment is a reported limitation, not a passing quality score. These OS 27 APIs remain beta at the September 8, 2026 cutoff; record actual test destinations and unresolved SDK or entitlement limits.

## Sources

- [Foundation Models](https://developer.apple.com/documentation/foundationmodels.md) and [LanguageModel](https://developer.apple.com/documentation/foundationmodels/languagemodel.md)
- [Multimodal prompting](https://developer.apple.com/documentation/foundationmodels/analyzing-images-with-multimodal-prompting.md)
- [Dynamic sessions and profiles](https://developer.apple.com/documentation/foundationmodels/composing-dynamic-sessions-with-instructions-and-profiles.md)
- [Private Cloud Compute adoption](https://developer.apple.com/documentation/foundationmodels/adding-server-side-intelligence-with-private-cloud-compute.md)
- [iOS developer overview](https://developer.apple.com/ios/whats-new/)
- [Core AI](https://developer.apple.com/documentation/coreai.md)
- [Evaluations](https://developer.apple.com/documentation/evaluations.md)
