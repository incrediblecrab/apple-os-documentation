# Music Understanding

Analyze musical structure and time-varying properties of audio.

**Framework platforms:** iOS 27.0+ | iPadOS 27.0+ | Mac Catalyst 27.0+ | macOS 27.0+ | tvOS 27.0+ | visionOS 27.0+ | watchOS 27.0+

## Overview

Music Understanding analyzes an audio asset or a stream of audio buffers. It reports rhythm, key, loudness, pace, structure, and instrument activity. Use these measurements to drive features such as beat-aligned visuals or navigation through a track.

The API analyzes content; it does not identify a commercial recording, obtain playback rights, or replace [MusicKit](MusicKit.md), [ShazamKit](ShazamKit.md), or [Media Intents](MediaIntents.md).

## Topics

### Session lifecycle

- [`MusicUnderstandingSession`](https://developer.apple.com/documentation/musicunderstanding/musicunderstandingsession.md) — An actor that coordinates an analysis.
- [`init(asset:)`](https://developer.apple.com/documentation/musicunderstanding/musicunderstandingsession/init(asset:).md) — Asynchronously initialize with a `Sendable` `AVAsset` containing audio. The asset must represent local media or a complete file; HTTP livestreams (HLS) are unsupported.
- [`init(audioProvider:)`](https://developer.apple.com/documentation/musicunderstanding/musicunderstandingsession/init(audioprovider:).md) — Supply a nonthrowing asynchronous sequence of `AVReadOnlyAudioPCMBuffer` values (`Failure == Never`). Handle upstream audio-pipeline errors before supplying buffers.
- [`analyze(for:)`](https://developer.apple.com/documentation/musicunderstanding/musicunderstandingsession/analyze(for:).md) — Request a nonempty `Set` of [`AnalysisType`](https://developer.apple.com/documentation/musicunderstanding/analysistype.md) values; `analyze()` requests all available analyses.
- [`cancel()`](https://developer.apple.com/documentation/musicunderstanding/musicunderstandingsession/cancel().md) — Cancel an ongoing analysis when the track or view changes.

Use a session for one analysis run. Requesting analysis while it is already running throws; create a new session for another run or after cancellation. A canceled session cannot be reused.

### Results

- [`SessionResult`](https://developer.apple.com/documentation/musicunderstanding/musicunderstandingsession/sessionresult.md) — Aggregate the requested analysis results.
- [`RhythmResult`](https://developer.apple.com/documentation/musicunderstanding/rhythmresult.md) — Beat positions, bar boundaries, and tempo.
- [`KeyResult`](https://developer.apple.com/documentation/musicunderstanding/keyresult.md) — Musical key over time ranges.
- [`LoudnessResult`](https://developer.apple.com/documentation/musicunderstanding/loudnessresult.md) — Integrated, short-term, momentary, and peak measurements.
- [`PaceResult`](https://developer.apple.com/documentation/musicunderstanding/paceresult.md) — Perceptual pace independent of fixed tempo.
- [`StructureResult`](https://developer.apple.com/documentation/musicunderstanding/structureresult.md) and [`InstrumentActivityResult`](https://developer.apple.com/documentation/musicunderstanding/instrumentactivityresult.md) — Structural boundaries and instrument activity.
- [`loudnessResults`](https://developer.apple.com/documentation/musicunderstanding/musicunderstandingsession/loudnessresults.md) — Consume incremental loudness results; not every analysis promises incremental output.

## Integration and validation

Choose only the analyses your feature needs, keep their timestamps aligned with playback, and discard obsolete results when the source changes. Handle [`MusicUnderstandingError`](https://developer.apple.com/documentation/musicunderstanding/musicunderstandingerror.md) and preserve playback if analysis fails.

Test silence, short or incomplete audio, live-stream completion, cancellation, and tempo changes. Compare against reviewed fixtures using tolerances appropriate to each measurement, with [Swift Testing](Testing.md) and [XCTest](XCTest.md). See Apple's [visualization sample](https://developer.apple.com/documentation/musicunderstanding/create-visuals-using-musicunderstanding-analysis-results.md).

**Availability:** The session's [versioned DocC metadata](https://developer.apple.com/tutorials/data/documentation/musicunderstanding/musicunderstandingsession.json) explicitly includes Mac Catalyst 27.0+. The unversioned Catalyst entry in the Markdown export is not evidence of a missing SDK minimum.

*Sources: [Music Understanding](https://developer.apple.com/documentation/musicunderstanding.md), [MusicUnderstandingSession](https://developer.apple.com/documentation/musicunderstanding/musicunderstandingsession.md).*
