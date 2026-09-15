# XCTest

Write unit, UI, asynchronous, and performance tests for an Xcode project.

**Tools:** Xcode 5.0+; individual APIs and test destinations have separate availability.

## Overview

XCTest provides test cases, assertions, lifecycle hooks, expectations, and performance measurements. Use it with [XCUIAutomation](XCUIAutomation.md) to launch an app and validate user interactions. It remains the documented choice for UI and performance tests.

For new Swift unit tests, consider [Swift Testing](Testing.md), included in Xcode 16 and later. A target may contain both frameworks' tests, but do not mix their APIs inside the same test.

## Topics

### Test cases and assertions

- [`XCTestCase`](https://developer.apple.com/documentation/xctest/xctestcase.md) — Define test methods and setup/teardown behavior.
- [Defining test cases and test methods](https://developer.apple.com/documentation/xctest/defining-test-cases-and-test-methods.md) — Organize a test target and its assertions.
- [Equality assertions](https://developer.apple.com/documentation/xctest/equality-and-inequality-assertions.md) and [error assertions](https://developer.apple.com/documentation/xctest/error-assertions.md) — Check deterministic results and expected failures.
- [Skipping tests](https://developer.apple.com/documentation/xctest/methods-for-skipping-tests.md) and [expected failures](https://developer.apple.com/documentation/xctest/expected-failures.md) — Record unsupported environments or tracked failures without disguising regressions.

### Async, UI, and integration testing

- [Asynchronous tests and expectations](https://developer.apple.com/documentation/xctest/asynchronous-tests-and-expectations.md) — Test asynchronous work, including completion-handler APIs.
- [XCUIAutomation](XCUIAutomation.md) — Query elements, interact with controls, and capture screenshots.
- [App Intents Testing](AppIntentsTesting.md) — Add out-of-process intent and entity checks to a UI testing bundle on supported OS 27 destinations.
- [Activities and attachments](https://developer.apple.com/documentation/xctest/activities-and-attachments.md) — Keep diagnostics with the failed step.

### Performance

- [Performance tests](https://developer.apple.com/documentation/xctest/performance-tests.md) — Compare measurements against a baseline under consistent conditions.
- [Xcode profiling](Xcode.md#profiling) — Use Instruments to explain a regression; a passing microbenchmark does not establish whole-app responsiveness.

## Xcode 27 behavior

The [Xcode 27 release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes.md) add test-plan control over target-app crash severity during UI testing and over Swift Testing/XCTest interoperability warnings. Keep crash handling intentional, and continue to separate assertion frameworks.

Compare results using the same selected toolchain, runtime, device, build configuration, and test data. Record an unavailable test destination as unavailable, not as a successful run.

*Source: [XCTest](https://developer.apple.com/documentation/xctest.md).*
