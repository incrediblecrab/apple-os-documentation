# Migrate one asynchronous feature to Swift 6 checking

Move a data-loading feature and its shared cache to checked isolation without unnecessarily raising the app's deployment target.

## Prerequisites and availability

- Use a reproducible toolchain and a passing test baseline. Xcode 27 (`27A266a`) shipped September 14, 2026, includes the Swift 6.4 compiler, and **requires an Apple silicon Mac running macOS Tahoe 26.6 or later**.
- Record the compiler version, target **Swift language mode**, Strict Concurrency Checking setting, default actor isolation, SDK, and deployment target. They are separate settings.
- The Swift 6 language mode is an opt-in compiler setting, not an OS 27 runtime requirement. Keep the deployment requirements of the APIs your feature actually calls.
- This recipe uses established `actor`, `Sendable`, `@MainActor`, and asynchronous-call semantics. It does not require a speculative Swift 6.4 feature. See [Swift](../documentation/Swift.md) and [Apple's adoption guide](https://developer.apple.com/documentation/swift/adoptingswift6.md).

## 1. Enable diagnostics before changing behavior

Select one app module or feature with useful tests. In its Swift 5 language mode, change **Strict Concurrency Checking** to **Complete**. Build and group diagnostics by shared state, actor-isolated access, and values crossing isolation boundaries.

Fix ownership at the source instead of adding suppression to every caller. Keep the same compiler while comparing modes so compiler changes aren't confused with migration changes. Do not upgrade every dependency or raise every platform minimum merely to enable checking.

## 2. Give shared state an owner

Keep UI state on `@MainActor`. Put independently shared mutable state behind an actor, or pass immutable `Sendable` values instead of sharing a mutable object. For example, this cache owns its dictionary and returns a value snapshot:

```swift
struct SearchEntry: Sendable {
    let title: String
}

actor SearchCache {
    private var entries: [String: SearchEntry] = [:]

    func store(_ entry: SearchEntry, for key: String) {
        entries[key] = entry
    }

    func entry(for key: String) -> SearchEntry? {
        entries[key]
    }
}
```

Call actor-isolated methods with `await` from outside the actor. Do not pass a mutable, non-Sendable reference into the cache and assume the actor also protects accesses made elsewhere.

An `await` can suspend execution. Recheck assumptions after a suspension rather than treating a sequence of asynchronous calls as one atomic transaction.

## 3. Preserve task lifetime and failure behavior

- Prefer child tasks or task groups when work belongs to the caller's lifetime.
- If the UI owns an unstructured `Task`, retain its handle, cancel it when obsolete, and observe its result. The Swift 6.4 changelog adds warnings for implicitly unused throwing tasks.
- Use [`Task.checkCancellation()`](https://developer.apple.com/documentation/swift/task/checkcancellation().md) at appropriate boundaries and handle `CancellationError` as cancellation, not success or a reason to retry forever.
- Keep completion-handler adapters single-completion and test all error paths. A [`CheckedContinuation`](https://developer.apple.com/documentation/swift/checkedcontinuation.md) must be resumed exactly once on every execution path. Never block the cooperative executor with a semaphore while waiting for asynchronous work.
- Return UI updates to the Main Actor. `async` alone does not mean “run expensive work off the main actor.”

Do not use `@unchecked Sendable`, unsafe isolation escapes, or broad warning suppression as substitutes for establishing ownership.

## 4. Switch the selected target to Swift 6 language mode

In **Swift Compiler – Language > Swift Language Version**, select Swift 6 and rebuild. Address diagnostics in the changed module and its public interfaces. Migrate remaining modules incrementally.

If a dependency blocks migration, keep a narrow, tested interface to it and document the outstanding work. A temporary return to Swift 5 mode is an incremental migration option; it is not evidence that shared-state races have been fixed.

### What is actually new in the 6.4 compiler?

The [canonical Swift reference](../documentation/Swift.md) tracks the reviewed `release/6.4.x` changes:

- Async `defer` allows asynchronous cleanup; keep cleanup bounded and account for suspension.
- Task cancellation shields suppress cancellation observation in a scope; they are not locks, transactions, or permission to ignore cancellation indefinitely. Check the selected SDK's runtime declaration before adopting a new runtime API.
- `~Sendable` explicitly suppresses inferred conformance; it does not make a type safe to transfer.
- `@diagnose` changes existing **warning-group** behavior, not arbitrary diagnostics or Swift 6's correctness requirements.
- `anyAppleOS` is shorthand for OS versions **26.0+**; platform-specific availability overrides still take precedence.

`weak let` was implemented in **Swift 6.3**, not 6.4. Accepted future proposals are not part of this recipe unless the release changelog establishes implementation.

## 5. Validate the migration

1. Add deterministic [Swift Testing](../documentation/Testing.md) cases for concurrent cache reads/writes, stale requests, cancellation, failed loads, and UI handoff. Test invariants rather than scheduler ordering.
2. Run the feature's existing [XCTest](../documentation/XCTest.md) tests too. Do not mix Swift Testing and XCTest assertions inside one test.
3. For a Swift package with a `SearchCacheTests` suite, run `swift test --filter SearchCacheTests`. With the verified 6.4 toolchain, bounded repetition is available through [SwiftPM](../documentation/swift-packages.md); retain any initial failure.
4. Test the oldest supported runtime as well as OS 27. Compiler acceptance is not a substitute for deployment testing.
5. Profile the feature with **Swift Concurrency plus Time Profiler or CPU Profiler**. Xcode 27's Profile detail and Swift Executors instrument help separate running work from queued or suspended tasks. Older runtimes may show unknown executor names.

The outcome is a passing, checked module with explicit ownership and tested cancellation—not simply a changed language-version setting. Record any remaining source-compatibility limitations from [Xcode's release notes](../documentation/Xcode-Release-Notes.md).

## Sources

- [Adopting strict concurrency in Swift 6 apps](https://developer.apple.com/documentation/swift/adoptingswift6.md)
- [Swift language guide: Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/) ([DocC source](https://docs.swift.org/swift-book/data/documentation/the-swift-programming-language/concurrency.json))
- [Swift 6.4 branch changelog](https://raw.githubusercontent.com/swiftlang/swift/release/6.4.x/CHANGELOG.md)
- [SE-0481: weak let, implemented in Swift 6.3](https://raw.githubusercontent.com/swiftlang/swift-evolution/main/proposals/0481-weak-let.md)
- [Xcode 27 release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes.md)
