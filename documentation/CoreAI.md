# Core AI

Prepare and run on-device neural-network models on Apple silicon.

**Platforms:** iOS 27.0+ | iPadOS 27.0+ | Mac Catalyst 27.0+ | macOS 27.0+ | tvOS 27.0+ | visionOS 27.0+ | watchOS 27.0+

## Overview

Core AI provides Swift APIs for loading model assets, specializing them for a device, and running inference across available CPU, GPU, and Neural Engine resources. Its API surface is now documented; it is not limited to an announcement or an unverified session summary.

Start with an `.aimodel` asset. An `AIModelAsset` represents the unspecialized source, while `AIModel` represents a specialization for inference. The framework handles default compute selection and caching, with controls for applications that need to tune preparation time, storage, or execution.

Use [Foundation Models](FoundationModels.md) for its session, structured-generation, and tool-calling abstractions. For a Core AI language model, `CoreAILanguageModel` in Apple's open-source `coreai-models` package conforms to Foundation Models' `LanguageModel` protocol, so a `LanguageModelSession` can run the exported model; see [Running a Core AI model in a Foundation Models session](https://developer.apple.com/documentation/foundationmodels/running-a-core-ai-model-in-a-foundation-models-session.md), which states macOS 27, iOS 27, and Xcode 27 or later. [Core ML](CoreML.md) remains appropriate for non-neural model types, including decision trees and tabular feature engineering.

## Topics

### Assets and inference

- [Integrating on-device AI models](https://developer.apple.com/documentation/coreai/integrating-on-device-ai-models-in-your-app-with-core-ai.md) — Add an `.aimodel` to a target and install Xcode's **Metal Toolchain**, required for building these model assets.
- [`AIModelAsset`](https://developer.apple.com/documentation/coreai/aimodelasset.md) — Represent a source model before specialization.
- [`AIModel`](https://developer.apple.com/documentation/coreai/aimodel.md) — Load with asynchronous `init(contentsOf:options:)`; inspect `functionNames` and use `loadFunction(named:)`.
- [`InferenceFunction`](https://developer.apple.com/documentation/coreai/inferencefunction.md) — Execute [`run(inputs:states:outputViews:)`](https://developer.apple.com/documentation/coreai/inferencefunction/run(inputs:states:outputviews:)-14emi.md). Loading can throw; a missing function name returns `nil`.
- [`InferenceFunctionDescriptor`](https://developer.apple.com/documentation/coreai/inferencefunctiondescriptor.md) and [`InferenceValue`](https://developer.apple.com/documentation/coreai/inferencevalue.md) — Verify the names, shapes, and types of inputs, outputs, and states instead of assuming every model has the same signature.

Supply mutable views for every required state; omitting one causes an error. The shorter `run(inputs:)` call is suitable when the function has no required states. Outputs supplied through `outputViews` are updated in place and are not also returned in the output collection.

### Arrays and images

- [`NDArray`](https://developer.apple.com/documentation/coreai/ndarray.md) — Store multidimensional scalar data. Use mutable views for writes and read-only views for results.
- [`NDArrayDescriptor`](https://developer.apple.com/documentation/coreai/ndarraydescriptor.md) — Describe shape, scalar type, and layout requirements.
- [`ImageDescriptor`](https://developer.apple.com/documentation/coreai/imagedescriptor.md) — Check image dimensions and pixel format before passing image inputs.
- [`ComputeStream`](https://developer.apple.com/documentation/coreai/computestream.md) — Represent asynchronously executed work.

### Specialization and caching

- [Managing specialization and caching](https://developer.apple.com/documentation/coreai/managing-model-specialization-and-caching.md) — Schedule preparation outside latency-sensitive interactions and handle cache misses.
- [`AIModelCache`](https://developer.apple.com/documentation/coreai/aimodelcache.md) — Check cached models by source and options, manage entries, and configure persistence.
- [`SpecializationOptions`](https://developer.apple.com/documentation/coreai/specializationoptions.md) — Keep default compute selection unless measurements justify an override; consider `expectFrequentReshapes` for frequently changing input shapes.
- [`ComputeUnitKind.availableKinds`](https://developer.apple.com/documentation/coreai/computeunitkind/availablekinds.md) — Discover the compute units actually available on the device.
- [Ahead-of-time compilation](https://developer.apple.com/documentation/coreai/compiling-core-ai-models-ahead-of-time.md) — Use `coreai-build` to generate architecture-specific `.aimodelc` assets. This reduces, but does not eliminate, on-device specialization.

OS updates invalidate cached specializations regardless of cache policy. Source-model changes can also invalidate entries, and storage pressure can remove purgeable entries. On tvOS the `.persistent` cache policy is unavailable and cache entries must stay purgeable under storage pressure, so use the default policy there. A persistent cache is not a substitute for a recoverable source-model deployment. Ahead-of-time compilation has a narrower documented hardware scope—devices supporting Apple Intelligence—than the framework's platform list, and it is not supported on tvOS or watchOS.

### Preparation and debugging tools

- [Core AI Optimization](https://apple.github.io/coreai-optimization) and [Core AI PyTorch Extensions](https://apple.github.io/coreai-torch) — Prepare and export models.
- [Core AI Models](https://github.com/apple/coreai-models) — Ready-to-export model examples and Swift inference helpers.
- [Inspecting, debugging, and profiling models](https://developer.apple.com/documentation/coreai/inspecting-debugging-and-profiling-core-ai-models.md) — Use the Xcode model viewer, Core AI debug gauge, Core AI instrument, and [Core AI Debugger](https://developer.apple.com/core-ai-debugger/).
- [`AssetError`](https://developer.apple.com/documentation/coreai/asseterror.md) — Handle asset failures without assuming a usable model was loaded.

## Validation and release-note limitations

Test cold and warm loads, missing assets/functions, incompatible shapes, offline downloads, and cache invalidation on representative hardware. Keep a non-AI or previously supported model path when preparation or inference fails. Use [Evaluations](Evaluations.md) to measure model quality on your own data, including comparing candidate models before you bundle one, and [XCTest](XCTest.md) for deterministic behavior and performance. Apple's [Evaluating a Core AI model](https://developer.apple.com/documentation/evaluations/evaluating-a-core-ai-model.md) sample (macOS 27, Xcode 27) runs one evaluation against a Core AI model and the system on-device model. A Core AI Debugger comparison against a reference run shows whether conversion or optimization changed outputs, not whether the model does your task well.

The [Xcode 27 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes.md) now list three Core AI issues as resolved: unreliable extraction of inputs from prediction events in the Core AI gauge (172502576), inaccurate parameter counts in the Xcode model view for multi-function models that share parameters (177784390), and models that might fail to execute with Metal API Validation enabled (177991751). The notes don't name the build that fixed them, and the Xcode 27.1 and 27.2 notes have no Core AI section. Earlier Xcode 27 beta notes listed 172502576 as a known issue, so on a pre-release build a missing gauge capture still isn't proof that inference had no input.

*Source: [Core AI](https://developer.apple.com/documentation/coreai.md).*
