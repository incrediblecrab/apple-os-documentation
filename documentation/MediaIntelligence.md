# Media Intelligence

Group detected faces in image collections and find representative moments in videos.

**Platforms:** iOS 27.0+ | iPadOS 27.0+ | Mac Catalyst 27.0+ | macOS 27.0+ | tvOS 27.0+ | visionOS 27.0+

## Overview

Media Intelligence provides on-device image and video analysis. It can maintain groups of matching faces across an image collection, identify video highlights, and select a representative keyframe. These are media-analysis tasks, distinct from [Visual Intelligence](VisualIntelligence.md) system search or [Foundation Models](FoundationModels.md) conversational image input.

The documented face and video analysis runs on device. Your app still needs legitimate access to the source media; local processing does not bypass Photos, file, or capture authorization.

## Topics

### Face grouping

- [`FaceGroupAnalyzer`](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer.md) — Initialize with a writable working directory whose contents the framework manages.
- [`MediaIntelligenceImageAsset`](https://developer.apple.com/documentation/mediaintelligence/mediaintelligenceimageasset.md) — Supply identifiable images for analysis.
- [Detecting and grouping faces](https://developer.apple.com/documentation/mediaintelligence/detecting-and-grouping-faces-in-images.md) — Insert or update assets, run grouping with `update(subprogress:)`, and retrieve results by asset, face, or entity.

Inserted faces initially have no group `entityID`. Grouping assigns it. Check the analyzer's `ready`, `stale`, or `updating` state; if the app exits during grouping, the next launch can resume from retained data by updating again. Remove deleted source assets through the analyzer API rather than editing its working directory.

### Video highlights and keyframes

- [`VideoAnalyzer`](https://developer.apple.com/documentation/mediaintelligence/videoanalyzer.md) — Use `shared.analyze(_:for:)` with an asset and one or more requests.
- [`MediaIntelligenceVideoAsset`](https://developer.apple.com/documentation/mediaintelligence/mediaintelligencevideoasset.md) — Represent the video to analyze.
- [`HighlightAnalysisRequest`](https://developer.apple.com/documentation/mediaintelligence/highlightanalysisrequest.md) — Find candidate highlight segments.
- [`KeyFrameAnalysisRequest`](https://developer.apple.com/documentation/mediaintelligence/keyframeanalysisrequest.md) — Select a representative frame.
- [Finding the best moments in a video](https://developer.apple.com/documentation/mediaintelligence/finding-the-best-moments-in-a-video.md) — Combine requests to share decoding work and inspect each request's result independently.

The documented analyzer serializes queued video analyses without imposing a maximum queue depth or timeout. Bound submissions in your app, cancel work that is no longer needed, and allow time for cooperative cancellation to finish.

### Errors and validation

Handle [`MediaIntelligenceError`](https://developer.apple.com/documentation/mediaintelligence/mediaintelligenceerror.md), missing media, and per-request failures. Keep manual browsing and thumbnail selection available when analysis is unavailable or inconclusive. Face groups are analysis results, not verified real-world identities.

Use [Swift Testing](Testing.md) for state and result handling, [XCTest](XCTest.md) for performance regressions, and representative user-authorized fixtures for grouping and highlight quality. Test asset deletion, interrupted grouping, queue pressure, cancellation, and denied library access.

*Source: [Media Intelligence](https://developer.apple.com/documentation/mediaintelligence.md).*
