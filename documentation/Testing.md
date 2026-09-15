# Swift Testing

Create and run tests for your Swift packages and Xcode projects.

**Tools:** Swift 6.0+ | Xcode 16.0+

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

## Xcode 27 testing changes

The [Xcode 27 release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes.md) document individually identifiable parameterized-test links and improved handling of large parameterized suites. SwiftPM adds repeat-until-pass/fail execution; see [Swift packages](swift-packages.md).

Choose a test surface according to the behavior under test:

- **Swift Testing:** Keep deterministic unit tests, including error, cancellation, and concurrency cases. The framework's introduction in Swift 6/Xcode 16 is unchanged.
- **[XCTest](XCTest.md) and [XCUIAutomation](XCUIAutomation.md):** Continue to use these for UI tests, and XCTest for performance tests. Both unit-test frameworks can coexist in one target, but do not mix their assertion APIs within one test.
- **[App Intents Testing](AppIntentsTesting.md):** Run out-of-process intent, query, Spotlight, and view-annotation tests in an XCTest UI testing bundle. This is not a replacement for all UI tests.
- **[Evaluations](Evaluations.md):** Define datasets and metrics, attach `EvaluationTrait` with `@Test(.evaluates(...))`, and inspect `EvaluationContext.current.result`. Model-quality measurement supplements unit tests.

Xcode 27 reports a warning when an assertion from one test framework fails inside a test from the other framework; the test-plan **Swift Testing and XCTest Interoperability** setting controls this behavior. It does not make mixing frameworks in a test recommended. Xcode 27 requires **Apple silicon and macOS Tahoe 26.6+**; the macOS 27 SDK supports back deploying Universal apps to macOS 12 and later, and Intel development remains possible with Rosetta-supporting macOS such as macOS 27. The new App Intents Testing and Evaluations APIs have their own OS 27 availability.

## Topics

### Essentials
- [Defining test functions](https://developer.apple.com/documentation/testing/definingtests.md) - Define a test function to validate that code is working correctly.
- [Organizing test functions with suite types](https://developer.apple.com/documentation/testing/organizingtests.md) - Organize tests into test suites.
- [Migrating a test from XCTest](https://developer.apple.com/documentation/testing/migratingfromxctest.md) - Migrate an existing test method or test class written using XCTest.
- **@Test** - Declare a test with a macro.
- **Test** - A type representing a test or suite.
- **@Suite** - Declare a test suite with a macro.

### Test Parameterization
- [Implementing parameterized tests](https://developer.apple.com/documentation/testing/parameterizedtesting.md) - Specify different input parameters to generate multiple test cases from a test function.
- **@Test** - Declare a test parameterized over a collection of values.
- **@Test** - Declare a test parameterized over two collections of values.
- **@Test** - Declare a test parameterized over two zipped collections of values.
- **CustomTestArgumentEncodable** - A protocol for customizing how arguments passed to parameterized tests are encoded, which is used to match against when running specific arguments.
- **Test.Case** - A single test case from a parameterized test.

### Behavior Validation
- [Expectations and confirmations](https://developer.apple.com/documentation/testing/expectations.md) - Check for expected values, outcomes, and asynchronous events in tests.
- [Known issues](https://developer.apple.com/documentation/testing/known-issues.md) - Mark issues as known when running tests.

### Test Customization
- [Traits](https://developer.apple.com/documentation/testing/traits) - Annotate test functions and suites, and customize their behavior.

### Data Collection
- [Attachments](https://developer.apple.com/documentation/testing/attachments) - Attach values to tests to help diagnose issues and gather feedback.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/Testing)*
