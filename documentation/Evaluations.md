# Evaluations

Measure the quality of intelligence-powered features with datasets and explicit metrics.

**Tools:** Xcode 27.0+

**Platforms:** iOS 27.0+ | iPadOS 27.0+ | Mac Catalyst 27.0+ | macOS 27.0+ | visionOS 27.0+ | watchOS 27.0+

Apple's framework and core-symbol metadata do **not** list tvOS. Model availability remains a separate constraint from the evaluation framework's availability.

## Overview

Evaluations runs an app feature against a dataset, scores each result, and aggregates measurements. Use it to compare prompts or providers and detect quality regressions. Retain deterministic unit tests for parsing, authorization, business rules, and tool implementations.

An evaluation can call any model integrated through [Foundation Models](FoundationModels.md), including a custom provider. This does not grant access to a model: check device eligibility, runtime, region, entitlements, connectivity, and quota before a model-backed run.

## Topics

### Define the evaluation

- [`Evaluation`](https://developer.apple.com/documentation/evaluations/evaluation.md) — Supply `dataset`, implement `subject(from:)`, declare `evaluators`, and aggregate metrics in `aggregateMetrics(using:)`.
- [`ModelSample`](https://developer.apple.com/documentation/evaluations/modelsample.md) — Pair a prompt with optional expected output and tool-call expectations.
- [`ModelSubject`](https://developer.apple.com/documentation/evaluations/modelsubject.md) — Return the feature's output and, when needed, the session's structured transcript.
- [Evaluating language model responses](https://developer.apple.com/documentation/evaluations/evaluating-language-model-responses.md) — Follow the complete dataset-to-report workflow.

### Load datasets

- [`Loader`](https://developer.apple.com/documentation/evaluations/loader.md) — Provide a dataset through a `Sendable` loader.
- [`ArrayLoader`](https://developer.apple.com/documentation/evaluations/arrayloader.md) — Use an in-memory sample set.
- [`JSONLoader`](https://developer.apple.com/documentation/evaluations/jsonloader.md) — Load JSON or JSONL samples. Malformed entries are logged and skipped; failure to open the file throws. Validate the loaded sample count rather than silently accepting a reduced dataset.
- [`StreamLoader`](https://developer.apple.com/documentation/evaluations/streamloader.md) — Supply samples from an asynchronous sequence.
- [`SampleGenerator`](https://developer.apple.com/documentation/evaluations/samplegenerator.md) — Expand a dataset synthetically; review generated cases rather than treating them as independent ground truth.

### Score and aggregate

- [`Metric`](https://developer.apple.com/documentation/evaluations/metric.md) — Name a measurement and return `passing(rationale:)`, `failing(rationale:)`, `scoring(_:rationale:)`, or [`ignore(rationale:)`](https://developer.apple.com/documentation/evaluations/metric/ignore(rationale:).md). Ignored results are excluded from aggregation.
- [`Evaluator`](https://developer.apple.com/documentation/evaluations/evaluator.md) — Apply a closure-based check to each sample and subject.
- [`MetricsAggregator`](https://developer.apple.com/documentation/evaluations/metricsaggregator.md) — Compute summaries such as means and maxima, and organize related metrics into groups.
- [`EvaluationResult`](https://developer.apple.com/documentation/evaluations/evaluationresult.md) — Read aggregate `summary`, per-sample `detailed`, and the formatted `groupedSummary`.
- [`ResultColumn`](https://developer.apple.com/documentation/evaluations/resultcolumn.md) — Access typed result columns, including an evaluation's `inputColumn`, `responseColumn`, and `expectedColumn`.

Use separate metrics for output correctness, refusal handling, tool selection, and latency. A high average can hide a failed category; inspect per-sample outcomes and record skipped or ignored cases.

[`aggregateValue(_:)`](https://developer.apple.com/documentation/evaluations/evaluationresult/aggregatevalue(_:).md) returns `-1` when it finds no matching aggregate. Check that the requested metric exists before interpreting that value or applying a threshold.

### Model-judge evaluation

- [`ModelJudgeEvaluator`](https://developer.apple.com/documentation/evaluations/modeljudgeevaluator.md) — Score subjective qualities with pointwise ratings or pairwise comparisons.
- [`ScoreDimension`](https://developer.apple.com/documentation/evaluations/scoredimension.md) — Define separately measurable dimensions and scoring criteria.
- [`ModelJudgePrompt`](https://developer.apple.com/documentation/evaluations/modeljudgeprompt.md) — Configure the judge's instructions, targets, and reference material.
- [Scoring with model-judge evaluators](https://developer.apple.com/documentation/evaluations/scoring-with-model-as-judge-evaluators.md) — Configure scoring and compare results with human review.

Record the judge model and configuration as well as the model under test. A judge is another fallible model, not an authority on correctness; calibrate it against reviewed examples.

### Tool-call evaluation

- [`ToolCallEvaluator`](https://developer.apple.com/documentation/evaluations/toolcallevaluator.md) — Compare actual tool calls from a structured transcript with expectations.
- [`TrajectoryExpectation`](https://developer.apple.com/documentation/evaluations/trajectoryexpectation.md) and [`ToolExpectation`](https://developer.apple.com/documentation/evaluations/toolexpectation.md) — Describe expected calls and ordering.
- [`ArgumentMatcher`](https://developer.apple.com/documentation/evaluations/argumentmatcher.md) — Check arguments exactly, against allowed values, or within a range.
- [Evaluating tool-calling behavior](https://developer.apple.com/documentation/evaluations/evaluating-tool-calling-behavior.md) — Capture `session.transcript.structuredTranscript` in the subject and score the trajectory as well as the final output.

The transcript is required for tool-call evaluation. A `nil` transcript throws [`EvaluationError.missingTranscript(evaluatorType:)`](https://developer.apple.com/documentation/evaluations/evaluationerror/missingtranscript(evaluatortype:).md); it does not mean the model made no tool calls.

Use test doubles for side-effecting tools. A trajectory score does not verify a tool's implementation, and evaluation should not send real messages, spend money, or modify a person's data.

### Swift Testing integration

[`EvaluationTrait`](https://developer.apple.com/documentation/evaluations/evaluationtrait.md), attached with `@Test(.evaluates(...))`, runs the evaluation and records result attachments. Inside the test, [`EvaluationContext.current.result`](https://developer.apple.com/documentation/evaluations/evaluationcontext.md) provides the result for threshold assertions. Open the **Evaluations** item under the test run in Xcode's Report navigator.

For a non-test runner, [`Evaluation.run(info:)`](https://developer.apple.com/documentation/evaluations/evaluation/run(info:).md) runs the evaluation directly.

An evaluation can finish despite individual inference or evaluator failures. Inspect the `SubjectInferenceError` and `EvaluatorErrors` columns in `detailed` when present; failed subjects have a `nil` response. A returned result or a passing aggregate is not proof that every sample completed successfully.

## Validation and runtime limits

Version the dataset, prompts, tools, model configuration, and acceptance thresholds. Include unavailable-model, offline, denied-access, quota, cancellation, and unsupported-input cases. Report infrastructure failures separately from quality scores; never count an unavailable model as a passing evaluation.

These are beta APIs at the September 8, 2026 cutoff. Validate the suite on each intended runtime, with the actual model access it needs. See [Swift Testing](Testing.md), [App Intents Testing](AppIntentsTesting.md), [Xcode profiling](Xcode.md#profiling), and the [intelligence integration recipe](../guides/intelligence-integration.md).

*Source: [Evaluations](https://developer.apple.com/documentation/evaluations.md).*
