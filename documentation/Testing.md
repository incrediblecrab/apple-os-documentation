# Swift Testing

Create and run tests for your Swift packages and Xcode projects.

**Platforms:** Swift 6.0+ | Xcode 16.0+

## Overview

With **Swift Testing** you leverage powerful and expressive capabilities of the Swift programming language to develop tests with more confidence and less code. The library integrates seamlessly with Swift Package Manager testing workflow, supports flexible test organization, customizable metadata, and scalable test execution.

### Key Features

- Define test functions almost anywhere with a single attribute
- Group related tests into hierarchies using Swift's type system  
- Integrate seamlessly with Swift concurrency
- Parameterize test functions across wide ranges of inputs
- Enable tests dynamically depending on runtime conditions
- Parallelize tests in-process
- Categorize tests using tags
- Associate bugs directly with the tests that verify their fixes or reproduce their problems

### Related Videos

- Meet Swift Testing
- Go further with Swift Testing

## What's New in OS 27

> **Xcode 27, Swift 6.4:** Two testing surfaces are added alongside Swift Testing.

**App Intents Testing**

Validates your Siri, Shortcuts, and Spotlight integration by exercising real system pathways rather than driving the UI. Because [SiriKit is deprecated](SiriKit.md) and App Intents is now the primary assistant integration point, this is the mechanism for catching integration regressions before shipping.

**Evaluations**

Model-backed features produce non-deterministic output, which unit tests express poorly. The [Evaluations](Evaluations.md) framework is designed for validating AI feature behavior against expectations rather than exact strings.

**Toolchain note**

Both require Xcode 27, which requires macOS 27 Golden Gate on Apple silicon.

## Topics

### Essentials
- [Defining test functions](https://developer.apple.com/documentation/testing/defining_test_functions) - Define a test function to validate that code is working correctly.
- [Organizing test functions with suite types](https://developer.apple.com/documentation/testing/organizing_test_functions_with_suite_types) - Organize tests into test suites.
- [Migrating a test from XCTest](https://developer.apple.com/documentation/testing/migrating_a_test_from_xctest) - Migrate an existing test method or test class written using XCTest.
- **Test** - Declare a test.
- **Test** - A type representing a test or suite.
- **Suite** - Declare a test suite.

### Test Parameterization
- [Implementing parameterized tests](https://developer.apple.com/documentation/testing/implementing_parameterized_tests) - Specify different input parameters to generate multiple test cases from a test function.
- **Test** - Declare a test parameterized over a collection of values.
- **Test** - Declare a test parameterized over two collections of values.
- **Test** - Declare a test parameterized over two zipped collections of values.
- **CustomTestArgumentEncodable** - A protocol for customizing how arguments passed to parameterized tests are encoded, which is used to match against when running specific arguments.
- **Case** - A single test case from a parameterized Test.

### Behavior Validation
- [Expectations and confirmations](https://developer.apple.com/documentation/testing/expectations_and_confirmations) - Check for expected values, outcomes, and asynchronous events in tests.
- [Known issues](https://developer.apple.com/documentation/testing/known_issues) - Mark issues as known when running tests.

### Test Customization
- [Traits](https://developer.apple.com/documentation/testing/traits) - Annotate test functions and suites, and customize their behavior.

### Data Collection
- [Attachments](https://developer.apple.com/documentation/testing/attachments) - Attach values to tests to help diagnose issues and gather feedback.

---

*SDK baseline: Apple OS 27 generation — iOS 27, iPadOS 27, macOS Golden Gate 27, tvOS 27, watchOS 27, visionOS 27 (developer beta as of August 2026; expected September 2026). Current shipping line: OS 26.6. Build with Xcode 27 and Swift 6.4. Reviewed 2026-08-09.*

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Testing)*
